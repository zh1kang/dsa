"""Authenticated LeetCode access through a Chrome-owned local profile.

Chrome owns and encrypts the persistent profile outside the repository.
Playwright connects to that running browser over a loopback-only DevTools
endpoint, so it never launches the profile with a different keychain identity.
All GraphQL calls remain same-origin browser fetches.
"""
from __future__ import annotations

import shutil
import socket
import sqlite3
import subprocess
import time
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import urlopen

from playwright.sync_api import Error as PlaywrightError, sync_playwright

import leetcode_api
from config import Config
from leetcode_api import LeetCodeAPIError

BASE_URL = "https://leetcode.com/"
LOGIN_URL = "https://leetcode.com/accounts/login/"
DEBUG_HOST = "127.0.0.1"

_GRAPHQL_FETCH_JS = r"""
async ({ query, variables }) => {
  const match = document.cookie.match(/(?:^|; )csrftoken=([^;]+)/);
  const headers = { "Content-Type": "application/json" };
  if (match) headers["X-CSRFToken"] = decodeURIComponent(match[1]);
  const operationName = query.match(/\b(?:query|mutation)\s+(\w+)/)?.[1];
  const response = await fetch("/graphql/", {
    method: "POST",
    credentials: "same-origin",
    headers,
    body: JSON.stringify({ query, variables, operationName }),
  });
  return { status: response.status, body: await response.text() };
}
"""


