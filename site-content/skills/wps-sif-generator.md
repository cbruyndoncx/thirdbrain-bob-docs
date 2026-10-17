---
layout: skill-detail.njk
bodyClasses: skill-detail
seo:
  title: wps-sif-generator — ThirdBrain BOB skill
  description: Generate the UAE Wage Protection System Salary Information File and confirm payroll compliance. The SIF is the pipe-delimited file submitted to the bank every p
  socialImage: /assets/images/thirdbrain-bob-obsidian-ai-logos-desk.jpg
skillName: wps-sif-generator
catLabel: finance
area: finance
desc: Multi-jurisdiction payroll statutory compliance — generates jurisdiction- specific payroll submission files, validates formats, reconciles payroll totals, and creates…
summary: Generate the UAE Wage Protection System Salary Information File and confirm payroll compliance. The SIF is the pipe-delimited file submitted to the bank every payroll cycle; MOL monitors it to confirm salaries are paid on time and in full.
difficulty: beginner
inputType: data
outputType: spreadsheet
requires: '[none]'
roles: '[Finance Manager]'
inputs:
- payroll_month — YYYY-MM, e.g. 2025-12
- employee_list — List of employees with basic salary, allowances, deductions, IBAN
- sif_file — The generated SIF file to validate, in the scratch output location (`output.scratch`)
- wps_record — Wps record used to confirm SIF total matches payroll journal entry and MOL confirmation received
- payroll_je — Journal entry for the payroll period
outputs:
- conversation
- prefer a permanent directory)
- sif-file (txt)
- updated-wps-record (markdown)
- validation-report (markdown)
- wps-record (markdown)
- '{company.hr.wps}/WPS-{YYYY}-{MM}.md'
prompts:
- Generate a payroll submission
- Validate a compliance file
- Confirm payroll compliance status
---
