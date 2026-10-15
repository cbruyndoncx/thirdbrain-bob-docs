---
description: Use this skill to choose the right PM workflow, run it with the minimum required inputs, and return a concrete artifact rather than generic PM advice.
title: product-manager-toolkit
---

# product-manager-toolkit

Use this skill to choose the right PM workflow, run it with the minimum required inputs, and return a concrete artifact rather than generic PM advice.

| | |
|---|---|
| **Area** | Strategy |
| **Category** | product management |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Product Manager] |

Full PM workflow toolkit — PRD templates, customer interview analysis, product roadmaps, and discovery frameworks.

## How you ask

- “Prioritize these features using RICE scoring”
- “Generate a PRD template for our new feature”
- “Analyze these customer interview transcripts for patterns”
- “Build a product roadmap from our discovery findings”

## Inputs

- transcript — Interview transcript or call notes — needed only for customer discovery
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set

## Outputs

- product-manager-toolkit (markdown)
- {scope.knowledge-base.product}/product-manager-toolkit-{YYYY-MM-DD}.md

