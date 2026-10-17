#!/usr/bin/env bash
# Regenerate data/catalogue.json (the skills and workflows library) with the website's
# emitter, limited to what the latest full release shipped, check the site builds, then
# commit and push. Run after a release is published, not on every vault edit.
# Usage: scripts/sync_catalogue.sh [--no-push] [VAULT] [WEBSITE_REPO] [RELEASE_REPO]
# The release-history repository is only read (ls-tree), never fetched or written.
set -euo pipefail
cd "$(dirname "$0")/.."
PUSH=1
if [[ "${1:-}" == "--no-push" ]]; then PUSH=0; shift; fi
VAULT="${1:-/mnt/c/Users/bruyn/Documents/brncx-skills}"
SITE="${2:-/home/cb/projects/dev/brncx}"
RELEASES="${3:-$VAULT/../brncx-releases}"
[[ -d "$VAULT" && -f "$SITE/scripts/emit_catalogue.py" ]] || { echo "missing source: $VAULT or $SITE/scripts/emit_catalogue.py" >&2; exit 1; }

if [[ -n "$(git status --porcelain -- data)" ]]; then
  echo "data/ has uncommitted changes; commit or discard them first" >&2; exit 1
fi
if (( PUSH )); then git pull --ff-only --quiet; fi

TAG=$(git -C "$RELEASES" tag -l 'thirdbrain-full-v*' --sort=-v:refname | head -1)
[[ -n "$TAG" ]] || { echo "no thirdbrain-full tag in $RELEASES" >&2; exit 1; }
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
{
  git -C "$RELEASES" -c core.quotePath=false ls-tree --name-only "$TAG:thirdbrain-full/00-CORE/Agents/skills" | sed 's/^/skill:/'
  git -C "$RELEASES" -c core.quotePath=false ls-tree --name-only "$TAG:thirdbrain-full/00-CORE/Playbooks" | grep '\.md$' | sed 's/\.md$//; s/^/playbook:/'
} > "$TMP/released.txt"
echo "release: $TAG ($(grep -c '^skill:' "$TMP/released.txt") skill folders, $(grep -c '^playbook:' "$TMP/released.txt") playbooks)"

uv run --quiet "$SITE/scripts/emit_catalogue.py" --vault "$VAULT" --out "$PWD/data/catalogue.json" --released "$TMP/released.txt"

scripts/build.sh
if command -v mkdocs > /dev/null; then mkdocs build --strict --quiet
else uv run --quiet --no-project --with-requirements requirements.txt mkdocs build --strict --quiet; fi

git add -A data reports
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git diff --cached --stat | tail -1
git commit --quiet -m "Sync library catalogue: $TAG"
if (( PUSH )); then git push --quiet && echo "pushed; the Pages workflow deploys in about 2 minutes"
else echo "committed, not pushed"; fi
