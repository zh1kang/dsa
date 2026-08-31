# LeetCode Tracker

A small, local-first LeetCode practice tracker:

```text
LeetCode → local Playwright sync → Git/GitHub → GitHub Actions → FSRS
         → review-schedule.json → ChatGPT/Codex reminder
```

There is no browser extension, backend, hosted database, or LeetCode secret in
GitHub. You solve on LeetCode as usual. A local browser profile reads your own
submission history, preserves every exact source file and comment, and pushes
the resulting files to your repository.

## What is stored

- `tracker.json` — canonical problem and complete attempt history.
- `solutions/<number>-<slug>/<submission-id>.<ext>` — exact submitted source.
- `solutions/<number>-<slug>/metadata.json` — convenient per-problem copy.
- `review-log.json` — append-only explicit review grades; scheduling truth.
- `review-schedule.json` — compact derived FSRS schedule for reminders.
- `google-sheets.csv` — one accepted attempt per row, with clean note columns.

Submission IDs are immutable keys. A repeat sync is idempotent. Existing source
is never overwritten; a byte mismatch stops the sync loudly. Non-accepted
attempts are preserved, but only accepted problems become review cards.

## Initial setup

Create or clone the GitHub repository, then:

```bash
git clone git@github.com:zh1kang/dsa.git
cd dsa
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/playwright install chromium
git add .
git commit -m "chore: initialize LeetCode tracker"
git push -u origin main
```

Edit only non-secret settings in `config.toml`:

```toml
[leetcode]
browser_profile = "~/.leetcode-tracker/browser"
account_file = "~/.leetcode-tracker/account.json"
request_delay_seconds = 1.0

[tracker]
timezone = "America/New_York"

[fsrs]
desired_retention = 0.90

[git]
auto_push = true
```

The browser profile and local account pin are intentionally outside the
repository. The first successful login writes only the account ID/username to
`account_file`; later runs reject a different logged-in account instead of
mixing datasets. Do not move the profile into Git, copy it to GitHub Actions,
or share it: it contains bearer-equivalent LeetCode authentication state.

### First login

```bash
.venv/bin/python scripts/sync_leetcode.py
```

When no profile exists, Chromium opens automatically. Log into LeetCode using
the normal page (including 2FA or Cloudflare if shown). The script waits for a
valid signed-in session and then imports the full available history slowly.
Future runs reuse that profile headlessly.

If a profile exists but you need to see the browser:

```bash
.venv/bin/python scripts/sync_leetcode.py --show-browser
```

## Daily use

Manual synchronization:

```bash
.venv/bin/python scripts/sync_leetcode.py
```

The script requires a clean tracked worktree, fast-forwards from its upstream,
imports unseen IDs, refreshes the first known boundary submission for changed
LeetCode notes/metrics/status, writes atomically, and commits as:

```text
leetcode: sync 3 new submissions
```

and pushes when `git.auto_push = true`. No new or changed submission means no commit.
Use `--no-push` to skip both pull and push. A failed push is an error, but the
local files and commit remain available for recovery.

### Codex automation

Run the first interactive login manually. Then configure the Codex automation
with this repository as its working directory and this command:

```bash
.venv/bin/python scripts/sync_leetcode.py
```

The automation needs normal local filesystem access to the configured browser
profile and your existing Git credentials. It needs no LeetCode username,
password, cookie, or environment variable.

### macOS `launchd` alternative

The included plist targets `/Users/caleb/Desktop/dsa`. If the repository moves,
update its absolute paths before installing it:

```bash
mkdir -p ~/.leetcode-tracker/logs
cp launchd/com.leetcode-tracker.sync.plist.example \
  ~/Library/LaunchAgents/com.leetcode-tracker.sync.plist
launchctl bootstrap gui/$(id -u) \
  ~/Library/LaunchAgents/com.leetcode-tracker.sync.plist
```

It runs at about 8:30 PM and writes local logs. The plist contains no secrets
and calls the virtual environment directly, so no shell activation is needed.

## Source comments and notes

The source file is always the authoritative, exact submission. In addition,
`raw_comments` retains ordered comment bodies from:

- Python `#` comments and standalone triple-quoted note/docstring text;
- C-family `//` and `/* ... */` comments;
- SQL `--` and `/* ... */` comments;
- shell/Ruby-style `#` comments.

Structured notes are conservative. They are populated only when your comment
uses an explicit label; unlabeled thoughts remain in `raw_comments` and are
never guessed or summarized:

```python
# thought process: start from every zero
# core insight: multi-source BFS assigns shortest distances in one traversal
# pattern: multi-source BFS
# mistakes: forgot to mark initial zero cells visited
# edge cases: all cells are zero
# time complexity: O(rows * cols)
# space complexity: O(rows * cols)
```

Supported fields are `thought_process`, `core_insight`, `pattern`, `mistakes`,
`edge_cases`, `time_complexity`, and `space_complexity`. An LLM enrichment step
can be added later without replacing the original source or `raw_comments`.

## Recording a review

After a reminder, redo the problem on LeetCode first. Then explicitly grade the
review:

```bash
.venv/bin/python scripts/record_review.py 542 good
.venv/bin/python scripts/record_review.py 542-01-matrix good \
  --minutes 12 --hints 0 \
  --notes "Remembered initialization; briefly forgot visited handling"
.venv/bin/python scripts/record_review.py 01-matrix hard
```

The identifier may be the number, canonical ID, or slug. Grades mean:

- **Again** — could not solve; major conceptual failure or looked it up.
- **Hard** — solved with substantial struggle or a meaningful hint.
- **Good** — solved independently with normal effort and remembered the pattern.
- **Easy** — immediate recognition, clean implementation, easy to explain.

