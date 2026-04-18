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
   - Local: `/sessions/.../mnt/Projects/Productivity/CLAUDE.md`
   - GitHub fallback: `https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/CLAUDE.md`

2. **Read TASKS.md** (current task list)
   - Same paths as above (TASKS.md)

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
| Personal / health / travel | No project memory needed |

---

## During Session

**Update TASKS.md immediately** when task status changes. Don't batch to the end.

**Append to `Productivity/memory/session-log.md`** as significant work completes (not required every 5 minutes, but log major milestones).

**Push to GitHub** every 1-2 hours or when a file changes.

---

## Session Wrap-Up (Automated)

**Trigger:** 5:30pm daily (scheduled task)

**Manual step (complete once):**
1. Complete the session wrap-up task in dashboard
2. Template auto-fills: what was requested, what was done, key decisions, pending items
3. Click "Push to GitHub" button (if available) or manual push

**Files to update before closing:**
- `Productivity/TASKS.md` — mark tasks [x] if complete
- `Productivity/memory/session-log.md` — append session entry
- Any project files you edited

**Confirmation in chat:**
```
✅ Pushed to GitHub
- Productivity/TASKS.md — [what changed]
- Productivity/memory/session-log.md — session documented
```

---

## GitHub Write Pattern

1. **Get current SHA** (prevents race conditions)
   ```bash
   TOKEN=$(cat /sessions/.../mnt/OPS/.github_token)
   REPO="yohanloyer1-dev/Projects"
   SHA=$(curl -s -H "Authorization: token $TOKEN" \
     "https://api.github.com/repos/$REPO/contents/Productivity/TASKS.md" | jq -r '.sha')
   ```

2. **Base64 encode content** and PUT to GitHub
   ```bash
   CONTENT=$(base64 -i /path/to/file)
   curl -X PUT -H "Authorization: token $TOKEN" \
     -d "{\"message\":\"Update TASKS.md\",\"content\":\"$CONTENT\",\"sha\":\"$SHA\"}" \
     https://api.github.com/repos/$REPO/contents/Productivity/TASKS.md
   ```

**Never write local-only.** Everything goes to GitHub.

---

## Key URLs

| What | URL |
|------|-----|
| **Operating System (this doc)** | https://github.com/yohanloyer1-dev/Projects/blob/main/CLAUDE-COWORK-OPERATING-SYSTEM.md |
| **Live Dashboard** | https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html |
| **CLAUDE.md** | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/CLAUDE.md |
| **TASKS.md** | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/TASKS.md |
| **Repo** | https://github.com/yohanloyer1-dev/Projects |

---

## Troubleshooting

**"Mount not available"**  
Use GitHub raw URLs above. You can still read + write via API.

**"GitHub token missing"**  
Check: `/sessions/.../mnt/OPS/.github_token` — ask Yohan if not found.

**"TASKS.md out of sync"**  
Read from GitHub, compare with dashboard, update via API to match.

**"File push failed"**  
Verify SHA via curl, try again with latest SHA. Check token is valid.

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

---

## Next: Phase 2-4 Architecture

See: `Productivity/TASKS.md` → "Claude Architecture" section for Phase 2-4 builds.
