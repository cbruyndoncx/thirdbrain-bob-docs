---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: skill-doc-generator — ThirdBrain BOB skill
  description: Generate and maintain per-skill documentation notes in `{company.qms.skill-docs}/`. Each note synthesises frontmatter, inputs, outputs, setup instructions, depe
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: skill-doc-generator
catLabel: utilities
area: foundational
desc: Generate and maintain structured documentation notes for all vault skills.
summary: Generate and maintain per-skill documentation notes in `{company.qms.skill-docs}/`. Each note synthesises frontmatter, inputs, outputs, setup instructions, dependencies, example prompts, and workflow summary from the source. Notes power the `skill-docs.base` view for browsing, filtering, and tier-alignment analysis.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- vault_root — Root path of the Obsidian vault
- skill — Skill folder name to enrich
- skill — Restrict the render to one skill by directory name
- 'output — Optional output PDF path (default: {company.qms.skill-docs}/skills-catalog-review.pdf)'
- request — Optional — skill name to focus on, or blank to open full explorer
outputs:
- Error, warning, and pass counts for output paths
- 'The ## Output Locations block, rewritten between its generated markers'
- build_skill_docs_pdf.py's default; --output writes elsewhere
- catalog_review_pdf (pdf)
- skill-explorer (html)
- skill_doc (markdown)
- skill_docs (markdown)
- '{company.qms.root}/skill-docs-catalogue.pdf'
- '{company.qms.root}/skill-explorer.html'
- '{company.qms.skill-docs}/skills-catalog-review.pdf'
- '{company.qms.skill-docs}/{skill-name}.md'
- '{skills.root}/{skill-name}/'
prompts:
- Regenerate skill documentation for all vault skills
- Update the skill-doc note for the copywriting skill
- Audit skill documentation for consistency and missing fields
- Rebuild the skill docs and export to PDF
- Open the skill explorer
- Show me the skill lineage graph
- Build the skills catalog review PDF
---
