# Phase 4 Testing: Quick Reference Checklist

**Status:** Ready for Execution  
**Total Duration:** ~4 hours across 1-2 sessions  
**Executor:** New Claude session (no prior context)  

---

## Pre-Test Checklist

- [ ] Fresh Cowork session started
- [ ] `/mnt/Projects` directory mounted
- [ ] Network connection stable
- [ ] Browser available (Chrome/Safari)
- [ ] GitHub token available (`yl_gist_token`)
- [ ] Read PHASE_4_TESTING_STRATEGY.md (full test plan)

---

## Phase 4.1: Startup Protocol (30 min)

### Automated Test
```bash
chmod +x test-phase-4.1-startup.sh
./test-phase-4.1-startup.sh
# Result: Should show ✓ 8/8 PASS
```

### Manual Verification
- [ ] Can read CLAUDE.md from GitHub
- [ ] Can read TASKS.md from GitHub
- [ ] Can read DASHBOARD-TASKS.md from GitHub
- [ ] Local files match GitHub versions
- [ ] Memory routing files exist
- [ ] Git status shows clean working tree

**Go/No-Go:** All 8 tests PASS → Continue to 4.2

---

## Phase 4.2: Dashboard Features (30 min)

### Load & Inspect
- [ ] Open: https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html
- [ ] Verify: Loads in <3 seconds, no 404 error
- [ ] Check: No console errors (F12 → Console tab)

### Feature Testing
- [ ] Toggle "Personal" mode → Tasks filter correctly
- [ ] Toggle "Work" mode → Gorgias tasks visible
- [ ] Add test task → Appears in list
- [ ] Reload page → Test task persists
- [ ] Mark test task done → Moves to "Done" log
- [ ] Click "↑ Sync TASKS" → Shows "syncing..." then "✓ synced"

### Cloud Sync (if token available)
- [ ] Complete a task
- [ ] GitHub Gist syncs automatically (check UI indicator)
- [ ] Open dashboard in new browser window (no localStorage)
- [ ] Reload → Task still marked done (data persisted in Gist)

**Go/No-Go:** All features work, no JavaScript errors → Continue to 4.3

---

## Phase 4.3: Document Consistency (20 min)

### Verify Paths & References
- [ ] CLAUDE.md paths are illustrative (local macOS) or mapped to `/mnt/Projects`
- [ ] CLAUDE-COWORK-OPERATING-SYSTEM.md URLs all live (test 5-10 links)
- [ ] Memory routing table lists 4 project files
- [ ] No stale task markings ([x] tasks have session-log entries)

### Check URLs
```bash
# Sample URL checks (replace with actual URLs from docs)
curl -I https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md
curl -I https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html
curl -I https://nebuleusebijoux.com/a/return
```

**Go/No-Go:** No broken links, no contradictions → Continue to 4.4

---

## Phase 4.4: Git & GitHub Integration (20 min)

### Repository Health
```bash
cd /mnt/Projects
git status           # Should show clean (0 modified, 0-1 untracked)
git log --oneline -5 # Should show recent commits
git fetch origin main
git diff --name-only main origin/main  # Should show no diff
```

- [ ] Git status: clean working tree
- [ ] Commits: recent (all 2026 dates)
- [ ] Remote sync: local = remote
- [ ] GitHub Pages: workflow exists and recent build succeeded

**Go/No-Go:** All git checks pass → Continue to 4.5

---

## Phase 4.5: Scheduled Tasks (15 min)

### Verify Scheduling (Phase 3 Task)
- [ ] Check: `process-claude-task-queue` task exists OR Phase 3.2 is pending
- [ ] Document: Status (implemented or pending)
- [ ] Note: Wrap-up task timing (5:30pm documented in CLAUDE-COWORK-OPERATING-SYSTEM.md)

**Go/No-Go:** Status documented (implement or pending is OK) → Continue to 4.6

---

## Phase 4.6: Memory System Routing (15 min)

### Verify Files Exist
```bash
ls -la /mnt/Projects/Productivity/memory/projects/
# Expected: 4 files
```

