---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: vault-upgrade — ThirdBrain BOB skill
  description: 'Upgrades user vaults while preserving customizations and backing up modifications with three-way merge. Use when the user says ''upgrade vault'', ''update vault'', '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: vault-upgrade
catLabel: obsidian
area: foundational
desc: Upgrades user vaults while preserving customizations and backing up modifications with three-way merge.
summary: Upgrades user vaults while preserving customizations and backing up modifications with three-way merge. Use when the user says 'upgrade vault', 'update vault', 'sync vault', 'newer version', or 'three-way merge methodology'.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[config]'
roles: '[]'
inputs:
- custom-path — CUSTOM_PATH — the live customized vault (--custom)
- new-path — NEW_PATH — the extracted new release (--new)
- original-path — ORIGINAL_PATH — the prior-release baseline the user last installed (--original)
- output-path — Staging path (--output); defaults to the CUSTOM_PATH.upgraded sibling
outputs:
- 'Machine-readable result written by --execute: updated, added, preserved, conflicts, ai_merges, errors; the source of the Step 7 delta and the Step 8 report'
- Merged staging vault written by --execute, a sibling of CUSTOM_PATH outside any vault; kept until the owner confirms the finalize
- One merge prompt per file that needs a three-way merge (Step 6)
- Structured upgrade summary saved in Step 8
- prefer a permanent directory)
- '{custom-path}.upgraded/'
- '{custom-path}.upgraded/.merge-requests/'
- '{custom-path}.upgraded/.upgrade-report.json'
prompts:
- Upgrade my vault to the latest version
- Sync my vault with the upstream changes
- Update my vault while preserving my customizations
---
