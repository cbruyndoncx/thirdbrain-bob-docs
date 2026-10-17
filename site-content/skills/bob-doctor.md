---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: bob-doctor — ThirdBrain BOB skill
  description: 'The environment counterpart to `vault-preflight`. Where `vault-preflight` checks whether the business context exists (Layer 2), `bob-doctor` checks whether the '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: bob-doctor
catLabel: utilities
area: foundational
desc: Layer-1 environment readiness check for a new BOB install — the one-command 'what do I need' front door.
summary: The environment counterpart to `vault-preflight`. Where `vault-preflight` checks whether the business context exists (Layer 2), `bob-doctor` checks whether the machine is ready to run BOB at all (Layer 1) — OS, Obsidian, plugins, AI CLI, auth, paths, `uv`.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- vault — Vault path (defaults to auto-detected root from CWD).
- deep — Also scan every note for indexer-stalling size/duplication and broken symlinks. Costs a full vault walk (~30-60s on WSL/NTFS); off by default.
outputs:
- bob-doctor-report (markdown)
- prefer a permanent directory)
prompts:
- Bob doctor
- Check my setup
- Is my environment ready
---
