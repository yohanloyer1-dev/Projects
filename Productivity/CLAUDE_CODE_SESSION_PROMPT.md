# ~~Claude Code Session Prompt — Dashboard Fix F~~
> ⚠️ **COMPLETED & ARCHIVED — 2026-05-03**  
> All fixes (A–F) are done. Do NOT use this as a session briefing.  
> Current dashboard version: v3.8. Check `git log` for actual state.

**Date updated:** 2026-05-02
**Prepared by:** Claude Sonnet (Cowork session)
**Target file:** `~/Projects/Productivity/dashboard.html`
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
  Token stored in **localStorage** at `yl_gist_token`.
- **Task DOM structure:** Tasks are hardcoded HTML
  `<div class="t [urg|hi|cl]" data-id="..." data-xp="..." data-project="...">`.
  No dynamic task creation from a data model.
- **`notify()` function exists** — use it for user-visible alerts, not `alert()` or `console.error()`.
- **Pre-commit hook is live** — added 2026-04-20, commit `7232546`. Do not bypass.

---

## Already Fixed (DO NOT RE-DO)

All fixes below are verified live as of 2026-05-02. Confirm before touching related code:

### Fixed #1 — `renderBrief()` mode-aware ranking
```bash
grep -n "activeViews" ~/Projects/Productivity/dashboard.html
# Should return a line around 2958
```
Brief now scores only tasks from the active mode's views.

### Fixed #2 — DTN Someday/Waiting cap
```bash
grep -n "Math.min(score, 50)" ~/Projects/Productivity/dashboard.html
```
Someday/Waiting tasks can no longer outscore urgent tasks via stale deadlines.

### Fixed #3 — Fix B: Visible sync error notifications (commit `4199358`)
```bash
grep -n "notify.*token invalid\|notify.*Sync conflict\|notify.*GitHub API" ~/Projects/Productivity/dashboard.html
```
`syncDashboardTasks`, `gistPush`, `gistPull` all surface errors via `notify()`.

### Fixed #4 — Fix C: Dynamic Claude Tasks tab (commit `ec12ed2`, patched `595dcf6`)
```bash
grep -n "function renderClaudeTasks" ~/Projects/Productivity/dashboard.html
```
`renderClaudeTasks()` is live. Hardcoded cards removed. Wired into `updateUI` and `setMode`.

### Fixed #5 — Fix D: Dead queue call disabled (commit `ec12ed2`)
```bash
grep -n "fetchClaudeQueue\|syncQueueResults" ~/Projects/Productivity/dashboard.html
```
`fetchClaudeQueue` call and `syncQueueResults` timeout are both commented out.

### Fixed #6 — Fix E: `dtnSkipIdx` divide-by-zero guard (commit `ec12ed2`)
```bash
grep -n "scored.length.*return null" ~/Projects/Productivity/dashboard.html
```
Guard exists in `dtnGetTopTask()`.

### Fix A — CLOSED (intentional revert, commit `1988e82`)
Token stays in localStorage. sessionStorage required re-entry every browser session — wrong
tradeoff for a single-user personal tool on GitHub Pages. No external scripts, no CDN.
The no-token warning notification was kept (useful for new device setup).

---

## Only Remaining Fix — Apply This Now

### Fix F — Drag-and-drop section reordering
**Priority:** Medium — UX improvement, no data risk  
**Estimated time:** 30–45 min

Users want to drag entire task sections (e.g. move "Japan Trip" above "Admin & Finance") to
reprioritize them within a view. Order persists in localStorage so it survives refresh.

**Verify it's not already done:**
```bash
grep -n "section-block\|initSectionDrag\|yl_section_orders" ~/Projects/Productivity/dashboard.html
# Should return nothing — if it does, this fix is already applied, stop here
```

---

#### Step 1 — Understand the section DOM structure

Sections use `<div class="sh">` headers. Each section = the `.sh` div + all sibling `.t` task
rows that follow it until the next `.sh`. Sections live inside view containers.

Verify:
```bash
grep -n 'class="sh"' ~/Projects/Productivity/dashboard.html | head -20
```

**Personal view sections (approximate line numbers):**
- Strategy & Vision (~1021)
- Admin & Finance (~1052)
- Health (~1089)
- Real Estate & Travel (~1120)
- Tech & Accounts (~1172)
- Network & Others (~1199)
- Productivity (~1214)

**Freelance view sections:** Clients (~1236), Agency (~1279)  
**Work view sections:** Gorgias Day Job (~1319)

---

#### Step 2 — Wrap each section in a `section-block` div (HTML change)

Each section needs to be wrapped so the header + its tasks move as one unit.

For every section in `#view-personal`, `#view-freelance`, `#view-pro`:

**Before:**
```html
<div class="sh"><div class="sh-lbl">Admin &amp; Finance</div></div>
<div class="t urg" data-id="..." ...>...</div>
<div class="t hi" data-id="..." ...>...</div>
```

**After:**
```html
<div class="section-block" data-section-id="admin-finance">
  <div class="sh"><div class="sh-lbl">Admin &amp; Finance</div></div>
  <div class="t urg" data-id="..." ...>...</div>
  <div class="t hi" data-id="..." ...>...</div>
</div>
```

`data-section-id` = kebab-case slug of the section name. Use these exact IDs:

| Section | `data-section-id` |
|---|---|
| Strategy & Vision | `strategy-vision` |
| Admin & Finance | `admin-finance` |
| Health | `health` |
| Real Estate & Travel | `real-estate-travel` |
| Tech & Accounts | `tech-accounts` |
| Network & Others | `network-others` |
| Productivity | `productivity` |
| Clients (Freelance) | `clients` |
| Agency (Freelance) | `agency` |
| Gorgias Day Job (Work) | `gorgias-day-job` |

