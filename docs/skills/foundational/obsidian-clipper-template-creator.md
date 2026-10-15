---
description: Create, repair, and standardize templates for the Obsidian Web Clipper.
title: obsidian-clipper-template-creator
---

# obsidian-clipper-template-creator

Create, repair, and standardize templates for the Obsidian Web Clipper.

- **Area:** Foundational
- **Category:** obsidian
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** 

Creates importable templates for the Obsidian Web Clipper.

## How you ask

- “Create a web clipper template for saving articles”
- “Build a clipping template with custom frontmatter fields”
- “Fix my web clipper template — the CSS selectors aren't matching”

## Inputs

- url — Example page URL the template must parse
- url — Example page URL
- entity_type — Vault entity type the clipped note must validate against
- template — Existing clipper template that is mis-parsing
- url — Page it fails on, for reproduction

## Outputs

- clipper-template (json)
- prefer a permanent directory)
- repaired-template (json)

