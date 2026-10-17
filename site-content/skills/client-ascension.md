---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: client-ascension — ThirdBrain BOB skill
  description: Turn won clients into your biggest revenue source. Structured post-sale playbook for upsells, cross-sells, retention, and LTV maximization.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: client-ascension
catLabel: sales
area: sales
desc: Maximizes revenue from existing clients through structured upsell/cross-sell mapping, retention playbooks, renewal conversations, and LTV optimization.
summary: Turn won clients into your biggest revenue source. Structured post-sale playbook for upsells, cross-sells, retention, and LTV maximization.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- client-context — Client outcomes, current engagement, health signals, needs, and applicable company offerings.
- offerings — Canonical offerings catalogue used to identify upsell and expansion paths.
- engagement-evidence — Delivery, adoption, satisfaction, risk, and relationship evidence for the client.
- renewal-context — Contract timing, delivered value, open risks, stakeholders, and renewal objective.
outputs:
- ascension-map (markdown)
- reengagement-plan (markdown)
- renewal-script (markdown)
- retention-playbook (markdown)
- '{scope.sales}/ascension-map-{client}-{date}.md'
- '{scope.sales}/reengage-{client}-{date}.md'
- '{scope.sales}/renewal-script-{client}-{date}.md'
- '{scope.sales}/retention-playbook-{client}-{date}.md'
prompts:
- Build an ascension map for our AI transformation clients — what's the natural upsell path?
- Create a 90-day retention playbook for our new enterprise client
- Write a renewal conversation script for a client whose project ends next month
- Build a re-engagement sequence for clients we haven't spoken to in 6 months
- What's our highest-leverage LTV move right now?
---
