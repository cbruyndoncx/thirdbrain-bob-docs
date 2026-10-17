---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: obsidian-ops — ThirdBrain BOB skill
  description: Comprehensive vault maintenance toolkit for Obsidian. Covers assessment, metadata, tags, connections, MOCs, daily notes, content curation, optimization, and qua
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: obsidian-ops
catLabel: obsidian
area: foundational
desc: Maintains an Obsidian vault by assessing health, standardizing tags, adding frontmatter metadata, and generating Maps of Content.
summary: Comprehensive vault maintenance toolkit for Obsidian. Covers assessment, metadata, tags, connections, MOCs, daily notes, content curation, optimization, and quality review.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[]'
inputs:
- request — The vault or subtree to check up on, and any prior checkup to compare against.
- request — Which targeted maintenance operation to run and its scope — score, tags, connections, MOCs, daily notes, or directory indexes.
- request — The maintenance work to validate and which phase's checklist applies.
- prior-report — A prior full-checkup or assessment report, read back to compute the before/after metric delta. Absent, the review reports current state only.
outputs:
- 5-dimension vault health score, letter grade, delta tracking, and top-3 fixes.
- Combined scoring, tag analysis, and raw assessment report with an SVG dashboard from a single full-checkup run.
- Directories that meet the indexing threshold but do not yet have an INDEX.md.
- Per-phase checklist results, spot-checked files, and the before/after metric comparison, returned inline.
- Report of INDEX.md / AGENTS.md entry points generated or updated across the scanned directory trees.
- Tag standardization findings — inconsistent or duplicate tags and the normalization report.
- Temporal and topic link suggestions connecting daily notes.
- '{me.inbox}/OPS-YYYY-MM-DD-daily_connectivity.md'
- '{me.inbox}/OPS-YYYY-MM-DD-index_generation.md'
- '{me.inbox}/OPS-YYYY-MM-DD-index_suggestions.md'
- '{me.inbox}/OPS-YYYY-MM-DD-tag_analysis.md'
- '{me.inbox}/OPS-YYYY-MM-DD-vault_checkup.md'
- '{me.inbox}/OPS-YYYY-MM-DD-vault_score.md'
prompts:
- Assess the health of my Obsidian vault
- Standardize tags across all my vault notes
- Find orphaned notes and suggest connections
- Generate a Map of Content for my knowledge base
- Generate INDEX.md files for profile and product directories so agents stop globbing
- Suggest which directories should have an INDEX.md
---
