---
description: Creates product strategies using where-to-play/how-to-win choices, beachhead market selection, and strategic canvas frameworks. Use when user mentions 'product strategy,' 'where to play,' 'beachhead market,' 'competitive positioning,' 'crossing the chasm,' 'strategic roadmap.'
title: strategy-frameworks
---

# strategy-frameworks

Creates product strategies using where-to-play/how-to-win choices, beachhead market selection, and strategic canvas frameworks. Use when user mentions 'product strategy,' 'where to play,' 'beachhead market,' 'competitive positioning,' 'crossing the chasm,' 'strategic roadmap.'

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder, Head of Marketing, Product Manager] |

Creates product strategies using where-to-play/how-to-win choices, beachhead market selection, and strategic canvas frameworks.

## How you ask

- “Create a product strategy using where-to-play/how-to-win”
- “Select our beachhead market for crossing the chasm”
- “Build a strategic canvas for competitive positioning”
- “Define our product strategy and strategic roadmap”

## Inputs

- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- strategy-frameworks (markdown)
- {scope.knowledge-base.product}/strategy-frameworks-{YYYY-MM-DD}.md

