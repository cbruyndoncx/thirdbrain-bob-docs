---
description: Validates vault content against the data-model business rules defined in DATAMODEL-FULL. Pure Python, no LLM calls — deterministic and reliable.
title: vault-validator
---

# vault-validator

Validates vault content against the data-model business rules defined in DATAMODEL-FULL. Pure Python, no LLM calls — deterministic and reliable.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | obsidian |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Validates Obsidian frontmatter, link targets, and entity relationships against the data model.

## How you ask

- “Validate frontmatter consistency across my vault”
- “Check referential integrity of all entity links”
- “Run data model checks on my vault content”
- “Audit my vault against the business rules in the data model”

## Inputs

- wiki_manual — User-manual chapters whose cited paths are checked.
- request — What to produce

## Outputs

- undeclared-fields-report (markdown)
- vault-validation-yyyy-mm-dd (markdown)
- {company.qms.audits}/vault-validation-YYYY-MM-DD.md
- {me.inbox}/OPS-{YYYY-MM-DD}-undeclared_fields.md

