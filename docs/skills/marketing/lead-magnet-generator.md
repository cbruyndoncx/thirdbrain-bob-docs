---
description: 'Target audience: anyone who needs a gated asset that earns an email address, and the posts that make people want it.'
title: lead-magnet-generator
---

# lead-magnet-generator

Target audience: anyone who needs a gated asset that earns an email address, and the posts that make people want it.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Turns a topic into a downloadable lead magnet — guide, checklist, template, or toolkit — plus three promotion posts written from distinct angles (contrarian, pain-first,…

## How you ask

- “Turn this topic into a lead magnet with promotion posts”
- “Make a checklist we can gate for email capture”
- “Write three LinkedIn angles for our existing pricing guide”
- “We need a downloadable template for fit-out contractors”

## Inputs

- topic — The subject of the magnet; may come from a trend pipeline
- format — guide, checklist, template, or toolkit; inferred from the topic when omitted
- scope — `company` (default), or a client-id under {company.clients}/ when the magnet markets a client's business; decides the output folder
- icp — ICP — who the magnet is for
- tone-of-voice — Tone of voice — keeps the posts on-brand
- topic — The subject of the magnet
- format — guide, checklist, template, or toolkit
- magnet — Path to the existing lead magnet

## Outputs

- lead-magnet (markdown)
- promotion-posts (markdown)
- {scope.marketing.lead-magnets}/{slug}/promotion-{slug}.md
- {scope.marketing.lead-magnets}/{slug}/{slug}.md

