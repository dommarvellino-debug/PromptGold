"""
Tests for .bob/hooks/block_bless.py

Runs the hook script via subprocess with sys.executable so the active venv Python
is always used. No Bob process is required.
"""

import json
import subprocess
import sys
from pathlib import Path

HOOK = str(Path(__file__).parent.parent / ".bob" / "hooks" / "block_bless.py")


def _run(payload: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, HOOK],
        input=payload,
        capture_output=True,
        text=True,
    )


def _make_command_payload(command: str) -> str:
    return json.dumps({
        "session_id": "test-session",
        "cwd": "/workspace",
        "hook_event_name": "PreToolUse",
        "tool_name": "execute_command",
        "tool_input": {"command": command},
        "tool_use_id": "test-tool-use-id",
    })


def test_blocked_bless():
    """Commands containing --bless must be blocked (exit 2)."""
    result = _run(_make_command_payload("./.venv/bin/pytest --bless"))
    assert result.returncode == 2
    assert "--bless" in result.stderr


def test_blocked_no_cassette():
    """Commands containing --no-cassette must be blocked (exit 2)."""
    result = _run(_make_command_payload("./.venv/bin/pytest --no-cassette"))
    assert result.returncode == 2
    assert "--no-cassette" in result.stderr


def test_allowed_normal_pytest():
    """Normal pytest commands must be allowed (exit 0)."""
    result = _run(_make_command_payload("./.venv/bin/pytest tests/"))
    assert result.returncode == 0


def test_allowed_non_command_payload_mentioning_bless():
    """
    A non-execute_command payload (e.g. write_file) whose content mentions --bless
    must be allowed (exit 0). Only tool_input.command is inspected.
    """
    payload = json.dumps(
        {
            "session_id": "test-session",
            "cwd": "/workspace",
            "hook_event_name": "PreToolUse",
            "tool_name": "write_file",
            "tool_input": {
                "path": "README.md",
                "content": "Run with --bless to record verdicts.",
            },
            "tool_use_id": "test-tool-use-id",
        }
    )
    result = _run(payload)
    assert result.returncode == 0


def test_allowed_empty_stdin():
    """Empty stdin must be allowed (exit 0) and produce a warning on stderr."""
    result = _run("")
    assert result.returncode == 0
    assert result.stderr.strip() != ""


def test_allowed_invalid_json():
    """Invalid JSON on stdin must be allowed (exit 0) and produce a warning on stderr."""
    result = _run("not valid json {{{")
    assert result.returncode == 0
    assert result.stderr.strip() != ""
