---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: json-canvas — ThirdBrain BOB skill
  description: This skill enables skills-compatible agents to create and edit valid JSON Canvas files (`.canvas`) used in Obsidian and other applications.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: json-canvas
catLabel: obsidian
area: foundational
desc: Creates and edits JSON Canvas files (.canvas) with nodes, edges, groups, and connections.
summary: This skill enables skills-compatible agents to create and edit valid JSON Canvas files (`.canvas`) used in Obsidian and other applications.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — The structure to lay out and any layout constraint that binds it — orientation, grouping, colour meaning, or viewport size.
- structure-type — Layout family to build. Left unset, the route infers it from the relationships described; naming one fixes the grid and edge conventions up front. (flowchart | map | board | dependency-graph | freeform)
- node-sources — Vault note paths and external URLs to render as `file` and `link` nodes instead of text nodes, so the canvas points at live content rather than copying it.
- output-path — Destination the caller names for the `.canvas` file. Left unset, the canvas is returned inline and written to the default output location.
- canvas-file — Canvas to modify, read back so existing node ids, file-node paths and group boundaries are preserved rather than regenerated.
- request — The change to make, naming which nodes or edges are added, updated, or removed so the patch scope can be reported back.
- canvas-file — Canvas to check against the Validation Rules and the `autosize_canvas.py` loop. The route runs against any canvas, including one this skill did not create.
- request — The reported symptom — which boxes are unreadable, which edges look wrong — used to order the checks so the likely cause is tested first.
- apply-fixes — Whether to let `autosize_canvas.py --apply` write the resize and overlap fixes back to the file (keeping a `.bak`) rather than only reporting them.
outputs:
- Patched canvas with the named nodes and edges changed, every untouched file-node path and group boundary intact, and boxes re-sized to the new content.
- Valid JSON Canvas document — `nodes` and `edges` arrays with unique ids, resolved edge references, and node boxes sized to their content.
- either "Verification passed" or the nodes still undersized or overlapping.
- prefer a permanent directory)
prompts:
- Create a JSON Canvas file with connected nodes
- Build a visual mind map as a .canvas file
- Edit this canvas file to add a new group of nodes
---
