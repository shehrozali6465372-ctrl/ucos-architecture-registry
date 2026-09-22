# Architecture Change Log

## Baseline
- Registry established as a separate control-plane/documentation repository.
- Implementation source of truth: UCOS main repository.
- Certified implementation baseline: `0f0c92bdf2bc815df3ec1f9bdf033d0613e44a20`.
- Certification evidence: CI #501, 10,162 passed, 87 warnings, 0 failures, 0 errors; 23/23 boot.

## Change protocol
For every architecture-affecting implementation change record:
1. implementation commit
2. affected layer(s)
3. contract/dependency/data-flow impact
4. tests/CI evidence
5. operational status change
6. rollback/recovery consideration

Never record a capability as complete solely because a file exists.
