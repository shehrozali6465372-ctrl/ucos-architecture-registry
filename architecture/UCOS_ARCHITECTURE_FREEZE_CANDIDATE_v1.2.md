# UCOS Architecture Freeze Candidate v1.2

**Status:** FREEZE CANDIDATE — NOT YET FREEZE-READY  
**Supersedes for review:** `UCOS_WORKING_ARCHITECTURE_BLUEPRINT_v1.0.md`  
**Implementation repository:** `shehrozali6465372-ctrl/universal-content-operating-system`  
**Architecture registry:** `shehrozali6465372-ctrl/ucos-architecture-registry`  
**Review branch:** `working-blueprint-v1`

> This document is the v1.2 adversarial revision of v1.1. v1.1 remains immutable historical evidence; v1.2 supersedes it for freeze review. After explicit approval, this exact version becomes the Frozen Production Architecture Baseline and later architectural changes require an Architecture Change Request (ACR).

---

## 1. System mission

UCOS is a production digital-marketing operating system that converts evidence into account-isolated, policy-aware, measurable content workflows and controlled external actions.

Canonical business lineage:

`source → niche → keyword → content → asset → platform → account → publish → click → conversion → revenue`

The architecture preserves provenance, identity, authorization, policy, state, attribution, external-effect evidence and auditability across the lineage.

### Non-goals

- UCOS is not 23 independently deployed microservices.
- UCOS does not fabricate provider success, analytics, conversions or revenue.
- UCOS does not share credentials, memory, learning state, analytics state or publication history across accounts without explicit authorization.
- UCOS does not blindly repeat an externally ambiguous mutation.
- UCOS does not treat staging activity as production evidence.
- UCOS does not equate a provider tracking identifier with a public post identifier.
- UCOS does not equate a local database row with proof of network publication.

---

## 2. Architecture principles

1. **Evidence before claims.** External effects are claimed only from provider evidence.
2. **One logical owner per concern.** Deployment consolidation must not create overlapping business ownership.
3. **Contract before implementation.** Layers interact through versioned contracts, ports or explicit adapters.
4. **Durability before retry.** A retry is allowed only when the prior step's state can be reconstructed safely.
5. **Ambiguity is a state.** Unknown external outcomes are retained and reconciled; they are never silently converted into failure.
6. **Identity is mandatory.** Every externally mutable business operation is scoped to tenant/workspace/brand/account/platform identity.
7. **Production truth is PostgreSQL.** SQLite and local files are development/test compatibility only unless explicitly classified as non-business temporary state.
8. **Provider semantics remain outside orchestration.** L14 coordinates; L07/L11 adapters perform provider-specific behavior.
9. **Observed and derived data remain separate.**
10. **No safety control is bypassed by a score or convenience path.**

---

## 3. Logical layers and runtime domains

UCOS retains 23 logical bounded layers for ownership, auditability and contract isolation.

Production deployment consolidates those logical layers into capability domains. A capability domain is an operational boundary, not a business ownership boundary.

| Runtime domain | Logical layers | Purpose |
|---|---|---|
| Foundation & Security | L01, L13, L16, L17 | identity-independent foundations, persistence, database mechanics, security |
| Research & Intelligence | L02, L03 | external evidence and intelligence transformation |
| Content & Creative | L04, L05, L12, L20 | planning, writing, AI routing, assets/media |
| Quality & Monetization | L06, L10 | publication quality and commercial/affiliate evidence |
| Publishing & Integrations | L07, L11 | publication semantics and external provider lifecycle |
| Control & Durable Execution | L14, L15 | workflow meaning and restart-safe execution |
| Analytics & Operations | L08, L09, L18, L19, L21, L22, L23 | observations, learning, projections, operations, deployment, documentation and web lifecycle |

A production deployment MAY split a domain into multiple processes later; such a split is a deployment decision, not a layer ownership change.

---

## 4. Canonical 23-layer ownership

| Layer | Canonical name | Frozen responsibility | Canonical output |
|---|---|---|---|
| L01 | Core | runtime configuration, foundational state, lifecycle, basic memory/file abstractions, scheduler entry points, logging/backup coordination | RuntimeContext |
| L02 | Research | source discovery, audience/source research, provenance capture | ResearchResult |
| L03 | Intelligence | niche, keyword, intent, entity, evidence and novelty transformation | IntelligenceBundle |
| L04 | Writing | deterministic content planning, drafting, variants, CTA and writing policy | WritingResult / PlannerResult |
| L05 | Image / Creative Generation | image/creative intent, prompt construction, generation requests and creative metadata | ImageGenerationResult |
| L06 | Quality | factuality, safety, compliance, originality, brand and publication gates | QualityResult |
| L07 | Publishing | publication semantics, shared PublicationGateway, publish intents, external mutation lifecycle | PublishIntentResult / ProviderSubmissionResult |
| L08 | Analytics | ingestion and normalization of observed platform/traffic metrics | AnalyticsResult |
| L09 | Learning | evidence-based lessons and improvement actions from verified production observations | LearningResult |
| L10 | Monetization / Affiliate | product/program evidence, affiliate semantics, commercial attribution and revenue/commission evidence | AffiliateResult / RevenueResult |
| L11 | Integrations | external provider lifecycle and provider adapters; transport integration boundaries | IntegrationResult |
| L12 | AI Foundation | model routing, provider metadata, usage, model failure semantics and generation boundary | GenerationResult |
| L13 | Persistence | canonical production persistence contracts, repositories and persistence-facing domain records | DurableRecord |
| L14 | Enterprise Integration / Control Plane | workflow meaning, request identity, correlation, orchestration, policy composition | WorkflowEnvelope |
| L15 | Durable Execution | task execution, scheduling, retry, timeout, cancellation, leases, reconciliation workers and DLQ/operator queues | TaskExecution |
| L16 | Database Engineering | SQL, connections, pools, transactions, migrations, schema mechanics and database recovery primitives | TransactionalOperation |
| L17 | Security | authentication, authorization, secret handling, encryption/signatures, SSRF/path/replay/tool safety | SecurityDecision |
| L18 | Monitoring | runtime/dependency/capability health, telemetry and operational recovery visibility | HealthTelemetry |
| L19 | Analytics Engine | forecasts, recommendations and derived analytics with observed/projected separation | ForecastResult |
| L20 | Image Pipeline | canonical asset validation/normalization, provenance, public-media lifecycle and multimodal asset handling | ValidatedAsset |
| L21 | Deployment | build, container/runtime, readiness, release, rollback, SBOM/vulnerability and recovery deployment controls | DeployableArtifact |
| L22 | Documentation | contracts, ADRs, architecture records, runbooks, support matrix and incident knowledge | DocumentationEvidence |
| L23 | Website Manager | website lifecycle, WordPress/AtoZ/web operations; website publishing MUST use shared PublicationGateway | WebsiteResult |

