# Dashboard Changelog
<!-- Running log of all changes made to dashboard.html, in reverse chronological order -->
<!-- Format: ## YYYY-MM-DD | short title | commit hash (if known) -->

---

## 2026-05-02 | Fix gistPull 401/other errors: add notify() popups | pending

### Problem Fixed
- `gistPull` 401 only updated banner text — no visible popup, inconsistent with `gistPush` Fix B
- Non-401 errors (e.g. 403, 5xx) silently hid the banner with no feedback at all

### Changes
- 401 branch: added `notify('err', 'Gist sync failed', 'Token invalid (401)…')`
- Other non-ok branch: added `notify('err', 'Gist sync failed', 'GitHub API error (${res.status})…')`
- Snapshot: `versions/dashboard_v3.4_2026-05-02_pre-gistpull-401.html`

---

## 2026-05-02 | Fix F: drag-and-drop section reordering with localStorage persistence | pending

### Feature Added
- Users can now drag entire task sections (by the header) to reorder them within a view
- Order persists across refreshes via `yl_section_orders` in localStorage

### Changes
- HTML: wrapped all 10 sections in `<div class="section-block" data-section-id="...">` — 7 in `#view-personal` (strategy-vision, admin-finance, health, real-estate-travel, tech-accounts, network-others, productivity), 2 in `#view-freelance` (clients, agency), 1 in `#view-pro` (gorgias-day-job)
- CSS: added `.section-block.dragging`, `.section-block.drag-over`, `.sh[draggable="true"]`, `.sh[draggable="true"]:active`
- JS: added `saveSectionOrder(viewId)`, `restoreSectionOrders()`, `initSectionDrag()`, `resetSectionOrder(viewId)`
- Init: `restoreSectionOrders()` and `initSectionDrag()` called at page load (after updateUI override)
- `setMode()`: `initSectionDrag()` added at end so drag handlers apply after mode switch
- Snapshot: `versions/dashboard_v3.3_2026-05-02_pre-drag-sections.html`

---

## 2026-05-02 | Add URSSAF Q1 + impôts 2042-C-PRO tasks (urgent, deadline May 8) | bdcb7bb

### Changes
- Added `urssaf-q1-decl`: "Déclarer CA Q1 URSSAF (auto-entrepreneur)" — class `t urg hi`, Tax & Declarations section, Personal mode
- Added `impots-fr-2042cpro`: "Déclaration impôts France — formulaire 2042-C-PRO" — class `t urg hi`, same section
- Both tasks seeded with deadline `2026-05-08` in `PRE_DEADLINES`
- Snapshot: `versions/dashboard_v3.3_2026-05-02_pre-new-tasks.html`

---

## 2026-05-02 | Option 3 claude-findings: fetch + overlay research on Claude Tasks cards | 073afa5

### Changes
- `claude-findings.json` created: schema `{ taskId: { summary, updatedAt } }`. Research pre-loaded for `decl-ae` and `adhd-diag`.
- `claudeFindings` global + `fetchClaudeFindings()`: fetches JSON from GitHub raw URL on DOMContentLoaded (cache-busted), re-renders Claude Tasks tab on success
- `renderClaudeTasks()`: uses `S.notes[id]` first (user note wins), falls back to `claudeFindings[id].summary`; adds purple "🤖 Researched YYYY-MM-DD" badge on cards with findings; note rendered with `white-space:pre-wrap` so line breaks in findings display correctly
- `adhd-diag`: added `cl` class → now appears in Claude Tasks tab (Personal mode)
- Removed `cl` from 3 completed `productivity-dashboard-*` tasks → no longer pollute Claude Tasks tab
- Snapshot: `versions/dashboard_v3.2_2026-05-02_pre-findings.html`

---

## 2026-05-02 | Fix C: ct-head click handler (cursor was pointer with no action) | pending

### Problem Fixed
- `.ct-head` has `cursor:pointer` + hover styling in CSS but no click handler in dynamic cards
- Clicking the card header did nothing — misleading UX

