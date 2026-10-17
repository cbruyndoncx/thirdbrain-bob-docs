---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: buyback-rate — ThirdBrain BOB skill
  description: Computes the owner's Buy Back Rate — the dollar value of one hour of their time — then turns a two-week time-and-energy audit into a ranked list of exactly whic
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: buyback-rate
catLabel: productivity
area: foundational
desc: Computes your Buy Back Rate and turns a time-and-energy audit into a ranked 'offload this first' list — routing each task to automate-with-AI before hire.
summary: 'Computes the owner''s Buy Back Rate — the dollar value of one hour of their time — then turns a two-week time-and-energy audit into a ranked list of exactly which tasks to offload first, routing each to AI/automation before a human hire. It is the quantitative front-end to delegation: `delegation` coaches the human handoff; this skill produces the number and the ranked target list that tell you *what* to hand off and *to what*.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Operations Manager]'
inputs:
- income — Annual income basis = profit + owner salary + business expenses (the value the owner's 2,000 working hours produce).
- time_log — A task time-log (manual table, or exported from ai-work-audit / time-tracking-reporter). One row per recurring task with rough weekly hours.
- income — Income basis for the rate. If omitted, the audit reports relative ranking only (no dollar threshold).
outputs:
- offload-report (markdown)
- prefer a permanent directory)
- rate-brief (markdown)
prompts:
- What's my time worth
- What should I stop doing
- Buy back my time
---
