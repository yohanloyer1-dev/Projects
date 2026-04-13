# Dashboard Changelog
<!-- Running log of all changes made to dashboard.html, in reverse chronological order -->
<!-- Format: ## YYYY-MM-DD | short title | commit hash (if known) -->

---

## 2026-04-13 | Quick-add modal: mode-filtered sections
**Commit:** `6b365d7`

### Bug Fixed
- **Section dropdown showed all sections regardless of Personal/Work mode** — no filtering, wrong names, missing sections (Work Travel, Role Optimization, Follow-ups, Presentations & Events)
- `injectQuickAddTask()` routing used old stale project names (`'Agency'`, `'Nébuleuse'`) that no longer matched new section values

### Changes
- **HTML:** Replaced flat project `<select>` with mode-annotated options using `data-mode="personal"` or `data-mode="work"` attributes. All section names now exactly match dashboard card titles.
- **Personal sections:** Strategy & Vision, Tools & Integrations, Dashboard & Productivity, Admin & Finance, Health, Real Estate, Japan Trip, Travel & Errands, Tech & Accounts, Network & Others, Bots & Automation
- **Work sections:** Work Travel, Presentations & Events, Role Optimization, Follow-ups, Nébuleuse Bijoux, Accessory Partners, Gorgias Agency, LinkedIn Content
- **New `filterQaProjectsByMode(mode)`** — hides options whose `data-mode` doesn't match current mode. Resets selection if current value becomes hidden.
- **`selectQaMode()`** — now calls `filterQaProjectsByMode()` on every mode switch
- **`openQuickAdd()`** — filters on open, so dropdown is already correct when modal appears
- **`injectQuickAddTask()` routing** — updated project name lists to match new section values

---

## 2026-04-13 | TASKS.md sync system rebuild (Option B)
**Commit:** `1f73241`

### Architecture
- **Problem solved:** `syncTaskDoneToGitHub()` was using wrong token type, had silent failures, fuzzy name matching. Replaced entirely.
- **New approach:** Button-triggered batch sync (not per-completion) to avoid race conditions on SHA requirement. `beforeunload` fires best-effort sync on page close.

### New Functions
- **`buildTaskMap()`** — builds `id→name` lookup from live DOM at runtime. Reliable because Claude controls both dashboard HTML and TASKS.md.
- **`syncToTasksMd(silent)`** — fetches TASKS.md SHA + content from GitHub API, marks completed tasks `[x]` by matching `data-id` → bold name in TASKS.md, PUTs back atomically. Falls back to name-only match if id not in map.
- **`setTasksSyncStatus(status, msg)`** — updates topbar button + indicator. States: idle / syncing / ok / error. Shows last sync time on idle.

### UI
- **Topbar sync group** — "↑ Sync TASKS" button + small indicator showing last sync time or current status
- **Button disabled** during sync (prevents concurrent writes / SHA race condition)
- **Color coding:** amber = syncing, green = ok, red = error

### Triggers
- **Manual:** click "↑ Sync TASKS" in topbar anytime
- **Auto (pending flag):** when a task is completed, `_tasksSyncPending = true`. Button shows idle state nudging user to sync.
- **Auto (beforeunload):** `window.beforeunload` fires `syncToTasksMd(true)` silently if pending. Best-effort — browser may not complete it on fast close.

### Security
- Same token (`yl_gist_token`) reused — already in localStorage, same XSS risk profile as Gist sync
- No new attack surface introduced
- SHA required by GitHub API prevents overwriting concurrent changes

### Error handling
- **401:** shown as "auth" error — token invalid or missing repo scope
- **403:** shown as "forbidden" — token lacks repo write access
- **Network failure:** shown as "network" error, caught cleanly
- All errors visible in topbar (not silent console.warn)

---

## 2026-04-13 | Claude task queue system + overdue processor notifications

### Queue System (lines ~1727-2650)
- **New: initNotePanel()** (lines ~2509-2650)
  - "Queue for Claude" checkbox UI with safe rendering
  - Submission handler: validates task exists, captures project/title, sends to GitHub Gist endpoint
  - Appends "Queued at [timestamp]" to task notes
  - XSS: all DOM methods safe (no innerHTML), timestamp validated before rendering (ISO 8601 check, fallback to 'today')
  - Race condition fix: uses existing queue item as fallback if task DOM element missing (deletion edge case)
