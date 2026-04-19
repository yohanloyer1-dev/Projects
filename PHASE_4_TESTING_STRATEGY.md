# Phase 4: Testing & Verification Strategy
## Claude Cowork Operating System

**Version:** 1.0  
**Date Created:** 2026-04-19  
**Status:** Ready for Execution  
**Approval Required:** Before Phase 4.1 execution

---

## Executive Summary

Phase 4 tests the completeness, correctness, and robustness of the Claude Cowork Operating System through structured verification in a fresh session. This ensures that any new Claude session can reliably bootstrap using the system, that critical integrations work, and that edge cases are identified before real-world deployment.

**Success Definition:** A fresh Cowork session can complete all 10 test categories with zero critical failures, and can simulate a complete real-world workflow (read memory → work → push) without errors.

---

## Test Scope

| Category | What We Test | Why | Pass/Fail Criteria |
|----------|---|---|---|
| **4.1: Startup** | All files load, URLs valid, no 404s | System foundation | 10/10 files readable, all URLs live |
| **4.2: Content** | File content accurate, paths correct, consistency | System correctness | No stale paths, no contradictions |
| **4.3: Dashboard** | Features work, sync functions | Primary UX interface | Dashboard loads, toggle/add/mark done work |
| **4.4: GitHub Integration** | Repo state, file sync, deploy timing | Source of truth | No uncommitted files, Pages deploys <30s |
| **4.5: Scheduling** | 5:30pm wrap-up task exists, cron valid | Automation foundation | Task scheduled, fires on time |
| **4.6: Memory System** | Project memory files exist, routing table complete | Knowledge base | All project files readable |
| **4.7: Real-World Workflow** | Fresh session → read → work → push → verify | End-to-end | Can complete full cycle without errors |
| **4.8: Edge Cases** | Offline behavior, race conditions, auth failures | Resilience | System degrades gracefully |
| **4.9: Performance** | Dashboard load time, file sizes, sync latency | User experience | Dashboard <3s cold load, sync <5s |
| **4.10: Security** | XSS, injection, token exposure, auth | Safety | No security findings |

---

## Test Execution Plan

### Phase 4.1: Complete Startup Protocol (30 min)

**Objective:** Verify that a brand-new Cowork session can bootstrap successfully.

**Preconditions:**
- Fresh Cowork session started (new Claude instance)
- `/mnt/Projects` mounted to local user directory
- No prior context loaded

**Test Steps:**

```bash
# T-4.1.1: Read CLAUDE.md from GitHub
- URL: https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md
- Expected: File readable, >5KB, contains "Me", "Companies", "File System" sections
- Check: No 404, no timeout, no encoding issues

# T-4.1.2: Read TASKS.md from GitHub
- URL: https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/TASKS.md
- Expected: File readable, contains "Phase 1", "Phase 2", "Phase 3", "Phase 4" sections
- Check: Master task list matches local version

# T-4.1.3: Read DASHBOARD-TASKS.md from GitHub
- URL: https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/DASHBOARD-TASKS.md
- Expected: File readable, contains Personal/Professional/Freelance sections
- Check: 150+ tasks, status markers intact

# T-4.1.4: Read CLAUDE-COWORK-OPERATING-SYSTEM.md from GitHub
- URL: https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE-COWORK-OPERATING-SYSTEM.md
- Expected: File readable, contains "Session Startup", "Memory Routing Table" sections
- Check: All 4 routing table entries present

# T-4.1.5: Verify local file paths
- Read: /mnt/Projects/CLAUDE.md (should match GitHub version)
- Read: /mnt/Projects/TASKS.md (should match GitHub version)
- Read: /mnt/Projects/Productivity/DASHBOARD-TASKS.md
- Check: Timestamps recent (within 7 days of last commit)

# T-4.1.6: Read memory routing files
- /mnt/Projects/Productivity/memory/session-log.md (exists, >1KB)
- /mnt/Projects/Productivity/memory/dashboard-changelog.md (exists, >5KB)
- /mnt/Projects/Productivity/memory/sync-automation-audit.md (exists, documents broken sync)
- /mnt/Projects/Productivity/memory/context/ohtani-matrix.md (exists, locked goal defined)
- /mnt/Projects/Productivity/memory/projects/ (directory contains 4+ project files)
- Check: All files readable, no corruption

# T-4.1.7: Verify .gitignore
- Read: /mnt/Projects/.gitignore
- Expected: Contains N8N/ai_agents_az (task #29 not yet done)
- Check: File readable, standard entries present

# T-4.1.8: Verify git status is clean
- Run: git status --short
- Expected: 0 untracked files OR only CLAUDE-COWORK-OPERATING-SYSTEM-PLAINTEXT.txt
- Check: No stray modified files, staging area clean
```

**Success Criteria:**
- ✓ All 8 tests pass (0 failures)
- ✓ All GitHub URLs return 200 OK
- ✓ Local files match GitHub versions (byte-for-byte or near-identical)
- ✓ Git status shows clean working tree
- ✓ No file read errors

**Failure Mode:** If ANY test fails, print file content and error to debug log.

---

### Phase 4.2: Dashboard Verification (30 min)

**Objective:** Confirm GitHub Pages dashboard is live, features work, and cloud sync functions.

**Test Steps:**

