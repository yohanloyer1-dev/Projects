# Yohan's Projects Repository — Navigation Guide

Welcome. This repository is your single source of truth for Claude-powered Cowork automation. All files, configs, and state live on GitHub. Local desktop folder is convenience only.

---

## Quick Navigation: Find What You Need

| I Need | File | What's in it |
|--------|------|-------------|
| **My memory/context** | `/CLAUDE.md` | WHO you are: your role, companies, projects, contacts, file system, preferences, key URLs. Updated automatically via Cowork sessions. |
| **How to operate** | `/CLAUDE-COWORK-OPERATING-SYSTEM.md` | HOW Cowork sessions work: startup protocol, memory routing, wrap-up, GitHub writes. Pasted into Cowork global instructions (one-time setup). |
| **Phase 1-4 roadmap** | `/CLAUDE-ARCHITECTURE.md` | WHY + WHAT: The four-phase vision (Foundation, File Organization, Automation, Testing) with implementation details, tasks, and success metrics. Reference document for ongoing architecture work. |
| **All my work** | `/TASKS.md` | WHAT'S NEXT: Master task list tracking Claude architecture, operations, and session management. |
| **Productivity tasks** | `/Productivity/DASHBOARD-TASKS.md` | Personal, Professional (Gorgias), and Freelance tasks. Synced with dashboard.html. |
| **Interactive task manager** | `/Productivity/dashboard.html` | Your daily driver. Personal/Work toggle, Focus mode, deadline system, XP/streaks, GitHub Gist cloud sync. |
| **Session log** | `/Productivity/memory/session-log.md` | What happened each session: requests, work done, key decisions. Append at end of every session. |
| **Dashboard changelog** | `/Productivity/memory/dashboard-changelog.md` | Every code change to dashboard.html: what, why, commit hash. Append whenever dashboard changes. |

---

## File Structure

```
/
├── CLAUDE.md                              ← Memory/context (WHO)
├── CLAUDE-COWORK-OPERATING-SYSTEM.md      ← Operating system (HOW) — paste into global instructions
├── CLAUDE-ARCHITECTURE.md                 ← Phase 1-4 roadmap (WHY + WHAT)
├── TASKS.md                               ← Master tasks (Claude + operations)
├── REPO-README.md                         ← This file (navigation)
├── README.md                              ← GitHub repo description
│
└── Productivity/
    ├── DASHBOARD-TASKS.md                 ← Personal/Work/Freelance tasks
    ├── dashboard.html                     ← Interactive task manager (live at GitHub Pages)
    ├── versions/                          ← Dashboard version history
    │   └── dashboard_v2.6_2026-03-27.html (example)
    ├── memory/
    │   ├── session-log.md                 ← Every session's work (append at end)
    │   ├── dashboard-changelog.md         ← Dashboard code changes (append every edit)
    │   └── context/
    │       ├── ohtani-matrix.md           ← Decision OS (locked goal: €50K/yr, ≤20h/week)
    │       └── adhd-dashboard-research.md ← Research for ADHD-optimized variant
    └── .gitignore (for this folder if needed)
```

---

## Typical Cowork Session Flow

**Startup (every session):**
1. Read `/CLAUDE.md` — remember who you are, your role, projects
2. Read `/TASKS.md` — understand what work exists
3. Read `/CLAUDE-COWORK-OPERATING-SYSTEM.md` (from global instructions) — how to operate
4. Read project-specific memory if applicable (e.g., Nébuleuse context in CLAUDE.md)
5. Confirm in chat: "✓ Read: CLAUDE.md, TASKS.md, DASHBOARD-TASKS.md, [project] (GitHub verified)"

**Work:**
- Check TASKS.md — what's the priority?
- Work on the task
- Update TASKS.md, session-log.md, and relevant memory files as you go

**Wrap-up (before ending session):**
1. Update `Productivity/memory/session-log.md` — append what was done, key decisions
2. Update `Productivity/memory/dashboard-changelog.md` if dashboard.html changed
3. Push to GitHub: `git add . && git commit -m "Session: [work done]" && git push origin main`
4. Confirm push in chat: "✅ Pushed to GitHub — [files changed]"

For detailed startup/wrap-up protocol, see `/CLAUDE-COWORK-OPERATING-SYSTEM.md`.

---

## Key Projects & Active Tasks

**Nébuleuse Bijoux AI Agent:** Increase automation 8.1% → 50% by April 30, 2026  
→ See: `CLAUDE.md` § Nébuleuse, `/Productivity/DASHBOARD-TASKS.md` § Nébuleuse Bijoux

**Accessory Partners CX:** Build scalable CX OS (WISMO, multi-brand, returns, CSAT)  
→ See: `CLAUDE.md` § Accessory Partners, `/Productivity/DASHBOARD-TASKS.md` § Accessory Partners

**Gorgias Agency:** Productized Gorgias services agency (name TBD)  
→ See: `/Productivity/DASHBOARD-TASKS.md` § Gorgias Agency, website on Lovable

**LinkedIn Content:** 5 pillars, 2 posts/week, #1 CX authority  
→ See: `CLAUDE.md` § LinkedIn, `/Productivity/DASHBOARD-TASKS.md` § LinkedIn Content

**Claude Architecture:** Four-phase Cowork OS buildout (Phases 1-3 complete, Phase 4 in progress)  
→ See: `/CLAUDE-ARCHITECTURE.md`, `/TASKS.md` § Claude Architecture & Operations

---

## GitHub as Source of Truth

All files live on GitHub. **Never edit local-only.**

- **GitHub repo:** https://github.com/yohanloyer1-dev/Projects
- **Dashboard live URL:** https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html (GitHub Pages, auto-deploys ~30s)
- **Raw file access:** https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md (etc.)

Every push to main triggers GitHub Pages deployment. Dashboard syncs via GitHub Gist cloud storage.

---

## Quick Links

| Resource | URL |
|----------|-----|
| GitHub repo | https://github.com/yohanloyer1-dev/Projects |
| Dashboard (live) | https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html |
| CLAUDE.md (raw) | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md |
| TASKS.md (raw) | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/TASKS.md |
| DASHBOARD-TASKS.md (raw) | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/DASHBOARD-TASKS.md |
| Operating System (raw) | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE-COWORK-OPERATING-SYSTEM.md |
| Architecture (raw) | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE-ARCHITECTURE.md |

---

## Help — I Need to...

- **Know what I'm working on today** → Open `/Productivity/dashboard.html` (syncs across all devices)
- **Check what's blocked me** → See `/Productivity/DASHBOARD-TASKS.md` § tasks with `[?]` status
- **Understand who to contact** → See `/CLAUDE.md` § Companies + Key Contacts
- **Remember how to operate** → See `/CLAUDE-COWORK-OPERATING-SYSTEM.md`
- **Check yesterday's work** → See `/Productivity/memory/session-log.md` (latest entry at top)
- **See dashboard code changes** → See `/Productivity/memory/dashboard-changelog.md` (latest at top)

---

## Questions?

All files are markdown. They're meant to be read and understood. If something is unclear or needs updating, it's a sign the docs need clarification — update them.

**This repo is evolving.** Phases 1-3 complete (Foundation, File Organization, Automation). Phase 4 (Testing & Verification) is now in progress. See `/CLAUDE-ARCHITECTURE.md` for the full roadmap.
