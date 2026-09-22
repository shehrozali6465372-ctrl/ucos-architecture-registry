# Architecture Contracts

## Contract classes
- Layer input/output contracts
- Shared model schemas
- Provider adapter contracts
- Persistence/transaction contracts
- Account-isolation contracts
- Publishing mutation/idempotency contracts
- Analytics observation contracts
- Learning evidence contracts
- Security/trust-boundary contracts
- Health/readiness contracts

## Hard rules
- Contract failures are explicit and fail closed where safety or external mutation is involved.
- Provider adapters validate credentials/configuration and response shape.
- External mutation results distinguish confirmed, failed and uncertain states.
- Learning cannot treat unknown outcomes as observed outcomes.
- Quality/security/compliance hard failures cannot be overridden by a weighted score.
- SQLite may support development tests; PostgreSQL is the production persistence source of truth.
