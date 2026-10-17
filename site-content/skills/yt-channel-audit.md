---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: yt-channel-audit — ThirdBrain BOB skill
  description: Diagnose why a YouTube channel is stalling, identify the single biggest growth bottleneck, and deliver a scored, actionable audit across five dimensions — strat
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: yt-channel-audit
catLabel: content
area: marketing
desc: Perform a comprehensive YouTube channel audit — analyze strategy, packaging, content retention, growth trajectory, and competitive positioning across 5 scored dimensions.
summary: Diagnose why a YouTube channel is stalling, identify the single biggest growth bottleneck, and deliver a scored, actionable audit across five dimensions — strategy, packaging, content, growth, and competitive positioning.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[api-key]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- channel — YouTube channel URL, handle (@name), or channel name
- analytics_data — YouTube Studio metrics — CTR, avg view duration, traffic sources (from yt-studio-analytics or manual)
- goals — Channel goals — growth, leads, revenue, authority
- 'watchlist — Path to the watchlist YAML (default: under the marketing area, `company.marketing`, `youtube/peer_watchlist.yaml`)'
- 'lookback_days — How many days back to scan (default: 7)'
- themes — Cluster topics across channels with Claude Haiku (requires ANTHROPIC_API_KEY)
outputs:
- Scored audit report with bottleneck diagnosis and priority action plan
- peer-report (markdown)
- '{company.marketing}/video/audits/channel_audit_{YYYY-MM-DD}.md'
- '{me.inbox}/peer_report_{YYYY-MM-DD}.md'
prompts:
- Audit my YouTube channel
- Why is my channel not growing?
- YouTube channel health check
- Channel review — what am I doing wrong?
- Run a channel diagnosis for @channelname
---
