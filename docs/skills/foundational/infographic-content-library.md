---
description: Organizes visual content libraries with naming conventions, README navigation indexes, SEMANTIC-GRAPH documentation, slide mosaics and curated guides. Use when the user wants an asset catalog, image library documentation, a slide preview or a themed collection of graphics. This is the visual asset library methodology.
title: infographic-content-library
---

# infographic-content-library

Organizes visual content libraries with naming conventions, README navigation indexes, SEMANTIC-GRAPH documentation, slide mosaics and curated guides. Use when the user wants an asset catalog, image library documentation, a slide preview or a themed collection of graphics. This is the visual asset library methodology.

- **Area:** Foundational
- **Category:** diagramming
- **Level:** beginner
- **Input:** conversation
- **Output:** diagram
- **Setup:** none
- **Roles:** 

Organizes visual content libraries with naming conventions, README navigation indexes, SEMANTIC-GRAPH documentation, slide mosaics and curated guides.

## How you ask

- “Organize my infographic assets into a catalogued library”
- “Create an asset index for our visual content collection”
- “Maintain naming conventions across our image library”

## Inputs

- folder — Content folder being documented; may already contain source assets (PDF, infographic image, slide deck) to reference.
- request — Which documentation artifact to produce — README.md, SEMANTIC-GRAPH.md, or both — and any content specifics to reflect.
- folder — Content folder holding the source slide PDF; the mosaic is generated from its slides and embedded back into the folder's README.
- request — Any non-default mosaic parameters (grid size, DPI, thumbnail padding) — defaults are a 4-column tile (rows grow with slide count) at 100 DPI with 300px thumbnails.
- folder — Destination under curated-guides/ (or an existing guide folder) where the curated collection is written.
- request — The theme and the 3+ related content pieces to link into the guide, with the focus each contributes.
- folder — Content folder or curated guide holding the artifact under review.
- request — Which artifact to review (README, SEMANTIC-GRAPH, slide mosaic, or curated guide) and whether STRICT REVIEW fault-finding applies.

## Outputs

- Curated-guide README.md, written into the guide folder so its relative links to the content folders resolve, (and optional CONTENT.md) linking 3+ related content pieces under a shared theme, with use cases and statistics.
- README.md written into the content folder itself, so its relative links (./infographic.jpg, ./slides.pdf) resolve against the folder's real assets.
- Review Report with pass/fail status against the applicable checklist (README, SEMANTIC-GRAPH, slide mosaic, or curated guide).
- SEMANTIC-GRAPH.md written next to the README in the content folder, per the two-file documentation pattern.
- Slide preview grid embedded in the folder's README and linked to the source PDF.
- prefer a permanent directory)
- {folder}/README.md
- {folder}/SEMANTIC-GRAPH.md
- {folder}/slides_mosaic.png

