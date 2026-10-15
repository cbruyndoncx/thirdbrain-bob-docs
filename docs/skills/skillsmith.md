---
description: Entry point for all skill creation, architecture, improvement, and management operations.
title: skillsmith
---

# skillsmith

Entry point for all skill creation, architecture, improvement, and management operations.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Creates or updates vault skills and drives new skills through the full QMS creation path.

## How you ask

- “Create a new skill for handling customer surveys”
- “Update the workflow section of this existing skill”
- “Drive this skill through the full QMS creation path”

## Inputs

- skill-name — Name of the new skill (kebab-case)
- purpose — What the skill should do and who would trigger it
- skill — Skill to update
- change — What to change, stated as a delta from the current
- skill — Skill to improve, or the name of a new one
- goal — What the skill should do that it does not do today
- request — The original skill-work request that cannot proceed

## Outputs

- QMS scorecard entry appended for the new skill (Step 5f).
- SKILLS.md
- Temporary analysis; {descriptor} is a short kebab-case task slug.
- draft-package (markdown)
- improved-skill (markdown)
- prefer a permanent directory)
- skill-package (markdown)
- skills-index (markdown)
- updated-skill (markdown)
- {company.qms.mapping}
- {skills.root}/{skill-name}/

