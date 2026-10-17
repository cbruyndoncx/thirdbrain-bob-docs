---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ai-vampire-guard — ThirdBrain BOB skill
  description: 'Prevent AI-amplified burnout by making cognitive load visible. Inspired by Steve Yegge''s "AI Vampire" concept — when AI tools amplify your productivity so much '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ai-vampire-guard
catLabel: productivity
area: foundational
desc: Monitors Claude Code usage intensity and generates an energy burn-rate gauge.
summary: Prevent AI-amplified burnout by making cognitive load visible. Inspired by Steve Yegge's "AI Vampire" concept — when AI tools amplify your productivity so much that you burn through energy without realizing it.
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[]'
inputs:
- request — What to produce
outputs:
- ai-vampire-guard-yyyy-mm-dd (markdown)
- '{me.inbox}/ai_vampire_guard_YYYY-MM-DD.md'
prompts:
- Check my Claude Code usage intensity
- Am I overworking in Claude Code today?
- Show my energy burn-rate gauge
- What's my current work zone and usage score?
---