### Frozen ownership migration obligations

The ownership table is normative; renaming a layer is insufficient.

- L07 → L11: provider adapters, provider API clients, OAuth/provider lifecycle, capability discovery and provider error normalization.
- L07 → canonical credential boundary: account credential resolver moves out of L07; L07 consumes the resolver contract.
- L14 → L11: search, affiliate, GA4/analytics and external provider transport from real_integrations; business semantics remain L02/L08/L10/L23.
- L14 → L23: WordPress/web business semantics remain L23; L14 only orchestrates.
- L14 → L10/L11: affiliate rules remain L10; affiliate-network adapters move L11.
- layer11_async_runtime durable responsibilities → L15; only integration transport/plugin primitives remain L11.
- L15 task state, leases, retry state, reconciliation and DLQ/operator state are PostgreSQL-backed.

Freeze evidence must include source path → target layer/contract → disposition (move/wrap/retire) for every affected module.

### Frozen ownership decisions

- **L10 naming is canonicalized as “Monetization / Affiliate”.** Existing `layer10_monetization` naming is compatible and is not treated as a second layer.
- **L11 is Integrations, not Async Runtime.**
- **L15 is the only canonical durable async execution owner.**
- The existing `layer11_async_runtime` implementation is a migration source: generic integration transport/plugin capabilities may move under L11; durable scheduling, worker, retry, cancellation and queue capabilities move to L15; redundant implementation is retired after migration.
- L14 never implements provider-specific mutation.
- L13 is the canonical persistence owner; L16 supplies database mechanics.
- L12 owns model routing; L05 requests creative generation and L20 validates/normalizes resulting assets.
- L07 owns publication semantics; L11 owns provider lifecycle/adapters.
- L08 owns observed analytics; L19 owns projections/derived decision support.
- L23 owns website business semantics but does not bypass the shared publication boundary.

---

## 5. Dependency architecture

The canonical dependency graph is directional and contract-based.

`L01 → L17 → L13/L16 → L14 → L15`

`L02 → L03 → L04 → L12 → L05 → L20 → L06 → L07 → L08 → L19/L09`

L10 → L11 only through explicit monetization-provider contracts; provider evidence returns through typed result contracts. No implementation-level L11 → L10 dependency is permitted.

L07/L08/L10/L23 → L11 provider adapters through explicit ports; L11 does not import those layer business implementations.

`L23 → L07 PublicationGateway` and `L11` provider adapters.

`L18/L21` observe and operate runtime/deployment state but do not mutate business state implicitly.

`L22` documents stable boundaries.

### Dependency rules

- Direct imports of another layer's private implementation are prohibited when a stable contract/port exists.
- No dependency may create a business-ownership cycle.
- Shared utilities are cross-cutting infrastructure and cannot silently become a layer's business owner.
- L14 orchestrates by contract, not by constructing provider-specific classes.
- L15 executes workflow tasks; it does not define business workflow policy.
- L16 must never become a second persistence authority.

---

## 6. Canonical end-to-end workflow

Every production content job has a durable `workflow_id`, `workflow_step_id` values and a stable `publish_operation_id` for each external logical publication.

`PREFLIGHT → RESEARCH → INTELLIGENCE → PLANNING → ATTRIBUTION → GENERATION → QUALITY → AUTHORIZATION_RECHECK → PUBLISH → VERIFY → ANALYTICS → LEARNING → REVENUE`

### 6.1 PREFLIGHT
Validate identity, authorization, provider/account readiness, credential status, publish mode, media capability, AI availability, quality prerequisites and platform policy.

### 6.2 RESEARCH
L02 produces provenance-bearing source observations.

### 6.3 INTELLIGENCE
L03 produces an `IntelligenceBundle` from research evidence.

### 6.4 PLANNING
L04 produces deterministic content/platform intent and asset requirements. L14 orchestrates this step but does not own planning logic.

### 6.5 ATTRIBUTION
Create/resolve tracked destinations and affiliate references before mutation where applicable.

### 6.6 GENERATION
L12 generates text; L05 requests creative generation; L20 validates/normalizes assets. Provider failure is explicit.

### 6.7 QUALITY
L06 evaluates hard safety/compliance gates and weighted quality metrics.

### 6.8 AUTHORIZATION_RECHECK
Immediately before external mutation, revalidate account identity, authorization, credential usability and provider capability.

### 6.9 PUBLISH
L07 creates a durable logical publication intent and delegates provider-specific calls to the adapter.

### 6.10 VERIFY
Reconcile provider evidence into a canonical publication state.

### 6.11 ANALYTICS
L08 records observed metrics independently of publication success.

