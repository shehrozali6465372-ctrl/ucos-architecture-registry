# UCOS 1 Architecture Model

The sole authoritative architecture is UCOS v1.2:

- architecture/UCOS_ARCHITECTURE_FROZEN_PRODUCTION_BASELINE_v1.2.md
- architecture/UCOS_ARCHITECTURE_FREEZE_REVIEW_v1.2_FINAL.md

The system retains 23 bounded logical layers. This registry records layer ownership, dependencies, contracts, persistence, integrations, tests, failure boundaries and evidence-backed status. Generated inventories are derived source records, not alternative architecture specifications.

Isolation principle: failures should be contained at component boundaries, and repairs should avoid unrelated components. Architecture changes after freeze require the documented Architecture Change Request process.
