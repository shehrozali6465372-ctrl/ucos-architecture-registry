# UCOS Architecture v1.2 — Implementation Conformance Audit

**Scope:** `shehrozali6465372-ctrl/universal-content-operating-system` current default branch  
**Architecture target:** `UCOS_ARCHITECTURE_FREEZE_CANDIDATE_v1.2.md`  
**Audit posture:** adversarial / evidence-first  
**Decision:** NOT CONFORMANT — DO NOT FREEZE

## Evidence inspected

- L14 `pipeline_wiring.py`
- L07 `content_repetition_guard.py`
- L07 `publish_request.py`
- L07 `publish_executor.py`
- L07 `publisher_manager.py`
- L07 `meta_credentials.py`
- L13 PostgreSQL `schema.py`
- L14 `real_integrations/__init__.py`
- L11/L15 layer inventory evidence from repository architecture records

## Confirmed deviations

### P0-01 — publish_mode is caller-controlled

**Evidence:** L14 `PipelineWiring._preflight()` reads `req.metadata["publish_mode"]` and accepts `staging` or `production`. `execute()` also defaults the request metadata from APP_ENV.

**Contract violation:** v1.2 requires server-side effective-mode resolution from deployment environment + immutable account environment. A production account cannot be switched into a caller-selected staging path.

**Required correction:** introduce a server-side ModePolicy/PublishContext resolver; persist `requested_mode` separately from immutable `effective_mode`; reject unsafe account/environment combinations before mutation.

### P0-02 — repetition ledger is SQLite and check/reserve is not the canonical PostgreSQL ledger

**Evidence:** L07 `ContentRepetitionGuard` creates SQLite `content_history`; PublisherManager creates per-account `publishing_history.sqlite3`.

**Contract violation:** v1.2 requires PostgreSQL canonical publication/repetition state and atomic check-and-reserve under L07 ownership.

**Required correction:** PostgreSQL publication ledger + unique constraints/transactional locking; migrate legacy SQLite histories with provenance.

### P0-03 — unresolved intent is not represented by the frozen state machine

**Evidence:** current guard has only `reserved/pending/published`; stale `reserved` rows are deleted after 1800 seconds. No canonical OUTCOME_UNKNOWN/RECONCILING/verification states exist.

**Contract violation:** ambiguous external effects can be erased instead of retained.

**Required correction:** canonical PublicationIntent/Attempt/ProviderEffect/Verification tables and durable state transitions; no destructive TTL cleanup for post-call ambiguity.

### P0-04 — PostgreSQL schema lacks canonical publication workflow entities

**Evidence:** L13 schema currently contains legacy tables such as `published_posts`, `scheduled_jobs`, `analytics_cache`, `learning_history`, but no frozen identity, workflow, publish intent/attempt/effect/verification, inbox/outbox or reconciliation entities.

**Required correction:** versioned PostgreSQL migration implementing the v1.2 contract before publication migration.

### P0-05 — tracking ID and final post ID are conflated

**Evidence:** L07 repetition guard stores `tracking_id` in `post_id`; `pending()` returns it as `tracking_id`; finalization overwrites the same field.

**Contract violation:** TikTok/provider processing identifiers are not equivalent to externally visible post IDs.

**Required correction:** separate `provider_tracking_id`, `external_post_id`, `external_url`, and provider-effect records.

### P0-06 — publication finalization occurs on provider success, before canonical verification

**Evidence:** L07 PublisherManager calls `guard.finalize(...)` immediately when `pub_result.success` is true.

**Contract violation:** v1.2 requires accepted/submitted processing to remain non-final until verification evidence satisfies platform visibility semantics.

**Required correction:** finalize only through canonical verification transition to VERIFIED_PUBLIC; accepted-processing stays SUBMITTED.

### P0-07 — request identity is process-local

**Evidence:** `PublishRequest` uses `itertools.count(1)` to create `req_1`, `req_2`, etc.

**Contract violation:** durable idempotency and recovery require durable operation/workflow identifiers.

**Required correction:** UUID/ULID-backed workflow_id/publish_operation_id persisted in PostgreSQL; provider idempotency keys must include the logical operation identity.

