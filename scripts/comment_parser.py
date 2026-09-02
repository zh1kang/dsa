"""Extract exact ordered comment bodies and conservative structured notes.

Raw comment bodies are authoritative. Extraction removes only syntax
delimiters and one conventional separator space; it never rewrites,
dedents, trims, or summarizes the remaining text.
Structured note parsing is conservative: it fills a field only from an
explicit "label:" line and never invents content.
"""
from __future__ import annotations

import re

NOTE_FIELDS = (
    "thought_process",
    "notes",
    "core_insight",
    "pattern",
    "mistakes",
    "edge_cases",
    "time_complexity",
    "space_complexity",
)

_PYTHON = {"python", "python3", "pandas"}
_HASH = {"bash", "shell", "sh", "ruby", "rb", "elixir"}
_SQL = {"sql", "mysql", "mssql", "oraclesql", "postgresql"}
_C_LIKE = {
    "c", "c++", "cpp", "c#", "cs", "csharp", "java", "javascript", "js",
    "typescript", "ts", "go", "golang", "rust", "kotlin", "swift", "scala",
    "dart", "php",
}
_STRING_PREFIXES = {"r", "b", "u", "f", "rb", "br", "fr", "rf"}

_LABEL_ALIASES = {
    "thought process": "thought_process",
    "thoughts": "thought_process",
    "approach": "thought_process",
    "intuition": "thought_process",
    "core insight": "core_insight",
    "key insight": "core_insight",
    "insight": "core_insight",
    "pattern": "pattern",
    "patterns": "pattern",
    "mistake": "mistakes",
    "mistakes": "mistakes",
    "pitfall": "mistakes",
    "pitfalls": "mistakes",
    "edge case": "edge_cases",
    "edge cases": "edge_cases",
    "tc": "time_complexity",
    "sc": "space_complexity",
}
_LABEL_RE = re.compile(r"^\s*(?:[-*•]+\s*)?([A-Za-z][A-Za-z ]{0,30}?)\s*:\s*(.*)$")
_DIVERGENCES_RE = re.compile(
    r"^\s*(?:main\s+)?divergences(?:\s+\d+)?\s*:?\s*(.*)$",
    re.IGNORECASE,
)


def family_for(language: str) -> str | None:
    key = language.casefold().replace(" ", "")
    if key in _PYTHON:
        return "python"
    if key in _HASH:
        return "hash"
    if key in _SQL:
        return "sql"
    if key in _C_LIKE:
        return "c"
    return None


def extract_comments(code: str, language: str) -> list[str]:
    """Return ordered comment bodies for the given language, or [] if unknown."""
    family = family_for(language)
    if family is None or not code:
        return []
    if family == "python":
        return _scan_python(code)
    if family == "hash":
        return _scan_generic(code, line_markers=("#",), block_pair=None,
                             quotes="\"'", doubled_quote_escape=False)
    if family == "sql":
        return _scan_generic(code, line_markers=("--",), block_pair=("/*", "*/"),
                             quotes="\"'", doubled_quote_escape=True)
    markers = ("//", "#") if language.casefold().replace(" ", "") == "php" else ("//",)
    return _scan_generic(code, line_markers=markers, block_pair=("/*", "*/"),
                         quotes="\"'`", doubled_quote_escape=False)


def _comment_body(inner: str) -> str:
    """Remove one conventional post-delimiter space; preserve everything else."""
    return inner[1:] if inner.startswith(" ") else inner


def _scan_generic(code: str, line_markers: tuple[str, ...],
                  block_pair: tuple[str, str] | None, quotes: str,
                  doubled_quote_escape: bool) -> list[str]:
    comments: list[str] = []
    i, n = 0, len(code)
    while i < n:
        ch = code[i]
        if ch in quotes:
            i += 1
            while i < n:
                if code[i] == "\\" and not doubled_quote_escape:
                    i += 2
                    continue
                if code[i] == ch:
                    if doubled_quote_escape and code.startswith(ch, i + 1):
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            continue
        if block_pair and code.startswith(block_pair[0], i):
            end = code.find(block_pair[1], i + len(block_pair[0]))
            inner = code[i + len(block_pair[0]): end if end != -1 else n]
            comments.append(_comment_body(inner))
            i = n if end == -1 else end + len(block_pair[1])
            continue
        marker = next((m for m in line_markers if code.startswith(m, i)), None)
        if marker is not None:
            end = code.find("\n", i)
            inner = code[i + len(marker): end if end != -1 else n]
            comments.append(_comment_body(inner.rstrip("\r")))
            i = n if end == -1 else end + 1
            continue
        i += 1
    return comments


