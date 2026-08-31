"""Tests for non-secret configuration validation."""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import config


def write_config(
    path: Path,
    problems: str = "Problems",
    submissions: str = "Submissions",
    reviews: str = "Reviews",
) -> None:
    path.write_text(f"""
[leetcode]
browser_profile = ".dsa/browser"
request_delay_seconds = 1.0

[tracker]
timezone = "America/New_York"
tracking_start_date = "2026-08-31"

[fsrs]
desired_retention = 0.9

[git]
auto_push = false

[google_sheets]
problems_worksheet = "{problems}"
submissions_worksheet = "{submissions}"
reviews_worksheet = "{reviews}"
github_repository = "zh1kang/dsa"
""")


class TestGoogleSheetNames(unittest.TestCase):
    def test_worksheet_names_must_be_different(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.toml"
            write_config(path, "Problems", "Problems", "Reviews")
            with self.assertRaises(ValueError):
                config.load_config(path)

    def test_worksheet_names_are_trimmed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.toml"
            write_config(path, " Problems ", " Submissions ", " Reviews ")
            loaded = config.load_config(path)
            self.assertEqual(loaded.problems_worksheet, "Problems")
            self.assertEqual(loaded.submissions_worksheet, "Submissions")
            self.assertEqual(loaded.reviews_worksheet, "Reviews")
            self.assertEqual(loaded.github_repository, "zh1kang/dsa")
            self.assertEqual(loaded.tracking_start_date.isoformat(), "2026-08-31")
            root = Path(directory).resolve()
            self.assertEqual(loaded.browser_profile, root / ".dsa/browser")
            self.assertEqual(
                loaded.google_credentials_file,
                root / ".dsa/google/client_secret.json",
            )

    def test_runtime_state_must_stay_in_dsa_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.toml"
            write_config(path)
            text = path.read_text().replace(
                'browser_profile = ".dsa/browser"',
                'browser_profile = "~/.old-dsa/browser"',
            )
            path.write_text(text)
            with self.assertRaises(ValueError):
                config.load_config(path)

    def test_tracking_start_date_must_be_iso_date(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "config.toml"
            write_config(path)
            path.write_text(path.read_text().replace("2026-08-31", "08/31/2026"))
            with self.assertRaises(ValueError):
                config.load_config(path)


if __name__ == "__main__":
    unittest.main()
