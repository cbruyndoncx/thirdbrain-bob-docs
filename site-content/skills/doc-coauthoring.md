---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: doc-coauthoring — ThirdBrain BOB skill
  description: Act as an active guide, walking users through Context Gathering, Refinement & Structure, and Reader Testing.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: doc-coauthoring
catLabel: documents
area: foundational
desc: Guide users through a structured workflow for co-authoring documentation -- outline structure, draft sections, iterate on feedback, and refine language.
summary: Act as an active guide, walking users through Context Gathering, Refinement & Structure, and Reader Testing.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — The document to write -- type, purpose, and audience -- used to scope Stage 1 context gathering.
- template — Existing template or reference document the user has and wants the new draft's structure to follow.
- request — The revision goal -- what to tighten, restructure, or clarify in the existing draft.
- existing-draft — The draft to revise, read first so edits are targeted rather than a rewrite from scratch.
outputs:
- The existing draft with targeted revisions applied, without a full structural rebuild.
- The scaffolded, section-drafted, and reader-tested document produced across all three stages.
- prefer a permanent directory)
prompts:
- Help me draft a technical specification document
- Co-author a proposal document with me
- Help me write an RFC for our new authentication system
- Draft a design doc for the migration project
---