### Changes
- `renderClaudeTasks()`: added click handler on `.ct-head` → calls `goToTask()` using the card's `ct-start` data attributes
- Snapshot: `versions/dashboard_v3.1_2026-05-02_pre-cursor-fix.html`

---

## 2026-05-02 | Fixes C + D(complete) + E: dynamic Claude tab, queue call disabled, DTN guard | ec12ed2

### Changes
- **Fix C — renderClaudeTasks()** (line ~4666): New function replaces 8 hardcoded `.claude-task` cards
  - Reads live `.t.cl[data-id]` tasks from the active mode's view (personal/freelance/pro)
  - Filters out completed tasks (cross-checks `S.done` by id and name)
  - Sorts urgent > important > rest
  - Generates cards using existing `.ct-head`, `.ct-status`, `.ct-note`, `.ct-copy`, `.ct-start` CSS
  - "Copy session prompt" uses `S.notes[id]` if set, else generic prompt
  - "Jump to task" uses existing `goToTask()` with correct tab id
  - Wired into `setMode()` (re-renders on mode switch) and `updateUI()` (re-renders on task completion)
  - Initial call at DOMContentLoaded
  - Removed: 8 hardcoded cards covering polymarket-bot, adhd-diag, goals-2026, agency-name, service-packages, role-brainstorm, stub-articles, multi-brand (2 of which no longer existed as cl-marked tasks)
  - Added `claude-hint` class to hint div for JS anchor; updated hint text
- **Fix D(complete)** (line ~2697): Disabled `setTimeout(syncQueueResults, 500)` — was making a 404 network request on every page load
- **Fix E** (line ~4650): Added `if (!scored.length) return null` guard before `dtnSkipIdx % scored.length` in `dtnGetTopTask()`

---

## 2026-05-02 | Revert Fix A: restore yl_gist_token to localStorage | 1988e82

### Reason for revert
Fix A moved the GitHub token to sessionStorage, requiring re-entry every session.
For a single-user personal dashboard on GitHub Pages with no external scripts or CDN,
the XSS threat model doesn't justify the daily friction. Token stayed in localStorage.
The no-token warning notification is kept (useful for first-time setup).

### Changes reverted
- Migration block removed
- `gistGetToken()` → back to `localStorage.getItem('yl_gist_token')`
- `saveGistToken()` → back to `localStorage.setItem('yl_gist_token', token)`
- `resetAndResync()` → back to localStorage for token preserve/restore
- `gistSetId()` → back to `localStorage.setItem('yl_gist_id', id)`
- Notification setTimeout now checks `localStorage` (kept — useful for new device setup)
- Comments updated to reflect localStorage

---

## 2026-05-02 | Fix D: Remove stale queue processor banner message | e18f28b

### Problem Fixed
- `queueOverdueBanner` referenced a Claude queue processor that no longer exists
- `fetchClaudeQueue()` was already removed in a prior session; this cleans up the last UI artifact

### Changes
- Banner text (line ~784): "Claude queue processor hasn't run yet / Expected at 10:30 AM..." → "Claude-ready tasks in queue / Use the 🤖 Claude Tasks tab"
- No code removed — `syncQueueResults` kept (harmless, silently 404s if queue.json absent)

---

## 2026-05-02 | Fix B: Visible error notifications for all sync failures | 4199358

### Problem Fixed
- `gistPush` / `gistPull` failures were silent (only status indicator changed, no popup)
- `syncDashboardTasks` PUT response had no specific 401/409/5xx handling

### Changes
- `gistPush` (line ~2599): replaced silent `console.warn` + status with `notify` for 401, 409, 5xx, network errors
- `gistPull` catch (line ~2684): added `notify('warn', 'Gist pull failed', ...)` for network errors
- `syncDashboardTasks` PUT block (line ~2346): added specific branches for 401 → token invalid message, 409 → conflict message, 5xx → API error message
- Note: `syncDashboardTasks` GET + catch were already fully notified (fix written before those were added)

