"""
PreToolUse hook — blocks execute_command calls that contain --bless or --no-cassette.

Exit codes:
  0  allow the tool call to proceed
  2  block the tool call (Bob treats exit 2 as a hard block)

Any other non-zero exit is treated by Bob as a benign hook failure and ignored,
so parse errors fall through as exit 0 with a stderr warning.
"""

import json
import sys


def main() -> None:
    raw = sys.stdin.read()

    if not raw.strip():
        print("block_bless: empty stdin, skipping check", file=sys.stderr)
        sys.exit(0)

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"block_bless: invalid JSON on stdin ({exc}), skipping check", file=sys.stderr)
        sys.exit(0)

    # Real Bob payload uses "tool_input"; fall back to legacy "input" for safety.
    tool_input = payload.get("tool_input") or payload.get("input") or {}
    command = tool_input.get("command", "")

    for flag in ("--bless", "--no-cassette"):
        if flag in command:
            print(
                f"block_bless: '{flag}' is a human-approval-only flag. "
                "Run this command yourself in your own terminal.",
                file=sys.stderr,
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
