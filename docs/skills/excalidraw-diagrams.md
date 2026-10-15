---
description: Create flowcharts, architecture diagrams, mind maps, timelines, and other visual diagrams from text content. Outputs Obsidian-ready `.md` files that render directly in the Excalidraw plugin.
title: excalidraw-diagrams
---

# excalidraw-diagrams

Create flowcharts, architecture diagrams, mind maps, timelines, and other visual diagrams from text content. Outputs Obsidian-ready `.md` files that render directly in the Excalidraw plugin.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | diagramming |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | diagram |
| **Setup** | [none] |
| **Roles** | [] |

Creates flowcharts, architecture diagrams, and visual concepts as Obsidian- ready Excalidraw `.md` files.

## How you ask

- “Draw an architecture diagram for our API in Excalidraw”
- “Create a flowchart showing the user registration process”
- “Sketch a system overview diagram as an Excalidraw file”
- “Visualize our data pipeline as an Excalidraw diagram”

## Inputs

- request — The content or structure to visualize, plus any size, readability, or styling constraint the layout has to respect.
- diagram-type — Visual form to build. Left unset, the route picks the form that fits the relationships in the content; naming one overrides that choice and is what to do when the reader expects a specific shape. (flowchart | mind-map | hierarchy | relationship | comparison | timeline | matrix | freeform)
- output-path — Destination the caller names for the generated note. Left unset, the file is written under the default output location using the `[topic].[diagram-type].md` naming rule.
- diagram-file — Excalidraw note to modify, read back so existing element ids, group ids and container bindings survive the edit instead of being regenerated.
- request — The structural change to make, stated as elements and relationships rather than coordinates, so the route can re-derive the layout.
- diagram-file — Excalidraw note to check against the Validation Checklist and the `check_overlap.py` bounding-box preflight.
- request — The reported symptom — what fails to render, or where the layout looks wrong — used to order the checks so the likely cause is tested first.

## Outputs

- Obsidian-ready Excalidraw note — plugin frontmatter, the required warning banner, an empty Text Elements section, and the drawing JSON inside `%%` markers.
- Per-check result against the Validation Checklist plus the overlap preflight output, including the SKIPPED-with-exit-2 case for a compressed-json drawing.
- Updated Excalidraw note with the requested change applied and every unchanged relationship, label and binding carried over.
- prefer a permanent directory)