---

## 2026-05-02 | Fix A: Move yl_gist_token from localStorage to sessionStorage | 589eeac

### Problem Fixed
- Token persisted across sessions in localStorage, readable by any injected script (XSS risk)

### Changes
- Migration block added at start of GITHUB GIST section: reads legacy token from localStorage, moves to sessionStorage, removes from localStorage (one-time, runs on every load until done)
- `gistGetToken()` (line ~1775): reads from `sessionStorage` instead of `localStorage`
- `saveGistToken()` (line ~1782): writes to `sessionStorage` instead of `localStorage`
- `resetAndResync()` (lines ~1791–1794): reads/restores token via `sessionStorage`
- `gistSetId()` (line ~1798): writes id to `sessionStorage`
- DOMContentLoaded (line ~2693): added 1500ms delayed `notify('warn')` if no token in sessionStorage
- Updated stale comment on line ~1875 to reflect sessionStorage
- Snapshot: `versions/dashboard_v3.0_2026-05-02_pre-fix-A.html`

---

## 2026-05-01 | Reorder mode toggle: Personal → Work → Freelance | a71e4e3+

### Change
- Swapped Work and Freelance button order in mode toggle HTML (line ~801)
- New order: 🏠 Personal · 💼 Work · 🔧 Freelance

---

## 2026-05-02 | Add Freelance as standalone mode (3-way toggle) | pending

### Goal
Separate Freelance from Work mode so each area (Personal / Freelance / Work) has its own dedicated context, Brief, and Do This Now suggestions. Freelance was previously grouped with Professional (Work) mode, causing cognitive blending.

### Changes
- **CSS** (line ~82): Added `.mode-btn#mode-freelance.active { color: var(--green) }` — green highlight for Freelance mode button
- **Mode toggle HTML** (line ~801): Added `🔧 Freelance` button between Personal and Work
- **Nav tab emoji** (line ~957): Changed Freelance tab from `💼` to `🔧` to match new mode button
- **Mode constants** (line ~2903): Refactored `PERSONAL_TABS`, extracted `FREELANCE_TABS = ['freelance']`, `WORK_TABS = ['pro']` (removed `freelance` from Work). Added `ALL_MODE_TABS` union for show/hide loop.
- **`setMode()`** (line ~2913): 3-way logic — shows only the tabs for the active mode; `briefMode` maps `'freelance'` → `'work'` so Brief's `data-mode="work"` Project Snapshot still renders in Freelance mode; topbar subtitle shows `'Freelance Dashboard'`
- **`renderBrief()`** (line ~2961): Added `mode === 'freelance' ? ['view-freelance']` case — Brief now scores only freelance tasks when in Freelance mode
- **`dtnGetActiveTasks()`** (line ~4576): Added `mode === 'freelance' ? ['view-freelance']` case — DTN and Pick for Me now surface only freelance tasks
- **`QA_SECTIONS`** (line ~4050): Extracted `freelance` key with `['Nébuleuse Bijoux', 'Accessory Partners', 'Gorgias Agency (name TBD)', 'LinkedIn Content', 'Claude OS']`; `work` key now contains only Gorgias sections
- **Quick Add modal HTML** (line ~1542): Added `🔧 Freelance` mode button — pre-selects correctly when dashboard is in Freelance mode

### Revert
- Version snapshot: `versions/dashboard_v2.9_2026-05-02_pre-freelance-mode.html`
- All changes isolated to ~9 specific locations; no task data or localStorage keys touched

---

## 2026-04-22 | Add Productivity category (Personal) + 3 tasks | pending

### Changes
- Added new "Productivity" section to Personal view in dashboard.html (after Network & Others)
- Added 3 tasks: Dashboard Audit P1 (continue), Security fixes, Git conflicts + DTN audit
- Added `Productivity` to `SECTION_PARENT` map (→ `## 🧑 Personal`)
- Added `Productivity` to `QA_SECTIONS.personal` array
- Added `Productivity` emoji (`⚡`) to project emoji map
- Version snapshot: `versions/dashboard_v2.8_2026-04-22-pre-productivity.html`