### 6.12 LEARNING
L09 consumes only verified production observations.

### 6.13 REVENUE
L10 records commercial revenue/commission evidence only when supported by an authoritative external source.

---

## 7. Workflow and result contracts

All durable result contracts are versioned and serializable.

Required contracts:

- `WorkflowEnvelope`
- `ResearchResult`
- `IntelligenceBundle`
- `PlannerResult`
- `TrackingResult`
- `GenerationResult`
- `QualityResult`
- `PublishIntentResult`
- `ProviderSubmissionResult`
- `VerificationResult`
- `AnalyticsResult`
- `LearningResult`
- `AffiliateResult`
- `RevenueResult`

Common envelope fields:

`schema_version, workflow_id, workflow_step_id, tenant_id, workspace_id, brand_id, account_id, platform, platform_account_id, request_id, correlation_id, created_at, status, provenance`

Additional semantic fields are required as appropriate:

- `provider`
- `provider_request_id`
- `provider_tracking_id`
- `external_post_id`
- `error_code`
- `retryable`
- `observed_at`
- `source_id`
- `source_timestamp`
- `confidence`

### Contract invariant

A workflow step cannot be retried into a later step unless its prior result is durably persisted or deterministically reconstructible.

---

## 8. Identity and tenancy

Canonical hierarchy:

`Tenant → Workspace → Brand → Account → PlatformAccount`

### Required identifiers

- tenant_id
- workspace_id
- brand_id
- account_id
- platform
- platform_account_id
- external_account_id where applicable
- workflow_id
- workflow_step_id
- publish_operation_id where applicable
- request_id
- correlation_id

### Isolation

Every business record uses the narrowest applicable scope.

Database repositories MUST require or derive the correct scope. Missing scope is an error for scoped business records.

Production authorization MUST validate:

`tenant → workspace → brand → account → platform account → operation`

No credential, content history, learning state, analytics state, media or publication intent crosses account scope without explicit authorized access.

### Identity uniqueness

Canonical uniqueness constraints include:

- `platform_account(provider, external_account_id)`
- `platform_account(account_id, platform)`
- `workflow(workflow_id)`
- `publish_intent(account_id, platform, publish_operation_id)`
- `publish_intent(idempotency_key)`

Exact DB constraint naming is implementation detail; uniqueness semantics are architectural.

---

## 9. Canonical PostgreSQL persistence model

PostgreSQL is the only production business source of truth.

### Core tables / entities

**Identity**

`tenants, workspaces, brands, accounts, platform_accounts`

**Credentials**

`credentials, oauth_grants, credential_versions`

**Workflow**

`workflows, workflow_steps, task_leases, dead_letter_items`

**Research / intelligence**

`research_records, research_sources, intelligence_bundles, content_plans`

**Content / assets**

`content_assets, creative_generations, quality_results, tracked_links`

**Publication**

`publish_intents, publish_attempts, provider_effects, publication_verifications, publication_history`

**Analytics / monetization / learning**

`analytics_observations, affiliate_programs, affiliate_events, revenue_events, learning_observations, forecasts`

**Operations**

`audit_events, inbox_events, outbox_events`

### Persistence ownership

L13 owns domain persistence contracts and repositories.

L16 owns:

- connection/pool mechanics
- SQL/query mechanics
- transaction context
- migrations
- schema validation
- database recovery primitives

No layer creates a second production database authority.

### SQLite rule

SQLite MAY be used for development/test compatibility only. Production paths must fail closed when PostgreSQL is unavailable or not configured as required.

---

## 10. Canonical publication data model

A publication is modeled as a logical operation, not as one HTTP request.

### PublishIntent

A `PublishIntent` identifies the exact logical content publication UCOS intends to perform.

Required fields include:

`intent_id, publish_operation_id, workflow_id, account_id, platform, platform_account_id, idempotency_key, content_asset_refs, tracked_link_ref, requested_visibility, policy_snapshot, created_at`

### PublishAttempt

One intent may contain multiple provider calls.

Required fields include:

`attempt_id, intent_id, attempt_number, started_at, finished_at, outcome_classification, provider_request_id, error_code, retryable`

### ProviderEffect

Every known external effect is recorded separately.

Examples:

- provider tracking ID
- external post ID
- uploaded media ID
- resumable upload session
- container ID
- provider operation ID

Fields include:

`effect_id, intent_id, provider, effect_type, provider_effect_id, discovered_at, metadata`

### PublicationVerification

Stores provider-side evidence and canonical verification result.

### PublicationHistory

Stores the final business history after a terminal or explicitly retained unresolved outcome.

---

## 11. Publish state machine — frozen

RESERVED → INTENT_CREATED → CALLING

CALLING → FAILED_CONFIRMED | OUTCOME_UNKNOWN | SUBMITTED

SUBMITTED → VERIFYING | PUBLISHED_NOT_PUBLIC | VERIFIED_PUBLIC | VERIFICATION_UNKNOWN | IDENTITY_MISMATCH | VERIFICATION_FAILED

OUTCOME_UNKNOWN → RECONCILING

RECONCILING → SUBMITTED | VERIFYING | PUBLISHED_NOT_PUBLIC | VERIFIED_PUBLIC | VERIFICATION_UNKNOWN | EXPIRED_UNVERIFIED | IDENTITY_MISMATCH | VERIFICATION_FAILED | FAILED_CONFIRMED

VERIFYING → VERIFIED_PUBLIC | PUBLISHED_NOT_PUBLIC | VERIFICATION_UNKNOWN | IDENTITY_MISMATCH | VERIFICATION_FAILED | EXPIRED_UNVERIFIED

PUBLISHED_NOT_PUBLIC → VERIFYING | VERIFIED_PUBLIC | VERIFICATION_UNKNOWN | EXPIRED_UNVERIFIED

