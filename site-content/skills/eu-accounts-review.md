---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: eu-accounts-review — ThirdBrain BOB skill
  description: 'Orchestrate a unified analytical review across a group structure that spans Belgian (NBB) and Dutch (KvK) entities. Input: a mixed list of KBO and KvK enterpris'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: eu-accounts-review
catLabel: finance
area: finance
desc: Reviews EU group structures across Belgium and the Netherlands and produces a consolidated audit-style deliverable.
summary: 'Orchestrate a unified analytical review across a group structure that spans Belgian (NBB) and Dutch (KvK) entities. Input: a mixed list of KBO and KvK enterprise numbers (auto-detected by length — 10 digits = KBO, 8 digits = KvK). Output: a consolidated group deliverable combining per-entity reviews from the jurisdiction skills, plus cross-border analyses that neither single-jurisdiction skill can produce.'
difficulty: advanced
inputType: data
outputType: spreadsheet
requires: '[install]'
roles: '[Finance Manager]'
inputs:
- parent_enterprise_number — Parent KBO (10 digits, BE) or KvK (8 digits, NL)
- subsidiary_enterprise_numbers — Mixed list of KBO and KvK numbers; jurisdiction auto-detected per entity
- years — Years used to run analytical review across a group spanning BE and NL entities, producing a unified deliverable
- client_id — Client id used to run analytical review across a group spanning BE and NL entities, producing a unified deliverable
- parent_enterprise_number — Parent enterprise number used to for a parent holding subsidiaries across BE and NL, scan carrying value (in parent jurisdiction) against subsidiary equity (in subsidiary jurisdiction). Highlights FX and accounting-policy differences
- subsidiary_enterprise_numbers — Subsidiary enterprise numbers used to for a parent holding subsidiaries across BE and NL, scan carrying value (in parent jurisdiction) against subsidiary equity (in subsidiary jurisdiction). Highlights FX and accounting-policy differences
outputs:
- group_bundle (markdown)
- impairment_scan (markdown)
- prefer a permanent directory)
prompts:
- Cross- border group
- Consolidated audit-style review
- EU group structure
---
