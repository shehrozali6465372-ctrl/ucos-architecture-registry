# UCOS Working Architecture Blueprint v1.0

**Status:** WORKING / PRE-FREEZE  
**Repository:** `shehrozali6465372-ctrl/universal-content-operating-system`  
**Architecture registry:** `shehrozali6465372-ctrl/ucos-architecture-registry`  
**Purpose:** authoritative engineering blueprint for review before architecture freeze.

> **FREEZE RULE:** No new architectural implementation begins from this document until the architecture review, contract/ownership review, and explicit freeze decision are complete. Existing implementation is audited against this blueprint; the blueprint is not bent to fit undocumented legacy behavior.

---

## 1. System mission

UCOS is a production digital-marketing operating system that turns evidence into account-isolated, measurable, policy-aware content and publication workflows.

Canonical business lineage:

`source → niche → keyword → content → asset → platform → account → publish → click → conversion → revenue`

The system must preserve provenance, identity, authorization, state, attribution and evidence across that entire lineage.

### Non-goals

- UCOS is not 23 independently deployed microservices.
- UCOS does not fabricate provider success, analytics, conversions or revenue.
- UCOS does not use one account's credentials, memory or history for another account.
- UCOS does not blindly retry an externally ambiguous publish.
- UCOS does not treat staging activity as production business evidence.

---

## 2. Architectural shape

### 2.1 Logical architecture

UCOS retains **23 logical bounded layers** because they provide ownership, contracts and auditability.

### 2.2 Deployment architecture

The 23 layers are consolidated into approximately **7 runtime capability domains**. Logical separation is preserved even when components share one process/container.

| Runtime domain | Logical layers |
|---|---|
| Foundation & Security | L01, L13, L16, L17 |
| Research & Intelligence | L02, L03 |
| Content & Creative | L04, L05, L12, L20 |
| Quality & Monetization | L06, L10 |
| Publishing & External Integrations | L07, L11 |
| Control & Durable Execution | L14, L15 |
| Analytics, Learning, Operations & Web | L08, L09, L18, L19, L21, L22, L23 |

**Rule:** deployment consolidation must never create shared mutable ownership between layers.

---

## 3. Twenty-three layer ownership contract

| Layer | Canonical owner | Primary responsibility | Canonical output |
|---|---|---|---|
| L01 Core | Core | config, foundational state, memory, scheduling, logging, backup | validated runtime context |
| L02 Research | Research | source/audience research and provenance | ResearchResult |
| L03 Intelligence | Intelligence | niche, keyword, intent, entities, evidence, novelty | IntelligenceBundle |
| L04 Writing | Writing | plans, drafts, variants, CTA | WritingResult |
| L05 Image | Creative | image generation/orchestration and asset provenance | ImageAsset |
| L06 Quality | Quality | safety, factuality, compliance, originality, publication gates | QualityResult |
| L07 Publishing | Publishing | provider adapters, mutation, publication lifecycle | ProviderSubmissionResult |
| L08 Analytics | Analytics | platform metric ingestion and attribution inputs | AnalyticsResult |
| L09 Learning | Learning | observed outcomes, mistakes, improvement actions | LearningResult |
| L10 Affiliate | Monetization | product/program evidence and attribution | AffiliateResult |
| L11 Integrations | Integration | external provider lifecycle boundary | IntegrationResult |
| L12 AI Foundation | AI | model routing, provider metadata, usage/failure handling | GenerationResult |
| L13 Persistence | Persistence | PostgreSQL production source of truth | durable records |
| L14 Enterprise Integration | Control Plane | request identity, correlation, orchestration, enterprise boundary | WorkflowEnvelope |
| L15 Async Runtime | Runtime | retries, cancellation, bounded tasks, DLQ | TaskExecution |
| L16 Database | Database | SQL, transactions, pools, migrations | transactional operations |
| L17 Security | Security | credentials, threat controls, SSRF/path/replay/tool safety | security decisions |
| L18 Monitoring | Operations | health, telemetry, dependency/recovery visibility | Health/Telemetry |
| L19 Analytics Engine | Analytics Engine | forecasting/recommendations with observed/projected separation | ForecastResult |
| L20 Image Pipeline | Creative Pipeline | media validation, provider capability, provenance | ValidatedAsset |
| L21 Deployment | Deployment | container/runtime/readiness/build/recovery | deployable artifact |
| L22 Documentation | Documentation | contracts, ADRs, runbooks, supported interfaces | documentation evidence |
| L23 Website Manager | Web | websites, AtoZ/WordPress and website operations | WebsiteResult |

