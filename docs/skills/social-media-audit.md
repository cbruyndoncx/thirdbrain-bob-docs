---
description: Analyze a brand's social media presence across all major platforms, score each channel against best-practice benchmarks, identify gaps and opportunities, and deliver a prioritized improvement plan — all without requiring API keys.
title: social-media-audit
---

# social-media-audit

Analyze a brand's social media presence across all major platforms, score each channel against best-practice benchmarks, identify gaps and opportunities, and deliver a prioritized improvement plan — all without requiring API keys.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | marketing content |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Audits a brand's social media footprint across LinkedIn, Instagram, Facebook, X, TikTok, and YouTube — scoring profile completeness, content quality, engagement…

## How you ask

- “Run a social media audit for our company”
- “Audit our LinkedIn and Instagram presence”
- “Compare our social media with [competitor1] and [competitor2]”
- “Which social platforms should we focus on?”
- “Social media health check for client [name]”

## Inputs

- marketing_context — Positioning and messaging context.
- accounts — Profiles to audit, one per platform
- account — Profile to audit
- platform — The one channel to audit — linkedin, twitter, instagram, youtube, tiktok, or facebook. Each has its own benchmark set. (facebook | instagram | linkedin | tiktok | twitter | youtube)
- accounts — Own profiles
- competitor_accounts — Competitor profiles to benchmark against

## Outputs

- social-media-audit-report (markdown)
- social-media-audit-report-client (markdown)
- {client.marketing}/social-audits/social_media_audit_{YYYY-MM-DD}.md
- {company.marketing}/social-audits/social_media_audit_{YYYY-MM-DD}.md

## Seen in these workflows

- [Six platforms. Zero visibility.](../workflows/social-media-audit.md)