VERIFICATION_UNKNOWN → RECONCILING | VERIFYING | VERIFIED_PUBLIC | PUBLISHED_NOT_PUBLIC | EXPIRED_UNVERIFIED | IDENTITY_MISMATCH | VERIFICATION_FAILED

IDENTITY_MISMATCH → RECONCILING | VERIFICATION_FAILED | EXPIRED_UNVERIFIED

VERIFICATION_FAILED → RECONCILING | EXPIRED_UNVERIFIED

EXPIRED_UNVERIFIED is terminal for automatic reconciliation, but is not proof of non-publication.

### Reservation action matrix

| State | Reservation | Automatic new publish |
|---|---|---|
| RESERVED/INTENT_CREATED/CALLING | held | blocked |
| SUBMITTED/VERIFYING/PUBLISHED_NOT_PUBLIC | held | blocked |
| OUTCOME_UNKNOWN/RECONCILING/VERIFICATION_UNKNOWN | held | blocked |
| IDENTITY_MISMATCH/VERIFICATION_FAILED | held | blocked; operator review |
| EXPIRED_UNVERIFIED | held by default | blocked until operator resolution |
| FAILED_CONFIRMED | releasable transactionally | allowed after release |
| VERIFIED_PUBLIC | completed | allowed only as a new logical operation |

Provider silence, timeout, process death or lost response MUST NOT become FAILED_CONFIRMED without independent evidence.
---

## 12. Reservation and idempotency semantics

Reservation, repetition check and INTENT_CREATED are one PostgreSQL transaction. The check-and-reserve operation is atomic and uses PostgreSQL uniqueness/locking: two concurrent requests cannot both win the same policy slot. L06 supplies the decision; L07 owns the reservation ledger.

The logical publish identity is:

`tenant_id + account_id + platform + workflow_id + publish_operation_id`

The idempotency key is derived from that logical identity, not from generated text.

A workflow may contain multiple publication operations; each gets a distinct `publish_operation_id`.

### Reservation retention

The reservation remains held for:

`RESERVED, INTENT_CREATED, CALLING, SUBMITTED, OUTCOME_UNKNOWN, RECONCILING, VERIFYING, PUBLISHED_NOT_PUBLIC, VERIFICATION_UNKNOWN`

Only definitive `FAILED_CONFIRMED` may release the business reservation automatically.

No startup cleanup is allowed to delete a post-call unresolved record.

### Unresolved-intent gate

L07 blocks a new publish for an account/platform while an intent is in CALLING, SUBMITTED, OUTCOME_UNKNOWN, RECONCILING, VERIFYING, PUBLISHED_NOT_PUBLIC, VERIFICATION_UNKNOWN, IDENTITY_MISMATCH, VERIFICATION_FAILED or EXPIRED_UNVERIFIED. The response exposes intent_id, state, age and reconciliation/operator status. Only an audited operator-resolution API may release the block.

---

## 13. Crash-safe external mutation protocol

External mutation and database transaction are intentionally separated.

### Before provider call

1. Transaction creates/updates `PublishIntent`.
2. State becomes `CALLING`.
3. An audit event and outbox event are committed.
4. Transaction commits.

### Provider call

Provider adapter performs its provider-specific API sequence.

### After provider response

In a new transaction:

1. Record `PublishAttempt`.
2. Record any `ProviderEffect`.
3. Record normalized outcome.
4. Transition state.
5. Emit audit/outbox records.
6. Commit.

### Crash between provider call and DB save

The process is not allowed to release the intent.

The reconciler finds `CALLING` attempts without final DB outcome and moves them into `OUTCOME_UNKNOWN` / `RECONCILING`, then performs provider discovery.

This directly covers fault-injection case B.

---

## 14. Provider adapter contract — frozen

Every production provider adapter implements the common publication boundary:

- `preflight(context)`
- `capabilities()`
- `publish(intent)`
- `get_post(external_post_id)`
- `get_publish_status(provider_tracking_id)` when provider supports asynchronous processing
- `find_by_marker(marker)` when provider supports provider-side search
- `normalize_error(error)`
- optional `delete_or_hide(effect)` only where supported and explicitly authorized

### Provider submission result

A provider result MUST classify:

- confirmed rejection
- transient failure before mutation
- ambiguous outcome
- accepted/processing
- accepted with external identifier
- confirmed external object created
- unsupported operation

A provider tracking ID is never silently stored as `external_post_id`.

### Provider marker

The adapter MAY send a safe, deterministic, non-secret marker that allows reconciliation to locate a publication when a final external ID was not returned.

Marker requirements:

- deterministic for the publish operation
- does not contain credentials or secrets
- scoped to the intended account where possible
- persisted in `PublishIntent`

---

## 15. Provider capability model — frozen

Capabilities must expose at least:

`supports_images`

`supports_video`

`supports_carousel`

`supports_edit`

`supports_delete_or_hide`

`supports_native_schedule`

`supports_async_processing`

`supports_operation_status`

`supports_lookup_by_id`

`supports_lookup_by_marker`

`requires_public_media_url`

`requires_local_file`

`supported_visibility_modes`

`max_text_length`

`max_assets`

`platform_policy_requirements`

Provider capability discovery is part of preflight and authorization recheck.

---

## 16. Platform-specific verification semantics

### Facebook

Public verification requires provider evidence for:

- intended Page/account ownership
- object existence
- published state
- non-hidden state where applicable
- public permalink

### Instagram

Verification must prove:

- intended Instagram account ownership
- media object existence
- container/publish processing completion where applicable
- requested visibility/public availability
- stable external identifier

### Pinterest

Verification must prove:

- intended account/board ownership
- Pin existence
- valid public Pin state
- canonical Pin URL

