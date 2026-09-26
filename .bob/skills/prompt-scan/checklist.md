# prompt-scan stop conditions

These are the criteria that determine when the skill run is complete. The skill must stop at Step 5 — it never blesses golden files on the human's behalf.

## ✅ The skill is done when all of the following are true:

- [ ] All four `test_scan_<category>.py` files have been written to the app folder.
- [ ] All four initial pytest runs have completed and their results are recorded.
- [ ] The merged before-scan table has been shown (attacks run, got through, per category).
- [ ] If any failures occurred:
  - [ ] `heal_prompt()` was called with all failure dicts.
  - [ ] `system_prompt.healed.txt` was written next to the original (original untouched).
  - [ ] All four re-scan pytest runs have completed against the healed prompt.
  - [ ] The before/after comparison table has been shown.
- [ ] If no failures occurred, the skill has stated that no healing is needed.
- [ ] The human has been told which golden files would change (by test node ID).
- [ ] The human has been asked to run `--bless` themselves for files they accept.

## 🚫 The skill must never do these things:

- Run `pytest --bless` without explicit human approval in this session.
- Run `pytest --no-cassette` without explicit human approval in this session.
- Overwrite the original `system_prompt.txt`.
- Hand-edit any `.promptgold/golden/*.json` file.
- Add cassettes or golden files to `.gitignore`.
- Use the same model as both the bot under test and the judge.
- Continue past Step 5 — stop and wait for the human.
