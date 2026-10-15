---
description: Create distribution-ready branded PDFs that explain how a skill works, what pack it belongs to, what files support it, what outputs it produces, and what governance applies.
title: skill-pipeline-explainer
---

# skill-pipeline-explainer

Create distribution-ready branded PDFs that explain how a skill works, what pack it belongs to, what files support it, what outputs it produces, and what governance applies.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Head of Marketing, Content Manager] |

Creates branded explainer PDFs that document a vault skill's workflow, source pack, supporting files, outputs, and quality gates.

## How you ask

- “Document this skill like the website audit PDF”
- “Make a pipeline PDF for business-baseline”
- “Show what pack this skill belongs to”

## Inputs

- skill — Skill folder name under {skills.root}/, e.g. business-baseline.
- audience — Reader framing. Default: partners and operators evaluating the skill.
- output_dir — Vault-relative output directory. Default: `{company.marketing.skool-lead-magnets}/{skill}-pipeline/`.
- client-id — Client id for white-label deliverable routing. When set, output defaults to the client project folder `{client.projects}/{project-id}/` and uses deliverable frontmatter. Required with --deliverable.
- project-id — Client project folder id for deliverable mode. Defaults to YYYY-MM-{skill}-pipeline.
- brand-theme — Optional company/client brand theme passed through to the PDF renderer. Omitted, branded-pdf uses the single `*-brand-theme.md` in `{company.assets-brand-guidelines}`.
- source (Refresh Existing Explainer) — Existing explainer source note.
- skill — Skill folder name under {skills.root}/.

## Outputs

- beside source, versioned when locked
- explainer_pdf (pdf)
- explainer_source (markdown)
- refreshed_pdf (pdf)
- refreshed_source (markdown)
- same as source
- {company.marketing.skool-lead-magnets}/{skill}-pipeline/{skill}-pipeline.md
- {company.marketing.skool-lead-magnets}/{skill}-pipeline/{skill}-pipeline.pdf

