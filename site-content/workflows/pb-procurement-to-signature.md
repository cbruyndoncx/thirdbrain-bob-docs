---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Procurement To Signature — BOB Workflow
  description: Procurement To Signature
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: pb-procurement-to-signature
youtubeId: ''
published: ''
privacy: unlisted
title: Procurement To Signature
thumbnail: ''
subtitle: Procurement, security, legal, and signature path made explicit, with owners, blockers, and deadlines tracked to completion
inputs: []
outputs:
- label: Procurement Path.md
  icon: 📁
- label: Security Review Tracker.md
  icon: 📋
- label: Legal Review Tracker.md
  icon: 📋
- label: Signature Readiness Checklist.md
  icon: 📋
steps:
- label: vault-preflight → confirm the deal, latest notes, and commercial context are loaded before running paper-process execution
  actor: agent
- label: MEDDPICC Qualification → extract paper process, decision process, procurement assumptions, and known blockers
  actor: agent
- label: decision-maker-mapper → confirm procurement, legal, and technical/security reviewers plus signer path where possible
  actor: agent
- label: negotiation → handle active commercial trade-offs that emerge during procurement or legal review without letting the paper process hide margin concessions
  actor: agent
- label: Update [[Mutual Action Plan]] with procurement, security, legal, and signature milestones so the close path remains visible
  actor: agent
- label: crm-pipeline → sync the highest-priority next action and due date back to the deal record
  actor: agent
trigger: '"The buyer wants to move forward, but procurement, security, legal, or signature process now controls the timeline"'
timeSavings: 'Typical run: 45-120 minutes to establish; ongoing updates through late-stage deal execution'
compounding: Each run refines templates and context — 6 automated steps improve with accumulated data
frequency: Per opportunity
hook: 'The buyer said yes.

  Procurement, security, and legal have not.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---


