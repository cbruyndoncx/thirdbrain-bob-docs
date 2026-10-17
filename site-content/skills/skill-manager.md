---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skill-manager — ThirdBrain BOB skill
  description: Manage skill availability to control context and auto-activation behavior.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skill-manager
catLabel: utilities
area: foundational
desc: Toggles vault skills by flipping `disable-model-invocation` in each skill's frontmatter, lists the active inventory by category and status, and bulk-enables or…
summary: Manage skill availability to control context and auto-activation behavior.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — The inventory question to answer — which slice of the library the caller wants to see and at what grouping.
- filter — Narrows the listing to one activation state. The choice decides whether the report can confirm a toggle took effect or only browse the library. (enabled | disabled | all)
- pretty — Renders the listing as a wide table instead of the compact one-line-per-skill form.
- request — The toggle to perform, stated as the one skill the caller means rather than a category that happens to contain it.
- action — Direction of the toggle. Disabling removes the skill from auto-activation and from the context budget; enabling restores both. (enable | disable)
- skill-name — Exact skill directory name under {skills.root}/. An alias or partial name is a pattern target and belongs on the `pattern-or-category` route.
- request — The bulk change to perform, including the scope the caller believes it covers so the preview can be checked against that belief.
- action — Direction of the toggle applied to every skill in the matched set. (enable | disable)
- target — The match expression — `all`, a frontmatter category, an explicit `category:<name>`, a documented alias, or a shell-style folder pattern. Open-ended, because categories and aliases both move with the library.
- dry-run — Prints the skills the target would match and changes nothing. Run it before any broad target so the matched set is confirmed rather than assumed.
- request — Which indexes need refreshing and what changed upstream to make them stale.
- indexes — The subset of derived indexes to rebuild. Absent, all three are regenerated, which is the safe default because they are read together.
- shipping-only — Excludes private-tier playbooks from the workflow index, producing the index that matches a client-facing release rather than the internal library.
outputs:
- Capability index — every enabled skill with its description, category, tier and value chains.
- PLAYBOOKS.md
- SKILLS.md
- Stage-coverage map — which skills and playbooks cover each stage of each value chain, and which stages have none.
- The listing as printed by `list_skills.py`, ending with the enabled and disabled counts.
- The resolved match set, the skills whose activation state changed, the resulting enabled and disabled counts, and the restart reminder.
- The skill touched, its before and after activation state, the resulting enabled and disabled counts, and the restart reminder.
- VALUE-CHAINS.md
- Workflow index — every routable playbook grouped by value chain.
- Written inventory report — one row per skill with its activation state, category and tier — saved when the caller wants the listing as a file rather than on screen.
- prefer a permanent directory)
prompts:
- List all enabled skills and their categories
- Disable the video skills to reduce context usage
- Enable only the marketing-related skills
- Show which skills are currently active
---
