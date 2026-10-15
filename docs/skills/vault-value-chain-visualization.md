---
description: Generate derived value-chain and playbook visuals from the vault's canonical value-chain and playbook sources. The process below is the operational summary of the visualization README; do not hand-edit generated HTML, PDFs, PNGs, or draw.io outputs.
title: vault-value-chain-visualization
---

# vault-value-chain-visualization

Generate derived value-chain and playbook visuals from the vault's canonical value-chain and playbook sources. The process below is the operational summary of the visualization README; do not hand-edit generated HTML, PDFs, PNGs, or draw.io outputs.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Generates value-chain maps, chain PDFs, combined catalogues, and single-playbook one-sheets from the BRNCX vault.

## How you ask

- “Regenerate the value-chain catalogue”
- “Make a one-sheet PDF for the client-onboarding playbook”
- “Build a starter-tier preview of the value chain — nothing above that tier”
- “Refresh the draw.io map and the combined value-chain PDF”

## Inputs

- vault_path — Vault root containing the canonical value-chain and playbook sources
- playbook — Playbook title or filename stem
- tier — Release tier, such as starter, pro, or full
- playbook — Optional playbook title for a single preview

## Outputs

- combined_pdf (pdf)
- pdf (pdf)
- preview (pdf)
- {release_staging_dir}/
- {viz_output_dir}/all-value-chains.pdf
- {viz_output_dir}/playbook-{stem}.pdf

