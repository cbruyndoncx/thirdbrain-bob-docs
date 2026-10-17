---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Solo Weekly Operating System — BOB Workflow
  description: Solo Weekly Operating System
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-solo-weekly-operating-system
youtubeId: ''
published: ''
privacy: unlisted
title: Solo Weekly Operating System
thumbnail: ''
subtitle: Weekly Cadence for Solo Operators
inputs:
- label: inbox
  icon: 📬
- label: pipeline-data
  icon: 📊
- label: calendar
  icon: 📅
outputs:
- label: triaged_inbox.md
  icon: 📬
- label: weekly_focus.md
  icon: 🎯
- label: linkedin_post.md
  icon: 📝
steps:
- email-triage → classify inbox
- crm-pipeline → deals and follow-ups
- booking-scheduler → meeting prep
- label: Set weekly focus (max 3)
  actor: human
- social-content → draft visibility post
trigger: '"Run my weekly system" or every Monday'
timeSavings: ~3 hrs Monday admin → ~30 min automated
compounding: Pipeline discipline compounds — nothing falls through the cracks
frequency: Weekly
hook: 'No team. No manager.

  Just you, and whatever you remember to do.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: strategy
---


