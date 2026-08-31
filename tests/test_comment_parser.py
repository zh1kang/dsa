"""Tests for exact comment extraction and conservative structured notes."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import comment_parser


class TestPythonComments(unittest.TestCase):
    def test_ordered_hash_comments(self):
        code = "# first\nx = 1  # second\n# third\n"
        self.assertEqual(comment_parser.extract_comments(code, "python3"),
                         ["first", "second", "third"])

    def test_hash_inside_string_is_not_a_comment(self):
        code = 'x = "# not a comment"\ny = 1  # real\n'
        self.assertEqual(comment_parser.extract_comments(code, "python3"), ["real"])

    def test_standalone_triple_string_is_note_like(self):
        code = '"""\nplan: two pointers\n"""\nx = 1\n'
        self.assertEqual(comment_parser.extract_comments(code, "python3"),
                         ["\nplan: two pointers\n"])

    def test_docstring_is_captured(self):
        code = 'def f():\n    """docstring body"""\n    return 1\n'
        self.assertEqual(comment_parser.extract_comments(code, "python3"),
                         ["docstring body"])

    def test_assigned_triple_string_is_not_a_comment(self):
        code = 's = """assigned value"""\n'
        self.assertEqual(comment_parser.extract_comments(code, "python3"), [])

    def test_fstring_prefix_is_not_note_like(self):
        code = 'f"""\ntemplate {x}\n"""\n'
        self.assertEqual(comment_parser.extract_comments(code, "python3"), [])

    def test_exact_body_is_preserved(self):
        code = "# Mistakes: forgot the empty list => IndexError  \n#  intentional indent\n"
        self.assertEqual(comment_parser.extract_comments(code, "python"),
                         ["Mistakes: forgot the empty list => IndexError  ",
                          " intentional indent"])


class TestOtherLanguages(unittest.TestCase):
    def test_c_like_line_and_block(self):
        code = '// line one\nint x = 0; /* block\n * inner line\n */\nchar *s = "// nope";\n'
        self.assertEqual(comment_parser.extract_comments(code, "cpp"),
                         ["line one", "block\n * inner line\n "])

    def test_java_string_protects_markers(self):
        code = 'String s = "/* not a comment */"; // trailing\n'
        self.assertEqual(comment_parser.extract_comments(code, "java"), ["trailing"])

    def test_sql_dash_dash(self):
        code = "-- pick max\nSELECT '--literal' AS c FROM t; -- done\n"
        self.assertEqual(comment_parser.extract_comments(code, "mysql"),
                         ["pick max", "done"])

    def test_sql_doubled_quote_escape(self):
        code = "SELECT 'it''s -- fine' FROM t;\n-- real\n"
        self.assertEqual(comment_parser.extract_comments(code, "mysql"), ["real"])

    def test_shell_hash(self):
        code = '# comment\necho "# not"\n'
        self.assertEqual(comment_parser.extract_comments(code, "bash"), ["comment"])

    def test_unknown_language_returns_empty(self):
        self.assertEqual(comment_parser.extract_comments("# x", "brainfuck"), [])


class TestStructuredNotes(unittest.TestCase):
    def test_labels_map_to_fields(self):
        comments = [
            "thought process: sort then sweep",
            "core insight: overlaps merge when start <= last end",
            "pattern: intervals",
            "mistakes: off by one on the boundary",
            "edge cases: empty input",
            "time complexity: O(n log n)",
            "space: O(1)",
        ]
        notes = comment_parser.parse_structured_notes(comments)
        self.assertEqual(notes["thought_process"], "sort then sweep")
        self.assertEqual(notes["core_insight"], "overlaps merge when start <= last end")
        self.assertEqual(notes["pattern"], "intervals")
        self.assertEqual(notes["mistakes"], "off by one on the boundary")
        self.assertEqual(notes["edge_cases"], "empty input")
        self.assertEqual(notes["time_complexity"], "O(n log n)")
        self.assertEqual(notes["space_complexity"], "O(1)")

    def test_multiline_continuation_within_one_comment(self):
        comments = ["approach: binary search\nshrink the window each step"]
        notes = comment_parser.parse_structured_notes(comments)
        self.assertEqual(notes["thought_process"],
                         "binary search\nshrink the window each step")

    def test_unlabeled_comments_do_not_fill_fields(self):
        notes = comment_parser.parse_structured_notes(["just a stray remark"])
        self.assertTrue(all(value == "" for value in notes.values()))

    def test_all_fields_default_empty(self):
        notes = comment_parser.parse_structured_notes([])
        self.assertEqual(set(notes), set(comment_parser.NOTE_FIELDS))
        self.assertTrue(all(value == "" for value in notes.values()))

    def test_raw_comments_are_not_modified_by_parsing(self):
        comments = ["time complexity: O(n)"]
        before = list(comments)
        comment_parser.parse_structured_notes(comments)
        self.assertEqual(comments, before)


if __name__ == "__main__":
    unittest.main()
