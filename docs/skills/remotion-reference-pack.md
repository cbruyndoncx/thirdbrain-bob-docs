---
description: Internal Remotion reference bundle. Load it when another skill or repo task needs Remotion-specific implementation guidance; it is not a user-facing video workflow.
title: remotion-reference-pack
---

# remotion-reference-pack

Internal Remotion reference bundle. Load it when another skill or repo task needs Remotion-specific implementation guidance; it is not a user-facing video workflow.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | video |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | video-script |
| **Setup** | [none] |
| **Roles** | [] |

Provides an internal reference pack for Remotion implementation patterns used by other video skills.

## How you ask

- “I need help setting up a Remotion composition with proper sequencing for my avatar-video project”
- “The captions in my Remotion render are out of sync with the audio — help me debug the timing”
- “Show me how to add transitions between sequences in my workflow-video Remotion project”
- “My Remotion render is failing with an FFmpeg codec error — help me diagnose it”

## Inputs

- target-project — Project or downstream skill that owns the actual composition and output.
- subtask — Composition, sequencing, captions, audio, assets, animation, transition, or render-debug work to perform.

## Outputs

- conversation
- implementation-handoff (markdown)

