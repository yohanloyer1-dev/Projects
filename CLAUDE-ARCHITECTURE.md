# Claude Architecture: Cowork Operating System (Phase 1-4)

**Status:** Phase 1 Complete | Phase 2 Complete | Phase 3 Ready to Start | Phase 4 Queued  
**Last Updated:** 2026-04-19  
**Owner:** Yohan Loyer (yohanloyer1@gmail.com)

---

## Overview

This document defines the four-phase architecture for Claude-powered Cowork automation, transforming manual task management into a systematic, repeatable operating system that enables asynchronous collaboration between human and AI.

### Core Principle
**GitHub as single source of truth** — all files, configs, and state live on GitHub. Local desktop folder is convenience only. This prevents sync issues, enables easy context-switching between Cowork sessions, and allows Claude to operate from any session without losing state.

### Key Constraints
- **Token efficiency:** Global instructions must be ≤600 words (down from 6,000+)
- **No manual overhead:** No copy/pasting instructions into every new session
- **Clarity first:** Every file has a single responsibility
- **Testable:** Each phase can be verified independently

---

## Phase 1: Foundation (GitHub Single Source of Truth)

### Status: ✅ COMPLETE

### What We Did
1. **Moved CLAUDE.md to root** — Single authoritative memory/context file
   - Removed: "Quick Startup Checklist", "GitHub Write Protocol" (duplicates)
   - Kept: Me, Role, Companies, Projects, File System, Dashboard, Voice Notes, Preferences, Terms, Key URLs
   - Location: `/CLAUDE.md` (root)

2. **Created CLAUDE-COWORK-OPERATING-SYSTEM.md** — Canonical operating system
   - Purpose: How to operate in Cowork sessions (startup, memory routing, wrap-up, GitHub writes)
   - Word count: ~591 words (fits ≤600 constraint)
   - Location: `/CLAUDE-COWORK-OPERATING-SYSTEM.md` (root)
   - Scope: For pasting into Cowork global instructions (one-time setup)

3. **Verified GitHub Pages deployment** — Dashboard is live
   - Dashboard live URL: https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html
   - Auto-deploys ~30 seconds after push
   - Verified: MD5 hash matches, file synced, GitHub Pages working

4. **Reconciled and pushed audit files** — Renamed for clarity
   - `AUDIT-SUMMARY.md` → `COWORK-AUDIT-SUMMARY-2026-04-15.md` (what, when)
   - `AUDIT_SUMMARY.md` → `DASHBOARD-CODE-AUDIT-2026-04-07.md` (what, when)
   - Archived old versions in `Productivity/versions/` (not deleted, for recovery)
   - Committed: d78978d1, 87808d1, 6953ec2, 48b4620 (archive files)
   - Committed: 2c43bc4 (moved CLAUDE.md to root)
   - Committed: f4c9890 (simplified CLAUDE.md, point to Operating System)

### Deliverables
| File | Purpose | Location |
|------|---------|----------|
| CLAUDE.md | Memory/context (WHO you are, your role, projects) | /CLAUDE.md (root) |
| CLAUDE-COWORK-OPERATING-SYSTEM.md | How to operate (startup, memory routing, wrap-up, GitHub) | /CLAUDE-COWORK-OPERATING-SYSTEM.md (root) |
| dashboard.html | Interactive task/goal manager | /Productivity/dashboard.html |
| TASKS.md | Master task list (Claude architecture + operations) | /TASKS.md (root) |
| DASHBOARD-TASKS.md | Dashboard tasks (Personal, Professional, Freelance) | /Productivity/DASHBOARD-TASKS.md |

### How to Verify
```bash
cd ~/Projects
git log --oneline | head -10
# Should show recent commits with "Move CLAUDE.md to root", archive commits, etc.

cat CLAUDE.md | head -20
# Should show "# Memory" and "## Me"

cat CLAUDE-COWORK-OPERATING-SYSTEM.md | wc -w
# Should show ~591 words
```

---

## Phase 2: File Organization & Clarity

### Status: ✅ COMPLETE

### What We Did

#### Task 2.1: Split TASKS.md ✅ COMPLETE
- **What:** Separate master task list from dashboard-specific tasks
- **Rationale:** Master list tracks ALL work (Claude architecture, operations, external commitments). Dashboard tracks only personal/work/freelance (what shows in productivity dashboard).
- **Implementation:**
  - Root `/TASKS.md` — Master file (Claude Architecture & Operations section)
  - `/Productivity/DASHBOARD-TASKS.md` — Dashboard file (Personal, Professional, Freelance)
  - Both maintained in sync via Git
- **Commit:** d6d4f2f (2026-04-19)
- **Verification:** Both files on GitHub, no encoding issues, clear section headers

#### Task 2.2: Create CLAUDE-ARCHITECTURE.md (THIS FILE) ✅ COMPLETE
- **What:** Document Phase 1-4 roadmap with implementation details
- **Purpose:** Reference guide for ongoing architecture work, testing, and iteration
- **Contents:** Overview + 4 phases with status, tasks, deliverables
- **Location:** `/CLAUDE-ARCHITECTURE.md` (root)
- **Word count:** 1,834 words (target was 2,000-3,000; content is complete and comprehensive)
- **Commit:** ef74a7e (2026-04-19)

