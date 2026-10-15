---
description: Production guide for creating professional marketing videos. Covers ad types, platform formats, creative best practices, and complete workflows using AI video generation. Route clip generation through ai-video-gen, which defaults Veo requests to veo-video-gen using the operator's Gemini key. The `infsh` examples in this guide and its references apply when inference.sh is explicitly requested or the router selects it as a fallback.
title: marketing-video-guide
---

# marketing-video-guide

Production guide for creating professional marketing videos. Covers ad types, platform formats, creative best practices, and complete workflows using AI video generation. Route clip generation through ai-video-gen, which defaults Veo requests to veo-video-gen using the operator's Gemini key. The `infsh` examples in this guide and its references apply when inference.sh is explicitly requested or the router selects it as a fallback.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | video |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | video-script |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Creates video ad scripts, generates platform-specific prompts, structures multi-clip ad workflows, and assembles complete marketing videos with voiceover.

## How you ask

- “Create a video ad script for our Facebook campaign”
- “Generate platform-specific prompts for our promo video”
- “Structure a multi-clip ad workflow for our product launch”
- “Write a YouTube pre-roll ad script with voiceover”

## Inputs

- marketing_context — Positioning and messaging context.
- brief — Campaign goal, audience, platform and format
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- variant_count — Number of hook variants (the guide's example uses four)

## Outputs

- Clip prompts per scene plus voiceover, music and merge steps in execution order
- Production brief with concept, specs, platform format and requirements
- Script with scene beats, hook and voiceover
- Variant prompts, the single variable each one changes, and the test hypothesis
- {scope.marketing}/videos/video-brief-{name}.md
- {scope.marketing}/videos/video-prompts-{name}.md
- {scope.marketing}/videos/video-script-{name}.md
- {scope.marketing}/videos/video-variants-{name}.md