### TikTok

The Content Posting API `publish_id` is a provider tracking identifier.

Verification must use provider status/reconciliation semantics and MUST NOT claim that `publish_id` is a final public post ID.

Production publishing requires `PUBLIC_TO_EVERYONE` where the provider requires that public option. If it is unavailable, preflight blocks production mutation.

### YouTube

Verification must inspect the actual video resource and requested `privacyStatus` plus ownership/channel identity. A private or unverified resource is not `VERIFIED_PUBLIC`.

### General rule

A successful provider HTTP response is submission evidence, not necessarily public-visibility evidence.

---

## 17. Shared Publication Gateway

L07 owns a reusable `PublicationGateway`.

The gateway is the only canonical mutation boundary used by:

- social publishing
- website/WordPress publishing
- future external publication targets

The gateway enforces:

`authorization → quality → repetition → intent → provider mutation → verification`

L23 supplies website-specific content semantics to the gateway but MUST NOT directly create a network publication outside it.

This removes the previous L23 local-`PUBLISHED` side door.

---

## 18. Website / WordPress architecture

L23 owns:

- websites
- articles
- website SEO
- website structure
- site-level business semantics
- website scheduling intent

External WordPress/network publication uses:

`L23 → L07 PublicationGateway → L11 WordPress Adapter → external network → verification`

A local `ArticleStatus.PUBLISHED` is never sufficient for production network publication truth.

Local drafts MAY exist in development/test storage, but production article state must be backed by PostgreSQL and network verification evidence.

---

## 19. Identity-aware credentials

Every production credential has:

- credential_id
- provider
- account_id
- platform_account_id where applicable
- credential_type
- issued_at
- expires_at OR non_expiring=true
- scope
- status
- encryption_key_version
- credential_version

Optional refresh metadata includes a secure refresh reference and lifecycle timestamps.

### Credential rules

- Unknown expiry is not production-valid.
- Credentials are encrypted at rest.
- Secret material never appears in logs, analytics, audit payloads, registry documents, workflow results or Git history.
- Refresh is serialized per credential identity to prevent refresh races.
- Revoked credentials cannot be selected for mutation.
- Authorization is rechecked immediately before mutation.

---

## 19A. Publication verification attestation and canary

A privileged provider lookup is not sufficient proof of public visibility where provider semantics are role-dependent.

Every production provider/account/platform requires a readiness attestation recording application mode/status, authorization scope/role, capability test, visibility method, canary ID/time, independent/non-role observation where possible, trial/review/audit restrictions, expiry and owner.

A production canary must prove that a new test publication is observable with intended visibility by an independent/non-role viewer or equivalent public endpoint. A privileged role-holder read is insufficient where non-representative.

Provider certification must explicitly cover Facebook Development/Live mode, Pinterest Trial/review limitations, TikTok Direct Post audit/readiness and YouTube public/unlisted/private semantics.

If independent observation is unavailable, use VERIFICATION_UNKNOWN or PUBLISHED_NOT_PUBLIC as appropriate; never promote to VERIFIED_PUBLIC solely from privileged evidence.

---

## 20. Public media architecture

Canonical flow:

`L05 creative generation → L20 validated asset → public media object → HTTPS URL → L07 provider adapter`

Asset record requires:

- asset_id
- content_hash
- MIME type
- byte size
- dimensions/duration
- provenance
- account/brand scope
- storage object reference
- public URL state
- retention class

### Production requirement

Local `output/images`, `/tmp`, container filesystems and `articles.json` are not production public media origins.

The deployment must provide an object/media origin capable of:

- HTTPS
- stable object addressing
- appropriate cache headers
- access policy
- lifecycle cleanup
- health validation

An asset with an unresolved publication dependency MUST NOT be garbage-collected.

---

## 21. Quality architecture

L06 is the final publication quality gate.

`QualityResult` contains both hard gates and quantitative metrics.

Minimum structure:

- factuality
- source/evidence coverage
- safety
- platform policy
- brand policy
- originality
- repetition
- affiliate disclosure where applicable
- media validity
- tracked-link validity
- hard_failures[]
- warnings[]
- score

### Hard-gate invariant

A weighted quality score cannot override a hard safety, policy, authorization or publication-compliance failure.

Example:

`score = 0.97 + hard_safety_failure = REJECT`

---

## 22. Repetition architecture

Repetition protection is business policy, not the publication state machine.

Canonical key scope:

`account + platform + fingerprint + policy window`

Fingerprint types may include:

- exact content fingerprint
- structural/template fingerprint
- hook family fingerprint
- media similarity fingerprint

Policy windows are configurable per account/platform policy.

A template identifier alone is not evidence of output repetition.

Repetition checks run before external mutation and are independent of the provider's publication state.

---

## 23. Staging versus production

publish_mode is resolved server-side; a caller cannot select a privileged mode directly.

### Mode authority

effective_mode = policy(deployment_environment, account_environment, requested_mode).

The production deployment matrix is normative: production + staging account = staging only; production + production account = production only; no caller can elevate a production account into a lower-safety path that bypasses production gates.

- A client may request only an equal-or-more-restrictive mode; it cannot elevate staging to production.
- Production deployment + production account requires production mode and production authorization.
- Production deployment + staging account permits staging only; production credentials must not be used.
- Development/test deployments cannot execute production publication.
- effective_mode is persisted at INTENT_CREATED and cannot be changed afterward without a new authorized workflow.
- requested_mode and effective_mode are auditable.

| Deployment | Staging account | Production account |
|---|---:|---:|
| development | staging only | blocked |
| test/CI | staging only | blocked |
| production | staging only | production only |

Caller-supplied staging therefore cannot bypass production gates for a production account. Offline-draft, authorization, quality, credential and mutation-safety gates remain mandatory.

