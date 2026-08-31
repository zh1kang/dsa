"""Deterministic FSRS-6 replay of explicit review events.

``review-log.json`` is the only source of truth for FSRS state. Accepted
submissions never produce implicit ratings. An accepted problem without an
explicit grade is app-level ``new`` and is due on its latest accepted date.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from fsrs import Card, Rating, Scheduler, State

from tracker import DataError, NOTE_FIELDS, validate_timestamp

GRADES = {
    "Again": Rating.Again,
    "Hard": Rating.Hard,
    "Good": Rating.Good,
    "Easy": Rating.Easy,
}
GRADE_BY_CASEFOLD = {name.casefold(): (name, rating) for name, rating in GRADES.items()}


def deterministic_card_id(key: str) -> int:
    digest = hashlib.sha256(key.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") & 0x7FFF_FFFF_FFFF_FFFF


def build_scheduler(desired_retention: float) -> Scheduler:
    return Scheduler(
        desired_retention=desired_retention,
        learning_steps=(),
        relearning_steps=(),
        enable_fuzzing=False,
    )


def _utc(value: str, label: str) -> datetime:
    return validate_timestamp(value, label).astimezone(timezone.utc)


def validate_review_log(events: Any, known_problems: set[str]) -> list[dict[str, Any]]:
    """Validate the append-only event stream and return it unchanged."""
    if not isinstance(events, list):
        raise DataError("review log must be a JSON list")
    last_seen: dict[str, datetime] = {}
    for index, event in enumerate(events):
        context = f"review event {index}"
        if not isinstance(event, dict):
            raise DataError(f"{context} must be an object")
        key = event.get("problem")
        if key not in known_problems:
            raise DataError(f"{context} references unknown problem {key!r}")
        grade = event.get("grade")
        if not isinstance(grade, str) or grade.casefold() not in GRADE_BY_CASEFOLD:
            raise DataError(f"{context} has invalid grade {grade!r}")
        when = _utc(str(event.get("reviewed_at")), f"{context} reviewed_at")
        previous = last_seen.get(key)
        if previous is not None and when <= previous:
            raise DataError(f"{context} is a duplicate or out of order for {key}")
        last_seen[key] = when
        minutes = event.get("elapsed_minutes")
        if minutes is not None and (
            not isinstance(minutes, (int, float)) or isinstance(minutes, bool) or minutes <= 0
        ):
            raise DataError(f"{context} has invalid elapsed_minutes {minutes!r}")
        hints = event.get("hints_used")
        if hints is not None and (
            not isinstance(hints, int) or isinstance(hints, bool) or hints < 0
        ):
            raise DataError(f"{context} has invalid hints_used {hints!r}")
        if event.get("notes") is not None and not isinstance(event["notes"], str):
            raise DataError(f"{context} has invalid notes")
        if event.get("solved_without_help") is not None and not isinstance(
            event["solved_without_help"], bool
        ):
            raise DataError(f"{context} has invalid solved_without_help")
    return events


def _accepted_attempts(problem: dict[str, Any]) -> list[dict[str, Any]]:
    return [attempt for attempt in problem["attempts"] if attempt["status"].casefold() == "accepted"]


def compute_reviews(
    tracker_data: dict[str, Any],
    events: list[dict[str, Any]],
    desired_retention: float,
    now: datetime,
) -> dict[str, dict[str, Any]]:
    """Replay explicit events per problem and return derived review snapshots."""
    if now.tzinfo is None:
        raise DataError("now must be timezone-aware")
    now = now.astimezone(timezone.utc)
    scheduler = build_scheduler(desired_retention)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for event in events:
        grouped.setdefault(event["problem"], []).append(event)

    reviews: dict[str, dict[str, Any]] = {}
    for key, problem in tracker_data["problems"].items():
        problem_events = grouped.get(key, [])
        if not problem_events:
            accepted = _accepted_attempts(problem)
            if not accepted:
                continue
            due = _utc(problem["last_solved_at"], "last_solved_at")
            reviews[key] = {
                "state": "new",
                "stability": None,
                "difficulty": None,
                "retrievability": None,
                "last_review": None,
                "next_review": due.isoformat(),
                "reps": 0,
                "lapses": 0,
            }
            continue

        first = _utc(problem_events[0]["reviewed_at"], "reviewed_at")
        card = Card(card_id=deterministic_card_id(key), due=first)
        lapses = 0
        for event in problem_events:
            when = _utc(event["reviewed_at"], "reviewed_at")
            _, rating = GRADE_BY_CASEFOLD[event["grade"].casefold()]
            if card.state == State.Review and rating == Rating.Again:
                lapses += 1
            card, _ = scheduler.review_card(card, rating, review_datetime=when)
        reviews[key] = {
            "state": card.state.name.lower(),
            "stability": card.stability,
            "difficulty": card.difficulty,
            "retrievability": scheduler.get_card_retrievability(card, now),
            "last_review": card.last_review.astimezone(timezone.utc).isoformat(),
            "next_review": card.due.astimezone(timezone.utc).isoformat(),
            "reps": len(problem_events),
            "lapses": lapses,
        }
    return reviews


def _local_date(value: str | None, local_timezone: ZoneInfo) -> str | None:
    return _utc(value, "review timestamp").astimezone(local_timezone).date().isoformat() if value else None


def build_schedule(
    root: Path,
    tracker_data: dict[str, Any],
    events: list[dict[str, Any]],
    reviews: dict[str, dict[str, Any]],
    desired_retention: float,
    now: datetime,
    local_timezone: ZoneInfo,
) -> dict[str, Any]:
    """Build compact reminder data with top-level ISO dates for easy due queries."""
    latest_grades: dict[str, str] = {}
    for event in events:
        latest_grades[event["problem"]] = GRADE_BY_CASEFOLD[event["grade"].casefold()][0]

    entries: list[dict[str, Any]] = []
    for key, review in reviews.items():
        problem = tracker_data["problems"][key]
        accepted = _accepted_attempts(problem)
        latest = accepted[-1] if accepted else None
        if latest and not (root / latest["code_path"]).is_file():
            raise DataError(f"missing stored code: {latest['code_path']}")
        notes = latest.get("notes", {}) if latest else {}
        entry = {
            "problem_id": key,
            "leetcode_id": problem["leetcode_id"],
            "slug": problem["slug"],
            "title": problem["title"],
            "leetcode_url": problem["leetcode_url"],
            "difficulty": problem["difficulty"],
            "tags": problem["tags"],
            "state": review["state"],
            "next_review": _local_date(review["next_review"], local_timezone),
            "next_review_at": review["next_review"],
            "last_review": _local_date(review["last_review"], local_timezone),
            "last_review_at": review["last_review"],
            "last_grade": latest_grades.get(key),
            "stability": review["stability"],
            "fsrs_difficulty": review["difficulty"],
            "retrievability": review["retrievability"],
            "retrievability_as_of": now.astimezone(timezone.utc).isoformat(),
            "reps": review["reps"],
            "lapses": review["lapses"],
            "latest_solution": latest["code_path"] if latest else None,
            "latest_submission_id": latest["submission_id"] if latest else None,
            "raw_comments": latest.get("raw_comments", []) if latest else [],
            "leetcode_notes": latest.get("leetcode_notes") if latest else None,
            **{field: notes.get(field, "") for field in NOTE_FIELDS},
        }
        entries.append(entry)
    entries.sort(key=lambda entry: (entry["next_review"], entry["problem_id"]))
    return {
        "schema_version": 1,
        "generated_at": now.astimezone(local_timezone).isoformat(),
        "timezone": str(local_timezone),
        "fsrs": {
            "algorithm": "FSRS-6",
            "package": "fsrs",
            "package_version": metadata.version("fsrs"),
            "desired_retention": desired_retention,
            "learning_steps": [],
            "relearning_steps": [],
            "fuzzing": False,
        },
        "problems": entries,
    }
