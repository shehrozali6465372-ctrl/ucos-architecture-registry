# Layer 21 — Deployment

**Implementation mapping:** `layers/layer21_deployment`.

**Responsibility:** container/runtime startup, readiness, deployment configuration and recovery concerns.

**Verified architecture:** Docker startup and HTTP health boundaries are tested; production requires immutable builds, dependency readiness, secret injection, migration gates, vulnerability/SBOM controls and rollback procedures.

**Status:** VERIFIED CI/deployment boundary; production operations remain environment-specific.

**Boundary:** deployment health is distinct from application feature health.