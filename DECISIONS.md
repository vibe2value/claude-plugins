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

## 2026-09-21: decision-log 1.2.0 makes logging dependable, not hopeful
**Chose:** four changes together: a "log it now" reminder, a Stop hook that holds a turn once when files changed but the log did not, the skill kept as /decision-log:log for asking directly, and a one line count so a quiet log looks different from a broken one
**Over:** the 1.1.0 reminder alone, which in its first real session logged late, in batches, and only on the user's own messages
**Why:** "the main thing is that it works so that the log can later be analysed - an empty log that the user thought would be populated is worse than useless"
**Source:** stated
