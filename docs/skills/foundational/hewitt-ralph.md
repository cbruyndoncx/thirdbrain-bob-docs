---
description: RALPH (Repeated Autonomous Loop for PRD Handling) implements coding tasks using strict test-driven development — write a failing test, make it pass, refactor, repeat. Adapted from [Craig Hewitt's Ralph skill](https://github.com/thecraighewitt/skills).
title: hewitt-ralph
---

# hewitt-ralph

RALPH (Repeated Autonomous Loop for PRD Handling) implements coding tasks using strict test-driven development — write a failing test, make it pass, refactor, repeat. Adapted from [Craig Hewitt's Ralph skill](https://github.com/thecraighewitt/skills).

- **Area:** Foundational
- **Category:** development
- **Level:** advanced
- **Input:** conversation
- **Output:** document
- **Setup:** install
- **Roles:** Product Manager

Autonomous TDD coding loop — runs tests, writes code, runs tests again, iterates until passing.

## How you ask

- “Ralph”
- “TDD loop”
- “Red-green-refactor”

## Inputs

- task_description — What to implement — a user story, issue description, or task spec
- project_path — Absolute path to the project being worked on
- task_list — List of tasks to implement — can be a markdown checklist, issue list, or PRD
- max_iterations — Maximum iterations before stopping (default: 10)

## Outputs

- Full loop log with all iterations, tests, and commits
- Log of what was implemented, tests written, and commit made
- prefer a permanent directory)

