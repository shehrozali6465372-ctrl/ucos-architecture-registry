# UCOS Data Flow

## Target business lineage
`source → niche → keyword → content → asset → platform → account → publish → click → conversion → revenue`

## Required provenance
Every production intelligence record should retain source identity/provenance, timestamp, status and confidence where applicable. Observed external outcomes must remain distinguishable from projected or unknown values.

## Flow boundaries
1. Research ingests/observes external or explicitly non-production inputs.
2. Intelligence transforms evidence into typed opportunities/bundles.
3. Writing converts intelligence into content variants.
4. Image/asset pipelines create or reference real assets with provenance.
5. Quality gates validate the publishable artifact.
6. Publishing performs controlled external mutations with account identity and idempotency/reconciliation.
7. Analytics normalizes observed platform outcomes.
8. Analytics Engine derives projections/recommendations without relabeling projections as observations.
9. Learning consumes only observed outcomes and records evidence-backed actions.

## No-fake rule
Missing upstream evidence stops or marks the downstream result as unavailable; it must not be replaced with invented products, URLs, statistics, clicks, conversions or revenue.
