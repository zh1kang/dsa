"""Tests for atomic JSON writes and immutable submission imports."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import tracker


def make_submission(**overrides):
    base = {
        "submission_id": "1001",
        "frontend_id": "1",
        "slug": "two-sum",
        "title": "Two Sum",
        "difficulty": "Easy",
        "tags": ["Array", "Hash Table"],
        "submitted_at": "2025-05-01T10:00:00+00:00",
        "language": "python3",
        "status": "Accepted",
        "code": "# note\nclass Solution: pass\n",
        "raw_comments": ["note"],
        "notes": {},
    }
    base.update(overrides)
    return base


class TestAtomicJson(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def test_write_and_reload(self):
        path = self.root / "data.json"
        tracker.atomic_json_write(path, {"a": 1})
        self.assertEqual(json.loads(path.read_text()), {"a": 1})

    def test_failed_write_keeps_original_and_leaves_no_temp(self):
        path = self.root / "data.json"
        tracker.atomic_json_write(path, {"a": 1})
        with self.assertRaises(TypeError):
            tracker.atomic_json_write(path, {"bad": {1, 2}})
        self.assertEqual(json.loads(path.read_text()), {"a": 1})
        self.assertEqual([p.name for p in self.root.iterdir()], ["data.json"])


class TestImport(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)
        self.data = {"schema_version": 1, "problems": {}}

    def test_import_creates_problem_attempt_and_code_file(self):
        self.assertTrue(tracker.import_submission(self.root, self.data, make_submission()))
        problem = self.data["problems"]["1-two-sum"]
        self.assertEqual(len(problem["attempts"]), 1)
        code_path = self.root / problem["attempts"][0]["code_path"]
        self.assertEqual(code_path, self.root / "solutions" / "1-two-sum" / "1001.py")
        self.assertEqual(code_path.read_text(), make_submission()["code"])
        self.assertEqual(problem["first_solved_at"], "2025-05-01T10:00:00+00:00")

    def test_reimport_is_idempotent(self):
        tracker.import_submission(self.root, self.data, make_submission())
        self.assertFalse(tracker.import_submission(self.root, self.data, make_submission()))
        self.assertEqual(len(self.data["problems"]["1-two-sum"]["attempts"]), 1)

    def test_existing_submission_refreshes_mutable_metadata_not_raw_comments(self):
        tracker.import_submission(self.root, self.data, make_submission())
        changed = tracker.import_submission(self.root, self.data, make_submission(
            runtime="42 ms", memory="18 MB", leetcode_notes="new note",
            raw_comments=["rewritten parser output"], notes={"core_insight": "changed"},
        ))
        attempt = self.data["problems"]["1-two-sum"]["attempts"][0]
        self.assertTrue(changed)
        self.assertEqual(attempt["runtime"], "42 ms")
        self.assertEqual(attempt["leetcode_notes"], "new note")
        self.assertEqual(attempt["raw_comments"], ["note"])
        self.assertEqual(attempt["notes"]["core_insight"], "")

    def test_conflicting_code_for_same_id_is_rejected(self):
        tracker.import_submission(self.root, self.data, make_submission())
        with self.assertRaises(tracker.DataError):
            tracker.import_submission(self.root, self.data,
                                      make_submission(code="print('different')\n"))

    def test_existing_file_with_different_bytes_is_never_overwritten(self):
        target = self.root / "solutions" / "1-two-sum" / "1001.py"
        target.parent.mkdir(parents=True)
        target.write_text("original bytes\n")
        with self.assertRaises(tracker.DataError):
            tracker.import_submission(self.root, self.data, make_submission())
        self.assertEqual(target.read_text(), "original bytes\n")

    def test_nonaccepted_attempts_are_stored_but_do_not_solve(self):
        tracker.import_submission(self.root, self.data,
                                  make_submission(status="Wrong Answer"))
        problem = self.data["problems"]["1-two-sum"]
        self.assertEqual(len(problem["attempts"]), 1)
        self.assertIsNone(problem["first_solved_at"])
        self.assertIsNone(problem["last_solved_at"])

    def test_missing_required_field_is_rejected(self):
        bad = make_submission()
        del bad["code"]
        with self.assertRaises(tracker.DataError):
            tracker.import_submission(self.root, self.data, bad)

    def test_naive_timestamp_is_rejected(self):
        with self.assertRaises(tracker.DataError):
            tracker.import_submission(self.root, self.data,
                                      make_submission(submitted_at="2025-05-01T10:00:00"))

    def test_unsafe_identifiers_are_rejected_before_writing(self):
        for bad in (make_submission(submission_id="../1001"),
                    make_submission(slug="../two-sum"),
                    make_submission(frontend_id="../1")):
            with self.assertRaises(tracker.DataError):
                tracker.import_submission(self.root, self.data, bad)
        self.assertFalse((self.root / "solutions").exists())

    def test_known_submission_ids(self):
        tracker.import_submission(self.root, self.data, make_submission())
        self.assertEqual(tracker.known_submission_ids(self.data), {"1001"})


if __name__ == "__main__":
    unittest.main()
