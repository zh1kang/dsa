"""Regenerate derived review state, review-schedule.json, and google-sheets.csv.

The review log is the source of truth. This command is idempotent for a fixed
log and tracker; only generated_at and retrievability depend on the clock.
"""
from __future__ import annotations

import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fsrs_scheduler
import comment_parser
import google_sheets
import tracker
from config import Config, load_config


def regenerate(
    config: Config, now: datetime | None = None
) -> tuple[dict[str, Any], list[list[str]], list[list[str]]]:
    """Rebuild review state, schedule, and both sheet exports."""
    now = now or datetime.now(timezone.utc)
    root = config.root
    tracker_data = tracker.load_tracker(root / "tracker.json")
    events = tracker.load_json(root / "review-log.json", list)
    for problem in tracker_data["problems"].values():
        for attempt in problem["attempts"]:
            attempt["notes"] = comment_parser.parse_structured_notes(
                attempt.get("raw_comments", [])
            )
    accepted = {key for key, problem in tracker_data["problems"].items()
                if problem.get("last_solved_at")}
    fsrs_scheduler.validate_review_log(events, accepted)
    active_events = fsrs_scheduler.events_on_or_after(
        events, config.tracking_start_date, config.timezone
    )
    reviews = fsrs_scheduler.compute_reviews(
        tracker_data,
        active_events,
        config.desired_retention,
        now,
        tracking_start_date=config.tracking_start_date,
        local_timezone=config.timezone,
    )
    for key, problem in tracker_data["problems"].items():
        problem["review"] = reviews.get(key, deepcopy(tracker.EMPTY_REVIEW))
    schedule = fsrs_scheduler.build_schedule(
        root, tracker_data, active_events, reviews,
        config.desired_retention, now, config.timezone
    )
    tracker.write_tracker(root, tracker_data)
    tracker.atomic_json_write(root / "review-schedule.json", schedule)
    rows = google_sheets.build_rows(tracker_data)
    review_rows = google_sheets.build_review_rows(tracker_data, active_events)
    google_sheets.write_csv(root / "google-sheets.csv", rows)
    google_sheets.write_csv(root / "mindsolve-log.csv", review_rows)
    return schedule, rows, review_rows


def main(argv: list[str] | None = None) -> int:
    config = load_config()
    now = datetime.now(timezone.utc)
    schedule, _, _ = regenerate(config, now)
    today = now.astimezone(config.timezone).date().isoformat()
    due = sum(1 for entry in schedule["problems"] if entry["next_review"] <= today)
    print(f"schedule updated: {len(schedule['problems'])} problems, {due} due")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
