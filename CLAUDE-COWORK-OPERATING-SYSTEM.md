# Claude Cowork Operating System
**Version:** 1.0  
**Source of Truth:** GitHub (yohanloyer1-dev/Projects)  
**Status:** Live

---

## What This Is
GitHub is the source of truth. Every session: read memory → work → push changes.

---

## Session Startup (5 minutes)

**Every session, in order:**

1. **Read CLAUDE.md** (project memory)
   - Local: `/sessions/.../mnt/Projects/CLAUDE.md`
   - GitHub fallback: `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md`

2. **Read TASKS.md** (master task list)
   - Local: `/sessions/.../mnt/Projects/TASKS.md`
   - GitHub fallback: `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/TASKS.md`

2b. **Read DASHBOARD-TASKS.md** (dashboard-specific: Personal, Professional, Freelance)
   - Local: `/sessions/.../mnt/Projects/Productivity/DASHBOARD-TASKS.md`
   - GitHub fallback: `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/DASHBOARD-TASKS.md`

3. **Read project-specific memory** (if applicable — see Routing Table below)

4. **Confirm in chat:** `✓ Read: CLAUDE.md, TASKS.md, [project if relevant] (GitHub verified)`

5. **Check alignment:** Scan Ohtani Matrix (`Productivity/memory/context/ohtani-matrix.md`) — does this task fit constraints?

**Never assume task status. Always read TASKS.md first.**

---

## Memory Routing Table

| If you're working on... | Read this file |
|-------------------------|---|
| Nébuleuse AI Agent | `Productivity/memory/projects/nebuleuse-bijoux.md` |
| Accessory Partners | `Productivity/memory/projects/accessory-partners.md` |
| Gorgias Help Center | `Productivity/memory/projects/gorgias-agency.md` |
| LinkedIn content | `Productivity/memory/projects/linkedin-content-system.md` |
| n8n / automation | `Productivity/memory/projects/n8n-automation.md` |
| Dashboard / productivity | Read "Dashboard System" section in CLAUDE.md |
| New/unlisted project | Read CLAUDE.md "Key Projects" section — find the relevant memory file |
| Personal / health / travel | No project memory needed |

---

## During Session — Update Rules

**TASKS.md:** Update immediately when status changes. Don't batch to the end.

**Project memory:** Update when new context is shared (add to relevant `Productivity/memory/projects/*.md`).

**Session log:** Append to `Productivity/memory/session-log.md` as significant work completes (not required every 5 minutes, log major milestones).

**Push to GitHub:** Every 1-2 hours, or when a file changes significantly.

---

## Session Wrap-Up (Automated)

**Trigger:** 5:30pm daily (scheduled task)

**Manual step (complete once):**
1. Complete the session wrap-up task in dashboard
2. Template auto-fills: what was requested, what was done, key decisions, pending items
3. Click "Push to GitHub" button (if available) or manual push

**Files to update before closing:**
- `/TASKS.md` (root) — update master task list status
- `Productivity/DASHBOARD-TASKS.md` — update dashboard-specific tasks if changed
- `Productivity/memory/session-log.md` — append session entry
- Any project files you edited

**Confirmation in chat:**
```
✅ Pushed to GitHub
- TASKS.md — [what changed]
- Productivity/memory/session-log.md — session documented
```

---

## If Files Conflict

- Local version ≠ GitHub version → GitHub wins. Always.
- TASKS.md shows old status → Refresh from GitHub before starting work.
- Unsure which version is current → Ask in chat: "GitHub status unclear, fetching..."

---

## GitHub Write Pattern

**Authentication:** HTTPS + osxkeychain (macOS credential manager)

Verified setup (run once per device):
```bash
git config --global credential.helper osxkeychain
```

**For pushes:** Use standard git commands. Credentials are cached automatically by osxkeychain after first authentication.

```bash
cd /Users/yohanloyer/Projects
git add [files]
git commit -m "Session: [description]"
git push origin main
```

**First push on a device:** Git will prompt for GitHub credentials once. osxkeychain saves them for future use.

**Verify setup:**
```bash
git config credential.helper  # Should return "osxkeychain"
git ls-remote https://github.com/yohanloyer1-dev/Projects HEAD  # Should return commit SHA (no auth prompt)
```

**Never write local-only.** Everything goes to GitHub.

---

## Key URLs

| What | URL |
|------|-----|
| **Operating System (this doc)** | https://github.com/yohanloyer1-dev/Projects/blob/main/CLAUDE-COWORK-OPERATING-SYSTEM.md |
| **Live Dashboard** | https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html |
| **CLAUDE.md** | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md |
| **TASKS.md (master)** | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/TASKS.md |
| **DASHBOARD-TASKS.md** | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/DASHBOARD-TASKS.md |
| **Repo** | https://github.com/yohanloyer1-dev/Projects |

---

## Troubleshooting

**"Mount not available"**  
Use GitHub raw URLs above. Git commands work on remote URLs directly.

**"Authentication failed on first push"**  
GitHub will prompt for credentials on first HTTPS push. Enter your GitHub username + personal access token (or use SSO). osxkeychain saves credentials automatically.

**"TASKS.md out of sync"**  
Refresh from GitHub: `git pull origin main` before reading files locally.

**"File push failed"**  
Verify remote is configured: `git remote -v` (should show https://github.com/yohanloyer1-dev/Projects.git). Check credentials with `git ls-remote https://github.com/yohanloyer1-dev/Projects HEAD`.

**"New device / lost laptop"**  
Clone: `git clone https://github.com/yohanloyer1-dev/Projects.git ~/Projects`  
Mount in Cowork, resume work. Everything is on GitHub.

---

## Rules

✅ **Do This:**
- Always read CLAUDE.md + TASKS.md at startup
- Verify GitHub is up-to-date (compare with memory)
- Push every change to GitHub immediately
- Update session-log.md as work happens
- Use GitHub raw URLs if no local mount

❌ **Never Do This:**
- Write local-only (no backup = lost work)
- Assume task status (always check TASKS.md)
- Skip memory reads (context loss)
- Leave files out of sync

