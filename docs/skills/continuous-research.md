---
description: Run recurring research cycles against configurable domain configs. Each cycle discovers new entries, scores them through a weighted quality gate, compares against the previous knowledge base, and writes an updated KB with a change delta.
title: continuous-research
---

# continuous-research

Run recurring research cycles against configurable domain configs. Each cycle discovers new entries, scores them through a weighted quality gate, compares against the previous knowledge base, and writes an updated KB with a change delta.

| | |
|---|---|
| **Area** | Research |
| **Category** | research |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [api-key] |
| **Roles** | [Head of Marketing, Product Manager] |

Runs recurring research cycles in OpenAI, DeepSeek, Perplexity, or Tavily and maintains a scored knowledge base.

## How you ask

- “Run a research cycle for the procurement-ai domain”
- “Set up a new research domain to monitor competitor AI tools in logistics”
- “What's new in the procurement-ai knowledge base since last cycle?”
- “Run all overdue research domains”
- “Generate a PDF report from the latest procurement-ai KB”

## Inputs

- domain-configs — Research domain configs — the cycles available to run.
- domain_id — Research domain to run, matching a config in the research-domains folder (`resource.research-domains`)
- provider — Research backend for this cycle (deepseek, openai, notebooklm, perplexity, tavily). Omit to use the provider recorded on the research-domain record. (deepseek | notebooklm | openai | perplexity | tavily)
- domain-id — loaded from your vault context
- domain-id-changelog — loaded from your vault context
- domain-id-kb-latest — loaded from your vault context
- schedule_filter — Restrict the sweep to domains matching this schedule (e.g. Monday, weekly)
- topic — Ad-hoc topic or question to scan, without creating a persistent domain
- domain_id — Domain whose existing KB entries are to be rescored
- scoring_weights — Override weights per scoring dimension; defaults to the domain config
- domain_id — Domain to report on
- cycle_date — Cycle to report; defaults to the most recent
- name — Human-readable domain name
- scope — What the domain covers and what it deliberately excludes
- provider — Provider used to run the research cycle for this domain (deepseek | notebooklm | openai | perplexity | tavily)
- schedule — Cadence for the recurring cycle (e.g. Monday 08:00)

## Outputs

- Config changes found during the cycle (new search queries), written instead of editing the config; applied at Step 1 of the next cycle.
- Dated knowledge-base snapshot for the cycle, kept beside the overwritten `_kb_latest.md`.
- Per-domain changelog the cycle appends to. Read as context and written on every run.
- Query set written before the provider call.
- Raw findings; derive topic-slug by kebab-casing the topic input.
- domain-config (markdown)
- kb-latest (markdown)
- personal-research (markdown)
- prefer a permanent directory)
- reranked-results (markdown)
- research-all-report (markdown)
- research-cycle-report (markdown)
- research-report-pdf (pdf)
- {input.root}/{domain-id}_cycle_{YYYY-MM-DD}.md
- {me.inbox}/research_{domain-id}_{YYYY-MM-DD}.md
- {resource.research-domains}/{domain-id}.md
- {resource.research-kb}/all_domains_report_{YYYY-MM-DD}.md
- {resource.research-kb}/{domain-id}/cycle_{YYYY-MM-DD}.md
- {resource.research-kb}/{domain-id}/reranked_{YYYY-MM-DD}.md
- {resource.research-kb}/{domain-id}/{domain-id}_changelog.md
- {resource.research-kb}/{domain-id}/{domain-id}_config_proposal_{YYYY-MM-DD}.md
- {resource.research-kb}/{domain-id}/{domain-id}_kb_latest.md
- {resource.research-kb}/{domain-id}/{domain-id}_kb_{YYYY-MM-DD}.md
- {resource.research-kb}/{domain-id}/{domain-id}_report_{YYYY-MM-DD}.pdf

## Seen in these workflows

- [The market moved.](../workflows/continuous-research.md)

