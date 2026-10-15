---
description: What playbooks are, how to run them, how they create TaskNote logs, and
  how the governed process layer works
title: BOB User Manual — 16. Playbooks & Processes
---

# 16. Playbooks & Processes

A skill handles one type of task. A playbook handles a sequence of them.

When your work naturally spans multiple steps — onboard a new client, close the month, run a quarterly business review — a playbook chains the right skills together in the right order, with checkpoints between steps so you stay in control. You do not need to remember the sequence or know which skill does what at each stage. The playbook knows.

## What a playbook is

A playbook is a structured document with four required elements:

| Element | Purpose |
|---------|---------|
| **Trigger** | The event or statement that starts the playbook — what you say or what happens |
| **Outcome** | The concrete result when the playbook is complete |
| **Numbered steps** | An ordered sequence, each step calling one or more skills |
| **Duration** | An honest time estimate so you can plan the session |

Playbooks live in `{company.playbooks}` (the shared library), `{company.processes}/Playbooks/` (company-scoped), and `{me.playbooks}` (personal). The full index is at [PLAYBOOKS](../../03-Learn/Concepts/playbooks.md). A full vault stores over 80 active playbooks.

**Starter vault.** A starter vault stores no playbooks (`{company.playbooks}` ships empty, for your own). The shared playbooks and the value chains are served by the skills MCP server: BOB asks it with `list_playbooks` and `get_playbook` (and `list_value_chains` and `get_value_chain` for value chains), and the server also offers playbooks as MCP prompts. Ask "which playbooks do you have for month-end close?" and BOB looks them up there. A step that names a skill is run locally if the skill is local, otherwise fetched from the server (see [chapter 14](14-skills-system.md)). Your own playbooks stay in your vault.

Each playbook belongs to a value chain — Lead-to-Cash, Deliver-to-Satisfaction, Record-to-Insight, and so on. This is how BOB groups them when you browse or ask for suggestions.

## Running a playbook

Start a playbook the same way you start any BOB request — natural language or an explicit name:

```
Run the monthly close playbook
```

```
/monthly-close
```

BOB loads the playbook, confirms the trigger conditions are met, and begins at step one.

### Checkpoints

Most playbooks include checkpoints between steps — points where BOB pauses, shows you what it has done, and asks for confirmation before proceeding. A checkpoint might look like:

```
Step 3 complete: trial balance reconciled. Differences: none.
Proceed to step 4 (generate financial statements)? [yes / no / stop]
```

Checkpoints exist for a reason. They are the moments where your judgment matters — before BOB writes a file, sends a draft to a folder, or makes a decision that affects live data. Do not skip them reflexively.

If you stop a playbook mid-run, the work completed so far is saved. You can resume by telling BOB which step you were on.

## TaskNotes and the step log

When a playbook runs, BOB creates or updates a **TaskNote** — a note in `{output.tasks}` that tracks the run. The TaskNote's frontmatter links back to the playbook and records the current step and status.

The body of the TaskNote holds the step log: a timestamped record of what was done, which skills were called, what files were written, and any decisions made at checkpoints. This is your audit trail. If you need to explain what was done and when — for a client, a partner, or yourself three months from now — the step log is the record.

The TaskNote stays open (`status: in-progress`) until all steps are complete and the Done When criteria are satisfied. At that point it closes (`status: done`) and the log is final.

## Creating your own playbook

If you repeat a multi-step process regularly and BOB does not have a playbook for it, create one. The structure is the same as any other playbook — trigger, outcome, steps, duration — saved as a Markdown note with `type: playbook` in the frontmatter.

Start from the template in `{vault.templates}` and follow these conventions:

| Field | Required | Example |
|-------|----------|---------|
| `trigger` | Yes | `"End of quarter — run QBR with client"` |
| `outcome` | Yes | `"QBR document delivered and next quarter agreed"` |
| `total-steps` | Yes | `7` |
| `status` | Yes | `draft` (change to `active` when tested) |

Save the file to `{me.playbooks}` for personal use or `{company.processes}/Playbooks/` for shared use. Once saved, BOB can find and run it by name.

Personal playbooks are not quality-scored by the QMS — they are yours to maintain. If a personal playbook proves stable and useful across multiple runs, it is a candidate for promotion to the shared library.

## The governed process layer

Playbooks cover most repeatable work. For processes that require tighter governance — defined policies, event logging, compliance evidence, or formal cost tracking — BOB supports a more structured layer: **process definitions** and **process runs**.

### Process definitions

A process definition (`type: process-definition`) is a formal specification of a business process. It binds specific activities to specific skills, declares the value chain it serves, and attaches policies — rules that must hold true at each phase, with explicit breach conditions and consequences.

Process definitions live in `{company.processes}/definitions/{process-id}/`. You would typically use a process definition for work that is audited, regulated, or financially material: period close, procurement approval, payroll.

### Process runs

Each time a governed process executes, BOB creates a **process run** (`type: process-run`) in `{company.runs}`. The run note tracks the case ID, start time, current state, and halt count. Alongside it, BOB writes an event log (a JSONL file) that is the authoritative record of everything that happened: every activity, every policy check, every cost.

The note is a readable view of the run; the event log is the source of truth. If there is ever a discrepancy, the event log wins.

For most day-to-day work, playbooks are the right tool. Move to process definitions and runs when you need the formal audit trail, policy enforcement, or AI cost tracking per case that the governed layer provides.