### Ownership prohibitions

- L07 owns provider mutation; L14 may orchestrate but must not implement provider-specific mutation.
- L13 owns production persistence; L16 owns database mechanics. No second production database authority.
- L12 owns model routing; L05/L20 consume the canonical AI/provider boundary.
- L17 owns security primitives; individual layers consume them rather than creating parallel secret systems.
- L08 owns observed metric ingestion; L19 owns derived forecasting/recommendations.
- L11 owns integration lifecycle; L07 owns social publishing semantics.
- L15 owns execution mechanics; L14 owns workflow meaning.

---

## 4. Canonical dependency DAG

`L01 → L17 → L13/L16 → L14 → L15`

`L02 → L03 → L04 → L12 → L05/L20 → L06 → L10/L07 → L08 → L09/L19`

`L11 → provider capabilities used by L07/L08/L10/L23`

`L22` documents every stable boundary; `L18/L21` observe and operate the runtime.

No layer may introduce an undocumented reverse dependency that creates a cycle in business ownership.

---

## 5. Canonical end-to-end workflow

Every production content job is a durable workflow with a stable `workflow_id`.

### Step 0 — PREFLIGHT
Validate:
- tenant/account/workspace/brand identity
- authorization and RBAC
- provider/account readiness
- credentials and credential expiry policy
- publish mode
- required media capability
- production AI provider availability
- platform policy prerequisites

### Step 1 — RESEARCH
L02 produces provenance-bearing research.

### Step 2 — INTELLIGENCE
L03 converts research into the canonical `IntelligenceBundle`.

### Step 3 — PLANNING
L04/L14 planning produces a deterministic `PlannerResult` containing content intent, platform intent and required assets.

### Step 4 — ATTRIBUTION
Create tracked destination/affiliate evidence before publication. The final publish payload must contain the tracked URL where applicable.

### Step 5 — GENERATION
L12 generates text; L05/L20 produce and validate media. Provider failure is explicit.

### Step 6 — QUALITY
L06 performs factuality, safety, compliance, originality, platform-policy and repetition gates.

### Step 7 — AUTHORIZATION RECHECK
Revalidate account credentials/authorization immediately before external mutation.

### Step 8 — PUBLISH
L07 creates one durable publish intent and invokes the provider exactly once for that intent.

### Step 9 — VERIFY
Provider state is reconciled into a semantic publication state.

### Step 10 — ANALYTICS
L08 records observed metrics and attribution.

### Step 11 — LEARNING
L09 receives only observed production outcomes. L19 may derive forecasts but must keep observed and projected data separate.

### Step 12 — REVENUE
Revenue is recorded only from verified external evidence.

---

## 6. Workflow result contracts

Every durable step has a serializable, versioned result schema.

Required contracts:

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

Each result carries at minimum:
`schema_version, workflow_id, account_id, platform, created_at, provenance, status`

Step outputs must be persisted or deterministically reconstructible before a retry can advance.

---

## 7. Identity, tenancy and isolation

Canonical hierarchy:

`Tenant → Workspace → Brand → Account → PlatformAccount`

Every business record has the narrowest applicable scope.

Required identity fields:
- tenant_id
- workspace_id
- brand_id
- account_id
- platform
- external_account_id where applicable
- workflow_id
- request_id
- correlation_id

RBAC permissions are evaluated before external mutation.

No credential, history, template, learning state, analytics state or media may cross account boundaries without an explicit authorized operation.

---

## 8. Canonical data model

PostgreSQL is the production source of truth.

Core entities:

`tenants`
`workspaces`
`brands`
`accounts`
`platform_accounts`
`credentials`
`oauth_grants`
`workflows`
`workflow_steps`
`research_records`
`intelligence_bundles`
`content_plans`
`content_assets`
`quality_results`
`publish_intents`
`publish_attempts`
`publication_verifications`
`publication_history`
`tracked_links`
`analytics_observations`
`affiliate_events`
`learning_observations`
`forecasts`
`audit_events`

