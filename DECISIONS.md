# Decisions

Why things in claude-plugins are the way they are, recorded as the work happened.

## 2026-09-21: decision-log carries a reminder hook
**Chose:** a UserPromptSubmit hook in the plugin that adds a one line reminder to each message you send
**Over:** a memory note only, or a Stop hook that holds every response until the log is checked
**Why:** you asked for the plugin itself to do it after a whole session went unlogged; a message is when decisions arrive, and a reminder there costs one line where a Stop hook would cost an extra pass on every reply
**Source:** inferred

## 2026-09-21: The log uses no em dash and speaks to you
**Chose:** the source on its own **Source:** line, entries in the second person, the project's CLAUDE.md rules applied to the log
**Over:** the 1.0.3 format, with the source after an em dash at the end of the Why line
**Why:** your writing rules ban the em dash, and a log that breaks the project's own style is a log nobody trusts
**Source:** stated
