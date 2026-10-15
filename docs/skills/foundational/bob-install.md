---
description: '<!-- context-pack: ok-file — release: bob-install runs from the unpacked release vault before any skill is installed, so its commands run from the vault root (owner decision 2026-09-23) -->'
title: bob-install
---

# bob-install

<!-- context-pack: ok-file — release: bob-install runs from the unpacked release vault before any skill is installed, so its commands run from the vault root (owner decision 2026-09-23) -->

- **Area:** Foundational
- **Category:** utilities
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Installs a freshly unpacked BOB vault — runs the interactive TUI installer that sets up system dependencies (Node, Python/uv, jq, git), AI CLIs through acp-doctor,…

## How you ask

- “I just unzipped the vault, now what?”
- “Install BOB on this machine”
- “Run setup phase 4 — my plugins didn't install”

## Inputs

- vault_path — Vault root. Auto-detected from script location or cwd when omitted.
- headless — Run non-interactively (--headless). Skips prompts; phase 7 API keys must then be set by hand.
- phase — 1=System 2=AI-Tools 3=Obsidian 4=Plugins 5=Vault 6=Optional 7=API-Keys (1 | 2 | 3 | 4 | 5 | 6 | 7)
- vault_path — Vault root. Auto-detected when omitted.
- write — Write the rendered templates. Omitted, the route only reports and exits 1 when anything would change.
- output_dir — Write the rendered tree here instead of in place — verification, or a workspace being scaffolded.
- replace_existing — Overwrite a destination file that differs from the rendered template, keeping a copy under .template-backups/. Omitted, such a file is kept as found and reported.
- write — Merge the rendered values into the files. Omitted, the route only reports drift and exits 1 when it finds any.
- only — Render only the .obsidian JSON settings, or only the Bases. (all | settings | bases)
- command — refresh (default) writes this host's entry; show prints it (with --tool NAME for one tool); hosts lists every machine in the file. (refresh | show | hosts)
- dry_run — refresh only: print this host's entry and write nothing.
- headless — Run without prompts (--headless); installs every missing plugin in the manifest.

## Outputs

- /tmp/thirdbrain-setup-{YYYYMMDD-HHMMSS}.log
- API keys written by the interactive phase 7. Never printed.
- API keys written when phase 7 is the selected phase. Never printed.
- Bases whose folder filters now name the active pack's folders.
- JSON-compatible YAML, one entry per hostname under `hosts`. Only this host's `detected` section is rewritten; other hosts and this host's `config`, `install_policy` and `wanted` are kept. A copy of the previous file goes to ~/backups/{vault-name}/system-yaml-{date}/ first.
- The layout the vault was last rendered for, so a later pack change can be recognised. Written only with --write.
- The note templates with every {key} expanded to this workspace's folders.
- Written by setup.sh (Linux/WSL/macOS) to /tmp. On native Windows setup.ps1 tees the same transcript to %TEMP%\thirdbrain-setup-{YYYYMMDD-HHMMSS}.log.
- app.json, daily-notes.json, templates.json and the mapped plugin data.json files, merged in place — every other key and its order preserved.
- updated-plugin-config (json)
- {vault.agents}/system.yaml
- {vault.bases}/
- {vault.templates}/
- {vault}/.env
- {vault}/.obsidian/
- {vault}/.obsidian/bob-rendered-paths.json
- {vault}/.obsidian/community-plugins.json