- [ ] nebuleuse-bijoux.md (exists, >2KB)
- [ ] accessory-partners.md (exists, >2KB)
- [ ] gorgias-agency.md (exists, >2KB)
- [ ] linkedin-content-system.md (exists, >2KB)

### Verify Memory Structure
- [ ] `/Productivity/memory/context/ohtani-matrix.md` (exists, locked goal: €50K, ≤20h/week)
- [ ] `/Productivity/memory/session-log.md` (latest entry ≤7 days old)
- [ ] `/Productivity/memory/dashboard-changelog.md` (documents recent dashboard changes)

**Go/No-Go:** All 4 routing files exist and current → Continue to 4.7

---

## Phase 4.7: Real-World Workflow Simulation (45 min)

### Simulate Complete Session: Nébuleuse Task

```
Step 1: Read Memory (5 min)
  ✓ Read CLAUDE.md, TASKS.md, DASHBOARD-TASKS.md
  ✓ Read /Productivity/memory/projects/nebuleuse-bijoux.md
  
Step 2: Analyze Task (10 min)
  ✓ Task: "Share Baback integration checklist"
  ✓ Status: [>] Important
  ✓ Context: +45-52% automation unlock
  
Step 3: Update Dashboard (5 min)
  ✓ Find task in Freelance → Nébuleuse section
  ✓ Change status to [~] In Progress
  ✓ Take screenshot showing change
  
Step 4: Simulate Work (10 min)
  ✓ Write brief summary to /tmp/baback-summary.txt
  ✓ Content: checklist items, ready for client
  
Step 5: Complete Task & Sync (10 min)
  ✓ Mark task as [x] Done in dashboard
  ✓ Add task note: "Shared 2026-04-19, awaiting feedback"
  ✓ Click "↑ Sync TASKS" button
  ✓ Wait for ✓ synced indicator
  
Step 6: Update Session Log (5 min)
  ✓ Append to /Productivity/memory/session-log.md
  ✓ Format: ## YYYY-MM-DD | Nébuleuse Baback | Phase 4 Test
  ✓ Content: Requested, Done, Key decision
  
Step 7: Verify (5 min)
  ✓ Run: git log --oneline -3
  ✓ Verify: New commits show task + session log
  ✓ Verify: Dashboard and GitHub state match
```

**Go/No-Go:** All 7 steps complete without errors → Continue to 4.8

---

## Phase 4.8: Edge Cases & Resilience (45 min)

### Quick Edge Case Tests

1. **Offline Behavior**
   - [ ] Disable network
   - [ ] Try to sync TASKS
   - [ ] Expected: Graceful error message (not crash)
   - [ ] Re-enable network, retry → Succeeds

2. **Auth Token Missing**
   - [ ] Clear localStorage
   - [ ] Try to sync → Shows "Auth required" message
   - [ ] Set token, retry → Succeeds

3. **Rapid Task Completion**
   - [ ] Complete 5 tasks in <2 seconds (click fast)
   - [ ] Click "↑ Sync TASKS"
   - [ ] Expected: All 5 sync in single commit (no duplicates)

4. **Cache Behavior**
   - [ ] Reload dashboard 5 times fast
   - [ ] Check Network tab → See 304 Not Modified (cache hits)
   - [ ] Verify: Hot load <500ms

5. **Concurrent Operations**
   - [ ] Open dashboard in 2 browser tabs
   - [ ] Complete task in tab 1, add task in tab 2, mark done in tab 3 simultaneously
   - [ ] Expected: No interference, final state consistent

**Go/No-Go:** 5/5 edge cases handled gracefully → Continue to 4.9

---

## Phase 4.9: Performance Metrics (30 min)

### Measure Load Times

```bash
# Cold load (clear cache, first load)
# Expected: <3 seconds
# URL: https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html

# Hot load (cached, reload)
# Expected: <500ms
# Use: Cmd+R (reload with cache)

# File sizes
ls -lh /mnt/Projects/Productivity/dashboard.html  # Expected: ~244KB
ls -lh /mnt/Projects/CLAUDE.md                     # Expected: ~10KB
ls -lh /mnt/Projects/TASKS.md                      # Expected: ~2KB
```

