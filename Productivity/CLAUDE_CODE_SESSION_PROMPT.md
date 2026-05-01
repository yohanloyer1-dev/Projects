# Claude Code Session Prompt — Dashboard Fixes
**Date prepared:** 2026-05-01
**Prepared by:** Claude Sonnet (Cowork session — supersedes SONNET_SESSION_PROMPT.md)
**Target file:** `~/Projects/Productivity/dashboard.html` (4,766 lines)
**Repo:** `~/Projects/` — push to `main`, no feature branch needed
**Live URL:** https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html

---

## MANDATORY: Read Before Touching Anything

```bash
cat ~/Projects/dashboard-edit-SKILL.md
```

This file defines the non-negotiable commit protocol. The repo has a **pre-commit hook** at
`~/Projects/.git/hooks/pre-commit` that **blocks any commit** of `dashboard.html` unless
`Productivity/memory/dashboard-changelog.md` is staged in the same commit. Do not use `--no-verify`.

**Protocol summary:**
1. Before any edit: save a version snapshot to `Productivity/versions/dashboard_vX.X_YYYY-MM-DD.html`
2. Make all edits
3. Update `Productivity/memory/dashboard-changelog.md` (prepend new entry)
4. Stage `dashboard.html` + `dashboard-changelog.md` + version snapshot together
5. Commit and push

---

## Context: What This Dashboard Actually Is

Single-file productivity app (`dashboard.html`, vanilla JS/CSS, no framework). Key architecture facts:

- **State object `S`:** All state lives in one object — `S.done` (array of completed tasks),
  `S.statuses` (manual overrides), `S.deadlines`, `S.notes`, `S.links`, `S.xp`,
  `S.queuedForClaude`, etc. Persisted via `save()` → localStorage key `yl_state`.
- **NOT `doneList` or `tasks` arrays** — older doc files reference these; they are wrong.
  The real state uses `S.done` and hardcoded task HTML in the DOM.
- **GitHub sync:** Two systems — (1) Gist sync for cross-device state (`gistPush/Pull`),
  (2) DASHBOARD-TASKS.md sync via GitHub Contents API (`syncDashboardTasks()`).
  Token stored in **localStorage** at `yl_gist_token` (this is what Fix A changes).
- **Task DOM structure:** Tasks are hardcoded HTML
  `<div class="t [urg|hi|cl]" data-id="..." data-xp="..." data-project="...">`.
  No dynamic task creation from a data model.
- **`notify()` function exists** — use it for user-visible alerts, not `alert()` or `console.error()`.
- **Pre-commit hook is live** — added 2026-04-20, commit `7232546`. Do not bypass.

---

## Already Fixed (DO NOT RE-DO)

Verify these exist before touching related code:

### Fixed #1 — `renderBrief()` mode-aware ranking
```bash
grep -n "activeViews" ~/Projects/Productivity/dashboard.html
# Should return a line around 2958
```
Brief now scores only tasks from the active mode's views. No invisible cross-mode slots.

### Fixed #2 — DTN Someday/Waiting cap
```bash
grep -n "Math.min(score, 50)" ~/Projects/Productivity/dashboard.html
# Should return a line
```
Someday/Waiting tasks can no longer outscore genuinely urgent tasks via stale deadlines.

---

## Fix List — Apply In This Order

### Fix A — Token security: move `yl_gist_token` to sessionStorage
**Priority:** High — real XSS exposure (localStorage persists across sessions, readable by any
injected script; sessionStorage clears on tab close)

Find all occurrences:
```bash
grep -n "yl_gist_token\|yl_gist_id" ~/Projects/Productivity/dashboard.html
```

**Changes:**
1. `gistGetToken()` → `sessionStorage.getItem('yl_gist_token')`
2. `gistSetId()` → `sessionStorage.setItem('yl_gist_id', id)`
3. Wherever `saveGistToken()` writes to localStorage → switch to sessionStorage
4. Add a one-time migration block at the very top of the script (before `gistGetToken()` is called):

```javascript
// One-time migration: move token from localStorage to sessionStorage
const _legacyToken = localStorage.getItem('yl_gist_token');
if (_legacyToken && !sessionStorage.getItem('yl_gist_token')) {
  sessionStorage.setItem('yl_gist_token', _legacyToken);
  localStorage.removeItem('yl_gist_token');
}
```

5. Add a notification for users who have no token set (delayed so `notify()` is ready):
```javascript
setTimeout(() => {
  if (!sessionStorage.getItem('yl_gist_token')) {
    notify('GitHub token not set — paste your PAT in Settings to enable sync', 'warn', 8000);
  }
}, 1500);
```

6. Do NOT move `yl_state` (main task data) — that stays in localStorage. Only the token moves.

