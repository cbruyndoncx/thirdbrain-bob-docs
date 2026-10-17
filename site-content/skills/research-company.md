---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: research-company — ThirdBrain BOB skill
  description: Comprehensive company intelligence research and report generation for any company and industry.
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: research-company
catLabel: research
area: research
desc: Conducts comprehensive company intelligence research and generates detailed reports including competitor analysis, industry insights, USP profiling, growth…
summary: Comprehensive company intelligence research and report generation for any company and industry.
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Head of Sales]'
inputs:
- scope — `company`, or a client-id under the clients root (`client.root`) — a string with one reserved value, not a closed set
outputs:
- Existing client profile, appended with the report's key insights after the run.
- Optional Step 7 detailed PDF of the report, only after the Step 6 checkpoint passes.
- Optional Step 7 presentation built with gamma-presenter, only after the Step 6 checkpoint passes.
- Post-research SWOT, competitor analysis and growth opportunities notes, one file each.
- Post-research executive summary and action plan, one file each.
- Step 6 intelligence report — company snapshot, competitor intelligence, industry trends, growth opportunities, AI/automation. The alternate sink is the company-scope run.
- '{client.analysis}/{analysis-doc}.md'
- '{client.deliverables}/company_research_deck.pptx'
- '{client.deliverables}/company_research_report.pdf'
- '{client.deliverables}/{summary-doc}.md'
- '{client.profile}'
- '{client.research}/company_research_report.md'
prompts:
- Research Acme Corp and generate an intelligence report
- Analyze the competitive landscape for this industry
- Create a company profile with growth opportunities and AI recommendations
- Run a full company analysis including USP profiling
---
