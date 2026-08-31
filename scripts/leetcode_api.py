"""Pure LeetCode GraphQL helpers: queries, strict parsing, pagination stop.

No network access here. LeetCode's internal API is undocumented and brittle,
so every parser fails closed on missing, null, or unexpected data.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

PAGE_SIZE = 20


class LeetCodeAPIError(RuntimeError):
    """Raised on any HTTP, GraphQL, schema, or challenge failure."""


USER_STATUS_QUERY = """
query globalData {
  userStatus {
    userId
    username
    isSignedIn
  }
}
"""

SUBMISSION_LIST_QUERY = """
query submissionList($offset: Int!, $limit: Int!, $slug: String) {
  submissionList(offset: $offset, limit: $limit, questionSlug: $slug) {
    hasNext
    submissions {
      id
      title
      titleSlug
      statusDisplay
      lang
      timestamp
      runtime
      memory
    }
  }
}
"""

SUBMISSION_DETAILS_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    id
    timestamp
    statusDisplay
    lang { name }
    code
    runtime
    memory
    notes
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    difficulty
    topicTags {
      name
      slug
    }
  }
}
"""


def epoch_to_iso(timestamp: Any) -> str:
    try:
        seconds = int(timestamp)
    except (TypeError, ValueError) as exc:
        raise LeetCodeAPIError(f"invalid epoch timestamp: {timestamp!r}") from exc
    if seconds <= 0:
        raise LeetCodeAPIError(f"invalid epoch timestamp: {timestamp!r}")
    return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat()


def parse_graphql_payload(status: int, body: str) -> dict[str, Any]:
    """Parse a raw GraphQL HTTP response. Fail closed on every anomaly."""
    if status != 200:
        raise LeetCodeAPIError(
            f"graphql http status {status}; possible challenge or expired login: {body[:200]!r}"
        )
    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise LeetCodeAPIError(
            f"graphql returned non-json; possible challenge page: {body[:200]!r}"
        ) from exc
    if not isinstance(payload, dict):
        raise LeetCodeAPIError("graphql response is not an object")
    if payload.get("errors"):
        raise LeetCodeAPIError(f"graphql errors: {payload['errors']!r}")
    data = payload.get("data")
    if not isinstance(data, dict):
        raise LeetCodeAPIError("graphql response has no data object")
    return data


def _require(mapping: Any, field: str, context: str) -> Any:
    if not isinstance(mapping, dict) or field not in mapping or mapping[field] is None:
        raise LeetCodeAPIError(f"{context} is missing required field {field!r}")
    return mapping[field]


def _text(mapping: Any, field: str, context: str) -> str:
    value = _require(mapping, field, context)
    if not isinstance(value, str) or not value:
        raise LeetCodeAPIError(f"{context}.{field} is not non-empty text")
    return value


def _numeric_id(mapping: Any, field: str, context: str) -> str:
    value = _require(mapping, field, context)
    if isinstance(value, bool) or not isinstance(value, (str, int)) or not str(value).isdigit():
        raise LeetCodeAPIError(f"{context}.{field} is not a numeric ID")
    return str(value)


def _optional_text(mapping: dict[str, Any], field: str, context: str) -> str | None:
    value = mapping.get(field)
    if value is not None and not isinstance(value, str):
        raise LeetCodeAPIError(f"{context}.{field} is not text or null")
    return value


def parse_user_status(data: dict[str, Any]) -> dict[str, Any]:
    status = _require(data, "userStatus", "userStatus response")
    signed_in = _require(status, "isSignedIn", "userStatus")
    if not isinstance(signed_in, bool):
        raise LeetCodeAPIError("userStatus.isSignedIn is not a boolean")
    if not signed_in:
        return {"user_id": None, "username": "", "is_signed_in": False}
    return {
        "user_id": _numeric_id(status, "userId", "userStatus"),
        "username": _text(status, "username", "userStatus"),
        "is_signed_in": True,
    }


def parse_submission_list(data: dict[str, Any]) -> dict[str, Any]:
    listing = _require(data, "submissionList", "submissionList response")
    submissions = _require(listing, "submissions", "submissionList")
    if not isinstance(submissions, list):
        raise LeetCodeAPIError("submissionList.submissions is not a list")
    parsed = []
    for item in submissions:
        timestamp = _require(item, "timestamp", "submission list item")
        if isinstance(timestamp, bool) or not isinstance(timestamp, (str, int)) or not str(timestamp).isdigit():
            raise LeetCodeAPIError("submission list item.timestamp is not an epoch")
        parsed.append({
            "submission_id": _numeric_id(item, "id", "submission list item"),
            "title": _text(item, "title", "submission list item"),
            "title_slug": _text(item, "titleSlug", "submission list item"),
            "status": _text(item, "statusDisplay", "submission list item"),
            "language": _text(item, "lang", "submission list item"),
            "timestamp": int(timestamp),
            "runtime": _optional_text(item, "runtime", "submission list item"),
            "memory": _optional_text(item, "memory", "submission list item"),
        })
    has_next = _require(listing, "hasNext", "submissionList")
    if not isinstance(has_next, bool):
        raise LeetCodeAPIError("submissionList.hasNext is not a boolean")
    return {"has_next": has_next, "submissions": parsed}


def parse_submission_details(data: dict[str, Any]) -> dict[str, Any]:
    details = _require(data, "submissionDetails", "submissionDetails response")
    lang = _require(details, "lang", "submissionDetails")
    code = _require(details, "code", "submissionDetails")
    if not isinstance(code, str) or not code:
        raise LeetCodeAPIError("submissionDetails.code is empty")
    notes = _optional_text(details, "notes", "submissionDetails")
    return {
        "submission_id": _numeric_id(details, "id", "submissionDetails"),
        "submitted_at": epoch_to_iso(_require(details, "timestamp", "submissionDetails")),
        "status": _text(details, "statusDisplay", "submissionDetails"),
        "language": _text(lang, "name", "submissionDetails.lang"),
        "code": code,
        "runtime": _optional_text(details, "runtime", "submissionDetails"),
        "memory": _optional_text(details, "memory", "submissionDetails"),
        "leetcode_notes": notes if notes else None,
    }


def parse_question(data: dict[str, Any]) -> dict[str, Any]:
    question = _require(data, "question", "question response")
    tags = _require(question, "topicTags", "question")
    if not isinstance(tags, list):
        raise LeetCodeAPIError("question.topicTags is not a list")
    difficulty = _text(question, "difficulty", "question")
    if difficulty not in {"Easy", "Medium", "Hard"}:
        raise LeetCodeAPIError(f"question.difficulty is unexpected: {difficulty!r}")
    return {
        "frontend_id": _numeric_id(question, "questionFrontendId", "question"),
        "title": _text(question, "title", "question"),
        "slug": _text(question, "titleSlug", "question"),
        "difficulty": difficulty,
        "tags": [_text(tag, "name", "question.topicTags item") for tag in tags],
    }


def split_new_submissions(submissions: list[dict[str, Any]],
                          known_ids: set[str]) -> tuple[list[dict[str, Any]], bool]:
    """Take newest-first stubs until the first already-known submission ID.

    Returns (fresh_stubs, stop). stop is True once a known ID is seen, which
    ends pagination on incremental syncs. On a first run known_ids is empty,
    so pagination continues through the full history until hasNext is false.
    """
    fresh: list[dict[str, Any]] = []
    for stub in submissions:
        if stub["submission_id"] in known_ids:
            return fresh, True
        fresh.append(stub)
    return fresh, False