**Testing:**
- Open DevTools → Application → localStorage: `yl_gist_token` should be gone
- Open DevTools → Application → sessionStorage: token present after entering it
- Refresh page → token cleared from sessionStorage, warning notification appears
- Legacy users: localStorage entry removed automatically on first load

---

### Fix B — GitHub sync: visible error notifications
**Priority:** High — sync failures are currently silent (user never knows their completions didn't sync)

Find the function:
```bash
grep -n "async function syncDashboardTasks\|function syncDashboardTasks" ~/Projects/Productivity/dashboard.html
```

**Changes:**
1. In the `catch` block, replace `console.error(...)` with:
   `notify('GitHub sync failed — will retry next session', 'error', 6000)`
2. After the `fetch` call, add HTTP status checking:
   - 401: `notify('GitHub token invalid — re-enter in Settings', 'error', 8000)`
   - 409: `notify('Sync conflict — refresh to get latest version', 'warn', 6000)`
   - 5xx: `notify('GitHub API error — will retry', 'warn', 4000)`
3. On success: check if a success notification already exists — if not, add:
   `notify('Synced ✓', 'success', 2000)`

Do NOT add full retry logic with exponential backoff — that's overengineering.
The sync button already acts as a manual retry. Keep it simple: fail visibly.

---

### Fix C — Dynamic Claude Tasks tab
**Priority:** Medium — the Claude Tasks tab (`view-claude`) has 9 hardcoded cards that drift
out of sync as tasks are completed or added

Find the tab:
```bash
grep -n 'id="view-claude"' ~/Projects/Productivity/dashboard.html
```

**Build `renderClaudeTasks()`:**

```javascript
function renderClaudeTasks() {
  const container = document.getElementById('view-claude');
  if (!container) return;

  const mode = localStorage.getItem('yl_mode') || 'personal';
  const viewIds = mode === 'personal'
    ? ['view-personal']
    : mode === 'freelance'
      ? ['view-freelance']
      : ['view-pro', 'view-freelance'];

  const doneIds = new Set(S.done.map(d => d.id || d.n));

  // Collect all cl-marked, undone tasks
  const clTasks = viewIds
    .map(id => document.getElementById(id))
    .filter(Boolean)
    .flatMap(v => Array.from(v.querySelectorAll('.t.cl[data-id]')))
    .filter(t => {
      if (t.classList.contains('done-t')) return false;
      const id = t.dataset.id;
      const name = t.querySelector('.tn')?.textContent || '';
      return !doneIds.has(id) && !doneIds.has(name);
    });

  // Sort: urg first, then hi, then rest
  clTasks.sort((a, b) => {
    const score = el => (el.classList.contains('urg') ? 2 : el.classList.contains('hi') ? 1 : 0);
    return score(b) - score(a);
  });

  // Find the dynamic section (or create it)
  let dynamicSection = container.querySelector('.claude-dynamic');
  if (!dynamicSection) {
    dynamicSection = document.createElement('div');
    dynamicSection.className = 'claude-dynamic';
    // Insert before the first hardcoded .claude-task, or at top after the header
    const firstCard = container.querySelector('.claude-task');
    if (firstCard) container.insertBefore(dynamicSection, firstCard);
    else container.appendChild(dynamicSection);
  }

  if (!clTasks.length) {
    dynamicSection.innerHTML = '<p style="color:var(--t3);font-size:13px;font-family:var(--fm)">No Claude-ready tasks in this mode.</p>';
    return;
  }

  dynamicSection.innerHTML = clTasks.map(t => {
    const id = t.dataset.id;
    const name = t.querySelector('.tn')?.textContent || id;
    const project = t.dataset.project || '';
    const note = S.notes?.[id] || '';
    const isUrgent = t.classList.contains('urg');
    const isHi = t.classList.contains('hi');
    const badge = isUrgent ? '🔴 Urgent' : isHi ? '🟡 Important' : '';

    return `<div class="claude-task" data-id="${escapeHtml(id)}">
      <div class="ct-header">
        <div class="ct-name">${escapeHtml(name)}</div>
        ${badge ? `<span class="claude-status" style="background:rgba(217,95,75,.15);color:var(--red)">${badge}</span>` : ''}
      </div>
      ${project ? `<div class="ct-proj" style="font-size:11px;color:var(--t3);font-family:var(--fm);margin:2px 0 6px">${escapeHtml(project)}</div>` : ''}
      ${note ? `<div class="ct-note">${escapeHtml(note)}</div>` : ''}
      <button class="ct-copy" data-task-id="${escapeHtml(id)}" data-task-name="${escapeHtml(name)}" data-task-note="${escapeHtml(note)}">📋 Ask Claude now</button>
    </div>`;
  }).join('');

  // Wire up Ask Claude buttons
  dynamicSection.querySelectorAll('.ct-copy').forEach(btn => {
    btn.addEventListener('click', () => {
      const name = btn.dataset.taskName;
      const note = btn.dataset.taskNote;
      const prompt = note
        ? `Task: ${name}\n\nContext / instructions:\n${note}`
        : `I need help with this task: ${name}`;
      navigator.clipboard.writeText(prompt).then(() => {
        btn.textContent = '✓ Copied! Opening Claude...';
        setTimeout(() => {
          window.open('https://claude.ai/new', '_blank');
          btn.textContent = '📋 Ask Claude now';
        }, 800);
      }).catch(() => window.open('https://claude.ai/new', '_blank'));
    });
  });
}
```

Wire into `updateUI` the same way `dtnRender()` is wired (check around line 4716):
```javascript
updateUI = function() { _origUpdateUI.apply(this, arguments); dtnRender(); renderClaudeTasks(); };
```
Also call `renderClaudeTasks()` in the `setMode()` function so it updates on mode switch.

Once verified working, remove the hardcoded `.claude-task` cards in the same commit.

---

### Fix D — Disable dead `fetchClaudeQueue()`
**Priority:** Low — 5 min job

```bash
grep -n "fetchClaudeQueue" ~/Projects/Productivity/dashboard.html
```

Comment out the call (don't delete the function):
```javascript
// fetchClaudeQueue(); // Disabled 2026-05-01 — no queue processor running
```

Also find the "Claude queue processor hasn't run yet" message (search for it) and remove or replace with something accurate, e.g. "Use the 🤖 Claude Tasks tab to work on Claude-ready tasks."

---

### Fix E — `dtnSkipIdx` divide-by-zero guard
**Priority:** Low — 2 min job

Find in `dtnGetTopTask()` (~line 4600):
```javascript
const idx = dtnSkipIdx % scored.length;
```

Add a guard immediately before it:
```javascript
if (!scored.length) return null;
const idx = dtnSkipIdx % scored.length;
```

(Check if `active.length === 0` is already guarded above — it probably is, but `scored` could
theoretically be empty if all active tasks are filtered out by scoring. Add the guard explicitly.)

---

## Commit Strategy

**Two commits:**

**Commit 1** — Fixes A + B + D (security + visibility + noise):
```bash
git add Productivity/dashboard.html Productivity/memory/dashboard-changelog.md Productivity/versions/dashboard_vX.X_YYYY-MM-DD.html
git commit -m "fix: token sessionStorage migration, sync error visibility, queue call disabled"
git push origin main
```

**Commit 2** — Fixes C + E (dynamic Claude tab + edge case):
```bash
git add Productivity/dashboard.html Productivity/memory/dashboard-changelog.md
git commit -m "feat/fix: dynamic Claude Tasks tab, dtnSkipIdx guard"
git push origin main
```

---

## What to IGNORE from Older Docs

`SONNET_SESSION_PROMPT.md`, `HANDOVER_PHASE_1_IMPLEMENTATION.md`, `PHASE_1_SECURITY_A11Y_FIXES.md`
were created by Haiku and contain **inaccurate code examples** that don't match the real dashboard:

- They reference `doneList`, `tasks`, `markTaskDone(task)` — none of these exist in the real file
- Fix 1.3 (CSRF nonce) — not needed for a personal single-user tool
- Fix 2.1 (IndexedDB archival) — over-engineered; `S.done` stores tiny objects, quota won't be hit
- Fix 2.2 (error boundary wrapper) — doesn't apply to this DOM-driven architecture
- "15–20 hours" estimate — wildly off; these 5 fixes are 2–3 hours total

**Use this document, not the Haiku docs.**

---

## Testing Checklist

After each commit, open https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html

**Fix A:** DevTools → localStorage: no `yl_gist_token`. DevTools → sessionStorage: token present.
Refresh → token gone, warning notification appears.

**Fix B:** With invalid token, trigger sync → visible error notification (not just console).

**Fix C:** Claude Tasks tab shows current `cl`-marked tasks. Mark one done → it disappears.
Mode switch → tab updates to show correct mode's tasks.

**Fix D:** DevTools → Network → reload → no 404 for queue.json.

**Fix E:** Mark all tasks done → DTN shows "All tasks cleared", no JS error in console.

---

## Key Files

| File | Path |
|------|------|
| Main dashboard | `~/Projects/Productivity/dashboard.html` |
| Edit protocol (MANDATORY) | `~/Projects/dashboard-edit-SKILL.md` |
| Changelog | `~/Projects/Productivity/memory/dashboard-changelog.md` |
| Versions | `~/Projects/Productivity/versions/` |
| Session log | `~/Projects/Productivity/memory/session-log.md` |
| CLAUDE.md | `~/Projects/CLAUDE.md` |

**Pre-commit hook:** `~/Projects/.git/hooks/pre-commit` — blocks dashboard commits without
changelog staged. Never bypass with `--no-verify`.
