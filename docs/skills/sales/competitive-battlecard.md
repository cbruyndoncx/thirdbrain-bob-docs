---
description: Generate structured competitive battlecards — concise, scannable quick-reference documents that sales teams use mid-conversation to position against a specific competitor.
title: competitive-battlecard
---

# competitive-battlecard

Generate structured competitive battlecards — concise, scannable quick-reference documents that sales teams use mid-conversation to position against a specific competitor.

- **Area:** Sales & Clients
- **Category:** sales
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Sales

Generates structured competitive battlecards for sales teams.

## How you ask

- “Create a battlecard for competing against HubSpot”
- “Build a competitive cheat sheet: us vs Salesforce”
- “Battlecard comparing us against HubSpot, Pipedrive, and Freshsales”
- “Update the Salesforce battlecard with their new pricing”

## Inputs

- competitor — Competitor name or URL
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
- icp — ICP to frame why we win vs this competitor.
- marketing-context — Positioning context for differentiation framing.
- offerings — Offerings for feature/price comparison.
- profile — Company or client profile for identity and credibility.
- competitors — List of competitor names or URLs
- icp — ICP to frame why we win vs these competitors.

## Outputs

- battlecard (markdown)
- client-output-artifact (markdown)
- {client.sales}/battlecards/{competitor-slug}.md
- {company.sales}/battlecards/overview_{date}.md
- {company.sales}/battlecards/{competitor-slug}.md

