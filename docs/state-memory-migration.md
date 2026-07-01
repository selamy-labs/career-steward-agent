# State And Memory Layout

## Writable State

The mutable root is `/opt/data/**`.

Recommended layout:

```text
/opt/data/wiki/                  private wiki and durable notes
/opt/data/work/                  generated artifacts and working files
/opt/data/cron/jobs.json         reconciled schedules
/opt/data/audit/events.jsonl     append-only audit stream
/opt/data/state/                 workflow state
/opt/data/migrations/            applied migration records
```

## Immutable Runtime

Repo-owned runtime files are mounted read-only:

```text
/etc/hermes/**
/opt/scripts/**
/usr/local/bin/**
```

Runtime changes happen through source changes and artifact publication, not live pod mutation.

## Migration Story

Each agent version declares:

- source version
- target version
- affected state paths
- forward migration command
- rollback/read compatibility note
- verification check

Migrations are idempotent and recorded under `/opt/data/migrations/applied.json`. A migration that cannot prove completion blocks startup.

## Upgrade Rule

The runtime may read old state for at least two minor versions. Removing a state field requires a schema major bump or an explicit migration that writes the new layout and records verification evidence.

