# Choosing Your AI Knowledge Base Folder Structure

**Purpose:** Share this file with your AI assistant (Claude Code, Codex CLI, etc.) to help it create the right folder structure for your needs.

---

## How to Use This Reference

Tell your AI:
> "Read this reference file and help me create a folder structure based on my role: [describe yourself]"

The AI will recommend and create an appropriate structure.

---

## The Essential Files (Required for All Structures)

No matter which structure you choose, you need these files at the root:

```
📄 AGENTS.md        # Universal AI context (all tools read this)
📄 CLAUDE.md        # Claude-specific instructions (optional)
📄 CODEX.md         # Codex/GPT-specific instructions (optional)
📄 GEMINI.md        # Gemini-specific instructions (optional)
```

**AGENTS.md** is the universal context file. Tool-specific files extend it for customization.

---

## Popular Folder Structure Systems

### 1. PARA Method (Tiago Forte)

**Best for:** General productivity, life management, mixed personal/professional use

```
📁 your-vault/
├── 📁 Projects/        # Active, time-bound work with deadlines
├── 📁 Areas/           # Ongoing responsibilities (Health, Finance, Career)
├── 📁 Resources/       # Reference material, topics of interest
├── 📁 Archive/         # Completed or inactive items
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

**Philosophy:** Organize by actionability, not topic. Projects are active, Areas are ongoing, Resources are reference, Archive is done.

---

### 2. Johnny Decimal

**Best for:** People who want strict organization, large file collections, team environments

```
📁 your-vault/
├── 📁 10-19 Administration/
│   ├── 📁 11 Company/
│   ├── 📁 12 Finance/
│   └── 📁 13 Legal/
├── 📁 20-29 Clients/
│   ├── 📁 21 Active Clients/
│   └── 📁 22 Past Clients/
├── 📁 30-39 Projects/
│   ├── 📁 31 Current/
│   └── 📁 32 Completed/
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

**Philosophy:** Every item gets a unique ID (XX.XX). Maximum 10 areas, 10 categories per area. Forces constraints to prevent sprawl.

---

### 3. ACE Method (Nick Milo)

**Best for:** Obsidian power users, networked thinking, knowledge workers

```
📁 your-vault/
├── 📁 Atlas/           # Maps of Content, indexes, navigation
├── 📁 Calendar/        # Time-based notes (daily, weekly, meetings)
├── 📁 Efforts/         # Active work, projects, initiatives
├── 📁 Sources/         # Books, articles, references (optional)
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

**Philosophy:** Atlas = navigation layer, Calendar = time layer, Efforts = action layer. Relies heavily on linking between notes.

---

### 4. Minimal / Steph Ango Approach

**Best for:** Beginners, people who over-engineer, bottom-up thinkers

```
📁 your-vault/
├── 📁 notes/           # All your notes, flat
├── 📁 daily/           # Daily notes (YYYY-MM-DD.md)
├── 📁 templates/       # Note templates
├── 📁 attachments/     # Images, PDFs, files
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

**Philosophy:** Start simple, add structure only when needed. Use links and tags over folders. Let organization emerge from usage.

---

## Role-Based Starter Templates

### For Consultants / Agencies

```
📁 your-vault/
├── 📁 00-INBOX/            # Quick capture
├── 📁 10-CLIENTS/          # Client workspaces
│   ├── 📁 client-alpha/
│   │   ├── context.md      # Client background
│   │   ├── projects/       # Their projects
│   │   └── meetings/       # Meeting notes
│   └── 📁 client-beta/
├── 📁 20-INTERNAL/         # Your business operations
│   ├── processes/
│   ├── templates/
│   └── finance/
├── 📁 30-KNOWLEDGE/        # Reference & learning
├── 📁 40-ARCHIVE/          # Completed work
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

---

### For Content Creators / YouTubers

```
📁 your-vault/
├── 📁 00-INBOX/            # Ideas, inspiration
├── 📁 10-CONTENT/          # Content by status
│   ├── 📁 ideas/           # Raw ideas
│   ├── 📁 drafts/          # In progress
│   ├── 📁 ready/           # Ready to publish
│   └── 📁 published/       # Live content
├── 📁 20-AUDIENCE/         # Community, comments, feedback
├── 📁 30-BRAND/            # Style guides, assets, voice
├── 📁 40-RESEARCH/         # Topics, trends, competitors
├── 📁 50-BUSINESS/         # Sponsors, analytics, revenue
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

