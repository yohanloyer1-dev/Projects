# Master Tasks List

<!-- Status: [!] Urgent | [>] Important | [~] In Progress | [?] Waiting/Blocked | [_] Someday | [ ] Normal | [x] Done -->

## 🤖 Claude Architecture & Operations

### Cowork System Architecture
- [~] **Phase 1: Foundation (GitHub Single Source of Truth)** — Complete. GitHub is locked as authoritative source. Local mount is convenience only.
  - [x] Move CLAUDE.md to root
  - [x] Create CLAUDE-COWORK-OPERATING-SYSTEM.md
  - [x] Verify dashboard deployed to GitHub Pages
  - [x] Reconcile and push renamed audit files
- [ ] **Phase 2: File Organization & Clarity** — IN PROGRESS
  - [ ] Split TASKS.md: root (master) vs Productivity/DASHBOARD-TASKS.md (dashboard-specific)
  - [ ] Create CLAUDE-ARCHITECTURE.md with Phase 1-4 roadmap
  - [ ] Clean CLAUDE.md: remove duplicate protocol sections
  - [ ] Create REPO-README.md navigation guide
- [ ] **Phase 3: Automation & Process** — Queued
  - [ ] Paste CLAUDE-COWORK-OPERATING-SYSTEM.md into Cowork global instructions (one-time setup)
  - [ ] Setup 5:30pm scheduled task: session wrap-up with auto-template
  - [ ] Implement automatic CLAUDE.md update proposal system
- [ ] **Phase 4: Testing & Verification** — Queued
  - [ ] Test complete startup protocol in new Cowork session
  - [ ] Verify GitHub Pages dashboard is live and synced
  - [ ] Document any issues and iterate

### Ongoing File Management
- [_] **Push Nébuleuse project files to GitHub** — Deferred until Phase 2 complete. Untracked files: 528+ files (AI Agent data, One Pilot guidance, financial models, etc.)
- [ ] **Add N8N/ai_agents_az/ to .gitignore** — Run: `echo "N8N/ai_agents_az/" >> /Users/yohanloyer/Projects/.gitignore && git add .gitignore && git commit -m "Add N8N/ai_agents_az to gitignore" && git push origin main`

---

## Reference: Productivity Dashboard Tasks

**See:** `/Productivity/DASHBOARD-TASKS.md` for Personal, Professional (Gorgias), and Freelance task lists.

This master file tracks Claude-specific architecture, operations, and session management. Productivity dashboard tasks are maintained separately to keep concerns clearly separated.
