"""Build local CSV exports and mirror tracker data into a Sheets template.

The CSV files retain the compact r-chong/dsa-compatible contracts. The live
spreadsheet uses Problems, Submissions, and Reviews tables plus a small
dashboard. Untrusted cells that start with a formula character are prefixed
with an apostrophe before Google Sheets receives them.
"""
from __future__ import annotations

import csv
import os
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

import fsrs_scheduler
from comment_parser import NOTE_FIELDS
from config import Config
from tracker import EMPTY_REVIEW

SHEETS_SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
MAX_CELL_CHARACTERS = 50_000

HEADER = [
    "number", "title", "slug", "url", "difficulty", "tags",
    "submission_id", "submitted_at", "language", "runtime", "memory", "code_path",
    "leetcode_notes", "raw_comments", *NOTE_FIELDS,
    "review_state", "next_review", "last_review",
    "stability", "fsrs_difficulty", "retrievability", "reps", "lapses",
]
REVIEW_HEADER = [
    "reviewed_at", "problem", "result", "failure_stage",
    "elapsed_minutes", "hints", "notes",
]

PROBLEMS_HEADER = [
    "Problem ID", "LC #", "Slug", "Problem", "Difficulty", "Tags",
    "LeetCode URL", "First Solved", "Last Solved", "Latest Submission ID",
    "Latest Language", "Latest Solution Path", "GitHub Solution URL",
    "Attempt Count", "Raw Comments (Latest)", "Thought Process", "Notes",
    "Core Insight", "Pattern", "Mistakes", "Edge Cases", "Time Complexity",
    "Space Complexity", "FSRS State", "Stability (days)", "FSRS Difficulty",
    "Retrievability", "Last Review", "Next Review", "Last Grade", "Reps",
    "Lapses", "Review Status", "Days Until Due", "Last Synced",
]
SUBMISSIONS_HEADER = [
    "Submission ID", "Problem ID", "LC #", "Problem", "Submitted At",
    "Status", "Language", "Runtime", "Memory", "Solution Path",
    "GitHub Solution URL", "Raw Comments", "Thought Process", "Notes",
    "Core Insight", "Pattern", "Mistakes", "Edge Cases", "Time Complexity",
    "Space Complexity", "Is Review Attempt?", "Imported At", "Source",
]
REVIEWS_HEADER = [
    "Review ID", "Reviewed At", "Problem ID", "LC #", "Problem", "Grade",
    "Solved Without Help?", "Hints Used", "Elapsed Minutes", "Review Notes",
    "Failure Stage", "Submission ID", "Stability Before", "Difficulty Before",
    "Retrievability Before", "Stability After", "Difficulty After",
    "Retrievability After", "Next Review", "Logged At",
]
REVIEW_INPUT_WORKSHEET = "Review Input"
REVIEW_INPUT_HEADER = [
    "Review ID", "Problem", "Grade", "Minutes", "Hints", "Notes",
    "Failure Stage", "Reviewed At", "Status", "Message",
]

README_VALUES = [
    {"range": "A1", "values": [["dsa"]]},
    {"range": "A2", "values": [[
        "LeetCode submissions, solution notes, and spaced reviews."
    ]]},
    {"range": "A4", "values": [["Problems tracked"]]},
    {"range": "C4", "values": [["Accepted submissions"]]},
    {"range": "E4", "values": [["Reviews logged"]]},
    {"range": "G4", "values": [["Due / overdue"]]},
    {"range": "A5", "values": [[
        '=COUNTIF(Problems!A2:A1000,"<>")'
    ]]},
    {"range": "C5", "values": [[
        '=COUNTIFS(Submissions!A2:A5000,"<>",Submissions!F2:F5000,"Accepted")'
    ]]},
    {"range": "E5", "values": [[
        '=COUNTIF(Reviews!A2:A5000,"<>")'
    ]]},
    {"range": "G5", "values": [[
        '=COUNTIFS(Problems!AC2:AC1000,"<="&TODAY(),Problems!AC2:AC1000,"<>")'
    ]]},
    {"range": "A7", "values": [["how it works"]]},
    {"range": "A8:B12", "values": [
        ["sync submissions", ".venv/bin/python scripts/sync_leetcode.py"],
        ["sync grades", ".venv/bin/python scripts/sync_reviews.py"],
        ["thoughts", "top comments before the solution code"],
        ["notes", "comments after divergences:"],
        ["reviews", "enter a problem and grade in Review Input"],
    ]},
    {"range": "A13:B13", "values": [[
        "repository", "https://github.com/zh1kang/dsa"
    ]]},
    {"range": "A16", "values": [["tabs"]]},
    {"range": "A17:B21", "values": [
        ["Problems", "current solution and review state"],
        ["Submissions", "complete attempt history"],
        ["Reviews", "explicit review history"],
        ["Review Input", "enter new review grades here"],
        ["Due Today", "problems ready to review"],
    ]},
]

