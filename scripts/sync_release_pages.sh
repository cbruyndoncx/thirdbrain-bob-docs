#!/usr/bin/env bash
# Copy the release pages the vault generates into data/release/, check the site builds,
# then commit and push. CI rebuilds the site. Run after a release, next to
# sync_catalogue.sh: the vault regenerates these files during the release (vault-release),
# and this repository only copies them; scripts/build_release_pages.py converts them.
#   SKILL-PACKS.md  -> /skill-packs/  (one anchor per pack: #core, #sales, ...)
# Usage: scripts/sync_release_pages.sh [--no-push] [VAULT]
set -euo pipefail
cd "$(dirname "$0")/.."
PUSH=1
if [[ "${1:-}" == "--no-push" ]]; then PUSH=0; shift; fi
VAULT="${1:-/mnt/c/Users/bruyn/Documents/brncx-skills}"
FILES=(SKILL-PACKS.md)
for f in "${FILES[@]}"; do
  [[ -f "$VAULT/$f" ]] || { echo "missing source: $VAULT/$f" >&2; exit 1; }
done

if [[ -n "$(git status --porcelain -- data/release)" ]]; then
  echo "data/release/ has uncommitted changes; commit or discard them first" >&2; exit 1
fi
if (( PUSH )); then git pull --ff-only --quiet; fi

mkdir -p data/release
for f in "${FILES[@]}"; do cp "$VAULT/$f" "data/release/$f"; done

scripts/build.sh
if command -v mkdocs > /dev/null; then mkdocs build --strict --quiet
else uv run --quiet --no-project --with-requirements requirements.txt mkdocs build --strict --quiet; fi

git add -A data/release reports
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git diff --cached --stat | tail -1
git commit --quiet -m "Sync release pages from vault ($(date +%F))"
if (( PUSH )); then git push --quiet && echo "pushed; the Pages workflow deploys in about 2 minutes"
else echo "committed, not pushed"; fi
