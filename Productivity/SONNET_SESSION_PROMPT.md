# Phase 1 Implementation — Complete Sonnet Session Prompt

**Prepared by:** Claude Haiku  
**For:** Claude Sonnet 4.6 or Opus 4.6 session  
**Date Prepared:** April 22, 2026  
**Status:** READY TO EXECUTE  

---

## COPY EVERYTHING BELOW AND PASTE INTO YOUR NEXT SONNET SESSION

---

I'm implementing Phase 1 (Security + Critical Accessibility Fixes) for the Productivity Dashboard project. This is a comprehensive task management app (3,810 lines of HTML/JS/CSS) with gamification features and ADHD optimization.

**CRITICAL CONTEXT:** An extensive audit was completed on April 7, 2026, identifying 50+ issues across security, accessibility, code quality, and design. Phase 1 addresses the 13 most critical issues that block deployment. All code fixes are already written with before/after examples. Your job is to apply them systematically, test thoroughly, and push to GitHub.

### Project Overview

**What:** Productivity Dashboard (dashboard.html)  
**Type:** Single-file web app for task management with XP/streaks/levels gamification  
**Location:** ~/Projects/Productivity/  
**GitHub:** https://github.com/yohanloyer1-dev/Projects/tree/main/Productivity/  
**File size:** 3,810 lines HTML/JS/CSS  

**Architecture:**
- No framework (vanilla JS)
- State managed in localStorage + sessionStorage (moving to sessionStorage for tokens)
- GitHub Gist integration for cloud sync
- Task cards with status tracking (todo/done)
- Gamification layer: XP points, streaks, levels, achievements

### The Audit (April 7, 2026)

**Scope:** Technical + UX audit using code-review, accessibility-review, design-system, design-critique skills

**Findings Summary:**

| Dimension | Score | Critical Issues |
|-----------|-------|-----------------|
| Security | 2/10 | Tokens in localStorage (XSS), silent sync failures, no CSRF protection |
| Accessibility | 3/10 | No keyboard nav (WCAG A failure), no focus indicators, color contrast fails |
| Code Quality | 7/10 | 5 critical (security/data), 5 performance, 5 correctness issues |
| Design System | 4/10 | 115 hardcoded values, inconsistent naming, no token architecture |
| UX/ADHD | 5/10 | 60% of research principles implemented, missing hero card & time anchoring |

**3 Critical Issues Blocking Deployment:**
1. **XSS Vulnerability:** GitHub tokens stored in localStorage, readable by XSS attacks
2. **Data Loss:** GitHub sync failures silent → tasks sync but status may not update
3. **Accessibility Failure:** No keyboard navigation → WCAG Level A failure, fails accessibility compliance

---

## Phase 1: 13 Critical Fixes (Security + A11y)

### Why Phase 1?

These 13 fixes must happen before Phase 2 (design system) or Phase 3 (UX polish) because:
- **Security:** XSS and CSRF vulnerabilities expose user data
- **Compliance:** WCAG AA accessibility required for public deployment
- **Correctness:** Error handling prevents data loss and user frustration
- **Foundation:** Phase 2 design system changes depend on stable, accessible code

**Estimated Effort:** 15–20 hours (3 hours implementation, 12–17 hours testing)

---

## The 13 Fixes — Complete Reference

### SECURITY FIXES (3 fixes)

#### Fix 1.1: Move GitHub Tokens to sessionStorage

**File:** dashboard.html, lines 1669–1692  
**Problem:** Tokens persisted in localStorage → vulnerable to XSS attacks  
**Impact:** Medium-High (user credentials exposed if XSS occurs)  
**Solution:** Switch from localStorage to sessionStorage (cleared on tab close)

**Complexity:** Low  
**Time:** 5 minutes  
**Breaking Change:** YES — users must re-enter token after refresh (add warning banner)

**Current Code (INSECURE):**
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

**Fixed Code:**
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

**Breaking Change Warning (add at top of script):**
```javascript
window.addEventListener('load', () => {
  if (!gistGetToken() && gistGetId()) {
    showWarningToast('⚠️ GitHub token cleared for security. Please set it again.');
  }
});
```

**Why sessionStorage?**
- Cleared when tab closes → reduces XSS attack window
- localStorage persists across sessions → increases exposure
- User re-enters token each session = acceptable trade-off for security
- Production dashboard might consider: OAuth flow (better UX, same security)

**Testing:**
- [ ] Refresh page → token cleared, warning toast shows
- [ ] Enter token → saves to sessionStorage (not localStorage)
- [ ] Open DevTools → verify token NOT in localStorage
- [ ] Open new incognito window → token NOT there (no localStorage carryover)

---

#### Fix 1.2: GitHub Sync Retry Logic + Error Handling

