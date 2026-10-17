---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: copywriting — ThirdBrain BOB skill
  description: Write conversion-focused marketing copy for web pages.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: copywriting
catLabel: marketing-content
area: marketing
desc: Writes conversion-focused headlines, CTAs, and page copy for homepages, landing pages, pricing pages, feature pages, and about pages.
summary: Write conversion-focused marketing copy for web pages.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- phrase-bank — Approved phrases and banned words.
- url — Live page URL to audit in URL Analysis Mode (or Sub-Agent Mode); omit when writing new copy from vault context
- scope — `company`, or a client-id under the client root (`client.root`) — a string with one reserved value, not a closed set
- marketing-context — Marketing context for voice and positioning.
- icp — ICP — who the copy speaks to.
- profile — Company profile — sender identity and credibility anchors.
- tone-of-voice — Tone of voice — copy register and brand sound.
- offerings — Offerings catalogue — what the copy is selling.
outputs:
- copywriting (markdown)
- '{scope.marketing}/content/copywriting-{YYYY-MM-DD}.md'
prompts:
- Write homepage copy for our project management SaaS
- Improve the headlines on our pricing page
- Write CTA copy for our free trial signup
- Rewrite our About page to be more compelling
- Analyze the copy on this URL and suggest improvements
---