```bash
# T-4.2.1: Dashboard loads in browser
- URL: https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html
- Expected: Page loads, renders task lists, no 404
- Check: HTTP 200, <3 second load time, no console errors

# T-4.2.2: Dashboard features work
- Toggle Personal/Work mode
  - Expected: Task list filters (Personal vs Professional vs Freelance visible)
  - Check: Both modes show correct section titles
- Add a test task
  - Expected: Task appears in Personal list, counter increments
  - Check: Task persists on page reload
- Mark test task as done
  - Expected: Task moves to Done log, XP counter increments
  - Check: Task no longer in open list

# T-4.2.3: GitHub Gist cloud sync
- Prerequisite: yl_gist_token set in localStorage (use saved token from previous session)
- Action: Complete another task (requires successful Gist auth)
- Expected: Gist syncs successfully (UI shows "✓ synced")
- Check: Open another browser → clear localStorage → reload → data persists from Gist

# T-4.2.4: Dashboard file size and structure
- File: /mnt/Projects/Productivity/dashboard.html
- Expected: 4,305 lines (±100 lines acceptable)
- Check: No minification corruption, HTML structure valid

# T-4.2.5: GitHub Pages deploy timing
- Action: Make a trivial change to dashboard.html (add comment)
- Commit & push: git push origin main
- Expected: GitHub Pages deploys within 30 seconds
- Check: New version live at GitHub Pages URL (compare file hash or timestamp)

# T-4.2.6: TASKS.md sync functionality
- Prerequisite: GitHub token available
- Action: Click "↑ Sync TASKS" button in topbar
- Expected: Button shows "syncing..." then "✓ synced" (or "error" if auth missing)
- Check: TASKS.md updated in GitHub repo with new completed task
```

**Success Criteria:**
- ✓ Dashboard loads <3s
- ✓ All 6 features work without JavaScript errors
- ✓ GitHub Gist sync works (if token available)
- ✓ GitHub Pages deploys <30s
- ✓ No console errors

**Failure Mode:** If dashboard fails to load, check GitHub Pages build status. If features fail, check localStorage and console for JavaScript errors.

---

### Phase 4.3: Document Consistency Check (20 min)

**Objective:** Identify stale paths, contradictions, or accuracy issues.

**Test Steps:**

```bash
# T-4.3.1: Cross-reference file paths
- CLAUDE.md lists paths under "File System"
  - /Users/yohanloyer/Projects/Productivity/
  - /Users/yohanloyer/Projects/Nébuleuse Bijoux/
  - /Users/yohanloyer/Projects/Gorgias/
  - /Users/yohanloyer/Projects/Linkedin posting/
  - /Users/yohanloyer/Projects/N8N/
- Check: Are these referenced anywhere in CLAUDE-COWORK-OPERATING-SYSTEM.md?
- Expected: Paths are illustrative (local setup on macOS), not required for execution
- Action: Note any discrepancies

# T-4.3.2: Operating System references
- CLAUDE-COWORK-OPERATING-SYSTEM.md references:
  - GitHub raw URLs (should be live)
  - Local paths (should use /mnt/Projects equivalent)
  - Routing table (should list all 4 project files)
- Check: All references are internally consistent

# T-4.3.3: Task status accuracy
- Sample 5 "Done" tasks from DASHBOARD-TASKS.md (marked [x])
  - Cross-ref session-log.md: when were they marked done?
  - Expected: All [x] tasks have session-log entries
  - Check: No orphaned done markers

# T-4.3.4: Dashboard-TASKS.md sync status
- DASHBOARD-TASKS.md states: "Dashboard v2.5... Features: ..."
- Check dashboard.html actual feature set
- Expected: Features match or exceed DASHBOARD-TASKS.md description
- Action: Update DASHBOARD-TASKS.md if description is stale

# T-4.3.5: URL validity
- All URLs in CLAUDE.md and CLAUDE-COWORK-OPERATING-SYSTEM.md
  - GitHub URLs (raw.githubusercontent.com)
  - GitHub Pages URLs (github.io)
  - External links (icvk1xljokz.typeform.com, nebuleusebijoux.com, etc.)
- Check: HEAD request returns 200 (or 301 redirect)
- Expected: No broken links
```

**Success Criteria:**
- ✓ All paths are consistent or documented as illustrative
- ✓ No internal contradictions
- ✓ All GitHub URLs valid
- ✓ No stale task markings
- ✓ File descriptions match actual file state

**Failure Mode:** Document issues in a "PHASE_4_ISSUES.md" file for later remediation.

---

### Phase 4.4: Git & GitHub Integration (20 min)

**Objective:** Verify repository state, commit history, and deployment.

**Test Steps:**

```bash
# T-4.4.1: Repository health
- Run: git status
- Expected: On branch main, no uncommitted changes (except plaintext file)
- Check: Staging area clean, working tree clean

# T-4.4.2: Commit history integrity
- Run: git log --oneline -20
- Expected: 20+ commits, messages are clear
- Check: No malformed commits, dates reasonable (all 2026)

# T-4.4.3: Remote sync
- Run: git fetch origin main && git diff --name-only main origin/main
- Expected: No difference (local = remote)
- Check: Local and remote are in sync

# T-4.4.4: Branch protection
- GitHub web: check branch main settings
- Expected: main branch is protected, requires PR review (or documented as intentionally unprotected)
- Action: Note protection status

# T-4.4.5: GitHub Actions (CI/CD)
- GitHub web: check Actions tab for recent runs
- Expected: Pages deploy workflow exists and succeeded
- Check: Latest build <24h old, status = success

# T-4.4.6: File permissions
- Run: find /mnt/Projects -type f -name "*.md" -exec ls -l {} \; | head -10
- Expected: All files readable by cowork user (644 or 600)
- Check: No permission errors when reading files
```

**Success Criteria:**
- ✓ Git status clean
- ✓ Commits well-formed and recent
- ✓ Local = remote
- ✓ GitHub Pages deploy workflow exists
- ✓ All files readable

**Failure Mode:** If remote differs, run git pull and re-test.

---

### Phase 4.5: Scheduled Tasks (15 min)

**Objective:** Verify the 5:30pm wrap-up task is scheduled and configured correctly.

**Test Steps:**

```bash
# T-4.5.1: Scheduled task exists
- Check: /Users/yohanloyer/Documents/Claude/Scheduled/ directory
- Expected: process-claude-task-queue/SKILL.md file exists
- Check: Readable, contains prompt and cron expression

# T-4.5.2: Wrap-up task timing
- Expected: 5:30pm (17:30) local time, daily
- Check: Cron expression = "30 17 * * *" (5:30pm) or documented equivalent
- Note: May not be implemented yet (Phase 3 task)

# T-4.5.3: Scheduled task structure
- File should contain:
  - Clear instructions for what to do at 5:30pm
  - Reference to session-log.md and dashboard-changelog.md
  - Git push command ready to execute
  - Template for CLAUDE.md update proposal
- Expected: Full automation-ready template
- Check: No manual steps required

# T-4.5.4: Fallback for missing scheduled task
- If task doesn't exist: document that Phase 3.2 (Setup scheduling) is pending
- Check: Phase 3.3 (CLAUDE.md update proposals) also pending
- Note: System works without scheduling, but daily wrap-ups are manual
```

