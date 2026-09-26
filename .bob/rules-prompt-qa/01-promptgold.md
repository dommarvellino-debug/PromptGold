# Promptgold Rules for Prompt QA Mode

## Tool Execution
- Always run tools as `./.venv/bin/pytest` and `./.venv/bin/ruff`.

## Baseline Management
- Never run pytest with `--bless` or `--no-cassette`.
- When a new baseline is needed, stop and ask the human.
- Never edit `.promptgold/golden/*.json`.

## Assertion Preferences
- Prefer `contains()` and `matches()` over `judge()`.

## Judge Model
- The judge model must never be the same model as the model under test.
- Check `PROMPTGOLD_JUDGE_MODEL` before trusting any verdict.

## Task Summary
End every task with a summary:
- tests added
- attacks run
- failures found
- fixes proposed
- cost from the run summary