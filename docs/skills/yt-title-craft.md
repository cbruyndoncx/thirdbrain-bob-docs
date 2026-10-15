---
description: Write, optimize, and A/B test YouTube video titles. Every title is a promise to the viewer -- the job is to get the click without breaking trust.
title: yt-title-craft
---

# yt-title-craft

Write, optimize, and A/B test YouTube video titles. Every title is a promise to the viewer -- the job is to get the click without breaking trust.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | content |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Content Manager] |

Write and optimize YouTube video titles for maximum CTR.

## How you ask

- “Write a title”
- “Title ideas”
- “Optimize my title”

## Inputs

- youtube_context — Channel niche, audience, positioning and format (`company.marketing`). Optional — the route collects minimum context from the user when absent.
- video_topic — One-sentence description of the video's core idea
- viewer_takeaway — What the viewer gets by watching
- intent_type — search, browse, or hybrid — determines keyword vs curiosity priority
- proof_points — Numbers, timeframes, personal results to include
- emotional_angle — Curiosity, urgency, surprise, relief, controversy
- existing_title — Current title to optimize (optimization mode)

## Outputs

- 3-5 scored title variants with mobile preview, type, reasoning, and thumbnail pairing
- {company.marketing}/video/titles/{video-slug}_titles_{YYYY-MM-DD}.md

