# Data Sources

This file documents the origin of every corpus or dataset used by promptgold,
including the adversarial attack strings in
[`src/promptgold/adversarial.py`](src/promptgold/adversarial.py) and the
fictional example data bundled in `examples/`.

A human **must** verify the licence / terms column before any public release or
redistribution. Licences were reviewed by the team on 2026-09-27.

---

## Adversarial attack strings (`src/promptgold/adversarial.py`)
All attack strings were written by the team. The sources above describe the attack techniques; no text was copied from them.

The attack strings are short, manually adapted probes. They are not verbatim
copies of any single dataset; they are inspired by the technique families listed
below. The "source name" column names the public resource that documents or
popularises each technique family.

| Category | Source name | URL | Licence / terms |
|---|---|---|---|
| **Jailbreak** – DAN / "Do Anything Now" persona swap | OWASP LLM Top 10 – LLM01: Prompt Injection | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Jailbreak** – roleplay / persona override ("you have no guidelines", grandma trick) | OWASP LLM Top 10 – LLM01: Prompt Injection | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Jailbreak** – SYSTEM OVERRIDE / deactivation framing | OWASP LLM Top 10 – LLM01: Prompt Injection | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Jailbreak** – dual-answer / "two personalities" pattern | Gandalf-style Prompt Injection Probes (Lakera AI) | <https://gandalf.lakera.ai/> |  Not a dataset — technique inspiration only, no text copied |
| **Jailbreak** – language-switching / translation smuggling | Perez & Ribeiro, "Ignore Previous Prompt" (arXiv 2022) | <https://arxiv.org/abs/2211.09527> | CC BY-NC-SA 4.0 — technique reference only, no text copied |
| **Jailbreak** – "simulation environment / policies don't apply" | Gandalf-style Prompt Injection Probes (Lakera AI) | <https://gandalf.lakera.ai/> | Not a dataset — technique inspiration only, no text copied |
| **Prompt injection** – instruction smuggling via user-supplied data (order numbers, feedback fields) | OWASP LLM Top 10 – LLM01: Prompt Injection | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Prompt injection** – HTML / XML tag confusion (`</system>` injection) | OWASP LLM Top 10 – LLM01: Prompt Injection | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Prompt injection** – base64-encoded hidden instruction | Perez & Ribeiro, "Ignore Previous Prompt" (arXiv 2022) | <https://arxiv.org/abs/2211.09527> | CC BY-NC-SA 4.0 — technique reference only, no text copied |
| **Prompt injection** – email / log-entry action execution | OWASP LLM Top 10 – LLM02: Insecure Output Handling | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Leak probe** – direct system-prompt extraction ("quote word for word") | Gandalf-style Prompt Injection Probes (Lakera AI) | <https://gandalf.lakera.ai/> | Not a dataset — technique inspiration only, no text copied |
| **Leak probe** – "repeat everything above this message" | Perez & Ribeiro, "Ignore Previous Prompt" (arXiv 2022) | <https://arxiv.org/abs/2211.09527> | CC BY-NC-SA 4.0 — technique reference only, no text copied |
| **Leak probe** – developer / security-audit authority claim | OWASP LLM Top 10 – LLM06: Sensitive Information Disclosure | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Leak probe** – complete-the-sentence prompt leakage | Gandalf-style Prompt Injection Probes (Lakera AI) | <https://gandalf.lakera.ai/> | Not a dataset — technique inspiration only, no text copied |
| **Leak probe** – cross-user data / PII exfiltration probe | OWASP LLM Top 10 – LLM06: Sensitive Information Disclosure | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |
| **Topic escape** – off-topic requests (poems, medical advice, homework, politics, stock tips) | OWASP LLM Top 10 – LLM01: Prompt Injection | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | CC BY-SA 4.0 (commercial use allowed with attribution) |

---

## Fictional example data (`examples/`)

These assets are wholly invented by the project team and carry no third-party
rights.

| Asset | Description | Source |
|---|---|---|
| `examples/supportbot/system_prompt.txt` | System prompt for "Sabun", fictional LuxMart soap-shop support bot | Original, created by the team |
| `examples/supportbot/` (test conversations) | Simulated customer dialogues used as test fixtures | Original, created by the team |
| `examples/velvet/system_prompt.txt` | System prompt for the Velvet bot example | Original, created by the team |
| `examples/velvet/` (test conversations) | Simulated dialogues used as test fixtures | Original, created by the team |


---

## How to update this file

1. When a new corpus, dataset, or set of example strings is added, add a row
   here **in the same PR**.
2. Replace `TO VERIFY` with the actual SPDX licence identifier or a short
   description of the terms (e.g. `CC BY 4.0`, `MIT`, `Apache 2.0`,
   `Research / non-commercial only`).
3. If a resource has no explicit licence, note `No licence stated — contact
   owner` and do not distribute that material until resolved.
