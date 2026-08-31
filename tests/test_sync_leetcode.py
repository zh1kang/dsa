"""Network-free tests for incremental sync orchestration."""
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import leetcode_api
import sync_leetcode
import tracker


class PagingSession:
    def __init__(self):
        self.calls = []

    def graphql(self, query, variables):
        self.calls.append((query, variables))
        if variables["offset"] == 0:
            return {"submissionList": {"hasNext": True, "submissions": [
                {"id": "30", "title": "Two Sum", "titleSlug": "two-sum",
                 "statusDisplay": "Accepted", "lang": "python3", "timestamp": 30,
                 "runtime": "1 ms", "memory": "1 MB"},
                {"id": "29", "title": "Two Sum", "titleSlug": "two-sum",
                 "statusDisplay": "Wrong Answer", "lang": "python3", "timestamp": 29,
                 "runtime": None, "memory": None},
            ]}}
        return {"submissionList": {"hasNext": True, "submissions": [
            {"id": "28", "title": "Old", "titleSlug": "old",
             "statusDisplay": "Accepted", "lang": "cpp", "timestamp": 28,
             "runtime": "2 ms", "memory": "2 MB"}
        ]}}


class DetailSession:
    def __init__(self):
        self.question_calls = 0

    def graphql(self, query, variables):
        if query == leetcode_api.SUBMISSION_DETAILS_QUERY:
            sid = variables["submissionId"]
            return {"submissionDetails": {
                "id": sid, "timestamp": 1714557600 + sid,
                "statusDisplay": "Accepted", "lang": {"name": "python3"},
                "code": f"# core insight: use a map\nprint({sid})\n",
                "runtime": "1 ms", "memory": "10 MB", "notes": "keep it simple",
            }}
        self.question_calls += 1
        return {"question": {
            "questionId": "1", "questionFrontendId": "1", "title": "Two Sum",
            "titleSlug": "two-sum", "difficulty": "Easy",
            "topicTags": [{"name": "Array", "slug": "array"}],
        }}


class TestIncrementalPaging(unittest.TestCase):
    def test_pages_until_first_known_submission(self):
        session = PagingSession()
        stubs = sync_leetcode.collect_sync_stubs(session, {"28"})
        self.assertEqual([stub["submission_id"] for stub in stubs], ["30", "29", "28"])
        self.assertEqual([call[1]["offset"] for call in session.calls], [0, 2])
        self.assertTrue(all(call[1]["slug"] is None for call in session.calls))

    def test_duplicate_across_pages_fails_closed(self):
        session = PagingSession()
        original = session.graphql
        def repeated(query, variables):
            if variables["offset"] == 0:
                return original(query, variables)
            return {"submissionList": {"hasNext": False, "submissions": [
                {"id": "30", "title": "Two Sum", "titleSlug": "two-sum",
                 "statusDisplay": "Accepted", "lang": "python3", "timestamp": 30,
                 "runtime": "1 ms", "memory": "1 MB"}
            ]}}
        session.graphql = repeated
        with self.assertRaises(leetcode_api.LeetCodeAPIError):
            sync_leetcode.collect_sync_stubs(session, set())

    def test_empty_nonterminal_page_fails_closed(self):
        session = SimpleNamespace(graphql=lambda query, variables: {
            "submissionList": {"hasNext": True, "submissions": []}
        })
        with self.assertRaises(leetcode_api.LeetCodeAPIError):
            sync_leetcode.collect_sync_stubs(session, set())

    def test_first_run_reaches_has_next_false(self):
        session = PagingSession()
        # Make the second page terminal rather than known.
        original = session.graphql
        session.graphql = lambda query, variables: (
            {**original(query, variables), "submissionList": {
                **original(query, variables)["submissionList"], "hasNext": False}}
            if variables["offset"] else original(query, variables)
        )
        stubs = sync_leetcode.collect_sync_stubs(session, set())
        self.assertEqual([stub["submission_id"] for stub in stubs], ["30", "29", "28"])


