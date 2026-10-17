---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Hire To Productivity — Hire-to-Productivity
  description: Hire-to-Productivity
  socialImage: https://img.youtube.com/vi/n8-Fh1O1YYw/maxresdefault.jpg
skillName: pb-hire-to-productivity
youtubeId: n8-Fh1O1YYw
published: '2026-08-01'
privacy: public
title: Hire-to-Productivity
thumbnail: https://img.youtube.com/vi/n8-Fh1O1YYw/maxresdefault.jpg
subtitle: Right person hired, onboarded, and productive within 90 days
inputs:
- label: Role title and team it belongs to
  icon: 📋
- label: Why the hire is needed (growth, replacement, new capability)
  icon: 📋
- label: Budget / compensation range
  icon: 💰
- label: Timeline (when do you need someone started)
  icon: 📅
- label: Must-have vs nice-to-have skills
  icon: 📋
outputs:
- label: Role Definition.md
  icon: 📋
- label: Job Description.md
  icon: 📋
- label: Boolean Searches.md
  icon: 🔍
- label: Offer Letter.pdf
  icon: 📄
- label: 30/60/90 Plan.md
  icon: 🗺️
- label: Review Doc.md
  icon: 📋
steps:
- label: 'team-composition-analysis → define the role: responsibilities, skills needed, reporting line, success criteria'
  actor: agent
- label: hr-ops → create job description, choose sourcing channels, set interview process
  actor: agent
- label: Review JD and interview plan, begin sourcing
  actor: human
- label: linkedin-searches → build Boolean searches for candidate sourcing on LinkedIn
  actor: agent
- label: Interview candidates, check references, make offer
  actor: human
- label: employment-contract-templates → draft offer letter and employment contract
  actor: agent
trigger: '"Need to hire someone — new role, replacement, or capacity expansion"'
timeSavings: 'Typical run: Weeks to months — recruitment through first performance check'
compounding: Each run refines templates and context — 4 automated steps improve with accumulated data
frequency: Per new client
hook: 'You hired someone.

  Ninety days later they still aren''t productive.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: people
---

Right person hired, onboarded, and productive within 90 days


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.
