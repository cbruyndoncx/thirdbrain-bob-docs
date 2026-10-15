---
description: USE WHEN user says "ascii art fixer", "run ascii-art-fixer", or requests similar functionality. Fix alignment and spacing issues in ASCII art diagrams, architecture drawings, and box-and-line visualizations.
title: ascii-art-fixer
---

# ascii-art-fixer

USE WHEN user says "ascii art fixer", "run ascii-art-fixer", or requests similar functionality. Fix alignment and spacing issues in ASCII art diagrams, architecture drawings, and box-and-line visualizations.

- **Area:** Foundational
- **Category:** diagramming
- **Level:** beginner
- **Input:** conversation
- **Output:** diagram
- **Setup:** none
- **Roles:** 

Reviews and fixes ASCII art diagrams with alignment issues.

## How you ask

- “Fix the alignment in this ASCII art diagram”
- “My ASCII architecture diagram has broken box borders — fix them”
- “Clean up the spacing in this text-based flowchart”

## Inputs

- source (Alignment audit) — File containing the ASCII diagram or table to audit
- source (Repair) — File whose ASCII art is misaligned
- target_width — Column width to align to; inferred from the widest row when omitted
- source (Validation) — File to re-check after repair

## Outputs

- audit-report (markdown)
- prefer a permanent directory)
- repaired-art (markdown)
- validation-report (markdown)