### Staging

- test/private provider operations where permitted;
- marked in audit/workflow;
- no production publication history;
- no production learning;
- no production revenue;
- no production credentials where avoidable.

### Production

Requires production identity, authorization, real credentials, AI/content prerequisites, quality approval, public media when required, attribution where required, durable intent and verification/reconciliation.
---

## 24. Analytics architecture

L08 owns observed analytics.

Observed records require:

`provider, account_id, platform, external_object_id, metric, value, observed_at, received_at, source`

Examples:

- impressions
- reach
- clicks
- reactions
- comments
- shares
- views

L08 does not manufacture missing values.

Analytics outages do not retroactively change publication state.

---

## 25. Monetization and revenue architecture

L10 owns commercial/affiliate semantics.

Separate concepts:

`click`

`conversion`

`commission`

`revenue settlement`

must not be collapsed into one generic metric.

`RevenueResult` requires authoritative external evidence and includes:

- provider/program
- external event ID
- account/brand scope
- workflow/publication reference where known
- amount
- currency
- event occurred_at
- received_at
- deduplication key
- source/provenance
- evidence status

Unknown revenue is not zero revenue.

---

## 26. Analytics Engine and Learning

L19 consumes observed data and produces:

- forecasts
- projections
- recommendations
- evidence-backed decision support

Projected values are stored separately from observed values.

L09 consumes verified production observations only.

Forbidden:

- staging → production learning
- unknown outcome → negative outcome
- projection → observed result
- another account's learning state → current account without explicit authorized transfer
- inferred revenue → reported revenue

---

## 27. Inbox / Outbox architecture

### Inbox

`inbox_events` provides idempotent handling of inbound events such as:

- provider webhooks
- OAuth callbacks
- provider processing notifications
- analytics events
- affiliate/conversion events

Canonical deduplication key:

`provider + external_event_id`

with payload hashing and processing status.

### Outbox

Any DB state transition that must cause asynchronous work records its outbox message in the same PostgreSQL transaction.

Canonical flow:

`state mutation + outbox row → commit → outbox dispatcher → execution`

This prevents “DB committed but worker notification lost” inconsistencies.

---

## 28. Durable execution and reconciliation

L15 is the sole owner of execution mechanics and uses PostgreSQL-backed durable state.

Every CALLING attempt has call_deadline_at and attempt_lease_expires_at. Reconciliation cannot classify a still-leased active call as crashed. Crash classification requires both deadline and lease expiry, or definitive worker lease/heartbeat loss, and is transactional.

For unresolved publication: claim lease; validate account/credential scope; inspect provider effect IDs; inspect processing status; search deterministic markers; validate owner and requested visibility; use independent/public observation where required; transition transactionally; release lease; create operator action if inconclusive.

A provider search/list “not found” is not FAILED_CONFIRMED by itself. It remains VERIFICATION_UNKNOWN and, after the reconciliation window, EXPIRED_UNVERIFIED unless independent evidence proves non-publication.

### Baseline cadence and SLA

- first reconciliation within 30 seconds;
- subsequent attempts approximately 1m, 5m, 15m, 30m, 60m;
- default reconciliation SLA 2 hours;
- provider-specific longer windows may override when documented;
- SLA exhaustion → EXPIRED_UNVERIFIED + operator-resolution item, never inferred failure.

Every reconciliation task has lease_owner, lease_acquired_at, lease_expires_at and attempt_count. Expired leases are recoverable; worker crash must not strand a publication.
---

## 29. Retry policy

Retries are classified:

### Safe to retry automatically

- pre-provider read-only lookup
- idempotent database operations
- confirmed transient provider failures before mutation
- reconciliation lookups

### Not safe to blindly retry

- external mutation after ambiguous transport failure
- mutation where provider effect may already exist
- operations lacking an idempotency key or reconciliation route

A retry of an ambiguous mutation MUST be a reconciliation action first.

---

## 30. Scheduling

All persistent schedules use UTC timestamps internally and retain the originating timezone metadata.

Scheduling semantics define:

- schedule identity
- timezone
- DST behavior
- misfire policy
- cancellation
- lease ownership
- late execution policy
- duplicate prevention
- retry window

Scheduled publication still creates a normal `PublishIntent` before the external mutation.

---

## 31. Monitoring and health

Health has separate dimensions:

- process liveness
- dependency readiness
- database readiness
- workflow runtime readiness
- provider readiness
- capability readiness
- account readiness

A single broken integration MUST NOT necessarily mark unrelated capabilities as globally unavailable.

Every health observation identifies:

`component, account/platform when applicable, dependency, status, timestamp, correlation`

HTTP readiness endpoints return a failure status when the declared readiness criteria fail.

---

## 32. Security boundaries

L17 provides reusable:

- authentication
- authorization
- secret encryption/redaction
- SSRF prevention
- path containment
- replay protection
- idempotency protection
- input validation
- tool execution safety
- audit integrity

Security failures at an external-mutation boundary are fail-closed.

No provider adapter may choose a different credential outside the account-scoped credential resolver.

---

## 33. Audit architecture

Audit events are append-only business/security evidence.

Required fields:

`event_id, timestamp, actor_id, tenant_id, workflow_id, request_id, account_id, platform, layer, operation, old_state, new_state, outcome, correlation_id, trace_id, application_version, provider_request_id`

Secrets, authorization headers and raw credential material are redacted or excluded.

Audit retention is a deployment policy, but production certification requires an explicit retention configuration and restore test.

---

## 34. Backup, recovery and disaster recovery

PostgreSQL is backed up using the deployment's managed backup strategy.

Production recovery must prove:

