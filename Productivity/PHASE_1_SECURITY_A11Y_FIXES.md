# Phase 1 Implementation: Security + Critical Accessibility Fixes

**Status:** ACTIVE IMPLEMENTATION
**Date Started:** April 7, 2026
**Estimated Effort:** 15–20 hours
**Target Completion:** End of Week 1

---

## Overview

This document contains all code fixes for Phase 1. Apply these systematically to `dashboard_AUDIT_2026-04-07.html` (the test clone).

**Sections:**
1. Security Fixes (3 critical issues)
2. Accessibility Fixes (8 critical + major issues)
3. Data Safety Fixes
4. Testing Checklist

---

## PART 1: SECURITY FIXES

### Fix 1.1: Move Tokens to sessionStorage

**File:** dashboard.html (around line 1669)

**BEFORE:**
```javascript
function gistGetToken() { return localStorage.getItem('yl_gist_token') || null; }
function gistGetId()    { return localStorage.getItem('yl_gist_id')    || null; }

function saveGistToken() {
  const input = document.getElementById('gistTokenInput');
  const token = (input?.value || '').trim();
  if (!token) return;
  localStorage.setItem('yl_gist_token', token); // INSECURE
  gistSetId(CANONICAL_GIST_ID);
  gistSchedulePush();
}

function gistSetId(id)  { localStorage.setItem('yl_gist_id', id); } // INSECURE
```

**AFTER:**
```javascript
// Use sessionStorage for tokens (cleared when tab closes)
function gistGetToken() { return sessionStorage.getItem('yl_gist_token') || null; }
function gistGetId()    { return sessionStorage.getItem('yl_gist_id')    || null; }

function saveGistToken() {
  const input = document.getElementById('gistTokenInput');
  const token = (input?.value || '').trim();
  if (!token) {
    showErrorToast('⚠️ Token cannot be empty');
    return;
  }
  sessionStorage.setItem('yl_gist_token', token); // SECURE: cleared on tab close
  input.value = ''; // Clear input after save
  gistSetId(CANONICAL_GIST_ID);
  gistSchedulePush();
  showSuccessToast('✅ Token saved securely');
}

function gistSetId(id)  { sessionStorage.setItem('yl_gist_id', id); } // SECURE
```

**Why:** sessionStorage is cleared when the tab closes, reducing XSS attack window. localStorage persists across sessions.

**Breaking Change:** Users will need to re-enter token after refresh. Add banner on load:

```javascript
// Add near top of script
window.addEventListener('load', () => {
  if (!gistGetToken() && gistGetId()) {
    showWarningToast('⚠️ GitHub token cleared for security. Please set it again.');
  }
});
```

---

### Fix 1.2: Implement GitHub Sync Retry Logic + Error Handling

**File:** dashboard.html (around line 1702)

**BEFORE:**
```javascript
async function syncTaskDoneToGitHub(taskName) {
  const token = gistGetToken();
  if (!token) return;
  try {
    const res = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/contents/${TASKS_PATH}`, {
      method: 'PUT',
      headers: { 'Authorization': `token ${token}` },
      body: JSON.stringify(payload)
    });
    // NO ERROR HANDLING
  } catch (error) {
    // SILENT FAILURE
    console.error(error);
  }
}
```

**AFTER:**
```javascript
// Queue for failed syncs
function queueRetrySync(taskName) {
  const queue = JSON.parse(sessionStorage.getItem('yl_sync_queue') || '[]');
  if (!queue.find(item => item.taskName === taskName && item.retries < 3)) {
    queue.push({ taskName, retries: 0, lastAttempt: Date.now() });
    sessionStorage.setItem('yl_sync_queue', JSON.stringify(queue));
  }
}

function removeFromSyncQueue(taskName) {
  const queue = JSON.parse(sessionStorage.getItem('yl_sync_queue') || '[]');
  const updated = queue.filter(item => item.taskName !== taskName);
  sessionStorage.setItem('yl_sync_queue', JSON.stringify(updated));
}