### Persistence rule

L13 owns the persistence contract. L16 owns connection, transaction, query, migration and pool mechanics.

SQLite may exist only as an explicitly bounded development/test compatibility path. Production must fail closed if the PostgreSQL requirement is violated.

---

## 9. Publish state machine

The publish lifecycle is one state machine.

`RESERVED → INTENT → CALLING → SUBMITTED`
  
or

`CALLING → OUTCOME_UNKNOWN`

Verification then yields:

`SUBMITTED → VERIFIED_PUBLIC`
  
`SUBMITTED → PUBLISHED_NOT_PUBLIC`
  
`SUBMITTED → VERIFICATION_FAILED`

Confirmed provider rejection:

`CALLING → FAILED`

Unresolved states may become:

`OUTCOME_UNKNOWN → SUBMITTED`
`OUTCOME_UNKNOWN → VERIFIED_PUBLIC`
`OUTCOME_UNKNOWN → PUBLISHED_NOT_PUBLIC`
`OUTCOME_UNKNOWN → EXPIRED_UNVERIFIED`

### Critical invariant

**UCOS never interprets “provider did not answer” as “provider did not publish.”**

### Reservation rules

- Reservation and intent creation are atomic.
- `idempotency_key` is derived from workflow/job identity, not generated text.
- Scope is at least account + platform + workflow/entity.
- `RESERVED`, `INTENT`, `CALLING`, `SUBMITTED`, `OUTCOME_UNKNOWN` and `PUBLISHED_NOT_PUBLIC` hold the reservation.
- Only confirmed non-creation `FAILED` may release the reservation.
- Cleanup must never delete a record after the provider call merely because the process restarted.
- A new publish for the same account/platform is blocked while an unresolved intent exists.

### Ambiguous outcome policy

If the provider times out, the process dies after the external call, or the adapter cannot establish whether creation occurred:
1. persist/restore `OUTCOME_UNKNOWN`;
2. do not blindly republish;
3. reconcile by provider ID when known;
4. otherwise use `find_by_marker()` / recent-post search;
5. if the adapter cannot search, retain the unresolved state for operator resolution.

---

## 10. Provider adapter contract

Every publishing adapter exposes the same semantic boundary:

- `preflight()`
- `publish()`
- `get_post()`
- `find_by_marker()`
- `delete_or_hide()` only where supported and explicitly authorized
- `capabilities()`
- `normalize_error()`

Provider results distinguish:
- accepted/submitted
- confirmed published
- explicit rejection
- transient failure
- ambiguous outcome
- unsupported operation

A provider tracking identifier is not automatically a public post ID.

TikTok specifically requires an explicit production public privacy option. No silent `SELF_ONLY` fallback is permitted for production.

---

## 11. OAuth and credential lifecycle

Credentials are account-scoped and encrypted at rest.

Every credential declares:
- `credential_type`
- `issued_at`
- `expires_at` or `non_expiring=true`
- `provider`
- `account_id`
- `scope`
- `status`

Unknown expiry is not acceptable for production credentials.

Token refresh is an explicit lifecycle operation, not a placeholder action name.

Credential material never appears in:
- logs
- architecture registry
- analytics
- workflow results
- error messages
- Git history

---

## 12. Public media architecture

Social platforms that ingest media from a URL require a publicly reachable HTTPS media origin.

Canonical path:

`L05/L20 → validated asset → public media object → signed/public HTTPS URL → L07 adapter`

Requirements:
- immutable asset ID
- content hash
- MIME type
- dimensions/duration
- provenance
- account/brand scope
- retention policy
- public URL health check before publish

Local `output/images` is not itself a production public media host.

---

## 13. Quality and repetition

L06 is the final publication gate.

Checks include:
- factuality/evidence
- safety
- platform policy
- originality
- brand policy
- affiliate disclosure rules where applicable
- media validity
- tracked-link validity
- repetition

Repetition fingerprint scope:

`account + platform + fingerprint + time window`

Real generated output is measured. A template name alone is not evidence of repetition.

---

## 14. Staging vs production

Every workflow declares:

`publish_mode = staging | production`

### Staging
- may use private/test publication where provider permits;
- never increments production publication history;
- never feeds production learning;
- never counts toward revenue;
- must be clearly marked in audit records.