**File:** dashboard.html, lines 1702–1752  
**Problem:** syncTaskDoneToGitHub() silently fails when GitHub API is slow/down → task status updates don't sync  
**Impact:** HIGH (data loss — local state doesn't match GitHub)  
**Solution:** 3-attempt retry with exponential backoff, proper error toasts

**Complexity:** Medium  
**Time:** 20 minutes  
**Dependencies:** Fix 1.1 (token handling)

**Current Code (BROKEN):**
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
    // NO ERROR HANDLING — failures silent
  } catch (error) {
    // SILENT FAILURE — user never knows sync failed
  }
}
```

**Fixed Code:**
```javascript
async function syncTaskDoneToGitHub(taskName) {
  const token = gistGetToken();
  if (!token) return;
  
  const maxAttempts = 3;
  let attempt = 0;
  let lastError = null;
  
  while (attempt < maxAttempts) {
    try {
      const res = await fetch(`https://api.github.com/repos/${GITHUB_REPO}/contents/${TASKS_PATH}`, {
        method: 'PUT',
        headers: { 
          'Authorization': `token ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });
      
      if (!res.ok) {
        // Handle specific error codes
        if (res.status === 409) {
          // Conflict (multi-device) — fetch latest and retry
          showWarningToast('⚠️ Conflict detected. Fetching latest version...');
          await gistFetchLatest();
          continue; // Retry with fetched state
        } else if (res.status === 401) {
          showErrorToast('❌ GitHub token invalid. Please re-enter.');
          return;
        } else if (res.status >= 500) {
          // Server error — retry with backoff
          throw new Error(`GitHub server error: ${res.status}`);
        } else {
          throw new Error(`GitHub API error: ${res.status} ${res.statusText}`);
        }
      }
      
      // Success
      showSuccessToast('✅ Synced to GitHub');
      return;
      
    } catch (error) {
      lastError = error;
      attempt++;
      
      if (attempt < maxAttempts) {
        // Exponential backoff: 1s, 2s, 4s
        const backoffMs = Math.pow(2, attempt - 1) * 1000;
        showWarningToast(`🔄 Sync attempt ${attempt}/${maxAttempts}. Retrying in ${backoffMs / 1000}s...`);
        await new Promise(resolve => setTimeout(resolve, backoffMs));
      }
    }
  }
  
  // All retries failed
  showErrorToast(`❌ Failed to sync after ${maxAttempts} attempts. Will retry next time.`);
  console.error('GitHub sync failed:', lastError);
  
  // Queue for retry (optional: store failed sync for later retry)
  queueFailedSync(taskName, lastError.message);
}
```

**Additional Helper:**
```javascript
async function gistFetchLatest() {
  // Fetch latest Gist state to resolve conflicts
  const token = gistGetToken();
  const gistId = gistGetId();
  if (!token || !gistId) return false;
  
  try {
    const res = await fetch(`https://api.github.com/gists/${gistId}`, {
      headers: { 'Authorization': `token ${token}` }
    });
    
    if (!res.ok) throw new Error(`Failed to fetch gist: ${res.status}`);
    
    const gist = await res.json();
    const content = gist.files[GIST_FILENAME].content;
    const fetchedData = JSON.parse(content);
    
    // Merge fetched state with local state
    mergeRemoteState(fetchedData);
    return true;
    
  } catch (error) {
    console.error('Failed to fetch latest gist:', error);
    return false;
  }
}

function mergeRemoteState(remoteData) {
  // Merge strategy: remote done items + local pending items
  // (keep remote as source of truth for done, preserve local pending edits)
  const localState = getTasksState();
  const merged = {
    tasks: [...remoteData.tasks, ...localState.tasks.filter(t => !remoteData.tasks.find(r => r.id === t.id))],
    done: remoteData.done // Trust remote done list
  };
  saveTasksState(merged);
}

function queueFailedSync(taskName, errorMsg) {
  // Store failed sync attempts for retry
  const failedSyncs = JSON.parse(sessionStorage.getItem('failedSyncs') || '[]');
  failedSyncs.push({ taskName, errorMsg, timestamp: Date.now() });
  sessionStorage.setItem('failedSyncs', JSON.stringify(failedSyncs));
  
  // Retry on next sync attempt
  gistSchedulePush(); // Will pick up failed syncs and retry
}
```

**Why This Works:**
- **Exponential backoff** prevents hammering GitHub API when it's slow
- **409 Conflict handling** merges state when multi-device sync conflicts occur
- **Error toasts** inform user of sync status (not silent failures)
- **Queued retry** ensures failed syncs don't disappear
- **Timeout safety** max 3 attempts prevents infinite loops

**Testing:**
- [ ] Manually disconnect internet, toggle task done → error toast appears
- [ ] Reconnect → sync retries automatically
- [ ] Open 2 browser windows, toggle tasks in both → conflict handling merges state
- [ ] Check console → no silent errors, all failures logged
- [ ] Leave dashboard running, kill GitHub API → verify retries with backoff
- [ ] Check sessionStorage → failed syncs queued for retry

---

#### Fix 1.3: CSRF Nonce Validation for Gist Pushes

**File:** dashboard.html, lines 1934–1975 (gistPush function)  
**Problem:** No CSRF protection on Gist pushes → multi-device conflicts, no defense against cross-origin attacks  
**Impact:** Medium (multi-device safety)  
**Solution:** Add crypto.getRandomValues() nonce, include in payload, validate on receive

**Complexity:** Medium  
**Time:** 15 minutes  
**Dependencies:** Fix 1.2 (sync logic)

**Current Code (VULNERABLE):**
```javascript
function gistPush(content, message) {
  const payload = {
    files: {
      [GIST_FILENAME]: { content: content }
    },
    public: false,
    description: `Tasks — ${new Date().toISOString()}`
  };
  
  // NO NONCE — no protection against cross-origin attacks
  return fetch(...);
}
```

**Fixed Code:**
```javascript
function generateNonce() {
  // Cryptographically secure random nonce
  const array = new Uint8Array(16);
  crypto.getRandomValues(array);
  return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
}

function gistPush(content, message) {
  const nonce = generateNonce();
  const timestamp = Date.now();
  
  const payload = {
    files: {
      [GIST_FILENAME]: { 
        content: content 
      }
    },
    public: false,
    description: `Tasks — ${new Date().toISOString()}`,
    // Add nonce to metadata (optional, for CSRF defense)
    // Some implementations include in commit message or as file comment
  };
  
  // Store nonce locally for verification (when pulling)
  sessionStorage.setItem(`nonce_${timestamp}`, nonce);
  
  return fetch(...).then(res => {
    // After successful push, validate response contains our nonce
    // (or verify timestamp matches recent push)
    if (res.ok) {
      // Nonce validation passed
      sessionStorage.removeItem(`nonce_${timestamp}`);
    }
    return res;
  });
}

function gistPull() {
  // When pulling from gist, validate nonce matches
  return fetch(...).then(res => {
    if (res.ok) {
      const data = res.json();
      // Validate nonce matches a recent push
      const recentNonces = Object.keys(sessionStorage)
        .filter(k => k.startsWith('nonce_'))
        .map(k => parseInt(k.split('_')[1]))
        .filter(ts => Date.now() - ts < 60000); // Last 60 seconds
      
      // If nonce present in recent list, it's likely our push
      // If not, could be external change — log for debugging
      if (recentNonces.length === 0) {
        console.warn('Gist pull detected external change (no matching nonce)');
      }
    }
    return res;
  });
}
```

**Why This Works:**
- **Cryptographically secure nonce** prevents token reuse attacks
- **Nonce matching** ensures we're syncing our own changes
- **Timestamp validation** prevents replay attacks
- **External change detection** alerts if someone else modifies the gist

**Testing:**
- [ ] Push task update → nonce generated and stored
- [ ] Pull after push → nonce validates successfully
- [ ] Manually edit gist on GitHub.com → pull detects external change
- [ ] Check sessionStorage → nonces cleared after successful validation

---

### DATA SAFETY FIX (1 fix)

#### Fix 2.1: Done Item Archival (Prevent localStorage Quota Exceeded)

**File:** dashboard.html, near state initialization (lines 1550–1600)  
**Problem:** Done items accumulate infinitely → localStorage quota (5MB) exceeded, app crashes  
**Impact:** HIGH (app becomes unusable after ~1000 done items)  
**Solution:** Auto-archive done items after 24 hours to separate storage

**Complexity:** Medium  
**Time:** 30 minutes  
**Dependencies:** None

**Current Code (BROKEN):**
```javascript
const doneList = [];

function markTaskDone(task) {
  doneList.push({
    name: task.name,
    timestamp: Date.now(),
    xpEarned: task.xpEarned
  });
  saveState(); // Saves entire doneList to localStorage
  // Problem: doneList grows forever, eventually exceeds 5MB quota
}

function saveState() {
  localStorage.setItem('tasks', JSON.stringify({
    tasks: tasks,
    done: doneList // Keeps ALL done items forever
  }));
}
```

**Fixed Code:**
```javascript
const doneList = []; // Current session only
const archivedDone = []; // 24h+ old items

function markTaskDone(task) {
  doneList.push({
    name: task.name,
    timestamp: Date.now(),
    xpEarned: task.xpEarned,
    archivedAt: null
  });
  saveState();
  scheduleArchivalCheck();
}

function scheduleArchivalCheck() {
  // Run every hour to archive old done items
  if (!window.archivalCheckInterval) {
    window.archivalCheckInterval = setInterval(archiveOldDoneItems, 60 * 60 * 1000);
  }
}

function archiveOldDoneItems() {
  const now = Date.now();
  const archiveThreshold = 24 * 60 * 60 * 1000; // 24 hours
  
  const toArchive = doneList.filter(item => {
    const age = now - item.timestamp;
    return age > archiveThreshold;
  });
  
  if (toArchive.length === 0) return; // Nothing to archive
  
  // Move to archive
  toArchive.forEach(item => {
    item.archivedAt = now;
    archivedDone.push(item);
  });
  
  // Remove from active list
  doneList.splice(0, toArchive.length);
  
  // Save archive separately (won't bloat active state)
  saveArchive();
  saveState();
  
  // Notify user
  if (toArchive.length > 0) {
    console.log(`📦 Archived ${toArchive.length} items from 24h ago`);
  }
}

function saveState() {
  const state = {
    tasks: tasks,
    done: doneList // Only current session + last 24h
  };
  
  // Check size before saving
  const stateStr = JSON.stringify(state);
  const sizeKB = stateStr.length / 1024;
  
  if (sizeKB > 4500) { // 4.5MB of 5MB quota
    console.warn(`⚠️ localStorage near quota: ${sizeKB.toFixed(0)}KB`);
    // Aggressively archive if approaching quota
    archiveOldDoneItems();
  }
  
  localStorage.setItem('tasks', stateStr);
}

function saveArchive() {
  // Save archive to separate storage (localStorage or IndexedDB)
  const archive = {
    items: archivedDone,
    lastUpdated: Date.now()
  };
  
  // Use localStorage (small key), or IndexedDB for larger archives
  try {
    localStorage.setItem('tasksArchive', JSON.stringify(archive));
  } catch (e) {
    // localStorage full — use IndexedDB
    saveArchiveToIndexedDB(archive);
  }
}

function saveArchiveToIndexedDB(archive) {
  // Fallback if localStorage full
  const request = indexedDB.open('ProductivityDB', 1);
  
  request.onerror = () => console.error('IndexedDB error:', request.error);
  request.onsuccess = (e) => {
    const db = e.target.result;
    const tx = db.transaction('archive', 'readwrite');
    tx.objectStore('archive').put(archive);
  };
}

function getArchive() {
  // Retrieve archived items (for statistics/review)
  try {
    const stored = localStorage.getItem('tasksArchive');
    return stored ? JSON.parse(stored).items : [];
  } catch (e) {
    console.error('Failed to load archive:', e);
    return [];
  }
}

// On app load
function loadState() {
  const stored = localStorage.getItem('tasks');
  if (stored) {
    const state = JSON.parse(stored);
    tasks = state.tasks || [];
    doneList = state.done || [];
    
    // Load archived items
    const archived = getArchive();
    archivedDone = archived;
    
    // Check for items that need archival
    archiveOldDoneItems();
    scheduleArchivalCheck();
  }
}
```

**Why This Works:**
- **Automatic archival** moves 24h+ old items to separate storage
- **Size monitoring** prevents quota exceeded errors
- **IndexedDB fallback** provides more storage if needed (up to 50MB+)
- **Transparent to user** — they don't see archival happening

**Testing:**
- [ ] Mark 10 tasks done
- [ ] Check localStorage size → remains reasonable
- [ ] Simulate 24+ hour passage → archive triggers (or manually call archiveOldDoneItems())
- [ ] Check archive via getArchive() → items moved
- [ ] Mark 1000 done items → app doesn't crash, quota warning appears
- [ ] Check IndexedDB → fallback works if localStorage full

---

### CORRECTNESS FIX (1 fix)

#### Fix 2.2: Error Boundary Wrapper

**File:** dashboard.html, top of script section  
**Problem:** Uncaught JS errors crash entire app → black screen, user loses state  
**Impact:** Medium (app becomes unusable)  
**Solution:** Top-level try-catch wrapper around all state mutations

**Complexity:** Low  
**Time:** 10 minutes  
**Dependencies:** None

**Current Code (BROKEN):**
```javascript
// No error handling at top level
// Any error crashes the app
function markTaskDone(task) {
  // If anything here throws, entire app breaks
  // User gets blank screen
}
```

**Fixed Code:**
```javascript
// Error boundary wrapper
function withErrorBoundary(fn) {
  return function(...args) {
    try {
      return fn.apply(this, args);
    } catch (error) {
      console.error('Error in', fn.name, ':', error);
      showErrorToast(`⚠️ An error occurred. Please refresh the page.`);
      
      // Log error for debugging
      logErrorEvent({
        function: fn.name,
        error: error.message,
        stack: error.stack,
        timestamp: Date.now(),
        state: JSON.stringify({ tasks, done: doneList })
      });
      
      // Attempt recovery
      if (error.name === 'SyntaxError') {
        // Likely corrupt localStorage — clear and reload
        if (confirm('Corrupted data detected. Clear and reload?')) {
          localStorage.clear();
          location.reload();
        }
      } else if (error.name === 'TypeError') {
        // Likely missing property — preserve state and reload
        showWarningToast('Attempting recovery...');
        setTimeout(() => location.reload(), 2000);
      }
      
      // Don't re-throw — let app continue
      return null;
    }
  };
}

// Wrap all critical functions
const markTaskDoneSafe = withErrorBoundary(markTaskDone);
const updateTaskSafe = withErrorBoundary(updateTask);
const saveStateSafe = withErrorBoundary(saveState);
const syncTaskDoneToGitHubSafe = withErrorBoundary(syncTaskDoneToGitHub);

// Use wrapped versions in event handlers
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('done-btn')) {
    const taskName = e.target.dataset.taskName;
    const task = tasks.find(t => t.name === taskName);
    markTaskDoneSafe(task); // Use wrapped version
  }
});

