---
description: Analyze shipment data across carriers, routes, and packaging to surface delivery performance issues, cost optimization opportunities, and fulfilment bottlenecks. Works from CSV/JSON data dumps (standalone) or live ERP queries (connected mode via MCP).
title: logistics-shipping
---

# logistics-shipping

Analyze shipment data across carriers, routes, and packaging to surface delivery performance issues, cost optimization opportunities, and fulfilment bottlenecks. Works from CSV/JSON data dumps (standalone) or live ERP queries (connected mode via MCP).

| | |
|---|---|
| **Area** | Operations |
| **Category** | operations |
| **Level** | beginner |
| **Input** | conversation |
| **Output** | document |
| **Setup** | [none] |
| **Roles** | [Operations Manager] |

Analyze shipment performance, carrier comparison, delivery tracking, package optimization, and fulfilment route efficiency.

## How you ask

- “Give me a shipment status overview for Acme Corp's last 30 days”
- “Compare carrier performance across all our outbound shipments this quarter”
- “Analyze shipping costs by carrier and destination zone for client bobbolt”
- “Which fulfilment routes have the longest transit times and highest failure rates?”
- “Audit our packaging fill rates and flag over-packaged shipments”

## Inputs

- shipment_ids — Shipments to report on; defaults to everything in flight
- client_id — Restrict the snapshot to one client
- profile — Company profile — jurisdiction and operating regions for shipping rules.
- carriers — Carriers to compare or select between
- lane — Origin → destination lane the comparison applies to
- shipment_data — Shipment records with weights, lanes, and charges
- currency — Reporting currency; convert before aggregating if the data is mixed
- origin — Pickup location
- destination — Delivery location
- constraints — Transit-time, cost, or customs constraints to respect
- product_spec — Dimensions, weight, and fragility of what is being shipped
- mode — Transport mode the packaging is being right-sized for — air, sea, road, or courier. Sets the default dimensional-weight divisor (references/workflow-steps.md, Route: packaging); pallet and stacking rules belong to packaging-logistics. (air | sea | road | courier)

## Outputs

- carrier-scorecard (markdown)
- cost-report (markdown)
- packaging-report (markdown)
- route-report (markdown)
- status-report (markdown)
- {client.deliverables.logistics}/carrier_report_{YYYY-MM-DD}.md
- {client.deliverables.logistics}/cost_report_{YYYY-MM-DD}.md
- {client.deliverables.logistics}/packaging_report_{YYYY-MM-DD}.md
- {client.deliverables.logistics}/route_report_{YYYY-MM-DD}.md
- {client.deliverables.logistics}/status_report_{YYYY-MM-DD}.md