### P0-08 — L14 still directly owns/constructs external integration implementation

**Evidence:** `pipeline_wiring.py` imports `real_integrations.IntegrationGateway` for external research and `LineageStore`; architecture requires L11 provider adapters and explicit contracts with L14 orchestration only.

**Required correction:** split provider transport/adapters into L11 and retain business semantics in their owning layers; L14 consumes ports.

### P1-01 — credential resolver remains in L07

**Evidence:** `pipeline_wiring.py` imports L07 `MetaCredentialProvider`; that provider directly depends on L07 AccountRegistry.

**Contract violation:** v1.2 migration obligation moves credential resolution to the canonical credential boundary rather than leaving it as a publication-layer side door.

**Required correction:** L11/L17 contract boundary for credential retrieval/authorization, with L07 consuming an interface.

### P1-02 — current pipeline does not implement the frozen verification/reconciliation path

**Evidence:** current execution graph is P0-Preflight → L2 → L3 → L4 → L12 → L5 → L6 → L7, followed by optional analytics/learning. No explicit durable INTENT_CREATED/CALLING/SUBMITTED/VERIFYING/RECONCILING stages are present.

**Required correction:** route publication through the canonical L07 PublicationGateway and L15 durable execution/reconciliation contracts.

### P1-03 — L15 durable implementation is not yet evidenced

**Evidence:** architecture inventory identifies L15 runtime mechanics; no PostgreSQL task store/DLQ/reconciliation persistence was established in this audit.

**Required correction:** implementation proof for task state, leases, retry state, cancellation, reconciliation tasks and DLQ/operator state before L15 certification.

### P1-04 — L23 bypass risk remains

**Evidence:** prior audited implementation allows local article publication semantics independent of the global PublicationGateway.

**Required correction:** production L23 network publication must use the shared L07 gateway and canonical verification state.

### P1-05 — learning/lineage semantic contamination remains a review item

**Evidence:** L14 lineage records generated `content` and `asset` stages with status `observed` in the current implementation.

**Contract violation:** generated artifacts are not observed external outcomes.

**Required correction:** reserve `observed` for externally evidenced observations; use generated/projected statuses for generated artifacts.

## Conformance matrix

| Contract | Status |
|---|---|
| Server-authoritative publish_mode | FAIL / P0 |
| Atomic PostgreSQL repetition reservation | FAIL / P0 |
| Unresolved intent retention | FAIL / P0 |
| Canonical PG publication schema | FAIL / P0 |
| Tracking ID vs post ID separation | FAIL / P0 |
| Verify-before-finalize | FAIL / P0 |
| Durable request identity | FAIL / P0 |
| L11/L14 ownership boundary | FAIL / P0 |
| Credential resolver ownership | FAIL / P1 |
| Durable verification/reconciliation execution | FAIL / P1 |
| L15 PostgreSQL durability evidence | UNKNOWN/FAIL until proven |
| L23 gateway enforcement | FAIL / P1 |
| Generated vs observed lineage | FAIL / P1 |

## Freeze decision

**NOT FREEZE-READY.**

The architecture candidate now describes the required target correctly in these areas, but the implementation has not converged on that target. No architecture freeze approval should be recorded until the P0 conformance failures have either been implemented and tested or explicitly resolved by an architecture change.

## Required implementation order

1. Stage 0 P0 safety baseline.
2. PostgreSQL canonical identity/publication schema and repositories.
3. L07 atomic repetition + unresolved-intent ledger.
4. PublishIntent/Attempt/ProviderEffect/Verification state machine.
5. Server-authoritative mode policy.
6. L11 provider/credential boundary extraction.
7. L15 PostgreSQL durable task/reconciliation store.
8. Provider-specific verification/canary contracts.
9. L23 PublicationGateway enforcement.
10. Migration of legacy SQLite/local stores.
11. Contract/fault tests A–H.
12. Full integration and production certification.

**Important:** this audit does not claim that external provider canaries, L15 implementation details, or L23 current files are fully certified; those require direct implementation/runtime evidence in the UCOS repository.
