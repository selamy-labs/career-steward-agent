# Instantiate For A New Person In Sim Mode

This walkthrough touches no real account.

## Steps

1. Clone or copy the repo.
2. Edit `agent.manifest.yaml` identity fields for the new operator.
3. Leave `contracts/required-secrets.yaml` as references only; do not add values.
4. Run:

```bash
make verify
```

5. Inspect `generated/sim-run.json`.

## Expected Loop

The sim run proves:

- intake from fake data
- classification
- draft generation
- approval gate blocks external send
- private pipeline row update
- privacy validation
- no real account touched

The `touchedRealAccounts` field must be `false`, and `externalSideEffects` must be empty.

