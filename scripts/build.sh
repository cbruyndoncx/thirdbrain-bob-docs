#!/usr/bin/env bash
# Regenerate docs/ from the vault wiki and the website's skills/workflows pages.
# Usage: scripts/build.sh [VAULT_WIKI] [SITE_CONTENT_EN]
set -euo pipefail
cd "$(dirname "$0")/.."
WIKI="${1:-/mnt/c/Users/bruyn/Documents/brncx-skills/00-CORE/Wiki}"
SITE="${2:-/home/cb/projects/dev/brncx/src/content/en}"
rm -rf docs build && mkdir -p docs build reports
python3 scripts/build_library.py "$SITE" docs --linkmap build/linkmap.json
python3 scripts/export_wiki.py "$WIKI" docs --linkmap build/linkmap.json
cp -r assets/. docs/ 2>/dev/null || true
