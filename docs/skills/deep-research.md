---
description: Run one foreground research job, wait for the result, and return the saved markdown report.
title: deep-research
---

# deep-research

Run one foreground research job, wait for the result, and return the saved markdown report.

| | |
|---|---|
| **Area** | Research |
| **Category** | research |
| **Level** | advanced |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [api-key] |
| **Roles** | [CEO / Founder, Head of Marketing, Product Manager] |

Runs OpenAI, DeepSeek, or Perplexity research jobs and saves cited markdown reports.

## How you ask

- “Research the current state of AI video generation tools”
- “Run a deep investigation comparing React vs Vue for our project”
- “Synthesize multiple sources on remote work productivity trends”
- “Generate a comprehensive research report on competitor strategies”

## Inputs

- request — The research question to send to the provider.
- provider — Which research backend to use — openai for slower deep synthesis (10-20 min, needs poll), deepseek for a fast general pass (1-2 min), perplexity for current, web-cited results returned in seconds via MCP. (openai | deepseek | perplexity)
- query-template — Override template ID (e.g. 'T05') to force a specific query template instead of the auto-matched one, or 'skip template' to send the raw query.
- request — The delta question describing what should be added or changed versus the prior report.
- prior-report — Previous research output being amended; read back to formulate the delta query and merge new findings into it.
- provider — Which research backend to run the follow-up query against — normally the same provider the prior report used. (openai | deepseek | perplexity)
- query-template — Override template ID to force a specific query template for the delta query, or 'skip template' to send it raw.
- job-id — Job ID from a prior new-run launch (e.g. 'resp_abc123') identifying the openai request to check.
- provider — Which backend the job was launched against; deepseek and perplexity have no poll route because they return synchronously. (openai)

## Outputs

- Newly generated, cited research report answering the request.
- Research report retrieved once the polled job completes; on timeout no file is written and retry instructions are returned instead.
- Updated research report merging new findings into the prior output, with changes highlighted.
- prefer a permanent directory)

