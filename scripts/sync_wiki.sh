#!/usr/bin/env bash
# Copy the published part of the vault wiki into this repository, check the site
# builds, then commit and push. CI rebuilds the site.
# Usage: scripts/sync_wiki.sh [--no-push] [VAULT_WIKI]
set -euo pipefail
cd "$(dirname "$0")/.."
PUSH=1
if [[ "${1:-}" == "--no-push" ]]; then PUSH=0; shift; fi
WIKI="${1:-/mnt/c/Users/bruyn/Documents/brncx-skills/00-CORE/Wiki}"
[[ -d "$WIKI" ]] || { echo "missing source: $WIKI" >&2; exit 1; }

if [[ -n "$(git status --porcelain -- wiki)" ]]; then
  echo "wiki/ has uncommitted changes; commit or discard them first" >&2; exit 1
fi
if (( PUSH )); then git pull --ff-only --quiet; fi

# Only what the export publishes: no excluded folders, no publish:false pages, no unused assets.
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
python3 scripts/export_wiki.py "$WIKI" "$TMP/docs" --sources-list "$TMP/sources.txt" > /dev/null
rm -rf wiki && mkdir wiki
rsync -a --files-from="$TMP/sources.txt" "$WIKI/" wiki/

scripts/build.sh
if command -v mkdocs > /dev/null; then mkdocs build --strict --quiet
else uv run --quiet --no-project --with-requirements requirements.txt mkdocs build --strict --quiet; fi

git add -A wiki reports
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git diff --cached --stat | tail -1
git commit --quiet -m "Sync wiki from vault ($(date +%F))"
if (( PUSH )); then git push --quiet && echo "pushed; the Pages workflow deploys in about 2 minutes"
else echo "committed, not pushed"; fi
