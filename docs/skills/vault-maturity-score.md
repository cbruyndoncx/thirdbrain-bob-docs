---
description: Quantifies how much accumulated context a ThirdBrain vault has, broken down across the foundation (company-level context), each active client, and the coverage of declared skill inputs. Produces a dated Markdown report that makes accumulation visible and rewarding — partners can watch the score climb as they fill out ICP fragments, client profiles, meeting histories, and feedback notes.
title: vault-maturity-score
---

# vault-maturity-score

Quantifies how much accumulated context a ThirdBrain vault has, broken down across the foundation (company-level context), each active client, and the coverage of declared skill inputs. Produces a dated Markdown report that makes accumulation visible and rewarding — partners can watch the score climb as they fill out ICP fragments, client profiles, meeting histories, and feedback notes.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | utilities |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [CEO / Founder] |

Measures vault context two ways — supply (how much context exists against what skills declare they need) and demand (which context agents actually read and edited, from…

## How you ask

- “Baseline vault maturity”
- “Context accumulation”
- “Skill coverage”
- “Which context notes do we actually use”
- “What company knowledge has gone cold”

## Inputs

- vault — Vault root path (defaults to $VAULT_PATH, else the vault found above the working directory)
- substance-words — Minimum word count for a context file to count as 'present with substance' (default 50)
- days — Log window in days (default 400 — spans the full ACP archive)
- half-life — Recency half-life in days (default 45)
- scope — Top-level folders to rank (default {me.root} {company.root} {company.clients})
- edit-weight — Weight of an edit (default 3.0; use 0 for the skills corpus)

## Outputs

- CONTEXT-USAGE.md
- Dependency graph written by the parse phase (`parse_skill_inputs.py`) from every skill's declared inputs, with per-path `path_scopes`; the scoring phase reads it. Overwritten each run after a timestamped backup.
- latest (json)
- maturity-report (markdown)
- snapshot (json)
- usage-ledger (jsonl-gz)
- usage-report (markdown)
- usage-snapshot (json)
- {company.qms.maturity}/latest.json
- {company.qms.maturity}/skill-dependencies.json
- {company.qms.maturity}/snapshots/{YYYY-MM-DD}-usage.json
- {company.qms.maturity}/snapshots/{YYYY-MM-DD}.json
- {company.qms.maturity}/usage-ledger.jsonl.gz
- {company.qms.maturity}/{YYYY-MM-DD}-maturity-report.md