**Success Criteria:**
- ✓ Process scheduler task exists (Phase 3.1 complete) OR documented as pending (Phase 3.2)
- ✓ Wrap-up timing is documented (even if not automated)
- ✓ Session-log structure clear and maintained

**Failure Mode:** If scheduled tasks missing, this is expected (Phase 3 not yet complete). Document for Phase 3 execution.

---

### Phase 4.6: Memory System Routing (15 min)

**Objective:** Verify all project memory files exist and routing table is complete.

**Test Steps:**

```bash
# T-4.6.1: Memory routing table coverage
- CLAUDE-COWORK-OPERATING-SYSTEM.md lists:
  | If working on... | Read this file |
  | Nébuleuse AI Agent | Productivity/memory/projects/nebuleuse-bijoux.md |
  | Accessory Partners | Productivity/memory/projects/accessory-partners.md |
  | Gorgias Help Center | Productivity/memory/projects/gorgias-agency.md |
  | LinkedIn content | Productivity/memory/projects/linkedin-content-system.md |

- Check: All 4 files exist and are readable
- Expected: Each file >2KB, contains project-specific context
- Action: Verify content relevance

# T-4.6.2: Memory directory structure
- Expected structure:
  /mnt/Projects/Productivity/memory/
    ├── context/
    │   ├── ohtani-matrix.md (decision OS)
    │   ├── adhd-dashboard-research.md (optional)
    ├── projects/
    │   ├── nebuleuse-bijoux.md
    │   ├── accessory-partners.md
    │   ├── gorgias-agency.md
    │   ├── linkedin-content-system.md
    ├── session-log.md
    ├── dashboard-changelog.md
    ├── sync-automation-audit.md
    └── code-review-log.md

- Check: All directories and files present
- Expected: 8+ files, 0 corruption

# T-4.6.3: Ohtani Matrix (decision OS)
- File: /mnt/Projects/Productivity/memory/context/ohtani-matrix.md
- Expected: Locked goal documented, 3 levers defined, constraints clear
- Check: Readable and up-to-date (not stale)
- Action: Verify goal = "€50K net/year within 3 years, ≤20h/week"

# T-4.6.4: Session log currency
- File: /mnt/Projects/Productivity/memory/session-log.md
- Expected: Latest entry ≤7 days old
- Check: Format consistent (YYYY-MM-DD | topic | session type)
- Action: Note most recent session date

# T-4.6.5: Project memory freshness
- Sample 1 file: nebuleuse-bijoux.md
- Expected: Mentions Phase 1/2 progress, baseline metrics, recent actions
- Check: Not outdated or contradicting CLAUDE.md
- Action: Flag if >30 days stale
```

**Success Criteria:**
- ✓ All 4 routing table files exist and readable
- ✓ Memory directory structure complete
- ✓ Ohtani Matrix locked goal matches CLAUDE.md
- ✓ Session log ≤7 days old
- ✓ Project memory files are current

**Failure Mode:** If any file missing, create a stub with template content and note in ISSUES.

---

### Phase 4.7: Real-World Workflow Simulation (45 min)

**Objective:** Simulate a complete user session (bootstrap → work → commit).

**Preconditions:**
- Fresh Cowork session
- All Phase 4.1-4.6 tests passed
- GitHub token available in environment

**Test Scenario:** "Handle a Nébuleuse task: implement Baback integration checklist share"

**Workflow Steps:**

```bash
# Step 1: Read system memory (5 min)
- Read CLAUDE.md from GitHub (full context loading)
- Read TASKS.md
- Read DASHBOARD-TASKS.md
- Read /mnt/Projects/Productivity/memory/projects/nebuleuse-bijoux.md
- Confirm: ✓ Read complete (log in chat)

# Step 2: Understand task (10 min)
- Task: "Share Baback integration checklist with client"
- Status: [>] Important, but not assigned
- Context from memory: Baback integration = +45-52% automation unlock
- Action: Simulate task analysis (no actual work needed)
- Output: 2-3 sentence summary of what needs to be done

# Step 3: Update dashboard (5 min)
- Simulate: Go to Nébuleuse Freelance section, mark "Share Baback integration checklist" as [~] In Progress
- Action: Take screenshot of dashboard state change
- Verify: Task now shows [~] in-progress status

# Step 4: Simulate work completion (10 min)
- Simulate: Create a brief "work output" (e.g., text summary or document)
- Action: Write output to `/tmp/baback-checklist-summary.txt` for demo purposes
- Content: "Baback Integration Checklist - Ready for Client. Includes: [...items...]"

# Step 5: Update task and commit (10 min)
- Mark task as done [x] in dashboard
- Add task note: "Shared via email on 2026-04-19, awaiting client feedback"
- Trigger: "↑ Sync TASKS" button in dashboard
- Expected: TASKS.md updates in GitHub within 5 seconds
- Verify: git log shows new commit with task completion

# Step 6: Update session log (5 min)
- Simulate: Create session-log entry for this session
- Format: ## YYYY-MM-DD | Nébuleuse Baback Checklist Share | Phase 4 Test
- Content: "Requested: [task], Done: [completion], Key decision: [...]"
- Action: Append to /mnt/Projects/Productivity/memory/session-log.md

# Step 7: Final verification (5 min)
- Run: git status (should show session-log.md modified + TASKS.md synced)
- Run: git log --oneline -3 (should show latest commits)
- Verify: Dashboard state matches GitHub state
- Expected: Everything in sync, no errors
```

**Success Criteria:**
- ✓ All 7 steps completed without errors
- ✓ TASKS.md syncs to GitHub successfully
- ✓ Session log created and committed
- ✓ No manual git commands needed (UI sync works)
- ✓ Dashboard and GitHub states match

