#!/bin/bash
# Session wrap-up push — 2026-04-24
# Run this from Terminal to push today's wrap-up changes to GitHub
# Files updated: nebuleuse-bijoux.md, DASHBOARD-TASKS.md, session-log.md

cd ~/Projects

# Remove stale git lock if present
[ -f .git/index.lock ] && rm .git/index.lock && echo "Removed stale lock"

# Pull first to include any remote-only commits (like the 3 pending from Apr 21-22)
git pull origin main --no-rebase 2>&1

# Stage the 3 updated files
git add Productivity/memory/projects/nebuleuse-bijoux.md
git add Productivity/DASHBOARD-TASKS.md
git add Productivity/memory/session-log.md

# Commit and push
git commit -m "Session: 2026-04-24 wrap-up sync"
git push origin main

echo ""
echo "✅ Done. GitHub is up to date."
