"""Validated, atomic storage and append-only attempt merging."""
from __future__ import annotations

import json
import os
import re
import tempfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any

NOTE_FIELDS = ("thought_process", "core_insight", "pattern", "mistakes", "edge_cases", "time_complexity", "space_complexity")
EMPTY_REVIEW = {"state": "new", "stability": None, "difficulty": None, "retrievability": None, "last_review": None, "next_review": None, "reps": 0, "lapses": 0}

class DataError(ValueError):
    pass


def load_json(path: Path, expected: type) -> Any:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise DataError(f"cannot load valid JSON from {path}: {exc}") from exc
    if not isinstance(value, expected):
        raise DataError(f"{path} must contain a {expected.__name__}")
    return value


def atomic_json_write(path: Path, value: Any) -> None:
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    json.loads(text)  # Validate before touching the destination.
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        json.loads(Path(temporary).read_text(encoding="utf-8"))
        os.replace(temporary, path)
    except BaseException:
        try: os.unlink(temporary)
        except FileNotFoundError: pass
        raise


def validate_timestamp(value: str, label: str = "timestamp") -> datetime:
    try: parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (TypeError, ValueError) as exc: raise DataError(f"invalid {label}: {value!r}") from exc
    if parsed.tzinfo is None: raise DataError(f"{label} must include a timezone")
    return parsed


def canonical_id(frontend_id: str | int, slug: str) -> str:
    number = str(frontend_id).strip()
    if not number.isdigit() or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise DataError("problem ID must be numeric and slug must be lowercase kebab-case")
    return f"{number}-{slug}"


def extension_for(language: str) -> str:
    key = language.casefold().replace(" ", "")
    return {"python":"py", "python3":"py", "pandas":"py", "c++":"cpp", "cpp":"cpp", "c":"c", "c#":"cs", "java":"java", "javascript":"js", "typescript":"ts", "go":"go", "golang":"go", "rust":"rs", "kotlin":"kt", "swift":"swift", "ruby":"rb", "bash":"sh", "shell":"sh", "mysql":"sql", "mssql":"sql", "oraclesql":"sql", "postgresql":"sql", "php":"php", "scala":"scala", "dart":"dart", "racket":"rkt", "erlang":"erl", "elixir":"ex"}.get(key, "txt")


def known_submission_ids(tracker: dict[str, Any]) -> set[str]:
    return {str(a["submission_id"]) for p in tracker.get("problems", {}).values() for a in p.get("attempts", [])}


def _validate_tracker(tracker: dict[str, Any]) -> None:
    if tracker.get("schema_version") != 1 or not isinstance(tracker.get("problems"), dict):
        raise DataError("unsupported tracker schema")
    seen: set[str] = set()
    for key, problem in tracker["problems"].items():
        if key != canonical_id(problem["leetcode_id"], problem["slug"]): raise DataError(f"canonical key mismatch: {key}")
        if not isinstance(problem.get("attempts"), list): raise DataError(f"attempts must be a list: {key}")
        for attempt in problem["attempts"]:
            sid = str(attempt["submission_id"])
            if not sid.isdigit(): raise DataError(f"invalid submission ID: {sid}")
            if sid in seen: raise DataError(f"duplicate submission ID: {sid}")
            code_path = PurePosixPath(str(attempt.get("code_path", "")))
            if code_path.is_absolute() or ".." in code_path.parts or code_path.parts[:1] != ("solutions",):
                raise DataError(f"unsafe code path for submission {sid}")
            seen.add(sid); validate_timestamp(attempt["submitted_at"], "submitted_at")


def load_tracker(path: Path) -> dict[str, Any]:
    tracker = load_json(path, dict); _validate_tracker(tracker); return tracker


