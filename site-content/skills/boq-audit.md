---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: boq-audit — ThirdBrain BOB skill
  description: 'Target Audience: Quantity surveyors, construction project managers, interior design firms, fit-out contractors, owner''s representatives, and procurement leads w'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: boq-audit
catLabel: engineering
area: operations
desc: Audit construction Bills of Quantities (BOQ) and contractor bids for specification gaps, quantity anomalies, and Extra Over pricing errors — exporting a normalised…
summary: 'Target Audience: Quantity surveyors, construction project managers, interior design firms, fit-out contractors, owner''s representatives, and procurement leads who receive contractor BOQs or bids and need to validate them against industry standards before award or payment.'
difficulty: expert
inputType: conversation
outputType: document
requires: '[mcp, api-key]'
roles: '[Operations Manager, Finance Manager]'
inputs:
- boq-file — Path to the BOQ file (CSV, XLSX, or PDF). Must include item description, unit, quantity, rate, amount columns.
- project-context — One-line project description (sector, scope, region) — sharpens flag prioritisation.
- drawings-ref — Path or summary of architectural drawings (RCP, plans) used to cross-reference geometry.
- notebook-alias — NotebookLM alias for the matter — must contain the client's spec book, accepted brand list, regional price list, contract, and any prior-project BOQ history. Per `provenance-standard.md`, grounding is required, not optional. If no alias exists, stop and ask before proceeding.
- bid-files — Comma-separated paths to 2+ contractor bid files (CSV/XLSX/PDF).
- sov-template — Optional path to a custom SOV category map; defaults to the bundled SOV template.
- notebook-alias — NotebookLM alias for the matter — must contain the tender package, contractor bid documents, and reference price list. Per `provenance-standard.md`, grounding is required. If no alias exists, stop and ask before proceeding.
- audit-report — Path to a prior audit report from the audit-boq route.
- boq-file — Path to the BOQ; volatile items are auto-detected (steel, cement, copper, tariff-exposed imports).
- index-source — Index reference (default — local statistics agency CPI for construction materials).
- project-context — Project description — sector, scope, regions, scale.
outputs:
- anomaly-json (json)
- audit-report (markdown)
- boq-csv (csv)
- boq-scaffold (markdown)
- checklist (markdown)
- clauses (markdown)
- prefer a permanent directory)
- sov-csv (csv)
- sov-report (markdown)
prompts:
- Bill of quantities
- Audit BOQ
- Level bids
---
