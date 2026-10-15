---
description: The environment counterpart to `vault-preflight`. Where `vault-preflight` checks whether the business context exists (Layer 2), `bob-doctor` checks whether the machine is ready to run BOB at all (Layer 1) — OS, Obsidian, plugins, AI CLI, auth, paths, `uv`.
title: bob-doctor
---

# bob-doctor

The environment counterpart to `vault-preflight`. Where `vault-preflight` checks whether the business context exists (Layer 2), `bob-doctor` checks whether the machine is ready to run BOB at all (Layer 1) — OS, Obsidian, plugins, AI CLI, auth, paths, `uv`.

- **Area:** Foundational
- **Category:** utilities
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Layer-1 environment readiness check for a new BOB install — the one-command 'what do I need' front door.

## How you ask

- “Bob doctor”
- “Check my setup”
- “Is my environment ready”

## Inputs

- vault — Vault path (defaults to auto-detected root from CWD).
- deep — Also scan every note for indexer-stalling size/duplication and broken symlinks. Costs a full vault walk (~30-60s on WSL/NTFS); off by default.

## Outputs

- bob-doctor-report (markdown)
- prefer a permanent directory)