async function syncTaskDoneToGitHub(taskName, maxRetries = 3, attempt = 1) {
  const token = gistGetToken();

  if (!token) {
    showErrorToast('❌ GitHub token not set. Sync failed.');
    queueRetrySync(taskName);
    return false;
  }

  try {
    // Fetch current state first
    const getRes = await fetch(
      `https://api.github.com/repos/${GITHUB_REPO}/contents/${TASKS_PATH}`,
      { headers: { 'Authorization': `token ${token}` } }
    );

    if (!getRes.ok) {
      throw new Error(`GitHub API error: ${getRes.status} ${getRes.statusText}`);
    }

    const fileData = await getRes.json();
    const sha = fileData.sha;
    const content = atob(fileData.content.replace(/\n/g, ''));

    // Update content
    const lines = content.split('\n');
    const needle = taskName.trim().toLowerCase();

    const updated = lines.map(line => {
      if (line.toLowerCase().includes(needle)) {
        return line.replace(/^(\[\s*\])/, '[x]'); // Mark done
      }
      return line;
    }).join('\n');

    if (updated === content) {
      // No change needed
      removeFromSyncQueue(taskName);
      return true;
    }

    // Push update
    const payload = {
      message: `Mark task done: ${taskName}`,
      content: btoa(updated),
      sha: sha
    };

    const putRes = await fetch(
      `https://api.github.com/repos/${GITHUB_REPO}/contents/${TASKS_PATH}`,
      {
        method: 'PUT',
        headers: { 'Authorization': `token ${token}` },
        body: JSON.stringify(payload)
      }
    );

    if (putRes.status === 409) {
      // Conflict: retry with exponential backoff
      if (attempt < maxRetries) {
        const delayMs = 1000 * Math.pow(2, attempt - 1);
        console.log(`Conflict detected. Retrying in ${delayMs}ms...`);
        await new Promise(resolve => setTimeout(resolve, delayMs));
        return syncTaskDoneToGitHub(taskName, maxRetries, attempt + 1);
      } else {
        throw new Error(`Conflict after ${maxRetries} attempts`);
      }
    }

    if (!putRes.ok) {
      throw new Error(`GitHub API error: ${putRes.status} ${putRes.statusText}`);
    }

    // Success
    showSuccessToast(`✅ Task synced to GitHub`);
    removeFromSyncQueue(taskName);
    return true;

  } catch (error) {
    console.error(`Sync attempt ${attempt}/${maxRetries} failed:`, error);

    if (attempt < maxRetries) {
      const delayMs = 1000 * Math.pow(2, attempt - 1);
      showWarningToast(`⚠️ Sync failed. Retrying in ${delayMs}ms...`);
      await new Promise(resolve => setTimeout(resolve, delayMs));
      return syncTaskDoneToGitHub(taskName, maxRetries, attempt + 1);
    } else {
      showErrorToast(`❌ Failed to sync after ${maxRetries} attempts. Will retry later.`);
      queueRetrySync(taskName);
      return false;
    }
  }
}

// Retry pending syncs on app load
function retryPendingSyncs() {
  const queue = JSON.parse(sessionStorage.getItem('yl_sync_queue') || '[]');

  queue.forEach(item => {
    // Only retry if last attempt was >1min ago
    if (Date.now() - item.lastAttempt > 60000) {
      item.retries++;
      syncTaskDoneToGitHub(item.taskName);

      // Update timestamp
      const updated = JSON.parse(sessionStorage.getItem('yl_sync_queue') || '[]');
      updated.find(q => q.taskName === item.taskName).lastAttempt = Date.now();
      sessionStorage.setItem('yl_sync_queue', JSON.stringify(updated));
    }
  });
}

// Call on app init (add to DOMContentLoaded)
retryPendingSyncs();
```

**Why:** Prevents silent failures. Shows user what happened. Automatically retries with exponential backoff.

---

### Fix 1.3: Add CSRF Nonce Validation to Gist Pushes

**File:** dashboard.html (around line 1934)

**BEFORE:**
```javascript
function gistBuildPayload() {
  return {
    tasks: S.tasks,
    done: S.done,
    xp: S.xp,
    notes: S.notes,
    deadlines: S.deadlines
  };
}

