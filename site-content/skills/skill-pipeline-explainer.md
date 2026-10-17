---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skill-pipeline-explainer — ThirdBrain BOB skill
  description: Create distribution-ready branded PDFs that explain how a skill works, what pack it belongs to, what files support it, what outputs it produces, and what govern
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skill-pipeline-explainer
catLabel: utilities
area: foundational
desc: Creates branded explainer PDFs that document a vault skill's workflow, source pack, supporting files, outputs, and quality gates.
summary: Create distribution-ready branded PDFs that explain how a skill works, what pack it belongs to, what files support it, what outputs it produces, and what governance applies.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Marketing, Content Manager]'
inputs:
- skill — Skill folder name under {skills.root}/, e.g. business-baseline.
- 'audience — Reader framing. Default: partners and operators evaluating the skill.'
- 'output_dir — Vault-relative output directory. Default: `{company.marketing.skool-lead-magnets}/{skill}-pipeline/`.'
- client-id — Client id for white-label deliverable routing. When set, output defaults to the client project folder `{client.projects}/{project-id}/` and uses deliverable frontmatter. Required with --deliverable.
- project-id — Client project folder id for deliverable mode. Defaults to YYYY-MM-{skill}-pipeline.
- brand-theme — Optional company/client brand theme passed through to the PDF renderer. Omitted, branded-pdf uses the single `*-brand-theme.md` in `{company.assets-brand-guidelines}`.
- source (Refresh Existing Explainer) — Existing explainer source note.
- skill — Skill folder name under {skills.root}/.
outputs:
- beside source, versioned when locked
- explainer_pdf (pdf)
- explainer_source (markdown)
- refreshed_pdf (pdf)
- refreshed_source (markdown)
- same as source
- '{company.marketing.skool-lead-magnets}/{skill}-pipeline/{skill}-pipeline.md'
- '{company.marketing.skool-lead-magnets}/{skill}-pipeline/{skill}-pipeline.pdf'
prompts:
- Document this skill like the website audit PDF
- Make a pipeline PDF for business-baseline
- Show what pack this skill belongs to
---
