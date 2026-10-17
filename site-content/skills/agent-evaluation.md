---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: agent-evaluation — ThirdBrain BOB skill
  description: 'Target Audience: Founders, operators, and team leads evaluating AI agent tools for knowledge work delegation.'
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: agent-evaluation
catLabel: utilities
area: foundational
desc: Evaluate AI agent tools against three structural dimensions (Persistent Memory, Inspectable Surfaces, Compounding Context) and generate calibrated delegation specs.
summary: 'Target Audience: Founders, operators, and team leads evaluating AI agent tools for knowledge work delegation.'
difficulty: beginner
inputType: conversation
outputType: document
requires: '[none]'
roles: '[CEO / Founder, Product Manager, Operations Manager]'
inputs:
- tool-name — Name of the agent tool being evaluated
- task-description — Specific task or workflow intended for delegation
- quality-definition — What 'good' looks like for this task
- tools — Comma-separated list of tool names to compare
- task-description — The task all tools will be evaluated against
outputs:
- comparison (markdown)
- scorecard (markdown)
- '{company.decisions}/agent-comparison-{YYYY-MM-DD}.md'
- '{company.decisions}/agent-eval-{tool-slug}-{YYYY-MM-DD}.md'
prompts:
- Evaluate this agent
- Should I use this tool
- Agent comparison
---
