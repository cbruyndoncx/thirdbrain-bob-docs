---
title: Customer Vault Installation — get a client live on BOB
---

# Customer Vault Installation — get a client live on BOB

*Customer has a working BOB vault on their machine, opened in Obsidian, with first daily note and TaskNote created*

<div class="video-wrap"><iframe width="100%" height="420" src="https://www.youtube.com/embed/oDmRAyijRHs?rel=0" title="Customer Vault Installation — get a client live on BOB" frameborder="0" allowfullscreen loading="lazy"></iframe></div>

> They bought it.
> Now it has to actually run on their machine.

- **Area:** Sales & Clients
- **Time savings:** Typical run: 60–90 min (mostly synchronous with customer)
- **Try it:** "New customer ready to receive their BOB vault — release package available, customer scheduled for install session"
- **Compounding:** Each run refines templates and context — 6 automated steps improve with accumulated data
- **Frequency:** Per new client
- **Published:** 2026-06-29

## Inputs

- 🏢 Customer name and client_id
- 👤 Release package name and version
- 📋 Customer OS (Mac / Windows / Linux)
- 📋 Customer Obsidian version
- 📁 Whether customer needs Google Workspace integration
- 📅 Install session date/time and channel

## What BOB does

1. create-client → set up customer record in support staff's vault (`30-CLIENTS/{client-id}/`) with profile, install date, package version
2. vault-intro → generate a customer-tailored install briefing: what they're getting, what to expect, prerequisites checklist
3. technical-writing → produce the install runbook: step-by-step commands for the customer's OS, screenshots placeholders, common gotchas
4. Pre-flight check with customer (5 min before scheduled session) — confirm Obsidian installed, Python available, release zip received and unzipped
5. Live install session — share screen with customer, walk them through each step from the runbook. They execute on their machine; support staff observes and corrects
6. meeting-intelligence → capture install session notes: what was installed, customer's environment specifics, any deviations from runbook, customer questions surfaced
7. technical-writing → document the install in customer's record (`30-CLIENTS/{client-id}/00-PROFILE/install-record.md`): versions, config choices, gotchas hit, fixes applied
8. tasknotes → schedule first support check-in (24–48h post-install) and log any open follow-ups from the session

## Outputs

- 🏢 Customer profile (from create-client)
- 📋 Install Briefing.md (step 2 — sent to customer in advance)
- 📋 Install Runbook.md (step 3 — used live during session)
- 🎙️ Install Session Notes.md (step 7 — captured during call)
- 📋 install-record.md (step 8 — permanent record of what was installed and how)
- 📅 Follow-up TaskNote scheduled (step 9)

