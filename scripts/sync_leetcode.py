"""Sync LeetCode submissions into the local tracker.

Order of operations: clean-worktree check, optional fast-forward pull, scrape,
strict validation of every detail, atomic tracker replacement, schedule and
sheet regeneration, one commit, optional push. Grades are never inferred from
accepted submissions. If nothing new exists, nothing is written or committed.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import comment_parser
import git_utils
import google_sheets
import leetcode_api
import tracker
import update_review_schedule
from config import Config, load_config
from leetcode_api import LeetCodeAPIError

SYNC_PATHS = [
    "tracker.json", "review-schedule.json", "google-sheets.csv",
    "mindsolve-log.csv",
]


def push_google_sheet(config: Config, tracker_data: dict[str, Any]) -> None:
    events = tracker.load_json(config.root / "review-log.json", list)
    google_sheets.push_tracker(config, tracker_data, events)


def bind_local_account(config: Config, status: dict[str, Any]) -> None:
    """Pin this dataset to the first authenticated LeetCode account."""
    identity = {"user_id": str(status["user_id"]), "username": status["username"]}
    path = config.account_file
    if path.exists():
        expected = tracker.load_json(path, dict)
        if expected != identity:
            raise LeetCodeAPIError(
                f"authenticated LeetCode account {identity['username']!r} does not match "
                f"the locally pinned account {expected.get('username')!r}; log into the "
                f"original account or intentionally remove {path} to start another dataset"
            )
        return
    tracker.atomic_json_write(path, identity)
    path.chmod(0o600)
    print(f"pinned local LeetCode account: {identity['username']} ({identity['user_id']})")


def delete_browser_profile(profile: Path) -> None:
    """Delete only the configured local browser profile. Guarded and explicit."""
    profile = profile.expanduser().resolve()
    home = Path.home().resolve()
    if profile == home or home not in profile.parents:
        raise SystemExit(f"refusing to delete {profile}: not inside the home directory")
    if profile.exists():
        shutil.rmtree(profile)
        print(f"deleted browser profile: {profile}")
    else:
        print(f"browser profile does not exist: {profile}")


def collect_sync_stubs(session: Any, known_ids: set[str]) -> list[dict[str, Any]]:
    """Collect new stubs plus the first known boundary for change detection."""
    stubs: list[dict[str, Any]] = []
    seen = set(known_ids)
    offset = 0
    while True:
        data = session.graphql(leetcode_api.SUBMISSION_LIST_QUERY, {
            "offset": offset,
            "limit": leetcode_api.PAGE_SIZE,
            "slug": None,
        })
        page = leetcode_api.parse_submission_list(data)
        page_ids = [stub["submission_id"] for stub in page["submissions"]]
        if len(page_ids) != len(set(page_ids)):
            raise LeetCodeAPIError("submissionList returned duplicate IDs within one page")
        duplicates = set(page_ids) & (seen - known_ids)
        if duplicates:
            raise LeetCodeAPIError(
                f"submissionList changed during pagination; repeated IDs: {sorted(duplicates)}"
            )
        fresh, stop = leetcode_api.split_new_submissions(page["submissions"], known_ids)
        stubs.extend(fresh)
        seen.update(page_ids)
        if stop:
            boundary = next(stub for stub in page["submissions"]
                            if stub["submission_id"] in known_ids)
            stubs.append(boundary)
            return stubs
        if not page["submissions"]:
            if page["has_next"]:
                raise LeetCodeAPIError("submissionList returned an empty non-terminal page")
            return stubs
        if not page["has_next"]:
            return stubs
        offset += len(page["submissions"])


def fetch_submissions(session: Any, stubs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Fetch and strictly validate details plus question metadata, oldest first."""
    question_cache: dict[str, dict[str, Any]] = {}
    submissions: list[dict[str, Any]] = []
    for stub in reversed(stubs):
        details = leetcode_api.parse_submission_details(session.graphql(
            leetcode_api.SUBMISSION_DETAILS_QUERY,
            {"submissionId": int(stub["submission_id"])},
        ))
        if details["submission_id"] != stub["submission_id"]:
            raise LeetCodeAPIError(
                f"submissionDetails id mismatch: asked {stub['submission_id']}, "
                f"got {details['submission_id']}"
            )
        slug = stub["title_slug"]
        if slug not in question_cache:
            question = leetcode_api.parse_question(session.graphql(
                leetcode_api.QUESTION_QUERY, {"titleSlug": slug}
            ))
            if question["slug"] != slug:
                raise LeetCodeAPIError(f"question slug mismatch for {slug!r}")
            question_cache[slug] = question
        question = question_cache[slug]
        raw_comments = comment_parser.extract_comments(details["code"], details["language"])
        submissions.append({
            "submission_id": details["submission_id"],
            "frontend_id": question["frontend_id"],
            "slug": question["slug"],
            "title": question["title"],
            "difficulty": question["difficulty"],
            "tags": question["tags"],
            "submitted_at": details["submitted_at"],
            "language": details["language"],
            "status": details["status"],
            "code": details["code"],
            "runtime": stub["runtime"],
            "memory": stub["memory"],
            "leetcode_notes": details["leetcode_notes"],
            "raw_comments": raw_comments,
            "notes": comment_parser.parse_structured_notes(raw_comments),
        })
    return submissions


