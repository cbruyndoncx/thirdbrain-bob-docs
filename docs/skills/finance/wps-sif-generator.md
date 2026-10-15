---
description: Generate the UAE Wage Protection System Salary Information File and confirm payroll compliance. The SIF is the pipe-delimited file submitted to the bank every payroll cycle; MOL monitors it to confirm salaries are paid on time and in full.
title: wps-sif-generator
---

# wps-sif-generator

Generate the UAE Wage Protection System Salary Information File and confirm payroll compliance. The SIF is the pipe-delimited file submitted to the bank every payroll cycle; MOL monitors it to confirm salaries are paid on time and in full.

- **Area:** Finance
- **Category:** finance
- **Level:** beginner
- **Input:** data
- **Output:** spreadsheet
- **Setup:** none
- **Roles:** Finance Manager

Multi-jurisdiction payroll statutory compliance — generates jurisdiction- specific payroll submission files, validates formats, reconciles payroll totals, and creates…

## How you ask

- “Generate a payroll submission”
- “Validate a compliance file”
- “Confirm payroll compliance status”

## Inputs

- payroll_month — YYYY-MM, e.g. 2025-12
- employee_list — List of employees with basic salary, allowances, deductions, IBAN
- sif_file — The generated SIF file to validate, in the scratch output location (`output.scratch`)
- wps_record — Wps record used to confirm SIF total matches payroll journal entry and MOL confirmation received
- payroll_je — Journal entry for the payroll period

## Outputs

- conversation
- prefer a permanent directory)
- sif-file (txt)
- updated-wps-record (markdown)
- validation-report (markdown)
- wps-record (markdown)
- {company.hr.wps}/WPS-{YYYY}-{MM}.md

