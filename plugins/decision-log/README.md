# decision-log

Keep a running log of the decisions you make while building with AI, and the reason for each one.

## Why

The code is cheap now. The reasoning behind it is not, and it is the part that evaporates. A week later the code is still there and nobody remembers why it is like that, including you.

This runs underneath the work, not before it. There is no setup and nothing to remember, which is the whole point: the moment it needs a step, it is dead.

## Install

```
/plugin marketplace add vibe2value/claude-plugins
/plugin install decision-log@vibe2value
```

## Use

Nothing. That is the feature.

Once installed, decisions get appended to `DECISIONS.md` as they happen.

**Why there are hooks.** A skill only runs when the AI notices it should. In its first real session, with no hook, a whole day of decisions went unlogged until the person asked where the log was. With only a reminder, entries arrived late, in batches, and never for decisions the AI made itself mid-task. So the plugin carries two small hooks:

- **Each message you send** adds a one line reminder to the AI's context: if this settles a decision, log it now, before anything else.
- **Each turn as it ends** gets a check. If the turn changed files and wrote nothing to `DECISIONS.md`, the AI is asked once whether a decision was settled. If one was, it logs it; if not, it stops. It never asks twice in a row.

Neither blocks you, asks you anything or needs setting up. When something is logged you see one line, `decision-log: 1 logged this turn, 4 this session.`, so a log that is quiet because nothing was decided looks different from one that is broken. The end of turn check needs `python3`; without it the check is skipped and the reminder still works.

**You can also ask for it.** `/decision-log:log` means "log this now", with or without words after it. It is the backup, not the main path.

**There can be more than one log.** A `DECISIONS.md` can appear in any git repository you touch that is reachable from the directory you started Claude in, and nowhere else. Work in three repos in one session and you get three logs, one in each. That is the whole blast radius.

It goes in the **nearest enclosing git repository** of whatever you are changing, because the log has to travel with the code: the repo is what gets cloned, reviewed and read by somebody else later. If the work is in a folder that is not a repo at all, it falls back to the directory you started in.

When the file is first created you are told what has appeared, what will end up in it, and why it is scoped that way rather than to the folder you started Claude in. After that it says one line per session, the first time it writes, so you can tell a quiet session apart from one where nothing fired. It never asks you anything.

```markdown
## 2026-09-21: Deck keys use the Ghost member id
**Chose:** key every deck on the Ghost `member.id`
**Over:** a slug built from the client's name
**Why:** names change and ids do not, so a rename would silently orphan every deck
**Source:** stated
```

Three rules it keeps:

- **It logs forks, not actions.** A decision is a point where the project could have gone another way. A log of everything you did is a transcript, and you already have one.
- **It never invents a reason.** Reasons you actually gave are marked `stated`. Reasons the AI worked out for itself are marked `inferred`, and are never dressed up as yours.
- **It stays out of the way.** No announcements, no permission, no interruptions, and no nagging about projects you never finished.

Plain markdown on purpose: it diffs in git, greps from the terminal and reads without a tool.

## What it is for

Mostly, answering "why is it like this?" months later.

But not everything you vibe makes it to production, and that is the point. The log never asks you to finish anything. Most of what gets built with AI is an experiment, and experiments are supposed to die.

If something does start heading towards real people, the log becomes evidence. The [shape+build+launch framework](../shape-build-launch) can then be run backwards over it. Which decisions still hold up, which drifted, which nobody can explain, before your name goes on it:

```
/plugin install shape-build-launch@vibe2value
/shape-build-launch:review
```

That is optional, and it always will be. This plugin does not require the framework, and you do not need to have heard of it.
