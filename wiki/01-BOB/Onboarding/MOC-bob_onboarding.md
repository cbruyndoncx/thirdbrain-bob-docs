---
type: knowledge-base
title: "Map of Content — BOB Onboarding"
status: final
created: 2026-04-27
modified: 2026-04-27
tags: [bob, moc, onboarding, guide]
---

# BOB Onboarding — Map of Content

Central entry point for anyone getting started with BOB (Business Operating Brain). These materials form the foundation for understanding the system, verifying your environment, and preparing for installation.

---

## Quick Navigation

| Resource | Purpose | Time |
|----------|---------|------|
| [[bob_learning_path]] | Structured learning sequence (5 steps) | 5–8 hours |
| [[bob_overview]] | Conceptual foundation (what + why) | 30–45 min |
| [[environment_checklist]] | Pre-flight verification | 45–60 min |

---

## Content Structure

```
BOB Onboarding
│
├─ bob_learning_path.md (START HERE)
│  └─ Structured 5-step sequence:
│     1. Read BOB Overview
│     2. Research tech stack
│     3. Verify environment
│     4. Terminal basics
│     5. Ready for installation
│
├─ bob_overview.md (Step 1 reading)
│  └─ What is BOB?
│     • Business problem + solution
│     • 4-layer tech stack
│     • Data flow & skills
│     • Business applications
│
└─ environment_checklist.md (Step 3)
   └─ Pre-flight verification
      • OS & WSL2
      • Programming languages (Node, Python, git)
      • System resources
      • Version tracking
```

---

## How to Use This MOC

### New to BOB

1. **Start with [[bob_learning_path]]** — it guides you through all steps
2. **Follow the 5-step sequence** — each step builds on the previous one
3. **Use [[bob_overview]] as reference** throughout
4. **Run [[environment_checklist]]** when instructed in Step 3
5. **You're ready for installation** when all 5 steps are complete

### Technical Lead Onboarding Someone

1. **Share [[bob_learning_path]]** with your team member
2. **Set a timeline** (suggest 5–8 hours over several days)
3. **Check in** after Step 1 (BOB Overview) to answer questions
4. **Review Step 3 results** (environment checklist) to understand what needs installing
5. **Move to installation phase** once all 5 steps are done

### Planning a Team Rollout

1. **Use bob_learning_path as template** for your team's onboarding
2. **Adjust timeline** for your context (intensive vs self-paced)
3. **Set up check-in schedule** if needed (weekly reviews, office hours, etc.)
4. **Collect feedback** on what's clear vs what needs clarification
5. **Iterate** — these materials improve with real usage

---

## Core Materials

### bob_learning_path.md
**Purpose**: Guided onboarding sequence  
**Audience**: Anyone new to BOB  
**Content**: 5-step learning path with time estimates, key concepts, and next steps  
**Length**: ~2000 words  
**Deliverables**: Completed each step (concept understanding, diagram, environment check results)  
**Prerequisites**: None

### bob_overview.md
**Purpose**: Conceptual foundation  
**Audience**: Technical and non-technical users  
**Content**: What BOB is, how it differs from ChatGPT, 4-layer tech stack, business applications  
**Length**: ~3500 words (30–45 min read)  
**Key sections**: Business problems, tech stack explanation, data flow, skills concept  
**Prerequisites**: None (written for complete beginners)

### environment_checklist.md
**Purpose**: Pre-flight verification  
**Audience**: Anyone preparing to install BOB  
**Content**: Command-by-command checks for OS, WSL2, programming languages, git, disk space, RAM  
**Length**: ~2000 words  
**Deliverable**: Completed summary table (pass/fail, version numbers)  
**Prerequisites**: Terminal access, basic familiarity with running commands

---

## Typical Adoption Timeline

| Phase | Materials | Duration | Outcome |
|-------|-----------|----------|---------|
| **Onboarding** | bob_learning_path + bob_overview + environment_checklist | 5–8 hours | Understand system, verify environment ready |
| **Installation** | [[getting_started]] (DIY) or DFY setup | 2–4 hours | All components installed & running |
| **First Run** | [[quickstart]] | 30 min | Successfully ask BOB a business question |
| **Learning Skills** | Skills documentation | Ongoing | Use BOB for real work |

---

## Related Resources

**In this vault:**
- [[getting_started]] — General vault setup (Obsidian, plugins, CLI)
- [[claude-code-installation-on-windows-using-wsl]] — Windows/WSL technical details
- [[agent-client-installation]] — ACP plugin setup
- [[obsidian-architecture]] — How Obsidian works (visual)
- [[linux_bash_cheatsheet]] — Terminal command reference

**External:**
- [Obsidian Docs](https://obsidian.md/docs) — Official Obsidian documentation
- [Claude Code Docs](https://code.claude.com) — Official Claude Code documentation
- [ACP Specification](https://agentclientprotocol.com) — Agent Client Protocol standard

---

## Feedback & Iteration

These materials are living documents. If you find something:
- **Unclear**: Note what confused you and suggest clearer language
- **Missing**: Identify what you needed but didn't find
- **Wrong**: Flag inaccuracies

Share feedback so these materials improve for the next person.

---

## Version History

| Date | Change | Author |
|------|--------|--------|
| 2026-04-27 | Initial materials created: BOB Overview, Environment Checklist, Learning Path | Carine Bruyndoncx |

