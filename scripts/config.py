"""Load non-secret tracker configuration."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Config:
    root: Path
    timezone: ZoneInfo
    browser_profile: Path
    account_file: Path
    request_delay_seconds: float
    desired_retention: float
    auto_push: bool
    spreadsheet_id: str
    worksheet: str
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
    sheets = raw.get("google_sheets", {})
    browser_profile = Path(raw["leetcode"]["browser_profile"]).expanduser().resolve()
    account_file = Path(
        raw["leetcode"].get("account_file", "~/.leetcode-tracker/account.json")
    ).expanduser().resolve()
    google_credentials_file = Path(
        sheets.get("credentials_file", "~/.leetcode-tracker/google/client_secret.json")
    ).expanduser().resolve()
    google_token_file = Path(
        sheets.get("token_file", "~/.leetcode-tracker/google/token.json")
    ).expanduser().resolve()
    for label, local_path in (
        ("leetcode.browser_profile", browser_profile),
        ("leetcode.account_file", account_file),
        ("google_sheets.credentials_file", google_credentials_file),
        ("google_sheets.token_file", google_token_file),
    ):
        if local_path == root or root in local_path.parents:
            raise ValueError(f"{label} must be outside the repository")
    return Config(
        root=root,
        timezone=ZoneInfo(raw["tracker"]["timezone"]),
        browser_profile=browser_profile,
        account_file=account_file,
        request_delay_seconds=delay,
        desired_retention=retention,
        auto_push=bool(raw["git"].get("auto_push", True)),
        spreadsheet_id=str(sheets.get("spreadsheet_id", "")).strip(),
        worksheet=str(sheets.get("worksheet", "LeetCode")),
        google_credentials_file=google_credentials_file,
        google_token_file=google_token_file,
    )
