# Run (keep a live system honest)

The full 5 run ideas, each with its exact Sharpen prompt. Find the one that fits the decision, paste its prompt, and run it until the decision is sharp. Generated from vibe2value.com; do not edit by hand.

### 4.1.1 You Haven't Finished a Deploy Until You've Practised Undoing It

Decide what triggers a deploy to each environment, how you confirm it landed and the exact route back to the previous version.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this deploy and rollback plan is clear enough before you move forward.

Constraint:
Someone who has never deployed this project must be able to deploy it, confirm it landed and get back to the previous version using only what is written down.

Example of the standard:
Vague: "It deploys automatically when we merge and we can roll back if we need to."
Sharp: "A merge to main triggers the deploy action, which builds and swaps the container. It has landed when /health returns the new build sha, which you check yourself rather than trusting the green tick. To get back, re-run the previous action from the runs list, which takes about two minutes. Migrations are forward-only, so a code rollback does not undo one. That has to be handled separately."
The sharp version can be followed by a stranger under pressure. The vague one cannot.

Working draft:
What triggers a deploy to each environment: [merge, tag, manual run, schedule]
How you know it worked: [the check you make against the running thing]
The route back: [exact steps and roughly how long]

Task:
Decide whether a person who has never done this could deploy, confirm and roll back from these three lines alone. If not, rewrite them to meet the standard above. If the route back does not exist yet, say so plainly rather than describing one nobody has ever run.

Check:
- Does "how you know it worked" check the running thing, or does it trust the report of whatever ran the deploy?
- Have you actually performed the rollback, or only assumed it?
- Do data changes ride along with the code? Does undoing one undo the other?

Return:
- Verdict: clear, or needs work
- The corrected three lines
- Anything that has never actually been tested, named as such
```

### 4.1.2 If the Secret Only Exists on Your Machine, You Are the Single Point of Failure

Decide where secrets live and how they are set per environment, with every name the code reads written down and no real value anywhere near it.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this secrets plan is clear enough before you move forward.

Constraint:
A new person must be able to get the project running from what is written, without anyone handing them a value privately. Every name the code reads appears in the list. No real value appears anywhere in it.

Example of the standard:
Vague: "Secrets are in the environment and in the deploy settings."
Sharp: "The code reads DATABASE_URL, STRIPE_SECRET_KEY and ANTHROPIC_API_KEY. Locally they come from .env, which is gitignored and mirrored by .env.example with empty values. On develop and main they are set in the platform environment settings and two people can read them. Rotating one means changing it there and redeploying, because nothing picks it up at runtime."
The sharp version names every key and where its value lives per environment. The vague one names neither.

Working draft:
Names the code reads: [every one]
Where the value lives per environment: [local, plus each deployed environment]
How a new person gets set up: [the actual steps]

Task:
Decide whether a new person could get running from these three lines without being handed a value privately. Check that every name the code actually reads appears. If a real value has been written down anywhere, say so, because that is the thing to fix first.

Check:
- Does the code read a name that is not on the list?
- Is there a real value written into any file that is tracked?
- Can you say who is able to read each value? Can you say how one gets rotated?

Return:
- Verdict: clear, or needs work
- The corrected three lines
- Any name the code reads that is missing. Any real value that should not be there
```

### 4.2.1 The Failure Whose Only Symptom Is That the Answer Looks Wrong

Decide where each kind of failure appears and what a person is handed when it does, including the ones that never go red.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this failure surfacing plan is clear enough before you move forward.

Constraint:
Every kind of failure must have a named place it appears and a named thing a person is handed when it does. A failure that surfaces nowhere is a gap. Saying so counts as an answer.

Example of the standard:
Vague: "Errors are logged and we get alerts."
Sharp: "A failed payment writes the order id and the provider decline code to the app log and posts to #alerts within a minute. A model call that returns an empty summary surfaces nowhere: the user sees a blank card and we hear about it when they tell us. That one is a known gap and it is the next thing we close."
The sharp version names where each kind lands and what you get to work from. It also names the one that lands nowhere instead of leaving it off the list.

Working draft:
Kinds of failure: [list them, including the ones that do not crash]
Where each one appears: [log, channel, dashboard, nowhere]
What a person is handed: [what they can actually work from]

Task:
Decide whether every kind of failure has a named place and a named handoff. If one has neither, say so plainly and mark it as a gap rather than inventing a route for it.

Check:
- Is there a kind of failure whose only symptom is that the answer looks wrong?
- Could a person who did not build this act on what they are handed?
- Have you named the failures that surface nowhere, rather than leaving them off the list?

Return:
- Verdict: clear, or needs work
- The corrected three lines
- Any failure that surfaces nowhere, named as a gap
```

### 4.2.2 Decide What Reaches You Before Everything Does

Decide which work runs unattended, what hands itself back to a person and what that person actually receives when it does.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this escalation line is clear enough before you move forward.

Constraint:
You must be able to say which work runs unattended, what hands itself back to a person and what that person receives when it does. "Someone looks at everything" is not a line.

Example of the standard:
Vague: "We keep an eye on it and step in when something looks off."
Sharp: "Summaries under 400 words publish without review. Anything longer, or anything citing a source we have not seen before, stops and goes to the review queue with the draft, the sources and the reason it stopped. Payment failures never retry silently: they stop and post to #alerts with the order id. Everything else runs unattended and we read the weekly digest."
The sharp version says what carries on, what stops and what the person is holding. The vague one relies on somebody noticing.

Working draft:
Runs unattended: [what carries on without anyone]
Hands back to a person: [what stops, plus what triggers it]
What the person receives: [what they can act on immediately]

Task:
Decide whether the line is real. If the answer is that a person checks everything, that is not a line, it is the absence of one. The honest move is to name what should run unattended and start there.

Check:
- Is the line written down anywhere, or does it live in one person's head?
- When something hands back, does the person get enough to act, or do they have to reconstruct it?
- Is anything running unattended that you would not have chosen?

Return:
- Verdict: clear, or needs work
- The corrected three lines
- Anything running unattended by accident rather than by decision
```

### 4.3.2 How Would You Know If Any of This Worked?

Decide what evidence would tell you the knowledge base is doing its job, then take the reading before you start so you have something to compare against.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are taking a reading, not sharpening a sentence. Do the work first, then report.

Task:
Work through knowledge-base/ and fill it in, so the next person or the next AI could pick this project up from what is written there. Do not ask me anything. Make the best call you can and keep going.

Then report three numbers and nothing else.

Invented:
Every statement you made about this project that you could not source from something already in the repo. List them one per line, each naming the file you put it in. This is the number that matters, so do not soften it.

Named gaps:
Every place you wrote that something is not decided yet rather than filling the space. List them one per line.

Size:
The word count of knowledge-base after you finished.

Return:
- The three counts
- Both lists in full
- One sentence on which file was hardest to fill and why

Then stop. Do not offer to fix anything. The person reading this is the only one who can tell which of your statements are actually false. Your list is where they start rather than the verdict.
```