---

## 2026-04-21 | DTN + Brief scoring fixes — mode-aware ranking + Someday cap | pending

### Problems Fixed
- **Brief showed rank "3" in Personal mode**: `renderBrief()` was scoring ALL views (personal + work + freelance) together, then hiding cross-mode items with CSS. Result: work tasks occupied invisible slots 1+2, leaving only slot 3 visible. Same bug caused only 2 tasks visible in Work mode.
- **Someday tasks with stale deadlines outranked urgent tasks**: A Someday task 30 days overdue scored 1100+ (deadline boost) vs 600 for a genuine urgent task. Explicitly deprioritised tasks were surfacing first.

### Changes
- `renderBrief()`: Changed `allViews` → `activeViews` filtered by mode BEFORE scoring. Removed `taskMode` candidate property. Removed `data-mode` attribute from rendered brief items. Removed CSS post-filter loop (`#briefGrid [data-mode]`). Brief now always shows 3 slots from the correct mode.
- `dtnGetTopTask()`: Moved Someday/Waiting penalty to AFTER deadline scoring, applied as a hard cap (`score = Math.min(score, 50)`). Prevents deadline boost from overriding explicit deprioritisation.

### Version snapshot
- `Productivity/versions/dashboard_v2.8_2026-04-21-pre-dtn-fix.html`

---

## 2026-04-20 | Inline task rename — pencil button + double-click | pending

### Feature Added
- Pencil button `✏️` injected on every task (appears on hover, same pattern as 📝 note btn)
- Double-click on task name also triggers edit — two entry points, one interaction
- Clicking pencil or double-clicking: `.tn` span replaced with inline `<input>` pre-filled
- Enter / click away → saves; Escape → cancels with no change
- Completed tasks (`done-t`) are not editable
- On save: updates DOM, `yl_renames` localStorage key, triggers silent `syncDashboardTasks()`
- `syncDashboardTasks()`: new Step 4b applies pending renames to MD file via bold-name regex
  replace, clears `yl_renames` after successful write
- Works for both hardcoded tasks (`bind()`) and quick-add tasks (`bindSingleTask()`)
- Mobile: `.edit-btn` added to always-visible button list on small screens

### New function
- `startInlineEdit(taskEl)` — handles full edit lifecycle (input inject, save, cancel, sync)

### New CSS
- `.edit-btn` — amber hover colour, matches `.note-btn` / `.link-btn` sizing pattern
- `.tn-edit` — amber border input, matches dashboard dark theme

---

## 2026-04-20 | Reduce completion buffer from 60s to 10s | pending

### Change
- `scheduleCompletionSync()`: timeout reduced from 60000ms to 10000ms
- 60s was too long — accidental completions required a full minute wait to undo
- 10s gives enough time to notice and uncheck without feeling like a delay
- All comments updated to reflect new value

---

## 2026-04-20 | Fix UTF-8 encoding in GitHub API read/write + rebuild DASHBOARD-TASKS.md clean | 435c914

### Root Cause
- `atob()` returns a raw byte string, not Unicode — emoji and French accented chars (é, à, ô etc.)
  decoded to garbled `ÃÂ°...` sequences on every GitHub API read
- `btoa(unescape(encodeURIComponent(...)))` write pattern perpetuated the corruption on every PUT
- DASHBOARD-TASKS.md was fully corrupted — every emoji and accented char mangled

### Fix
- **Read (line ~2034):** replaced `atob(...)` with proper UTF-8 decode:
  `new TextDecoder('utf-8').decode(Uint8Array.from(atob(...), c => c.charCodeAt(0)))`
- **Write (line ~2192):** replaced `btoa(unescape(encodeURIComponent(...)))` with:
  `btoa(String.fromCharCode(...new TextEncoder().encode(content)))`
