---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: hewitt-ralph — ThirdBrain BOB skill
  description: RALPH (Repeated Autonomous Loop for PRD Handling) implements coding tasks using strict test-driven development — write a failing test, make it pass, refactor, r
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: hewitt-ralph
catLabel: development
area: foundational
desc: Autonomous TDD coding loop — runs tests, writes code, runs tests again, iterates until passing.
summary: RALPH (Repeated Autonomous Loop for PRD Handling) implements coding tasks using strict test-driven development — write a failing test, make it pass, refactor, repeat. Adapted from [Craig Hewitt's Ralph skill](https://github.com/thecraighewitt/skills).
difficulty: advanced
inputType: conversation
outputType: document
requires: '[install]'
roles: '[Product Manager]'
inputs:
- task_description — What to implement — a user story, issue description, or task spec
- project_path — Absolute path to the project being worked on
- task_list — List of tasks to implement — can be a markdown checklist, issue list, or PRD
- 'max_iterations — Maximum iterations before stopping (default: 10)'
outputs:
- Full loop log with all iterations, tests, and commits
- Log of what was implemented, tests written, and commit made
- prefer a permanent directory)
prompts:
- Ralph
- TDD loop
- Red-green-refactor
---
