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

**Session log:** At end of session, append one entry to `Productivity/memory/session-log.md` with: request, work done, key decisions. Entries are prepended (newest at top).

**Push to GitHub:** Every 1-2 hours, or when a file changes significantly.

---

## Session Wrap-Up (Automated)

**Trigger:** 5:30pm daily (scheduled task)

**Manual step:**
1. Update TASKS.md with completed task statuses
2. Append to `Productivity/memory/session-log.md`: request, work done, key decisions
3. Push to GitHub (see GitHub Write Pattern section below)

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
- Unsure which version is current → In Cowork, ask Claude: "GitHub status unclear, let me verify..." Then run `git ls-remote https://github.com/yohanloyer1-dev/Projects HEAD` to check latest commit.

---

## GitHub Write Pattern

**Authentication:** Fine-grained PAT stored on disk at `~/Projects/.github-token`.

**Token location:** `~/Projects/.github-token` — never committed (in `.gitignore`).  
**Dashboard sync:** Token also stored in browser `localStorage` as `yl_gist_token` on the dashboard page.  
**Setup date:** 2026-04-30 | Token name: **"Cowork Sandbox"** (fine-grained PAT, not classic)  
**Required permissions:** Contents: Read and write + **Gists: Read and write** (account permission — without this, dashboard Gist sync fails with 403)

**From Cowork sandbox (Claude uses this — fully autonomous):**
```bash
TOKEN=$(cat ~/Projects/.github-token)
# Push via GitHub API
CONTENT=$(base64 -w 0 /path/to/file)
SHA=$(curl -s -H "Authorization: token $TOKEN" \
  "https://api.github.com/repos/yohanloyer1-dev/Projects/contents/PATH" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")
curl -s -X PUT \
  -H "Authorization: token $TOKEN" \
  -H "Content-Type: application/json" \
  "https://api.github.com/repos/yohanloyer1-dev/Projects/contents/PATH" \
  -d "{\"message\": \"COMMIT MSG\", \"content\": \"$CONTENT\", \"sha\": \"$SHA\"}"
```

**From terminal (manual fallback):**
```bash
cd ~/Projects
git add [files]
git commit -m "Session: [description]"
git push origin main
```

**If token is lost:** Go to github.com/settings/tokens?type=beta → "Cowork Sandbox" → Regenerate. Save to `~/Projects/.github-token` and restore in dashboard localStorage: `localStorage.setItem('yl_gist_token', 'NEW_TOKEN')`. Ensure Gists: Read and write is set under Account permissions.

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
- Always read CLAUDE.md + TASKS.md + DASHBOARD-TASKS.md at startup
- Verify GitHub is up-to-date (compare with memory)
- Push every change to GitHub immediately
- Update session-log.md as work happens
- Use GitHub raw URLs if no local mount

❌ **Never Do This:**
- Write local-only (no backup = lost work)
- Assume task status (always check TASKS.md)
- Skip memory reads (context loss)
- Leave files out of sync

