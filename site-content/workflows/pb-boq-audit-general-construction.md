---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: BOQ Audit General Construction — BOB Workflow
  description: BOQ Audit General Construction
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-boq-audit-general-construction
youtubeId: ''
published: ''
privacy: unlisted
title: BOQ Audit General Construction
thumbnail: ''
subtitle: BOQ audited for spec gaps, quantity anomalies, and pricing errors; bids levelled into a Schedule of Values; inspection checklist and escalation clauses ready for use
inputs:
- label: Contractor BOQ(s)
  icon: 📋
- label: Project context (sector, region, currency, scope summary)
  icon: 📋
- label: Drawings (RCP, plans) if available
  icon: 🗺️
- label: Tender deadline and award timeline
  icon: 📅
outputs: []
steps:
- label: '**boq-audit (audit-boq)** → using `--alias {matter-alias}`, parse the contractor BOQ, run the four audit passes (spec-gap, quantity-validation, EO-pricing, cost-completeness), produce markdown
    audit report + JSON anomaly array with NLM citations on every flag'
  actor: agent
- label: '**boq-audit (level-bids)** → normalise all contractor bids into a Schedule of Values, flag "too good to be true" rates, buried preliminaries, and missing line items'
  actor: agent
- label: '**Review audit and SOV findings with owner-rep or QS** — walk through Critical and High flags, agree which to challenge with contractor, agree the lowest responsible bidder advisory'
  actor: human
- label: '**Issue findings to contractor** with 7-day response window for itemised re-bid or clarifications'
  actor: human
- label: '**boq-audit (inspection-checklist)** → derive a site inspection checklist from the audited BOQ — mock-up requirements, MEP coordination points, hold-points before installation'
  actor: agent
- label: '**Owner-rep makes award decision** based on audit + SOV + contractor responses + capacity assessment. Award is binding only at this step'
  actor: human
trigger: '"BOQ or contractor bid received for a general construction project (residential, commercial, mixed-use) — needs auditing before award or payment"'
timeSavings: 'Typical run: 1-2 days for single BOQ; 2-3 days for multi-bid leveling'
compounding: Each run refines templates and context — 3 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'The bid came in low.

  Low bids are where the claims come from.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: operations
---