**Failure Mode:** Document error at which step it fails. If sync fails, check auth token and retry.

---

### Phase 4.8: Edge Cases & Resilience (45 min)

**Objective:** Verify system behavior under stress, offline, and auth failure scenarios.

**Test Steps:**

```bash
# T-4.8.1: Offline behavior
- Precondition: Complete a task
- Action: Disable network (simulate offline)
- Expected: Dashboard continues to work locally
- Action: Try to sync TASKS.md
- Expected: Sync fails gracefully (not crash), UI shows error
- Action: Restore network
- Expected: Next sync succeeds, no data loss

# T-4.8.2: Auth token missing
- Action: Clear localStorage (remove yl_gist_token)
- Action: Try to sync TASKS.md or use Gist cloud sync
- Expected: UI shows "Auth required" message, with link to set token
- Expected: No cryptic error, no crash
- Action: Set token and retry
- Expected: Sync succeeds

# T-4.8.3: Malformed task data
- Action: Manually edit dashboard.html to inject invalid JSON in localStorage
- Action: Reload dashboard
- Expected: Dashboard detects corruption, falls back to fresh state
- Expected: No crash, no data loss

# T-4.8.4: Race condition: rapid task completion
- Action: Complete 5 tasks in <2 seconds (click rapidly)
- Expected: Dashboard marks all as done locally
- Action: Click "↑ Sync TASKS"
- Expected: All 5 task completions sync to GitHub in single commit
- Expected: No duplicate entries, no sync conflicts

# T-4.8.5: GitHub API rate limit
- Action: Trigger 50 syncs in 1 minute (rapid task completions + sync clicks)
- Expected: GitHub API returns 429 Too Many Requests
- Expected: Dashboard shows rate limit error (not crash)
- Action: Wait 1 minute, retry
- Expected: Sync succeeds after rate limit resets

# T-4.8.6: Corrupted GitHub file
- Action: Manually corrupt TASKS.md on GitHub (edit raw, save invalid structure)
- Action: Try to sync from dashboard
- Expected: Sync detects invalid JSON/YAML, shows error
- Expected: Fallback to local version, doesn't overwrite corruption
- Action: Fix file manually, retry
- Expected: Sync succeeds

# T-4.8.7: Dashboard file download/cache
- Action: Do NOT clear browser cache
- Action: Reload dashboard 10 times in rapid succession
- Expected: All 10 loads use cached version (no GitHub API calls)
- Expected: Load time <100ms (cached)
- Check: Browser DevTools Network tab shows 304 Not Modified responses
```

**Success Criteria:**
- ✓ 7/7 edge cases handled gracefully
- ✓ No crashes or unrecoverable errors
- ✓ Error messages are user-friendly
- ✓ System degrades gracefully (works offline, shows auth errors, etc.)
- ✓ No data loss in any scenario

**Failure Mode:** For each failed edge case, document the error and root cause for Phase 4 remediation.

---

### Phase 4.9: Performance & Load Testing (30 min)

**Objective:** Verify dashboard load times, file sizes, and sync latency meet expectations.

**Test Steps:**

```bash
# T-4.9.1: Dashboard cold load time
- Clear browser cache completely
- Load dashboard for first time
- Measure: Time from page load to "fully interactive" (all features clickable)
- Expected: <3 seconds (measured by browser DevTools Performance tab)
- Action: Repeat 3 times, take average

# T-4.9.2: Dashboard hot load time
- Page already loaded and cached
- Reload dashboard (Cmd+R)
- Measure: Time to fully rendered
- Expected: <500ms (cached version)

# T-4.9.3: File sizes
- dashboard.html: Expected 240KB-250KB (4,305 lines)
- CLAUDE.md: Expected 10KB-12KB
- TASKS.md: Expected 2KB-3KB
- DASHBOARD-TASKS.md: Expected 11KB-12KB
- Check: No unexplained bloat (likely minification issues)

# T-4.9.4: GitHub API response time
- Action: Fetch CLAUDE.md from GitHub raw URL
- Measure: Time to first byte (TTFB)
- Expected: <200ms (GitHub CDN)
- Repeat 5 times, take average

# T-4.9.5: TASKS.md sync latency
- Action: Complete a task, click "↑ Sync TASKS"
- Measure: Time from click to "✓ synced" UI message
- Expected: <5 seconds (includes network + GitHub API + re-render)
- Note: 5s is reasonable for GitHub API call + commit + deploy time

# T-4.9.6: GitHub Gist cloud sync latency
- Precondition: yl_gist_token configured
- Action: Complete a task, wait for auto-sync in beforeunload
- Measure: Time to sync completion (check browser DevTools Network tab)
- Expected: <2 seconds (Gist API is faster than repo commits)

# T-4.9.7: Dashboard memory usage
- Action: Load dashboard
- Open browser DevTools, Memory tab
- Take heap snapshot
- Expected: <10MB heap usage (no memory leaks)
- Action: Complete 50 tasks, take another snapshot
- Expected: No significant increase (memory-efficient)

# T-4.9.8: Concurrent operations
- Action: Load 3 browser tabs, all running dashboard
- Simultaneously: Sync in tab 1, add task in tab 2, mark done in tab 3
- Expected: All 3 operations complete without interference
- Check: No race conditions, final state consistent
```

**Success Criteria:**
- ✓ Cold load <3s, hot load <500ms
- ✓ File sizes reasonable (<1MB total)
- ✓ GitHub API response <200ms
- ✓ TASKS.md sync <5s, Gist sync <2s
- ✓ Memory usage <10MB, no leaks
- ✓ Concurrent operations safe

**Failure Mode:** If any test fails, document numbers and root cause. Minor failures (e.g., cold load 3.5s instead of <3s) may be acceptable depending on network conditions.

---

### Phase 4.10: Security Audit (30 min)

**Objective:** Verify no security vulnerabilities exist in dashboard or OS design.

**Test Steps:**

