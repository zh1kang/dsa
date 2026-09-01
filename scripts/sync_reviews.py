"""Import explicit review grades from the Google Sheets Review Input queue."""
from __future__ import annotations

import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fsrs_scheduler
import git_utils
import google_sheets
import record_review
import tracker
import update_review_schedule
from config import Config, load_config

REVIEW_ID_RE = re.compile(r"RI-[0-9a-f]{12}")


def _optional_float(value: str, label: str) -> float | None:
    if not value:
        return None
    try:
        number = float(value)
    except ValueError as exc:
        raise tracker.DataError(f"{label} must be a number") from exc
    if not math.isfinite(number) or number <= 0:
        raise tracker.DataError(f"{label} must be positive")
    return number


def _optional_int(value: str, label: str) -> int | None:
    if not value:
        return None
    try:
        number = float(value)
    except ValueError as exc:
        raise tracker.DataError(f"{label} must be a whole number") from exc
    if not math.isfinite(number) or not number.is_integer() or number < 0:
        raise tracker.DataError(f"{label} must be a non-negative whole number")
    return int(number)


def _build_sheet_event(
    tracker_data: dict[str, Any], review_input: dict[str, str | int]
) -> dict[str, Any]:
    row_number = int(review_input["row_number"])
    context = f"Review Input row {row_number}"
    review_id = str(review_input["review_id"])
    if not REVIEW_ID_RE.fullmatch(review_id):
        raise tracker.DataError(f"{context} has an invalid managed Review ID")
    identifier = str(review_input["problem"])
    if not identifier:
        raise tracker.DataError(f"{context} needs a problem number or ID")
    grade = str(review_input["grade"])
    if not grade:
        raise tracker.DataError(f"{context} needs a grade")
    reviewed_at = tracker.validate_timestamp(
        str(review_input["reviewed_at"]), f"{context} Reviewed At"
    )
    event = record_review.build_event(
        record_review.resolve_problem(tracker_data, identifier),
        grade,
        reviewed_at,
        _optional_float(str(review_input["minutes"]), f"{context} Minutes"),
        _optional_int(str(review_input["hints"]), f"{context} Hints"),
        str(review_input["notes"]) or None,
        str(review_input["failure_stage"]) or None,
    )
    event["source"] = "google_sheets"
    event["source_id"] = review_id
    return event


def _collect_events(
    tracker_data: dict[str, Any],
    events: list[dict[str, Any]],
    review_inputs: list[dict[str, str | int]],
    now: datetime,
) -> tuple[list[dict[str, Any]], list[tuple[int, str, str]], list[tuple[int, str]]]:
    accepted = {
        key for key, problem in tracker_data["problems"].items()
        if problem.get("last_solved_at")
    }
    known_ids = {
        str(event["source_id"])
        for event in events
        if event.get("source") == "google_sheets" and event.get("source_id")
    }
    batch_ids: set[str] = set()
    new_events: list[dict[str, Any]] = []
    outcomes: list[tuple[int, str, str]] = []
    pending: list[tuple[int, str]] = []
    for review_input in review_inputs:
        row_number = int(review_input["row_number"])
        review_id = str(review_input["review_id"])
        if review_id in known_ids:
            outcomes.append((row_number, "Processed", "Already imported"))
            continue
        if review_id in batch_ids:
            outcomes.append((row_number, "Error", "Duplicate Review ID"))
            continue
        batch_ids.add(review_id)
        try:
            event = _build_sheet_event(tracker_data, review_input)
            if tracker.validate_timestamp(event["reviewed_at"], "reviewed_at") > now:
                raise tracker.DataError(
                    f"Review Input row {row_number} Reviewed At cannot be in the future"
                )
            fsrs_scheduler.validate_review_log(
                events + new_events + [event], accepted
            )
        except (tracker.DataError, ValueError) as exc:
            outcomes.append((row_number, "Error", str(exc)))
            continue
        new_events.append(event)
        pending.append((row_number, event["problem"]))
    return new_events, outcomes, pending


def run_sync(config: Config) -> int:
    root = config.root
    in_repo = git_utils.is_repo(root)
    if in_repo:
        git_utils.ensure_clean(root)
        if config.auto_push and git_utils.has_upstream(root):
            git_utils.pull_ff_only(root)

    now = datetime.now(timezone.utc)
    tracker_data = tracker.load_tracker(root / "tracker.json")
    events = tracker.load_json(root / "review-log.json", list)
    review_inputs = google_sheets.claim_review_inputs(config, now)
    if not review_inputs:
        print("no pending review inputs")
        return 0

    new_events, outcomes, pending = _collect_events(
        tracker_data, events, review_inputs, now
    )
    schedule: dict[str, Any] | None = None
    failed = False
    if new_events:
        updated_events = events + new_events
        tracker.atomic_json_write(root / "review-log.json", updated_events)
        schedule, _, _ = update_review_schedule.regenerate(config, now)
        if in_repo:
            git_utils.stage(root, record_review.GENERATED_PATHS)
            if git_utils.has_staged_changes(root):
                git_utils.commit(
                    root, f"leetcode: import {len(new_events)} sheet reviews"
                )
                if config.auto_push:
                    if not git_utils.has_upstream(root):
                        print(
                            "error: auto-push is enabled but this branch has no upstream; "
                            "local commit kept",
                            file=sys.stderr,
                        )
                        failed = True
                    else:
                        try:
                            git_utils.push(root)
                        except git_utils.GitError as exc:
                            print(
                                f"error: push failed; the local commit is kept: {exc}",
                                file=sys.stderr,
                            )
                            failed = True
        google_sheets.push_tracker(
            config,
            tracker.load_tracker(root / "tracker.json"),
            updated_events,
        )
        next_reviews = {
            entry["problem_id"]: entry["next_review"]
            for entry in schedule["problems"]
        }
        outcomes.extend(
            (
                row_number,
                "Processed",
                f"Next review: {next_reviews.get(problem, 'not scheduled')}",
            )
            for row_number, problem in pending
        )

    google_sheets.mark_review_inputs(config, outcomes)
    errors = sum(status == "Error" for _, status, _ in outcomes)
    print(f"imported {len(new_events)} review inputs; {errors} errors")
    return 1 if failed else 0


def main() -> int:
    try:
        return run_sync(load_config())
    except (git_utils.GitError, tracker.DataError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