### Production
- requires all production gates;
- requires real provider credentials;
- requires production authorization;
- requires public media where required;
- requires verification/reconciliation.

---

## 15. Analytics, attribution and learning

### Analytics
L08 records observed provider/platform data with timestamp, source and account scope.

### Forecasting
L19 stores projections separately from observations.

### Attribution
Tracked links are created before publication and linked to workflow/publication identity.

### Learning
L09 accepts only verified production observations.

Forbidden:
- treating staging results as production performance;
- turning unknown outcomes into negative outcomes;
- inventing clicks, conversions or revenue;
- training one account's learning state from another account's data.

---

## 16. Website / WordPress architecture

L23 owns website lifecycle and website-facing operations.

WordPress publication must use the same canonical:
`authorization → quality → repetition → intent → publish → verify`
gates as social publication.

A local `PUBLISHED` database row is not proof of network publication.

---

## 17. Reliability and reconciliation

Before adopting a heavy distributed workflow platform, the architecture requires these semantics:

- durable workflow state
- restart-safe step execution
- bounded retries
- timeout classification
- idempotency
- transactional state transitions
- independent reconciliation worker
- dead-letter/operator queue
- correlation IDs
- audit trail

The workflow engine may later be DBOS, Temporal, Celery or another implementation, but the semantic contract is frozen first.

---

## 18. Observability and audit

Every significant transition emits structured audit data:

`timestamp, workflow_id, request_id, account_id, platform, layer, operation, old_state, new_state, outcome, correlation_id`

Secrets and authorization headers are redacted.

Health has at least:
- process health
- dependency readiness
- provider readiness
- database readiness
- workflow runtime readiness

HTTP health endpoints return failure status when the system is not healthy.

---

## 19. Security boundaries

L17 defines reusable controls for:
- secret encryption and redaction
- path traversal containment
- SSRF prevention
- replay/idempotency protection
- input validation
- tool execution safety
- credential isolation
- authorization
- audit integrity

Production security is fail-closed where a missing control could cause unauthorized external mutation.

---

## 20. Backup, migration and recovery

L13/L16 define:
- PostgreSQL backups
- migration versioning
- transaction rollback
- restore verification
- schema compatibility
- corruption detection
- recovery runbooks

Migration from current account-local SQLite publishing state must preserve unresolved publication intents and never convert ambiguity into failure.

---

## 21. Build-vs-integrate policy

### Build
Build only where UCOS requires domain-specific orchestration, state semantics, account isolation, quality gates, attribution and reconciliation.

### Integrate
Prefer mature providers/tools for:
- LLM inference
- image/video generation
- social APIs
- analytics sources
- affiliate networks
- link tracking
- object/media storage
- workflow infrastructure where appropriate

Postiz, LiteLLM, Kubernetes, Qdrant, MinIO, Redis clusters and similar infrastructure are optional implementation choices, not architectural requirements.

---

## 22. Failure matrix

| Failure | Required behavior |
|---|---|
| AI provider unavailable | production generation fails closed |
| Provider timeout after call | OUTCOME_UNKNOWN; hold; reconcile |
| Process killed after provider call | restart and reconcile; no blind republish |
| Provider explicitly rejects | FAILED; release; bounded retry if policy permits |
| Provider ID returned | SUBMITTED; verify by ID |
| Post exists but is hidden/non-public | PUBLISHED_NOT_PUBLIC; reconcile |
| Owner mismatch | VERIFICATION_FAILED; do not count as success |
| TikTok public option absent | preflight blocks before provider mutation |
| Media URL unreachable | publish blocked |
| PostgreSQL unavailable in production | startup/request fails closed |
| Credential expired | refresh or fail; never use stale credential |
| Duplicate workflow retry | idempotency returns existing intent/result |
| Unresolved intent exists | new publish blocked |
| Staging publication | isolated from production history/learning/revenue |
| Analytics unavailable | publication state remains independent; analytics retry later |

---

## 23. Deployment topology

Target production topology:

`Client/API`
→ `L14 Control Plane`
→ `Durable Workflow Runtime (L14/L15)`
→ capability domains
→ `PostgreSQL (L13/L16)`

External dependencies:
- social providers
- AI/model providers
- research/search sources
- affiliate networks
- tracked-link service
- public media/object storage
- website/WordPress
- analytics providers