**Important:** The closing `</div>` for each section-block goes immediately before the next
`.sh` div (or before the end of the view container).

---

#### Step 3 — Add JavaScript functions

Add these functions near the other utility functions (e.g. near `dtnRender` or `renderClaudeTasks`):

```javascript
// ── Section drag-and-drop ──────────────────────────────────────────────────

function saveSectionOrder(viewId) {
  if (!viewId) return;
  const view = document.getElementById(viewId);
  if (!view) return;
  const order = Array.from(view.querySelectorAll(':scope > .section-block'))
    .map(b => b.dataset.sectionId);
  const orders = JSON.parse(localStorage.getItem('yl_section_orders') || '{}');
  orders[viewId] = order;
  localStorage.setItem('yl_section_orders', JSON.stringify(orders));
}

function restoreSectionOrders() {
  const orders = JSON.parse(localStorage.getItem('yl_section_orders') || '{}');
  Object.entries(orders).forEach(([viewId, order]) => {
    const view = document.getElementById(viewId);
    if (!view) return;
    order.forEach(sectionId => {
      const block = view.querySelector(`.section-block[data-section-id="${sectionId}"]`);
      if (block) view.appendChild(block);
    });
  });
}

function initSectionDrag() {
  document.querySelectorAll('.section-block').forEach(block => {
    const header = block.querySelector('.sh');
    if (!header) return;

    header.setAttribute('draggable', 'true');

    header.addEventListener('dragstart', e => {
      e.dataTransfer.effectAllowed = 'move';
      e.dataTransfer.setData('text/plain', block.dataset.sectionId);
      block.classList.add('dragging');
    });

    header.addEventListener('dragend', () => {
      block.classList.remove('dragging');
      document.querySelectorAll('.section-block').forEach(b => b.classList.remove('drag-over'));
    });

    block.addEventListener('dragover', e => {
      e.preventDefault();
      e.dataTransfer.dropEffect = 'move';
      block.classList.add('drag-over');
    });

    block.addEventListener('dragleave', e => {
      // Only remove class if leaving the block itself, not a child
      if (!block.contains(e.relatedTarget)) block.classList.remove('drag-over');
    });

    block.addEventListener('drop', e => {
      e.preventDefault();
      block.classList.remove('drag-over');
      const draggedId = e.dataTransfer.getData('text/plain');
      const draggedBlock = document.querySelector(`.section-block[data-section-id="${draggedId}"]`);
      if (!draggedBlock || draggedBlock === block) return;
      block.parentNode.insertBefore(draggedBlock, block);
      saveSectionOrder(block.closest('[id^="view-"]')?.id);
    });
  });
}

function resetSectionOrder(viewId) {
  const orders = JSON.parse(localStorage.getItem('yl_section_orders') || '{}');
  delete orders[viewId];
  localStorage.setItem('yl_section_orders', JSON.stringify(orders));
  location.reload();
}
```

---

#### Step 4 — Add CSS

Add to the stylesheet (near other drag/interaction styles):

```css
.section-block.dragging { opacity: 0.45; }
.section-block.drag-over { outline: 2px solid var(--accent); outline-offset: -2px; border-radius: 6px; }
.sh[draggable="true"] { cursor: grab; user-select: none; }
.sh[draggable="true"]:active { cursor: grabbing; }
```

---

#### Step 5 — Wire into init

Find where `dtnRender()` and `renderClaudeTasks()` are called at page load (around line 4716).
Add `restoreSectionOrders()` and `initSectionDrag()` immediately after:

```javascript
// existing line:
updateUI = function() { _origUpdateUI.apply(this, arguments); dtnRender(); renderClaudeTasks(); };

// add after:
restoreSectionOrders();
initSectionDrag();
```

Also add `initSectionDrag()` at the end of `setMode()` so drag handlers apply after a mode switch:

```javascript
function setMode(m) {
  // ... existing code ...
  renderClaudeTasks(); // already there
  initSectionDrag();   // add this line
}
```

---

#### Step 6 — Commit

```bash
cd ~/Projects

# Save version snapshot first (required by pre-commit hook)
cp Productivity/dashboard.html Productivity/versions/dashboard_v3.2_$(date +%Y-%m-%d)_pre-drag-sections.html

# Make edits (steps 2–5 above)

# Update changelog (prepend entry to dashboard-changelog.md)

# Stage and commit
git add Productivity/dashboard.html \
        Productivity/memory/dashboard-changelog.md \
        Productivity/versions/

git commit -m "feat: drag-and-drop section reordering with localStorage persistence"
git push origin main
```

---

## Testing Checklist

After pushing, open https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html

- [ ] Section headers show `grab` cursor on hover
- [ ] Drag "Japan Trip" above "Admin & Finance" → order updates visually
- [ ] Refresh → order persists
- [ ] Switch to Work mode → Work sections unaffected
- [ ] Switch back to Personal → Personal order still correct
- [ ] Mark a task done inside a reordered section → task disappears, section stays in place
- [ ] Notes, links, XP still work on tasks inside reordered sections
- [ ] No JS errors in DevTools console during or after drag

---

## What to IGNORE from Older Docs

`SONNET_SESSION_PROMPT.md`, `HANDOVER_PHASE_1_IMPLEMENTATION.md`, `PHASE_1_SECURITY_A11Y_FIXES.md`
were created by Haiku and contain **inaccurate code examples** that don't match the real dashboard:

- They reference `doneList`, `tasks`, `markTaskDone(task)` — none of these exist in the real file
- Fix 1.3 (CSRF nonce) — not needed for a personal single-user tool
- Fix 2.1 (IndexedDB archival) — over-engineered; `S.done` stores tiny objects, quota won't be hit

**Use this document, not the Haiku docs.**

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
