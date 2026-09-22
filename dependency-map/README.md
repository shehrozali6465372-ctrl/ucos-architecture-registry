# Dependency Map

## Principle
Dependencies are directional and contract-based. A layer must not reach into another layer's private implementation when an explicit interface/event/adapter exists.

## Primary dependency domains
- L01 Core provides configuration, state, memory, logging and foundational scheduling/services.
- L11/L12 provide external provider and model boundaries.
- L13/L16 provide persistence/database foundations.
- L14/L15 provide enterprise request and asynchronous execution boundaries.
- L17 protects all trust boundaries.
- L18 observes runtime/dependency health.
- L06 gates content before publication.
- L07 owns external publishing mutations.
- L08/L19 consume observed analytics and produce analytics intelligence.
- L09 consumes observed outcomes for learning.
- L10 owns affiliate/commerce decisioning.
- L20 owns image-pipeline provider/asset validation.
- L23 owns website-level orchestration and website/traffic operations.

## Change rule
Any implementation change must identify direct dependencies, downstream consumers and the contract/test surface that proves compatibility. Do not broaden a change merely because a dependency exists; modify only the affected boundary and required regression tests.

## Shared infrastructure
The main repository also contains shared DI, event bus, interfaces, provider abstractions and shared models. These are cross-cutting contracts and must be treated as dependency surfaces rather than layer-owned business logic.
