---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Spiced Discovery — BOB Workflow
  description: SPICED Discovery
  socialImage: https://img.youtube.com/vi/exV5Mc8f_UQ/maxresdefault.jpg
skillName: pb-spiced-discovery
youtubeId: exV5Mc8f_UQ
published: '2026-08-01'
privacy: public
title: SPICED Discovery
thumbnail: https://img.youtube.com/vi/exV5Mc8f_UQ/maxresdefault.jpg
subtitle: Complete SPICED profile (Situation, Pain, Impact, Critical Event, Decision) documented, deal qualified, and next action agreed
inputs:
- label: Prospect company name and URL
  icon: 🏢
- label: Contact name and role
  icon: 👤
- label: How the lead was sourced (referral, inbound, outbound)
  icon: 📋
- label: Available meeting notes, emails, or prior context
  icon: 📧
- label: Call duration (to calibrate question bank depth)
  icon: 🎙️
outputs:
- label: Question Bank.md
  icon: 📋
- label: Decision-Maker Map.md
  icon: 🗺️
- label: SPICED Profile.md
  icon: 📋
- label: Qualification Scorecard.md
  icon: 📊
- label: Executive Brief.md
  icon: 📋
steps:
- label: research-company → gather company intelligence, financials, recent news, tech stack
  actor: agent
- label: decision-maker-mapper → map buying committee, identify likely champion and economic buyer
  actor: agent
- label: consultative-selling → generate SPICED-structured discovery question bank tailored to prospect's industry and situation
  actor: agent
- label: Review question bank, prioritize questions for call time available, note pre-call hypotheses
  actor: human
- label: 'Conduct discovery call using SPICED flow: Situation → Pain → Impact → Critical Event → Decision'
  actor: human
- label: meeting-intelligence → extract SPICED components, decisions, and action items from call notes or transcript
  actor: agent
- label: consultative-selling → score deal using SPICED scorecard, generate diagnostic brief or executive brief based on findings
  actor: agent
- label: 'Review qualification score, decide next action: propose, nurture, or disqualify'
  actor: human
trigger: '"Discovery call scheduled with a prospect — need structured preparation and a buyer-centric discovery framework"'
timeSavings: 'Typical run: 2-4 hours across pre-call prep, call, and post-call documentation'
compounding: Each run refines templates and context — 5 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'Discovery call tomorrow.

  You''ll wing it, like last time.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Complete SPICED profile (Situation, Pain, Impact, Critical Event, Decision) documented, deal qualified, and next action agreed


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.
