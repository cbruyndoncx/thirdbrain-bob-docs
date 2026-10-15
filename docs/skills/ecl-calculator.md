---
description: Calculate the IFRS 9 Expected Credit Loss provision on trade receivables and post the credit loss expense journal entry. Replaces the old incurred-loss model with a forward-looking provision from day one.
title: ecl-calculator
---

# ecl-calculator

Calculate the IFRS 9 Expected Credit Loss provision on trade receivables and post the credit loss expense journal entry. Replaces the old incurred-loss model with a forward-looking provision from day one.

| | |
|---|---|
| **Area** | Finance |
| **Category** | finance |
| **Level** | beginner |
| **Input** | data |
| **Output** | spreadsheet |
| **Setup** | [none] |
| **Roles** | [Finance Manager] |

Calculates IFRS 9 Expected Credit Loss for trade receivables and individually significant balances.

## How you ask

- “Period-end ECL provision”
- “ECL stage”
- “Credit loss expense”

## Inputs

- period_id — Period id used to apply historical loss rates to AR aging buckets across the whole portfolio
- loss_rates — Historical loss rates per aging bucket — defaults from references/default_loss_rates.md
- period_id — Period id used to assess ECL individually for large or credit-impaired receivable balances
- client_list — Client IDs or invoice wikilinks for individual assessment
- current_ecl — Current-period ECL assessment — closing loss allowance.
- prior_ecl — Prior-period ECL assessment — provides the opening balance.

## Outputs

- ecl-assessment (markdown)
- ecl-je (markdown)
- {scope.finance.ecl}/ECL-{YYYY}-{QQ}.md
- {scope.finance.journals}/JE-{YYYY}-{NNN}.md