```bash
# T-4.10.1: XSS vulnerability scan
- Task: Manually test XSS vectors
  - Add task with name: <img src=x onerror="alert('XSS')">
  - Add task with name: <script>alert('XSS')</script>
  - Add task note: <svg onload="alert('XSS')">
- Expected: All injected content rendered as literal text, not executed
- Check: No browser alerts triggered

# T-4.10.2: Token exposure
- Check: localStorage for yl_gist_token
- Expected: Token present (needed for auth), but never logged to console
- Action: Add task, complete task, sync
- Expected: Token never appears in network requests URL (must be in header)
- Check: DevTools Network tab shows no tokens in query parameters

# T-4.10.3: Session/CSRF protection
- Action: Open dashboard in 2 tabs simultaneously
- Action: Sync TASKS in tab 1 while tab 2 is syncing
- Expected: Second sync queues or shows "already syncing" message
- Expected: No race condition, no double-submit
- Check: GitHub commit shows single commit (not duplicate)

# T-4.10.4: Sensitive data in logs
- Action: Read dashboard.html source code
- Search: for "password", "secret", "key", "token" (case-insensitive)
- Expected: Only yl_gist_token mentioned (in localStorage getter/setter)
- Expected: No hardcoded credentials, no API keys, no personal data

# T-4.10.5: Input sanitization
- Action: Add task with unusual characters: é, 中, 🚀, \n, \t
- Expected: All characters render correctly, no encoding issues
- Expected: Newlines in task name don't break TASKS.md format

# T-4.10.6: Access control
- Precondition: dashboard.html on public GitHub Pages URL
- Action: Try to read user's Gist data without token
- Expected: Gist API returns 403 Forbidden (Gist is private)
- Expected: Dashboard shows "Please set your token" message

# T-4.10.7: Code review: dashboard.html
- Review 5 random functions (line numbers pulled from git diff --stat)
- Check: escapeHtml() used for user input before rendering?
- Check: JSON.parse() wrapped in try/catch?
- Check: Event listeners use data-* attributes, not onclick/onload?
- Expected: Modern, defensive coding practices

# T-4.10.8: Dependencies and supply chain
- Action: Check dashboard.html for <script src="..."> imports
- Expected: Only standard browser APIs (no external CDN)
- Expected: No package managers, no npm modules (single HTML file)
- Check: No supply chain attack surface

# T-4.10.9: File permissions check
- Run: ls -la /mnt/Projects/Productivity/dashboard.html
- Expected: Permissions 644 (readable by all, writable by owner only)
- Check: No world-writable files

# T-4.10.10: GitHub token scope
- Check: Cowork global instructions or environment variables
- Expected: Token has repo + gist scope (minimum required)
- Expected: Token NOT exposed in logs, config files, or documentation
```

**Success Criteria:**
- ✓ 0 XSS vulnerabilities
- ✓ 0 token exposure incidents
- ✓ No CSRF issues
- ✓ No hardcoded credentials
- ✓ Input properly sanitized
- ✓ Access control enforced
- ✓ Code follows security best practices
- ✓ No supply chain risks
- ✓ File permissions correct
- ✓ Token scope minimal and secure

**Failure Mode:** Any security finding = critical. Document with proof-of-concept and fix immediately before proceeding.

---

## Test Execution Order

**Sequential execution (dependencies between phases):**

1. **Phase 4.1: Startup** (30 min) — Foundation test
2. **Phase 4.2: Dashboard** (30 min) — Depends on 4.1
3. **Phase 4.3: Consistency** (20 min) — Depends on 4.1
4. **Phase 4.4: Git Integration** (20 min) — Depends on 4.1
5. **Phase 4.5: Scheduling** (15 min) — Independent
6. **Phase 4.6: Memory** (15 min) — Depends on 4.1
7. **Phase 4.7: Real Workflow** (45 min) — Depends on 4.1-4.6
8. **Phase 4.8: Edge Cases** (45 min) — Depends on 4.2, 4.7
9. **Phase 4.9: Performance** (30 min) — Independent
10. **Phase 4.10: Security** (30 min) — Independent

**Total Execution Time:** ~4 hours (can be parallelized for 4.5, 4.9, 4.10)

**Recommended Schedule:**
- **Session 1 (Friday):** 4.1-4.7 (2.5 hours)
- **Session 2 (Friday):** 4.8 + 4.9 + 4.10 in parallel (1.5 hours)

---

## Test Automation & Scripts

### Script 1: Automated Startup Verification

