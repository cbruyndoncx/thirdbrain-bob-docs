---
description: Prepare, conduct, and debrief coaching discovery sessions that may lead to a paid coaching, advisory, or hybrid coaching-plus-consulting engagement.
title: coaching-discovery
---

# coaching-discovery

Prepare, conduct, and debrief coaching discovery sessions that may lead to a paid coaching, advisory, or hybrid coaching-plus-consulting engagement.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Sales

ICF-informed coaching discovery and conversion workflow for coaches, advisors, and consultants.

## How you ask

- “Prep me for tomorrow's call — Abbas sent a CEO from a fintech, 35M revenue, mentioned founder burnout”
- “Debrief yesterday's discovery — here are my notes [paste]”
- “Is this coaching or consulting? Here's what they said: [paste]”
- “Design a hybrid engagement for [lead] based on the debrief”
- “Draft the follow-up — strong fit”

## Inputs

- prospect_context — What is known: referrer, role, company, public context, prior notes
- offerings — Offerings catalogue used to shape the conversion path and boundary script.
- prep_ref — Path to the prep output to load context from
- session_notes — Notes or transcript from the discovery call
- lead_id — Lead identifier under the leads folder (`company.leads`)
- lead_id — Lead identifier
- debrief_ref — Path to the debrief that this design follows from
- referrer — Name or role of the person who made the introduction

## Outputs

- discovery-debrief (markdown)
- discovery-prep (markdown)
- hybrid-design (markdown)
- live-guide (markdown)
- referral-analysis (markdown)
- {lead.root}/discovery_debrief_{YYYY-MM-DD}.md
- {lead.root}/discovery_prep_{YYYY-MM-DD}.md
- {lead.root}/hybrid_design_{YYYY-MM-DD}.md
- {lead.root}/referral_analysis_{YYYY-MM-DD}.md
- {me.inbox}/live_guide_{YYYY-MM-DD}.md

