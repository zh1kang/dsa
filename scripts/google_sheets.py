"""Google Sheets export: always a local CSV, optionally the Sheets API.

One row per accepted attempt. Exact LeetCode notes, raw comments, and every
structured note field get their own columns. Cells that begin with =, +, -,
or @ are prefixed with an apostrophe to block formula injection in both the
CSV and the API path. The API path uses a local Desktop OAuth credential and
token outside the repository with the spreadsheets-only scope. LeetCode
authentication is never involved here.
"""
from __future__ import annotations

import csv
import os
import tempfile
from pathlib import Path
from typing import Any

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


def write_csv(path: Path, rows: list[list[str]]) -> None:
    """Write the CSV atomically: temp file in the same directory, then replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            csv.writer(handle).writerows(rows)
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


def validate_sheet_rows(rows: list[list[str]]) -> None:
    if not rows or rows[0] != HEADER:
        raise ValueError("sheet rows must begin with the expected header")
    for row_number, row in enumerate(rows, start=1):
        if len(row) != len(HEADER):
            raise ValueError(f"sheet row {row_number} has {len(row)} cells; expected {len(HEADER)}")
        for column, cell in enumerate(row, start=1):
            if len(cell) > MAX_CELL_CHARACTERS:
                raise ValueError(
                    f"sheet cell {_column_name(column)}{row_number} exceeds "
                    f"Google Sheets' {MAX_CELL_CHARACTERS}-character limit"
                )


def push_rows(config: Config, rows: list[list[str]]) -> None:
    """Update the worksheet with RAW values without clearing good data first."""
    validate_sheet_rows(rows)
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
    spreadsheet = client.open_by_key(config.spreadsheet_id)
    try:
        worksheet = spreadsheet.worksheet(config.worksheet)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title=config.worksheet, rows=max(len(rows), 1), cols=len(HEADER)
        )
    old_rows = worksheet.row_count
    if old_rows < len(rows) or worksheet.col_count < len(HEADER):
        worksheet.resize(
            rows=max(old_rows, len(rows)), cols=max(worksheet.col_count, len(HEADER))
        )
    # The replacement is written before stale trailing rows are removed. If the
    # update fails, the previous worksheet remains intact.
    worksheet.update(range_name="A1", values=rows, value_input_option="RAW")
    if old_rows > len(rows):
        last_column = _column_name(len(HEADER))
        worksheet.batch_clear([f"A{len(rows) + 1}:{last_column}{old_rows}"])
