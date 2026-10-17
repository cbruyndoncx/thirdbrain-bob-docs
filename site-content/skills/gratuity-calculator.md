---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: gratuity-calculator — ThirdBrain BOB skill
  description: Calculate end-of-service gratuity entitlements and post monthly accrual journal entries. For the UAE it implements the Federal Decree-Law No. 33 of 2021 formula
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: gratuity-calculator
catLabel: finance
area: finance
desc: Calculates end-of-service and statutory gratuity using jurisdiction-specific laws and posts the monthly accrual journal entry.
summary: Calculate end-of-service gratuity entitlements and post monthly accrual journal entries. For the UAE it implements the Federal Decree-Law No. 33 of 2021 formula — basic salary only, tiered by years of service, capped at two years' total basic salary; for KSA, Saudi Labour Law Art. 84, 85 and 87. Other jurisdictions follow their workflow.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- employee — Employee person record with start_date and basic_salary.
- as_at_date — Defaults to today. Use termination date for final settlement.
- termination_type — resignation | termination | redundancy. Does not reduce entitlement under UAE Decree-Law 33/2021 (recorded for the settlement record and the gross-misconduct warning); under KSA Art. 85 resignation reduces the award.
- period_id — Period id used to post gratuity accrual JEs for all active employees for a period
- employee_list — Path to HR folder or list of employee wikilinks
- employee — Departing employee — final settlement basis.
- termination_date — Termination date used to calculate final gratuity, post settlement JE, close provision
- termination_type — resignation | termination | redundancy
outputs:
- accrual-journal-entries (markdown)
- conversation
- gratuity-calculation (markdown)
- gratuity-provision-notes (markdown)
- settlement-calculation (markdown)
- settlement-je (markdown)
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md'
- '{scope.finance.provisions-gratuity}/GRAT-{employee_id}-{YYYY}.md'
prompts:
- Gratuity calculator
- End-of-service provision
- Final settlement
---
