# dsa

A local-first LeetCode tracker for submissions, notes, spaced reviews, and Google Sheets.

## setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/sync_leetcode.py
```

The first sync opens Chrome if you need to sign in.
Runtime data and credentials stay in the ignored `.dsa/` directory.

## daily use

Run this after solving problems:

```bash
.venv/bin/python scripts/sync_leetcode.py
```

The sync imports new attempts, updates review data and Google Sheets, then commits and pushes when `git.auto_push = true`.
Use `--no-push` to keep the update local.

## solution notes

Write your thoughts as comments at the top, before the solution code.
Add `divergences:` after the code, then write what changed, what failed, or what you learned.

```python
# use multi-source BFS from every zero
# each level increases the distance by one
class Solution:
    ...

# divergences:
# forgot to mark each zero as visited before BFS
# queue initialization defines what distance is measured from
```

The sheet stores comments before the first marker as `thought_process`.
It stores comments after the marker as `notes`.
Each numbered solution file keeps every submitted version and its ordered comments.
A later submission is appended to the same file with a short submission comment.

These optional labels also get their own columns:

- `core insight:`
- `pattern:`
- `mistakes:`
- `edge cases:`
- `time complexity:`
- `space complexity:`

## reviews

Redo the problem before opening your old solution, then record the result:

```bash
.venv/bin/python scripts/record_review.py 542 good \
  --minutes 12 \
  --hints 0 \
  --notes "remembered the pattern" \
  --failure-stage "implementation"
```

Grades:

- `again` - could not solve it.
- `hard` - solved with substantial difficulty or help.
- `good` - solved independently with normal effort.
- `easy` - immediate recall and a clean solution.

Review tracking starts on `tracker.tracking_start_date` in `config.toml`.
Older solutions remain in the history but do not appear in `Due Today`.

## Google Sheets

Each sync updates the configured [Google Sheet](https://docs.google.com/spreadsheets/d/1tLwBlpgG0ehXyuksx1ktQJ1vnO6Pkg4NCgZYA8TGye0/edit):

- `Problems` contains the current solution notes and review state.
- `Submissions` contains the complete attempt history.
- `Reviews` contains explicit review events.
- `Due Today` shows the problems ready to review.

Google OAuth files stay under `.dsa/google/` and are never committed.

## main files

- `<number>-<slug>.<ext>` contains the submitted solutions for one problem and language.
- `tracker.json` contains the complete attempt history.
- `review-log.json` contains explicit review events.
- `review-schedule.json` contains the generated FSRS schedule.
- `google-sheets.csv` is the compact accepted-submission export.
- `mindsolve-log.csv` matches the r-chong/dsa review-log format.

## checks

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m compileall -q scripts tests
```