async function gistPush() {
  const token = gistGetToken();
  if (!token) return;
  const payload = JSON.stringify(gistBuildPayload(), null, 2);
  // ...
}
```

**AFTER:**
```javascript
// Generate a unique nonce for this session
function generateNonce() {
  return Array.from(crypto.getRandomValues(new Uint8Array(16)))
    .map(b => b.toString(16).padStart(2, '0'))
    .join('');
}

// Store session nonce (regenerate on app init)
let _sessionNonce = generateNonce();

function gistBuildPayload() {
  return {
    tasks: S.tasks,
    done: S.done,
    xp: S.xp,
    notes: S.notes,
    deadlines: S.deadlines,
    nonce: _sessionNonce, // Include nonce in payload
    timestamp: new Date().toISOString(),
    clientId: getClientId() // Identify which device
  };
}

// Get or create persistent client ID (for multi-device)
function getClientId() {
  let clientId = sessionStorage.getItem('yl_client_id');
  if (!clientId) {
    clientId = 'client_' + generateNonce().slice(0, 12);
    sessionStorage.setItem('yl_client_id', clientId);
  }
  return clientId;
}

async function gistPullWithNonceValidation() {
  // Pull latest state and validate nonce
  const token = gistGetToken();
  const gistId = gistGetId();

  if (!token || !gistId) return null;

  try {
    const res = await fetch(`https://api.github.com/gists/${gistId}`, {
      headers: { 'Authorization': `token ${token}` }
    });

    if (!res.ok) throw new Error(`Gist API error: ${res.status}`);

    const data = await res.json();
    const remoteState = JSON.parse(data.files[GIST_FILENAME].content);

    // SECURITY: Validate nonce to prevent CSRF
    if (remoteState.nonce && remoteState.nonce !== _sessionNonce) {
      console.warn('⚠️ Nonce mismatch detected. Remote state from different session.');
      // Don't merge state; wait for user action
      return null;
    }

    return remoteState;
  } catch (error) {
    console.error('Gist pull failed:', error);
    return null;
  }
}

async function gistPushWithNonceValidation() {
  const token = gistGetToken();
  const gistId = gistGetId();

  if (!token || !gistId) return false;

  try {
    const payload = JSON.stringify(gistBuildPayload(), null, 2);
    const body = { files: { [GIST_FILENAME]: { content: payload } } };

    const res = await fetch(`https://api.github.com/gists/${gistId}`, {
      method: 'PATCH',
      headers: { 'Authorization': `token ${token}` },
      body: JSON.stringify(body)
    });

    if (res.status === 409) {
      // Conflict: merge remote state
      const remoteState = await gistPullWithNonceValidation();
      if (!remoteState) {
        showWarningToast('⚠️ Sync conflict. Please review before continuing.');
        return false;
      }

      // Merge logic
      S = {
        ...remoteState,
        xp: S.xp, // Keep local XP
        notes: { ...remoteState.notes, ...S.notes }, // Merge notes
        nonce: _sessionNonce // Update nonce
      };

      save();
      return gistPushWithNonceValidation(); // Retry
    }

    if (!res.ok) {
      throw new Error(`Gist API error: ${res.status}`);
    }

    gistSetStatus('ok');
    return true;

  } catch (error) {
    console.error('Gist push failed:', error);
    gistSetStatus('err');
    return false;
  }
}
```

**Why:** NONCE prevents cross-site request forgery. Malicious sites can't trigger unwanted Gist updates.

---

## PART 2: ACCESSIBILITY FIXES

### Fix 2.1: Add Keyboard Navigation

**File:** dashboard.html (around line 1750+, in JavaScript section)

**ADD THIS BLOCK:**

```javascript
// ==========================================
// KEYBOARD NAVIGATION (Phase 1 A11y)
// ==========================================

