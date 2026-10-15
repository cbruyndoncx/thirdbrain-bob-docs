---
description: Help users find the right marketing strategies from 139 proven approaches, matched to their stage, budget, and goals.
title: marketing-ideas
---

# marketing-ideas

Help users find the right marketing strategies from 139 proven approaches, matched to their stage, budget, and goals.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing strategy |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Creates marketing plans and recommends channel-specific tactics for SaaS products from a library of 139 proven strategies.

## How you ask

- “Give me marketing ideas for our B2B SaaS product”
- “What marketing channels should we prioritize with a $10K budget?”
- “Recommend tactics to promote our new consulting service”
- “Create a marketing plan for our product launch”

## Inputs

- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set

## Outputs

- marketing-ideas (markdown)
- marketing-ideas-company (markdown)
- {client.marketing}/strategy/marketing-ideas-{focus}.md
- {company.marketing}/strategy/marketing-ideas-{focus}.md

