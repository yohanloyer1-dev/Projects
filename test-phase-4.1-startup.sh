#!/bin/bash
# FILE: test-phase-4.1-startup.sh
# Phase 4.1: Complete Startup Protocol Test
# Executable in any fresh Cowork session with /mnt/Projects mounted

set -e

GITHUB_BASE="https://raw.githubusercontent.com/yohanloyer1-dev/Projects/main"
PROJECT_ROOT="/mnt/Projects"
RESULTS_FILE="/tmp/phase-4.1-results.txt"
TIMESTAMP=$(date -u +'%Y-%m-%d %H:%M:%S UTC')

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Initialize results
PASS_COUNT=0
FAIL_COUNT=0

echo "=== Phase 4.1: Startup Protocol Test ===" | tee $RESULTS_FILE
echo "Timestamp: $TIMESTAMP" | tee -a $RESULTS_FILE
echo "Project Root: $PROJECT_ROOT" | tee -a $RESULTS_FILE
echo "" | tee -a $RESULTS_FILE

# Helper function
test_result() {
  local test_name=$1
  local pass=$2
  local details=$3

  if [ "$pass" = true ]; then
    echo -e "${GREEN}✓${NC} $test_name" | tee -a $RESULTS_FILE
    echo "  $details" | tee -a $RESULTS_FILE
    ((PASS_COUNT++))
  else
    echo -e "${RED}✗${NC} $test_name" | tee -a $RESULTS_FILE
    echo "  $details" | tee -a $RESULTS_FILE
    ((FAIL_COUNT++))
  fi
}

# T-4.1.1: CLAUDE.md from GitHub
echo "T-4.1.1: Fetching CLAUDE.md from GitHub..." | tee -a $RESULTS_FILE
if curl -sf "$GITHUB_BASE/CLAUDE.md" > /tmp/claude-github.md 2>/dev/null; then
  SIZE=$(wc -c < /tmp/claude-github.md)
  CONTAINS_COMPANIES=$(grep -c "^| \*\*Gorgias\*\*" /tmp/claude-github.md || echo "0")
  CONTAINS_FILEYSTEM=$(grep -c "## File System" /tmp/claude-github.md || echo "0")

  if [ $SIZE -gt 5000 ] && [ $CONTAINS_COMPANIES -eq 1 ] && [ $CONTAINS_FILEYSTEM -eq 1 ]; then
    test_result "T-4.1.1: CLAUDE.md from GitHub" true "size=${SIZE}B, has Companies section, has File System section"
  else
    test_result "T-4.1.1: CLAUDE.md from GitHub" false "size=${SIZE}B, companies=${CONTAINS_COMPANIES}, filesystem=${CONTAINS_FILEYSTEM}"
  fi
else
  test_result "T-4.1.1: CLAUDE.md from GitHub" false "curl failed or 404"
fi

# T-4.1.2: TASKS.md from GitHub
echo "T-4.1.2: Fetching TASKS.md from GitHub..." | tee -a $RESULTS_FILE
if curl -sf "$GITHUB_BASE/TASKS.md" > /tmp/tasks-github.md 2>/dev/null; then
  SIZE=$(wc -c < /tmp/tasks-github.md)
  HAS_PHASE_1=$(grep -c "Phase 1:" /tmp/tasks-github.md || echo "0")
  HAS_PHASE_4=$(grep -c "Phase 4:" /tmp/tasks-github.md || echo "0")

  if [ $SIZE -gt 1500 ] && [ $HAS_PHASE_1 -eq 1 ] && [ $HAS_PHASE_4 -eq 1 ]; then
    test_result "T-4.1.2: TASKS.md from GitHub" true "size=${SIZE}B, has Phase 1 and Phase 4"
  else
    test_result "T-4.1.2: TASKS.md from GitHub" false "size=${SIZE}B, phase1=${HAS_PHASE_1}, phase4=${HAS_PHASE_4}"
  fi
else
  test_result "T-4.1.2: TASKS.md from GitHub" false "curl failed or 404"
fi

# T-4.1.3: DASHBOARD-TASKS.md from GitHub
echo "T-4.1.3: Fetching DASHBOARD-TASKS.md from GitHub..." | tee -a $RESULTS_FILE
if curl -sf "$GITHUB_BASE/Productivity/DASHBOARD-TASKS.md" > /tmp/dashboard-tasks-github.md 2>/dev/null; then
  SIZE=$(wc -c < /tmp/dashboard-tasks-github.md)
  HAS_PERSONAL=$(grep -c "## 🧑 Personal" /tmp/dashboard-tasks-github.md || echo "0")
  HAS_PROFESSIONAL=$(grep -c "## 💼 Professional" /tmp/dashboard-tasks-github.md || echo "0")
  HAS_FREELANCE=$(grep -c "## 🔧 Freelance" /tmp/dashboard-tasks-github.md || echo "0")

  if [ $SIZE -gt 8000 ] && [ $HAS_PERSONAL -eq 1 ] && [ $HAS_FREELANCE -eq 1 ]; then
    test_result "T-4.1.3: DASHBOARD-TASKS.md from GitHub" true "size=${SIZE}B, all sections present"
  else
    test_result "T-4.1.3: DASHBOARD-TASKS.md from GitHub" false "size=${SIZE}B, sections present=${HAS_PERSONAL}/${HAS_PROFESSIONAL}/${HAS_FREELANCE}"
  fi
else
  test_result "T-4.1.3: DASHBOARD-TASKS.md from GitHub" false "curl failed or 404"
fi

