# UCOS Architecture Registry

Central, evidence-driven architecture and verification registry for the Universal Content Operating System (UCOS).

## Canonical architecture — UCOS v1.2

**Only these two documents are authoritative architecture specifications:**

1. architecture/UCOS_ARCHITECTURE_FROZEN_PRODUCTION_BASELINE_v1.2.md — frozen system architecture and 23-layer ownership/contracts.
2. architecture/UCOS_ARCHITECTURE_FREEZE_REVIEW_v1.2_FINAL.md — final review decision, binding invariants and freeze acceptance.

Do not create or maintain competing architecture blueprints in this registry. Post-freeze architecture changes require the Architecture Change Request (ACR) process defined by the canonical baseline.

## Repository purpose

The implementation source of truth remains:
shehrozali6465372-ctrl/universal-content-operating-system

This repository is the architecture registry and evidence index; it does not replace production code or certify deployment by itself.

- layers/layer-01 … layers/layer-23 — bounded layer records.
- generated/layers/ — source-derived module/class/function inventory produced by automation; generated inventory is not a competing architecture.
- dependency-map/ — dependency boundaries.
- data-flow/ — source-to-revenue lineage.
- contracts/ — interface and safety contracts.
- integrations/ — provider boundaries.
- status/ — evidence-backed operational state.
- changes/ and incidents/ — architecture change and recovery records.

## Status discipline

No invented capability, metric, provider, credential, traffic, conversion or revenue is allowed. UNKNOWN is preferred to inference. LIVE requires real runtime evidence. Source-code presence alone is never production certification.

## Synchronization

GitHub Actions scans the UCOS implementation repository and records its implementation SHA while generating layer-level Python module/class/function inventories. Validation requires all 23 layer boundaries and all 23 discovered layer roots. Generated inventories describe source structure only; they do not prove live integrations or production readiness.

## Historical CI evidence

Previously recorded baseline: 0f0c92bdf2bc815df3ec1f9bdf033d0613e44a20 (run #501, 10,162 passed, 87 warnings, 0 failures, 0 errors; 23/23 boot).

This is historical evidence for that tested commit, not a claim about the current deployed commit or live provider status. Verify current runs before making a current certification claim.