class TestBatchImport(unittest.TestCase):
    def test_later_validation_failure_removes_earlier_new_source(self):
        import tempfile
        base = {
            "submission_id": "1", "frontend_id": "1", "slug": "two-sum",
            "title": "Two Sum", "difficulty": "Easy", "tags": ["Array"],
            "submitted_at": "2025-01-01T00:00:00+00:00", "language": "python3",
            "status": "Accepted", "code": "# note\n", "raw_comments": ["note"],
            "notes": {},
        }
        bad = {**base, "submission_id": "2", "frontend_id": "2",
               "slug": "bad", "difficulty": "Unknown"}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = {"schema_version": 2, "problems": {}}
            with self.assertRaises(Exception):
                sync_leetcode.import_submissions(root, data, [base, bad])
            self.assertFalse((root / "1-two-sum.py").exists())
            self.assertEqual(data["problems"], {})

    def test_later_failure_restores_an_existing_flat_file(self):
        import tempfile
        first = {
            "submission_id": "1", "frontend_id": "1", "slug": "two-sum",
            "title": "Two Sum", "difficulty": "Easy", "tags": ["Array"],
            "submitted_at": "2025-01-01T00:00:00+00:00", "language": "python3",
            "status": "Accepted", "code": "# first\n", "raw_comments": ["first"],
            "notes": {},
        }
        second = {**first, "submission_id": "2",
                  "submitted_at": "2025-01-02T00:00:00+00:00", "code": "# second\n"}
        bad = {**first, "submission_id": "3", "frontend_id": "3",
               "slug": "bad", "difficulty": "Unknown"}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            data = {"schema_version": 2, "problems": {}}
            tracker.import_submission(root, data, first)
            before = (root / "1-two-sum.py").read_bytes()
            with self.assertRaises(Exception):
                sync_leetcode.import_submissions(root, data, [second, bad])
            self.assertEqual((root / "1-two-sum.py").read_bytes(), before)
            self.assertEqual(len(data["problems"]["1-two-sum"]["attempts"]), 1)


class TestAccountBinding(unittest.TestCase):
    def test_account_is_pinned_locally_and_mismatch_is_rejected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "account.json"
            config = SimpleNamespace(account_file=path)
            sync_leetcode.bind_local_account(
                config, {"user_id": "7", "username": "caleb", "is_signed_in": True}
            )
            self.assertEqual(path.stat().st_mode & 0o777, 0o600)
            with self.assertRaises(leetcode_api.LeetCodeAPIError):
                sync_leetcode.bind_local_account(
                    config, {"user_id": "8", "username": "other", "is_signed_in": True}
                )


class TestDetailFetch(unittest.TestCase):
    def test_details_are_oldest_first_and_question_metadata_is_cached(self):
        session = DetailSession()
        stubs = [
            {"submission_id": "31", "title_slug": "two-sum",
             "runtime": "31 ms", "memory": "31 MB"},
            {"submission_id": "30", "title_slug": "two-sum",
             "runtime": "30 ms", "memory": "30 MB"},
        ]
        results = sync_leetcode.fetch_submissions(session, stubs)
        self.assertEqual([item["submission_id"] for item in results], ["30", "31"])
        self.assertEqual(session.question_calls, 1)
        self.assertEqual(results[0]["runtime"], "30 ms")
        self.assertEqual(results[0]["memory"], "30 MB")
        self.assertEqual(results[0]["raw_comments"], ["core insight: use a map"])
        self.assertEqual(results[0]["notes"]["core_insight"], "use a map")
        self.assertEqual(results[0]["leetcode_notes"], "keep it simple")

    def test_divergence_notes_are_scraped_from_ordered_comments(self):
        session = DetailSession()
        original = session.graphql

        def graphql(query, variables):
            response = original(query, variables)
            if query == leetcode_api.SUBMISSION_DETAILS_QUERY:
                response["submissionDetails"]["code"] = (
                    "# try a hash map\n"
                    "class Solution: pass\n"
                    "# divergences:\n"
                    "# forgot duplicate values\n"
                )
            return response

        session.graphql = graphql
        result = sync_leetcode.fetch_submissions(session, [{
            "submission_id": "30", "title_slug": "two-sum",
            "runtime": "30 ms", "memory": "30 MB",
        }])[0]
        self.assertEqual(result["notes"]["thought_process"], "try a hash map")
        self.assertEqual(result["notes"]["notes"], "forgot duplicate values")


if __name__ == "__main__":
    unittest.main()
