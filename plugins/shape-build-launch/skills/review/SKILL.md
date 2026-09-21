---
name: review
description: Run the shape+build+launch framework backwards over decisions already made, using the project's DECISIONS.md as the source. Use when someone is deciding whether a build is ready to go in front of people, whether it is worth finishing, or whether they would put their name on it.
---

# Review decisions already made

The `guide` skill runs the framework forwards: make the next decision sharp before any code is written. This skill runs it backwards, over decisions already taken.

That is the common case. Almost nobody stops to shape before they build — they build, and only later start wondering whether the thing is real. At that point the framework is still the right tool, but the decisions are already behind them. What it needs is evidence.

## The source

`DECISIONS.md` at the project root, written by the `decision-log` plugin as the work happened. Each entry records what was chosen, what it was chosen over, the reason, and whether that reason was `stated` by the person or `inferred` by the AI.

The log is deliberately not framework-shaped. It carries no stages and no idea numbers, because it has to be usable by people who have never heard of shape+build+launch. Assigning stages is this skill's job, not the log's.

**If there is no `DECISIONS.md`**, say so and point at the log: `/plugin install decision-log@vibe2value`, then keep building and the review works next time. Then offer the fallback — orient from the code and run `guide` on the next change instead.

Do not reconstruct a log from git history or from the code. A commit says what changed, never why, so a reconstructed log is your guesswork wearing the costume of evidence. Reviewing it is worse than reviewing nothing, because it produces confidence rather than doubt.

## Before anything else, ask the gate question

Read the log, then ask one question and wait:

> Is this going in front of other people with your name on it?

**If no** — say the log did its job and stop. Do not review anyway. Do not list findings "just in case". Do not suggest they might want to launch it one day.

Most of what people build with AI is an experiment, and experiments are supposed to die. Not everything you vibe makes it to production, and that is the point. Auditing a throwaway is exactly the bogging-down this exists to prevent.

**If yes** — run the review.

## The review

Walk the log once, in order. Sort every entry into one of four buckets, and read the code where an entry is ambiguous — the log says what was decided, the code says what was actually done, and the gap between them is worth finding.

1. **Holds up.** The reason is still true and the decision still serves the project.
2. **Has drifted.** The reason was true when written and is not true now — a constraint lifted, scope changed, an assumption was tested and lost.
3. **Never had a reason.** Marked `inferred`, with nothing since supplying one. Start here: a load-bearing decision nobody can explain is the single most useful thing this review finds.
4. **Was never decided.** A gap where the framework expects a decision and the log has nothing — most often who it is for, what it deliberately does not do, or what signal would say it worked.

Then place each finding on the framework. Use the stage definitions and the situation list in the `guide` skill beside this one, and the bundled `reference/` files for the exact Sharpen prompt of any idea:

- Shape ideas (1.x.x): `reference/shape.md`
- Build ideas (2.x.x): `reference/build.md`
- Launch ideas (3.x.x): `reference/launch.md`

Reach first for the ideas that a log exposes better than code does: 1.1.1 and 1.1.2 when no entry says who it is for or what the problem was, 1.3.2 and 2.3.2 when scope grows across entries and nothing ever cuts, 2.1.3 when nothing records what the build was meant to teach, 2.2.3 when changes were made to a system nobody understood and the reasons are all `inferred`, 2.3.3 when no decision anywhere says how they would know it works, 3.1.3 when feedback arrived and no entry records what it changed, and 3.3.1 when nothing says what ready means.

## What you hand back

**Six findings, maximum.** Fewer is better. If the log throws up twenty, the six that matter are the ones that change what they do next.

This is a reality check, not an audit. Never produce a score, a percentage, a pass mark or a per-idea matrix. An audit becomes a document nobody acts on; the value here is being short enough to act on today.

For each finding, three lines:

```
**The decision:** <what the log says, quoted or close to it>
**What does not hold:** <one sentence — what changed, what is missing, what nobody can explain>
**The decision to make now:** <the single next decision, and the idea number it maps to>
```

Then the decisions that do hold up, as a plain list of one-liners. Do not expand them. Seeing what survived is most of the reassurance people come for, and it is the honest half of the picture.

If they want to act on a finding, hand off to `guide`: run the Sharpen prompt on that one decision until it reads one way. One decision at a time, same as always.

## Close on 3.3.3

End with the question the whole thing is for:

> Looking at these decisions, is this something you want to put your name on?

That is idea 3.3.3. It is theirs to answer. Do not answer it for them, do not push, and do not treat "no" as a failed review. A log that stops someone launching something they would not stand behind has just paid for itself.
