"""Record one explicit review grade as an append-only event.

The identifier may be a problem number, a canonical ID, or a slug.
The event is validated against the full log before the log file is replaced
atomically; prior entries are never edited.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fsrs_scheduler
import git_utils
import google_sheets
import tracker
import update_review_schedule
from config import load_config

GENERATED_PATHS = ["review-log.json", "tracker.json", "review-schedule.json",
                   "google-sheets.csv", "solutions"]


def resolve_problem(tracker_data: dict[str, Any], identifier: str) -> str:
    """Resolve a number, canonical ID, or slug to the canonical problem key."""
    ident = identifier.strip()
    problems = tracker_data["problems"]
    if ident in problems:
        matches = [ident]
    else:
        matches = [key for key, problem in problems.items()
                   if str(problem["leetcode_id"]) == ident or problem["slug"] == ident]
    if not matches:
        raise tracker.DataError(f"no tracked problem matches {identifier!r}")
    if len(matches) > 1:
        raise tracker.DataError(f"identifier {identifier!r} is ambiguous: {', '.join(matches)}")
    key = matches[0]
    if not any(attempt.get("status", "").casefold() == "accepted"
               for attempt in problems[key].get("attempts", [])):
        raise tracker.DataError(f"cannot review {key}: it has no accepted submission")
    return key


def build_event(key: str, rating: str, now: datetime, minutes: float | None,
                hints: int | None, notes: str | None) -> dict[str, Any]:
    grade = fsrs_scheduler.GRADE_BY_CASEFOLD.get(rating.casefold())
    if grade is None:
        raise tracker.DataError(f"invalid grade {rating!r}")
    if now.tzinfo is None:
        raise tracker.DataError("review time must be timezone-aware")
    return {
        "problem": key,
        "grade": grade[0],
        "reviewed_at": now.astimezone(timezone.utc).isoformat(),
        "elapsed_minutes": minutes,
        "hints_used": hints,
        "notes": notes,
        "solved_without_help": rating.casefold() != "again" and (hints or 0) == 0,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="record one review grade")
    parser.add_argument("identifier", help="problem number, canonical id, or slug")
    parser.add_argument("grade", choices=sorted(fsrs_scheduler.GRADE_BY_CASEFOLD))
    parser.add_argument("--minutes", type=float, default=None,
                        help="minutes spent on the review")
    parser.add_argument("--hints", type=int, default=None,
                        help="number of hints used")
    parser.add_argument("--notes", default=None, help="free-form review note")
    parser.add_argument("--no-push", action="store_true",
                        help="commit locally but do not push")
    args = parser.parse_args(argv)
    if args.minutes is not None and args.minutes <= 0:
        parser.error("--minutes must be positive")
    if args.hints is not None and args.hints < 0:
        parser.error("--hints must not be negative")

    config = load_config()
    root = config.root
    in_repo = git_utils.is_repo(root)
    if in_repo:
        git_utils.ensure_clean(root)
        if config.auto_push and not args.no_push and git_utils.has_upstream(root):
            git_utils.pull_ff_only(root)
    tracker_data = tracker.load_tracker(root / "tracker.json")
    key = resolve_problem(tracker_data, args.identifier)
    events = tracker.load_json(root / "review-log.json", list)
    now = datetime.now(timezone.utc)
    event = build_event(key, args.grade, now, args.minutes, args.hints, args.notes)
    accepted = {problem_key for problem_key, problem in tracker_data["problems"].items()
                if problem.get("last_solved_at")}
    fsrs_scheduler.validate_review_log(events + [event], accepted)
    tracker.atomic_json_write(root / "review-log.json", events + [event])
    print(f"recorded review: {key} {event['grade']}")

    schedule, rows = update_review_schedule.regenerate(config, now)
    entry = next(e for e in schedule["problems"] if e["problem_id"] == key)
    print(f"next review for {key}: {entry['next_review']}")

    failed = False
    if in_repo:
        git_utils.stage(root, GENERATED_PATHS)
        if git_utils.has_staged_changes(root):
            git_utils.commit(root, f"leetcode: record review {key} ({args.grade})")
            if config.auto_push and not args.no_push:
                if not git_utils.has_upstream(root):
                    print("error: auto-push is enabled but this branch has no upstream; local commit kept",
                          file=sys.stderr)
                    failed = True
                else:
                    try:
                        git_utils.push(root)
                    except git_utils.GitError as exc:
                        print(f"error: push failed; the local commit is kept: {exc}", file=sys.stderr)
                        failed = True
    if config.spreadsheet_id:
        try:
            google_sheets.push_rows(config, rows)
            print("google sheet updated")
        except Exception as exc:
            print(f"error: Google Sheets update failed: {exc}", file=sys.stderr)
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
