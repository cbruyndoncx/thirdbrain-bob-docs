---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: paperbanana-lite — ThirdBrain BOB skill
  description: Generate publication-quality academic illustrations using a multi-agent Gemini pipeline via a single-file script.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: paperbanana-lite
catLabel: diagramming
area: foundational
desc: Generates publication-quality academic methodology diagrams, charts, graphs, visualizations, and statistical plots using a multi-agent Gemini pipeline.
summary: Generate publication-quality academic illustrations using a multi-agent Gemini pipeline via a single-file script.
difficulty: advanced
inputType: conversation
outputType: diagram
requires: '[api-key]'
roles: '[]'
inputs:
- target_dir — Where to store reference sets (documented default ~/.paperbanana/reference_sets)
- input — Text file with the methodology section (--input)
- caption — Figure caption (--caption)
- iterations — Refinement iterations (--iterations, default 3)
- data — JSON file with the raw data (--data)
- intent — Visual intent caption, including the chart form wanted (--intent)
- image_ref — Existing render to refine
- changes — What to change, stated as a delta from the current image
outputs:
- Final image in the timestamped run directory the script creates under --output-dir, next to planning.json and the iter_N files
- Final image of the new run directory; the prior run stays untouched for comparison
- prefer a permanent directory)
- setup-confirmation (markdown)
prompts:
- Generate a methodology diagram for my research paper
- Create a publication-quality chart from this data
- Build a statistical visualization for my thesis appendix
- Generate a figure for my manuscript showing the experimental pipeline
---