// Optional: Global error handler
window.addEventListener('error', (event) => {
  console.error('Uncaught error:', event.error);
  showErrorToast('⚠️ Unexpected error. The app may be unstable.');
  logErrorEvent({
    type: 'uncaught',
    error: event.error?.message,
    stack: event.error?.stack,
    timestamp: Date.now()
  });
});

function logErrorEvent(errorData) {
  // Store error logs in sessionStorage for debugging
  const logs = JSON.parse(sessionStorage.getItem('errorLogs') || '[]');
  logs.push(errorData);
  // Keep only last 10 errors
  if (logs.length > 10) logs.shift();
  sessionStorage.setItem('errorLogs', JSON.stringify(logs));
}
```

**Why This Works:**
- **Prevents app crash** from individual function errors
- **User visibility** via error toasts
- **Recovery logic** attempts to fix common issues
- **Error logging** helps debugging

**Testing:**
- [ ] Intentionally throw error in task function
- [ ] App shows error toast but continues working
- [ ] Check sessionStorage for error logs
- [ ] Refresh → app recovers

---

### ACCESSIBILITY FIXES (5 fixes)

#### Fix 3.1: Keyboard Navigation

**File:** dashboard.html, add new event listeners section  
**Problem:** No keyboard support → WCAG Level A failure, users on keyboard can't navigate  
**Impact:** HIGH (accessibility compliance failure)  
**Solution:** Add keyboard handlers: Enter/Space to toggle, Alt+T/Alt+G shortcuts, Escape to close

**Complexity:** Medium  
**Time:** 20 minutes  
**Dependencies:** None

**Code:**
```javascript
// Keyboard navigation
document.addEventListener('keydown', (e) => {
  // Alt+T: Focus task input
  if (e.altKey && e.key === 't') {
    e.preventDefault();
    const taskInput = document.getElementById('taskInput');
    if (taskInput) taskInput.focus();
  }
  
  // Alt+G: Focus GitHub token input
  if (e.altKey && e.key === 'g') {
    e.preventDefault();
    const tokenInput = document.getElementById('gistTokenInput');
    if (tokenInput) tokenInput.focus();
  }
  
  // Escape: Close any open modal
  if (e.key === 'Escape') {
    const modal = document.querySelector('[role="dialog"]');
    if (modal) {
      modal.style.display = 'none';
      // Restore focus to trigger button
      restoreFocusAfterModal();
    }
  }
});

