#!/bin/bash
# Session wrap-up push — 2026-04-26
# Run this from Terminal to push all pending changes to GitHub
# Files updated: nebuleuse-bijoux.md, DASHBOARD-TASKS.md, session-log.md
# Covers: Apr 24 session changes + Apr 26 automated wrap-up

cd ~/Projects

# Remove stale git lock if present
[ -f .git/index.lock ] && rm .git/index.lock && echo "Removed stale lock"

# Pull first to sync remote state
git pull origin main --no-rebase 2>&1

# Stage all pending files
git add Productivity/memory/projects/nebuleuse-bijoux.md
git add Productivity/DASHBOARD-TASKS.md
git add Productivity/memory/session-log.md

# Commit and push
git commit -m "Session: 2026-04-24 + 2026-04-26 wrap-up sync"
git push origin main

echo ""
echo "✅ Done. GitHub is up to date."
