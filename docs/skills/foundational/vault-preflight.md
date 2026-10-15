---
description: Validate vault context completeness before starting workflows. This skill checks that required files and information exist for different types of work.
title: vault-preflight
---

# vault-preflight

Validate vault context completeness before starting workflows. This skill checks that required files and information exist for different types of work.

- **Area:** Foundational
- **Category:** utilities
- **Level:** intermediate
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Checks whether vault context is complete before a workflow runs — reports missing context files and readiness gaps for company, client, marketing or lead-generation work.

## How you ask

- “Check if my vault is ready for a marketing workflow”
- “What context files are missing before I start?”
- “Run a preflight check for client deliverable creation”
- “Validate vault context completeness for this project”

## Inputs

- marketing_context — Positioning, narrative and competitive frame.
- tone_of_voice — Brand voice the outbound copy must match.
- channels — Per-channel notes (LinkedIn, Substack, etc.) describing where output goes.
- scope — `company`, or a client-id (`client.root`)
- company_marketing_context — Marketing context note checked by the marketing readiness section.
- region-context — Regional business environment for the target market — Three-Layer Context layer 2; produced by `regional-context`.
- request — What to produce
- scope — `company`, or a client-id (`client.root`) — a string with one reserved value, not a closed set

## Outputs

- lead-gen-readiness (markdown)
- prefer a permanent directory)
- vault-preflight (markdown)

