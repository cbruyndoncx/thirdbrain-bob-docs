---
title: Skill Upgrade Cycle
---

# Skill Upgrade Cycle

*One skill is upgraded with current behavior evidence, validation, and a recorded QMS gate result*

> It worked last quarter. Nobody has checked since.

| | |
|---|---|
| **Area** | Foundational |
| **Time savings** | Typical run: 45-90 minutes, 1 session |
| **Try it** | "A governed skill needs inspection, patching, verification, and QMS evidence" |
| **Compounding** | Each run refines templates and context — 5 automated steps improve with accumulated data |
| **Frequency** | Per trigger event |

## Inputs

- 👤 Skill name and path
- 📋 Reproduced defect or requested improvement
- 🧪 Local test command or fixture route
- 📋 Any owner decision required before behavior or external publication changes

## What BOB does

1. vault-preflight → confirm the skill path, local instructions, current QMS mapping, and available test fixtures
2. skillsmith → inspect the current SKILL.md, scripts, references, and existing functional tests
3. qms-skill-management → compare the skill against its live CLI/docs and QMS registration
4. Apply the smallest scoped patch and run the skill's local test route
5. vault-validator → validate modified vault notes and generated metadata
6. qms-quality → run the QMS gate, save the evidence note, and record follow-up work

