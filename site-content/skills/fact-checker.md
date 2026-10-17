---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: fact-checker — ThirdBrain BOB skill
  description: 'Validate claims, reasoning, and conclusions from a conversation against credible external sources. Produce an honest, well-sourced assessment of what holds up, '
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: fact-checker
catLabel: research
area: research
desc: Validates claims, reasoning, and conclusions from a conversation against credible external sources.
summary: Validate claims, reasoning, and conclusions from a conversation against credible external sources. Produce an honest, well-sourced assessment of what holds up, what's shaky, and what can't be verified.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- conversation — The conversation to fact-check (current thread or pasted transcript)
- mode — Light validates highest-stakes claims only (at most 10 searches); Full validates all searchable claims (at most 25 searches) (light | full)
outputs:
- Verdict summary with sources, tally, and attention items
- prefer a permanent directory)
prompts:
- Fact-check this conversation
- Can you verify the claims we just discussed?
- Run a source check on everything we talked about
- Is what we said about market sizing accurate?
- Light fact-check before my board meeting
---
