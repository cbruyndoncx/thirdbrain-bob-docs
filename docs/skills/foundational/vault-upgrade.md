---
description: Upgrades user vaults while preserving customizations and backing up modifications with three-way merge. Use when the user says 'upgrade vault', 'update vault', 'sync vault', 'newer version', or 'three-way merge methodology'.
title: vault-upgrade
---

# vault-upgrade

Upgrades user vaults while preserving customizations and backing up modifications with three-way merge. Use when the user says 'upgrade vault', 'update vault', 'sync vault', 'newer version', or 'three-way merge methodology'.

- **Area:** Foundational
- **Category:** obsidian
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** config
- **Roles:** 

Upgrades user vaults while preserving customizations and backing up modifications with three-way merge.

## How you ask

- “Upgrade my vault to the latest version”
- “Sync my vault with the upstream changes”
- “Update my vault while preserving my customizations”

## Inputs

- custom-path — CUSTOM_PATH — the live customized vault (--custom)
- new-path — NEW_PATH — the extracted new release (--new)
- original-path — ORIGINAL_PATH — the prior-release baseline the user last installed (--original)
- output-path — Staging path (--output); defaults to the CUSTOM_PATH.upgraded sibling

## Outputs

- Machine-readable result written by --execute: updated, added, preserved, conflicts, ai_merges, errors; the source of the Step 7 delta and the Step 8 report
- Merged staging vault written by --execute, a sibling of CUSTOM_PATH outside any vault; kept until the owner confirms the finalize
- One merge prompt per file that needs a three-way merge (Step 6)
- Structured upgrade summary saved in Step 8
- prefer a permanent directory)
- {custom-path}.upgraded/
- {custom-path}.upgraded/.merge-requests/
- {custom-path}.upgraded/.upgrade-report.json