#### Task 2.3: Clean CLAUDE.md ✅ COMPLETE
- **What:** Remove "Quick Startup Checklist" and "GitHub Write Protocol" sections (already in CLAUDE-COWORK-OPERATING-SYSTEM.md)
- **Why:** Single responsibility — CLAUDE.md is memory/context, not protocol
- **Removed:** ~50 lines total (Quick Startup Checklist + GitHub Write Protocol)
- **Result:** CLAUDE.md reduced from ~12,100 bytes to ~11,000 bytes
- **Commit:** 2d3e679 (2026-04-19)

#### Task 2.4: Create REPO-README.md ✅ COMPLETE
- **What:** Navigation guide explaining purpose of each core file
- **Purpose:** Onboard Claude quickly: "what file do I read for X?"
- **Contents:**
  - Quick navigation table (file → purpose lookup)
  - File structure diagram
  - Typical Cowork session flow
  - Key projects overview
  - GitHub as source of truth section
  - Quick links
  - Help/troubleshooting section
- **Location:** `/REPO-README.md` (root)
- **Commit:** 2d3e679 (2026-04-19)

### Completion Criteria
- [x] All 4 tasks complete
- [x] No encoding issues in any markdown files
- [x] GitHub Pages dashboard still live
- [x] All files have clear headers and single responsibility
- [x] Root directory has ≤8 markdown files (6 files: CLAUDE.md, CLAUDE-COWORK-OPERATING-SYSTEM.md, CLAUDE-ARCHITECTURE.md, REPO-README.md, TASKS.md, README.md)

---

## Phase 3: Automation & Process

### Status: ⏳ READY TO START (Phase 2 Complete)

### Task 3.1: Paste CLAUDE-COWORK-OPERATING-SYSTEM.md into Cowork Global Instructions
- **What:** One-time setup in Cowork platform settings
- **Purpose:** Make operating system available to every session automatically
- **Steps:**
  1. Open Cowork → Settings → Global Instructions
  2. Paste entire content of `CLAUDE-COWORK-OPERATING-SYSTEM.md`
  3. Save
  4. Test in next new Cowork session: verify Claude reads it at startup
- **Verification:** Start new session, confirm Claude mentions reading global instructions

### Task 3.2: Setup 5:30pm Scheduled Task (Session Wrap-Up)
- **What:** Automated daily task at 5:30pm (end of business)
- **Purpose:** Remind Claude to sync TASKS.md and propose CLAUDE.md updates
- **Implementation:**
  ```bash
  # Scheduled task details
  Trigger: Daily at 5:30pm (user's local time)
  Template:
  - Check TASKS.md: what changed today?
  - Check CLAUDE.md: any context changes needed?
  - Draft update proposal to user
  - Wait for user approval before pushing to GitHub
  ```
- **Integration point:** Links to Task 3.3 (automatic update proposals)
- **Verification:** Scheduled task appears in `/Users/yohanloyer/Documents/Claude/Scheduled/` and runs daily

### Task 3.3: Implement Automatic CLAUDE.md Update Proposal System
- **What:** At end of session, Claude proposes CLAUDE.md updates based on what we worked on
- **Purpose:** Keep memory fresh without manual overhead; user reviews/approves
- **Workflow:**
  1. Session ends or wrap-up task triggers
  2. Claude reviews work: "What new context should I remember?"
  3. Claude drafts proposal: "I suggest adding X to [section] because [reason]"
  4. User approves/modifies in chat
  5. Claude updates CLAUDE.md and pushes to GitHub
  6. Next session reads updated CLAUDE.md
- **Integration:** Task 3.2 (scheduled task) calls this
- **Verification:** Next session shows updated CLAUDE.md in context

---

## Phase 4: Testing & Verification

### Status: ⏳ QUEUED (Starts after Phase 3)

### Task 4.1: Test Complete Startup Protocol in New Cowork Session
- **What:** Spin up fresh Cowork session and run full 5-step startup
- **Steps:**
  1. Read CLAUDE.md (context about Yohan, projects, roles)
  2. Read TASKS.md (what work exists)
  3. Read CLAUDE-COWORK-OPERATING-SYSTEM.md (how to operate) — should be in global instructions by Phase 3
  4. Read project-specific memory (if applicable)
  5. Confirm in chat: "✓ Read: CLAUDE.md, TASKS.md, [project] (GitHub verified)"
- **Expected outcome:** Claude has full context, no confusion about who/what/why
- **Verification:** Session transcript shows all 5 steps completed; no missing context errors

### Task 4.2: Verify GitHub Pages Dashboard is Live and Synced
- **What:** End-to-end dashboard verification
- **Steps:**
  1. Open https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html
  2. Check: Features work (toggle Personal/Work, add task, mark done)
  3. Check: GitHub Gist sync works (save progress, reload, data persists)
  4. Check: File timestamps match latest commit
