---
description: Run structured post-delivery satisfaction checks, collect NPS scores, prepare for renewal conversations, and build action plans when a client relationship is at risk. Keeps the deliver-to-satisfaction chain closed by ensuring each engagement has a documented satisfaction signal and a clear next step.
title: retention-check
---

# retention-check

Run structured post-delivery satisfaction checks, collect NPS scores, prepare for renewal conversations, and build action plans when a client relationship is at risk. Keeps the deliver-to-satisfaction chain closed by ensuring each engagement has a documented satisfaction signal and a clear next step.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Runs post-delivery satisfaction checks, collects NPS scores, and builds recovery plans for at-risk clients.

## How you ask

- “Post-delivery satisfaction”
- “Renewal conversation”
- “Recovery action plan”

## Inputs

- client-id — Client identifier for vault path resolution
- project-context — Recent delivery context from the client project folder (`client.root`).
- contact-details — Who to contact (`client.contacts`).
- client-profile — Client relationship baseline used to frame the renewal case.
- company-profile — Own-company context used to position the renewal offer.
- project-context — Engagement history from the client project folder (`client.root`).
- satisfaction-records — Prior satisfaction scores (`client.feedback`).
- satisfaction-record — Most recent satisfaction record with low score (`client.feedback`); absent when the trigger is silence, a complaint, or an invoice or scope dispute.

## Outputs

- recovery-plan (markdown)
- renewal-brief (markdown)
- satisfaction-record (markdown)
- {client.deals}/renewal_brief_{YYYY-MM-DD}.md
- {client.feedback}/recovery_plan_{YYYY-MM-DD}.md
- {client.feedback}/satisfaction_{YYYY-MM-DD}.md

