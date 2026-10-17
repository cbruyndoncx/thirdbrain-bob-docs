#!/usr/bin/env bash
# Generate docs/ from the synced sources in this repository. CI runs this before mkdocs.
# Usage: scripts/build.sh [WIKI_SRC] [SITE_CONTENT]
#   WIKI_SRC      raw Obsidian wiki (default: wiki/, filled by scripts/sync_wiki.sh)
#   SITE_CONTENT  website pages the library is built from (default: site-content/;
#                 interim until the library reads data/catalogue.json)
set -euo pipefail
cd "$(dirname "$0")/.."
WIKI="${1:-wiki}"
SITE="${2:-site-content}"
rm -rf docs build && mkdir -p docs build reports
python3 scripts/build_library.py "$SITE" docs --linkmap build/linkmap.json
python3 scripts/export_wiki.py "$WIKI" docs --linkmap build/linkmap.json
cp -r assets/. docs/ 2>/dev/null || true
