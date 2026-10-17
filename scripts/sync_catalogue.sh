#!/usr/bin/env bash
# Regenerate data/catalogue.json (the skills and workflows library) with the website's
# emitter, check the site builds, then commit and push. Run after a release is
# published, not on every vault edit. The emitter keeps only what the latest
# thirdbrain-full tag shipped; it finds the release-history repository through the
# vault's release-ops settings and only reads it.
# Usage: scripts/sync_catalogue.sh [--no-push] [VAULT] [WEBSITE_REPO]
set -euo pipefail
cd "$(dirname "$0")/.."
PUSH=1
if [[ "${1:-}" == "--no-push" ]]; then PUSH=0; shift; fi
VAULT="${1:-/mnt/c/Users/bruyn/Documents/brncx-skills}"
SITE="${2:-/home/cb/projects/dev/brncx}"
[[ -d "$VAULT" && -f "$SITE/scripts/emit_catalogue.py" ]] || { echo "missing source: $VAULT or $SITE/scripts/emit_catalogue.py" >&2; exit 1; }

if [[ -n "$(git status --porcelain -- data)" ]]; then
  echo "data/ has uncommitted changes; commit or discard them first" >&2; exit 1
fi
if (( PUSH )); then git pull --ff-only --quiet; fi

uv run --quiet "$SITE/scripts/emit_catalogue.py" --vault "$VAULT" --out "$PWD/data/catalogue.json"
TAG=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["release"])' data/catalogue.json)

scripts/build.sh
if command -v mkdocs > /dev/null; then mkdocs build --strict --quiet
else uv run --quiet --no-project --with-requirements requirements.txt mkdocs build --strict --quiet; fi

git add -A data reports
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git diff --cached --stat | tail -1
git commit --quiet -m "Sync library catalogue: $TAG"
if (( PUSH )); then git push --quiet && echo "pushed; the Pages workflow deploys in about 2 minutes"
else echo "committed, not pushed"; fi