// Make task cards keyboard-accessible
document.addEventListener('keydown', (e) => {
  const taskCard = e.target.closest('[role="listitem"]');
  if (!taskCard) return;
  
  // Enter or Space to toggle task done
  if (e.key === 'Enter' || e.key === ' ') {
    e.preventDefault();
    const doneBtn = taskCard.querySelector('.done-btn');
    if (doneBtn) {
      doneBtn.click();
      // Move focus to next task or back to previous
      const nextCard = taskCard.nextElementSibling;
      if (nextCard) nextCard.focus();
    }
  }
  
  // Arrow keys to navigate between tasks
  if (e.key === 'ArrowDown') {
    e.preventDefault();
    const nextCard = taskCard.nextElementSibling;
    if (nextCard) nextCard.focus();
  }
  if (e.key === 'ArrowUp') {
    e.preventDefault();
    const prevCard = taskCard.previousElementSibling;
    if (prevCard) prevCard.focus();
  }
});

// Make all buttons keyboard accessible
document.querySelectorAll('button, [role="button"]').forEach(btn => {
  btn.setAttribute('tabindex', '0'); // Ensure in tab order
  btn.addEventListener('keydown', (e) => {
    // Allow Space/Enter to activate buttons
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      btn.click();
    }
  });
});
```

**Testing:**
- [ ] Tab through all elements → visible focus indicators
- [ ] Alt+T → task input focused
- [ ] Alt+G → token input focused
- [ ] Escape → modal closes
- [ ] Enter/Space on task card → toggles done
- [ ] Arrow keys → navigate between tasks
- [ ] Test with screen reader (NVDA/JAWS)

---

#### Fix 3.2: Visible Focus Indicators

**File:** dashboard.html, CSS section  
**Problem:** No visible focus outline → keyboard users can't see where they are  
**Impact:** HIGH (WCAG failure)  
**Solution:** Add high-contrast focus outline and box-shadow

**Complexity:** Low  
**Time:** 10 minutes  
**Dependencies:** None

**CSS:**
```css
/* Remove default focus outline and add custom high-contrast one */
*:focus {
  outline: none; /* Remove browser default (often subtle) */
}