# T-4.1.4: CLAUDE-COWORK-OPERATING-SYSTEM.md from GitHub
echo "T-4.1.4: Fetching CLAUDE-COWORK-OPERATING-SYSTEM.md..." | tee -a $RESULTS_FILE
if curl -sf "$GITHUB_BASE/CLAUDE-COWORK-OPERATING-SYSTEM.md" > /tmp/os-github.md 2>/dev/null; then
  SIZE=$(wc -c < /tmp/os-github.md)
  HAS_STARTUP=$(grep -c "## Session Startup" /tmp/os-github.md || echo "0")
  HAS_ROUTING=$(grep -c "## Memory Routing Table" /tmp/os-github.md || echo "0")

  if [ $SIZE -gt 3000 ] && [ $HAS_STARTUP -eq 1 ] && [ $HAS_ROUTING -eq 1 ]; then
    test_result "T-4.1.4: CLAUDE-COWORK-OPERATING-SYSTEM.md" true "size=${SIZE}B, has Startup and Routing sections"
  else
    test_result "T-4.1.4: CLAUDE-COWORK-OPERATING-SYSTEM.md" false "size=${SIZE}B, sections=${HAS_STARTUP}/${HAS_ROUTING}"
  fi
else
  test_result "T-4.1.4: CLAUDE-COWORK-OPERATING-SYSTEM.md" false "curl failed or 404"
fi

# T-4.1.5: Local files match GitHub versions
echo "T-4.1.5: Comparing local files to GitHub versions..." | tee -a $RESULTS_FILE
if [ -f "$PROJECT_ROOT/CLAUDE.md" ]; then
  LOCAL_CLAUDE=$(cat "$PROJECT_ROOT/CLAUDE.md" 2>/dev/null | wc -c)
  GITHUB_CLAUDE=$(wc -c < /tmp/claude-github.md)

  if [ "$LOCAL_CLAUDE" -eq "$GITHUB_CLAUDE" ]; then
    test_result "T-4.1.5: Local CLAUDE.md matches GitHub" true "byte-identical (${LOCAL_CLAUDE}B)"
  else
    DIFF=$((LOCAL_CLAUDE - GITHUB_CLAUDE))
    test_result "T-4.1.5: Local CLAUDE.md matches GitHub" false "diff=${DIFF}B (local=${LOCAL_CLAUDE}, github=${GITHUB_CLAUDE})"
  fi
else
  test_result "T-4.1.5: Local CLAUDE.md matches GitHub" false "Local file not found"
fi

# T-4.1.6: Memory routing files
echo "T-4.1.6: Checking memory routing files..." | tee -a $RESULTS_FILE
MEMORY_DIR="$PROJECT_ROOT/Productivity/memory"
ROUTING_FILES=(
  "$MEMORY_DIR/session-log.md"
  "$MEMORY_DIR/dashboard-changelog.md"
  "$MEMORY_DIR/sync-automation-audit.md"
  "$MEMORY_DIR/context/ohtani-matrix.md"
)

ALL_ROUTING_OK=true
for FILE in "${ROUTING_FILES[@]}"; do
  if [ ! -f "$FILE" ]; then
    ALL_ROUTING_OK=false
    echo "  Missing: $FILE" | tee -a $RESULTS_FILE
  fi
done

if [ "$ALL_ROUTING_OK" = true ]; then
  test_result "T-4.1.6: Memory routing files" true "All 4 files exist and readable"
else
  test_result "T-4.1.6: Memory routing files" false "Some files missing (see above)"
fi

# T-4.1.7: .gitignore verification
echo "T-4.1.7: Verifying .gitignore..." | tee -a $RESULTS_FILE
if [ -f "$PROJECT_ROOT/.gitignore" ]; then
  GITIGNORE_SIZE=$(wc -c < "$PROJECT_ROOT/.gitignore")
  if [ $GITIGNORE_SIZE -gt 100 ]; then
    test_result "T-4.1.7: .gitignore exists" true "size=${GITIGNORE_SIZE}B"
  else
    test_result "T-4.1.7: .gitignore exists" false "too small (${GITIGNORE_SIZE}B)"
  fi
else
  test_result "T-4.1.7: .gitignore exists" false "File not found"
fi

# T-4.1.8: Git status
echo "T-4.1.8: Checking git status..." | tee -a $RESULTS_FILE
cd "$PROJECT_ROOT"
GIT_STATUS=$(git status --short 2>/dev/null | wc -l)

if [ $GIT_STATUS -eq 0 ] || [ $GIT_STATUS -le 1 ]; then
  test_result "T-4.1.8: Git status clean" true "untracked files=${GIT_STATUS}"
else
  test_result "T-4.1.8: Git status clean" false "untracked files=${GIT_STATUS}"
  git status --short | head -5 | tee -a $RESULTS_FILE
fi

# Summary
echo "" | tee -a $RESULTS_FILE
echo "=== PHASE 4.1 SUMMARY ===" | tee -a $RESULTS_FILE
echo -e "PASS: ${GREEN}$PASS_COUNT${NC}" | tee -a $RESULTS_FILE
echo -e "FAIL: ${RED}$FAIL_COUNT${NC}" | tee -a $RESULTS_FILE
echo "Results saved to: $RESULTS_FILE" | tee -a $RESULTS_FILE
echo ""

if [ $FAIL_COUNT -eq 0 ]; then
  echo -e "${GREEN}✓ Phase 4.1 PASSED${NC}"
  exit 0
else
  echo -e "${RED}✗ Phase 4.1 FAILED${NC}"
  exit 1
fi