- **Verification:** Dashboard fully functional, synced with GitHub
- **Measurement:** Load time <2s, no console errors, all UI elements responsive

### Task 4.3: Document Issues and Iterate
- **What:** Collect feedback from Phase 4 testing
- **Iterate on:**
  - Any missing context in CLAUDE.md?
  - Any confusing sections in CLAUDE-COWORK-OPERATING-SYSTEM.md?
  - Any missing navigation info in REPO-README.md?
  - Any performance issues with dashboard?
- **Output:** GitHub issue or CLAUDE.md update + new session to fix
- **Completion:** Zero critical issues, all "nice-to-haves" documented in backlog

---

## File Dependency Map

```
CLAUDE.md (root)
├── Memory/context for Claude
├── Updated by: Automatic update system (Phase 3.3)
├── Read by: Every session (startup step 1)
└── Depends on: Nothing

CLAUDE-COWORK-OPERATING-SYSTEM.md (root)
├── Operating system for Cowork sessions
├── Word count: ~591 (≤600 constraint)
├── Updated by: Manual (rarely)
├── Read by: Every session (in global instructions, Phase 3.1)
└── Depends on: CLAUDE.md (references memory routing)

CLAUDE-ARCHITECTURE.md (root) ← YOU ARE HERE
├── Phase 1-4 roadmap
├── Updated by: Manual at end of each phase
├── Read by: Onboarding, reference during work
└── Depends on: Everything (overview document)

TASKS.md (root)
├── Master task list (Claude architecture + operations)
├── Updated by: Manual, session wrap-up system (Phase 3.2)
├── Read by: Every session (startup step 2)
└── Depends on: DASHBOARD-TASKS.md (links to it)

DASHBOARD-TASKS.md (Productivity/)
├── Dashboard-specific tasks (Personal, Professional, Freelance)
├── Updated by: Dashboard UI + manual
├── Read by: Productivity sessions
└── Depends on: TASKS.md (referenced from master)

REPO-README.md (root)
├── Navigation guide (which file for what?)
├── Updated by: Manual
├── Read by: New Cowork sessions, reference
└── Depends on: All above (explains all)

dashboard.html (Productivity/)
├── Interactive task manager
├── Updated by: Git when code changes
├── Read by: User in browser
└── Depends on: GitHub Gist (cloud sync), localStorage
```

---

## Success Metrics

### Phase 1: Foundation
- [x] GitHub is authoritative source (not local desktop)
- [x] CLAUDE.md at root, <12KB, readable
- [x] CLAUDE-COWORK-OPERATING-SYSTEM.md exists, ≤600 words
- [x] Dashboard deployed to GitHub Pages
- [x] Audit files renamed with dates, old versions archived

### Phase 2: Clarity
- [x] TASKS.md split: root (master) + Productivity/ (dashboard)
- [x] CLAUDE-ARCHITECTURE.md documents Phase 1-4
- [x] CLAUDE.md cleaned: no duplicate protocol sections
- [x] REPO-README.md explains file navigation
- [x] Zero encoding issues in any .md file

### Phase 3: Automation
- [ ] CLAUDE-COWORK-OPERATING-SYSTEM.md in Cowork global instructions
- [ ] 5:30pm wrap-up task runs daily
- [ ] Automatic CLAUDE.md update proposals work
- [ ] Next session reads updated CLAUDE.md without issues

### Phase 4: Testing
- [ ] New session startup protocol: all 5 steps pass
- [ ] Dashboard live, synced, fully functional
- [ ] Zero critical issues in Phase 4 testing
- [ ] All "nice-to-haves" documented for future

---

## Next Steps (Immediate)

Phase 2 is complete. All deliverables on GitHub.

**Phase 3 Ready to Start:**

1. **Phase 3.1:** Paste CLAUDE-COWORK-OPERATING-SYSTEM.md into Cowork global instructions (one-time setup)
2. **Phase 3.2:** Setup 5:30pm scheduled task for session wrap-up
3. **Phase 3.3:** Implement automatic CLAUDE.md update proposal system
4. **Commit:** Update CLAUDE-ARCHITECTURE.md to mark Phase 2 complete and Phase 3 ready
5. **Then Phase 4:** Testing and verification (after Phase 3 automation is live)

---

## References

- **Operating System:** See `/CLAUDE-COWORK-OPERATING-SYSTEM.md`
- **Master Tasks:** See `/TASKS.md`
- **Dashboard Tasks:** See `/Productivity/DASHBOARD-TASKS.md`
- **Memory/Context:** See `/CLAUDE.md`
- **Dashboard Code:** See `/Productivity/dashboard.html`
- **GitHub Repo:** https://github.com/yohanloyer1-dev/Projects

---

## Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-04-19 | 1.1 | Mark Phase 2 complete; update success metrics and next steps | Claude |
| 2026-04-19 | 1.0 | Initial Phase 1-4 architecture document | Claude |

