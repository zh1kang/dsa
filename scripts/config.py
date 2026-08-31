"""Load non-secret tracker configuration."""
from __future__ import annotations

import re
import tomllib
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def _local_path(value: str, root: Path) -> Path:
    path = Path(value).expanduser()
    return (path if path.is_absolute() else root / path).resolve()


@dataclass(frozen=True)
class Config:
    root: Path
    timezone: ZoneInfo
    tracking_start_date: date | None
    browser_profile: Path
    account_file: Path
    request_delay_seconds: float
    desired_retention: float
    auto_push: bool
    spreadsheet_id: str
    problems_worksheet: str
    submissions_worksheet: str
    reviews_worksheet: str
    github_repository: str
    google_credentials_file: Path
    google_token_file: Path


def load_config(path: Path | None = None) -> Config:
    root = (path.parent if path else ROOT).resolve()
    with (path or root / "config.toml").open("rb") as handle:
        raw = tomllib.load(handle)
    retention = float(raw["fsrs"]["desired_retention"])
    delay = float(raw["leetcode"].get("request_delay_seconds", 1.0))
    if not 0 < retention < 1:
        raise ValueError("fsrs.desired_retention must be between 0 and 1")
    if delay < 0.5:
        raise ValueError("leetcode.request_delay_seconds must be at least 0.5")
    start_date_value = str(raw["tracker"].get("tracking_start_date", "")).strip()
    try:
        tracking_start_date = date.fromisoformat(start_date_value) if start_date_value else None
    except ValueError as exc:
        raise ValueError("tracker.tracking_start_date must be YYYY-MM-DD") from exc
    sheets = raw.get("google_sheets", {})
    worksheet_names = {
        "problems_worksheet": str(sheets.get("problems_worksheet", "Problems")).strip(),
        "submissions_worksheet": str(
            sheets.get("submissions_worksheet", "Submissions")
        ).strip(),
        "reviews_worksheet": str(sheets.get("reviews_worksheet", "Reviews")).strip(),
    }
    if not all(worksheet_names.values()):
        raise ValueError("google_sheets worksheet names must not be empty")
    if len(set(worksheet_names.values())) != len(worksheet_names):
        raise ValueError("google_sheets worksheet names must be different")
    github_repository = str(sheets.get("github_repository", "")).strip()
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", github_repository):
        raise ValueError("google_sheets.github_repository must be owner/repository")
    browser_profile = _local_path(raw["leetcode"]["browser_profile"], root)
    account_file = _local_path(
        raw["leetcode"].get("account_file", ".dsa/account.json"), root
    )
    google_credentials_file = _local_path(
        sheets.get("credentials_file", ".dsa/google/client_secret.json"), root
    )
    google_token_file = _local_path(
        sheets.get("token_file", ".dsa/google/token.json"), root
    )
    state_root = (root / ".dsa").resolve()
    for label, local_path in (
        ("leetcode.browser_profile", browser_profile),
        ("leetcode.account_file", account_file),
        ("google_sheets.credentials_file", google_credentials_file),
        ("google_sheets.token_file", google_token_file),
    ):
        if local_path == state_root or state_root not in local_path.parents:
            raise ValueError(f"{label} must be inside {state_root}")
    return Config(
        root=root,
        timezone=ZoneInfo(raw["tracker"]["timezone"]),
        tracking_start_date=tracking_start_date,
        browser_profile=browser_profile,
        account_file=account_file,
        request_delay_seconds=delay,
        desired_retention=retention,
        auto_push=bool(raw["git"].get("auto_push", True)),
        spreadsheet_id=str(sheets.get("spreadsheet_id", "")).strip(),
        problems_worksheet=worksheet_names["problems_worksheet"],
        submissions_worksheet=worksheet_names["submissions_worksheet"],
        reviews_worksheet=worksheet_names["reviews_worksheet"],
        github_repository=github_repository,
        google_credentials_file=google_credentials_file,
        google_token_file=google_token_file,
    )
