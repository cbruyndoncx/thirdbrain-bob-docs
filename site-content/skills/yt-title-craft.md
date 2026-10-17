---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: yt-title-craft — ThirdBrain BOB skill
  description: Write, optimize, and A/B test YouTube video titles. Every title is a promise to the viewer -- the job is to get the click without breaking trust.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: yt-title-craft
catLabel: content
area: marketing
desc: Write and optimize YouTube video titles for maximum CTR.
summary: Write, optimize, and A/B test YouTube video titles. Every title is a promise to the viewer -- the job is to get the click without breaking trust.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Content Manager]'
inputs:
- youtube_context — Channel niche, audience, positioning and format (`company.marketing`). Optional — the route collects minimum context from the user when absent.
- video_topic — One-sentence description of the video's core idea
- viewer_takeaway — What the viewer gets by watching
- intent_type — search, browse, or hybrid — determines keyword vs curiosity priority
- proof_points — Numbers, timeframes, personal results to include
- emotional_angle — Curiosity, urgency, surprise, relief, controversy
- existing_title — Current title to optimize (optimization mode)
outputs:
- 3-5 scored title variants with mobile preview, type, reasoning, and thumbnail pairing
- '{company.marketing}/video/titles/{video-slug}_titles_{YYYY-MM-DD}.md'
prompts:
- Write a title
- Title ideas
- Optimize my title
---
