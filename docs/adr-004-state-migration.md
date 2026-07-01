# ADR 004: State Migration

## Status

Accepted for v1.

## Decision

Use explicit, idempotent state migrations recorded in the mutable state root. The runtime refuses startup when a required migration is missing or unverified.

## Rationale

Reeve-class agents accumulate durable memory, pipeline state, audit logs, and workflow state. Upgrades must not silently reinterpret old state.

## Consequences

- Every breaking state change ships with a migration.
- Migration records are part of the agent's durable state.
- Sim mode must exercise the migration planner even when no migration is required.

