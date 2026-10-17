---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: hyperframes-studio — ThirdBrain BOB skill
  description: Design-first, render-deterministic motion graphics. Plan the visual direction, motion character, and brand identity before writing a single GSAP tween. Then com
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: hyperframes-studio
catLabel: video
area: marketing
desc: Produces brand-matched motion graphics videos — explainers, product promos, TTS-narrated tutorials, music-only text animations — via a 5-phase design-first pipeline…
summary: Design-first, render-deterministic motion graphics. Plan the visual direction, motion character, and brand identity before writing a single GSAP tween. Then compose production HTML and render to MP4 with the HyperFrames engine.
difficulty: advanced
inputType: conversation
outputType: video-script
requires: '[install]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- tone-of-voice — Brand voice for narration and on-screen copy.
- product-record — Product record — what the video explains.
- marketing_context — Positioning and messaging context.
- script — Voiceover script driving scene timing
- brand_assets — Logo, product screenshots, brand colors/fonts
- brand_assets — Logo, product shots, UI screenshots, brand colors, fonts
- brief — Scene narrative and key messages
- copy — Scene text content and narrative arc
outputs:
- HTML audio element left as placeholder for user's music
- design-spec (markdown)
- draft-video (mp4)
- final_mp4 (mp4)
- narration-audio (wav)
- narration-script (markdown)
- narration-timings (json)
- project/DESIGN.md
- project/SCRIPT.md
- project/draft.mp4
- project/final.mp4
- project/production/index.html
- project/production/narration.json
- project/production/narration.wav
- project/storyboard/
- project/storyboard/scene-NN.html
- storyboard-scene (html)
- storyboard-scenes (html)
prompts:
- Create a brand-matched talking-head explainer and pause for design approval before animation.
- Produce a product promo from these screenshots and this brief.
- Build a music-only kinetic text animation and leave the audio placeholder intact.
---
