---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: vault-validator — ThirdBrain BOB skill
  description: Validates vault content against the data-model business rules defined in DATAMODEL-FULL. Pure Python, no LLM calls — deterministic and reliable.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: vault-validator
catLabel: obsidian
area: foundational
desc: Validates Obsidian frontmatter, link targets, and entity relationships against the data model.
summary: Validates vault content against the data-model business rules defined in DATAMODEL-FULL. Pure Python, no LLM calls — deterministic and reliable.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- wiki_manual — User-manual chapters whose cited paths are checked.
- request — What to produce
outputs:
- undeclared-fields-report (markdown)
- vault-validation-yyyy-mm-dd (markdown)
- '{company.qms.audits}/vault-validation-YYYY-MM-DD.md'
- '{me.inbox}/OPS-{YYYY-MM-DD}-undeclared_fields.md'
prompts:
- Validate frontmatter consistency across my vault
- Check referential integrity of all entity links
- Run data model checks on my vault content
- Audit my vault against the business rules in the data model
---