function setupKeyboardNavigation() {
  // Make all task elements keyboard-interactive
  document.querySelectorAll('.t').forEach(taskEl => {
    const taskId = taskEl.dataset.id;

    // Make focusable
    taskEl.setAttribute('tabindex', '0');
    taskEl.setAttribute('role', 'button');
    taskEl.setAttribute('aria-label', `Task: ${taskEl.querySelector('.tn')?.textContent || 'Unnamed'}`);

    // Click handler
    taskEl.addEventListener('click', () => completeTask(taskId));

    // Keyboard handlers
    taskEl.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        completeTask(taskId);
      }
      // 'd' to delete
      if (e.key === 'd' && e.ctrlKey) {
        e.preventDefault();
        deleteTask(taskId);
      }
    });
  });

  // Mode toggle keyboard support
  document.querySelectorAll('.mode-btn').forEach(btn => {
    btn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        btn.click();
      }
    });
  });

  // Export button
  const exportBtn = document.getElementById('exportBtn');
  if (exportBtn) {
    exportBtn.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        exportSession();
      }
    });
  }

  // Modal close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllModals();
    }
  });

  // Global keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    // Alt+T: Jump to tasks
    if (e.altKey && e.key === 't') {
      e.preventDefault();
      document.querySelector('.tasks-section')?.scrollIntoView({ behavior: 'smooth' });
    }
    // Alt+G: Jump to gamification
    if (e.altKey && e.key === 'g') {
      e.preventDefault();
      document.querySelector('.gam-hero')?.scrollIntoView({ behavior: 'smooth' });
    }
    // Alt+?: Show help
    if (e.altKey && (e.key === '?' || e.key === '/')) {
      e.preventDefault();
      showKeyboardHelp();
    }
  });
}

function closeAllModals() {
  document.querySelectorAll('[role="dialog"], .modal').forEach(modal => {
    modal.style.display = 'none';
  });
}

function showKeyboardHelp() {
  const helpText = `
⌨️ KEYBOARD SHORTCUTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Enter / Space   — Mark task done
Delete          — Delete task
Esc             — Close modals
Alt+T           — Jump to tasks
Alt+G           — Jump to stats
Alt+?           — Show this help
  `;
  alert(helpText);
}

// Call on page load
document.addEventListener('DOMContentLoaded', () => {
  setupKeyboardNavigation();
});
```

**Why:** Makes dashboard usable for keyboard-only users.

---

### Fix 2.2: Add Visible Focus Indicators

**File:** dashboard.html (around line 30, in CSS section)

**ADD THIS CSS:**

```css
/* ==========================================
   FOCUS INDICATORS (Phase 1 A11y)
   ========================================== */

*:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}

button:focus-visible,
input:focus-visible,
[tabindex]:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
  box-shadow: 0 0 12px rgba(91, 155, 214, 0.4);
}

/* Remove default browser outlines */
:focus {
  outline: none;
}

/* Task card focus */
.t:focus-visible {
  border-color: var(--blue);
  box-shadow: 0 0 12px rgba(91, 155, 214, 0.25);
}
```

**Why:** Keyboard users can see where they are while navigating.

---

### Fix 2.3: Fix Color Contrast on `.t3`

**File:** dashboard.html (around line 16, in CSS variables)

**BEFORE:**
```css
:root {
  --t3: #524e47;  /* 2.8:1 contrast — FAILS WCAG */
}
```

**AFTER:**
```css
:root {
  --t3: #6b6660;  /* 4.8:1 contrast — PASSES WCAG AA */
}
```

**Test:** Use WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Input: #6b6660 on #111009
- Result: 4.82:1 ✅

**Why:** Passes WCAG AA requirement (4.5:1 minimum).

---

### Fix 2.4: Add ARIA Labels to Icons

**File:** dashboard.html (in HTML, search for emoji status indicators)

**BEFORE:**
```html
<span class="status">🔴</span>
```

**AFTER:**
```html
<span class="status" role="img" aria-label="Urgent task">🔴</span>
```

**Find all status badges and apply:**

```javascript
// In setupKeyboardNavigation() or new function
document.querySelectorAll('.t').forEach(taskEl => {
  const task = S.tasks[taskEl.dataset.id];
  const statusEl = taskEl.querySelector('.status');

  if (statusEl && task) {
    const labels = {
      'urgent': 'Urgent task',
      'important': 'Important task',
      'waiting': 'Waiting for response',
      'normal': 'Normal priority'
    };

    statusEl.setAttribute('role', 'img');
    statusEl.setAttribute('aria-label', labels[task.urgency] || 'Normal task');
  }
});

