"""Authenticated LeetCode access through a local Playwright Chromium profile.

The persistent profile lives outside the repository. The first run is headed
so you can log in manually; later runs reuse the stored session headlessly.
All GraphQL calls are same-origin fetches evaluated inside a real leetcode.com
page, so no cookies or tokens ever leave the local machine.
"""
from __future__ import annotations

import time
from typing import Any
from urllib.parse import urlparse

from playwright.sync_api import Error as PlaywrightError, sync_playwright

import leetcode_api
from config import Config
from leetcode_api import LeetCodeAPIError

BASE_URL = "https://leetcode.com/"
LOGIN_URL = "https://leetcode.com/accounts/login/"

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


def is_leetcode_url(url: str) -> bool:
    """Return whether a browser URL belongs to LeetCode."""
    hostname = (urlparse(url).hostname or "").lower()
    return hostname == "leetcode.com" or hostname.endswith(".leetcode.com")


class LeetCodeSession:
    """Context manager owning one persistent browser context."""

    def __init__(self, config: Config, headless: bool = True) -> None:
        self.config = config
        self.headless = headless
        self._playwright = None
        self._context = None
        self.page = None

    def __enter__(self) -> "LeetCodeSession":
        self.config.browser_profile.mkdir(parents=True, exist_ok=True)
        self._playwright = sync_playwright().start()
        try:
            self._context = self._playwright.chromium.launch_persistent_context(
                user_data_dir=str(self.config.browser_profile),
                headless=self.headless,
            )
            self.page = self._context.pages[0] if self._context.pages else self._context.new_page()
            self.page.goto(BASE_URL, wait_until="domcontentloaded")
        except BaseException:
            self.close()
            raise
        return self

    def __exit__(self, *exc_info: Any) -> None:
        self.close()

    def close(self) -> None:
        if self._context is not None:
            self._context.close()
            self._context = None
        if self._playwright is not None:
            self._playwright.stop()
            self._playwright = None

    def graphql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        """Run one throttled same-origin GraphQL request and parse it strictly."""
        time.sleep(self.config.request_delay_seconds)
        try:
            result = self.page.evaluate(
                _GRAPHQL_FETCH_JS, {"query": query, "variables": variables}
            )
        except PlaywrightError as exc:
            raise LeetCodeAPIError(f"browser fetch failed: {exc}") from exc
        if not isinstance(result, dict) or "status" not in result or "body" not in result:
            raise LeetCodeAPIError("browser fetch returned an unexpected shape")
        return leetcode_api.parse_graphql_payload(int(result["status"]), str(result["body"]))

    def user_status(self) -> dict[str, Any]:
        return leetcode_api.parse_user_status(
            self.graphql(leetcode_api.USER_STATUS_QUERY, {})
        )

    def ensure_signed_in(self, timeout_seconds: int = 300) -> dict[str, Any]:
        """Verify auth. In headed mode, wait only after confirmed signed-out state."""
        status = self.user_status()
        if status["is_signed_in"]:
            return status
        if self.headless:
            raise LeetCodeAPIError(
                "not signed in to leetcode. run: python scripts/sync_leetcode.py "
                "--show-browser and complete the login manually"
            )
        print("log in to leetcode in the browser window. waiting for the session...")
        self.page.goto(LOGIN_URL, wait_until="domcontentloaded")
        deadline = time.monotonic() + timeout_seconds
        while time.monotonic() < deadline:
            time.sleep(5)
            if not is_leetcode_url(self.page.url):
                continue
            status = self.user_status()
            if status["is_signed_in"]:
                print(f"signed in as {status['username']}")
                return status
        raise LeetCodeAPIError("login wait timed out; run the command again")
