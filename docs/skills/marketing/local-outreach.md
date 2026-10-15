---
description: Build local relationships that generate customers through community presence, in-person networking, and hyper-local digital engagement.
title: local-outreach
---

# local-outreach

Build local relationships that generate customers through community presence, in-person networking, and hyper-local digital engagement.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing

Creates local relationship-building strategies for customer acquisition.

## How you ask

- “Create a local networking strategy for our consulting firm”
- “Draft a chamber of commerce introduction script”
- “Plan community outreach for our new co-working space”
- “Generate engagement templates for local Facebook groups”

## Inputs

- icp — Ideal customer profile — who the output targets.
- profile — Company or client profile — entity and relationship context.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- local-outreach (markdown)
- local-outreach-company (markdown)
- {client.marketing}/local-outreach/local-outreach-{YYYY-MM-DD}.md
- {company.marketing}/local-outreach/local-outreach-{YYYY-MM-DD}.md

