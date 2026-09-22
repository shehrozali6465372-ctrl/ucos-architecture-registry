# UCOS Architecture Registry

Central, evidence-driven architecture and verification registry for the Universal Content Operating System (UCOS).

## Source of truth
The implementation source of truth is:
`shehrozali6465372-ctrl/universal-content-operating-system`

This repository is the control-plane record. It does not replace production code.

## Master architecture
- `architecture/UCOS_MASTER_ARCHITECTURE.md` — complete system architecture and 23-layer responsibility map.
- `layers/layer-01` … `layers/layer-23` — bounded layer records.
- `generated/layers/` — source-derived module/class/function inventory produced by automation.
- `dependency-map/` — dependency boundaries.
- `data-flow/` — source-to-revenue lineage.
- `contracts/` — interface and safety contracts.
- `integrations/` — real vs integration-ready provider boundaries.
- `status/` — evidence-backed operational state.
- `changes/` and `incidents/` — architecture evolution and recovery records.

## Status discipline
No invented capability, metric, provider, credential, traffic, conversion or revenue is allowed. `UNKNOWN` is preferred to inference. `LIVE` requires real runtime evidence. Source-code presence alone is never production certification.

## Synchronization
GitHub Actions can scan the exact UCOS implementation branch hourly, on repository-dispatch events, or manually. The scanner records the implementation SHA and generates layer-level Python module/class/function inventories. Validation requires all 23 layer boundaries to exist and the scanner to discover all 23 layer roots.

## Certified implementation baseline
`0f0c92bdf2bc815df3ec1f9bdf033d0613e44a20`

Latest certified CI baseline: run #501 — 10,162 passed, 87 warnings, 0 failures, 0 errors; 23/23 boot.

These figures certify the tested implementation commit only. They do not claim live external-provider or production deployment verification.
