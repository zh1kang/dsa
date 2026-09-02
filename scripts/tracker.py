"""Validated, atomic storage and append-only attempt merging."""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import tempfile
from copy import deepcopy
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any

NOTE_FIELDS = ("thought_process", "notes", "core_insight", "pattern", "mistakes", "edge_cases", "time_complexity", "space_complexity")
EMPTY_REVIEW = {"state": "new", "stability": None, "difficulty": None, "retrievability": None, "last_review": None, "next_review": None, "reps": 0, "lapses": 0}
TRACKER_SCHEMA_VERSION = 2

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


def atomic_bytes_write(path: Path, value: bytes) -> None:
    """Replace a binary file atomically after flushing it to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
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


def solution_path(frontend_id: str | int, slug: str, language: str) -> Path:
    """Return the flat, numbered solution path for one problem and language."""
    key = canonical_id(frontend_id, slug)
    return Path(f"{key}.{extension_for(language)}")


def _submission_marker(language: str, submission_id: str, submitted_at: str) -> bytes:
    key = language.casefold().replace(" ", "")
    if key in {"mysql", "mssql", "oraclesql", "postgresql"}:
        prefix = "--"
    elif key == "racket":
        prefix = ";"
    elif key in {"python", "python3", "pandas", "ruby", "bash", "shell"}:
        prefix = "#"
    else:
        prefix = "//"
    return f"{prefix} submission {submission_id} - {submitted_at}\n".encode("utf-8")


def _append_source(
    current: bytes, code: bytes, language: str, submission_id: str, submitted_at: str
) -> bytes:
    separator = b"\n" if current.endswith(b"\n") else b"\n\n"
    return current + separator + _submission_marker(
        language, submission_id, submitted_at
    ) + code


def known_submission_ids(tracker: dict[str, Any]) -> set[str]:
    return {str(a["submission_id"]) for p in tracker.get("problems", {}).values() for a in p.get("attempts", [])}


def _validate_tracker(
    tracker: dict[str, Any], expected_schema: int = TRACKER_SCHEMA_VERSION
) -> None:
    if (tracker.get("schema_version") != expected_schema
            or not isinstance(tracker.get("problems"), dict)):
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
            if code_path.is_absolute() or ".." in code_path.parts:
                raise DataError(f"unsafe code path for submission {sid}")
            if expected_schema == 1:
                if code_path.parts[:1] != ("solutions",):
                    raise DataError(f"unsafe code path for submission {sid}")
            else:
                expected_path = solution_path(
                    problem["leetcode_id"], problem["slug"], attempt["language"]
                )
                if code_path != PurePosixPath(expected_path.as_posix()):
                    raise DataError(f"incorrect flat code path for submission {sid}")
                digest = attempt.get("code_sha256")
                if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                    raise DataError(f"invalid source digest for submission {sid}")
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
    code_path = solution_path(
        submission["frontend_id"], submission["slug"], submission["language"]
    )
    absolute_code = root / code_path
    code_bytes = submission["code"].encode("utf-8")
    code_sha256 = hashlib.sha256(code_bytes).hexdigest()
    for problem in tracker["problems"].values():
        for existing in problem["attempts"]:
            if str(existing["submission_id"]) != sid:
                continue
            existing_path = root / existing["code_path"]
            if (existing.get("code_sha256") != code_sha256
                    or not existing_path.exists()
                    or code_bytes not in existing_path.read_bytes()):
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
    problem = tracker["problems"].setdefault(key, {
        "leetcode_id": str(submission["frontend_id"]), "slug": submission["slug"], "title": submission["title"],
        "difficulty": submission["difficulty"], "tags": submission["tags"],
        "leetcode_url": f"https://leetcode.com/problems/{submission['slug']}/", "first_solved_at": None,
        "last_solved_at": None, "attempts": [], "review": deepcopy(EMPTY_REVIEW),
    })
    if problem["slug"] != submission["slug"] or str(problem["leetcode_id"]) != str(submission["frontend_id"]):
        raise DataError(f"problem identity conflict for {key}")
    attempts_for_file = [
        attempt for attempt in problem["attempts"]
        if attempt.get("code_path") == code_path.as_posix()
    ]
    if absolute_code.exists():
        if not attempts_for_file:
            raise DataError(f"refusing to overwrite untracked file at {code_path}")
        combined = _append_source(
            absolute_code.read_bytes(), code_bytes, submission["language"],
            sid, submission["submitted_at"],
        )
    else:
        if attempts_for_file:
            raise DataError(f"missing flat solution file: {code_path}")
        combined = code_bytes
    atomic_bytes_write(absolute_code, combined)
    problem.update(title=submission["title"], difficulty=submission["difficulty"], tags=submission["tags"])
    attempt = {
        "submission_id": sid, "submitted_at": submission["submitted_at"], "status": submission["status"],
        "language": submission["language"], "code_path": code_path.as_posix(),
        "code_sha256": code_sha256, "runtime": submission.get("runtime"),
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
    _validate_tracker(tracker)
    atomic_json_write(root / "tracker.json", tracker)


def migrate_flat_solution_layout(
    root: Path, tracker_data: dict[str, Any]
) -> dict[str, Any]:
    """Migrate schema 1 submission files into flat per-problem archives."""
    if tracker_data.get("schema_version") == TRACKER_SCHEMA_VERSION:
        _validate_tracker(tracker_data)
        return tracker_data
    _validate_tracker(tracker_data, expected_schema=1)
    updated = deepcopy(tracker_data)
    planned: dict[Path, bytes] = {}
    for key, problem in updated["problems"].items():
        for attempt in problem["attempts"]:
            old_path = root / attempt["code_path"]
            if not old_path.is_file():
                raise DataError(f"missing stored code: {attempt['code_path']}")
            code = old_path.read_bytes()
            new_path = solution_path(
                problem["leetcode_id"], problem["slug"], attempt["language"]
            )
            if new_path in planned:
                planned[new_path] = _append_source(
                    planned[new_path], code, attempt["language"],
                    str(attempt["submission_id"]), attempt["submitted_at"],
                )
            else:
                planned[new_path] = code
            attempt["code_path"] = new_path.as_posix()
            attempt["code_sha256"] = hashlib.sha256(code).hexdigest()
    updated["schema_version"] = TRACKER_SCHEMA_VERSION
    _validate_tracker(updated)
    for relative_path, contents in planned.items():
        target = root / relative_path
        if target.exists() and target.read_bytes() != contents:
            raise DataError(f"refusing to overwrite untracked file at {relative_path}")
    for relative_path, contents in planned.items():
        atomic_bytes_write(root / relative_path, contents)
    write_tracker(root, updated)
    old_directory = root / "solutions"
    if old_directory.exists():
        shutil.rmtree(old_directory)
    return updated
