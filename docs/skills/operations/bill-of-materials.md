---
description: Build structured bills of materials, calculate material requirements for production runs, and compare requirements against inventory to surface sourcing gaps. Designed for operations and production teams who manage materials in spreadsheets or simple systems — no ERP required.
title: bill-of-materials
---

# bill-of-materials

Build structured bills of materials, calculate material requirements for production runs, and compare requirements against inventory to surface sourcing gaps. Designed for operations and production teams who manage materials in spreadsheets or simple systems — no ERP required.

- **Area:** Operations
- **Category:** operations
- **Level:** beginner
- **Input:** conversation
- **Output:** document
- **Setup:** none
- **Roles:** Operations Manager

Manages bills of materials, calculates material requirements, and identifies sourcing gaps for production planning.

## How you ask

- “Bill of materials”
- “Material needs”
- “Production run”

## Inputs

- product_name — Product name or SKU
- components — List of components with quantity, unit, and unit cost
- batch_size — Standard batch size (default: 1 unit)
- bom_file — Path to existing BOM file or inline BOM data
- batch_size — Number of units to produce
- scrap_factor — Scrap allowance percentage (e.g., 5 for 5%); default: 0
- requirements_file — Path to requirements file or inline requirements data
- inventory_data — Current stock on hand per component (CSV path, table, or inline data)

## Outputs

- Gap analysis table with shortfall quantities and sourcing flags
- Material requirements table with gross quantities including scrap allowance
- Structured BOM with component table and cost rollup
- {client.deliverables.operations}/availability_check_{product_sku}_{batch_size}units.md
- {client.deliverables.operations}/bom_{product_sku}.md
- {client.deliverables.operations}/material_requirements_{product_sku}_{batch_size}units.md