---

### For Developers / Engineers

```
📁 your-vault/
├── 📁 00-INBOX/            # Quick notes, snippets
├── 📁 10-PROJECTS/         # Active project docs
│   ├── 📁 project-x/
│   │   ├── architecture.md
│   │   ├── decisions.md    # ADRs
│   │   └── todos.md
│   └── 📁 project-y/
├── 📁 20-LEARNING/         # Tech notes, tutorials, TILs
├── 📁 30-REFERENCE/        # Docs, cheatsheets, configs
├── 📁 40-TEMPLATES/        # Code templates, boilerplate
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

---

### For Knowledge Workers / Researchers

```
📁 your-vault/
├── 📁 00-INBOX/            # Capture everything
├── 📁 10-PROJECTS/         # Active research/work
├── 📁 20-NOTES/            # Evergreen notes (Zettelkasten-style)
├── 📁 30-SOURCES/          # Books, papers, articles
├── 📁 40-OUTPUTS/          # Writing, presentations, deliverables
├── 📁 50-META/             # Templates, workflows, logs
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

---

### For Solopreneurs / Small Business

```
📁 your-vault/
├── 📁 00-INBOX/            # Quick capture
├── 📁 10-BUSINESS/         # Core business
│   ├── strategy/
│   ├── finance/
│   └── operations/
├── 📁 20-CLIENTS/          # Client work (if applicable)
├── 📁 30-MARKETING/        # Content, campaigns, brand
├── 📁 40-PRODUCTS/         # Products/services
├── 📁 50-LEARNING/         # Skills, courses, notes
├── 📁 60-PERSONAL/         # Personal notes (optional)
├── 📄 AGENTS.md
└── 📄 CLAUDE.md
```

---

## Principles for Any Structure

### 1. Start Simple, Evolve
Don't create 50 folders on day one. Start with 3-5, add when you feel friction.

### 2. Numbered Prefixes (Optional but Helpful)
`10-`, `20-`, `30-` keeps folders in order regardless of name. Skip numbers (10, 20, 30 not 1, 2, 3) to leave room for insertion.

### 3. INBOX is Your Friend
A catch-all folder for quick capture. Process weekly. Prevents "where does this go?" paralysis.

### 4. Flat > Deep
2-3 levels max. Deep nesting = lost files. If you're going 4+ levels deep, rethink the structure.

### 5. The Folder Isn't the Point
The AI reads AGENTS.md regardless of folder structure. The structure helps YOU navigate. The AI just needs good context files.

---

## Quick Decision Guide

| If you are... | Start with... |
|---------------|---------------|
| Unsure / new to this | **Minimal** (notes, daily, templates, attachments) |
| A consultant with clients | **Client-based** structure |
| A content creator | **Content pipeline** structure |
| A developer | **Project-based** with learning |
| Managing life + work | **PARA** method |
| Want strict organization | **Johnny Decimal** |
| Obsidian power user | **ACE** method |

---

## How to Ask Your AI to Create a Structure

Example prompts:

> "I'm a freelance consultant with 5 active clients. Create a folder structure for my knowledge base."

> "I'm a YouTuber who makes tech tutorials. Set up a folder structure for content creation."

> "I'm new to this. Give me the simplest possible structure to start with."

> "I want to use PARA method. Create the folders and a starter AGENTS.md."

The AI will create the folders and initial files based on your description.

---

## Sources / Inspiration

- **PARA Method** - Tiago Forte (Building a Second Brain)
- **Johnny Decimal** - Johnny Noble (johnny.decimal)
- **ACE Method** - Nick Milo (Linking Your Thinking)
- **Minimal Approach** - Steph Ango (Obsidian CEO)
- **Zettelkasten** - Niklas Luhmann (via Sönke Ahrens)

---

**Remember:** The best structure is the one you'll actually use. Start simple, iterate based on friction.
