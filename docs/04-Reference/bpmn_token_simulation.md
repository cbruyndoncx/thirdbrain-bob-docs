---
title: BPMN plugin — token simulation
---

# BPMN plugin — token simulation

The vault's BPMN plugin (community plugin `bpmn-plugin` by JoLeaf, wraps [bpmn-js](https://bpmn.io))
bundles **`bpmn-js-token-simulation`**, an official bpmn.io extension. It adds an animated play mode
to any `.bpmn` diagram opened in Obsidian. It ships in the plugin — nothing to install or configure
separately.

## What it does

- A **play button** in the diagram toolbar toggles simulation mode.
- Colored **tokens** (small dots) animate along the sequence flows from the start event through
  tasks and gateways to the end event(s), following the diagram's actual flow logic.
- **Exclusive/inclusive gateways** become clickable — pick which branch the token takes, so
  alternate paths can be walked by hand.
- **Parallel gateways** correctly fork a token into multiple simultaneous tokens and rejoin them.
- Tasks can be set to auto-complete or wait for a manual click, so a case can be stepped through
  activity by activity.
- Purely visual and interactive — no execution semantics, no data, nothing written back to the file.
  It is a reviewer's tool for walking a diagram, not a runtime.

## Where it's used

Process Harness compiles governed `process-definition` notes to executable BPMN
(`definition_to_bpmn.py`) at `{company.processes}/diagrams/{process-id}.bpmn`, with gateways,
boundary timer events, and multiple lanes — exactly the shape token simulation is built for. See
`{skills.root}/process-harness/references/lifecycle-state-machine.md` and
`engine-migration-and-deps.md` in the same folder for the full generation and execution design.

**Token simulation confirms the diagram's shape is sane — it does not confirm the runtime engine's
actual execution matches it.** For Process Harness, that correctness claim is made separately by an
automated shadow-diff test (`test_bpmn_engine.py`): the same case driven under both the legacy state
machine and SpiffWorkflow must produce an identical event sequence. Token simulation is a visual
sanity-check; the shadow diff is the record-level proof. Use both — they are complementary, not
redundant.

## Related

- `{skills.root}/process-harness/references/engine-migration-and-deps.md` — where BPMN
  execution sits in the Process Harness design
- `{skills.root}/process-harness/scripts/definition_to_bpmn.py` — the generator that
  produces diagrams worth simulating