```bash
#!/bin/bash
# FILE: test-phase-4.1-startup.sh
# Runs all startup protocol tests

set -e

GITHUB_BASE="https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main"
PROJECT_ROOT="/mnt/Projects"
RESULTS_FILE="/tmp/phase-4.1-results.txt"

echo "=== Phase 4.1: Startup Protocol Test ===" | tee $RESULTS_FILE
echo "Timestamp: $(date -u +'%Y-%m-%d %H:%M:%S UTC')" | tee -a $RESULTS_FILE
echo ""

# T-4.1.1: CLAUDE.md from GitHub
echo "T-4.1.1: Fetching CLAUDE.md from GitHub..." | tee -a $RESULTS_FILE
if curl -sf "$GITHUB_BASE/CLAUDE.md" > /tmp/claude-github.md 2>&1; then
  SIZE=$(wc -c < /tmp/claude-github.md)
  CONTAINS_COMPANIES=$(grep -c "^| \*\*Gorgias\*\*" /tmp/claude-github.md || echo "0")
  if [ $SIZE -gt 5000 ] && [ $CONTAINS_COMPANIES -eq 1 ]; then
    echo "✓ CLAUDE.md OK (size: ${SIZE} bytes, has Companies section)" | tee -a $RESULTS_FILE
  else
    echo "✗ CLAUDE.md FAILED (invalid content)" | tee -a $RESULTS_FILE
  fi
else
  echo "✗ CLAUDE.md FAILED (fetch error)" | tee -a $RESULTS_FILE
fi

# T-4.1.2: TASKS.md from GitHub
echo "T-4.1.2: Fetching TASKS.md from GitHub..." | tee -a $RESULTS_FILE
if curl -sf "$GITHUB_BASE/TASKS.md" > /tmp/tasks-github.md 2>&1; then
  SIZE=$(wc -c < /tmp/tasks-github.md)
  HAS_PHASE_1=$(grep -c "Phase 1:" /tmp/tasks-github.md || echo "0")
  HAS_PHASE_4=$(grep -c "Phase 4:" /tmp/tasks-github.md || echo "0")
  if [ $SIZE -gt 1500 ] && [ $HAS_PHASE_1 -eq 1 ] && [ $HAS_PHASE_4 -eq 1 ]; then
    echo "✓ TASKS.md OK (size: ${SIZE} bytes, all phases present)" | tee -a $RESULTS_FILE
  else
    echo "✗ TASKS.md FAILED (invalid content)" | tee -a $RESULTS_FILE
  fi
else
  echo "✗ TASKS.md FAILED (fetch error)" | tee -a $RESULTS_FILE
fi

# T-4.1.3: DASHBOARD-TASKS.md from GitHub
echo "T-4.1.3: Fetching DASHBOARD-TASKS.md from GitHub..." | tee -a $RESULTS_FILE
if curl -sf "$GITHUB_BASE/Productivity/DASHBOARD-TASKS.md" > /tmp/dashboard-tasks-github.md 2>&1; then
  SIZE=$(wc -c < /tmp/dashboard-tasks-github.md)
  HAS_PERSONAL=$(grep -c "## 🧑 Personal" /tmp/dashboard-tasks-github.md || echo "0")
  HAS_FREELANCE=$(grep -c "## 🔧 Freelance" /tmp/dashboard-tasks-github.md || echo "0")
  if [ $SIZE -gt 8000 ] && [ $HAS_PERSONAL -eq 1 ] && [ $HAS_FREELANCE -eq 1 ]; then
    echo "✓ DASHBOARD-TASKS.md OK (size: ${SIZE} bytes)" | tee -a $RESULTS_FILE
  else
    echo "✗ DASHBOARD-TASKS.md FAILED (invalid content)" | tee -a $RESULTS_FILE
  fi
else
  echo "✗ DASHBOARD-TASKS.md FAILED (fetch error)" | tee -a $RESULTS_FILE
fi

# T-4.1.5: Local files match GitHub versions (spot check)
echo "T-4.1.5: Comparing local files to GitHub versions..." | tee -a $RESULTS_FILE
LOCAL_CLAUDE=$(cat "$PROJECT_ROOT/CLAUDE.md" 2>/dev/null | wc -c)
GITHUB_CLAUDE=$(wc -c < /tmp/claude-github.md)
if [ "$LOCAL_CLAUDE" -eq "$GITHUB_CLAUDE" ]; then
  echo "✓ Local CLAUDE.md matches GitHub (byte-identical)" | tee -a $RESULTS_FILE
else
  echo "⚠ Local CLAUDE.md differs from GitHub (diff size: $(($LOCAL_CLAUDE - $GITHUB_CLAUDE)) bytes)" | tee -a $RESULTS_FILE
fi

# T-4.1.8: Git status
echo "T-4.1.8: Checking git status..." | tee -a $RESULTS_FILE
cd "$PROJECT_ROOT"
GIT_STATUS=$(git status --short | wc -l)
if [ $GIT_STATUS -eq 0 ] || [ $GIT_STATUS -eq 1 ]; then
  echo "✓ Git status clean (${GIT_STATUS} untracked files)" | tee -a $RESULTS_FILE
else
  echo "✗ Git status FAILED (${GIT_STATUS} untracked files)" | tee -a $RESULTS_FILE
fi

echo ""
echo "Test results saved to: $RESULTS_FILE"
```

**Usage:**
```bash
chmod +x test-phase-4.1-startup.sh
./test-phase-4.1-startup.sh
```

### Script 2: Dashboard Feature Test (Interactive)

```bash
#!/bin/bash
# FILE: test-phase-4.2-dashboard.sh
# Manual (or semi-automated) dashboard feature test

DASHBOARD_URL="https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html"

echo "=== Phase 4.2: Dashboard Verification Test ==="
echo ""
echo "T-4.2.1: Opening dashboard at: $DASHBOARD_URL"
echo "  Expected: Page loads in <3 seconds, no 404"
echo ""

# Measure load time
START_TIME=$(date +%s%N)
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$DASHBOARD_URL")
END_TIME=$(date +%s%N)
LOAD_TIME_MS=$(( (END_TIME - START_TIME) / 1000000 ))

if [ "$HTTP_STATUS" = "200" ]; then
  echo "✓ HTTP Status 200 OK"
  echo "  Load time: ${LOAD_TIME_MS}ms"
  if [ $LOAD_TIME_MS -lt 3000 ]; then
    echo "  ✓ Load time <3s"
  else
    echo "  ⚠ Load time >3s (acceptable if network is slow)"
  fi
else
  echo "✗ HTTP Status $HTTP_STATUS (FAILED)"
  exit 1
fi

echo ""
echo "T-4.2.2-T-4.2.6: Manual testing required"
echo "  → Open $DASHBOARD_URL in browser"
echo "  → Test: Personal/Work toggle"
echo "  → Test: Add task"
echo "  → Test: Mark task done"
echo "  → Test: Cloud sync (if token configured)"
echo "  → Check: No console errors (F12 → Console tab)"
echo ""
echo "Once complete, confirm in chat: Tests passed (Y/N)"
```

### Script 3: Security XSS Test

