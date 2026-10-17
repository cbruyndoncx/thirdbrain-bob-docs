---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: period-in-review — ThirdBrain BOB skill
  description: 'Produces a chronological "status / year-in-review" reel from a window of AI-assisted work: it measures what was done (from Claude Code session transcripts) and '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: period-in-review
catLabel: marketing-content
area: marketing
desc: Turns a period of AI-assisted work into a shareable status reel — measures the real work done (sessions, prompts, actions, tokens) from Claude Code session logs,…
summary: 'Produces a chronological "status / year-in-review" reel from a window of AI-assisted work: it measures what was done (from Claude Code session transcripts) and montages what was produced (real vault artifacts), rendered as an on-brand portrait video. Re-runnable on any period and scope, so the same skill makes a monthly all-work recap, a quarterly board reel, or a per-client "here''s everything we shipped for you" video.'
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[CEO / Founder, Head of Marketing, Content Manager]'
inputs:
- period — start (inclusive) / --end (exclusive) ISO dates.
- scope — all | client:{client-id} | project:{fragment}. Default all.
- period — start/--end ISO range.
outputs:
- prefer a permanent directory)
- props (json)
- reel (mp4)
- stats (json)
prompts:
- Period in review
- Year in review
- Month in review
---
