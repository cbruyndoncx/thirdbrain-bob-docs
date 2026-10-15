---
description: Design business models with the lightest canvas that still captures the strategic and commercial logic. Use this skill to choose the right canvas, fill it with specific answers, surface the assumptions that matter most, and prepare a review-ready business model document.
title: business-model-canvas
---

# business-model-canvas

Design business models with the lightest canvas that still captures the strategic and commercial logic. Use this skill to choose the right canvas, fill it with specific answers, surface the assumptions that matter most, and prepare a review-ready business model document.

- **Area:** Strategy
- **Category:** product management
- **Level:** beginner
- **Input:** conversation
- **Output:** diagram
- **Setup:** none
- **Roles:** CEO / Founder, Product Manager

Designs business models with Business Model Canvas, Lean Canvas, and Startup Canvas.

## How you ask

- “Create a Business Model Canvas for our marketplace idea”
- “Design a Lean Canvas for our SaaS startup”
- “Map how our business creates, delivers, and captures value”
- “Compare two business model options side by side”

## Inputs

- request — What canvas to produce and the decision it needs to support.
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- profile — Company or client profile — identity and stage the canvas has to stay consistent with.
- icp — ICP used to anchor the customer segment and value proposition sections.
- offerings — Existing offerings catalogue the canvas either describes or proposes changing.
- marketing-context — Positioning and competitive frame the value proposition and channels must stay aligned with.
- request — The idea, target segment, and problem space to canvas, since there is no vault profile to read it from.

## Outputs

- Completed canvas with the chosen framework's sections filled, a ranked assumptions list, and validation experiments.
- Draft canvas with visible assumptions and immediate validation experiments, delivered in conversation since no vault context exists to file it under.
- {scope.knowledge-base.product}/business-model-canvas-{YYYY-MM-DD}.md

