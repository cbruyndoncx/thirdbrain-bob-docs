---
description: Handle spreadsheets. Use when the user says 'Excel file', '.xlsx', 'CSV', 'spreadsheet cleanup', 'tabular data analysis', or 'spreadsheet methodology'. Handles .xlsx and CSV files, cleaning messy data, adding formulas, charts, and formatting.
title: xlsx-tools
---

# xlsx-tools

Handle spreadsheets. Use when the user says 'Excel file', '.xlsx', 'CSV', 'spreadsheet cleanup', 'tabular data analysis', or 'spreadsheet methodology'. Handles .xlsx and CSV files, cleaning messy data, adding formulas, charts, and formatting.

| | |
|---|---|
| **Area** | Foundational |
| **Category** | documents |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Finance Manager] |

Handle spreadsheets.

## How you ask

- “Create a spreadsheet with formulas for budget tracking”
- “Clean up this messy CSV data and add proper formatting”
- “Add charts to this Excel file based on the revenue data”
- “Convert this data into a formatted .xlsx with pivot tables”

## Inputs

- request — What to produce

## Outputs

- Optional visual-check render of the workbook via soffice (Rendering and Visual Checks); only when LibreOffice is available.
- The created or edited workbook (or CSV). An edit of an existing file is saved at the path the user names; a new workbook without a named path lands here.
- prefer a permanent directory)

