---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: coa-account — ThirdBrain BOB skill
  description: Manages the Chart of Accounts as a set of `coa-account` entities, one file per account, scoped per jurisdiction. Used by journal-entry-poster, trial-balance-gen
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: coa-account
catLabel: finance
area: finance
desc: Manages jurisdiction-aware Chart of Accounts records and validates COA accounts against the applicable statutory scheme.
summary: Manages the Chart of Accounts as a set of `coa-account` entities, one file per account, scoped per jurisdiction. Used by journal-entry-poster, trial-balance-generator, and financial-statement-generator as the canonical source for account codes, names, types, and the normal-balance side.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- chart-of-accounts — Existing chart of accounts — the population being read or extended.
- request — User request and source context for seed (own)
- request — User request and source context for seed (client live)
- request — User request and source context for seed (client audit)
- request — User request and source context for lookup
- request — User request and source context for add account
- request — User request and source context for deprecate
outputs:
- Books profile for the audit-scope books.
- Books profile for the client's live books.
- Books profile — entity, standard, currency, jurisdiction, materiality.
- Index page for the seeded jurisdiction listing every account by class.
- New analytical sub-account rolling up to its parent account.
- One note per account in the seeded chart.
- Opening accounting period.
- 'The same account note with status: inactive — updated in place, never deleted.'
- add-account-result (markdown)
- conversation
- deprecate-result (markdown)
- lookup-result (markdown)
- seed-client-audit-result (markdown)
- seed-client-live-result (markdown)
- seed-own-result (markdown)
- '{scope.finance.coa}/{jurisdiction}/_index.md'
- '{scope.finance.coa}/{jurisdiction}/{account_code}-{slug}.md'
- '{scope.finance.entity}'
- '{scope.finance.periods}/{period_id}.md'
prompts:
- Chart of accounts
- Journal entry account codes
- Seed the PCMN scheme
---
