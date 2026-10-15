---
description: Generate a self-contained HTML visualization from any Obsidian base. Works in Obsidian's HTML Reader plugin and any browser — no JS, no external assets.
title: base-viz
---

# base-viz

Generate a self-contained HTML visualization from any Obsidian base. Works in Obsidian's HTML Reader plugin and any browser — no JS, no external assets.

- **Area:** Foundational
- **Category:** obsidian
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Generates self-contained HTML visualizations (hero stats + optional coverage matrix + grouped card sections) from any Obsidian base, driven by a per-base YAML config.

## How you ask

- “Render the Value Chains base as a self-contained HTML coverage dashboard.”
- “Create a base-viz config that groups our partner base by partner type.”
- “Regenerate this base visualization from a cached markdown table.”

## Inputs

- base_path — Vault-relative path to the .base file
- config_path — Vault-relative path to the .viz.yml config file
- out_path — Output HTML path (default: `{output.scratch}/`)
- base_path — Vault-relative path to the .base file the new config will visualize
- group_by_field — Exact output-table column used to group cards and coverage rows

## Outputs

- config_file (yaml)
- html_file (html)
- prefer a permanent directory)
- {near the entity folder}

