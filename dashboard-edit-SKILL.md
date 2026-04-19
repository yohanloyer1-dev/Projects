# dashboard-edit

**ALWAYS invoke this skill before making any changes to dashboard.html.**

This skill enforces the mandatory protocol for dashboard edits. Every step is required — no exceptions.

## Trigger

Invoke automatically when:
- User asks to edit, fix, update, or change the dashboard
- User mentions `dashboard.html`, "the dashboard", or any feature of the dashboard
- Any task that will result in writing to `Productivity/dashboard.html`

## Mandatory Checklist — Follow In Order

### Step 1 — Read before touching
Before writing a single line of code:
```
Read: /sessions/.../mnt/Projects/Productivity/dashboard.html
Read: /sessions/.../mnt/Projects/Productivity/memory/dashboard-changelog.md
```
Understand what changed last. Never edit blind.

### Step 2 — Save a version snapshot
Before any edit, copy the current dashboard to versions/:
```
cp Productivity/dashboard.html Productivity/versions/dashboard_vX.X_YYYY-MM-DD.html
```
Check existing versions to determine the correct version number (increment from latest).

### Step 3 — Make the edit
Make all planned changes to `Productivity/dashboard.html`.

Verify after editing:
- Brace balance check (open == close)
- All new functions exist in file
- No regressions to existing functions

### Step 4 — Update dashboard-changelog.md IMMEDIATELY
**This step is non-negotiable and must happen before any commit.**

Prepend a new entry to `Productivity/memory/dashboard-changelog.md`:
```markdown
## YYYY-MM-DD | [short description] | [commit hash — fill after commit]

### Problem Fixed / Feature Added
- [what was broken or missing]

### Changes
- [function names changed/added]
- [behaviour changes]
- [anything removed]
```

### Step 5 — Commit BOTH files together
```bash
git add Productivity/dashboard.html Productivity/memory/dashboard-changelog.md Productivity/versions/dashboard_vX.X_YYYY-MM-DD.html
git commit -m "feat/fix: [description]"
git pull --rebase origin main
git push origin main
```

The pre-commit hook at `~/Projects/.git/hooks/pre-commit` will **block the commit** if `dashboard-changelog.md` is not staged. This is intentional.

### Step 6 — Update commit hash in changelog
After the commit succeeds, fill in the commit hash in the changelog entry.

### Step 7 — Confirm to user
Report:
- What changed
- Commit hash
- Link: https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html (live in ~30s)

## What Happens If You Skip Step 4

The pre-commit hook blocks the commit:
```
✗ COMMIT BLOCKED — Protocol violation
dashboard.html is staged but dashboard-changelog.md is not.
```

Fix: update the changelog, stage it, re-commit. Never use `--no-verify` to bypass the hook.