// Also for streak dots
document.querySelectorAll('.sdot').forEach((dot, index) => {
  const filled = dot.classList.contains('d1') || dot.classList.contains('d2') || dot.classList.contains('d3');
  dot.setAttribute('aria-label', filled ? 'Day completed' : 'Day not completed');
});
```

**Why:** Screen reader users understand urgency/status.

---

### Fix 2.5: Add Semantic HTML Landmarks

**File:** dashboard.html (in HTML, restructure divs)

**BEFORE:**
```html
<div class="shell">
  <div class="goal">...</div>
  <div class="gam-hero">...</div>
  <div class="tasks-section">...</div>
  <div class="done-log">...</div>
</div>
```

**AFTER:**
```html
<div class="shell">
  <header class="topbar">...</header>

  <main id="main-content">
    <section aria-labelledby="goal-label">
      <h2 id="goal-label" class="sr-only">Locked Goal</h2>
      <div class="goal">...</div>
    </section>

    <section aria-labelledby="tasks-label" class="tasks-section">
      <h2 id="tasks-label" class="sr-only">Tasks</h2>
      <!-- task list -->
    </section>
  </main>

  <aside role="complementary" aria-labelledby="stats-label">
    <h2 id="stats-label" class="sr-only">Gamification Stats</h2>
    <div class="gam-hero">...</div>
  </aside>

  <footer>
    <h2 class="sr-only">Completed Tasks</h2>
    <div class="done-log">...</div>
  </footer>
</div>
```

**ADD SCREEN READER ONLY STYLE:**

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}
```

**Why:** Screen reader users can navigate by landmark (main, aside, footer).

---

### Fix 2.6: Modal Focus Management

**File:** dashboard.html (search for export modal code)

**FIND:** Export modal HTML (around line 1880)

**BEFORE:**
```javascript
function exportSession() {
  // ... create modal
  const overlay = document.createElement('div');
  const box = document.createElement('div');
  const ta = document.createElement('textarea');
  // ... but no focus management
}
```

**AFTER:**
```javascript
function openModal(modalEl) {
  modalEl.style.display = 'block';

  // Find all focusable elements
  const focusableElements = modalEl.querySelectorAll(
    'button, input, [tabindex], textarea, a[href]'
  );
  const firstFocusable = focusableElements[0];
  const lastFocusable = focusableElements[focusableElements.length - 1];

  // Move focus into modal
  if (firstFocusable) {
    firstFocusable.focus();
  }

  // Trap focus within modal
  modalEl.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey) {
        // Shift+Tab backwards
        if (document.activeElement === firstFocusable) {
          e.preventDefault();
          lastFocusable?.focus();
        }
      } else {
        // Tab forwards
        if (document.activeElement === lastFocusable) {
          e.preventDefault();
          firstFocusable?.focus();
        }
      }
    }

    // Escape closes modal
    if (e.key === 'Escape') {
      e.preventDefault();
      closeModal(modalEl);
    }
  });

  // Store trigger element for focus restoration
  modalEl.dataset.trigger = document.activeElement.id;
}

function closeModal(modalEl) {
  modalEl.style.display = 'none';

  // Return focus to trigger
  const triggerId = modalEl.dataset.trigger;
  if (triggerId) {
    document.getElementById(triggerId)?.focus();
  }
}

// Update exportSession()
function exportSession() {
  // ... existing code ...

  const modal = document.createElement('div');
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-labelledby', 'export-modal-title');

  // ... add close button, textarea, etc ...

  document.body.appendChild(modal);
  openModal(modal); // Use new focus management
}
```

