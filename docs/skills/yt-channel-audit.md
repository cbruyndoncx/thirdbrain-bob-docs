---
description: Diagnose why a YouTube channel is stalling, identify the single biggest growth bottleneck, and deliver a scored, actionable audit across five dimensions — strategy, packaging, content, growth, and competitive positioning.
title: yt-channel-audit
---

# yt-channel-audit

Diagnose why a YouTube channel is stalling, identify the single biggest growth bottleneck, and deliver a scored, actionable audit across five dimensions — strategy, packaging, content, growth, and competitive positioning.

| | |
|---|---|
| **Area** | Marketing |
| **Category** | content |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [api-key] |
| **Roles** | [Head of Marketing, Content Manager] |

Perform a comprehensive YouTube channel audit — analyze strategy, packaging, content retention, growth trajectory, and competitive positioning across 5 scored dimensions.

## How you ask

- “Audit my YouTube channel”
- “Why is my channel not growing?”
- “YouTube channel health check”
- “Channel review — what am I doing wrong?”
- “Run a channel diagnosis for @channelname”

## Inputs

- channel — YouTube channel URL, handle (@name), or channel name
- analytics_data — YouTube Studio metrics — CTR, avg view duration, traffic sources (from yt-studio-analytics or manual)
- goals — Channel goals — growth, leads, revenue, authority
- watchlist — Path to the watchlist YAML (default: under the marketing area, `company.marketing`, `youtube/peer_watchlist.yaml`)
- lookback_days — How many days back to scan (default: 7)
- themes — Cluster topics across channels with Claude Haiku (requires ANTHROPIC_API_KEY)

## Outputs

- Scored audit report with bottleneck diagnosis and priority action plan
- peer-report (markdown)
- {company.marketing}/video/audits/channel_audit_{YYYY-MM-DD}.md
- {me.inbox}/peer_report_{YYYY-MM-DD}.md

