---
description: Create explainer videos from script to final cut. Route clip generation through ai-video-gen, which defaults Veo requests to veo-video-gen using the operator's Gemini key. The `infsh` examples below apply when inference.sh is explicitly requested or the router selects it as a fallback.
title: explainer-video-guide
---

# explainer-video-guide

Create explainer videos from script to final cut. Route clip generation through ai-video-gen, which defaults Veo requests to veo-video-gen using the operator's Gemini key. The `infsh` examples below apply when inference.sh is explicitly requested or the router selects it as a fallback.

- **Area:** Marketing
- **Category:** video
- **Level:** beginner
- **Input:** conversation
- **Output:** video-script
- **Setup:** none
- **Roles:** Head of Marketing, Content Manager

Guides explainer video production: scripting, voiceover, visuals, and assembly.

## How you ask

- “Help me create an explainer video for our product”
- “Write a script for a how-it-works video”
- “Plan the scene sequence for our product demo video”
- “What's the best pipeline for creating an animated explainer?”

## Inputs

- brief — Objective, audience and runtime of the explainer
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- production_constraints — Platform, aspect ratio, deadline and tools the producing team works with, as supplied by the user

## Outputs

- brief-only (markdown)
- company-explainer-video-guide (markdown)
- explainer-script (markdown)
- production-brief (markdown)
- scene-breakdown (markdown)
- script-first-scenes (markdown)
- script-first-script (markdown)
- voiceover (markdown)
- {client.marketing}/videos/explainer-script-{name}.md
- {client.marketing}/videos/production-brief-{name}.md
- {client.marketing}/videos/scene-breakdown-{name}.md
- {client.marketing}/videos/voiceover-{name}.md
- {company.marketing}/videos/explainer-video-guide-{{YYYY-MM-DD}}.md

