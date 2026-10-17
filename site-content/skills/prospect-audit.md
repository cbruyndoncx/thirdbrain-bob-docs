---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: prospect-audit — ThirdBrain BOB skill
  description: Full prospect research and scoring engine. Launches 5 parallel analysis agents, aggregates results into a weighted Prospect Score (0–100), and produces an actio
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: prospect-audit
catLabel: sales
area: sales
desc: Full prospect audit with parallel agent analysis — produces a PDF audit report with a 0-100 Prospect Score, grade, and action recommendations across 5 weighted…
summary: Full prospect research and scoring engine. Launches 5 parallel analysis agents, aggregates results into a weighted Prospect Score (0–100), and produces an actionable prospect analysis report.
difficulty: intermediate
inputType: conversation
outputType: document
requires: '[none]'
roles: '[Head of Sales]'
inputs:
- brand-theme — Brand theme applied to the audit PDF.
- company — Prospect company to audit
- url — Company website; when absent, Step 2 finds the official site by web search
- icp — ICP definition — frames the prospect fit dimension.
- profile — Our company profile — provides seller identity for the audit.
- offerings — Offerings catalogue — scores prospect interest against what we sell.
- marketing-context — Positioning context — anchors the competitive dimension.
- focus_area — Single dimension to audit — e.g. web presence, hiring, tech stack
outputs:
- company-lead-note (markdown)
- company-lead-pdf (pdf)
- prospect-analysis (markdown)
- prospect-analysis-pdf (pdf)
- '{client.sales}/prospect_analysis.md'
- '{client.sales}/prospect_analysis.pdf'
- '{lead.profile}'
- '{lead.root}/prospect_analysis.pdf'
prompts:
- Audit this prospect and give me a score
- Should we pursue Acme Corp? Run a full prospect analysis
- Score this company across all 5 analysis dimensions
- Evaluate this lead with a comprehensive prospect audit
---