- **New: syncQueueResults()** (lines ~1727-1783)
  - Fetches queue.json from GitHub raw URL (no auth needed)
  - Detects completed tasks by checking `queue.completed` array
  - Appends Claude's result to corresponding task notes
  - Updates task status badges (pending → processing → completed)
  - Checks `lastProcessed` timestamp; shows overdue banner if >24h old AND pending tasks exist
  - Triggered on page load (500ms after Gist sync)
- **Queue state persistence:** queue.json structure: `{ pending: [], completed: [], lastProcessed }`
- **Status badges CSS** (lines ~311-324): `.queue-status` styles for pending/processing/completed states
- **Overdue notification banner** (HTML lines ~751-760, CSS lines ~723-750)
  - Orange warning: "⚠️ Processor overdue (last run >24h ago)"
  - Shows only when processor hasn't run in 24+ hours AND pending tasks exist
  - Dismissible; auto-hides when sync succeeds
  - CSS animation: subtle pulse on .queue-overdue-banner

### Scheduled Processor Task
- **Task ID:** `process-claude-task-queue`
- **Schedule:** Daily at 10:30am (cron: "30 10 * * *", local timezone)
- **Action:** Reads queue.json, processes each pending task via Claude, appends result, updates queue status
- **Result sync:** Dashboard fetches results on next page load via syncQueueResults()

### Security Improvements
- **XSS prevention:** processedAt timestamp validated (ISO 8601 format check before rendering)
- **Race condition fix:** Note panel now uses queue item fallback when task is deleted while panel open
- **Safe DOM:** All queue UI uses createElement/appendChild, no innerHTML

### Known Limitations
- Processor relies on computer being awake at 10:30am; overdue banner alerts if missed
- Manual trigger available anytime via dashboard (not yet wired to UI button)

---

## 2026-04-11 | Disable broken TASKS.md sync automation + security XSS fixes
**Commits:** `1deb0e4` (XSS fixes), `9d4fd3b` (sync disable)

### Security: XSS Vulnerability Fixes (1deb0e4)
- **XSS via onclick handler (renderBrief, line 2416):** Replaced inline `onclick="goToTask(...)"` with event delegation using `data-*` attributes. Click listener now attached to `.brief-item` parent.
- **XSS via innerHTML (addLog, line 2596):** Refactored to use safe DOM methods (`createElement`, `appendChild`, `.textContent`) instead of template literal innerHTML injection.
- **XSS via unescaped template interpolation (renderBrief, line 2418):** Applied new `escapeHtml()` utility (line 1601) to all interpolated values.
- **Added escapeHtml() utility (line 1601):** Safe HTML entity conversion using browser's built-in textContent method.

