"""Tests for the interactive LeetCode browser login flow."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import leetcode_browser


class LoginPage:
    def __init__(self):
        self.url = leetcode_browser.BASE_URL

    def goto(self, url, wait_until):
        self.url = url


class TestInteractiveLogin(unittest.TestCase):
    def test_external_oauth_page_is_not_queried_as_leetcode(self):
        page = LoginPage()
        session = leetcode_browser.LeetCodeSession(SimpleNamespace(), headless=False)
        session.page = page

        statuses = iter([
            {"user_id": "", "username": "", "is_signed_in": False},
            {"user_id": "7", "username": "caleb", "is_signed_in": True},
        ])

        def user_status():
            self.assertTrue(leetcode_browser.is_leetcode_url(page.url))
            return next(statuses)

        session.user_status = Mock(side_effect=user_status)
        visited_urls = iter(["https://accounts.google.com/signin", leetcode_browser.BASE_URL])

        def advance_login(_seconds):
            page.url = next(visited_urls)

        with (
            patch("leetcode_browser.time.sleep", side_effect=advance_login),
            patch("leetcode_browser.time.monotonic", side_effect=[0, 1, 2]),
        ):
            status = session.ensure_signed_in(timeout_seconds=10)

        self.assertTrue(status["is_signed_in"])
        self.assertEqual(session.user_status.call_count, 2)


if __name__ == "__main__":
    unittest.main()