```bash
#!/bin/bash
# FILE: test-phase-4.10-security.sh
# Basic XSS vulnerability test

DASHBOARD_FILE="/mnt/Projects/Productivity/dashboard.html"

echo "=== Phase 4.10: Security Audit (Automated Checks) ==="
echo ""

# Check 1: No hardcoded tokens
echo "Check 1: Searching for hardcoded credentials..."
if grep -i "ghp_\|ghs_\|ghu_\|ghr_" "$DASHBOARD_FILE" >/dev/null 2>&1; then
  echo "✗ FOUND hardcoded GitHub token (SECURITY RISK)"
  exit 1
else
  echo "✓ No hardcoded GitHub tokens detected"
fi

# Check 2: XSS mitigation functions present
echo "Check 2: Verifying XSS mitigation functions..."
if grep -q "function escapeHtml" "$DASHBOARD_FILE"; then
  echo "✓ escapeHtml() function defined"
else
  echo "⚠ escapeHtml() not found (may be using different sanitization)"
fi

# Check 3: Dangerous patterns
echo "Check 3: Checking for dangerous DOM manipulation patterns..."
DANGEROUS_PATTERNS=$(grep -c "\.innerHTML\s*=" "$DASHBOARD_FILE" || echo "0")
if [ "$DANGEROUS_PATTERNS" -gt 0 ]; then
  echo "⚠ Found $DANGEROUS_PATTERNS instances of innerHTML assignment"
  echo "  (may or may not be safe depending on source)"
else
  echo "✓ No innerHTML assignments detected"
fi

# Check 4: Event handler patterns
echo "Check 4: Checking for onclick/on* attributes in HTML..."
ONCLICK_COUNT=$(grep -c "onclick=" "$DASHBOARD_FILE" || echo "0")
if [ "$ONCLICK_COUNT" -gt 0 ]; then
  echo "⚠ Found $ONCLICK_COUNT onclick attributes (prefer event delegation)"
else
  echo "✓ No onclick attributes detected (good security practice)"
fi

echo ""
echo "Automated security checks complete."
echo "Manual review still required (see Phase 4.10.7 in test plan)"
```

---

## Go/No-Go Decision Criteria

### Go Decision (Proceed to Production)

**ALL of the following must be true:**

1. **Phase 4.1-4.4** (Startup, Dashboard, Consistency, Git): 100% pass rate
2. **Phase 4.6** (Memory): All 4 routing table files exist and are current
3. **Phase 4.7** (Real Workflow): Complete session simulation passes without errors
4. **Phase 4.10** (Security): 0 critical findings, <3 low/medium findings
5. **Issues Log**: All critical issues resolved, remaining issues documented for future sprints
6. **Performance** (4.9): Dashboard load <3s (cold), TASKS.md sync <5s, no memory leaks
7. **Sign-off**: Product Owner (Yohan) reviews test results and approves

### No-Go Decision (Return to Phase 3)

**If any of the following are true:**

1. Any critical failure in Phase 4.1 (startup protocol broken)
2. Dashboard fails to load or core features don't work (Phase 4.2)
3. Security vulnerabilities found (Phase 4.10)
4. Real-world workflow fails (Phase 4.7) — missing critical integrations
5. GitHub integration broken (Phase 4.4) — can't push or pull changes
6. More than 5 high-priority issues identified

**Remediation Path:**
- Phase 4 returns to Phase 3
- Issues logged in `PHASE_4_ISSUES.md`
- Phase 3 work resumes to fix blocking issues
- Re-test Phase 4 in new session
- Go/No-Go decision when all issues resolved

---

## Rollback & Recovery Strategy

**If Phase 4 fails:**

1. **Identify failure point** — Which test failed? Phase 4.X?
2. **Isolate issue** — Root cause analysis from test logs
3. **Branch (optional)** — If major code changes needed, create `phase-4-fix` branch
4. **Fix implementation** — Minimal changes to address issue
5. **Re-test only affected phase** — Don't re-run all 10 phases
6. **Verify no regressions** — Run Phase 4.1, 4.3, 4.10 again (quick checks)
7. **Merge & push** — Once verified, push to main and re-run full Phase 4

**Rollback Commands (if needed):**

```bash
# If Phase 4 caused regressions, revert to last known good state
git revert HEAD --no-edit
git push origin main

# If GitHub Pages deploy failed
git log --oneline -1 Productivity/dashboard.html
git show COMMIT_HASH:Productivity/dashboard.html > /tmp/dashboard-backup.html
# Review /tmp/dashboard-backup.html, then restore if necessary
```

---

## Test Artifacts & Documentation

**All tests produce:**

1. **Phase 4 Results Summary** — PASS/FAIL per test, total time, date
2. **Issues Log** — `PHASE_4_ISSUES.md` (critical + recommendations)
3. **Performance Metrics** — Load times, sync latencies, memory usage
4. **Security Audit Report** — Vulnerabilities found (if any) + fixes
5. **Test Logs** — Full output from each shell script (saved to `/tmp/`)

**Saved to:**
```
/Users/yohanloyer/Projects/  (committed to GitHub in f343635)
├── PHASE_4_TESTING_STRATEGY.md (this file)
├── PHASE_4_RESULTS_TEMPLATE.md (fill in during testing)
├── PHASE_4_ISSUES.md (create if issues found)
└── PHASE_4_SECURITY_AUDIT.md (create if security findings)
```

---

## Execution Checklist

Use this when running Phase 4:

