# PromptGold repo rules

These rules apply in every mode. They are sourced from CONTRIBUTING.md — do not invent additions.

## Running commands

Always use the venv explicitly. Never invoke a global `pytest` or `ruff`.

**Mac / Linux**
```
./.venv/bin/pytest
./.venv/bin/ruff check src tests
```

**Windows**
```
.venv\Scripts\python -m pytest
.venv\Scripts\python -m ruff check src tests
```

If tests fail in a way that makes no sense, suggest rebuilding the venv first.

## Human-approval-only operations

Never run either of the following flags unless the human has explicitly said yes in this session:

- `--bless` — records (overwrites) golden verdicts
- `--no-cassette` — forces live API calls that cost money

## Golden files and cassettes

- Never edit `.promptgold/golden/*.json` by hand. They are generated files.
- Never add cassettes or golden files to `.gitignore`. Both are committed on purpose.

## Commits and pushes

Never run `git commit` or `git push` without the human explicitly saying yes in this session.

## Judge independence

`judge()` grades with the model set by `PROMPTGOLD_JUDGE_MODEL` (default `openai:gpt-4o-mini`).

The judge must never be the same model as the one under test. A model grading its own output is not a weaker result — it is an invalid one. Verify this before trusting any verdict.

Known past bug: `judge(model=llm.model)` with a wrapped model fell through to the default judge and hit the real API. Watch for that class of silent fallthrough.

## Assertion preference

Prefer `contains()` and `matches()` over `judge()` when either would work. Reserve `judge()` for cases where deterministic assertions are insufficient.

## Design constraints (deliberate rejections)

These are not gaps — they are explicit decisions. If a change would add any of the following, raise it in an issue before building:

- No dashboard or web UI
- No hosted tier, no accounts, no telemetry
- No 50-metric zoo — three assertions cover it
- No YAML-first config; tests are Python

## Testing conventions

- Use pytest, not unittest.
- A new feature requires new tests in the same commit.
- A feature is done when the suite is green and lint is clean, not before.