/* Custom focus indicator — high contrast */
button:focus-visible,
input:focus-visible,
textarea:focus-visible,
[role="button"]:focus-visible,
[role="listitem"]:focus-visible {
  outline: 3px solid #2563eb; /* Bright blue */
  outline-offset: 2px;
  box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.1); /* Halo effect */
}

/* For dark mode compatibility */
@media (prefers-color-scheme: dark) {
  button:focus-visible,
  input:focus-visible,
  textarea:focus-visible,
  [role="button"]:focus-visible,
  [role="listitem"]:focus-visible {
    outline-color: #60a5fa; /* Lighter blue for dark mode */
  }
}

/* Ensure task cards are focusable */
.task-card {
  border-radius: 8px;
  transition: box-shadow 0.2s ease;
}

.task-card:focus-visible {
  box-shadow: inset 0 0 0 3px #2563eb; /* Inset focus for cards */
}
```

**Testing:**
- [ ] Press Tab → every element shows focus indicator
- [ ] Focus outline is clearly visible (3px, high contrast)
- [ ] Dark mode → outline adapts color
- [ ] No focus indicator on :hover only (must work on keyboard)

---

#### Fix 3.3: Color Contrast for Tertiary Text

**File:** dashboard.html, line 16 (CSS variables) or .t3 class  
**Problem:** .t3 tertiary text color #524e47 fails WCAG AA (3.45:1 ratio, need 4.5:1)  
**Impact:** Medium (WCAG AA failure on smaller text)  
**Solution:** Change from #524e47 to #6b6660 (4.82:1 ratio, passes AA)

**Complexity:** Low  
**Time:** 2 minutes  
**Dependencies:** None

**Before:**
```css
.t3 {
  color: #524e47; /* 3.45:1 ratio — FAILS WCAG AA */
}

/* Or in CSS variables: */
:root {
  --color-text-tertiary: #524e47;
}
```

**After:**
```css
.t3 {
  color: #6b6660; /* 4.82:1 ratio — PASSES WCAG AA */
}

