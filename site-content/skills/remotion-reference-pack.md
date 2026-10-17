---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: remotion-reference-pack — ThirdBrain BOB skill
  description: Internal Remotion reference bundle. Load it when another skill or repo task needs Remotion-specific implementation guidance; it is not a user-facing video workf
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: remotion-reference-pack
catLabel: video
area: marketing
desc: Provides an internal reference pack for Remotion implementation patterns used by other video skills.
summary: Internal Remotion reference bundle. Load it when another skill or repo task needs Remotion-specific implementation guidance; it is not a user-facing video workflow.
difficulty: beginner
inputType: conversation
outputType: video-script
requires: '[none]'
roles: '[]'
inputs:
- target-project — Project or downstream skill that owns the actual composition and output.
- subtask — Composition, sequencing, captions, audio, assets, animation, transition, or render-debug work to perform.
outputs:
- conversation
- implementation-handoff (markdown)
prompts:
- I need help setting up a Remotion composition with proper sequencing for my avatar-video project
- The captions in my Remotion render are out of sync with the audio — help me debug the timing
- Show me how to add transitions between sequences in my workflow-video Remotion project
- My Remotion render is failing with an FFmpeg codec error — help me diagnose it
---
