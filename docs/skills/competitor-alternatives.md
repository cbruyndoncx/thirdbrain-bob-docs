---
description: Expert guidance for creating competitor comparison and alternative pages. Build pages that rank for competitive search terms, provide genuine value to evaluators, and position products effectively.
title: competitor-alternatives
---

# competitor-alternatives

Expert guidance for creating competitor comparison and alternative pages. Build pages that rank for competitive search terms, provide genuine value to evaluators, and position products effectively.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing strategy |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Head of Sales] |

Creates competitor comparison pages, researches competitor features, generates comparison tables, writes persuasive alternative content.

## How you ask

- “Create a comparison page: Our Product vs Competitor X”
- “Research competitor features and build a comparison table”
- “Write an alternatives page targeting 'Competitor X alternatives'”
- “Generate a competitive landing page for our vs page”

## Inputs

- client-icp — Client ICP for client-scoped comparison pages.
- client-offerings — Client offerings for client-scoped comparison pages.
- client-profile — Client profile for client-scoped comparison pages.
- marketing_context — Positioning and messaging context.
- profile — Business model, product overview
- offerings — Products, pricing
- icp — Target audience
- marketing-context — Positioning, differentiation, competitors
- request — The page format wanted (alternative, alternatives, vs, or competitor vs competitor) and the competitors to cover
- scope — `company`, or a client-id under `client.root` — a string with one reserved value, not a closed set

## Outputs

- alternative-page (markdown)
- alternatives-page (markdown)
- competitor-data (yaml)
- competitor-hub (markdown)
- competitor-page-plan (markdown)
- prefer a permanent directory)
- temporary-competitor-page (markdown)
- vs-page (markdown)
- {scope.marketing}/competitor-pages/alternatives/{competitor}-alternative.md
- {scope.marketing}/competitor-pages/alternatives/{competitor}-alternatives.md
- {scope.marketing}/competitor-pages/competitor-hub.md
- {scope.marketing}/competitor-pages/competitor-page-plan.md
- {scope.marketing}/competitor-pages/competitors/{slug}.yaml
- {scope.marketing}/competitor-pages/vs/us-vs-{competitor}.md

