---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Proposal From Meeting — The call went great
  description: The call went great.
  socialImage: https://img.youtube.com/vi/pWuipCZnWn8/maxresdefault.jpg
skillName: pb-proposal-from-meeting
youtubeId: pWuipCZnWn8
published: '2026-03-31'
privacy: public
title: The call went great.
thumbnail: https://img.youtube.com/vi/pWuipCZnWn8/maxresdefault.jpg
subtitle: Professional proposal ready to send
inputs:
- label: Meeting transcript or notes
  icon: 🎙️
- label: Client name
  icon: 👤
- label: Budget range (if discussed)
  icon: 💰
outputs:
- label: Extracted needs and action items
  icon: 📊
- label: Draft proposal
  icon: 📝
- label: Branded .docx proposal
  icon: 📄
steps:
- label: meeting-intelligence → extract decisions, needs, action items
  actor: agent
- label: Review extracted needs, confirm scope
  actor: human
- label: proposal-writer → draft proposal from findings
  actor: agent
- label: Review and adjust proposal
  actor: human
- label: docx-tools → generate branded .docx
  actor: agent
trigger: '"Discovery call or meeting just happened"'
timeSavings: ~3 hrs manual → ~30 min automated (6× faster)
compounding: Proposal templates improve with each iteration
frequency: Per sales meeting
hook: 'The call went great.

  Then three days passed before you sent the proposal.'
outcome: Meeting transcribed, needs extracted, branded proposal generated — same day.
benefits:
- 6× faster
- Key details captured automatically
- Proposals improve with each iteration
cta: Turn your next meeting into a proposal in 30 minutes
category: ''
filterGroup: sales
area: sales
---

The call went great.

Meeting transcribed, needs extracted, branded proposal generated — same day.
