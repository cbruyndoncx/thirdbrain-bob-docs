---
description: 'Analyze stock levels, calculate reorder points, classify SKUs, map warehouse layouts, and reconcile physical counts. Operates in two modes: standalone (CSV/JSON data dumps) or connected (live ERP via `mcp-server-odoo` or `erpnext-mcp`).'
title: inventory-management
---

# inventory-management

Analyze stock levels, calculate reorder points, classify SKUs, map warehouse layouts, and reconcile physical counts. Operates in two modes: standalone (CSV/JSON data dumps) or connected (live ERP via `mcp-server-odoo` or `erpnext-mcp`).

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Analyze stock levels, calculate reorder points, classify SKUs, map warehouse layouts, and reconcile physical counts against system stock.

## How you ask

- “Run an inventory health check for Acme Corp using their latest stock export”
- “Calculate reorder points and safety stock for all SKUs at 95% service level”
- “Classify our client's SKUs using ABC/XYZ analysis on their annual sales data”
- “Map the warehouse layout for Bobbolt's main distribution center”
- “We just finished a physical count — reconcile it against the system stock”

## Inputs

- stock_data — Stock snapshot data (CSV/JSON dump or MCP query result). Include standard_price (unit cost) for value calculations; SKUs without it are excluded from value totals and flagged 'value unknown'. expiration_date is optional for expiry-based flags.
- demand_history — Demand history for turnover/days-of-stock calculation. Schema: product_id, default_code, period_start, period_end, qty_consumed. If absent, turnover ratio and days-of-stock are reported as 'N/A — demand data required'.
- client_id — Client identifier for output routing
- demand_history — Historical demand data (min 3 months recommended)
- lead_times — Supplier lead times per SKU (defaults to 7 days if absent)
- service_level — Target service level 0-1 (default 0.95)
- sku_data — SKU-level sales/consumption data with value and volume
- location_data — Warehouse locations with zone, aisle, rack, bin identifiers
- stock_data — Current stock by location (for heatmap overlay)
- physical_count — Physical count results (SKU, location, counted qty)
- system_stock — System stock snapshot at time of count

## Outputs

- Prioritized SKU matrix with class assignments and action flags
- Reorder point and safety stock recommendations per SKU
- Stock health report with KPIs, flags, and recommendations
- Variance report with discrepancy flags and root-cause suggestions
- Visual warehouse layout with zones and stock distribution
- {client.deliverables.inventory}/abc_xyz_classification.md
- {client.deliverables.inventory}/inventory_health_report.md
- {client.deliverables.inventory}/reorder_recommendations.md
- {client.deliverables.inventory}/stock_variance_report.md
- {client.deliverables.inventory}/warehouse_layout.excalidraw

