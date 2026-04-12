---
name: Dashboard Sync & Automation Audit
description: Critical issues found in dashboard-to-GitHub sync system
type: project
---

# Dashboard Sync & Automation Audit

**Date:** 2026-04-11  
**Scope:** Dashboard → GitHub TASKS.md sync automation  
**Status:** 🔴 **CRITICAL ISSUES FOUND**

---

## Executive Summary

The dashboard has **automation code to sync completed tasks to TASKS.md on GitHub**, but it **has never worked properly** and the **token is not configured**. As a result:

1. ❌ Dashboard tasks marked done → **NOT synced** to TASKS.md
2. ❌ Manual sync was required (what I just did)
3. ❌ `syncTaskDoneToGitHub()` function exists but is **always silently failing**
4. ❌ Users have **no visibility** into sync failures (errors logged to console, not UI)

This is why **TASKS.md fell out of sync with the dashboard** — the automation never ran.

---

## Issues Found

### 🔴 **Critical Issue #1: Token Not Configured**

**Location:** Line 1723, `syncTaskDoneToGitHub()`

**Problem:**
```javascript
async function syncTaskDoneToGitHub(taskName) {
  const token = gistGetToken();  // ← Returns null if not set
  if (!token) return;             // ← SILENTLY FAILS — no error, no sync
```

**Why it fails:**
- Token must be set via: `localStorage.setItem('yl_gist_token', 'ghp_...')`
- This requires running code in browser console
- Most users never do this
- Even if token is set, it's **only for Gist sync**, not GitHub API sync

**Impact:** 🔴 **Critical** — Sync automation has never worked for anyone

---

### 🔴 **Critical Issue #2: Wrong Token Type**

**Location:** Line 1723-1729

**Problem:**
```javascript
const token = gistGetToken();  // Gets 'yl_gist_token' from localStorage
// This is meant for Gist syncing, NOT GitHub API calls
// But the code tries to use it for GitHub API: TASKS.md updates
```

**Why it's broken:**
- `yl_gist_token` is for GitHub Gist (dashboard state backup)
- The code tries to use it to update `Productivity/TASKS.md` in the main repo
- These are **different APIs** with **different token requirements**
- Token scope may not allow repo write access

**Impact:** 🔴 **Critical** — Even with token set, API calls would fail (403 Forbidden)

---

### 🟡 **Issue #3: Silent Failure — No Error Reporting**

**Location:** Line 1765-1766

```javascript
} catch(e) {
  console.warn('[YL/OPS] TASKS.md sync failed silently:', e);
  // ↑ Error ONLY logged to browser console
  // ↑ User never sees this message
  // ↑ No UI feedback, no notification
}
```

**Why it's bad:**
- Users have no idea sync failed
- Dashboard and TASKS.md diverge silently
- No way to know state is out of sync

**Impact:** 🟡 **Medium** — Masks the broken sync

---

### 🟡 **Issue #4: Fuzzy Matching is Fragile**

**Location:** Line 1737-1747

```javascript
const needle = taskName.trim().toLowerCase();
const lines = original.split('\n');
let matched = false;
const updated = lines.map(line => {
  if (matched) return line;  // ← Stops after FIRST match
  const bare = line.replace(/\*\*/g, '').toLowerCase();
  if (/^- \[[ ]\]/.test(line) && bare.includes(needle)) {
    matched = true;
    return line.replace('- [ ]', '- [x]');
  }
  return line;
});
```

**Problems:**
1. **Substring matching** — "Book hotel Barcelona" matches "Book hotel Barcelona 2" if it exists
2. **Stops at first match** — If TASKS.md has duplicates, only first gets marked
3. **Case-insensitive but brittle** — Typos/formatting changes break matching
4. **No validation** — Doesn't verify the correct task was marked done

**Impact:** 🟡 **Medium** — Could mark wrong task as done if naming is ambiguous

---

## Root Cause

The sync system was **designed but never tested or completed**:

✅ **What exists:**
- `syncTaskDoneToGitHub()` function
- Token setup instructions (localStorage)
- Error handling (silent fail)

❌ **What's missing:**
- **Proper token configuration** — needs repo write token, not Gist token
- **Error visibility** — UI banner or toast notification on sync failure
- **Testing** — nobody verified this actually works
- **Documentation** — how to set up the sync token

---

## Impact on Users

Because this automation is broken:

1. ✅ **Dashboard state IS saved to Gist** (different sync, works fine)
2. ❌ **TASKS.md is NOT updated when you mark tasks done**
3. ❌ **Manual sync required** (what happened today)
4. ❌ **State divergence creates confusion** (like today)

---

## Recommendations

### **Short-term (Disable broken sync)**

**Option A:** Remove the broken sync function
```javascript
// Delete syncTaskDoneToGitHub() entirely
// Remove call at line 2840
// Remove call at line 3819
// Add comment: "Dashboard → TASKS.md sync via manual export/import only"
```

**Why:** Prevents silent failures and false expectations

---

### **Long-term (Fix or rebuild)**

**Option B:** Fix the sync properly
1. Use proper GitHub API token (repo scope) instead of Gist token
2. Store token securely in a separate localStorage key
3. Add UI feedback (banner showing sync status)
4. Improve matching: use task `data-id` instead of fuzzy name matching
5. Add error notifications: toast on sync failure
6. Test the sync works end-to-end

**Effort:** ~3-4 hours

**Benefits:** Full automation, no manual syncing needed

---

### **Recommended: Option B (Hybrid)**

**Phase 1 (now):** Disable broken sync + update console message
```javascript
console.log('[YL/OPS] Dashboard-to-TASKS.md sync is currently disabled. Manual sync via export at session end.');
// Remove the actual sync function calls
```

**Phase 2 (later):** Rebuild with proper token + UI feedback
- Users set GitHub token in dashboard settings UI
- Sync status shown in banner
- One-click manual sync available
- Auto-sync on task completion (with error visibility)

---

## Files Affected

- `Productivity/dashboard.html` (lines 1722-1768, 2840, 3819)
- Token stored at: `localStorage.yl_gist_token` (wrong location)
- GitHub API calls expect: `yl_github_token` (doesn't exist)

---

## Resolution (2026-04-13)

**Status: ✅ RESOLVED — commit 1f73241**

Option B (rebuild) implemented. See `dashboard-changelog.md` entry for 2026-04-13 for full technical details.

- `syncTaskDoneToGitHub()` replaced by `syncToTasksMd()` + `buildTaskMap()`
- Token reuse (yl_gist_token has repo+gist scope — no new setup needed)
- Button-triggered + beforeunload safety net
- All errors visible in topbar (not silent console.warn)

---

## Verdict (original)

**Status: 🔴 Do Not Release Without Fix**

The sync automation is **non-functional** and creates **false expectations**. Either:
1. Remove it and document manual sync workflow, OR
2. Fix it properly before advertising it as a feature

Recommend **Option A (disable) immediately** + **Option B (fix) in next sprint**.

---

## Next Steps

1. ⚠️ Disable broken sync (2 min)
2. 📝 Update CLAUDE.md to document manual sync workflow (5 min)
3. 📋 Create backlog item for proper sync rebuild (future sprint)
4. 🧪 Add testing: verify sync works before re-enabling (when rebuilding)

