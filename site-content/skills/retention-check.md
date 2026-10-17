---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: retention-check — ThirdBrain BOB skill
  description: Run structured post-delivery satisfaction checks, collect NPS scores, prepare for renewal conversations, and build action plans when a client relationship is at
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: retention-check
catLabel: sales
area: sales
desc: Runs post-delivery satisfaction checks, collects NPS scores, and builds recovery plans for at-risk clients.
summary: Run structured post-delivery satisfaction checks, collect NPS scores, prepare for renewal conversations, and build action plans when a client relationship is at risk. Keeps the deliver-to-satisfaction chain closed by ensuring each engagement has a documented satisfaction signal and a clear next step.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- client-id — Client identifier for vault path resolution
- project-context — Recent delivery context from the client project folder (`client.root`).
- contact-details — Who to contact (`client.contacts`).
- client-profile — Client relationship baseline used to frame the renewal case.
- company-profile — Own-company context used to position the renewal offer.
- project-context — Engagement history from the client project folder (`client.root`).
- satisfaction-records — Prior satisfaction scores (`client.feedback`).
- satisfaction-record — Most recent satisfaction record with low score (`client.feedback`); absent when the trigger is silence, a complaint, or an invoice or scope dispute.
outputs:
- recovery-plan (markdown)
- renewal-brief (markdown)
- satisfaction-record (markdown)
- '{client.deals}/renewal_brief_{YYYY-MM-DD}.md'
- '{client.feedback}/recovery_plan_{YYYY-MM-DD}.md'
- '{client.feedback}/satisfaction_{YYYY-MM-DD}.md'
prompts:
- Post-delivery satisfaction
- Renewal conversation
- Recovery action plan
---