_RESULT_BY_GRADE = {
    "again": "fail",
    "hard": "partial",
    "good": "pass",
    "easy": "pass",
}


def sanitize_cell(value: Any) -> str:
    """Render a cell as text and neutralize leading formula characters."""
    if value is None:
        return ""
    text = value if isinstance(value, str) else str(value)
    if text.startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def _number_sort_key(number: str) -> tuple[int, Any]:
    return (0, int(number)) if str(number).isdigit() else (1, str(number))


def build_rows(tracker_data: dict[str, Any]) -> list[list[str]]:
    """Build header plus one sanitized row per accepted attempt."""
    rows: list[list[str]] = [list(HEADER)]
    problems = sorted(
        tracker_data["problems"].items(),
        key=lambda item: (_number_sort_key(item[1]["leetcode_id"]), item[0]),
    )
    for key, problem in problems:
        review = problem.get("review") or dict(EMPTY_REVIEW)
        for attempt in problem["attempts"]:
            if attempt["status"].casefold() != "accepted":
                continue
            notes = attempt.get("notes", {})
            raw = [
                problem["leetcode_id"], problem["title"], problem["slug"],
                problem["leetcode_url"], problem["difficulty"],
                ", ".join(problem["tags"]),
                attempt["submission_id"], attempt["submitted_at"],
                attempt["language"], attempt.get("runtime"),
                attempt.get("memory"), attempt["code_path"],
                attempt.get("leetcode_notes"),
                "\n".join(attempt.get("raw_comments", [])),
                *[notes.get(field, "") for field in NOTE_FIELDS],
                review.get("state"), review.get("next_review"),
                review.get("last_review"), review.get("stability"),
                review.get("difficulty"), review.get("retrievability"),
                review.get("reps"), review.get("lapses"),
            ]
            rows.append([sanitize_cell(value) for value in raw])
    return rows


def build_review_rows(
    tracker_data: dict[str, Any], events: list[dict[str, Any]]
) -> list[list[str]]:
    """Build the exact r-chong/dsa mindsolve-log column contract."""
    rows: list[list[str]] = [list(REVIEW_HEADER)]
    for event in events:
        problem = tracker_data["problems"][event["problem"]]
        result = _RESULT_BY_GRADE[event["grade"].casefold()]
        hints = event.get("hints_used")
        if result == "pass" and (hints or 0) > 0:
            result = "partial"
        raw = [
            event["reviewed_at"],
            problem["title"],
            result,
            event.get("failure_stage"),
            event.get("elapsed_minutes"),
            hints,
            event.get("notes"),
        ]
        rows.append([sanitize_cell(value) for value in raw])
    return rows


def _github_solution_url(repository: str, code_path: str) -> str:
    return f"https://github.com/{repository}/blob/main/{code_path}"


def _date_only(value: Any) -> str:
    if not value:
        return ""
    return str(value)[:10]


def _sheet_row(values: list[Any], formula_columns: set[int] | None = None) -> list[str]:
    formulas = formula_columns or set()
    return [
        str(value) if index in formulas else sanitize_cell(value)
        for index, value in enumerate(values)
    ]


