---
layout: workflow-detail.njk
bodyClasses: workflow-detail
seo:
  title: Customer Vault Installation
  description: Customer Vault Installation — get a client live on BOB
  socialImage: https://img.youtube.com/vi/oDmRAyijRHs/maxresdefault.jpg
skillName: pb-customer-vault-installation
youtubeId: oDmRAyijRHs
published: '2026-06-29'
privacy: public
title: Customer Vault Installation — get a client live on BOB
thumbnail: https://img.youtube.com/vi/oDmRAyijRHs/maxresdefault.jpg
subtitle: Customer has a working BOB vault on their machine, opened in Obsidian, with first daily note and TaskNote created
inputs:
- label: Customer name and client_id
  icon: 🏢
- label: Release package name and version
  icon: 👤
- label: Customer OS (Mac / Windows / Linux)
  icon: 📋
- label: Customer Obsidian version
  icon: 📋
- label: Whether customer needs Google Workspace integration
  icon: 📁
- label: Install session date/time and channel
  icon: 📅
outputs:
- label: Customer profile (from create-client)
  icon: 🏢
- label: Install Briefing.md (step 2 — sent to customer in advance)
  icon: 📋
- label: Install Runbook.md (step 3 — used live during session)
  icon: 📋
- label: Install Session Notes.md (step 7 — captured during call)
  icon: 🎙️
- label: install-record.md (step 8 — permanent record of what was installed and how)
  icon: 📋
- label: Follow-up TaskNote scheduled (step 9)
  icon: 📅
steps:
- label: create-client → set up customer record in support staff's vault (`30-CLIENTS/{client-id}/`) with profile, install date, package version
  actor: agent
- label: 'vault-intro → generate a customer-tailored install briefing: what they''re getting, what to expect, prerequisites checklist'
  actor: agent
- label: 'technical-writing → produce the install runbook: step-by-step commands for the customer''s OS, screenshots placeholders, common gotchas'
  actor: agent
- label: Pre-flight check with customer (5 min before scheduled session) — confirm Obsidian installed, Python available, release zip received and unzipped
  actor: human
- label: Live install session — share screen with customer, walk them through each step from the runbook. They execute on their machine; support staff observes and corrects
  actor: human
- label: 'meeting-intelligence → capture install session notes: what was installed, customer''s environment specifics, any deviations from runbook, customer questions surfaced'
  actor: agent
- label: 'technical-writing → document the install in customer''s record (`30-CLIENTS/{client-id}/00-PROFILE/install-record.md`): versions, config choices, gotchas hit, fixes applied'
  actor: agent
- label: tasknotes → schedule first support check-in (24–48h post-install) and log any open follow-ups from the session
  actor: agent
trigger: '"New customer ready to receive their BOB vault — release package available, customer scheduled for install session"'
timeSavings: 'Typical run: 60–90 min (mostly synchronous with customer)'
compounding: Each run refines templates and context — 6 automated steps improve with accumulated data
frequency: Per new client
hook: 'They bought it.

  Now it has to actually run on their machine.'
outcome: ''
benefits: []
cta: ''
category: ''
filterGroup: strategy
area: sales
---

Takes a customer from package to a working vault — briefing, runbook, live install session, permanent record.

More at brn.cx