Only this command adds an FSRS event. An Accepted submission never implies a
grade. The command appends an event, regenerates derived files, commits, and
pushes unless `--no-push` is supplied.

Force a derived-state rebuild at any time:

```bash
.venv/bin/python scripts/update_review_schedule.py
```

## FSRS policy

This project pins `fsrs==6.3.2` (FSRS-6), uses desired retention `0.90`, disables
fuzzing, and uses no intraday learning/relearning steps. Replay is deterministic
for the pinned package, settings, and event timestamps.

Historical accepted problems with no explicit grades are **new cards**. Their
`stability`, FSRS `difficulty`, and `retrievability` remain `null`; `reps` and
`lapses` remain zero. Their deterministic `next_review` is the local calendar
date of the most recent Accepted submission. No historical grade is fabricated.

`review-log.json` is truth. `tracker.json` review fields and
`review-schedule.json` are replaceable derived state.

## ChatGPT reminder contract

`review-schedule.json` is sorted by `next_review`. Every entry exposes the due
date and reminder context at the top level: title, URL, difficulty, tags,
`last_grade`, FSRS metrics, latest source path, raw comments, and structured
notes. It deliberately does **not** embed the old source code.

Due problems require only a date comparison:

```bash
today=$(TZ=America/New_York date +%F)
jq --arg today "$today" '.problems | map(select(.next_review <= $today))' \
  review-schedule.json
```

A ChatGPT automation can read each result and say, for example:

```text
Redo: 01 Matrix
Pattern: Multi-source BFS
Difficulty: Medium
Last result: Good
Due: Today

Your previous insight:
Start BFS simultaneously from every zero.

Do not open your old solution until you have tried it yourself.
https://leetcode.com/problems/01-matrix/
```

The external reminder never needs to run FSRS.

## Google Sheets note mirror

`google-sheets.csv` is always generated and can be imported directly. It has
one accepted attempt per row and separate columns for LeetCode notes,
newline-separated raw source comments, every structured note, metadata, source
path, URL, and review state. CSV multiline quoting is standards-compliant.
Potential formula prefixes (`=`, `+`, `-`, `@`) are neutralized with an
apostrophe; exact source and raw JSON remain unchanged in Git.

Optional automatic upload uses local Google Desktop OAuth:

1. In Google Cloud, enable the Google Sheets API.
2. Create an **OAuth client ID → Desktop app** and download its JSON to
   `~/.leetcode-tracker/google/client_secret.json`.
3. Put the target spreadsheet ID and worksheet name in `config.toml`.
4. Run a sync once and complete Google's local consent flow. The refresh token
   is saved to `~/.leetcode-tracker/google/token.json`.

```toml
[google_sheets]
spreadsheet_id = "ID_FROM_THE_SHEET_URL"
worksheet = "LeetCode"
credentials_file = "~/.leetcode-tracker/google/client_secret.json"
token_file = "~/.leetcode-tracker/google/token.json"
```

The client requests only the `spreadsheets` scope and writes values as `RAW`.
Both credential files remain local and are ignored by Git. GitHub Actions does
not upload to Sheets and never receives Google or LeetCode authentication.

## Reauthenticate safely

This deletes **only** the configured local Playwright profile, not tracker data:

```bash
.venv/bin/python scripts/sync_leetcode.py --reauth
```

The browser then opens for a normal login. You can also quit all tracker-owned
Chromium processes and manually remove the exact `leetcode.browser_profile`
directory. Reauthentication deliberately keeps `account_file`, preventing an
accidental login to another account. To intentionally start a separate dataset,
use a separate repository/profile/account file; never delete `tracker.json`,
`solutions/`, or `review-log.json` to fix authentication.

## GitHub Actions

`.github/workflows/update-review-schedule.yml` runs tests and regenerates the
schedule/CSV when tracker or review data changes, daily as a fallback, or via
`workflow_dispatch`. It commits generated changes with the normal
`github-actions[bot]` identity. Bot push events are skipped to avoid loops.
LeetCode access is intentionally absent from CI.

## Reliability and recovery

All JSON and source writes use temporary files plus atomic replacement. JSON is
validated before replacement. Parsers fail closed on missing fields, login
pages, GraphQL errors, null authenticated data, ID mismatches, or changed source
bytes. Historical attempts are never deleted automatically.

LeetCode's GraphQL interface is undocumented and may change. The script uses a
single browser, pages 20 rows at a time, waits between requests, and fetches
details only for unseen IDs plus the first known change-detection boundary. If
LeetCode changes the contract or shows a
challenge, the run stops instead of committing partial metadata. Review
LeetCode's current Terms before using automated access.

Git history is the primary backup. To recover a generated file, restore it from
Git and rerun `scripts/update_review_schedule.py`. To verify locally:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m compileall -q scripts tests
```

## Reference projects

The design was informed by both requested repositories before implementation:

- [`notAkki/eLeetCode`](https://github.com/notAkki/eLeetCode) (MIT): useful
  slug-keyed attempt history and GitHub-backed storage ideas. Its Chrome
  extension, pasted GitHub PAT, manual form, heuristic review flags, and
  non-atomic direct Contents API writes conflict with this project's local
  sync and FSRS requirements, so they were not adopted.
- [`r-chong/dsa`](https://github.com/r-chong/dsa): useful examples of a daily
  generated review artifact, strict checks, and CI scheduling. Its fixed
  intervals, Git-history-derived attempts, CSV authority, and manual lists were
  rejected. The repository had no detected license, so its code was not copied.

The implementation here is independent and keeps GitHub as the permanent
personal dataset without introducing a service layer.
