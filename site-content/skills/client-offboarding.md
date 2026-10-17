---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: client-offboarding — ThirdBrain BOB skill
  description: Generate professional client offboarding packages that close engagements gracefully, capture feedback, and open doors for future work.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: client-offboarding
catLabel: sales
area: sales
desc: Generates client offboarding packages as Markdown notes in the client folder, including results summaries, testimonial requests, exit surveys, referral asks, and…
summary: Generate professional client offboarding packages that close engagements gracefully, capture feedback, and open doors for future work.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- client_id — Client being offboarded
- engagement_period — Period the summary covers
- profile — loaded from your vault context
- tone-of-voice — loaded from your vault context
- contact-details — loaded from your vault context
- client_id — Client to ask
- ask_type — Which ask to make of the departing client — a testimonial, a referral introduction, or both in one message. Defaults to the lower-friction single ask. (testimonial | referral | both)
- client_id — Client to survey
- delivery_channel — How the exit survey reaches the client — an email with inline questions, a linked form, or a live interview the operator runs and transcribes. (email | form | interview)
- engagement_period — Period the offboarding covers
outputs:
- exit-survey (markdown)
- exit-survey-doc (markdown)
- handover (markdown)
- offboarding-package (markdown)
- referral-ask (markdown)
- results-summary (markdown)
- testimonial-request (markdown)
- '{client.offboarding}/{client-id}_exit_survey.md'
- '{client.offboarding}/{client-id}_handover.md'
- '{client.offboarding}/{client-id}_offboarding_package.md'
- '{client.offboarding}/{client-id}_referral_ask.md'
- '{client.offboarding}/{client-id}_results_summary.md'
- '{client.offboarding}/{client-id}_testimonial_request.md'
prompts:
- Create an offboarding package for our client Acme Corp
- Generate a testimonial request for the project we just finished
- Prepare a professional handover document for the client transition
- Draft an exit survey and results summary for client wrap-up
---
