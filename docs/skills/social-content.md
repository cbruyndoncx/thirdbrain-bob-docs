---
description: Create engaging social media content that builds audience and supports business goals.
title: social-content
---

# social-content

Create engaging social media content that builds audience and supports business goals.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing content |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Writes social posts for LinkedIn, X, and Substack, repurposes long-form content, and analyzes post performance.

## How you ask

- “Write a LinkedIn post about our latest product update”
- “Create a content calendar for our social channels this month”
- “Repurpose this blog post into a Twitter thread”
- “Generate hook formulas for our Instagram engagement posts”
- “Log my last 5 LinkedIn posts and their metrics”
- “Run the content loop — what's working?”
- “What patterns do you see in my content performance?”

## Inputs

- request — What to produce
- scope — `company`, or a client-id under {company.clients}/ — a string with one reserved value, not a closed set
- brand-voice — Locked brand and tone-of-voice context used to write in voice.
- target-audience — Target audience, ICP, and positioning context.
- content-calendar — Content calendar for scheduling.
- content-pillars — Content pillars for topic selection.

## Outputs

- Content Performance Review (references/content-review.md) — top and bottom posts, patterns, do-more and stop-doing calls, next-cycle bets.
- Self-learning loop Step 4 — patterns found across the last ~10 logged posts and the rule changes they justify, written before `social-content-rules.md` is updated.
- content-calendar (markdown)
- content-pillars (markdown)
- performance-log (markdown)
- social-content (markdown)
- social-content-rules (markdown)
- {scope.marketing.social}/content-calendar.md
- {scope.marketing.social}/content-pillars.md
- {scope.marketing.social}/performance-log.md
- {scope.marketing.social}/reviews/loop-analysis-{YYYY-MM-DD}.md
- {scope.marketing.social}/reviews/{YYYY-MM-DD}_review.md
- {scope.marketing.social}/social-content-rules.md
- {scope.marketing.social}/social-content-{YYYY-MM-DD}.md

