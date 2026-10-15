---
description: 'Manage IFRS 16 lease accounting: recognise ROU assets and lease liabilities at commencement, generate amortisation schedules, post monthly interest and depreciation JEs, and handle modifications and early terminations.'
title: lease-register
---

# lease-register

Manage IFRS 16 lease accounting: recognise ROU assets and lease liabilities at commencement, generate amortisation schedules, post monthly interest and depreciation JEs, and handle modifications and early terminations.

- **Area:** Finance
- **Category:** finance
- **Level:** beginner
- **Input:** data
- **Output:** spreadsheet
- **Setup:** none
- **Roles:** Finance Manager

Implements IFRS 16 lease accounting — calculates the opening Right-of-Use asset and lease liability, generates the full amortisation schedule, and posts monthly interest…

## How you ask

- “New lease”
- “Monthly IFRS 16 entries”
- “Modify a lease”

## Inputs

- lease_details — Lessor, asset description, start/end date, annual payment, payment frequency, discount rate (rate implicit in the lease if readily determinable, otherwise the lessee's IBR)
- period_id — Period id used to post interest on lease liability and ROU depreciation JEs for all active leases
- lease — Existing lease note to remeasure.
- modification_details — New end date, revised payment amount, modification date
- lease — Lease being terminated early — derecognises ROU and liability.
- termination_date — Termination date used to derecognise the ROU asset and lease liability before the contractual end date

## Outputs

- lease (markdown)
- lease-journal-entries (markdown)
- termination-je (markdown)
- updated-lease (markdown)
- {scope.finance.assets-leases}/LS-{NNN}-{description}.md
- {scope.finance.assets-leases}/{lease}.md
- {scope.finance.journals}/JE-{YYYY}-{NNN}.md
- {scope.finance.journals}/JE-{YYYY}-{NNN}.md (two JEs per lease)