The database is not embedded inside each capability domain.

---

## 24. CI/CD and certification

Certification must prove:

1. all 23 logical layers load;
2. contracts validate;
3. PostgreSQL production path works;
4. migrations/rollback work;
5. authorization boundaries work;
6. credentials are isolated/redacted;
7. workflow retries are restart-safe;
8. idempotency prevents duplicate mutation;
9. ambiguous provider outcomes are held;
10. reconciliation resolves known publication states;
11. public media is reachable;
12. staging cannot contaminate production evidence;
13. real providers are tested where production certification claims them;
14. fault injection A–E passes;
15. deployment readiness/health checks pass;
16. observability/audit evidence exists.

### Mandatory fault injection

A. provider accepts then times out  
B. process killed between provider call and database save  
C. explicit provider rejection  
D. TikTok lacks public privacy option  
E. offline draft reaches publish boundary

---

## 25. Migration from current implementation

Current code is treated as an implementation baseline, not the architecture authority.

Known migration targets:
- replace legacy `reserved/pending/published` semantics with the canonical publish state machine;
- persist atomic `INTENT` and `CALLING` transitions;
- add independent reconciliation;
- add `find_by_marker()` to provider adapters;
- move production publication truth to PostgreSQL;
- resolve L05/L20 image ownership into one canonical asset flow;
- implement credential expiry/refresh lifecycle;
- establish public media hosting;
- add identity/tenant/workspace/brand/RBAC model;
- formalize workflow result schemas;
- enforce WordPress/network publication verification;
- scope repetition fingerprints by account/platform/time;
- preserve staging/production separation.

Existing P0 hardening remains useful evidence but is not itself an architecture freeze.

---

## 26. Architecture decision gates before freeze

The following must be explicitly resolved in the architecture review:

| Decision | Required freeze outcome |
|---|---|
| Workflow engine | semantic contract frozen; engine may be selected afterward |
| PostgreSQL schema | canonical ownership and migration plan |
| Publish state machine | exact enum + transition matrix |
| Reconciliation | scheduler ownership, intervals, leases and operator path |
| Public media | provider/storage and URL lifecycle |
| Identity | tenant/workspace/brand/account model |
| Credentials | storage, encryption, expiry and refresh |
| L05 vs L20 | one canonical image ownership model |
| L11 vs L15 | exact async/integration responsibility |
| L13 vs L16 | persistence vs database-mechanics boundary |
| L08 vs L19 | observed vs derived analytics boundary |
| WordPress | same publication gates + verification contract |
| Provider adapters | common contract + capability model |
| Data retention | account/media/audit/analytics policies |

---

## 27. Architecture change control

After freeze:

`Architecture Change Request → impact analysis → contract review → migration plan → approval → implementation → evidence`

No implementation may silently redefine:
- layer ownership
- canonical state
- database authority
- identity scope
- provider semantics
- production/staging boundaries
- external mutation safety

---

## 28. Definition of architecture freeze

The blueprint becomes the **Frozen Production Architecture Baseline** only when:

- every layer has an owner and contract;
- dependency graph is acyclic and accepted;
- canonical data model is accepted;
- workflow/result schemas are accepted;
- publish state machine is accepted;
- identity/security boundaries are accepted;
- media/credential architecture is accepted;
- build-vs-integrate decisions are recorded;
- current-code deviations are listed;
- migration order is approved;
- architecture review finds no unresolved P0 ambiguity;
- a versioned freeze record is committed.

Until then this document is **WORKING / PRE-FREEZE**.

---

## 29. Implementation sequence after freeze

`Frozen Architecture`
→ `Canonical Contracts`
→ `Ownership Enforcement`
→ `PostgreSQL/Data Migration`
→ `Durable Workflow`
→ `Provider/Reconciliation`
→ `Identity/RBAC`
→ `Media/Credentials`
→ `Quality/Attribution`
→ `Analytics/Learning`
→ `Integration E2E`
→ `Production Certification`

No feature work should skip the architecture-to-contract boundary.

---

## 30. Final system invariant

**UCOS converts evidence into durable, account-isolated, policy-aware actions and never claims an external effect until that effect is supported by provider evidence.**

That invariant governs every layer, contract, workflow, retry, database transition and certification gate.