def import_submissions(
    root: Path, tracker_data: dict[str, Any], submissions: list[dict[str, Any]]
) -> tuple[dict[str, Any], int, int]:
    """Import a validated batch and restore every flat file if the batch fails."""
    updated = deepcopy(tracker_data)
    originals: dict[Path, bytes | None] = {}
    original_ids = tracker.known_submission_ids(tracker_data)
    imported = 0
    changed = 0
    try:
        for submission in submissions:
            source = root / tracker.solution_path(
                submission["frontend_id"], submission["slug"], submission["language"]
            )
            if source not in originals:
                originals[source] = source.read_bytes() if source.exists() else None
            if tracker.import_submission(root, updated, submission):
                if str(submission["submission_id"]) in original_ids:
                    changed += 1
                else:
                    imported += 1
    except BaseException:
        for source, original in originals.items():
            if original is None:
                source.unlink(missing_ok=True)
            else:
                tracker.atomic_bytes_write(source, original)
        raise
    return updated, imported, changed


def run_sync(config: Config, headless: bool, no_push: bool) -> int:
    root = config.root
    in_repo = git_utils.is_repo(root)
    if in_repo:
        git_utils.ensure_clean(root)
        if config.auto_push and not no_push and git_utils.has_upstream(root):
            git_utils.pull_ff_only(root)

    tracker_data = tracker.load_tracker(root / "tracker.json")
    known_ids = tracker.known_submission_ids(tracker_data)

    from leetcode_browser import LeetCodeSession

    with LeetCodeSession(config, headless=headless) as session:
        account = session.ensure_signed_in()
        bind_local_account(config, account)
        print(f"authenticated as {account['username']}")
        stubs = collect_sync_stubs(session, known_ids)
        if not stubs:
            print("no new or changed submissions")
            if config.spreadsheet_id:
                try:
                    push_google_sheet(config, tracker_data)
                    print("google sheet updated")
                except Exception as exc:
                    print(f"error: Google Sheets update failed: {exc}", file=sys.stderr)
                    return 1
            return 0
        print(f"found {len(stubs)} new submissions; fetching details")
        submissions = fetch_submissions(session, stubs)

    # Every network detail is validated before any source or tracker file is written.
    updated, imported, changed = import_submissions(root, tracker_data, submissions)
    if not imported and not changed:
        print("no new or changed submissions")
        if config.spreadsheet_id:
            try:
                push_google_sheet(config, tracker_data)
                print("google sheet updated")
            except Exception as exc:
                print(f"error: Google Sheets update failed: {exc}", file=sys.stderr)
                return 1
        return 0
    tracker.write_tracker(root, updated)
    update_review_schedule.regenerate(
        config, datetime.now(timezone.utc)
    )
    print(f"imported {imported} new and refreshed {changed} changed submissions")

    failed = False
    if (imported or changed) and in_repo:
        solution_paths = sorted({
            tracker.solution_path(
                submission["frontend_id"], submission["slug"], submission["language"]
            ).as_posix()
            for submission in submissions
        })
        git_utils.stage(root, SYNC_PATHS + solution_paths)
        if git_utils.has_staged_changes(root):
            if changed:
                message = f"leetcode: sync {imported} new, {changed} changed submissions"
            else:
                message = f"leetcode: sync {imported} new submissions"
            git_utils.commit(root, message)
            if config.auto_push and not no_push:
                if not git_utils.has_upstream(root):
                    print("error: auto-push is enabled but this branch has no upstream; local commit kept",
                          file=sys.stderr)
                    failed = True
                else:
                    try:
                        git_utils.push(root)
                    except git_utils.GitError as exc:
                        print(f"error: push failed; local data and commit are kept: {exc}",
                              file=sys.stderr)
                        failed = True
    if config.spreadsheet_id:
        try:
            push_google_sheet(
                config, tracker.load_tracker(root / "tracker.json")
            )
            print("google sheet updated")
        except Exception as exc:
            print(f"error: Google Sheets update failed: {exc}", file=sys.stderr)
            failed = True
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="sync leetcode submissions")
    parser.add_argument("--no-push", action="store_true",
                        help="do not pull or push; keep changes local")
    parser.add_argument("--show-browser", action="store_true",
                        help="run headed for a manual login")
    parser.add_argument("--reauth", action="store_true",
                        help="delete the local browser profile and log in again")
    args = parser.parse_args(argv)

    config = load_config()
    if args.reauth:
        delete_browser_profile(config.browser_profile)
        print("reauth requested: Chrome opens for a manual login")
    try:
        from leetcode_browser import has_leetcode_session, login_interactively

        if not has_leetcode_session(config.browser_profile):
            print("opening normal Chrome so you can log in to LeetCode")
            login_interactively(config)
        return run_sync(config, headless=not args.show_browser, no_push=args.no_push)
    except (LeetCodeAPIError, tracker.DataError, git_utils.GitError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
