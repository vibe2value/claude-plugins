#!/usr/bin/env python3
"""decision-log's end of turn safety net.

The reminder on each message is not enough on its own. In its first real session the log was
written late, in batches, and never for decisions the AI made itself mid-task. So when a turn is
about to end, this looks at what the turn did:

  - files were changed and DECISIONS.md was not   -> hold the turn ONCE and ask
  - DECISIONS.md was written                      -> one line to the person with the count
  - anything else                                 -> say nothing

The hold asks a question, it does not order a log: most turns that change files settle no
decision, and then the AI stops. stop_hook_active stops it asking twice in a row.

It never fails loudly. A transcript it cannot read, or no python, and the turn ends as normal:
a broken safety net must not break the session.
"""
import json
import os
import re
import sys

LOG = "DECISIONS.md"
WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
# A Bash command that plainly changes files. Deliberately narrow: a read-only command must not
# trigger a hold, and a missed write only means the reminder carries it instead.
BASH_WRITES = re.compile(r"(>>?|\bsed\s+-i\b|\btee\b|\bgit\s+commit\b|\bmv\s|\bcp\s|\brm\s|\bpatch\b)")

HOLD = (
    "decision-log: this turn changed files and wrote nothing to DECISIONS.md. "
    "Did it settle a real decision (one option chosen over another, scope cut, a constraint "
    "accepted, a default overridden, a reversal), including one you made yourself while working? "
    "If so, load the decision-log:log skill and append it now. If not, stop without comment."
)


def is_prompt(entry):
    """A message the person typed, as opposed to a tool result or an injected reminder."""
    if entry.get("type") != "user" or entry.get("isMeta"):
        return False
    content = (entry.get("message") or {}).get("content")
    if isinstance(content, str):
        return True
    return isinstance(content, list) and any(b.get("type") == "text" for b in content)


def tool_uses(entry):
    content = (entry.get("message") or {}).get("content")
    if entry.get("type") != "assistant" or not isinstance(content, list):
        return []
    return [b for b in content if b.get("type") == "tool_use"]


def writes(cmd):
    """True when a shell command plainly writes a file. Quoted text is dropped first, since code
    inside quotes is full of => and ->, then redirects to /dev/null and fd juggling like 2>&1."""
    bare = re.sub(r"'[^']*'|\"(?:\\.|[^\"\\])*\"", " ", cmd)
    bare = re.sub(r"\d*>&\d+|\d*>\s*/dev/null|[=-]>", " ", bare)
    return bool(BASH_WRITES.search(bare))


def touches_log(use):
    inp = use.get("input") or {}
    if use.get("name") in WRITE_TOOLS:
        return os.path.basename(inp.get("file_path", "") or inp.get("notebook_path", "")) == LOG
    if use.get("name") == "Bash":
        cmd = inp.get("command", "")
        return LOG in cmd and writes(cmd)
    return False


def changes_files(use):
    inp = use.get("input") or {}
    if use.get("name") in WRITE_TOOLS:
        return True
    return use.get("name") == "Bash" and writes(inp.get("command", ""))


def entries_in(use):
    """How many entries one write added: each entry has exactly one **Chose:** line."""
    inp = use.get("input") or {}
    text = inp.get("content") or inp.get("new_string") or inp.get("command") or ""
    return text.count("**Chose:**")


def main():
    try:
        hook = json.load(sys.stdin)
        with open(hook["transcript_path"], encoding="utf-8") as f:
            entries = [json.loads(line) for line in f if line.strip()]
    except Exception:
        return

    last_prompt = max((i for i, e in enumerate(entries) if is_prompt(e)), default=-1)
    session = [u for e in entries for u in tool_uses(e)]
    turn = [u for e in entries[last_prompt + 1:] for u in tool_uses(e)]

    logged_now = [u for u in turn if touches_log(u)]
    if logged_now:
        total = sum(entries_in(u) for u in session if touches_log(u))
        added = sum(entries_in(u) for u in logged_now)
        print(json.dumps({"systemMessage":
            f"decision-log: {added} logged this turn, {total} this session."}))
        return

    # stop_hook_active: this turn already came back once from a hold. Never ask twice.
    if hook.get("stop_hook_active"):
        return
    if any(changes_files(u) and not touches_log(u) for u in turn):
        print(json.dumps({"decision": "block", "reason": HOLD}))


if __name__ == "__main__":
    main()
