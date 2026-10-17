---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: audit-findings-tracker — ThirdBrain BOB skill
  description: Manage the full lifecycle of external audit findings — from fieldwork adjustments through management responses to the signed audit opinion. Ensures every findin
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: audit-findings-tracker
catLabel: finance
area: finance
desc: Tracks audit adjustments, management letter points, and audit opinion status across an external audit engagement.
summary: Manage the full lifecycle of external audit findings — from fieldwork adjustments through management responses to the signed audit opinion. Ensures every finding is documented, responded to, and resolved before the opinion is issued.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- engagement — Active audit engagement record — finding is logged against it.
- finding_details — Description, account affected, proposed debit/credit, risk level
- engagement — Active audit engagement record.
- opinion_type — unmodified | qualified | adverse | disclaimer
- signed_date — Signed date used to record the final opinion type and sign-off date
outputs:
- closed-engagement (markdown)
- conversation
- dashboard (markdown)
- management-letter (markdown)
- updated-engagement (markdown)
- '{scope.finance.audit}/AUD-{YYYY}-management-letter.md'
- '{scope.finance.audit}/AUD-{YYYY}.md'
prompts:
- Proposed audit adjustment
- Management letter point
- Open findings
---
