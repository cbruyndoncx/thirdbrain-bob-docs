---
description: Shared infrastructure skill for the Operations/ERP skill family. Contains the canonical data model, CSV schemas, and integration patterns that `inventory-management`, `order-management`, `production-planning`, and `logistics-shipping` all depend on.
title: erp-reference
---

# erp-reference

Shared infrastructure skill for the Operations/ERP skill family. Contains the canonical data model, CSV schemas, and integration patterns that `inventory-management`, `order-management`, `production-planning`, and `logistics-shipping` all depend on.

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Provides ERP schema details, field mappings, CSV dump formats, and MCP server setup guidance for Odoo and ERPNext.

## How you ask

- “What CSV columns do I need for an inventory snapshot export?”
- “Map the Odoo stock models to ERPNext equivalents”
- “Help me set up mcp-server-odoo for a client on Odoo 17”
- “What's the difference between stock.picking in Odoo and Delivery Note in ERPNext?”

## Inputs

- domain — Domain whose CSV dump schema is wanted (inventory, orders, production, logistics, or another domain with a schema in references/erp-integration.md)
- system — ERP system whose model names to include; omit for the system-neutral CSV spec (odoo | erpnext)
- domain — Domain (inventory, orders, production, logistics) or a specific model name to map between Odoo and ERPNext
- system — ERP system whose MCP server to configure; it also names the output file (odoo | erpnext)
- instance_url — URL of the client's ERP instance, carried into the configuration text

## Outputs

- csv-schema (markdown)
- model-map (markdown)
- prefer a permanent directory)
- setup-guide (markdown)

