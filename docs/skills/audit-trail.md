---
description: USE WHEN user says "audit trail", "run audit-trail", "agent logs", "session logs", "trace", "debug history", "activity log", or requests similar functionality. Extract and analyze audit information from Agent Client Logfiles for compliance, decision reconstruction, and quality review.
title: audit-trail
---

# audit-trail

USE WHEN user says "audit trail", "run audit-trail", "agent logs", "session logs", "trace", "debug history", "activity log", or requests similar functionality. Extract and analyze audit information from Agent Client Logfiles for compliance, decision reconstruction, and quality review.

| | |
|---|---|
| **Area** | Operations |
| **Category** | qms |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [] |

Extracts audit information from Claude Code and Agent Client Logfiles, including decisions, reasoning, tool calls, and session metadata.

## How you ask

- “Extract audit information from my agent session logs”
- “Reconstruct the decisions made during this AI-assisted session”
- “Generate a compliance report from agent client logfiles”
- “Analyze the tool calls and reasoning from my last session”

## Inputs

- session-selector — Session ID, log filename, or exact date identifying the one session to reconstruct.
- request — What the reconstruction needs to answer about this session — e.g. which decision or tool sequence to surface.
- scope — Output-path scope — `company`, or a client-id under {company.clients}/. Controls where the report is written, not which sessions are read; read scope is filtered separately when scope is client-scoped.
- log-corpus — Session log files searched to find and reconstruct the selected session.
- output-depth — How much detail the report includes — summary gives scope/session/outcome/limitations only, full adds decisions/tool-operations/files-touched/gaps, raw lists the matching session and the exact grep/query used instead of a narrative report. (summary | full | raw)
- compliance-filter — Client, agent type, or date period the compliance review spans.
- request — The compliance question to answer — e.g. what AI assistance was used, for whom, and over what window.
- log-corpus — Session log files searched across the requested window, client, or agent type.
- output-depth — How much detail the report includes — summary gives scope/session/outcome/limitations only, full adds decisions/tool-operations/files-touched/gaps, raw lists the matching sessions and the exact grep/query used instead of a narrative report. (summary | full | raw)
- target-file — Vault-relative path of the file or deliverable whose creation history is being traced.
- request — What the trace needs to answer — e.g. who changed the file, when, or how the current version was produced.
- log-corpus — Session log files searched for mentions of the target file's path.
- failure-filter — Session, date range, or client narrowing which failed or blocked operations to search for; omitted searches the full log corpus for failures.
- request — What failure or blocker the investigation needs to explain.
- log-corpus — Session log files searched for failed tool-call statuses and parsing gaps.

## Outputs

- Compliance report aggregating sessions across the requested client, period, or agent type, with gaps and partial coverage called out.
- Failed operations, parsing gaps, and broken output surfaced first, with the sessions and timestamps they occurred in.
- Session metadata, user requests, decisions, tool operations, files touched, and outcome summary for the one traced session.
- Trace of the sessions, requests, and tool calls that produced or modified the named file, in chronological order.
- {scope.qms.root}/audit-trail-{YYYY-MM-DD}.md

