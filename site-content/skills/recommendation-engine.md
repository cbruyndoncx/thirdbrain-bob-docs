---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: recommendation-engine — ThirdBrain BOB skill
  description: 'Target Audience: Consultants and operators building advisory MVPs that map a client or lead profile to a ranked shortlist of options (insurance plans, AI tools,'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: recommendation-engine
catLabel: sales
area: sales
desc: Generic recommendation engine built on cbruyndoncx/awesome-comparisons.
summary: 'Target Audience: Consultants and operators building advisory MVPs that map a client or lead profile to a ranked shortlist of options (insurance plans, AI tools, vendors, suppliers, methodologies). Typical use is a sales-advisory demo, a discovery proposal for a new lead, or an internal decision-support tool for an existing client.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[CEO / Founder, Head of Sales, Product Manager]'
inputs:
- vertical_id — kebab-case dataset id (e.g. uae-health-insurance, ai-cli-agents)
- source_corpus — folder of source spec files (PDFs) to convert with docling
- vertical_id — existing dataset id
- changed_specs — list of source filenames that changed
- vertical_id — dataset to query
- profile — hard_criteria + optional weights overrides + recipient block (client_id or lead_id)
- top_n — shortlist size, default 3
outputs:
- ../<projects-sibling-dir>/awesome-comparisons/datasets/{vertical_id}/
- complete dataset folder ready for awesome-comparisons build
- dataset folder with only the changed entries rewritten
- see Output Locations)
- see Output Locations)` — PDF deliverable or proposal in the shortlist_to_pdfreport.py layout — summary, profile, weights, ranking, comparison grids, per-option details, recommendation
- see Output Locations)` — ranked shortlist with score, why-it-fits, trade-off
prompts:
- Recommendation engine
- Compare and recommend
- Shortlist
---
