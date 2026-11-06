---
title: Tasks Plugin vs TaskNotes Plugin
type: knowledge-base
status: final
created: 2026-03-01
modified: 2026-03-01
tags:
  - obsidian
  - task-management
  - plugins
---

# Tasks Plugin vs TaskNotes Plugin

## Quick Decision Matrix

| Use Case | Recommended Plugin |
|----------|-------------------|
| Quick to-dos within notes | **Tasks** |
| Meeting action items | **Tasks** |
| Shopping lists, checklists | **Tasks** |
| Project deliverables with context | **TaskNotes** |
| Strategic initiatives | **TaskNotes** |
| Tasks needing documentation | **TaskNotes** |
| Client work items | **TaskNotes** |
| Personal reminders | **Tasks** |

---

## Philosophy Comparison

### Tasks Plugin: Checkbox-Enhanced

**Core idea**: Extend Obsidian's native checkboxes with querying, dates, and recurrence.

- Tasks live **inside** your notes (meeting notes, daily notes, project docs)
- Each task is a single line: `- [ ] Do something 📅 2026-03-15`
- Query tasks across your vault with code blocks
- Changes sync back to the source file

**Mental model**: "Scattered tasks, unified view"

### TaskNotes Plugin: One Note Per Task

**Core idea**: Each task is a full Markdown note with frontmatter metadata.

- Tasks **are** notes (stored in `{output.tasks}`)
- Each task has unlimited space for context, subtasks, notes
- View tasks in Kanban, Calendar, Timeline, Agenda views
- Powered by Obsidian Bases for querying

**Mental model**: "Tasks as first-class knowledge objects"

---

## Your JTBD Intuition is Correct

You're right that **TaskNotes aligns with Jobs To Be Done** thinking:

| Aspect | Tasks Plugin | TaskNotes Plugin |
|--------|--------------|------------------|
| **Focus** | Actions to complete | Outcomes to achieve |
| **Granularity** | Single-line items | Full documentation |
| **Context** | Minimal (tags, dates) | Rich (body, links, subtasks) |
| **Stability** | Tasks come and go | Tasks evolve over time |
| **Relationships** | Isolated checkboxes | Graph-connected notes |

### JTBD Alignment

**Jobs To Be Done** asks: *"What job is the customer hiring this product to do?"*

- **Tasks plugin job**: "Help me not forget small things"
- **TaskNotes plugin job**: "Help me manage meaningful work with full context"

A TaskNote like "Create Landing Page One-Pager" isn't just a checkbox—it's a **knowledge container** with context, deliverables, format options, and subtasks. It documents *why* and *how*, not just *what*.

---

## When to Use Each

### Use Tasks Plugin For:

1. **Transactional items** — Buy milk, call dentist, send email
2. **Meeting action items** — Quick captures during meetings
3. **Daily note todos** — Today's small tasks
4. **Recurring maintenance** — Weekly review, daily standup
5. **Delegated items** — Waiting-for lists
6. **Checklists** — Packing lists, process steps

**Characteristics:**
- Completes in one sitting
- Needs no documentation
- Context is in the surrounding note
- High volume, low complexity

### Use TaskNotes For:

1. **Project deliverables** — Landing pages, documents, features
2. **Strategic initiatives** — Quarterly goals, OKRs
3. **Client work items** — Anything billable or traceable
4. **Research tasks** — Topics requiring investigation
5. **Creative work** — Writing, design, content creation
6. **Complex problems** — Multi-step, multi-day efforts

**Characteristics:**
- Takes multiple sessions
- Benefits from notes/context
- May have subtasks
- Connects to projects/clients
- Worth tracking progress

---

## Practical Integration

### Capture Flow

```
Quick thought → Tasks checkbox (in daily note)
     ↓
If complex → Convert to TaskNote
     ↓
TaskNote → Full documentation space
```

### Example Workflow

**Morning standup** (Tasks plugin):
```markdown
## Today
- [ ] Review PR #142
- [ ] Respond to client email
- [ ] Prep for 2pm call
```

**Project work** (TaskNotes):
```
{output.tasks}
├── Create Landing Page One-Pager for vault product.md
├── Set up Fireflies to Google Drive integration.md
└── Add Anthropic Best Practices to Skillsmith.md
```

### Hybrid Approach

1. **Capture** quick items with Tasks syntax in daily/meeting notes
2. **Promote** complex items to TaskNotes when they need:
   - Multiple subtasks
   - Context documentation
   - Project linking
   - Extended timeline
3. **Query** both systems as needed

---

## Technical Differences

| Feature | Tasks | TaskNotes |
|---------|-------|-----------|
| **Storage** | Inline in any note | Dedicated note per task |
| **Metadata** | Emoji syntax inline | YAML frontmatter |
| **Querying** | Code blocks (`tasks`) | Bases views |
| **Views** | List only | Kanban, Calendar, Timeline, Agenda |
| **Dependencies** | None | Bases core plugin |
| **Mobile** | Via sync plugins | Native Obsidian |
| **Graph integration** | No | Yes |

---

## Recommended Configuration

### Tasks Plugin Settings

- Replace "Toggle checkbox status" hotkey with "Tasks: Toggle Done"
- Enable "Set done date on every completed task"
- Use in: Daily notes, meeting notes, quick captures

### TaskNotes Settings

- Store tasks in: `{output.tasks}`
- Use default statuses: `open`, `in-progress`, `done`, `cancelled`
- Link to projects via frontmatter
- Use in: Project work, client deliverables, strategic items

---

## Summary

| | Tasks | TaskNotes |
|-|-------|-----------|
| **Metaphor** | Sticky notes | Project briefs |
| **Volume** | Many small items | Fewer significant items |
| **Lifespan** | Hours to days | Days to weeks |
| **Documentation** | None needed | Essential |
| **JTBD alignment** | Low (action-focused) | High (outcome-focused) |

**Rule of thumb**: If you'd forget what the task means in a week, use Tasks. If you need to remember *why* and *how*, use TaskNotes.
