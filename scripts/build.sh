#!/usr/bin/env bash
# Generate docs/ from the synced sources in this repository. CI runs this before mkdocs.
# Usage: scripts/build.sh [WIKI_SRC] [CATALOGUE]
#   WIKI_SRC   raw Obsidian wiki (default: wiki/, filled by scripts/sync_wiki.sh)
#   CATALOGUE  skills and workflows library (default: data/catalogue.json, filled by
#              scripts/sync_catalogue.sh)
set -euo pipefail
cd "$(dirname "$0")/.."
WIKI="${1:-wiki}"
CATALOGUE="${2:-data/catalogue.json}"
rm -rf docs build && mkdir -p docs build reports
python3 scripts/build_library.py "$CATALOGUE" docs --linkmap build/linkmap.json
python3 scripts/export_wiki.py "$WIKI" docs --linkmap build/linkmap.json
cp -r assets/. docs/
cp -r pages/. docs/   # site-only pages (the landing page), over the export
