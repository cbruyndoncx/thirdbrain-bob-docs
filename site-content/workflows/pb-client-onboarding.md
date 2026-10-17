---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Client Onboarding — New client signed
  description: New client signed.
  socialImage: https://img.youtube.com/vi/qP4_FAEwLLI/maxresdefault.jpg
skillName: pb-client-onboarding
youtubeId: qP4_FAEwLLI
published: '2026-07-01'
privacy: public
title: New client signed.
thumbnail: https://img.youtube.com/vi/qP4_FAEwLLI/maxresdefault.jpg
subtitle: Client workspace ready with initial business map and a region-grounded operating-environment briefing
inputs:
- label: Client name + industry
  icon: 🏢
- label: Website URL
  icon: 🔗
- label: Key contacts
  icon: 👤
- label: Engagement scope
  icon: 📋
- label: Operating region(s)
  icon: 🌍
outputs:
- label: Workspace folders
  icon: 📁
- label: Client profile (+regions)
  icon: 🪪
- label: Business map (3-layer)
  icon: 🗺️
- label: Context completeness report
  icon: ✅
- label: Operating Environment briefing
  icon: 📑
steps:
- label: regional-context → confirm the client's region KB is fresh
  actor: agent
- label: create-client → set up workspace folders + profile, capture regions
  actor: agent
- label: Review client profile, add details, confirm regions
  actor: human
- label: business-baseline → business map with Three-Layer Context (World→Country→Industry)
  actor: agent
- label: Review business map, flag corrections
  actor: human
- label: vault-preflight → verify context + region KB freshness
  actor: agent
- label: Deliver 'Your Operating Environment Right Now' briefing
  actor: human
trigger: '"New client signed"'
timeSavings: ~4 hrs manual → ~1 hr automated (4× faster)
compounding: Each onboarding builds reusable templates and baseline data
frequency: Per new client
hook: 'New client signed.

  Now what? Scattered notes, missing context, slow start.'
outcome: Workspace set up, profile built, business map started — before the first real meeting.
benefits:
- 4× faster
- Nothing gets missed
- Baseline context from day one
cta: Onboard your next client in 1 hour
category: ''
filterGroup: sales
area: sales
---

New client signed.

Workspace set up, profile built, business map started — before the first real meeting.
