---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: cold-call — ThirdBrain BOB skill
  description: Expert B2B cold caller. Cold calling is the fastest path to a conversation with a decision-maker. Every dial is a 30-second audition for a meeting, not a pitch.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: cold-call
catLabel: sales
area: sales
desc: Write cold call scripts, handle phone objections, plan dial blocks, or debrief calls.
summary: Expert B2B cold caller. Cold calling is the fastest path to a conversation with a decision-maker. Every dial is a 30-second audition for a meeting, not a pitch. Tonality, pacing, and confidence matter more than the exact words.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- lead-records — Lead records — the prospects being worked.
- prospect_context — Who you are calling, what you sell, the pain you solve, proof points, and the meeting format
- 'script_type — Script focus: full (default), opener-only, voicemail, gatekeeper (full | opener-only | voicemail | gatekeeper)'
- profile — Company or client profile for sender identity and value framing.
- offerings — Offerings for matching solutions to prospect pain points.
- call_notes — Call notes, transcript, or recording summary with outcomes and any objections encountered
- 'metrics — Available metrics: dials, connects, conversations, meetings booked, connect rate, meeting rate'
outputs:
- call-review (markdown)
- cold-call-script (markdown)
- '{company.sales.outbound}/{campaign-slug}_cold_call_review_{YYYY-MM-DD}.md'
- '{company.sales.outbound}/{campaign-slug}_cold_call_script_{YYYY-MM-DD}.md'
prompts:
- Cold call script
- Phone script
- Phone prospecting
---
