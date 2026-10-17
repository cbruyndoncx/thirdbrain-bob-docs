---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: course-builder — ThirdBrain BOB skill
  description: Build a Skool-ready online course *from the owner's offer* — so every module sells the vault by mapping a buyer problem to a transformation.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: course-builder
catLabel: marketing-content
area: marketing
desc: Turns the owner's vault offer, ICP, and positioning context plus a course topic into a Skool-ready online course that sells the vault (BOB / ThirdBrain).
summary: Build a Skool-ready online course *from the owner's offer* — so every module sells the vault by mapping a buyer problem to a transformation.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- topic — Course topic or working title the course should teach/sell
- offer — Canonical offer/pricing — the spine the course is built from (`company.offerings`, or `company.products` per-product)
- icp — Ideal customer profile — drives problem/objection mapping
- positioning — Positioning + tone the course voice must follow (`company.marketing-context`, `company.brand`)
- module — Module number/name from the approved architecture
- architecture — The approved course architecture note this module belongs to
- module — Approved module to write lessons for
- module_notes — The module-notes working sheet produced by module-notes route
- course-id — The course folder/id under `{company.marketing.skool-courseware}`
outputs:
- architecture (markdown)
- courseware (markdown)
- lessons (markdown)
- module_notes (markdown)
- '{company.marketing.skool-courseware}/{course-id}/module-{n}-lessons.md'
- '{company.marketing.skool-courseware}/{course-id}/module-{n}-notes.md'
- '{company.marketing.skool-courseware}/{course-id}/{course-id}.md'
prompts:
- Build a course
- Design my Skool course
- Turn my offer into a course
---
