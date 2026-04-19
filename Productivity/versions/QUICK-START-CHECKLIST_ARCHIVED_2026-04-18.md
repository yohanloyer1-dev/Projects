# Cowork Session Quick Start Checklist
**Print this. Paste into every new Cowork session.**

---

## 🚀 Session Startup (5 minutes)

### 1. Read Memory Files (In Order)
```
✓ Productivity/CLAUDE.md
  Local: /sessions/.../mnt/Projects/Productivity/CLAUDE.md
  Fallback: https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/CLAUDE.md

✓ Productivity/TASKS.md
  Local or GitHub: https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/TASKS.md

✓ Project-Specific Memory (if applicable)
  Nébuleuse? → memory/projects/nebuleuse-bijoux.md
  Accessory Partners? → memory/projects/accessory-partners.md
  Gorgias? → memory/projects/gorgias-agency.md
  LinkedIn? → memory/projects/linkedin-content-system.md
  n8n? → memory/projects/n8n-automation.md
```

### 2. Verify Startup
Copy/paste this into chat:
```
✓ Read: CLAUDE.md, TASKS.md, [PROJECT if relevant] (GitHub verified)
```

### 3. Check Alignment
- Scan `Productivity/memory/context/ohtani-matrix.md` — does this task align?
- Scan `Productivity/memory/session-log.md` — understand recent context

### 4. You're Ready
Start work! Update TASKS.md as you go.

---

## 🔧 During Work

| Action | When | How |
|--------|------|-----|
| Update TASKS.md | Task status changes | Edit file → push immediately via GitHub API |
| Append to session-log.md | Major work completes | Add bullet to "Done" section |
| Push to GitHub | Every 30-60 min | `curl -X PUT` via GitHub API (see global instructions) |
| Use TodoWrite | Multi-step tasks | Good for progress visibility |

---

## 📦 Session Wrap-Up (10 minutes)

### 1. Update Task Status
- Mark completed tasks in TASKS.md with `[x]`
- Update in-progress status with `[~]`

### 2. Update Session Log
```markdown
## 2026-MM-DD | [topic] | [session type]

### Requested
- [what Yohan asked]

### Done
- [what was completed]

### Key Decisions
- [important choices]

### Pending
- [anything blocked]
```

### 3. Push to GitHub
```bash
TOKEN=$(cat /sessions/.../mnt/OPS/.github_token)
# Push these files via GitHub API:
# - Productivity/TASKS.md
# - Productivity/memory/session-log.md
# - Any project files you edited
```

### 4. Confirm in Chat
```
✅ Pushed to GitHub
- Productivity/TASKS.md — [what changed]
- Productivity/memory/session-log.md — session documented
- Live: https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html
```

---

## 🔑 Key URLs (Bookmark These)

| What | URL |
|------|-----|
| **Live Dashboard** | https://yohanloyer1-dev.github.io/Projects/Productivity/dashboard.html |
| **Repo** | https://github.com/yohanloyer1-dev/Projects |
| **CLAUDE.md (GitHub)** | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/CLAUDE.md |
| **TASKS.md (GitHub)** | https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main/Productivity/TASKS.md |

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| **Mount not available** | Use GitHub raw URLs (see above) |
| **GitHub token missing** | Check `/sessions/.../mnt/OPS/.github_token` or ask Yohan |
| **TASKS.md out of sync** | Read from GitHub, compare, update via API |
| **File push failed** | Verify SHA via `curl`, try again with latest SHA |
| **New device / lost laptop** | Clone repo: `git clone https://github.com/yohanloyer1-dev/Projects.git ~/Projects` |

---

## ❌ Never Do This

- ❌ Skip reading CLAUDE.md + TASKS.md
- ❌ Assume task status without checking TASKS.md
- ❌ Write local-only (always push to GitHub)
- ❌ Forget to update session-log.md
- ❌ Leave files out of sync
- ❌ Fabricate memory — read the files

---

## ✅ Golden Rules

1. **GitHub is the source of truth** — desktop is optional
2. **Always verify files from GitHub** — local copy might be stale
3. **Push every change** — don't batch to the end
4. **Update TASKS.md as you go** — not at session end
5. **Log your work** — session-log.md is the audit trail

---

**TL;DR:** Read CLAUDE.md → Read TASKS.md → Do work → Update TASKS.md → Push to GitHub → Confirm in chat

For full details, see: `Productivity/YL-OPS-COWORK-GLOBAL-INSTRUCTIONS.md`
