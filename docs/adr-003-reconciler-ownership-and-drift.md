# ADR 003: Reconciler Ownership And Drift

## Status

Accepted for v1.

## Decision

The source repo owns declarations and generated artifacts. The downstream infrastructure repo owns live deployment and live drift.

The reconciler generates artifacts and validates invariants, but it does not apply to live clusters.

## Drift Model

- Declaration drift: source repo failure.
- Generated artifact drift: reconciler failure.
- Live cluster drift: downstream infra failure.

## Consequences

The v1 repo can prove correctness without cluster access. Downstream operators can choose ArgoCD, Flux, or another reconciler without changing the source specification.

