# decision-log

Keep a running log of the decisions you make while building with AI, and the reason for each one.

## Why

The code is cheap now. The reasoning behind it is not, and it is the part that evaporates. A week later the code is still there and nobody remembers why it is like that — including you.

This runs underneath the work, not before it. There is no setup and nothing to remember, which is the whole point: the moment it needs a step, it is dead.

## Install

```
/plugin marketplace add vibe2value/claude-plugins
/plugin install decision-log@vibe2value
```

## Use

Nothing. That is the feature.

Once installed, decisions get appended to `DECISIONS.md` as they happen:

The file goes in the **nearest enclosing git repository** of whatever you are changing, so the log travels with the code rather than sitting in a folder above it. Work across two repos in one session and each gets its own. You are told once, when the file is first created, where it is and what it covers. It never asks you anything.

```markdown
## 2026-09-21 — Deck keys use the Ghost member id
**Chose:** key every deck on the Ghost `member.id`
**Over:** a slug built from the client's name
**Why:** names change and ids do not, so a rename would silently orphan every deck — stated
```

Three rules it keeps:

- **It logs forks, not actions.** A decision is a point where the project could have gone another way. A log of everything you did is a transcript, and you already have one.
- **It never invents a reason.** Reasons you actually gave are marked `stated`. Reasons the AI worked out for itself are marked `inferred`, and are never dressed up as yours.
- **It stays out of the way.** No announcements, no permission, no interruptions, and no nagging about projects you never finished.

Plain markdown on purpose: it diffs in git, greps from the terminal and reads without a tool.

## What it is for

Mostly, answering "why is it like this?" months later.

But not everything you vibe makes it to production, and that is the point. The log never asks you to finish anything. Most of what gets built with AI is an experiment, and experiments are supposed to die.

If something does start heading towards real people, the log becomes evidence. The [shape+build+launch framework](../shape-build-launch) can then be run backwards over it — which decisions still hold up, which drifted, which nobody can explain — before your name goes on it:

```
/plugin install shape-build-launch@vibe2value
/shape-build-launch:review
```

That is optional, and it always will be. This plugin does not require the framework, and you do not need to have heard of it.
