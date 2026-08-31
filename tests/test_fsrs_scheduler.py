"""Tests for deterministic FSRS replay, new-card policy, and sorted schedules."""
import sys
import tempfile
import unittest
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import fsrs_scheduler
import tracker

NOW = datetime(2025, 6, 1, 12, 0, tzinfo=timezone.utc)


def submission(sid, frontend_id, slug, title, submitted_at, status="Accepted"):
    return {
        "submission_id": sid, "frontend_id": frontend_id, "slug": slug,
        "title": title, "difficulty": "Easy", "tags": ["Array"],
        "submitted_at": submitted_at, "language": "python3", "status": status,
        "code": f"# solution {sid}\n", "raw_comments": [f"solution {sid}"], "notes": {},
    }


def event(key, grade, reviewed_at):
    return {"problem": key, "grade": grade.title(), "reviewed_at": reviewed_at}


class SchedulerBase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.data = {"schema_version": 2, "problems": {}}
        tracker.import_submission(self.root, self.data, submission(
            "1001", "1", "two-sum", "Two Sum", "2025-05-01T10:00:00+00:00"))
        tracker.import_submission(self.root, self.data, submission(
            "2002", "206", "reverse-linked-list", "Reverse Linked List",
            "2025-05-10T10:00:00+00:00"))


class TestNewCardPolicy(SchedulerBase):
    def test_unrated_accepted_problem_is_new_and_due_at_last_accept(self):
        reviews = fsrs_scheduler.compute_reviews(self.data, [], 0.9, NOW)
        review = reviews["1-two-sum"]
        self.assertEqual(review["state"], "new")
        self.assertIsNone(review["stability"])
        self.assertIsNone(review["difficulty"])
        self.assertIsNone(review["retrievability"])
        self.assertIsNone(review["last_review"])
        self.assertEqual(review["reps"], 0)
        self.assertEqual(review["lapses"], 0)
        self.assertEqual(review["next_review"], "2025-05-01T10:00:00+00:00")

    def test_next_review_tracks_most_recent_accept(self):
        tracker.import_submission(self.root, self.data, submission(
            "1005", "1", "two-sum", "Two Sum", "2025-05-20T09:00:00+00:00"))
        reviews = fsrs_scheduler.compute_reviews(self.data, [], 0.9, NOW)
        self.assertEqual(reviews["1-two-sum"]["next_review"], "2025-05-20T09:00:00+00:00")

    def test_problem_without_accept_or_events_has_no_card(self):
        tracker.import_submission(self.root, self.data, submission(
            "3003", "42", "trapping-rain-water", "Trapping Rain Water",
            "2025-05-11T10:00:00+00:00", status="Wrong Answer"))
        reviews = fsrs_scheduler.compute_reviews(self.data, [], 0.9, NOW)
        self.assertNotIn("42-trapping-rain-water", reviews)

    def test_tracking_cutoff_excludes_older_accepted_problems(self):
        reviews = fsrs_scheduler.compute_reviews(
            self.data,
            [],
            0.9,
            NOW,
            tracking_start_date=date(2025, 5, 15),
            local_timezone=timezone.utc,
        )
        self.assertEqual(reviews, {})

        tracker.import_submission(self.root, self.data, submission(
            "1005", "1", "two-sum", "Two Sum", "2025-05-15T09:00:00+00:00"
        ))
        reviews = fsrs_scheduler.compute_reviews(
            self.data,
            [],
            0.9,
            NOW,
            tracking_start_date=date(2025, 5, 15),
            local_timezone=timezone.utc,
        )
        self.assertEqual(set(reviews), {"1-two-sum"})
        self.assertEqual(
            reviews["1-two-sum"]["next_review"],
            "2025-05-15T09:00:00+00:00",
        )


class TestReplay(SchedulerBase):
    def test_tracking_cutoff_replays_only_current_events(self):
        events = [
            event("1-two-sum", "good", "2025-05-02T10:00:00+00:00"),
            event("1-two-sum", "hard", "2025-05-20T10:00:00+00:00"),
        ]
        review = fsrs_scheduler.compute_reviews(
            self.data,
            events,
            0.9,
            NOW,
            tracking_start_date=date(2025, 5, 15),
            local_timezone=timezone.utc,
        )["1-two-sum"]
        self.assertEqual(review["reps"], 1)
        self.assertEqual(review["last_review"], "2025-05-20T10:00:00+00:00")

    def test_replay_is_event_only(self):
        events = [event("1-two-sum", "good", "2025-05-02T10:00:00+00:00")]
        before = fsrs_scheduler.compute_reviews(self.data, events, 0.9, NOW)
        # New accepted attempts must not change FSRS state without a rating.
        tracker.import_submission(self.root, self.data, submission(
            "1009", "1", "two-sum", "Two Sum", "2025-05-25T10:00:00+00:00"))
        after = fsrs_scheduler.compute_reviews(self.data, events, 0.9, NOW)
        self.assertEqual(before["1-two-sum"], after["1-two-sum"])

    def test_replay_is_deterministic(self):
        events = [
            event("1-two-sum", "good", "2025-05-02T10:00:00+00:00"),
            event("1-two-sum", "again", "2025-05-08T10:00:00+00:00"),
            event("1-two-sum", "easy", "2025-05-09T10:00:00+00:00"),
        ]
        first = fsrs_scheduler.compute_reviews(self.data, events, 0.9, NOW)
        second = fsrs_scheduler.compute_reviews(self.data, events, 0.9, NOW)
        self.assertEqual(first, second)

    def test_rated_card_has_full_metrics_and_lapse_count(self):
        events = [
            event("1-two-sum", "good", "2025-05-02T10:00:00+00:00"),
            event("1-two-sum", "again", "2025-05-08T10:00:00+00:00"),
        ]
        review = fsrs_scheduler.compute_reviews(self.data, events, 0.9, NOW)["1-two-sum"]
        self.assertEqual(review["reps"], 2)
        self.assertEqual(review["lapses"], 1)
        self.assertIsNotNone(review["stability"])
        self.assertIsNotNone(review["difficulty"])
        self.assertIsNotNone(review["retrievability"])
        self.assertEqual(review["last_review"], "2025-05-08T10:00:00+00:00")
        self.assertGreater(review["next_review"], review["last_review"])

    def test_deterministic_card_ids(self):
        self.assertEqual(fsrs_scheduler.deterministic_card_id("1-two-sum"),
                         fsrs_scheduler.deterministic_card_id("1-two-sum"))
        self.assertNotEqual(fsrs_scheduler.deterministic_card_id("1-two-sum"),
                            fsrs_scheduler.deterministic_card_id("2-add-two-numbers"))