- backup exists
- backup integrity can be validated
- schema version is recoverable
- migration history is preserved
- unresolved publication intents survive restore
- no ambiguous publication is silently downgraded
- workflow leases can recover
- outbox/inbox records remain processable

Baseline operational targets:

- target RPO: ≤ 15 minutes
- target RTO: ≤ 60 minutes

These are architecture targets, not a claim that every deployed environment currently meets them.

---

## 35. Migration from current implementation

The current implementation is a migration baseline, not architecture authority. Inventory must include code, schemas, local stores and registries.

### Async ownership

layer11_async_runtime is inventoried file-by-file:
- integration transport/plugin primitives → L11;
- durable scheduler/task/worker/retry/cancellation → L15;
- stateless process-local helpers may remain only as mechanics;
- redundant implementations → retire after regression equivalence.

L15 certification requires PostgreSQL-backed task state, leases, retries, reconciliation and DLQ/operator state.

### Legacy publication mapping

| Legacy state | Evidence condition | Canonical state |
|---|---|---|
| reserved + proven no provider call could start | definitive pre-mutation evidence | RESERVED / INTENT_CREATED |
| reserved + call start cannot be distinguished | legacy code lacks call-start evidence | OUTCOME_UNKNOWN → RECONCILING |
| pending + known provider effect/tracking ID | provider effect exists | SUBMITTED / RECONCILING |
| pending + ambiguous outcome | no definitive result | OUTCOME_UNKNOWN |
| published + independent public evidence | independent verification exists | VERIFIED_PUBLIC |
| published without independent evidence | local legacy state only | RECONCILING / VERIFICATION_UNKNOWN |
| definitive provider rejection | authoritative rejection | FAILED_CONFIRMED |

Never migrate every legacy published row directly to VERIFIED_PUBLIC.

### Required inventory

At minimum: L07 account registry; L07 policy and credential resolver; L14 real_integrations search/affiliate/GA4/WordPress gateways; per-account publishing_history.sqlite3; agent.db; per-account memory/analytics/learning SQLite; policy registries; AtoZ job inbox/state; L11/L15 async queues/stores; L23 articles.json; provider credential/token stores and caches.

Each item gets owner, scope, schema, row count, authority classification, migration transform, retirement plan and verification evidence.

Legacy local stores migrate to canonical PostgreSQL contracts or are explicitly classified as non-authoritative cache/test artifacts before production certification. No local file is silently canonical.

L23 articles.json becomes development/test compatibility only; production website records migrate to PostgreSQL and network publication uses the shared PublicationGateway.
---

## 36. L05 / L20 freeze boundary

Frozen flow:

`L05 creative intent/generation → L20 asset validation/normalization/public-media → L07 publication`

L05 does not own canonical asset storage.

L20 does not own content strategy or writing.

L12 remains the model/provider routing owner.

---

## 37. L11 / L15 freeze boundary

Frozen split:

**L11 Integrations**
- provider lifecycle
- OAuth/provider API semantics
- provider capability discovery
- provider-specific transport/adapters
- provider error normalization

**L15 Durable Execution**
- task state
- worker lifecycle
- retries
- timeouts
- cancellation
- scheduling
- leases
- reconciliation jobs
- DLQ/operator queue

L11 MUST NOT create a competing workflow engine.

L15 MUST NOT implement provider-specific publication logic.

---

## 38. L13 / L16 freeze boundary

**L13**
- canonical domain repositories
- persistence contracts
- production records
- persistence-facing data model

**L16**
- SQL
- migrations
- transaction mechanics
- pool lifecycle
- query execution
- recovery primitives

L13 calls L16 mechanics through an explicit database interface.

No pipeline component creates an independent production SQLite store.

---

## 39. L08 / L19 freeze boundary

**L08:** observed external measurements.

**L19:** derived calculations, forecasts and recommendations.

An observed value may feed a forecast, but a forecast can never be written back as an observation.

---

## 40. L10 / L11 freeze boundary

**L10:** affiliate/monetization business semantics.

**L11:** external affiliate/network provider lifecycle.

Therefore:

`L10 Commercial Policy → L11 Provider Adapter → external source → L10 Evidence`

---

## 41. L14 / L15 freeze boundary

**L14**
- business workflow meaning
- orchestration graph
- request identity
- correlation
- step sequencing
- policy composition

**L15**
- execution state
- queue
- worker
- schedule
- lease
- retry
- timeout
- cancellation
- reconciliation

The workflow engine implementation remains replaceable behind the frozen durable execution contract.

---

## 42. Architecture decision record — durable workflow engine

The architecture freezes workflow semantics, not a vendor-specific product.

The existing L15 code is a mechanics library only unless durable implementation evidence is added. In-memory queues, retry helpers and thread pools alone do not satisfy the frozen contract.

L15 must persist in PostgreSQL: task/workflow-step state, task idempotency, lease owner/expiry, attempts, retry schedule, cancellation, timeout classification, reconciliation state and DLQ/operator state.

Process-local helpers are allowed only as stateless mechanics. No business task may depend on process memory as its sole durable state.

DBOS/Temporal/Celery/another engine may back L15 only behind the same contract. If existing L15 is used, PostgreSQL task persistence, crash recovery, lease recovery, DLQ and restart tests are mandatory before production certification. Duplicate layer11_async_runtime durable responsibilities are retired after regression equivalence.
---

## 43. Build-vs-integrate decisions

Build internally:

- domain orchestration
- account isolation
- policy gates
- publication state machine
- evidence model
- attribution semantics
- reconciliation semantics
- canonical contracts

Prefer mature integrations for:

- LLM inference
- image/video generation
- search/research sources
- social APIs
- affiliate networks
- link tracking
- public object/media storage
- optional workflow infrastructure

