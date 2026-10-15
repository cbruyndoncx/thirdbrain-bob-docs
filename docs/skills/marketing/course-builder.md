---
description: Build a Skool-ready online course *from the owner's offer* — so every module sells the vault by mapping a buyer problem to a transformation.
title: course-builder
---

# course-builder

Build a Skool-ready online course *from the owner's offer* — so every module sells the vault by mapping a buyer problem to a transformation.

- **Area:** Marketing
- **Category:** marketing content
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Head of Marketing, Content Manager

Turns the owner's vault offer, ICP, and positioning context plus a course topic into a Skool-ready online course that sells the vault (BOB / ThirdBrain).

## How you ask

- “Build a course”
- “Design my Skool course”
- “Turn my offer into a course”

## Inputs

- topic — Course topic or working title the course should teach/sell
- offer — Canonical offer/pricing — the spine the course is built from (`company.offerings`, or `company.products` per-product)
- icp — Ideal customer profile — drives problem/objection mapping
- positioning — Positioning + tone the course voice must follow (`company.marketing-context`, `company.brand`)
- module — Module number/name from the approved architecture
- architecture — The approved course architecture note this module belongs to
- module — Approved module to write lessons for
- module_notes — The module-notes working sheet produced by module-notes route
- course-id — The course folder/id under `{company.marketing.skool-courseware}`

## Outputs

- architecture (markdown)
- courseware (markdown)
- lessons (markdown)
- module_notes (markdown)
- {company.marketing.skool-courseware}/{course-id}/module-{n}-lessons.md
- {company.marketing.skool-courseware}/{course-id}/module-{n}-notes.md
- {company.marketing.skool-courseware}/{course-id}/{course-id}.md

