"""Tests for strict GraphQL parsing and the pagination stop helper (no network)."""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import leetcode_api
from leetcode_api import LeetCodeAPIError


def body(data):
    return json.dumps({"data": data})


class TestPayloadParsing(unittest.TestCase):
    def test_http_error_fails_closed(self):
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_graphql_payload(403, "forbidden")

    def test_challenge_html_fails_closed(self):
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_graphql_payload(200, "<html>challenge</html>")

    def test_graphql_errors_fail_closed(self):
        payload = json.dumps({"errors": [{"message": "nope"}], "data": None})
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_graphql_payload(200, payload)

    def test_null_data_fails_closed(self):
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_graphql_payload(200, json.dumps({"data": None}))


class TestShapes(unittest.TestCase):
    def test_user_status(self):
        data = json.loads(body({"userStatus": {
            "userId": 7, "username": "caleb", "isSignedIn": True}}))["data"]
        self.assertEqual(leetcode_api.parse_user_status(data),
                         {"user_id": "7", "username": "caleb", "is_signed_in": True})

    def test_submission_list(self):
        data = {"submissionList": {"hasNext": True, "submissions": [{
            "id": "22", "title": "Two Sum", "titleSlug": "two-sum",
            "statusDisplay": "Accepted", "lang": "python3",
            "timestamp": "1714557600", "runtime": "50 ms", "memory": "17 MB",
        }]}}
        page = leetcode_api.parse_submission_list(data)
        self.assertTrue(page["has_next"])
        self.assertEqual(page["submissions"][0]["submission_id"], "22")
        self.assertEqual(page["submissions"][0]["timestamp"], 1714557600)

    def test_submission_details(self):
        data = {"submissionDetails": {
            "id": 22, "timestamp": 1714557600, "statusDisplay": "Accepted",
            "lang": {"name": "python3", "verboseName": "Python3"},
            "code": "print(1)", "runtime": "50 ms",
            "memory": "17 MB", "notes": "remember dict",
        }}
        details = leetcode_api.parse_submission_details(data)
        self.assertEqual(details["submission_id"], "22")
        self.assertEqual(details["language"], "python3")
        self.assertEqual(details["submitted_at"], "2024-05-01T10:00:00+00:00")
        self.assertEqual(details["runtime"], "50 ms")
        self.assertEqual(details["leetcode_notes"], "remember dict")

    def test_null_details_fails_closed(self):
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_submission_details({"submissionDetails": None})

    def test_missing_code_fails_closed(self):
        data = {"submissionDetails": {
            "id": 22, "timestamp": 1714557600, "statusDisplay": "Accepted",
            "lang": {"name": "python3"}, "code": "",
        }}
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_submission_details(data)

    def test_question(self):
        data = {"question": {
            "questionId": "1", "questionFrontendId": "1", "title": "Two Sum",
            "titleSlug": "two-sum", "difficulty": "Easy",
            "topicTags": [{"name": "Array", "slug": "array"}],
        }}
        question = leetcode_api.parse_question(data)
        self.assertEqual(question["frontend_id"], "1")
        self.assertEqual(question["tags"], ["Array"])

    def test_question_missing_difficulty_fails_closed(self):
        data = {"question": {"questionFrontendId": "1", "title": "t",
                             "titleSlug": "s", "topicTags": []}}
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_question(data)

    def test_scalar_schema_drift_fails_closed(self):
        data = {"question": {
            "questionFrontendId": {"bad": 1}, "title": "Two Sum",
            "titleSlug": "two-sum", "difficulty": "Easy", "topicTags": [],
        }}
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.parse_question(data)


class TestPaginationStop(unittest.TestCase):
    def stub(self, sid):
        return {"submission_id": sid}

    def test_stops_at_first_known_id(self):
        page = [self.stub("30"), self.stub("29"), self.stub("28")]
        fresh, stop = leetcode_api.split_new_submissions(page, {"29", "28"})
        self.assertEqual([s["submission_id"] for s in fresh], ["30"])
        self.assertTrue(stop)

    def test_first_run_never_stops(self):
        page = [self.stub("30"), self.stub("29")]
        fresh, stop = leetcode_api.split_new_submissions(page, set())
        self.assertEqual(len(fresh), 2)
        self.assertFalse(stop)

    def test_epoch_validation(self):
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.epoch_to_iso(None)
        with self.assertRaises(LeetCodeAPIError):
            leetcode_api.epoch_to_iso(0)


if __name__ == "__main__":
    unittest.main()