def import_submission(root: Path, tracker: dict[str, Any], submission: dict[str, Any]) -> bool:
    """Import one normalized submission. Existing IDs are no-ops unless data conflicts."""
    required = ("submission_id", "frontend_id", "slug", "title", "difficulty", "tags", "submitted_at", "language", "status", "code")
    missing = [key for key in required if key not in submission]
    if missing: raise DataError(f"submission missing fields: {', '.join(missing)}")
    sid = str(submission["submission_id"])
    if not sid.isdigit(): raise DataError(f"invalid submission ID: {sid}")
    validate_timestamp(submission["submitted_at"], "submitted_at")
    if not isinstance(submission["code"], str) or not submission["code"]:
        raise DataError("submission code must be non-empty text")
    if submission["difficulty"] not in {"Easy", "Medium", "Hard"}:
        raise DataError(f"invalid difficulty: {submission['difficulty']!r}")
    if not isinstance(submission["tags"], list) or not all(isinstance(tag, str) for tag in submission["tags"]):
        raise DataError("submission tags must be a list of strings")
    if not isinstance(submission.get("raw_comments", []), list) or not all(isinstance(comment, str) for comment in submission.get("raw_comments", [])):
        raise DataError("raw_comments must be a list of strings")
    key = canonical_id(submission["frontend_id"], submission["slug"])
    code_path = Path("solutions") / key / f"{sid}.{extension_for(submission['language'])}"
    absolute_code = root / code_path
    code_bytes = submission["code"].encode("utf-8")
    for problem in tracker["problems"].values():
        for existing in problem["attempts"]:
            if str(existing["submission_id"]) != sid:
                continue
            existing_path = root / existing["code_path"]
            if not existing_path.exists() or existing_path.read_bytes() != code_bytes:
                raise DataError(f"stored code differs for immutable submission {sid}")
            if (problem["slug"] != submission["slug"]
                    or str(problem["leetcode_id"]) != str(submission["frontend_id"])):
                raise DataError(f"submission {sid} changed problem identity")
            for field in ("submitted_at", "language"):
                if existing[field] != submission[field]:
                    raise DataError(f"submission {sid} changed immutable field {field}")
            changed = False
            for field in ("status", "leetcode_notes"):
                value = submission.get(field)
                if existing.get(field) != value:
                    existing[field] = value
                    changed = True
            for field in ("runtime", "memory"):
                value = submission.get(field)
                if value is not None and existing.get(field) != value:
                    existing[field] = value
                    changed = True
            for field in ("title", "difficulty", "tags"):
                value = submission[field]
                if problem.get(field) != value:
                    problem[field] = value
                    changed = True
            accepted = [a for a in problem["attempts"] if a["status"].casefold() == "accepted"]
            first = accepted[0]["submitted_at"] if accepted else None
            last = accepted[-1]["submitted_at"] if accepted else None
            if problem.get("first_solved_at") != first or problem.get("last_solved_at") != last:
                problem["first_solved_at"], problem["last_solved_at"] = first, last
                changed = True
            _validate_tracker(tracker)
            return changed
    if absolute_code.exists() and absolute_code.read_bytes() != code_bytes:
        raise DataError(f"refusing to overwrite different code at {code_path}")
    absolute_code.parent.mkdir(parents=True, exist_ok=True)
    if not absolute_code.exists():
        descriptor, temporary = tempfile.mkstemp(prefix=f".{absolute_code.name}.", dir=absolute_code.parent)
        try:
            with os.fdopen(descriptor, "wb") as handle: handle.write(code_bytes); handle.flush(); os.fsync(handle.fileno())
            os.replace(temporary, absolute_code)
        except BaseException:
            try: os.unlink(temporary)
            except FileNotFoundError: pass
            raise
    problem = tracker["problems"].setdefault(key, {
        "leetcode_id": str(submission["frontend_id"]), "slug": submission["slug"], "title": submission["title"],
        "difficulty": submission["difficulty"], "tags": submission["tags"],
        "leetcode_url": f"https://leetcode.com/problems/{submission['slug']}/", "first_solved_at": None,
        "last_solved_at": None, "attempts": [], "review": deepcopy(EMPTY_REVIEW),
    })
    if problem["slug"] != submission["slug"] or str(problem["leetcode_id"]) != str(submission["frontend_id"]):
        raise DataError(f"problem identity conflict for {key}")
    problem.update(title=submission["title"], difficulty=submission["difficulty"], tags=submission["tags"])
    attempt = {
        "submission_id": sid, "submitted_at": submission["submitted_at"], "status": submission["status"],
        "language": submission["language"], "code_path": code_path.as_posix(), "runtime": submission.get("runtime"),
        "memory": submission.get("memory"), "leetcode_notes": submission.get("leetcode_notes"),
        "raw_comments": list(submission.get("raw_comments", [])), "notes": {field: submission.get("notes", {}).get(field, "") for field in NOTE_FIELDS},
    }
    problem["attempts"].append(attempt)
    problem["attempts"].sort(key=lambda item: (
        validate_timestamp(item["submitted_at"], "submitted_at"), int(item["submission_id"])
    ))
    accepted = [a for a in problem["attempts"] if a["status"].casefold() == "accepted"]
    problem["first_solved_at"] = accepted[0]["submitted_at"] if accepted else None
    problem["last_solved_at"] = accepted[-1]["submitted_at"] if accepted else None
    _validate_tracker(tracker)
    return True


def write_tracker(root: Path, tracker: dict[str, Any]) -> None:
    _validate_tracker(tracker); atomic_json_write(root / "tracker.json", tracker)
    for key, problem in tracker["problems"].items(): atomic_json_write(root / "solutions" / key / "metadata.json", problem)
