# Layer 18 — Monitoring

**Implementation mapping:** `layers/layer18_monitoring` in the UCOS implementation repository.

**Responsibility:** runtime health, dependency health, telemetry, error visibility and recovery state.

**Verified architecture:** monitoring must identify account/platform/content/layer/error context and external-mutation certainty where available; health must include dependencies rather than process liveness only.

**Status:** VERIFIED architecture; LIVE operational verification requires deployed runtime evidence.

**Boundary:** monitoring observes; it must not silently mutate business state.