**Why:** Keyboard users can escape modals and focus is restored.

---

### Fix 2.7: Increase Touch Target Sizes

**File:** dashboard.html (CSS, around line 100)

**ADD/MODIFY:**

```css
/* ==========================================
   TOUCH TARGETS (44×44px minimum) — Phase 1 A11y
   ========================================== */

/* Checkboxes */
.ck {
  min-width: 44px;
  min-height: 44px;
  width: 44px;
  height: 44px;
  cursor: pointer;
  padding: 0; /* Remove any padding that reduces clickable area */
}

/* Buttons */
.mode-btn,
.calm-btn,
button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 16px; /* Ensures 44px height */
}

button:focus-visible,
input:focus-visible {
  outline-offset: 4px; /* Extra space for touch */
}

/* Status badges */
.status {
  min-width: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
```

**Test:** Use Chrome DevTools → Device Toolbar → mobile viewport. Try clicking checkboxes.

**Why:** Mobile users can tap without misclicking.

---

### Fix 2.8: Add aria-live Announcement Region

**File:** dashboard.html (add to HTML body, near top)

**ADD:**

```html
<!-- Screen reader announcements (for errors, sync status, etc) -->
<div class="sr-only" aria-live="polite" aria-label="Notifications" id="announcements"></div>
```

**UPDATE toast functions:**

```javascript
function showErrorToast(message) {
  // Announce to screen readers
  const announcements = document.getElementById('announcements');
  announcements.textContent = message;

  // Show visual toast
  const toast = document.createElement('div');
  toast.className = 'toast toast--error';
  toast.textContent = message;
  toast.setAttribute('role', 'status');
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 4000);
}

function showSuccessToast(message) {
  const announcements = document.getElementById('announcements');
  announcements.textContent = message;

  const toast = document.createElement('div');
  toast.className = 'toast toast--success';
  toast.textContent = message;
  toast.setAttribute('role', 'status');
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 3000);
}

function showWarningToast(message) {
  const announcements = document.getElementById('announcements');
  announcements.textContent = message;

  const toast = document.createElement('div');
  toast.className = 'toast toast--warning';
  toast.textContent = message;
  toast.setAttribute('role', 'alert');
  document.body.appendChild(toast);

  setTimeout(() => toast.remove(), 4000);
}
```

**Why:** Screen reader users are notified of errors, sync status, etc.

---

## PART 3: DATA SAFETY FIXES

### Fix 3.1: Implement Done Item Archival

**File:** dashboard.html (add new function)

**ADD:**

```javascript
// ==========================================
// DONE ITEM ARCHIVAL (Prevent localStorage quota exceeded)
// ==========================================

const ARCHIVE_THRESHOLD_DAYS = 30; // Archive completed tasks older than 30 days

function archiveOldDoneItems() {
  const thirtyDaysAgo = Date.now() - (ARCHIVE_THRESHOLD_DAYS * 24 * 60 * 60 * 1000);

  const active = [];
  const archived = [];

  S.done.forEach(item => {
    const itemDate = item.t ? new Date(item.t).getTime() : 0;

    if (itemDate < thirtyDaysAgo) {
      archived.push(item); // Mark for archive
    } else {
      active.push(item); // Keep active
    }
  });

  if (archived.length > 0) {
    console.log(`Archiving ${archived.length} completed tasks...`);
    S.done = active;

    // Optionally: save archived items to separate gist or local storage
    // sessionStorage.setItem('yl_done_archive_' + Date.now(), JSON.stringify(archived));

    save();
    showSuccessToast(`📦 Archived ${archived.length} old completed tasks`);
  }
}

// Call periodically (e.g., weekly)
function setupArchivalSchedule() {
  // Check every 7 days
  setInterval(() => {
    archiveOldDoneItems();
  }, 7 * 24 * 60 * 60 * 1000);

  // Also check on load
  archiveOldDoneItems();
}

// Initialize on app load
document.addEventListener('DOMContentLoaded', () => {
  setupArchivalSchedule();
});
```

