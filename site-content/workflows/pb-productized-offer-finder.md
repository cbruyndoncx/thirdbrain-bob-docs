---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Productized Offer Finder — BOB Workflow
  description: Productized Offer Finder
  socialImage: https://img.youtube.com/vi/RUtF6Ltz2nk/maxresdefault.jpg
skillName: pb-productized-offer-finder
youtubeId: RUtF6Ltz2nk
published: '2026-08-01'
privacy: public
title: Productized Offer Finder
thumbnail: https://img.youtube.com/vi/RUtF6Ltz2nk/maxresdefault.jpg
subtitle: Ranked shortlist of 3-5 productized AI offer concepts with RICE scores, value-ladder slots, MVP brief for the top pick, and a validation plan to test before building
inputs:
- label: 'Business: what they sell, to whom, who pays them'
  icon: 🏢
- label: 'ICP: top 2-3 pains and recurring triggers'
  icon: 🎯
- label: Current offers (paid + free); identify gaps in the value ladder
  icon: 📋
- label: Existing offer ideas (or "start fresh")
  icon: 📋
- label: 'Build capacity: solo founder, small team, has dev resources'
  icon: 📋
- label: 'Constraints: brand voice, regulatory, time-to-launch deadline'
  icon: 📅
outputs:
- label: Offer Shortlist.md
  icon: 📋
- label: Value-Ladder Map.md
  icon: 🗺️
- label: MVP Brief.md
  icon: 📋
- label: Pricing Tiers.md
  icon: 💰
- label: Validation Plan.md
  icon: 🗺️
steps:
- label: vault-preflight → verify business/client context completeness; flag missing ICP, profile, or marketing context before starting
  actor: agent
- label: icp-discovery OR business-baseline → if ICP/profile missing, run discovery; if both present, skip to step 3
  actor: agent
- label: ai-usecase-discovery → ideate AI use cases for the buyer's domain; produces a long candidate list
  actor: agent
- label: free-tool-strategy / productized-offer route → shape candidates into 3-5 ranked productized offers across the four format categories (audit, playbook, roadmap, mini-system); each tagged with value-ladder
    slot, RICE, AI-fit, stack, ROI
  actor: agent
- label: Review shortlist; pick top idea OR adjust ranking based on founder constraints (build capacity, brand fit, urgency)
  actor: human
- label: prioritization-craft → optional deeper RICE/ICE comparison if shortlist is contested or close-scored
  actor: agent
- label: pricing-strategy → confirm value-ladder slot for the chosen idea; recommend price point and tier structure
  actor: agent
- label: zero-to-launch → MVP brief for the chosen idea (week-1 scope, build approach, success criteria)
  actor: agent
- label: 'product-testing → validation plan: smoke test, landing-page test, or pre-sale before development begins'
  actor: agent
trigger: '"Founder, coach, or operator wants ranked AI-automated offer ideas across the value ladder (lead magnet → tripwire → core → upsell → continuity)"'
timeSavings: 'Typical run: 90-150 minutes, single or two sessions'
compounding: Each run refines templates and context — 8 automated steps improve with accumulated data
frequency: Per trigger event
hook: 'You could sell anything.

  Which is why you sell nothing consistently.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---

Ranked shortlist of 3-5 productized AI offer concepts with RICE scores, value-ladder slots, MVP brief for the top pick, and a validation plan to test before building


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.
