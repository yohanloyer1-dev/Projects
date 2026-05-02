#!/bin/bash
# Session wrap-up push — 2026-04-29
# Run this from Terminal to push today's wrap-up changes to GitHub
# Files updated: session-log.md

cd ~/Projects

# Remove stale git lock if present
[ -f .git/index.lock ] && rm .git/index.lock && echo "Removed stale lock"

git pull --rebase origin main
git add Productivity/memory/session-log.md
git commit -m "Session: 2026-04-29 wrap-up sync"
git push origin main
echo "✅ Wrap-up pushed to GitHub"