- [ ] Dashboard cold load: _____ ms (target: <3000ms)
- [ ] Dashboard hot load: _____ ms (target: <500ms)
- [ ] TASKS.md sync latency: _____ sec (target: <5s)
- [ ] Gist sync latency: _____ sec (target: <2s)
- [ ] Memory usage: _____ MB (target: <10MB, no leaks)

**Go/No-Go:** Most metrics in range (minor variance acceptable) → Continue to 4.10

---

## Phase 4.10: Security Audit (30 min)

### Automated Checks
```bash
cd /mnt/Projects/Productivity
# Check 1: No hardcoded tokens
grep -i "ghp_\|ghs_\|ghu_\|ghr_" dashboard.html
# Expected: No output (no tokens found)

# Check 2: No dangerous patterns
grep -c "\.innerHTML\s*=" dashboard.html
# Expected: 0 (or document reason if >0)

# Check 3: No onclick attributes
grep -c "onclick=" dashboard.html
# Expected: 0 (prefers event delegation)
```

### Manual Tests

1. **XSS Prevention**
   - [ ] Add task with name: `<img src=x onerror="alert('XSS')">`
   - [ ] Expected: Rendered as literal text, no alert
   - [ ] Add task with: `<script>alert('XSS')</script>`
   - [ ] Expected: Literal text, no execution

2. **Token Security**
   - [ ] Check localStorage: token present but secure
   - [ ] Sync TASKS, check Network tab: token NOT in URL parameters
   - [ ] Expected: Auth header used (not query param)

3. **Access Control**
   - [ ] Try to read Gist without token
   - [ ] Expected: 403 Forbidden response from Gist API

### Code Review
- [ ] Scan dashboard.html for escapeHtml() usage (XSS mitigation)
- [ ] Check JSON.parse() has try/catch (error handling)
- [ ] Verify event listeners use data-* attributes (not onclick)

**Go/No-Go:** 0 critical security findings → Proceed to final decision

---

## Final Go/No-Go Decision

### Approval Criteria

✓ **GO** if:
- [ ] Phase 4.1-4.4: 100% PASS (startup, dashboard, consistency, git)
- [ ] Phase 4.6: All routing files exist and current
- [ ] Phase 4.7: Real workflow completes without errors
- [ ] Phase 4.10: 0 critical security findings
- [ ] Performance: Within acceptable ranges
- [ ] Dashboard: Stable and feature-complete

✗ **NO-GO** if:
- [ ] Any startup test fails (4.1)
- [ ] Dashboard features broken (4.2)
- [ ] Critical security vulnerabilities (4.10)
- [ ] Real workflow fails to complete (4.7)

---

## Sign-Off

**Tested By:** ___________________________  
**Date:** ___________________________  
**Total Duration:** _____ hours  
**Critical Issues:** _____ (expected: 0)  
**Recommendations:** ___________________________  

**Final Decision:** **[ ] GO** or **[ ] NO-GO**  

---

## Troubleshooting

| Issue | Diagnosis | Fix |
|-------|-----------|-----|
| Dashboard won't load | Check: HTTP status 404 or network error | Verify GitHub Pages URL, check if repo is public |
| Sync fails | Check: Auth token set? Network available? | Set token in localStorage, check curl commands |
| Git status shows untracked | Check: New temp files created during test | Run `git clean -fd` to remove, or add to .gitignore |
| Performance slow | Check: Network latency, browser cache, system load | Repeat tests, measure 3x take average |
| XSS test doesn't work | Check: Browser console for errors | Ensure JavaScript enabled, use vanilla HTML/JS (no frameworks) |

---

## Resources

- Full Plan: PHASE_4_TESTING_STRATEGY.md
- Startup Script: test-phase-4.1-startup.sh
- Issues Log: PHASE_4_ISSUES.md (created during testing)
- Results: PHASE_4_RESULTS.md (created at end)

**Execution Time Estimate:**
- Session 1: 4.1 - 4.7 (2.5 hours)
- Session 2: 4.8 - 4.10 (1.5 hours)
- **Total: ~4 hours across 1-2 sessions**

---

**Good luck! The system is well-architected. Phase 4 should pass cleanly.**
