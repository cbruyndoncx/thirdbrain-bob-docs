---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: blotato — ThirdBrain BOB skill
  description: Consolidated Blotato social-content workflow set. It keeps the upstream 7-skill behavior in one vault skill folder with one , and routes each capability to a de
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: blotato
catLabel: marketing-content
area: marketing
desc: Creates, grades, repurposes, and schedules platform-native social posts using the Blotato skill workflow set.
summary: Consolidated Blotato social-content workflow set. It keeps the upstream 7-skill behavior in one vault skill folder with one , and routes each capability to a dedicated workflow file.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- client-tone-of-voice — Client brand voice for scheduled posts.
- request — Broad content ask such as 'help me post something' or 'I don't know what to post'.
- brand-context — Answers to the 6 brand-brief questions, or existing profile/brand notes.
- topic — Topic, idea, offer, story, or source angle.
- platform — Target platform.
- post — Draft post text or path.
- source (Repurpose) — Blog post, newsletter, transcript, script, or long-form paste.
- topic — Topic and angle for the hook.
- post — Approved post text or path.
- platform — Target platform(s).
- schedule — Specific time or next free slot.
outputs:
- brand-brief (markdown)
- content-batch (markdown)
- conversation
- final-post (markdown)
- hooks (markdown)
- post (markdown)
- prefer a permanent directory)
- scheduling-result (markdown)
- scorecard (markdown)
- '{scope.brand}/'
- '{scope.marketing.social}/'
prompts:
- Help me post something
- Write me a post
- Grade this post
---
