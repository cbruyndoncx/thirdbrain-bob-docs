---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: lease-register — ThirdBrain BOB skill
  description: 'Manage IFRS 16 lease accounting: recognise ROU assets and lease liabilities at commencement, generate amortisation schedules, post monthly interest and deprecia'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: lease-register
catLabel: finance
area: finance
desc: Implements IFRS 16 lease accounting — calculates the opening Right-of-Use asset and lease liability, generates the full amortisation schedule, and posts monthly interest…
summary: 'Manage IFRS 16 lease accounting: recognise ROU assets and lease liabilities at commencement, generate amortisation schedules, post monthly interest and depreciation JEs, and handle modifications and early terminations.'
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- lease_details — Lessor, asset description, start/end date, annual payment, payment frequency, discount rate (rate implicit in the lease if readily determinable, otherwise the lessee's IBR)
- period_id — Period id used to post interest on lease liability and ROU depreciation JEs for all active leases
- lease — Existing lease note to remeasure.
- modification_details — New end date, revised payment amount, modification date
- lease — Lease being terminated early — derecognises ROU and liability.
- termination_date — Termination date used to derecognise the ROU asset and lease liability before the contractual end date
outputs:
- lease (markdown)
- lease-journal-entries (markdown)
- termination-je (markdown)
- updated-lease (markdown)
- '{scope.finance.assets-leases}/LS-{NNN}-{description}.md'
- '{scope.finance.assets-leases}/{lease}.md'
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md'
- '{scope.finance.journals}/JE-{YYYY}-{NNN}.md (two JEs per lease)'
prompts:
- New lease
- Monthly IFRS 16 entries
- Modify a lease
---
