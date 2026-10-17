---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: drawio — ThirdBrain BOB skill
  description: Create professional diagrams in Draw.io format with proper XML structure.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: drawio
catLabel: diagramming
area: foundational
desc: Creates, edits and exports Draw.io diagrams (.drawio files) — flowcharts, architecture and C4 diagrams, swimlane process flows, multi-page files — and renders them to…
summary: Create professional diagrams in Draw.io format with proper XML structure.
difficulty: beginner
inputType: conversation
outputType: diagram
requires: '[none]'
roles: '[]'
inputs:
- request — What to produce
- input — Source .drawio file
- pdf — Destination merged multi-page PDF
- png-dir — Directory to save per-page PNG images
outputs:
- drawio-file (drawio)
- pdf-file (pdf)
- png-images (png)
- prefer a permanent directory)
- '{caller-specified}'
- '{caller-specified}/*.png'
prompts:
- Create a Draw.io flowchart for our approval process
- Build an architecture diagram in .drawio format
- Draw a process flow with swimlanes in Draw.io
- Create a multi-page Draw.io diagram for our system design
---
