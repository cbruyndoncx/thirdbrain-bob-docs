---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: marketing-video-guide — ThirdBrain BOB skill
  description: Production guide for creating professional marketing videos. Covers ad types, platform formats, creative best practices, and complete workflows using AI video g
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: marketing-video-guide
catLabel: video
area: marketing
desc: Creates video ad scripts, generates platform-specific prompts, structures multi-clip ad workflows, and assembles complete marketing videos with voiceover.
summary: Production guide for creating professional marketing videos. Covers ad types, platform formats, creative best practices, and complete workflows using AI video generation. Route clip generation through ai-video-gen, which defaults Veo requests to veo-video-gen using the operator's Gemini key. The `infsh` examples in this guide and its references apply when inference.sh is explicitly requested or the router selects it as a fallback.
difficulty: beginner
inputType: conversation
outputType: video-script
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- marketing_context — Positioning and messaging context.
- brief — Campaign goal, audience, platform and format
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- variant_count — Number of hook variants (the guide's example uses four)
outputs:
- Clip prompts per scene plus voiceover, music and merge steps in execution order
- Production brief with concept, specs, platform format and requirements
- Script with scene beats, hook and voiceover
- Variant prompts, the single variable each one changes, and the test hypothesis
- '{scope.marketing}/videos/video-brief-{name}.md'
- '{scope.marketing}/videos/video-prompts-{name}.md'
- '{scope.marketing}/videos/video-script-{name}.md'
- '{scope.marketing}/videos/video-variants-{name}.md'
prompts:
- Create a video ad script for our Facebook campaign
- Generate platform-specific prompts for our promo video
- Structure a multi-clip ad workflow for our product launch
- Write a YouTube pre-roll ad script with voiceover
---