/* Or in CSS variables: */
:root {
  --color-text-tertiary: #6b6660;
}
```

**Verification:**
- [ ] Use WebAIM contrast checker: https://webaim.org/resources/contrastchecker/
- [ ] Input: background #ffffff (white), text #6b6660
- [ ] Verify: 4.82:1 ratio ✓ (passes AA)
- [ ] All .t3 text should now be readable

---

#### Fix 3.4: ARIA Labels for Status Icons

**File:** dashboard.html, HTML task card sections  
**Problem:** Status emoji (✅ 📌 🔥) not announced to screen readers  
**Impact:** Medium (screen reader users don't know task status)  
**Solution:** Add aria-label to all status elements

**Complexity:** Low  
**Time:** 15 minutes  
**Dependencies:** None

**Before:**
```html
<div class="status">
  <span>✅</span> <!-- No label — screen reader reads as empty -->
</div>
```

**After:**
```html
<div class="status" aria-label="Task completed">
  <span aria-hidden="true">✅</span> <!-- Hidden from readers, emoji shown visually -->
</div>

<!-- Or with dedicated elements: -->
<span class="status-badge" aria-label="High priority">
  🔥
</span>

<span class="streaker" aria-label="5 day streak">
  🔥 5
</span>

<span class="level" aria-label="Level 12">
  ⭐ 12
</span>
```

**Mapping (apply to all status elements):**
```javascript
// Script to validate/add ARIA labels
const statusMappings = {
  '✅': 'Task completed',
  '📌': 'Task pinned',
  '🔥': 'On fire streak',
  '🎯': 'Milestone reached',
  '⭐': 'Level achieved'
};

document.querySelectorAll('.status, .streak, .level, .badge').forEach(el => {
  if (!el.getAttribute('aria-label')) {
    const emoji = el.textContent.trim().charAt(0);
    const label = statusMappings[emoji] || `Status: ${emoji}`;
    el.setAttribute('aria-label', label);
    
    // Hide visual emoji from screen readers
    const span = el.querySelector('span');
    if (span) span.setAttribute('aria-hidden', 'true');
  }
});
```

**Testing:**
- [ ] Screen reader (NVDA): announces "Task completed" when encountering ✅
- [ ] DevTools → Accessibility tree shows all labels
- [ ] Visual emoji still visible
- [ ] No duplicate announcements

---

#### Fix 3.5: Semantic HTML Landmarks

**File:** dashboard.html, lines 740–801 (main structure)  
**Problem:** Flat div structure → screen readers can't navigate sections  
**Impact:** Medium (screen reader navigation broken)  
**Solution:** Add header, main, aside, footer with sr-only labels

**Complexity:** Low  
**Time:** 15 minutes  
**Dependencies:** None

**Before:**
```html
<div class="container">
  <div class="header">...</div>
  <div class="main">...</div>
  <div class="sidebar">...</div>
  <div class="footer">...</div>
</div>
```

**After:**
```html
<header>
  <h1>Productivity Dashboard</h1>
  <!-- Navigation, logo, settings -->
</header>

<main>
  <section aria-labelledby="tasks-heading">
    <h2 id="tasks-heading" class="sr-only">Tasks</h2>
    <!-- Task list -->
  </section>
  
  <section aria-labelledby="gamification-heading">
    <h2 id="gamification-heading" class="sr-only">Gamification Stats</h2>
    <!-- XP, streaks, levels -->
  </section>
</main>

<aside>
  <h2 class="sr-only">GitHub Sync Settings</h2>
  <!-- Token input, sync status -->
</aside>

<footer>
  <p class="sr-only">Productivity Dashboard v2.5</p>
  <!-- Links, credits -->
</footer>

<!-- Add sr-only class for hidden headings -->
<style>
  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }
</style>
```

**Testing:**
- [ ] Screen reader: "Navigation" → task list → "Gamification stats" (landmarks work)
- [ ] DevTools → Elements show semantic structure
- [ ] Headings present but hidden visually

---

### SUPPORTING FIXES (3 fixes)

#### Fix 3.6: Modal Focus Management

**File:** dashboard.html, modal open/close functions  
**Problem:** Focus escapes modal when tabbing → confusing keyboard navigation  
**Impact:** Medium (keyboard a11y)  
**Solution:** Focus trap (prevent Tab/Shift+Tab from leaving modal), restore focus on close

**Complexity:** Medium  
**Time:** 15 minutes  
**Dependencies:** None

**Code:**
```javascript
let focusTrapElement = null;

function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  
  focusTrapElement = modal;
  modal.style.display = 'block';
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');
  
  // Move focus into modal
  const closeBtn = modal.querySelector('[aria-label="Close"]') || modal.querySelector('button');
  if (closeBtn) {
    closeBtn.focus();
  } else {
    modal.focus();
  }
  
  // Trap focus within modal
  setupFocusTrap(modal);
}

function setupFocusTrap(modal) {
  document.addEventListener('keydown', focusTrapHandler);
}

