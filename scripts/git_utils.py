"""Minimal git helper for the tracker's automated commits."""
from __future__ import annotations

import subprocess
from pathlib import Path


class GitError(RuntimeError):
    pass


def run_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        raise GitError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def is_repo(root: Path) -> bool:
    try:
        return run_git(root, "rev-parse", "--is-inside-work-tree").strip() == "true"
    except GitError:
        return False


def worktree_changes(root: Path) -> list[str]:
    """Return every non-ignored tracked or untracked worktree change."""
    return [line for line in run_git(root, "status", "--porcelain").splitlines() if line]


def ensure_clean(root: Path) -> None:
    dirty = worktree_changes(root)
    if dirty:
        raise GitError(
            "worktree has uncommitted tracked changes; commit or restore them first:\n"
            + "\n".join(dirty)
        )


def has_upstream(root: Path) -> bool:
    try:
        run_git(root, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}")
        return True
    except GitError:
        return False


def pull_ff_only(root: Path) -> None:
    run_git(root, "pull", "--ff-only")


def stage(root: Path, paths: list[str]) -> None:
    existing = [path for path in paths if (root / path).exists()]
    if existing:
        run_git(root, "add", "--", *existing)


def has_staged_changes(root: Path) -> bool:
    result = subprocess.run(
        ["git", "-C", str(root), "diff", "--cached", "--quiet"],
        capture_output=True, text=True, check=False,
    )
    if result.returncode not in (0, 1):
        raise GitError(f"git diff --cached failed: {result.stderr.strip()}")
    return result.returncode == 1


def commit(root: Path, message: str) -> None:
    run_git(root, "commit", "-m", message)


def push(root: Path) -> None:
    run_git(root, "push")