```markdown
## Phase 4 Execution Checklist

### Pre-Test (Before Starting)
- [ ] Fresh Cowork session (no prior context)
- [ ] GitHub token available (yl_gist_token)
- [ ] Network connection stable
- [ ] All prerequisite files exist (CLAUDE.md, TASKS.md, etc.)
- [ ] Browser (for 4.2, 4.9, 4.10) ready

### Phase 4.1: Startup
- [ ] T-4.1.1: CLAUDE.md from GitHub
- [ ] T-4.1.2: TASKS.md from GitHub
- [ ] T-4.1.3: DASHBOARD-TASKS.md from GitHub
- [ ] T-4.1.4: CLAUDE-COWORK-OPERATING-SYSTEM.md
- [ ] T-4.1.5: Local files match GitHub
- [ ] T-4.1.6: Memory routing files readable
- [ ] T-4.1.7: .gitignore valid
- [ ] T-4.1.8: Git status clean
- [ ] Phase 4.1 Results: ___/8 PASS

### Phase 4.2: Dashboard
- [ ] T-4.2.1: Dashboard loads <3s
- [ ] T-4.2.2: Toggle Personal/Work mode
- [ ] T-4.2.2: Add task + persist on reload
- [ ] T-4.2.2: Mark done + move to Done log
- [ ] T-4.2.3: GitHub Gist cloud sync works
- [ ] T-4.2.4: dashboard.html file size OK
- [ ] T-4.2.5: GitHub Pages deploys <30s
- [ ] T-4.2.6: TASKS.md sync button works
- [ ] Phase 4.2 Results: ___/8 PASS

### Phase 4.3: Consistency
- [ ] T-4.3.1: File paths consistent
- [ ] T-4.3.2: OS references correct
- [ ] T-4.3.3: Task status accurate
- [ ] T-4.3.4: DASHBOARD-TASKS.md up-to-date
- [ ] T-4.3.5: No broken URLs
- [ ] Phase 4.3 Issues Found: ___

### Phase 4.4: Git Integration
- [ ] T-4.4.1: git status clean
- [ ] T-4.4.2: Commit history valid
- [ ] T-4.4.3: Local == Remote
- [ ] T-4.4.4: Branch protection documented
- [ ] T-4.4.5: GitHub Actions workflow exists
- [ ] T-4.4.6: File permissions correct
- [ ] Phase 4.4 Results: ___/6 PASS

### Phase 4.5: Scheduling
- [ ] T-4.5.1: Scheduled task exists (or Phase 3 pending)
- [ ] T-4.5.2: Wrap-up timing documented
- [ ] T-4.5.3: Task structure complete
- [ ] T-4.5.4: Fallback status noted
- [ ] Phase 4.5 Status: ___

### Phase 4.6: Memory Routing
- [ ] T-4.6.1: All 4 routing table files exist
- [ ] T-4.6.2: Memory directory structure complete
- [ ] T-4.6.3: Ohtani Matrix current
- [ ] T-4.6.4: Session log ≤7 days old
- [ ] T-4.6.5: Project files not stale
- [ ] Phase 4.6 Results: ___/5 PASS

### Phase 4.7: Real-World Workflow
- [ ] Step 1: Read system memory
- [ ] Step 2: Understand task
- [ ] Step 3: Update dashboard
- [ ] Step 4: Simulate work
- [ ] Step 5: Update task + commit
- [ ] Step 6: Update session log
- [ ] Step 7: Final verification
- [ ] Phase 4.7 Results: ___/7 PASS

### Phase 4.8: Edge Cases
- [ ] T-4.8.1: Offline behavior
- [ ] T-4.8.2: Auth token missing
- [ ] T-4.8.3: Malformed data recovery
- [ ] T-4.8.4: Race condition safe
- [ ] T-4.8.5: Rate limit handling
- [ ] T-4.8.6: Corrupted file recovery
- [ ] T-4.8.7: Cache behavior correct
- [ ] Phase 4.8 Results: ___/7 PASS

### Phase 4.9: Performance
- [ ] T-4.9.1: Cold load <3s
- [ ] T-4.9.2: Hot load <500ms
- [ ] T-4.9.3: File sizes reasonable
- [ ] T-4.9.4: GitHub API <200ms
- [ ] T-4.9.5: TASKS.md sync <5s
- [ ] T-4.9.6: Gist sync <2s
- [ ] T-4.9.7: Memory <10MB
- [ ] T-4.9.8: Concurrent ops safe
- [ ] Phase 4.9 Results: ___/8 PASS

### Phase 4.10: Security
- [ ] T-4.10.1: XSS vectors blocked
- [ ] T-4.10.2: Token not exposed
- [ ] T-4.10.3: CSRF protected
- [ ] T-4.10.4: No secrets in logs
- [ ] T-4.10.5: Input sanitization works
- [ ] T-4.10.6: Access control enforced
- [ ] T-4.10.7: Code review OK
- [ ] T-4.10.8: Supply chain secure
- [ ] T-4.10.9: File permissions correct
- [ ] T-4.10.10: Token scope minimal
- [ ] Phase 4.10 Results: ___/10 PASS (0 critical findings required)

### Final Go/No-Go
- [ ] All critical tests PASS (4.1-4.4, 4.7, 4.10)
- [ ] No critical security findings
- [ ] Performance acceptable
- [ ] Issues logged in PHASE_4_ISSUES.md
- [ ] Product Owner approval: YES / NO
- [ ] **DECISION: GO / NO-GO**

---

## Sign-Off

**Tested By:** [Claude Session ID]  
**Date:** 2026-04-19  
**Result:** PENDING EXECUTION  
**Issues Found:** 0 (baseline — will update after test)  
**Approval Status:** PENDING
```

---

## Key Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **GitHub token expired** | Auth failures during sync tests | Keep token fresh, test early in session |
| **Network latency** | Performance tests affected by ISP | Run 5+ iterations, take average |
| **Rate limits hit** | GitHub API 429 responses | Space out API calls, test rate limiting explicitly in 4.8 |
| **Stale memory files** | Routing table references wrong files | Update memory project files before Phase 4 |
| **Dashboard in flux** | Feature set changes mid-test | Lock dashboard.html before Phase 4 (tag commit) |
| **Local vs. GitHub divergence** | Tests compare different versions | Always fetch GitHub versions freshly, don't use cache |

---

## Success Metrics

**Phase 4 Complete when:**

1. ✓ Test execution log shows 10/10 phases tested
2. ✓ No critical findings (0 security, 0 startup failures)
3. ✓ Real-world workflow simulation succeeds
4. ✓ Performance metrics within bounds
5. ✓ All issues documented or resolved
6. ✓ System is production-ready

**Expected Outcome:** A bulletproof, tested Claude Cowork Operating System ready for daily use and new session bootstraps.

---

## Next Steps (Post-Phase 4)

If Go is approved:

1. **Push to GitHub** — Commit Phase 4 test results to repo
2. **Update TASKS.md** — Mark Phase 4 complete, remove from Queued
3. **Archive Phase 1-3** — Those phases now part of "Stable Foundation"
4. **Begin Phase 5** — "Ongoing Iteration" (maintenance, enhancements, scaling)

If No-Go is required:

1. **Create PHASE_4_ISSUES.md** — Document all findings
2. **Return to Phase 3** — Fix issues identified in testing
3. **Re-test Phase 4** — Once Phase 3 fixes merged
4. **Loop until Go** — Keep testing, fixing, re-testing
