---
description: Recurring research cycles — scored, filtered, compared — so you never fall behind.
title: The market moved.
---

# The market moved.

*Recurring Intelligence Cycles*

<div class="video-wrap"><iframe width="100%" height="420" src="https://www.youtube.com/embed/CdGlqzS3AFk?rel=0" title="The market moved." frameborder="0" allowfullscreen loading="lazy"></iframe></div>

> The market moved.
> You found out three months later.

**Outcome:** Recurring research cycles — scored, filtered, compared — so you never fall behind.

| | |
|---|---|
| **Area** | Research |
| **Level** | advanced |
| **Roles** | Head of Marketing, Product Manager |
| **Time savings** | 8 hours manual research → 15 minutes automated |
| **Try it** | "Run a research cycle on procurement-ai" |
| **Compounding** | Each cycle builds on previous — trends emerge over time |
| **Frequency** | Weekly per domain (cron scheduled) |
| **Published** | 2026-03-27 |

## Inputs

- ⚙️ domain-config.md
- 📊 previous_kb_latest.md
- 🎯 scoring_calibration.md

## What BOB does

1. Load domain config + previous KB
2. nlm-skill → deep research (50-70 sources)
3. Import & query NotebookLM notebook
4. Map entries → score with calibrated rubric
5. Delta detection vs previous cycle
6. Review findings, adjust weights
7. Write KB + changelog + briefing

## Outputs

- 📗 kb_2026-03-23.md
- 📋 changelog.md
- 📬 inbox_briefing.md
- 📕 report.pdf

## Benefits

- 32× faster
- Change detection between cycles
- Weighted scoring surfaces what matters

Built on the [continuous-research](../skills/continuous-research.md) skill.
