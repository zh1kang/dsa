"""Tests for Chrome-owned LeetCode browser sessions."""
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import leetcode_browser


class TestChromeCommand(unittest.TestCase):
    def test_uses_direct_chrome_with_local_debugging(self):
        command = leetcode_browser.chrome_command(
            Path("/Applications/Google Chrome"),
            Path("/tmp/tracker-browser"),
            leetcode_browser.BASE_URL,
            debugging_port=9222,
            headless=True,
        )

        self.assertIn("--remote-debugging-address=127.0.0.1", command)
        self.assertIn("--remote-debugging-port=9222", command)
        self.assertIn("--headless=new", command)
        self.assertFalse(any("mock-keychain" in argument for argument in command))
        self.assertFalse(any("enable-automation" in argument for argument in command))


class TestSessionCookie(unittest.TestCase):
    def test_detects_session_without_reading_cookie_value(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory)
            database = profile / "Default" / "Cookies"
            database.parent.mkdir(parents=True)
            with sqlite3.connect(database) as connection:
                connection.execute(
                    "CREATE TABLE cookies (host_key TEXT, name TEXT, encrypted_value BLOB)"
                )
                connection.execute(
                    "INSERT INTO cookies VALUES (?, ?, ?)",
                    (".leetcode.com", "LEETCODE_SESSION", b"secret bytes"),
                )

            self.assertTrue(leetcode_browser.has_leetcode_session(profile))

    def test_rejects_unrelated_cookies(self):
        with tempfile.TemporaryDirectory() as directory:
            profile = Path(directory)
            database = profile / "Default" / "Cookies"
            database.parent.mkdir(parents=True)
            with sqlite3.connect(database) as connection:
                connection.execute("CREATE TABLE cookies (host_key TEXT, name TEXT)")
                connection.execute(
                    "INSERT INTO cookies VALUES (?, ?)",
                    ("leetcode.com", "csrftoken"),
                )

            self.assertFalse(leetcode_browser.has_leetcode_session(profile))


class TestInteractiveLogin(unittest.TestCase):
    def test_stops_owned_chrome_after_session_is_saved(self):
        process = Mock()
        config = SimpleNamespace(browser_profile=Path("/tmp/tracker-browser"))

        with (
            patch("leetcode_browser.launch_chrome", return_value=process),
            patch("leetcode_browser.has_leetcode_session", return_value=True),
            patch("leetcode_browser.stop_chrome") as stop_chrome,
            patch("leetcode_browser.time.monotonic", side_effect=[0, 1]),
        ):
            leetcode_browser.login_interactively(config)

        stop_chrome.assert_called_once_with(process)

    def test_stops_owned_chrome_when_browser_closes_before_login(self):
        process = Mock()
        process.poll.return_value = 0
        config = SimpleNamespace(browser_profile=Path("/tmp/tracker-browser"))

        with (
            patch("leetcode_browser.launch_chrome", return_value=process),
            patch("leetcode_browser.has_leetcode_session", return_value=False),
            patch("leetcode_browser.stop_chrome") as stop_chrome,
            patch("leetcode_browser.time.monotonic", side_effect=[0, 1]),
            self.assertRaises(leetcode_browser.LeetCodeAPIError),
        ):
            leetcode_browser.login_interactively(config)

        stop_chrome.assert_called_once_with(process)


class TestBrowserFetch(unittest.TestCase):
    def test_retries_one_read_after_page_navigation(self):
        config = SimpleNamespace(request_delay_seconds=1)
        session = leetcode_browser.LeetCodeSession(config)
        session.page = Mock()
        session.page.evaluate.side_effect = [
            leetcode_browser.PlaywrightError("Execution context was destroyed"),
            {"status": 200, "body": json.dumps({"data": {"ok": True}})},
        ]

        with patch("leetcode_browser.time.sleep"):
            data = session.graphql("query test { ok }", {})

        self.assertEqual(data, {"ok": True})
        session.page.goto.assert_called_once_with(
            leetcode_browser.BASE_URL, wait_until="domcontentloaded"
        )

    def test_does_not_retry_other_browser_errors(self):
        config = SimpleNamespace(request_delay_seconds=1)
        session = leetcode_browser.LeetCodeSession(config)
        session.page = Mock()
        session.page.evaluate.side_effect = leetcode_browser.PlaywrightError("Target closed")

        with (
            patch("leetcode_browser.time.sleep"),
            self.assertRaises(leetcode_browser.LeetCodeAPIError),
        ):
            session.graphql("query test { ok }", {})

        self.assertEqual(session.page.evaluate.call_count, 1)

if __name__ == "__main__":
    unittest.main()
