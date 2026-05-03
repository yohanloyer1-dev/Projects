# Claude Cowork Operating System
**Version:** 1.1
**Source of Truth:** GitHub (yohanloyer1-dev/Projects)
**Status:** Live

---

## What This Is
GitHub is the source of truth. Every session: read memory → work → push changes.

---

## Session Startup

**Every session, in order:**

1. **Read CLAUDE.md** (project memory)
   - GitHub (source of truth): `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md`
   - Local (if available): `/sessions/.../mnt/Projects/CLAUDE.md`

2. **Read TASKS.md** (master task list)
   - GitHub (source of truth): `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/TASKS.md`
   - Local (if available): `/sessions/.../mnt/Projects/TASKS.md`

2b. **Read DASHBOARD-TASKS.md** (dashboard-specific: Personal, Professional, Freelance)
   - GitHub (source of truth): `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/DASHBOARD-TASKS.md`
   - Local (if available): `/sessions/.../mnt/Projects/Productivity/DASHBOARD-TASKS.md`

3. **Read project-specific memory** (if applicable — see Routing Table below)

4. **Confirm in chat:** `✓ Read: CLAUDE.md, TASKS.md, DASHBOARD-TASKS.md, [project if relevant] (GitHub verified)` — and session log if context-switching

5. **Check alignment:** Scan Ohtani Matrix (`Productivity/memory/context/ohtani-matrix.md`) — does this task fit constraints?

6. **Optional: Review session context** (if context-switching or returning to ongoing work)
   - Read last entry in `Productivity/memory/session-log.md` to understand previous session's work
   - Not required for new tasks or fresh starts

**Critical rule: Never assume task status. Always read TASKS.md first.**

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

**Session log:** At end of session, append one entry to `Productivity/memory/session-log.md` with: request, work done, key decisions. Entries are prepended (newest at top).

**Push to GitHub:** Every 1-2 hours, or when a file changes significantly.

---

## Session Wrap-Up (Automated at 5:30pm daily)

**Manual steps:**
1. Update TASKS.md with completed task statuses
2. Append to `Productivity/memory/session-log.md`: request, work done, key decisions
3. Push to GitHub

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
- TASKS.md shows old status → Refresh from GitHub: `git pull origin main` before reading locally.
- Unsure which version is current → Run `git ls-remote https://github.com/yohanloyer1-dev/Projects HEAD` to check latest commit.

---

## GitHub Write Pattern

**Authentication:** HTTPS + credential manager (macOS/Linux/Windows)

**macOS (verified setup):**
```bash
git config --global credential.helper osxkeychain
```

**Commands:**
```bash
cd /Users/yohanloyer/Projects
git add [files]
git commit -m "Session: [description]"
git push origin main
```

**First push on a device:** Git will prompt for GitHub credentials once. osxkeychain saves them for future use.

**Verify setup:**
```bash
git config credential.helper        # → osxkeychain
git ls-remote https://github.com/yohanloyer1-dev/Projects HEAD  # → commit SHA, no auth prompt
```

**PAT (for autonomous push without terminal):** Token "Cowork Sandbox" (fine-grained PAT) stored at `~/Projects/.github-token`. Required permissions: Contents: Read and write + Gists: Read and write. Token also stored in browser localStorage as `yl_gist_token` for dashboard Gist sync. If lost: regenerate at `github.com/settings/tokens?type=beta` → "Cowork Sandbox".

**Critical rule: Never write local-only. Everything goes to GitHub.**

---

## Key URLs

| What | URL |
|------|-----|
| **Operating System (this doc)** | `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE-COWORK-OPERATING-SYSTEM.md` |
| **CLAUDE.md** | `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/CLAUDE.md` |
| **TASKS.md (master)** | `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/TASKS.md` |
| **DASHBOARD-TASKS.md** | `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/DASHBOARD-TASKS.md` |
| **Live Dashboard** | `https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html` |
| **Repo** | `https://github.com/yohanloyer1-dev/Projects` |

---

## Troubleshooting

**"Mount not available"**
Use GitHub raw URLs above. Git commands work on remote URLs directly.

**"Authentication failed on first push"**
GitHub will prompt for credentials on first HTTPS push. Enter your GitHub username + personal access token. Credential manager saves credentials automatically.

**"TASKS.md out of sync"**
Refresh from GitHub: `git pull origin main` before reading files locally.

**"File push failed"**
Verify remote: `git remote -v` (should show `https://github.com/yohanloyer1-dev/Projects.git`).
Check credentials: `git ls-remote https://github.com/yohanloyer1-dev/Projects HEAD`.

**"New device / lost laptop"**
Clone: `git clone https://github.com/yohanloyer1-dev/Projects.git ~/Projects`
Mount in Cowork, resume work. Everything is on GitHub.

---

## Rules

✅ **Do This:**
- Always read CLAUDE.md + TASKS.md + DASHBOARD-TASKS.md at startup
- Verify GitHub is up-to-date (compare with memory)
- Push every change to GitHub immediately
- Update session-log.md as work happens
- Use GitHub raw URLs if no local mount
- **Present plan/options first, wait for approval before implementing** — especially for multi-step or ambiguous tasks. State the approach in 2-3 sentences and confirm before starting work.

❌ **Never Do This:**
- Write local-only (no backup = lost work)
- Assume task status (always check TASKS.md)
- Skip memory reads (context loss)
- Leave files out of sync
- **Suggest or build new dashboard features without first asking: does this help execute on Nébuleuse, Accessory Partners, or the agency — or is it just productivity theater?** The dashboard is a means, not an end.