def find_chrome_executable() -> Path:
    """Locate a normal Chrome installation instead of a test browser."""
    candidates = [
        Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
        Path.home() / "Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    for command in ("google-chrome", "google-chrome-stable"):
        resolved = shutil.which(command)
        if resolved:
            return Path(resolved)
    raise LeetCodeAPIError(
        "Google Chrome is required for LeetCode authentication; install Chrome and retry"
    )


def chrome_command(
    executable: Path,
    profile: Path,
    url: str,
    *,
    debugging_port: int | None = None,
    headless: bool = False,
) -> list[str]:
    """Build a direct Chrome command without Playwright launch flags."""
    command = [
        str(executable),
        f"--user-data-dir={profile}",
        "--no-first-run",
        "--no-default-browser-check",
    ]
    if debugging_port is not None:
        command.extend([
            f"--remote-debugging-address={DEBUG_HOST}",
            f"--remote-debugging-port={debugging_port}",
        ])
    if headless:
        command.append("--headless=new")
    command.append(url)
    return command


def launch_chrome(
    profile: Path,
    url: str,
    *,
    debugging_port: int | None = None,
    headless: bool = False,
) -> subprocess.Popen[bytes]:
    profile.mkdir(parents=True, exist_ok=True)
    return subprocess.Popen(
        chrome_command(
            find_chrome_executable(), profile, url,
            debugging_port=debugging_port, headless=headless,
        ),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def stop_chrome(process: subprocess.Popen[bytes]) -> None:
    """Stop only the Chrome process started by this module."""
    if process.poll() is not None:
        return
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


def _cookie_databases(profile: Path) -> tuple[Path, ...]:
    default = profile / "Default"
    return default / "Cookies", default / "Network" / "Cookies"


def has_leetcode_session(profile: Path) -> bool:
    """Check for a LeetCode session cookie without reading its value."""
    for database in _cookie_databases(profile):
        if not database.is_file():
            continue
        try:
            with sqlite3.connect(f"file:{database}?mode=ro", uri=True) as connection:
                row = connection.execute(
                    "SELECT 1 FROM cookies "
                    "WHERE host_key IN ('leetcode.com', '.leetcode.com', 'www.leetcode.com') "
                    "AND name = 'LEETCODE_SESSION' LIMIT 1"
                ).fetchone()
        except sqlite3.Error:
            continue
        if row is not None:
            return True
    return False


def login_interactively(config: Config, timeout_seconds: int = 300) -> None:
    """Let normal Chrome complete Cloudflare and login before automation starts."""
    process = launch_chrome(config.browser_profile, LOGIN_URL)
    print("log in to leetcode in the Chrome window. waiting for the session...")
    deadline = time.monotonic() + timeout_seconds
    try:
        while time.monotonic() < deadline:
            if has_leetcode_session(config.browser_profile):
                print("LeetCode session saved")
                return
            if process.poll() is not None:
                raise LeetCodeAPIError(
                    "Chrome closed before LeetCode finished signing in; run the command again"
                )
            time.sleep(1)
        raise LeetCodeAPIError("login wait timed out; run the command again")
    finally:
        stop_chrome(process)


def _available_port() -> int:
    with socket.socket() as listener:
        listener.bind((DEBUG_HOST, 0))
        return int(listener.getsockname()[1])


def _wait_for_debugger(
    process: subprocess.Popen[bytes], port: int, timeout_seconds: int = 15
) -> str:
    endpoint = f"http://{DEBUG_HOST}:{port}"
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise LeetCodeAPIError(
                f"Chrome exited before its local debugging endpoint started "
                f"(exit code {process.returncode})"
            )
        try:
            with urlopen(f"{endpoint}/json/version", timeout=1):
                return endpoint
        except (OSError, URLError):
            time.sleep(0.1)
    raise LeetCodeAPIError("Chrome local debugging endpoint did not start")


class LeetCodeSession:
    """Context manager that owns one direct Chrome process and CDP connection."""

    def __init__(self, config: Config, headless: bool = True) -> None:
        self.config = config
        self.headless = headless
        self._playwright = None
        self._browser = None
        self._chrome_process = None
        self.page = None

    def __enter__(self) -> "LeetCodeSession":
        self.config.browser_profile.mkdir(parents=True, exist_ok=True)
        port = _available_port()
        self._playwright = sync_playwright().start()
        try:
            self._chrome_process = launch_chrome(
                self.config.browser_profile,
                BASE_URL,
                debugging_port=port,
                headless=self.headless,
            )
            endpoint = _wait_for_debugger(self._chrome_process, port)
            self._browser = self._playwright.chromium.connect_over_cdp(endpoint)
            if not self._browser.contexts:
                raise LeetCodeAPIError("Chrome opened without a browser context")
            context = self._browser.contexts[0]
            self.page = context.pages[0] if context.pages else context.new_page()
            self.page.goto(BASE_URL, wait_until="domcontentloaded")
        except BaseException:
            self.close()
            raise
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()

    def close(self) -> None:
        if self._browser is not None:
            self._browser.close()
            self._browser = None
        if self._chrome_process is not None:
            stop_chrome(self._chrome_process)
            self._chrome_process = None
        if self._playwright is not None:
            self._playwright.stop()
            self._playwright = None

    def graphql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        """Run one throttled same-origin GraphQL request and parse it strictly."""
        result = None
        for attempt in range(2):
            time.sleep(self.config.request_delay_seconds)
            try:
                result = self.page.evaluate(
                    _GRAPHQL_FETCH_JS, {"query": query, "variables": variables}
                )
                break
            except PlaywrightError as exc:
                navigated = "Execution context was destroyed" in str(exc)
                if not navigated or attempt == 1:
                    raise LeetCodeAPIError(f"browser fetch failed: {exc}") from exc
                self.page.goto(BASE_URL, wait_until="domcontentloaded")
        if not isinstance(result, dict) or "status" not in result or "body" not in result:
            raise LeetCodeAPIError("browser fetch returned an unexpected shape")
        return leetcode_api.parse_graphql_payload(int(result["status"]), str(result["body"]))

    def user_status(self) -> dict[str, Any]:
        return leetcode_api.parse_user_status(
            self.graphql(leetcode_api.USER_STATUS_QUERY, {})
        )

    def ensure_signed_in(self) -> dict[str, Any]:
        status = self.user_status()
        if status["is_signed_in"]:
            return status
        raise LeetCodeAPIError(
            "not signed in to leetcode. run: python scripts/sync_leetcode.py "
            "--reauth and complete the login manually"
        )
