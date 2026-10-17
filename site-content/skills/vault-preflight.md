---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: vault-preflight — ThirdBrain BOB skill
  description: Validate vault context completeness before starting workflows. This skill checks that required files and information exist for different types of work.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: vault-preflight
catLabel: utilities
area: foundational
desc: Checks whether vault context is complete before a workflow runs — reports missing context files and readiness gaps for company, client, marketing or lead-generation work.
summary: Validate vault context completeness before starting workflows. This skill checks that required files and information exist for different types of work.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- marketing_context — Positioning, narrative and competitive frame.
- tone_of_voice — Brand voice the outbound copy must match.
- channels — Per-channel notes (LinkedIn, Substack, etc.) describing where output goes.
- scope — `company`, or a client-id (`client.root`)
- company_marketing_context — Marketing context note checked by the marketing readiness section.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id (`client.root`) — a string with one reserved value, not a closed set
outputs:
- lead-gen-readiness (markdown)
- prefer a permanent directory)
- vault-preflight (markdown)
prompts:
- Check if my vault is ready for a marketing workflow
- What context files are missing before I start?
- Run a preflight check for client deliverable creation
- Validate vault context completeness for this project
---
