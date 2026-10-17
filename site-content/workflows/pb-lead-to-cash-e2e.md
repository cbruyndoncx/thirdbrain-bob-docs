---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Lead To Cash E2E — Lead-to-Cash E2E
  description: Lead-to-Cash E2E
  socialImage: https://img.youtube.com/vi/88lrnBeUa1U/maxresdefault.jpg
skillName: pb-lead-to-cash-e2e
youtubeId: 88lrnBeUa1U
published: '2026-08-01'
privacy: public
title: Lead-to-Cash E2E
thumbnail: https://img.youtube.com/vi/88lrnBeUa1U/maxresdefault.jpg
subtitle: Lead converted, deal closed, work delivered, invoice paid, and margin reviewed
inputs:
- label: Lead source and initial contact information
  icon: 👤
- label: Product or service being sold
  icon: 📦
- label: Deal value estimate
  icon: 📋
- label: Timeline expectations
  icon: 📅
- label: Delivery scope (once deal closes)
  icon: 📋
outputs:
- label: Lead Scorecard.md
  icon: 📊
- label: Buying Committee.md
  icon: 📋
- label: Won Deal Record.md
  icon: 📋
- label: Client Workspace
  icon: 🏢
- label: Invoice.pdf
  icon: 📄
- label: AR Follow-up Log.md
  icon: 📋
steps:
- label: icp-discovery + lead-qualifier → identify if prospect matches ICP, score with BANT/MEDDIC
  actor: agent
- label: 'Review qualification and decide: pursue, nurture, or disqualify'
  actor: human
- label: research-company + prospect-audit → deep prospect research, score company fit
  actor: agent
- label: decision-maker-mapper → map buying committee and identify champion
  actor: agent
- label: proposal-writer → draft proposal from meeting notes and client intelligence
  actor: agent
- label: Review proposal, adjust pricing, send to prospect
  actor: human
- label: create-client → on deal won, set up client workspace with profile, contacts, project folders
  actor: agent
- label: invoice-description → generate invoice line items from completed work
  actor: agent
- label: Review and send invoice, track payment
  actor: human
- label: ar-followup → follow up on overdue invoices, escalate as needed
  actor: agent
trigger: '"New lead or prospect enters the pipeline — orchestrate the full journey to cash collected"'
timeSavings: 'Typical run: Weeks to months — runs across the full sales and delivery cycle'
compounding: Each run refines templates and context — 7 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'A lead came in.

  Somewhere between there and the invoice, it stalls.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Lead converted, deal closed, work delivered, invoice paid, and margin reviewed


This is an automated business workflow inside ThirdBrain BOB — the Business Operating Brain.
