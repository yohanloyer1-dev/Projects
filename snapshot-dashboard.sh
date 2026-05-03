#!/bin/zsh
# snapshot-dashboard.sh — save a versioned copy of dashboard.html before editing
# Usage: ./snapshot-dashboard.sh [description]
# Example: ./snapshot-dashboard.sh pre-drag-sections
# If no description given, defaults to "snapshot"

VERSIONS_DIR="$(dirname "$0")/Productivity/versions"
DASHBOARD="$(dirname "$0")/Productivity/dashboard.html"

if [[ ! -f "$DASHBOARD" ]]; then
  echo "✗ dashboard.html not found at $DASHBOARD"
  exit 1
fi

# Find latest version number — only look at dashboard_v files (not legacy subdir)
LATEST=$(ls "$VERSIONS_DIR"/dashboard_v[0-9]*.html 2>/dev/null \
  | grep -oE 'dashboard_v[0-9]+\.[0-9]+' \
  | sed 's/dashboard_v//' \
  | awk -F. '{ printf "%05d.%05d\n", $1, $2 }' \
  | sort -n \
  | tail -1 \
  | awk -F. '{ printf "%d.%d\n", $1+0, $2+0 }')

if [[ -z "$LATEST" ]]; then
  NEXT="1.0"
else
  MAJOR="${LATEST%.*}"
  MINOR="${LATEST#*.}"
  NEXT="${MAJOR}.$((MINOR + 1))"
fi

DESC="${1:-snapshot}"
TODAY=$(date +%Y-%m-%d)
FILENAME="dashboard_v${NEXT}_${TODAY}_${DESC}.html"
DEST="$VERSIONS_DIR/$FILENAME"

cp "$DASHBOARD" "$DEST"
echo "✓ Snapshot saved: Productivity/versions/$FILENAME"