class TestSchedule(SchedulerBase):
    def test_schedule_is_sorted_by_next_review(self):
        events = [event("206-reverse-linked-list", "easy", "2025-05-11T10:00:00+00:00")]
        reviews = fsrs_scheduler.compute_reviews(self.data, events, 0.9, NOW)
        schedule = fsrs_scheduler.build_schedule(
            self.root, self.data, events, reviews, 0.9, NOW, timezone.utc
        )
        ordered = [entry["next_review"] for entry in schedule["problems"]]
        self.assertEqual(ordered, sorted(ordered))
        self.assertEqual(schedule["problems"][0]["problem_id"], "1-two-sum")

    def test_schedule_entries_carry_reminder_payload(self):
        reviews = fsrs_scheduler.compute_reviews(self.data, [], 0.9, NOW)
        schedule = fsrs_scheduler.build_schedule(
            self.root, self.data, [], reviews, 0.9, NOW, timezone.utc
        )
        entry = next(e for e in schedule["problems"] if e["problem_id"] == "1-two-sum")
        self.assertEqual(entry["leetcode_url"], "https://leetcode.com/problems/two-sum/")
        self.assertEqual(entry["difficulty"], "Easy")
        self.assertEqual(entry["tags"], ["Array"])
        self.assertEqual(entry["latest_solution"], "1-two-sum.py")
        self.assertEqual(entry["raw_comments"], ["solution 1001"])
        self.assertEqual(entry["next_review"], "2025-05-01")
        self.assertNotIn("code", entry)

    def test_fsrs_metadata_block(self):
        schedule = fsrs_scheduler.build_schedule(
            self.root, self.data, [], {}, 0.9, NOW, timezone.utc
        )
        self.assertEqual(schedule["fsrs"]["algorithm"], "FSRS-6")
        self.assertEqual(schedule["fsrs"]["package_version"], "6.3.2")
        self.assertEqual(schedule["fsrs"]["learning_steps"], [])
        self.assertFalse(schedule["fsrs"]["fuzzing"])


class TestLogValidation(SchedulerBase):
    def known(self):
        return set(self.data["problems"])

    def test_valid_log_passes(self):
        events = [event("1-two-sum", "good", "2025-05-02T10:00:00+00:00")]
        self.assertEqual(fsrs_scheduler.validate_review_log(events, self.known()), events)

    def test_unknown_problem_is_rejected(self):
        events = [event("9-nope", "good", "2025-05-02T10:00:00+00:00")]
        with self.assertRaises(tracker.DataError):
            fsrs_scheduler.validate_review_log(events, self.known())

    def test_invalid_rating_is_rejected(self):
        events = [{"problem": "1-two-sum", "grade": "OK", "reviewed_at": "2025-05-02T10:00:00+00:00"}]
        with self.assertRaises(tracker.DataError):
            fsrs_scheduler.validate_review_log(events, self.known())

    def test_duplicate_timestamp_is_rejected(self):
        events = [event("1-two-sum", "good", "2025-05-02T10:00:00+00:00"),
                  event("1-two-sum", "easy", "2025-05-02T10:00:00+00:00")]
        with self.assertRaises(tracker.DataError):
            fsrs_scheduler.validate_review_log(events, self.known())

    def test_out_of_order_is_rejected(self):
        events = [event("1-two-sum", "good", "2025-05-03T10:00:00+00:00"),
                  event("1-two-sum", "easy", "2025-05-02T10:00:00+00:00")]
        with self.assertRaises(tracker.DataError):
            fsrs_scheduler.validate_review_log(events, self.known())

    def test_naive_timestamp_is_rejected(self):
        events = [event("1-two-sum", "good", "2025-05-02T10:00:00")]
        with self.assertRaises(tracker.DataError):
            fsrs_scheduler.validate_review_log(events, self.known())

    def test_invalid_optionals_are_rejected(self):
        base = event("1-two-sum", "good", "2025-05-02T10:00:00+00:00")
        for bad in ({"elapsed_minutes": -1}, {"hints_used": -2}, {"notes": 5},
                    {"failure_stage": 3},
                    {"solved_without_help": "yes"}):
            with self.assertRaises(tracker.DataError):
                fsrs_scheduler.validate_review_log([{**base, **bad}], self.known())


if __name__ == "__main__":
    unittest.main()
