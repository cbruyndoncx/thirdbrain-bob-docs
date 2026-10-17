---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: BOQ Audit Interior Fit Out — BOB Workflow
  description: BOQ Audit Interior Fit Out
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-boq-audit-interior-fit-out
youtubeId: ''
published: ''
privacy: unlisted
title: BOQ Audit Interior Fit Out
thumbnail: ''
subtitle: Fit-out BOQ audited with sector-specific spec depth (RCP coordination, false ceiling fascia, joinery EO pricing, finish brands), bids levelled, hold-points and escalation clauses generated
inputs: []
outputs: []
steps:
- label: '**Validate fit-out context** — confirm tenant tier, RCP availability, mock-up policy. Flag the sector context pack for the audit'
  actor: human
- label: '**boq-audit (audit-boq)** → using `--alias {matter-alias}` and the fit-out context pack, run the four audit passes; spec-gap pass uses the NLM-grounded fit-out brand list, EO-pricing pass uses
    fit-out patterns; every flag carries an NLM citation'
  actor: agent
- label: '**boq-audit (level-bids)** → with fit-out SOV extensions, split joinery into Fixed/Movable/Fascia, ensure mock-up line item appears'
  actor: agent
- label: '**Review with interior designer + owner-rep** — fit-out audits often require designer sign-off on finish specifications and brand acceptability'
  actor: human
- label: '**Issue findings to contractor** — 7-day response window. Specifically request mock-up scheduling.'
  actor: human
- label: '**boq-audit (inspection-checklist)** → fit-out checklist heavily emphasises mock-up approval gates, MEP-RCP coordination at every fixture, and finish verification at delivery'
  actor: agent
- label: '**Owner-rep + designer make award decision** — designer carries authority on aesthetic intent; owner-rep on commercial. Award is binding only at this step'
  actor: human
trigger: '"Interior fit-out BOQ received (commercial office, retail, hospitality, institutional fit-out) — needs auditing before award or payment"'
timeSavings: 'Typical run: 1-2 days for single BOQ; 2-3 days for multi-bid leveling'
compounding: Each run refines templates and context — 3 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'The fit-out quote looks fine.

  Until someone checks the ceiling and the joinery.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: operations
---


