---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: vault-value-chain-visualization — ThirdBrain BOB skill
  description: Generate derived value-chain and playbook visuals from the vault's canonical value-chain and playbook sources. The process below is the operational summary of t
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: vault-value-chain-visualization
catLabel: utilities
area: foundational
desc: Generates value-chain maps, chain PDFs, combined catalogues, and single-playbook one-sheets from the BRNCX vault.
summary: Generate derived value-chain and playbook visuals from the vault's canonical value-chain and playbook sources. The process below is the operational summary of the visualization README; do not hand-edit generated HTML, PDFs, PNGs, or draw.io outputs.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- vault_path — Vault root containing the canonical value-chain and playbook sources
- playbook — Playbook title or filename stem
- tier — Release tier, such as starter, pro, or full
- playbook — Optional playbook title for a single preview
outputs:
- combined_pdf (pdf)
- pdf (pdf)
- preview (pdf)
- '{release_staging_dir}/'
- '{viz_output_dir}/all-value-chains.pdf'
- '{viz_output_dir}/playbook-{stem}.pdf'
prompts:
- Regenerate the value-chain catalogue
- Make a one-sheet PDF for the client-onboarding playbook
- Build a starter-tier preview of the value chain — nothing above that tier
- Refresh the draw.io map and the combined value-chain PDF
---
