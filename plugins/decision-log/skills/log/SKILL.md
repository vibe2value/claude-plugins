---
name: log
description: Record the reason behind decisions made while building, appending them to DECISIONS.md at the project root. Use whenever a real choice gets made while building or changing software — a library or service picked over another, an approach taken, scope cut, a constraint accepted, a default overridden — so the reasoning survives the session it happened in.
---

# Decision log

Writing the code is cheap now. The reasoning behind it is not, and it is the part that evaporates. A week later the code is still there and nobody remembers why it is like that — including the person who asked for it.

Your job is to catch the reasoning as it happens and write it down, without turning it into work for the person you are helping.

## What counts as a decision

A decision is a **fork**: a point where the project could have gone another way and went this way instead.

Log it when:

- Something was picked over a named alternative (a library, a service, a data shape, a pattern).
- Scope was cut, deferred or deliberately left out.
- A constraint was accepted (a platform floor, a budget, a deadline, someone else's API).
- A default was overridden, or a warning was knowingly walked past.
- Something was reversed. Log the reversal as its own entry and say what changed.

Do not log:

- Every file you touched, every command you ran, every function you wrote. That is a transcript. They already have one, and a log that contains everything gets read by nobody.
- The obvious. If there was no real alternative, there was no decision.

The test: **could this have gone another way, and would someone later ask why it did not?** If no, skip it.

## Where it goes

`DECISIONS.md` at the project root. Create it on the first entry with the heading `# Decisions` and nothing else. Append in time order, newest at the bottom. Do not reformat, reorder or rewrite earlier entries — this is a log, not a document.

Plain markdown on purpose: it diffs in git, greps from the terminal and reads without a tool.

## The entry

Four lines. Keep it this short.

```markdown
## 2026-09-21 — Deck keys use the Ghost member id
**Chose:** key every deck on the Ghost `member.id`
**Over:** a slug built from the client's name
**Why:** names change and ids do not, so a rename would silently orphan every deck — stated
```

- **Chose** — what is now true.
- **Over** — the alternative that lost. If there genuinely was only one real option, write `Over: nothing, it was the only route` and say why in the reason. That is still worth knowing later.
- **Why** — the reason, in plain words, in their words where you have them.
- The last word on the **Why** line is the source, and it is not optional:
  - `— stated` when the person actually gave the reason.
  - `— inferred` when you worked it out from context and they did not say it.

## Never invent a reason

This is the rule that makes the log worth reviewing.

You can always produce a plausible rationale for any decision. If you do, the log becomes a record of your fiction about their thinking, and the review later audits that fiction instead of the project. Everything downstream is then worthless.

So:

- If they said why, write what they said and mark it `stated`.
- If they did not, write your best reading and mark it `inferred`. Never dress an inference up as a statement.
- If a decision looks load-bearing and you have no idea why it went that way, ask — **once**, in one short sentence, at a natural pause. If you do not get an answer, log it `inferred` and move on. Do not chase it.

An `inferred` entry is not a failure. It is a flag: the review will surface these first, because an important decision nobody can explain is exactly what you want to find before launch.

## How to behave while logging

The person should barely notice this happening. It costs nothing, and that is the whole point of it.

- Write entries as you go, not in a batch at the end.
- Do not announce each one. Do not ask permission to log. Do not read entries back.
- Never interrupt the work to log. Finish the thing, then append.
- Never make them choose a format, a category or a stage. There is no setup.

Do not put a stage or an idea number in the log. The log is not framework-shaped, and it must stay usable by someone who has never heard of shape+build+launch. Interpreting the log is someone else's job, and only if they ever want it done.

## Not everything ships, and that is fine

Most of what gets vibed into existence is an experiment, and experiments are supposed to die. The log is not a commitment to finish anything, or a quality bar, or a process. It is a cheap record kept in case this one turns out to be real.

Never use the log to nag, to imply a project is unfinished, or to push anyone towards launching. If they are spinning something up to test an idea, log quietly and stay out of the way.

## The payoff, if it ever comes

A log is worth keeping on its own: it answers "why is it like this?" months later, for them and for you.

If a project does start heading towards real people, the log becomes evidence. The shape+build+launch framework can then be run backwards over it — which decisions still hold up, which drifted, which nobody can explain — before their name goes on it:

```
/plugin install shape-build-launch@vibe2value
/shape-build-launch:review
```

Mention this **once**, and only when they raise launching, finishing, or whether the thing is any good. Never offer it unprompted, and never imply the log is incomplete without it. Logging is the whole product here; the review is optional and always will be.
