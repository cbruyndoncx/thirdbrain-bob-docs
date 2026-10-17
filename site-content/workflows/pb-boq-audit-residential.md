---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: BOQ Audit Residential — BOB Workflow
  description: BOQ Audit Residential
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-boq-audit-residential
youtubeId: ''
published: ''
privacy: unlisted
title: BOQ Audit Residential
thumbnail: ''
subtitle: Residential BOQ audited with sector-specific depth (kitchens, bathrooms, built-in wardrobes, finishes), bids levelled, escalation clauses and hold-points generated
inputs: []
outputs: []
steps:
- label: '**Validate residential context** — confirm new build vs renovation, kitchen/bath schedule, owner selection book. Load residential context pack'
  actor: human
- label: '**boq-audit (audit-boq)** → using `--alias {matter-alias}` and the residential context pack, run the four audit passes; spec-gap pass uses NLM-grounded owner brand preferences; quantity-validation
    pass uses residential benchmarks; every flag carries an NLM citation'
  actor: agent
- label: '**boq-audit (level-bids)** → with residential SOV extensions, normalise kitchen and bathroom categories across bidders'
  actor: agent
- label: '**Review with owner** — residential audits centre owner aesthetic decisions; walk through finish choices and pricing implications'
  actor: human
- label: '**Issue findings to contractor** — 5-7 day response. For renovations, flag site-condition allowances explicitly.'
  actor: human
- label: '**boq-audit (inspection-checklist)** → residential checklist emphasises waterproofing acceptance (wet areas), kitchen-module pre-installation check, finish snagging at handover'
  actor: agent
trigger: '"Residential construction or renovation BOQ received (single-family, multi-family, villa, apartment renovation) — needs auditing before award or payment"'
timeSavings: 'Typical run: 1 day for single BOQ; 2 days for multi-bid leveling'
compounding: Each run refines templates and context — 3 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'The villa quote is a spreadsheet.

  The kitchens and wardrobes are a guess.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: operations
---


