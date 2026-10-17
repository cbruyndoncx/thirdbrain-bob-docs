---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: yt-hook-writing — ThirdBrain BOB skill
  description: Write retention-optimized first-30-second hooks for YouTube videos. The hook determines whether 40% of your audience stays or leaves. Every word in the first 30
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: yt-hook-writing
catLabel: content
area: marketing
desc: Write first-30-second hooks for YouTube videos using the 3-step formula (Context Lean-In, Scroll-Stop, Contrarian Snapback).
summary: Write retention-optimized first-30-second hooks for YouTube videos. The hook determines whether 40% of your audience stays or leaves. Every word in the first 30 seconds must earn its place.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Content Manager]'
inputs:
- youtube_context — Channel niche, audience, positioning and format. Optional — the route collects minimum context from the user when absent.
- video_title — The video title (hook must deliver on its promise immediately)
- video_type — bold-claim, pattern-interrupt, story-open, result-tease, question, cold-open, or contrarian (bold-claim | pattern-interrupt | story-open | result-tease | question | cold-open | contrarian)
- key_takeaway — The single most important takeaway the video delivers
- compelling_moment — The most surprising or emotionally compelling thing in the video
outputs:
- Complete hook with spoken script, visual direction, text overlays, and transition
- '{company.marketing}/video/hooks/{video-slug}_hook_{YYYY-MM-DD}.md'
prompts:
- Write a hook
- Video intro
- Opening for my video
---