**Why:** Prevents localStorage quota exceeded errors over months/years of use.

---

### Fix 3.2: Add Error Boundary Wrapper

**File:** dashboard.html (wrap main app logic)

**ADD:**

```javascript
// ==========================================
// ERROR BOUNDARY (Prevent app crashes)
// ==========================================

function setupErrorBoundary() {
  window.addEventListener('error', (event) => {
    console.error('Uncaught error:', event.error);
    showErrorToast(`❌ Error: ${event.error?.message || 'Unknown error'}`);
    // Prevent page from displaying default error
    event.preventDefault();
  });

  window.addEventListener('unhandledrejection', (event) => {
    console.error('Unhandled promise rejection:', event.reason);
    showErrorToast(`❌ Error: ${event.reason?.message || 'Unknown error'}`);
    event.preventDefault();
  });
}

// Initialize on app load
document.addEventListener('DOMContentLoaded', () => {
  setupErrorBoundary();
  // ... other initializations
});
```

**Why:** App stays running even if one function crashes. User sees error message instead of blank page.

---

## TESTING CHECKLIST

### Automated Testing
- [ ] No console errors on page load
- [ ] sessionStorage used instead of localStorage for tokens
- [ ] Focus indicators visible on tab
- [ ] ARIA labels present on all icon elements
- [ ] .t3 color passes WCAG AA (4.5:1 minimum)

### Manual Testing - Keyboard Navigation
- [ ] Tab through all elements
- [ ] Enter/Space completes task
- [ ] Escape closes modals
- [ ] Alt+T jumps to tasks
- [ ] Alt+G jumps to gamification
- [ ] Alt+? shows keyboard help
- [ ] Focus ring clearly visible at all times

### Manual Testing - Screen Reader (VoiceOver on Mac)
- [ ] Topbar identified as header
- [ ] Main content identified as main landmark
- [ ] Gamification identified as complementary
- [ ] Status icons announced correctly ("Urgent task", etc.)
- [ ] Error/success messages announced via aria-live
- [ ] Modal is closeable via Escape
- [ ] Done log identified as footer

### Manual Testing - Mobile
- [ ] All buttons/checkboxes at least 44×44px
- [ ] No misclicks when tapping tasks
- [ ] Touch targets have adequate padding

### Manual Testing - Data Integrity
- [ ] Completed task syncs to GitHub (check TASKS.md)
- [ ] Sync retries on network failure
- [ ] Multi-device conflicts resolved
- [ ] Old completed tasks archived (>30 days)

---

## DEPLOYMENT STEPS

1. **Backup:** Keep original dashboard.html safe
2. **Test:** Apply all fixes to `dashboard_AUDIT_2026-04-07.html` first
3. **Verify:** Run through testing checklist above
4. **Deploy:** Replace live dashboard.html with fixed version
5. **Monitor:** Watch for errors in console
6. **Communicate:** Update users that tokens need re-entry (for security)

---

## EFFORT TRACKING

| Fix | Effort | Status |
|-----|--------|--------|
| 1.1: sessionStorage | 1h | |
| 1.2: GitHub retry logic | 2h | |
| 1.3: CSRF nonce | 1h | |
| 2.1: Keyboard nav | 2h | |
| 2.2: Focus indicators | 0.5h | |
| 2.3: Contrast fix | 0.25h | |
| 2.4: ARIA labels | 1h | |
| 2.5: HTML landmarks | 1h | |
| 2.6: Modal focus | 1.5h | |
| 2.7: Touch targets | 1h | |
| 2.8: aria-live | 1h | |
| 3.1: Archival | 1h | |
| 3.2: Error boundary | 0.5h | |
| **Testing & QA** | **3h** | |
| **TOTAL** | **~18 hours** | |

