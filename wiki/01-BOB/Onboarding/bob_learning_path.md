---
type: knowledge-base
title: "BOB Learning Path — Getting Started"
status: final
created: 2026-04-27
modified: 2026-04-27
tags: [bob, onboarding, learning, userguide]
---

# BOB Learning Path — Getting Started

A structured learning sequence for anyone adopting BOB. Follow these steps to understand the system, verify your environment, and prepare for installation.

---

## Overview

The learning path has **5 core steps** that build on each other:

1. **Understand what BOB is** — conceptual foundation
2. **Understand the tech stack** — how layers work together
3. **Verify your environment** — pre-flight checks
4. **Get comfortable with terminals** — hands-on practice
5. **Ready for installation** — next phase

**Time estimate**: 5–8 hours total (can be done at your own pace)

---

## Step 1: Read BOB Overview

**Time**: 30–45 minutes

Read [[bob_overview]] carefully. This covers:
- What BOB is and what problems it solves
- How BOB differs from ChatGPT
- The 4-layer tech stack (Obsidian → ACP → Claude Code → API)
- The data flow (question → search → skill → answer)
- Real business applications across sales, marketing, ops, finance, HR, strategy

**What to do:**
- Read through without rushing
- If a section is unclear, re-read it or research the concept independently
- Note 2–3 concepts that surprised you or felt confusing
- You now understand BOB conceptually

---

## Step 2: Research the Tech Stack

**Time**: 1–2 hours

Deep-dive into each of the 4 layers:

| Layer | What to Research | Key Questions |
|-------|------------------|----------------|
| **Obsidian** | Knowledge management, markdown, local-first | What is a vault? Why not cloud storage? What are plugins? |
| **ACP Plugin** | Agent Client Protocol, Obsidian integration | How does a plugin extend Obsidian? What does ACP do? |
| **Claude Code** | AI agent engine, decision-making | How is an agent different from a chatbot? What does "search" mean here? |
| **API Layer** | Anthropic, OpenAI, Gemini models | Why can you swap the AI model? What's the difference? |

**What to do:**
- Use the [[bob_overview]] as reference for what each layer does
- Read official docs or blog posts for deeper understanding
- Draw or sketch a simple tech stack diagram showing the 4 layers + data flow
- You now understand how the pieces fit together

---

## Step 3: Verify Your Environment

**Time**: 45–60 minutes

Run the [[environment_checklist]] to verify your machine has the required tools.

**What to do:**
1. Open a terminal (PowerShell on Windows, Terminal on Mac/Linux)
2. Follow each check in the checklist
3. Note the version numbers and pass/fail status
4. Fill in the summary table
5. If anything is missing, note it (you don't need to fix it yet)

**Outcome**: You now know what's on your machine and what you'll need to install

---

## Step 4: Terminal Basics

**Time**: 1–1.5 hours

Get comfortable running commands in a terminal. You'll need this for installation and troubleshooting.

**Key commands to practice:**

| Command | What it does | Practice |
|---------|--------------|----------|
| `pwd` | Print working directory | Run it; see your current path |
| `ls` or `dir` | List files | Navigate to a folder and list contents |
| `cd <folder>` | Change directory | Move into a subfolder |
| `node --version` | Check version | Verify software is installed |
| `mkdir <name>` | Create folder | Make a test folder |
| `cat <file>` | Read file | View a text file |

**What to do:**
- Open a terminal
- Run at least 5–10 of the commands above
- Try navigating folders, checking versions, creating files
- Get a feel for how commands work
- You now have basic terminal confidence

---

## Step 5: Ready for Installation

**Time**: 0 minutes (this is your checkpoint)

If you've completed Steps 1–4:

✅ You understand what BOB is  
✅ You understand the 4-layer tech stack  
✅ You verified your environment  
✅ You're comfortable with terminal basics  
✅ You know what's missing on your machine  

You're now ready for the **installation phase** — which provides step-by-step instructions for installing Obsidian, Claude Code, the ACP plugin, and this vault.

---

## How to Use This Path

### Self-Directed Learning
- Go through steps at your own pace
- Spend more time on steps that are confusing
- Use external resources (official docs, YouTube, blogs) to deepen understanding
- Note questions for your technical lead or team

### Guided Learning (with a technical lead)
- Technical lead assigns the path and sets a timeline
- Complete each step, sharing results (BOB overview notes, tech stack diagram, environment checklist)
- Technical lead reviews and provides feedback
- Ask questions async or in check-in calls

### Part of a Larger Program
- This path is Step 1 of a larger onboarding program
- After completing this path, you move to the installation phase
- Results from Step 3 (environment check) inform what gets installed in later phases

---

## Reference Materials

| Topic | Document | Time |
|-------|----------|------|
| BOB Overview | [[bob_overview]] | 30 min |
| Environment Check | [[environment_checklist]] | 45 min |
| Obsidian Getting Started | [[getting_started]] | 20 min |
| Claude Code Setup | [[claude-code-installation-on-windows-using-wsl]] | Reference |
| Terminal Cheatsheet | [[linux_bash_cheatsheet]] | Reference |
| Obsidian Architecture | [[obsidian-architecture]] | 10 min |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| BOB Overview is confusing | Re-read section; research the specific concept (Obsidian, Claude Code, etc.) |
| Don't know what to research | Use the "Key Questions" table in Step 2 as a guide |
| Environment check commands fail | See [[environment_checklist#Troubleshooting Commands]] |
| Not comfortable with terminal | Practice more commands; reach out for help |
| Don't understand the data flow | Draw it out; the [[bob_overview]] has a step-by-step example |

---

## What's Next

Once you've completed this learning path:

- **Installation**: see [[../../getting_started]] (full DIY) or jump to [[../../quickstart]] if you have a done-for-you install
- **First Run**: see [[../../quickstart]] — verify your install in 5 minutes
- **Day-to-Day Use**: see [[../../03-Learn/using_bob]] — patterns for real business work
- **Advanced Topics**: skills customization, vault management, multiple AI providers

The learning path is the foundation. Everything after builds on this understanding.

