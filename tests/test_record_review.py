"""Tests for identifier resolution and review event construction."""
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import record_review
import tracker

DATA = {"schema_version": 1, "problems": {
    "1-two-sum": {"leetcode_id": "1", "slug": "two-sum",
                  "attempts": [{"status": "Accepted"}]},
    "206-reverse-linked-list": {"leetcode_id": "206", "slug": "reverse-linked-list",
                                "attempts": [{"status": "Accepted"}]},
}}
NOW = datetime(2025, 6, 1, 12, 0, tzinfo=timezone.utc)


class TestResolve(unittest.TestCase):
    def test_resolve_by_number(self):
        self.assertEqual(record_review.resolve_problem(DATA, "1"), "1-two-sum")

    def test_resolve_by_slug(self):
        self.assertEqual(record_review.resolve_problem(DATA, "reverse-linked-list"),
                         "206-reverse-linked-list")

    def test_resolve_by_canonical_id(self):
        self.assertEqual(record_review.resolve_problem(DATA, "1-two-sum"), "1-two-sum")

    def test_unknown_identifier_is_rejected(self):
        with self.assertRaises(tracker.DataError):
            record_review.resolve_problem(DATA, "999")

    def test_problem_without_accepted_submission_is_rejected(self):
        data = {"schema_version": 1, "problems": {
            "2-add-two-numbers": {"leetcode_id": "2", "slug": "add-two-numbers",
                                  "attempts": [{"status": "Wrong Answer"}]}
        }}
        with self.assertRaises(tracker.DataError):
            record_review.resolve_problem(data, "2")


class TestBuildEvent(unittest.TestCase):
    def test_event_shape(self):
        event = record_review.build_event("1-two-sum", "good", NOW, 12.5, 0, "smooth")
        self.assertEqual(event["problem"], "1-two-sum")
        self.assertEqual(event["grade"], "Good")
        self.assertEqual(event["reviewed_at"], "2025-06-01T12:00:00+00:00")
        self.assertEqual(event["elapsed_minutes"], 12.5)
        self.assertEqual(event["notes"], "smooth")
        self.assertTrue(event["solved_without_help"])

    def test_hints_disable_solved_without_help(self):
        event = record_review.build_event("1-two-sum", "good", NOW, None, 2, None)
        self.assertFalse(event["solved_without_help"])

    def test_again_disables_solved_without_help(self):
        event = record_review.build_event("1-two-sum", "again", NOW, None, None, None)
        self.assertFalse(event["solved_without_help"])

    def test_invalid_rating_is_rejected(self):
        with self.assertRaises(tracker.DataError):
            record_review.build_event("1-two-sum", "meh", NOW, None, None, None)

    def test_naive_time_is_rejected(self):
        with self.assertRaises(tracker.DataError):
            record_review.build_event("1-two-sum", "good",
                                      datetime(2025, 6, 1, 12, 0), None, None, None)


if __name__ == "__main__":
    unittest.main()