### Bug Fixes (a7b8964)
- **Brief priority numbering gap:** Fixed renderBrief to skip rank labels when fewer than 3 tasks qualify (was showing #1 and #3, missing #2).
- **Task completion dates:** Fixed addLog to accept timestamp parameter (was always capturing current date, showing April 11 for all tasks).

### Automation Disabled (9d4fd3b)
- **Removed syncTaskDoneToGitHub() function (lines 1722-1768)** — non-functional for the following reasons:
  - Token: Uses `yl_gist_token` (Gist sync) for GitHub API calls to TASKS.md (different service, different scope)
  - Configuration: Token never set by users, function always returns silently
  - Error handling: Failures only logged to console, no user visibility
  - Matching: Fragile fuzzy substring matching with no fallback to data-id
  - Testing: Never actually tested or verified to work end-to-end
- **Removed sync call sites (lines 2840, 3819)** — both in task completion handlers
- **Replaced with manual sync workflow:**
  - Users: dashboard → exportSession() → copy markdown → paste to Claude
  - Claude: manually updates TASKS.md on GitHub and confirms
  - Future: Option B rebuild with proper token + UI feedback

### Documentation Added
- `memory/sync-automation-audit.md` — detailed analysis of sync system failure + recommendations
- `memory/code-review-log.md` — comprehensive security audit findings

### Tasks Updated
- Added Japan trip tasks: international driving license request, Okinawa accommodation, Okinawa return flight

---

## 2026-04-06 | 8-fix batch: mode filtering, new tasks, quick-add UX, timer, streak dots
**Commit:** `4695b80`

### Fixes
- **DTN "Do This Now" now mode-aware** — was showing tasks from all views regardless of Personal/Work toggle. Fixed `dtnGetActiveTasks()` to scope to `view-personal` or `view-pro + view-freelance` based on `yl_mode`.
- **setMode() now re-renders DTN** — switching modes updates both Top Priorities and Do This Now immediately.
- **Quick-add has Work/Personal mode selector** — pre-selects based on current dashboard mode. Mode is saved with task and used to route task to correct view on inject.
- **Accidental task completion fixed** — `bindSingleTask()` was firing on whole row click. Changed to checkbox-only click listener.
- **"Due today" badge showed twice** — deadline badge text updated to "Due today" / "in Nd" format. No duplicate static badge.
- **Focus button added to quick-add tasks** — was missing from `injectQuickAddTask()`.
- **Timer keeps running when tab is in background** — replaced `setInterval` decrement with absolute `_focusEndTime` timestamp. Polls every 500ms so it catches up accurately when returning to tab.
- **Streak dots light up immediately after completing a task** — added `renderStreakDots()` + `dtnRender()` + `renderBrief()` calls to both `bind()` and `bindSingleTask()` completion handlers.

### New tasks added to HTML
- Work Travel: "Book hotel Amsterdam" (urgent + important, #1)
- Follow-ups: Panagora Klaviyo, LTV Plus Lunch Vouchers, Follow up Nenad, Ping Spanish partners + Blas
- New card "Presentations & Events": Slides Fashion Commerce
- Japan Trip: Book hotel Taiwan May 9th, Confirm itinerary

---

## 2026-04-05 | Streak dots: colour by actual activity dates
**Commit:** `4903eff`

- `renderStreakDots()` was colouring dots based on streak count only (last N days from today). Rewritten to build a `Set` of YYYY-MM-DD strings from `S.done` timestamps and colour any dot whose date has a completed task. Recency-based intensity (d1–d4).

---

## 2026-04-05 | Fix XP sync: remove premature save() stamping yl_saved_at
**Commit:** `918e342`

- `save()` after `PRE_DEADLINES` was writing a fresh `yl_saved_at` timestamp before `gistPull()` ran, making local always look newer than Gist. Replaced `save()` with direct `localStorage.setItem('yl_deadlines', ...)`.

---

## 2026-04-05 | Banner fix: stays visible until sync confirmed
**Commit:** `fd1cede`

- `hideSyncBanner()` was called at line 1963 before the Gist fetch even started. Removed premature call.
- Banner now shows "Connecting to cloud sync…" when token is stored (not "Cloud sync not set up").
- 401 response keeps banner visible and updates title to prompt re-entry.
- `initGistSync()` early-return (after reload) now calls `hideSyncBanner()` so banner doesn't persist after confirmed sync.
- Banner HTML gets `.show` class by default (always visible on load).

---

## 2026-04-04 | Gist canonical ID + saved_at timestamp sync logic
**Commits:** `3f13248`, `245bf70`, `80d7be3`

- Hardcoded `CANONICAL_GIST_ID = '3410a8e3253dee00545350a2b745ca2d'` so all devices always use same Gist.
- Gist pull winner determined by `saved_at` ISO timestamp comparison (was using done-count, which was unreliable).
- `resetAndResync()` function: clears all localStorage except token, reloads.
- `save()` now writes `yl_saved_at` on every save.

---

## 2026-04-04 | Mobile CSS fixes
**Commit:** `02b7141` (approx)

- `@media (max-width: 768px)`: DTN strip stacks vertically, quick-add becomes bottom sheet, gamification hero stacks, 2-col stats row, nav tabs wrap to 2 rows of 3.

---

## 2026-04-04 | XP seed guard + yl_seed_done flag
**Commit:** `c683511`

- Seed was re-running because `save()` wrote `S.xp=0` back before seed values were read into state. Fixed: seed checks `+stored > 0` AND `yl_seed_done` flag. Sets `yl_seed_done='1'` so it never re-runs.

---

## 2026-03-27 | Initial dashboard v2.5
- Personal/Work toggle, mode-aware Brief, Focus mode overlay, deadline system, Pick for Me, task filtering, XP/streaks, GitHub Gist cloud sync foundation.

---

## Known issues / future work
- Auto-sync completed tasks to TASKS.md on GitHub (built but not confirmed working end-to-end)
- Quick-add tasks say "Will sync to TASKS.md at next session" — this should be automatic
- `renderBrief()` Top Priorities limited to 3 — should show more or be configurable
- Netlify suspended (free plan exceeded) — using GitHub Pages at `yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html`
