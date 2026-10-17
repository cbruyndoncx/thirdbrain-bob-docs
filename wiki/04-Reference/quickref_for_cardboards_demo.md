---
title: Quick Ref for Cardboards democreated:26-01-08
status: done
plugin_version: 0.13.0
---
## Quick Ref for Cardboards demo

### Board 1: Sprint Board 
- Configured with 6 columns
  - Backlog (`status/backlog`)
  - To Do (`status/todo`)
  - Doing (`status/doing`)
  - Reviewing (`status/review`)
  - Testing (`status/testing`)
  - Done (Completed type)
---
### Board 2: My Tasks (Personal)

**Board Name:** `My Tasks`

**Columns to add:**
1. Tag: `personal/urgent` → Name: `Urgent`
2. Tag: `personal/week` → Name: `This Week`
3. Tag: `personal/someday` → Name: `Someday`
4. Tag: `home/` → Name: `Home` (trailing slash for subtags)
5. Tag: `work/` → Name: `Work` (trailing slash for subtags)
6. Type: **Completed** → Name: `Completed`

**Configuration:**
- Show column tags: Yes
- Show filtered tags: Yes

---

### Board 3: Content Pipeline

**Board Name:** `Content Pipeline`

**Columns to add:**
1. Tag: `content/ideas` → Name: `Ideas`
2. Tag: `content/research` → Name: `Research`
3. Tag: `content/draft` → Name: `Drafting` → **Limit: 3**
4. Tag: `content/edit` → Name: `Editing` → **Limit: 2**
5. Tag: `content/ready` → Name: `Ready to Publish`
6. Type: **Completed** → Name: `Published`

**Configuration:**
- Show column tags: Yes
- Show filtered tags: Yes

---

### Board 4: Weekly Overview

**Board Name:** `Weekly Overview`

**Columns to add:**
1. Type: **Date** → Range: `Before today` → Name: `Overdue`
2. Type: **Date** → Range: `Between 0 and 0` → Name: `Today`
3. Type: **Date** → Range: `Between 1 and 7` → Name: `This Week`
4. Tag: `priority/high` → Name: `High Priority`
5. Tag: `status/doing` → Name: `In Progress`
6. Type: **Completed** → Name: `Completed`

**Configuration:**
- Show column tags: Yes
- Show filtered tags: Yes

---

## 📝 Configuration Instructions

### How to Add Boards

1. **Open Settings** → Community Plugins → **Card Board**
2. Click the **+** icon to add a new board
3. Enter the board name
4. Click **+** to add each column
5. For **Tag columns**:
   - Select "Named Tag" type
   - Enter tag (without `#`)
   - Enter column name
   - Optional: Set limit
6. For **Date columns**:
   - Select date range type
   - Enter column name
7. For **Completed columns**:
   - Select "Completed" type
   - Enter column name
8. Save the board

### Important Notes

- **Don't include `#`** in tag configuration (use `status/backlog` not `#status/backlog`)
- **Use trailing `/`** for subtag matching (e.g., `home/` matches `home/inside`, `home/outside`)
- **Column limits** prevent work-in-progress overload (recommended: 2-5 tasks)
- **Date ranges** use day offsets from today (0 = today, 1-7 = next week, etc.)

---

## 🎯 Demo Task Files

The following markdown files contain demo tasks ready to be organized:

- ✅ `Tasks/Sprint Board Demo.md` - Software development tasks
- ✅ `Tasks/Personal Tasks Demo.md` - Personal productivity tasks
- ✅ `Tasks/Content Pipeline Demo.md` - Content creation workflow
- ✅ `Tasks/Weekly Overview Demo.md` - Weekly planning tasks

Tasks will automatically appear on boards once tags match column configurations.

---