- **DASHBOARD-TASKS.md:** fully rebuilt from scratch — all emojis removed from `###` section
  headers (kept as plain text), all French accents restored, em-dashes (—) restored
- `###` headers now emoji-free: "Work Travel & Expenses", "Admin & Finance", etc.
  This permanently eliminates the emoji-in-header matching problem at source

---

## 2026-04-20 | Fix normSection emoji stripping — non-ASCII regex replaces codepoint allowlist | 31501e2

### Bug Fixed
- `normSection()` emoji regex allowlist (`\u{1F000}-\u{1FFFF}` etc.) failed to strip emoji
  bytes after `atob()` base64 decode — Safari/Chrome produce garbled multi-byte sequences
  (e.g. `"ã â ã â¢ã..."`) that don't match the Unicode ranges
- Result: `normFile` = `"ã â ã ... work travel & expenses"` — `startsWith("work travel")`
  fails → all 3 queued tasks hit ❌ NO MATCH → sync reports "Already up to date"

### Fix
- `normSection()`: replaced specific emoji codepoint regex with `/^[^\x00-\x7F\s]+\s*/g`
  (strip all leading non-ASCII character runs) + `/^[^\w]*/` (strip remaining non-word chars)
- More robust than an allowlist — handles any encoding artifact, not just known emoji ranges
- Both the file-side and queue-side strings now normalise to clean ASCII before comparison

---

## 2026-04-20 | Fuzzy section matching — legacy queue entries now sync correctly | fc3e0d1

### Bug Fixed
- 3 queued tasks stored with `project: "Work Travel"` (old abbreviated value) couldn't find
  the `"### ✈️ Work Travel & Expenses"` section in DASHBOARD-TASKS.md — exact normSection
  comparison returned no match → sync said "Already up to date" with tasks still pending
- Same issue in `addQuickAddTaskToUI()`: card title `"Work Travel & Expenses"` wouldn't match
  legacy queue entry `"Work Travel"` → tasks injected into floating fallback card instead of
  the correct section card

### Fix
- `syncDashboardTasks()` (line ~2050): two-pass section scan — exact match preferred, then
  `normFile.startsWith(normTarget)` fallback for legacy/abbreviated names
- `addQuickAddTaskToUI()` (line ~4088): same two-pass pattern for UI card injection
- Both functions: `startsWithTl` / `startsWithIdx` hold the fallback; exact match overrides

---

## 2026-04-20 | Fix section name mismatches between QA_SECTIONS and DASHBOARD-TASKS.md
**Commit:** pending

### Bug Fixed
- Sync still showed "Already up to date" after loop fix — `normSection("Work Travel")` = `"work travel"` but file header is `"Work Travel & Expenses"` → no match, nothing appended
- Other mismatches: `"Dashboard & Productivity"` vs `"Dashboard & Productivity System"`, `"Gorgias Agency"` vs `"Gorgias Agency (name TBD)"`, `"Bots & Automation"` vs `"Bots & Automation (Personal)"`
- `SECTION_PARENT` block search used `normParent.slice(0,10)` — fragile, breaks with emoji-prefixed `##` headers

### Fix
- Updated `QA_SECTIONS` dropdown values to exactly match `DASHBOARD-TASKS.md` headers (post-normalisation)
- Updated `SECTION_PARENT` keys to match new `QA_SECTIONS` values
- Fixed parent block search: replaced `slice(0,10)` with `normSection(lines2[i]) === normParent` — proper normalised comparison

---

## 2026-04-20 | Fix quick-add queue not syncing to DASHBOARD-TASKS.md
**Commit:** pending

### Bug Fixed
- Sync button showed "Already up to date" despite 3 tasks in queue — nothing was written to GitHub
- Two bugs in the append loop:
  1. `lines2` was rebuilt from `content.split('\n')` on every loop iteration — each task started from the original content, so only the last task's insertion survived in `content`
  2. When section was found via `SECTION_PARENT` (insertIdx === -2 sentinel), `content` was never updated from the mutated `lines2` (guarded by `if (insertIdx !== -2)`)

