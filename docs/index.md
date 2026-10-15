---
title: START HERE — Wiki
---

# START HERE — Wiki

**The single entry point for everything in this vault.** Pick a path based on where you are.

---

## 🚪 New Here? Pick Your Door

| Your situation | Start here |
|----------------|------------|
| **Done-for-you install** — BOB is already set up, I just want to use it | → [quickstart](02-Setup/quickstart.md) (5 min) |
| **DIY install** — I need to set this up from scratch | → getting_started (vault root) |
| **Curious** — I want to understand what BOB is before I install | → [bob_overview](01-BOB/Onboarding/bob_overview.md) (30 min) |
| **Manual reader** — I want the classical product manual, front to back | → [BOB User Manual](01-BOB/user-manual/index.md) |
| **Daily use** — I'm already using BOB and want to use it better | → [using_bob](03-Learn/using_bob.md) |
| **Concepts** — I want to understand the building blocks | → [playbooks](03-Learn/Concepts/playbooks.md) |
| **Reference** — I'm stuck on a command or path | → [linux_bash_cheatsheet](04-Reference/linux_bash_cheatsheet.md) |
| **Invoking skills** — how do I call a skill in Claude Code vs Codex? | → [skill_invocation_per_agent](04-Reference/skill_invocation_per_agent.md) |

---

## 🗺️ The Three Stages

Most users move through these in order:

```
Stage 1: UNDERSTAND        Stage 2: INSTALL & VERIFY      Stage 3: USE & MASTER
─────────────────────      ────────────────────────       ──────────────────────
bob_overview          →    getting_started          →    quickstart
(what is BOB?)             (full DIY setup)               (first 5 min)
                           or                             ↓
                           DFY install                    using_bob
                                                          (day-to-day)
                                                          ↓
                                                          03-Learn/Concepts
                                                          (deeper patterns)
```

---

## 📁 Folder Structure

```
{vault.wiki}
│
├─ start_here.md ← YOU ARE HERE
│
├─ 01-BOB/Onboarding/            Conceptual foundation
│  ├─ MOC-bob_onboarding.md      Section index
│  ├─ bob_overview.md            What BOB is + 4-layer stack
│  ├─ bob_learning_path.md       Structured 5-step learning sequence
│  └─ environment_checklist.md   Pre-install machine verification
│
├─ 02-Setup/                     Installation guides
│  ├─ quickstart.md              5-min DFY-install verification
│  ├─ symlink_setup.md           Skills folder symlinks
│  ├─ obsidian_cli_setup.md      Obsidian 1.12+ CLI for agents
│  ├─ Obsidian/                  Vault & Obsidian basics
│  └─ AI-Tools/                  Claude Code, ACP plugin
│
├─ 03-Learn/                     Concepts & examples
│  ├─ using_bob.md               Day-to-day usage patterns
│  ├─ Concepts/                  Playbooks, JTBD, tasks
│  └─ Examples/                  Sample skills, diagrams
│
├─ 04-Reference/                 Lookups & cheatsheets
│
└─ 05-Troubleshoot/              Symptom-based fix guides
   ├─ MOC-troubleshoot.md        Index by area
   ├─ ts_install.md              Installation problems
   ├─ ts_agent_client.md         Agent Client / ACP issues
   ├─ ts_skills.md               Skills not loading
   └─ ts_vault.md                Vault & Obsidian issues
```

---

## 📋 Section Summaries

### 01-BOB (Foundation)
What BOB is and how it's structured. Read [bob_overview](01-BOB/Onboarding/bob_overview.md) first; the rest is supporting depth.

### 02-Setup (Installation)
Step-by-step for installing Obsidian, Claude Code, and the ACP plugin on a fresh machine. Skip if you have a done-for-you install.

### 03-Learn (Concepts)
Mental models for working effectively: what playbooks are, how JTBD shapes work, how tasks vs TaskNotes differ. Read these as you encounter the concepts in real work — not all at once.

### 04-Reference (Lookups)
Bash commands, folder structures, permissions. Use search (Ctrl+Shift+F) when you need a specific thing fast.

### 05-Troubleshoot (Fix Guides)
Symptom-based guides covering installation, Agent Client, skills, and vault problems. Start at [MOC-troubleshoot](05-Troubleshoot/MOC-troubleshoot.md) if you're stuck.

---

## 🔗 Section Indexes

Each section has its own MOC for deeper navigation:

- [MOC-bob_onboarding](01-BOB/Onboarding/MOC-bob_onboarding.md) — BOB foundational learning
- [quickstart](02-Setup/quickstart.md) — 5-min install verification (primary 02-Setup entry)
- [README](02-Setup/Obsidian/Onboarding/README.md) — Obsidian-specific onboarding sequence
- [playbooks](03-Learn/Concepts/playbooks.md) — Core concepts entry point
- [linux_bash_cheatsheet](04-Reference/linux_bash_cheatsheet.md) — Reference entry point (use search for specific commands)
- [skill_invocation_per_agent](04-Reference/skill_invocation_per_agent.md) — Skill invocation: `/skill-name` (Claude Code) vs `$skill-name` (Codex)
- [MOC-troubleshoot](05-Troubleshoot/MOC-troubleshoot.md) — Troubleshooting index by area

---

## ❓ Can't Find What You Need?

1. **Search inside files** — `Ctrl+Shift+F` (full-text search)
2. **Graph view** — see related notes visually
3. **Ask BOB** — "Find a guide about X" in the Agent Client panel
4. **Missing entirely?** — create the doc and link it here

---

## Version

| Date | Change |
|------|--------|
| 2026-04-28 | Refactored for end-user audience: added DIY/DFY fork, quickstart and using_bob, removed internal training references |
