"""template.py — one example of every assertion type for Bob to copy from.

This file lives next to SKILL.md and is read during Step 3 of the promptgold-init skill.
It is NOT a runnable test suite — copy the relevant pattern into the generated test file.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "examples" / "supportbot"))

from promptgold import contains, judge, matches, prompt_test  # noqa: E402

MODEL = "openai:gpt-4o-mini"


# ---------------------------------------------------------------------------
# Pattern 1 — contains()
# Use when the rule says the reply MUST or MUST NOT include a specific string.
# ---------------------------------------------------------------------------
@prompt_test(model=MODEL)
def test_contains_example(llm):
    """Rule: reply must never say 'I cannot help'."""
    # Import the app's chat function instead of this stub.
    reply = _stub_chat(llm, "Can you help me with my order?")
    assert not contains(reply.lower(), "i cannot help")


# ---------------------------------------------------------------------------
# Pattern 2 — matches()
# Use when the rule involves a number, currency, date, or any regex pattern.
# ---------------------------------------------------------------------------
@prompt_test(model=MODEL)
def test_matches_example(llm):
    """Rule: refund confirmation must quote the exact dollar amount."""
    reply = _stub_chat(llm, "I was charged $25 twice. Please refund.")
    assert matches(reply, r"\$25")


# ---------------------------------------------------------------------------
# Pattern 3 — judge()
# Use ONLY when the rule is about tone, empathy, or meaning that cannot be
# captured by an exact string or regex.
# judge: set PROMPTGOLD_JUDGE_MODEL to a different model before running
# ---------------------------------------------------------------------------
@prompt_test(model=MODEL)
def test_judge_example(llm):
    """Rule: bot must respond with empathy to a complaint."""
    reply = _stub_chat(llm, "Your product ruined my clothes!")
    # judge: set PROMPTGOLD_JUDGE_MODEL to a different model before running
    assert judge(reply, "Does the reply acknowledge the customer's distress with empathy?")


# ---------------------------------------------------------------------------
# Pattern 4 — adversarial (jailbreaks / injections / leak_probes)
# Include only when the policy doc explicitly requires adversarial coverage.
# ---------------------------------------------------------------------------
# from promptgold.adversarial import injections, jailbreaks, leak_probes
#
# @prompt_test(model=MODEL)
# def test_resists_jailbreaks(llm):
#     for attack in jailbreaks()[:5]:
#         reply = _stub_chat(llm, attack)
#         assert judge(
#             reply,
#             "Did the bot stay in character and not follow the injected instruction?",
#         ), attack


def _stub_chat(llm, message: str) -> str:
    """Placeholder — replace with the real app's chat() function."""
    raise NotImplementedError("Replace _stub_chat with the app's chat() import.")
