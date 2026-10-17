---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Regional Context — BOB Workflow
  description: Refresh and maintain regional business environment intelligence files. Each region has a domain config (scope, queries, advisory context) and a `business-enviro
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: regional-context
youtubeId: ''
published: ''
privacy: unlisted
title: Regional Context
thumbnail: ''
subtitle: Regional Business Intelligence
inputs:
- label: region-config.md
  icon: 🌍
- label: current-environment.md
  icon: 📋
outputs:
- label: business-environment.md
  icon: 🌐
- label: changelog.md
  icon: 📝
- label: inbox-briefing.md
  icon: 📨
steps:
- Load domain config
- Research regulatory and economic signals
- Compare delta against previous
- Write updated environment file
- Drop inbox briefing
trigger: '"Refresh the UAE regional context"'
timeSavings: ~4-6 hrs manual research → ~15 min automated
compounding: Each refresh adds to the changelog — trend detection and risk tracking improve over time
frequency: Monthly for active regions · quarterly for stable markets
hook: 'You''re selling into a new region.

  Everything you assume about it is a year old.'
outcome: ''
benefits: []
cta: ''
difficulty: beginner
primaryRoles: []
pricingTier: starter
category: research
filterGroup: research
area: research
---

Refresh and maintain regional business environment intelligence files. Each region has a domain config (scope, queries, advisory context) and a `business-environment.md` output that business skills consume when working with clients in that region.
