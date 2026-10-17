---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: ascii-art-fixer — ThirdBrain BOB skill
  description: USE WHEN user says "ascii art fixer", "run ascii-art-fixer", or requests similar functionality. Fix alignment and spacing issues in ASCII art diagrams, architec
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: ascii-art-fixer
catLabel: diagramming
area: foundational
desc: Reviews and fixes ASCII art diagrams with alignment issues.
summary: USE WHEN user says "ascii art fixer", "run ascii-art-fixer", or requests similar functionality. Fix alignment and spacing issues in ASCII art diagrams, architecture drawings, and box-and-line visualizations.
difficulty: beginner
inputType: conversation
outputType: diagram
requires: '[none]'
roles: '[]'
inputs:
- source (Alignment audit) — File containing the ASCII diagram or table to audit
- source (Repair) — File whose ASCII art is misaligned
- target_width — Column width to align to; inferred from the widest row when omitted
- source (Validation) — File to re-check after repair
outputs:
- audit-report (markdown)
- prefer a permanent directory)
- repaired-art (markdown)
- validation-report (markdown)
prompts:
- Fix the alignment in this ASCII art diagram
- My ASCII architecture diagram has broken box borders — fix them
- Clean up the spacing in this text-based flowchart
---