Postiz, LiteLLM, Kubernetes, Qdrant, MinIO, Redis clusters and similar components are optional implementation choices.

---

## 44. Fault-injection certification matrix

The frozen architecture requires executable tests for:

### A — Provider accepts then transport times out

Expected:

`CALLING → OUTCOME_UNKNOWN → RECONCILING`

No blind republish.

### B — Process dies after provider call before DB save

Expected:

- intent remains recoverable;
- reconciler detects incomplete attempt;
- no duplicate logical publication is created;
- late provider effect is associated with original intent.

### C — Explicit provider rejection

Expected:

`CALLING → FAILED_CONFIRMED`

Reservation may be released according to policy.

### D — TikTok has no public privacy option

Expected:

- production preflight fails;
- provider mutation is never called.

### E — Offline draft reaches production boundary

Expected:
- production mutation blocked before provider call.

### F — Provider accepts, but resulting post is non-public

Expected:
- acceptance remains SUBMITTED;
- verification yields PUBLISHED_NOT_PUBLIC;
- no VERIFIED_PUBLIC claim;
- reservation remains held.

### G — Production environment receives staging request for a production account

Expected:
- server-side effective-mode policy rejects the unsafe request;
- caller-supplied staging cannot bypass production gates;
- no provider mutation occurs.

### H — Two concurrent requests race to reserve the same repetition slot

Expected:
- exactly one transaction acquires the canonical L07 reservation;
- the other receives deterministic conflict/unresolved response;
- no duplicate external mutation starts.

---

## 45. Production implementation sequence — mandatory Stage 0

No post-freeze implementation stage may skip the P0 safety baseline.

### Stage 0 — P0 safety baseline

CI must prove before later implementation certification:
- offline-draft gate blocks production mutation;
- ambiguous outcomes remain held/reconcilable;
- TikTok production requires the allowed public visibility path;
- Docker startup fails closed when required PostgreSQL/Redis dependencies are unavailable;
- readiness/health reports dependency failure correctly;
- CI is green for the production safety suite;
- fault tests E, G and ambiguity handling are executable.

Stage 0 is the first mandatory implementation certification gate after explicit architecture freeze.

---

## 46. Certification gates

Production architecture implementation is not certified merely because code compiles.

Certification evidence must prove:

1. 23 logical layers resolve to the frozen ownership map.
2. No duplicate async runtime owner remains.
3. Contract schemas validate.
4. PostgreSQL is the production source of truth.
5. Identity and account scoping are enforced.
6. Publish state transitions are transactionally valid.
7. Idempotency prevents duplicate logical mutation.
8. Provider tracking IDs and external post IDs remain distinct.
9. Ambiguous outcomes are retained.
10. Reconciliation can resolve known cases.
11. Public media is reachable.
12. L23 cannot bypass the shared publication boundary.
13. Staging cannot contaminate production evidence.
14. Hard quality/security gates cannot be overridden by score.
15. Inbox/outbox deduplication works.
16. Crash recovery works.
17. Backups/restore preserve unresolved state.
18. Required real-provider tests pass where claimed.
19. Health/readiness semantics are correct.
20. Audit evidence is complete and redacted.
21. Fault injections A–H pass.
22. Stage 0 P0 safety evidence is green.

---

## 47. Required architecture artifacts after freeze

The registry must contain:

- frozen master architecture
- layer ownership matrix
- dependency DAG
- canonical data model
- workflow contracts
- publish state machine
- provider adapter contract
- reconciliation specification
- identity/RBAC model
- media architecture
- credential lifecycle
- analytics/attribution model
- inbox/outbox model
- failure/recovery model
- migration mapping
- deployment topology
- security boundaries
- retention/RPO/RTO policy
- architecture change-control record

---

## 48. Architecture change control

After freeze:

`Architecture Change Request → impact analysis → contract review → migration plan → approval → implementation → regression → certification evidence`

No implementation change may silently alter:

- layer ownership
- canonical states
- identity scope
- persistence authority
- provider semantics
- staging/production boundaries
- external mutation safety

---

## 49. Freeze acceptance criteria

This candidate is ready for explicit freeze approval only when reviewers acknowledge all of the following:

- L10/L11/L15 ownership is unambiguous.
- L05/L20 ownership is unambiguous.
- L13/L16 ownership is unambiguous.
- L08/L19 ownership is unambiguous.
- L23 publication bypass is architecturally prohibited.
- PostgreSQL is canonical.
- canonical publication states are fixed.
- reconciliation is a first-class durable capability.
- provider identifiers are typed by semantic role.
- inbox/outbox behavior is defined.
- workflow contracts are versioned.
- identity hierarchy is fixed.
- production/staging semantics are fixed.
- migration mappings are conservative.
- fault-injection requirements A–H are fixed.
- P0 Stage 0 is a mandatory post-freeze implementation gate.
- the final system invariant is accepted.

---

## 50. Final invariant

**UCOS converts evidence into durable, account-isolated, policy-aware actions and never claims an external effect until that effect is supported by provider evidence.**

This invariant governs every layer, contract, retry, database transition, provider adapter, reconciliation action, analytics observation, learning event, revenue record and certification claim.

---

## 51. Freeze status

`UCOS Architecture Freeze Candidate v1.2`

**Status:** NOT YET FREEZE-READY — AWAITING ADVERSARIAL REVIEW

**Next architectural state after approval:**

`FROZEN PRODUCTION ARCHITECTURE BASELINE v1.2`

After approval, implementation proceeds in this order:

`P0 Safety Stage 0 → Canonical Contracts → Ownership Enforcement → PostgreSQL/Data Migration → Durable Execution → Provider/Reconciliation → Identity/RBAC → Media/Credentials → Quality/Attribution → Analytics/Learning → Integration E2E → Production Certification`