def _scan_python(code: str) -> list[str]:
    comments: list[str] = []
    i, n = 0, len(code)
    line_start = 0
    while i < n:
        ch = code[i]
        if ch == "\n":
            i += 1
            line_start = i
            continue
        if ch == "#":
            end = code.find("\n", i)
            inner = code[i + 1: end if end != -1 else n]
            comments.append(_comment_body(inner.rstrip("\r")))
            i = n if end == -1 else end
            continue
        if ch.isalnum() or ch == "_":
            j = i
            while j < n and (code[j].isalnum() or code[j] == "_"):
                j += 1
            word = code[i:j]
            if j < n and code[j] in "\"'" and word.casefold() in _STRING_PREFIXES:
                i = _consume_python_string(code, j, statement_start=False,
                                           comments=comments, line_start=line_start,
                                           string_start=i)
                continue
            i = j
            continue
        if ch in "\"'":
            statement_start = code[line_start:i].strip() == ""
            i = _consume_python_string(code, i, statement_start=statement_start,
                                       comments=comments, line_start=line_start,
                                       string_start=i)
            continue
        i += 1
    return comments


def _consume_python_string(code: str, quote_index: int, statement_start: bool,
                           comments: list[str], line_start: int,
                           string_start: int) -> int:
    n = len(code)
    quote = code[quote_index]
    triple = code.startswith(quote * 3, quote_index)
    delim = quote * (3 if triple else 1)
    body_start = quote_index + len(delim)
    k = body_start
    closed = False
    while k < n:
        if code[k] == "\\":
            k += 2
            continue
        if code.startswith(delim, k):
            closed = True
            break
        if not triple and code[k] == "\n":
            break
        k += 1
    inner = code[body_start:min(k, n)]
    end_index = (k + len(delim)) if closed else min(k, n)
    prefixed = string_start != quote_index
    if triple and closed and statement_start and not prefixed:
        rest_end = code.find("\n", end_index)
        rest = code[end_index: rest_end if rest_end != -1 else n]
        if rest.strip() == "":
            comments.append(inner)
    return end_index


def parse_structured_notes(comments: list[str]) -> dict[str, str]:
    """Fill note fields from explicit "label:" lines inside comment bodies.

    Continuation lines attach to the last labeled field only inside the same
    comment body and stop at a blank line or a new label. Unlabeled comments
    are never assigned to a field.
    """
    notes = {field: "" for field in NOTE_FIELDS}
    for comment in comments:
        current: str | None = None
        for line in comment.splitlines():
            match = _LABEL_RE.match(line)
            field = _LABEL_ALIASES.get(match.group(1).strip().casefold()) if match else None
            if field is not None:
                text = match.group(2).strip()
                if text:
                    notes[field] = f"{notes[field]}\n{text}" if notes[field] else text
                current = field
                continue
            if current is None:
                continue
            stripped = line.strip()
            if not stripped:
                current = None
                continue
            notes[current] = f"{notes[current]}\n{stripped}" if notes[current] else stripped
    sections = split_divergence_sections(comments)
    if sections is not None:
        notes["thought_process"], notes["notes"] = sections
    return notes


def split_divergence_sections(comments: list[str]) -> tuple[str, str] | None:
    """Split ordered comments at the first ``divergences`` marker.

    Comments before the marker are the author's thought process. The marker's
    inline text and every later comment become notes. The raw comment list is
    not changed. Without a marker, no section is inferred.
    """
    thoughts: list[str] = []
    divergence_notes: list[str] = []
    found = False
    for comment in comments:
        if found:
            divergence_notes.append(comment)
            continue
        lines = comment.splitlines()
        marker_index: int | None = None
        marker_text = ""
        for index, line in enumerate(lines):
            match = _DIVERGENCES_RE.fullmatch(line)
            if match is not None:
                marker_index = index
                marker_text = match.group(1)
                break
        if marker_index is None:
            thoughts.append(comment)
            continue
        found = True
        before = "\n".join(lines[:marker_index])
        after = "\n".join(lines[marker_index + 1:])
        if before:
            thoughts.append(before)
        if marker_text:
            divergence_notes.append(marker_text)
        if after:
            divergence_notes.append(after)
    if not found:
        return None
    return (_join_comment_bodies(thoughts), _join_comment_bodies(divergence_notes))


def _join_comment_bodies(comments: list[str]) -> str:
    return "\n".join(comments).strip("\n")
