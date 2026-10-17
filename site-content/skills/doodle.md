---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: doodle — ThirdBrain BOB skill
  description: 'Target Audience: business owners and consultants who need to explain an automation, pipeline or process to a non-technical client, colleague or prospect.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: doodle
catLabel: diagramming
area: foundational
desc: 'Draws a hand-drawn explainer strip (PNG, optional SVG) that shows how a system, pipeline or process works for non-technical readers: 3-6 left-to-right scenes, a small…'
summary: 'Target Audience: business owners and consultants who need to explain an automation, pipeline or process to a non-technical client, colleague or prospect.'
difficulty: advanced
inputType: conversation
outputType: diagram
requires: '[install]'
roles: '[]'
inputs:
- subject — What to explain, e.g. 'how our lead routing works'
- source-material — Code, logs, docs or a process note that describe what the system really does
outputs:
- Editable strip source; {slug} is a short kebab-case name for the subject.
- 'Optional (--svg): self-contained vector strip with logos and font embedded, for slides, print and carousels.'
- Rendered strip at 2x, width = scenes x 340 + 60 px.
- prefer a permanent directory)
prompts:
- /doodle how our lead routing works
- Make a napkin sketch of the client onboarding flow for the proposal
- Explain the invoice-collection automation to the client in one picture
---
