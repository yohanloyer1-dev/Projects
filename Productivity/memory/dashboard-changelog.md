# Dashboard Changelog
<!-- Running log of all changes made to dashboard.html, in reverse chronological order -->
<!-- Format: ## YYYY-MM-DD | short title | commit hash (if known) -->

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