def _sorted_problems(tracker_data: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    return sorted(
        tracker_data["problems"].items(),
        key=lambda item: (_number_sort_key(item[1]["leetcode_id"]), item[0]),
    )


def build_problem_rows(
    tracker_data: dict[str, Any],
    events: list[dict[str, Any]],
    repository: str,
    synced_at: datetime | None = None,
) -> list[list[str]]:
    """Build one current-state row per tracked problem."""
    synced_at = synced_at or datetime.now(timezone.utc)
    latest_grade = {
        event["problem"]: event["grade"]
        for event in events
    }
    rows: list[list[str]] = [list(PROBLEMS_HEADER)]
    for row_number, (key, problem) in enumerate(_sorted_problems(tracker_data), start=2):
        attempts = problem.get("attempts", [])
        accepted = [
            attempt for attempt in attempts
            if attempt.get("status", "").casefold() == "accepted"
        ]
        latest = accepted[-1] if accepted else attempts[-1]
        notes = latest.get("notes", {})
        review = problem.get("review") or dict(EMPTY_REVIEW)
        next_review_column = _column_name(PROBLEMS_HEADER.index("Next Review") + 1)
        status_formula = (
            f'=IF({next_review_column}{row_number}="","Unscheduled",'
            f'IF({next_review_column}{row_number}<TODAY(),"Overdue",'
            f'IF({next_review_column}{row_number}=TODAY(),"Due Today","Upcoming")))'
        )
        days_formula = (
            f'=IF({next_review_column}{row_number}="","",'
            f'{next_review_column}{row_number}-TODAY())'
        )
        values = [
            key,
            problem["leetcode_id"],
            problem["slug"],
            problem["title"],
            problem["difficulty"],
            ", ".join(problem["tags"]),
            problem["leetcode_url"],
            problem.get("first_solved_at"),
            problem.get("last_solved_at"),
            latest["submission_id"],
            latest["language"],
            latest["code_path"],
            _github_solution_url(repository, latest["code_path"]),
            len(attempts),
            "\n".join(latest.get("raw_comments", [])),
            notes.get("thought_process"),
            notes.get("notes"),
            notes.get("core_insight"),
            notes.get("pattern"),
            notes.get("mistakes"),
            notes.get("edge_cases"),
            notes.get("time_complexity"),
            notes.get("space_complexity"),
            str(review.get("state") or "new").title(),
            review.get("stability"),
            review.get("difficulty"),
            review.get("retrievability"),
            _date_only(review.get("last_review")),
            _date_only(review.get("next_review")),
            latest_grade.get(key, ""),
            review.get("reps", 0),
            review.get("lapses", 0),
            status_formula,
            days_formula,
            synced_at.isoformat(),
        ]
        rows.append(_sheet_row(values, {32, 33}))
    return rows


def build_submission_rows(
    tracker_data: dict[str, Any], repository: str
) -> list[list[str]]:
    """Build one row per imported submission, newest first."""
    submissions: list[tuple[str, dict[str, Any], dict[str, Any]]] = []
    for key, problem in tracker_data["problems"].items():
        submissions.extend((key, problem, attempt) for attempt in problem["attempts"])
    submissions.sort(
        key=lambda item: (item[2]["submitted_at"], int(item[2]["submission_id"])),
        reverse=True,
    )
    rows: list[list[str]] = [list(SUBMISSIONS_HEADER)]
    for key, problem, attempt in submissions:
        notes = attempt.get("notes", {})
        values = [
            attempt["submission_id"],
            key,
            problem["leetcode_id"],
            problem["title"],
            attempt["submitted_at"],
            attempt["status"],
            attempt["language"],
            attempt.get("runtime"),
            attempt.get("memory"),
            attempt["code_path"],
            _github_solution_url(repository, attempt["code_path"]),
            "\n".join(attempt.get("raw_comments", [])),
            notes.get("thought_process"),
            notes.get("notes"),
            notes.get("core_insight"),
            notes.get("pattern"),
            notes.get("mistakes"),
            notes.get("edge_cases"),
            notes.get("time_complexity"),
            notes.get("space_complexity"),
            "No",
            "",
            "LeetCode",
        ]
        rows.append(_sheet_row(values))
    return rows


def build_review_sheet_rows(
    tracker_data: dict[str, Any], events: list[dict[str, Any]]
) -> list[list[str]]:
    """Build the detailed live review table from append-only review events."""
    indexed_events = list(enumerate(events, start=1))
    indexed_events.sort(key=lambda item: item[1]["reviewed_at"], reverse=True)
    rows: list[list[str]] = [list(REVIEWS_HEADER)]
    for event_number, event in indexed_events:
        key = event["problem"]
        problem = tracker_data["problems"][key]
        accepted = [
            attempt for attempt in problem["attempts"]
            if attempt.get("status", "").casefold() == "accepted"
        ]
        submission_id = accepted[-1]["submission_id"] if accepted else ""
        values = [
            f"R{event_number:04d}",
            event["reviewed_at"],
            key,
            problem["leetcode_id"],
            problem["title"],
            event["grade"],
            "Yes" if event.get("solved_without_help") else "No",
            event.get("hints_used"),
            event.get("elapsed_minutes"),
            event.get("notes"),
            event.get("failure_stage"),
            submission_id,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            event["reviewed_at"],
        ]
        rows.append(_sheet_row(values))
    return rows


def write_csv(path: Path, rows: list[list[str]]) -> None:
    """Write the CSV atomically: temp file in the same directory, then replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            csv.writer(handle, lineterminator="\n").writerows(rows)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _column_name(index: int) -> str:
    name = ""
    while index:
        index, remainder = divmod(index - 1, 26)
        name = chr(65 + remainder) + name
    return name


def validate_sheet_rows(rows: list[list[str]], header: list[str] = HEADER) -> None:
    if not rows or rows[0] != header:
        raise ValueError("sheet rows must begin with the expected header")
    for row_number, row in enumerate(rows, start=1):
        if len(row) != len(header):
            raise ValueError(f"sheet row {row_number} has {len(row)} cells; expected {len(header)}")
        for column, cell in enumerate(row, start=1):
            if len(cell) > MAX_CELL_CHARACTERS:
                raise ValueError(
                    f"sheet cell {_column_name(column)}{row_number} exceeds "
                    f"Google Sheets' {MAX_CELL_CHARACTERS}-character limit"
                )


def _open_spreadsheet(config: Config) -> Any:
    if not config.spreadsheet_id:
        raise ValueError("google_sheets.spreadsheet_id is not configured")
    if not config.google_credentials_file.exists():
        raise FileNotFoundError(
            f"google oauth client secret not found: {config.google_credentials_file}"
        )
    import gspread

    config.google_token_file.parent.mkdir(parents=True, exist_ok=True)
    client = gspread.oauth(
        scopes=SHEETS_SCOPES,
        credentials_filename=str(config.google_credentials_file),
        authorized_user_filename=str(config.google_token_file),
    )
    return client.open_by_key(config.spreadsheet_id)


def ensure_review_input_worksheet(spreadsheet: Any) -> Any:
    """Create and validate the user-owned review input queue."""
    import gspread
    from gspread.utils import ValidationConditionType

    try:
        worksheet = spreadsheet.worksheet(REVIEW_INPUT_WORKSHEET)
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title=REVIEW_INPUT_WORKSHEET,
            rows=1000,
            cols=len(REVIEW_INPUT_HEADER),
        )
    if worksheet.col_count < len(REVIEW_INPUT_HEADER):
        worksheet.resize(cols=len(REVIEW_INPUT_HEADER))
    current_header = worksheet.row_values(1)
    if current_header and current_header[:len(REVIEW_INPUT_HEADER)] != REVIEW_INPUT_HEADER:
        raise ValueError(
            f"{REVIEW_INPUT_WORKSHEET} header does not match the expected schema"
        )
    worksheet.update(
        range_name="A1:J1",
        values=[REVIEW_INPUT_HEADER],
        value_input_option="RAW",
    )
    worksheet.freeze(rows=1)
    worksheet.format("A1:J1", {"textFormat": {"bold": True}})
    worksheet.format("A2:J1000", {
        "verticalAlignment": "TOP",
        "wrapStrategy": "WRAP",
    })
    worksheet.add_validation(
        "C2:C1000",
        ValidationConditionType.one_of_list,
        ["Again", "Hard", "Good", "Easy"],
        inputMessage="How well did you recall the solution?",
        strict=True,
        showCustomUi=True,
    )
    return worksheet


def claim_review_inputs(config: Config, now: datetime) -> list[dict[str, str | int]]:
    """Assign stable IDs and timestamps to unprocessed review input rows."""
    if now.tzinfo is None:
        raise ValueError("review input claim time must be timezone-aware")
    spreadsheet = _open_spreadsheet(config)
    worksheet = ensure_review_input_worksheet(spreadsheet)
    rows = worksheet.get_all_values()
    inputs: list[dict[str, str | int]] = []
    updates: list[dict[str, Any]] = []
    for row_number, row in enumerate(rows[1:], start=2):
        cells = (row + [""] * len(REVIEW_INPUT_HEADER))[:len(REVIEW_INPUT_HEADER)]
        if cells[8].strip().casefold() == "processed":
            continue
        if not any(cell.strip() for cell in cells[1:7]):
            continue
        review_id = cells[0].strip() or f"RI-{uuid4().hex[:12]}"
        reviewed_at = cells[7].strip() or (
            now.astimezone(timezone.utc)
            - timedelta(microseconds=max(1, len(rows) - row_number + 1))
        ).isoformat()
        if not cells[0].strip():
            updates.append({"range": f"A{row_number}", "values": [[review_id]]})
        if not cells[7].strip():
            updates.append({"range": f"H{row_number}", "values": [[reviewed_at]]})
        inputs.append({
            "row_number": row_number,
            "review_id": review_id,
            "problem": cells[1].strip(),
            "grade": cells[2].strip(),
            "minutes": cells[3].strip(),
            "hints": cells[4].strip(),
            "notes": cells[5],
            "failure_stage": cells[6].strip(),
            "reviewed_at": reviewed_at,
        })
    if updates:
        worksheet.batch_update(updates, value_input_option="RAW")
    return inputs


def mark_review_inputs(
    config: Config, outcomes: list[tuple[int, str, str]]
) -> None:
    """Write processing status without changing user-entered review fields."""
    if not outcomes:
        return
    spreadsheet = _open_spreadsheet(config)
    worksheet = ensure_review_input_worksheet(spreadsheet)
    worksheet.batch_update([
        {
            "range": f"I{row_number}:J{row_number}",
            "values": [[status, message]],
        }
        for row_number, status, message in outcomes
    ], value_input_option="RAW")


def _update_worksheet(spreadsheet: Any, title: str, rows: list[list[str]]) -> None:
    """Replace one existing template table without touching other worksheets."""
    header = rows[0]
    worksheet = spreadsheet.worksheet(title)
    old_rows = worksheet.row_count
    if old_rows < len(rows) or worksheet.col_count < len(header):
        worksheet.resize(
            rows=max(old_rows, len(rows)), cols=max(worksheet.col_count, len(header))
        )
    # The replacement is written before stale trailing rows are removed. If the
    # update fails, the previous worksheet remains intact.
    worksheet.update(range_name="A1", values=rows, value_input_option="USER_ENTERED")
    if old_rows > len(rows):
        last_column = _column_name(len(header))
        worksheet.batch_clear([f"A{len(rows) + 1}:{last_column}{old_rows}"])
    worksheet.freeze(rows=1)
    last_column = _column_name(len(header))
    worksheet.format(f"A2:{last_column}{max(len(rows), 2)}", {
        "verticalAlignment": "TOP",
        "wrapStrategy": "WRAP",
    })


def _sheet_metadata(spreadsheet: Any, title: str) -> tuple[int, str | None]:
    metadata = spreadsheet.fetch_sheet_metadata()
    for sheet in metadata["sheets"]:
        if sheet["properties"]["title"] != title:
            continue
        tables = sheet.get("tables", [])
        return sheet["properties"]["sheetId"], (tables[0]["tableId"] if tables else None)
    raise ValueError(f"worksheet metadata not found: {title}")


def _polish_table(
    spreadsheet: Any,
    title: str,
    row_count: int,
    column_count: int,
    widths: list[tuple[int, int, int]],
) -> None:
    sheet_id, table_id = _sheet_metadata(spreadsheet, title)
    requests: list[dict[str, Any]] = []
    if table_id is not None:
        requests.append({
            "updateTable": {
                "table": {
                    "tableId": table_id,
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 0,
                        "endRowIndex": max(row_count, 2),
                        "startColumnIndex": 0,
                        "endColumnIndex": column_count,
                    },
                },
                "fields": "range",
            }
        })
    requests.extend([
        {
            "updateSheetProperties": {
                "properties": {
                    "sheetId": sheet_id,
                    "gridProperties": {"hideGridlines": True},
                },
                "fields": "gridProperties.hideGridlines",
            }
        },
        {
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "ROWS",
                    "startIndex": 0,
                    "endIndex": 1,
                },
                "properties": {"pixelSize": 38},
                "fields": "pixelSize",
            }
        },
        {
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "ROWS",
                    "startIndex": 1,
                    "endIndex": max(row_count, 2),
                },
                "properties": {"pixelSize": 48},
                "fields": "pixelSize",
            }
        },
    ])
    for start, end, width in widths:
        requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": sheet_id,
                    "dimension": "COLUMNS",
                    "startIndex": start,
                    "endIndex": end,
                },
                "properties": {"pixelSize": width},
                "fields": "pixelSize",
            }
        })
    spreadsheet.batch_update({"requests": requests})


def _update_dashboard(spreadsheet: Any, config: Config) -> None:
    readme = spreadsheet.worksheet("README")
    readme.batch_clear(["A1:H25"])
    readme.batch_update(README_VALUES, value_input_option="USER_ENTERED")
    readme.format("A1:H25", {
        "verticalAlignment": "MIDDLE",
        "wrapStrategy": "WRAP",
    })
    readme.format("A8:A13", {"textFormat": {"bold": True}})
    readme.format("A17:A21", {"textFormat": {"bold": True}})

    due = spreadsheet.worksheet("Due Today")
    due_header = [
        "Problem ID", "Problem", "Difficulty", "Pattern", "LeetCode URL",
        "Due Date", "Days Overdue", "Last Grade", "Core Insight", "Notes",
        "Raw Comments", "GitHub Solution URL",
    ]
    due_formula = (
        '=IFERROR(FILTER({Problems!A2:A1000,Problems!D2:D1000,'
        'Problems!E2:E1000,Problems!S2:S1000,Problems!G2:G1000,'
        'Problems!AC2:AC1000,IF(Problems!AC2:AC1000<TODAY(),'
        'TODAY()-Problems!AC2:AC1000,0),Problems!AD2:AD1000,'
        'Problems!R2:R1000,Problems!Q2:Q1000,Problems!O2:O1000,'
        'Problems!M2:M1000},(Problems!AC2:AC1000<>"")*'
        '(Problems!AC2:AC1000<=TODAY())),"No reviews due")'
    )
    due.update(range_name="A1:L1", values=[due_header],
               value_input_option="USER_ENTERED")
    due.batch_clear(["A2:L1000"])
    due.update(range_name="A2", values=[[due_formula]],
               value_input_option="USER_ENTERED")
    due.freeze(rows=1)
    due.format("A2:L1000", {
        "verticalAlignment": "TOP",
        "wrapStrategy": "WRAP",
    })

    settings = spreadsheet.worksheet("Config")
    settings.update(
        range_name="A15:C15",
        values=[[
            "tracking_start_date",
            config.tracking_start_date.isoformat()
            if config.tracking_start_date else "all history",
            "Only activity on or after this local date enters the repetition schedule.",
        ]],
        value_input_option="RAW",
    )


def push_tracker(
    config: Config,
    tracker_data: dict[str, Any],
    events: list[dict[str, Any]],
) -> None:
    """Update the linked template after validating every generated table."""
    events = fsrs_scheduler.events_on_or_after(
        events, config.tracking_start_date, config.timezone
    )
    problem_rows = build_problem_rows(
        tracker_data, events, config.github_repository
    )
    submission_rows = build_submission_rows(
        tracker_data, config.github_repository
    )
    review_rows = build_review_sheet_rows(tracker_data, events)
    validate_sheet_rows(problem_rows, PROBLEMS_HEADER)
    validate_sheet_rows(submission_rows, SUBMISSIONS_HEADER)
    validate_sheet_rows(review_rows, REVIEWS_HEADER)
    spreadsheet = _open_spreadsheet(config)
    ensure_review_input_worksheet(spreadsheet)
    tables = [
        (config.problems_worksheet, problem_rows, [
            (0, 1, 190), (1, 2, 70), (2, 4, 210), (4, 5, 90),
            (5, 7, 220), (7, 9, 145), (9, 11, 135), (11, 13, 250),
            (13, 14, 90), (14, 23, 240), (23, 35, 120),
        ]),
        (config.submissions_worksheet, submission_rows, [
            (0, 2, 180), (2, 3, 70), (3, 4, 230), (4, 5, 155),
            (5, 7, 105), (7, 9, 95), (9, 11, 250), (11, 20, 240),
            (20, 23, 120),
        ]),
        (config.reviews_worksheet, review_rows, [
            (0, 1, 90), (1, 2, 155), (2, 3, 190), (3, 4, 70),
            (4, 5, 230), (5, 9, 115), (9, 11, 220), (11, 20, 125),
        ]),
    ]
    for title, rows, widths in tables:
        _update_worksheet(spreadsheet, title, rows)
        _polish_table(spreadsheet, title, len(rows), len(rows[0]), widths)
    _update_dashboard(spreadsheet, config)
