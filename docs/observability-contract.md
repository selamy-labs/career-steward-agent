# Observability Contract

## Logs

Logs are structured JSON. Each workflow run emits:

- `workflow.run.started`
- `workflow.step.completed`
- `approval.requested`
- `artifact.generated`
- `state.updated`
- `workflow.run.completed`

Errors include machine-readable `error.kind`, `error.message`, and `retryable`.

## OpenTelemetry

Required spans:

- `workflow.run`
- `connector.call`
- `approval.requested`
- `external.side_effect`
- `artifact.generated`
- `state.update`
- `privacy.validation`

Every span includes `agent.name`, `workflow.name`, `run.id`, and `sim_mode`.

## Metrics

Required metrics:

- workflow run count
- workflow error count
- connector call count and latency
- approval requested count
- approval denied count
- external side-effect count
- privacy validation failure count
- generated artifact count

## Immutable Audit Trail

Every outbound or state-mutating action records an append-only audit event:

- timestamp
- actor
- workflow
- action
- source evidence reference
- approval reference when applicable
- privacy validation result
- before/after state hash for state mutations

In sim mode the audit trail is written to the sim output JSON. In live mode the downstream deployment must provide an append-only sink.