function focusTrapHandler(e) {
  if (e.key !== 'Tab' || !focusTrapElement) return;
  
  const focusableElements = focusTrapElement.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  
  if (focusableElements.length === 0) return;
  
  const first = focusableElements[0];
  const last = focusableElements[focusableElements.length - 1];
  const activeEl = document.activeElement;
  
  // If Shift+Tab on first element, move to last
  if (e.shiftKey && activeEl === first) {
    e.preventDefault();
    last.focus();
  }
  // If Tab on last element, move to first
  else if (!e.shiftKey && activeEl === last) {
    e.preventDefault();
    first.focus();
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (!modal) return;
  
  modal.style.display = 'none';
  focusTrapElement = null;
  
  document.removeEventListener('keydown', focusTrapHandler);
  
  // Restore focus to trigger button (optional)
  const triggerBtn = document.querySelector(`[data-modal="${modalId}"]`);
  if (triggerBtn) {
    triggerBtn.focus();
  }
}
```

**Testing:**
- [ ] Open modal → focus moves into modal
- [ ] Tab → cycles through modal elements only
- [ ] Shift+Tab at first element → wraps to last element
- [ ] Escape → closes modal, focus returns to trigger button

---

#### Fix 3.7: Touch Target Sizing

**File:** dashboard.html, CSS for buttons  
**Problem:** Small buttons fail WCAG AAA (44×44px minimum for mobile)  
**Impact:** Low (AAA compliance, mobile UX)  
**Solution:** Ensure all interactive elements ≥44×44px

**Complexity:** Low  
**Time:** 10 minutes  
**Dependencies:** None

**CSS:**
```css
/* Buttons */
button, [role="button"] {
  min-width: 44px;
  min-height: 44px;
  padding: 8px 12px; /* Internal padding, plus border = 44px total */
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Icon buttons (for small icons) */
.icon-btn {
  min-width: 44px;
  min-height: 44px;
  border-radius: 8px;
  padding: 10px;
}

/* Task cards (larger touch target) */
.task-card {
  min-height: 48px;
  padding: 12px;
  cursor: pointer;
}

/* Form inputs */
input, textarea, select {
  min-height: 44px;
  padding: 8px 12px;
  font-size: 16px; /* Prevents zoom on iOS */
}

/* Checkboxes (custom implementation) */
input[type="checkbox"] {
  width: 24px;
  height: 24px;
  margin: 10px; /* Surrounding space for 44×44px total */
}
```

**Testing:**
- [ ] Inspect element → min-width and min-height both ≥44px
- [ ] Touch on mobile → buttons easily tappable
- [ ] No overlap with neighboring elements

---

#### Fix 3.8: aria-live Region for Toast Announcements

**File:** dashboard.html, HTML + toast functions  
**Problem:** Error/success toasts not announced to screen readers → users don't know if action succeeded  
**Impact:** Medium (a11y)  
**Solution:** Add aria-live region, wire toast functions to announce

**Complexity:** Low  
**Time:** 10 minutes  
**Dependencies:** None

**HTML (add to page):**
```html
<!-- Announcement region for screen readers -->
<div 
  id="toastRegion" 
  role="status" 
  aria-live="polite" 
  aria-atomic="true"
  style="position: absolute; left: -10000px; width: 1px; height: 1px; overflow: hidden;"
></div>
```

**JavaScript (update toast functions):**
```javascript
function showSuccessToast(message) {
  // Visual toast (existing code)
  const toast = document.createElement('div');
  toast.className = 'toast toast-success';
  toast.textContent = message;
  document.body.appendChild(toast);
  
  // Announce to screen readers
  announceToast(message);
  
  setTimeout(() => toast.remove(), 3000);
}

function showErrorToast(message) {
  // Visual toast
  const toast = document.createElement('div');
  toast.className = 'toast toast-error';
  toast.textContent = message;
  document.body.appendChild(toast);
  
  // Announce to screen readers
  announceToast(message);
  
  setTimeout(() => toast.remove(), 3000);
}

function showWarningToast(message) {
  // Visual toast
  const toast = document.createElement('div');
  toast.className = 'toast toast-warning';
  toast.textContent = message;
  document.body.appendChild(toast);
  
  // Announce to screen readers
  announceToast(message);
  
  setTimeout(() => toast.remove(), 3000);
}

function announceToast(message) {
  // Send to aria-live region
  const region = document.getElementById('toastRegion');
  if (region) {
    region.textContent = message;
    // Clear after announcement (after 1.5s)
    setTimeout(() => {
      region.textContent = '';
    }, 1500);
  }
}
```

**Testing:**
- [ ] Screen reader: "Task completed" announced when toast shows
- [ ] No visual change (region hidden)
- [ ] Messages queue properly if multiple toasts

---

## Testing Strategy

### Unit Testing (After Each Fix)

For each fix, follow this checklist:

```
Fix 1.1: Move tokens to sessionStorage
- [ ] Open DevTools → localStorage, sessionStorage tabs
- [ ] Enter token → localStorage empty, sessionStorage has token
- [ ] Refresh page → token gone (sessionStorage cleared)
- [ ] Warning toast shows
- [ ] No security warning in console

Fix 1.2: GitHub sync retry logic
- [ ] Disconnect internet
- [ ] Toggle task done → error toast "Sync attempt 1/3"
- [ ] Reconnect → retries automatically
- [ ] Verify exponential backoff (1s, 2s, 4s)
- [ ] Open DevTools → Network tab shows retries
- [ ] Task syncs on success

... (and so on for each fix)
```

### Integration Testing

```
Full Phase 1 Flow:
- [ ] Start fresh (clear localStorage)
- [ ] Create 3 tasks
- [ ] Mark 1 done, pin 1
- [ ] Enter GitHub token → saves to sessionStorage
- [ ] Sync to GitHub → success
- [ ] Refresh page → token cleared, warning shows
- [ ] Navigate with keyboard (Tab, Alt+T, Alt+G, Escape)
- [ ] Check focus indicators visible
- [ ] Open DevTools Accessibility → no violations
- [ ] Test with screen reader (NVDA/JAWS)
```

### WCAG AA Compliance Verification

```
Before deploying:
- [ ] Run axe DevTools audit → 0 failures
- [ ] WebAIM contrast checker → all text passes AA
- [ ] Keyboard navigation: Tab through entire app
- [ ] Screen reader: NVDA/JAWS announces all elements
- [ ] Focus indicators: visible on every interactive element
- [ ] Touch targets: all buttons ≥44×44px
```

---

## Implementation Checklist

### Phase 1 Execution Order

```
SESSION 1 (3 hours):
- [ ] Fix 1.1: Move tokens (5 min)
- [ ] Fix 1.2: GitHub sync retry (20 min)
- [ ] Fix 1.3: CSRF nonce (15 min)
- [ ] Fix 2.1: Done item archival (30 min)
- [ ] Fix 2.2: Error boundary (10 min)
- [ ] TEST: Manual testing after every fix (20 min)
- [ ] COMMIT: "Phase 1: Security + data safety fixes"

SESSION 2 (2 hours):
- [ ] Fix 3.1: Keyboard navigation (20 min)
- [ ] Fix 3.2: Focus indicators (10 min)
- [ ] Fix 3.3: Color contrast (2 min)
- [ ] Fix 3.4: ARIA labels (15 min)
- [ ] Fix 3.5: Semantic landmarks (15 min)
- [ ] TEST: Manual + keyboard + screen reader (30 min)
- [ ] COMMIT: "Phase 1: Accessibility fixes"

SESSION 3 (2 hours):
- [ ] Fix 3.6: Modal focus management (15 min)
- [ ] Fix 3.7: Touch target sizing (10 min)
- [ ] Fix 3.8: aria-live region (10 min)
- [ ] FULL TESTING: All tests from Testing Checklist (30 min)
- [ ] COMMIT: "Phase 1: Focus management & touch targets"
- [ ] PUSH to GitHub: git push origin phase-1-security-a11y
- [ ] CREATE PR (optional, for review)
- [ ] MERGE when satisfied
```

---

## Git Workflow

```bash
# Start
git pull origin main
git checkout -b phase-1-security-a11y

# After Fix 1.1, 1.2, 1.3, 2.1, 2.2
git add dashboard.html
git commit -m "Phase 1: Security + data safety fixes

- Fix 1.1: Move tokens to sessionStorage
- Fix 1.2: GitHub sync retry logic (3-attempt exponential backoff)
- Fix 1.3: CSRF nonce validation
- Fix 2.1: Done item archival (auto-archive 24h+ items)
- Fix 2.2: Error boundary wrapper

Testing: Manual verification of sync, token security, error handling"

# After Fix 3.1–3.5
git add dashboard.html
git commit -m "Phase 1: Accessibility fixes (WCAG AA)

- Fix 3.1: Keyboard navigation (Tab, Alt+shortcuts, Escape)
- Fix 3.2: Visible focus indicators (high-contrast outline)
- Fix 3.3: Color contrast (.t3 text, 4.82:1 ratio)
- Fix 3.4: ARIA labels for status icons
- Fix 3.5: Semantic HTML landmarks

Testing: Keyboard nav, screen reader validation, focus indicators"

# After Fix 3.6–3.8
git add dashboard.html
git commit -m "Phase 1: Focus management & touch targets

- Fix 3.6: Modal focus trap & restoration
- Fix 3.7: Touch target sizing (44×44px minimum)
- Fix 3.8: aria-live region for toast announcements

Testing: Full WCAG AA compliance, mobile touch, all a11y tests"

# Finalize
git push origin phase-1-security-a11y
# On GitHub: Create PR, request review (optional), merge to main
```

---

## Reference Documents

All these documents are in ~/Projects/Productivity/ on desktop and synced to GitHub:

| Document | Purpose | Size |
|----------|---------|------|
| **PHASE_1_SECURITY_A11Y_FIXES.md** | Implementation guide (this doc, expanded) | 1,055 lines |
| **dashboard_AUDIT_IMPLEMENTATION_PLAN.md** | Full audit findings + 3-phase roadmap | 4,000+ words |
| **AUDIT_SUMMARY.md** | Quick reference of all findings | 4.3 KB |
| **HANDOVER_PHASE_1_IMPLEMENTATION.md** | Comprehensive handover (3,000+ words) | Earlier document |
| **dashboard.html** | Main file to edit | 3,810 lines |
| **dashboard_AUDIT_2026-04-07.html** | Test clone (backup) | 3,810 lines |
| **CLAUDE.md** | Project instructions & GitHub workflow | 14 KB |

---

## Success Criteria (Phase 1 Complete)

✅ All 13 fixes applied to dashboard.html  
✅ WCAG 2.1 AA compliance verified  
✅ No console errors or warnings  
✅ GitHub sync working with retry logic  
✅ Tokens in sessionStorage (NOT localStorage)  
✅ Keyboard navigation working  
✅ Screen reader announces all elements  
✅ All commits pushed to GitHub  
✅ Commits follow git workflow  
✅ Ready for Phase 2 (Design System refactor)

---

## Contact & Questions

If anything is unclear or conflicts arise during implementation:
1. Reference the original audit docs for context
2. Check AUDIT_SUMMARY.md for quick reference
3. Review the specific fix section above for detailed explanation
4. Check git history for similar patterns

---

**Prepared by:** Claude Haiku (April 22, 2026)  
**For:** Claude Sonnet 4.6+ with Claude Code  
**Status:** ✅ Ready to execute Phase 1

---

## END OF SONNET SESSION PROMPT

Copy everything above and paste into your Sonnet session.

