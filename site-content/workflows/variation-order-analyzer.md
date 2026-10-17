---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Variation Order Analyzer — BOB Workflow
  description: 'Target Audience: Quantity surveyors, contract administrators, project directors, and claims consultants managing FIDIC variation orders in UAE/GCC construction '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: variation-order-analyzer
youtubeId: ''
published: ''
privacy: unlisted
title: Variation Order Analyzer
thumbnail: ''
subtitle: FIDIC Variation Valuation
inputs:
- label: variation-request.md
  icon: 📝
- label: schedule-of-rates.xlsx
  icon: 💰
- label: original-scope.pdf
  icon: 📜
outputs:
- label: vo_entitlement.md
  icon: ⚖️
- label: vo_valuation.md
  icon: 📊
- label: variation_register.md
  icon: 📋
steps:
- Assess entitlement
- Apply valuation hierarchy
- Calculate cost breakdown
- label: Review valuation
  actor: human
- Assess schedule impact
- Update variation register
trigger: '"Value this variation order using FIDIC Red Book 2017 rates"'
timeSavings: ~1-2 days manual valuation → ~25 min automated
compounding: Variation register grows into a defensible audit trail — cumulative value tracking
frequency: Per variation instruction · monthly register update
hook: 'The scope changed.

  What it''s worth is anyone''s guess.'
outcome: ''
benefits: []
cta: ''
difficulty: expert
primaryRoles:
- Operations Manager
pricingTier: pack-engineering-pro
category: engineering
filterGroup: engineering
area: operations
---

**Target Audience:** Quantity surveyors, contract administrators, project directors, and claims consultants managing FIDIC variation orders in UAE/GCC construction projects.
