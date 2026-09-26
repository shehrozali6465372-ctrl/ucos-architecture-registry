# UCOS Master Architecture

**Implementation source of truth:** `shehrozali6465372-ctrl/universal-content-operating-system`
**Current implementation baseline:** `733457c310d65ffbf3ccc4169662d485373beb6d` (UCOS `main`)

**Registry sync source:** UCOS `main`; open feature branches/PRs are not treated as architecture baseline until merged.
**Registry purpose:** evidence-driven architecture, dependency, data-flow, contract, integration and operational record.

## Rules
- The implementation repository is authoritative for executable behavior.
- This registry never invents capabilities, metrics, providers, credentials or completion status.
- UNKNOWN is preferred to inference.
- LIVE requires real runtime/provider evidence; integration-ready is not live.
- A layer owns its responsibility and exposes explicit contracts; cross-layer coupling must be justified and tested.
- Changes must identify affected boundaries and verification evidence.

## System shape
UCOS is a 23-layer content operating system with shared models, dependency injection, an event bus, persistence, AI/provider routing, research/intelligence, content production, publishing, analytics, learning, integrations and website management. The target business lineage is:

`source → niche → keyword → content → asset → platform → account → publish → click → conversion → revenue`

## 23-layer responsibility map
| Layer | Responsibility | Current registry status |
|---|---|---|
| L01 | Core: configuration, state, memory, scheduling, logging, backup and foundational services | VERIFIED from implementation/audit; detailed runtime inventory is maintained below |
| L02 | Research: audience/source research and provenance-aware research inputs | VERIFIED from implementation/audit |
| L03 | Intelligence: niche, keyword, intent, entities, audience fit, novelty and evidence bundles | VERIFIED from implementation/audit |
| L04 | Writing: writing plans, drafts, variants, CTA and writing intelligence | VERIFIED from implementation/audit |
| L05 | Image: image generation/orchestration and asset provenance | VERIFIED boundary; real provider required for production |
| L06 | Quality: content quality, safety, compliance, factuality, originality and publication gates | VERIFIED hard-gate architecture |
| L07 | Publishing: platform adapters, mutation results, publication and reconciliation boundaries | VERIFIED; live external mutation still requires provider/account evidence |
| L08 | Analytics: platform metric ingestion/normalization and attribution inputs | VERIFIED architecture; live data requires configured providers |
| L09 | Learning: observed-outcome learning, mistake detection and improvement actions | VERIFIED evidence-gated learning |
| L10 | Affiliate: commerce decisioning, product/program eligibility and attribution | VERIFIED boundary; real catalog/program required |
| L11 | Integrations: provider lifecycle and external service integration boundary | VERIFIED architecture |
| L12 | AI Foundation: model routing, provider metadata, usage/failure handling | VERIFIED architecture; real provider required for live use |
| L13 | Persistence: PostgreSQL production source of truth and persistence abstractions | VERIFIED; CI PostgreSQL path is certified |
| L14 | Enterprise Integration: durable request/idempotency/correlation and external enterprise boundaries | VERIFIED architecture; durable live evidence remains operational work |
| L15 | Async Runtime: bounded tasks, retries, cancellation and dead-letter behavior | VERIFIED architecture |
| L16 | Database: SQL/transaction/query/pool/migration safeguards | VERIFIED architecture |
| L17 | Security: threat boundaries, credentials, injection/SSRF/path/replay/tool safety | VERIFIED architecture/tests |
| L18 | Monitoring: health, dependency state, telemetry and recovery visibility | VERIFIED architecture |
| L19 | Analytics Engine: forecasting, recommendations and observed/projected separation | VERIFIED evidence-gated forecasting |
| L20 | Image Pipeline: provider capability, validation, provenance and multimodal asset flow | VERIFIED fail-closed provider boundary |
| L21 | Deployment: container/runtime/readiness/build/recovery concerns | VERIFIED CI/deployment boundary; production operations remain deployment work |
| L22 | Documentation: supported interfaces, ADRs and operational/runbook knowledge | VERIFIED documentation layer |
| L23 | Website Manager: websites, traffic, Pinterest/AtoZ/affiliate-facing website operations | VERIFIED architecture; live site credentials/runtime required |

## Cross-cutting architecture
### Identity and isolation
Persistent business records must be scoped by account, platform/external account and niche where applicable. Credentials are not architecture data and must never be copied into this registry.

### Execution gates
External mutation must pass applicable quality, safety, compliance, factuality, originality, platform-policy and identity gates. Uncertain external mutations require reconciliation rather than blind retry.

### Learning gate
Only observed outcomes may update production learning state. Unknown/unobserved outcomes do not become synthetic intelligence.

### Integration gateway
Real integrations are adapter-based. Missing credentials/provider configuration produces explicit failure rather than fabricated success.

### Resilience
Critical paths require bounded retries, timeouts, idempotency, transactional persistence, recovery/reconciliation and clear failure states.

## Evidence baseline
- Latest Layer 1 certified CI run: **#640**, run ID **35942475355**, conclusion **success** (post-merge `main` verification; PR certification was #639 / 35941752342).
- Latest Layer 1 result: **10,209 passed, 87 warnings, 0 failures/errors**.
- Layer 1 static inventory: **51 modules, 167 classes, 795 functions/methods, 0 syntax errors**.
- Boot certification: **23/23 layers loaded, 0 errors**.
- Layer 1 production-hardening PR **#16** was merged into `main` at **528539b19848c275e363407199998bb9e3fd9d10**.
- These CI facts certify the tested commit and local CI PostgreSQL/runtime paths; they do not constitute live external-provider certification.

## Detailed layer inventory policy
Each `layers/layer-XX/README.md` records verified implementation paths, functions/modules, contracts, dependencies, data flow, tests, failure boundaries, live/integration-ready status and remaining evidence. The registry must be updated from implementation evidence rather than assumptions.

## Architecture evolution
This document is the durable master architecture record. When implementation changes, update the affected layer record, dependency/data-flow impact, contracts and verification evidence. Preserve historical decisions rather than silently rewriting why a boundary exists.


## Layer 17 certification record
Layer 17 Security was production-certified on UCOS merge commit `733457c310d65ffbf3ccc4169662d485373beb6d` through dedicated workflow run #13. The dedicated gate passed compilation, strict lint, secret scanning, security invariants, legacy security regression tests, module regression checks, and evidence upload. Repository-wide CI remained blocked by an unrelated pytest collection collision between Layer 19 and Layer 20 production-certification test modules sharing the same basename.