### Fix
- Moved `const lines2 = content.split('\n')` outside the loop — array is built once and mutated in place across all iterations
- Removed per-iteration `content = lines2.join('\n')` assignments inside the loop
- Single `content = lines2.join('\n')` after the loop, only when `successfullyAdded.length > 0`
- Removed the now-unnecessary `insertIdx !== -2` guard

---

## 2026-04-20 | Fix duplicate completion bug — checkbox bound multiple times
**Commit:** pending

### Bug Fixed
- Checking a task off fired multiple completions (4x "Book hotel Milano" in Done log)
- Root cause: `bind()` and `bindSingleTask()` both attached click listeners to the same `.chk` element with no guard — `restoreQuickAddTasks()` runs after `bind()` and re-binds already-bound checkboxes; any re-call to `bind()` stacks another listener on top
- Each extra listener fired independently → one click = multiple completions, multiple Done log entries

### Fix
- Added `data-bound` guard to `.chk` in `bind()`: `if(chkEl && !chkEl.dataset.bound)` — sets `chkEl.dataset.bound = '1'` before attaching listener
- Same guard added to `bindSingleTask()` for quick-add tasks
- Once a `.chk` is bound, no subsequent call to either function can attach another listener

---

## 2026-04-19 | Unified auto-sync engine + sticky notifications (v2.7)
**Commit:** `d55067d` (pending push)

### Problems Fixed
- `syncToTasksMd()` was pointing to `Productivity/TASKS.md` (404) → fixed to `Productivity/DASHBOARD-TASKS.md` (commit `b067052`)
- New tasks added via quick-add were never synced to GitHub — only queued locally indefinitely
- Completing then un-completing a task within 60s still wrote `[x]` to GitHub
- Tasks already synced as `[x]` had no way to revert if uncompleted
- `S.done` filtered by name not ID — duplicate task names caused wrong tasks to be un-done
- Quick-added tasks injected into a floating "⚡ Quick-added" card instead of their correct section
- All sync failures were silent — no user-visible error feedback

### New: Sticky Notification System
- `notify('ok'|'err'|'warn', title, msg)` — top-right, stacked, colored left border, X to dismiss
- Used for all sync outcomes: success, failure, no-token warning
- Completely separate from XP toast (bottom-right) — no interference

### New: Unified `syncDashboardTasks()`
- Single function, single GitHub PUT, handles three ops atomically:
  1. Append new tasks from `yl_quickadd` queue → correct section in `DASHBOARD-TASKS.md`
  2. Mark completions `[x]` (after 60s buffer elapses)
  3. Revert un-completions back to original marker (`[!]`, `[>]`, `[ ]`)
- `syncToTasksMd()` kept as alias for backward compatibility

### New: `normSection()` — fuzzy section matching
- Strips leading emoji and trailing parentheticals before comparing
- `"Admin & Finance"` matches `"### 💰 Admin & Finance"` automatically
- New sections not found in MD → auto-created at bottom of correct `##` block

### New: 60s completion buffer
- `scheduleCompletionSync(taskId, name, origMarker)` — starts 60s countdown on check
- `cancelOrRevertCompletion(taskId, name)` — cancels if still in buffer, or queues revert if already synced
- `data-orig-marker` stored on task element at completion time for accurate revert

### New: `injectQuickAddTask()` — section-aware injection
- Now finds correct `.pc` card by matching project name to `.pc-title` (normalised)
- Falls back to floating "Quick-added" card only for unassigned/unmatched sections
- Floating card subtitle changed to "Syncing to DASHBOARD-TASKS.md…"

### Fix: ID-based S.done filtering
- `uncompleteTask()`, checkbox handler in `bind()`, and `bindSingleTask()` — all three now filter by `id` not `name`
- Prevents duplicate-name tasks from interfering with each other

### Removed
- `beforeunload` sync trigger — replaced by auto-sync pipeline
- `updateSyncQueueBadge()` on DOMContentLoaded — shows pending count on Sync button at load

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
