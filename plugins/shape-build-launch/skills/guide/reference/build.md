# Build (make it with AI)

The full 9 build ideas, each with its exact Sharpen prompt. Find the one that fits the decision, paste its prompt, and run it until the decision is sharp. Generated from vibe2value.com; do not edit by hand.

### 2.1.1 The Only Path Your Prototype Actually Needs to Walk

Define the prototype path: say what the prototype is meant to teach, which path will test it and what signal counts as proof.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this prototype path is clear enough before you move forward.

Constraint:
The prototype path must be specific enough that two people would build the same thin test from it.

Example of the standard:
Vague: "Test whether people like the check-in email."
Sharp: "Learning goal: whether a solo operator acts on a check-in email instead of ignoring it. Test path: they add three real subscriptions, get one email listing them and click through to mark one for cancel. Proof signal: at least one is marked within 24 hours."
The sharp version is specific enough that two people would build the same test. The vague one is not.

Working draft:
Learning goal: [what the prototype is meant to teach]
Test path: [which path will test it]
Proof signal: [what signal counts as proof]

Task:
Decide whether this prototype path is specific enough that two people would build the same thin test. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what the prototype teaches, which path tests it and what signal counts as proof?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.1.2 Where the User First Feels Value Is Where to Start Building

Find the first value moment: point to the moment the user first feels relief or progress and the step immediately before it.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this first value moment is clear enough before you move forward.

Constraint:
The first value moment must be specific enough that two people would optimize the same step from it.

Example of the standard:
Vague: "Users feel value once they start using the search tool."
Sharp: "A content creator feels value when the first search result reflects what they have already published, right after they enter their first question with saved context."
The sharp version is specific enough that two people would optimize the same step. The vague one is not.

Working draft:
User: [who first feels value]
First value moment: [the first moment they feel relief or progress]
Step right before it: [the step immediately before that moment]

Task:
Decide whether this first value moment is specific enough that two people would optimize the same step. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Does it meet this bar: You can point to the moment the user first feels relief or progress and the step immediately before it

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.1.3 What This Build Is Meant to Teach You, Not Just to Ship

Name the learning goal: say what you believe, what the build needs to answer and what signal will prove or weaken that belief.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this learning goal is clear enough before you move forward.

Constraint:
The learning goal must be specific enough that two people would collect the same evidence from it.

Example of the standard:
Vague: "This build should help us learn what users want from AI search."
Sharp: "This build should tell us whether a content creator gets more relevant results when their saved context shapes the search than when it does not."
The sharp version is specific enough that two people would collect the same evidence. The vague one is not.

Working draft:
Hypothesis: [what you believe]
Question: [what the build needs to answer]
Signal: [what signal will prove or weaken that belief]

Task:
Decide whether this learning goal is specific enough that two people would collect the same evidence. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what you believe, what the build needs to answer and what signal will prove or weaken that belief?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.2.1 The Routine Work Checklist Nobody Talks About

Define the routine work checklist: say what repeats, who owns it and what done looks like each time.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this routine work checklist is clear enough before you move forward.

Constraint:
The routine work checklist must be specific enough that two people would do the same checks from it.

Example of the standard:
Vague: "We will sort out the routine operational work later."
Sharp: "Every time the tooltip data changes, one person verifies the JSON is valid, checks that each slug matches a published post and confirms the tooltips render correctly before deploying the theme."
The sharp version is specific enough that two people would do the same checks. The vague one is not.

Working draft:
Recurring task: [what repeats]
Owner: [who owns it]
Done condition: [what done looks like each time]

Task:
Decide whether this routine work checklist is specific enough that two people would do the same checks. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what repeats, who owns it and what done looks like each time?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.2.2 Buy vs Build Is a Strategy Choice, Not an Engineering One

Make the buy versus build decision: say what the decision is about, why one side wins and which constraint makes the call.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this buy versus build decision is clear enough before you move forward.

Constraint:
The buy versus build decision must be specific enough that two people would choose the same leverage point from it.

Example of the standard:
Vague: "We should decide whether to use an existing service or build it ourselves."
Sharp: "Buy authentication because it is not where value lives. Build the context-shaped search because that is where the product makes a unique decision for the user."
The sharp version is specific enough that two people would choose the same leverage point. The vague one is not.

Working draft:
Decision area: [what the decision is about]
Why buy or build: [why one side wins]
Deciding constraint: [which constraint makes the call]

Task:
Decide whether this buy versus build decision is specific enough that two people would choose the same leverage point. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what the decision is about, why one side wins and which constraint makes the call?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.2.3 Understanding the Shape of the System Before You Change It

Map the system shape: say which part owns what, what each part depends on and where the important handoff happens.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this system shape is clear enough before you move forward.

Constraint:
The system shape must be specific enough that two people would draw the same core boundaries from it.

Example of the standard:
Vague: "The system has a few services that connect together."
Sharp: "The frontend handles the search interface and user context. The Worker orchestrates auth checks, database reads and AI search calls. The database stores preferences and history. Auth is handled externally. Each part has one job and one clear handoff to the next."
The sharp version is specific enough that two people would draw the same core boundaries. The vague one is not.

Working draft:
Part or boundary: [which part owns what]
Dependency or handoff: [where the important dependency or handoff happens]
Ownership boundary: [what each part should not own]

Task:
Decide whether this system shape is specific enough that two people would draw the same core boundaries. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state which part owns what, what each part depends on and where the important handoff happens?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.3.1 Where the Real Differentiation Actually Lives in Your Build

Name the real differentiation: point to the advantage, show where the user feels it and say what should remain standard.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this real differentiation is clear enough before you move forward.

Constraint:
The real differentiation must be specific enough that two people would invest in the same custom work from it.

Example of the standard:
Vague: "Our differentiation is that we use AI to make search better."
Sharp: "Our differentiation is that a content creator gets search results shaped by what they have already published. The context layer is the custom work. Everything else, auth, database, hosting, stays standard."
The sharp version is specific enough that two people would invest in the same custom work. The vague one is not.

Working draft:
Real advantage: [what the real advantage is]
Where the user feels it: [where the user feels that advantage]
What stays standard: [what should remain commodity or standard]

Task:
Decide whether this real differentiation is specific enough that two people would invest in the same custom work. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Does it meet this bar: You can point to the advantage, show where the user feels it and say what should remain standard

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.3.2 Why Cutting Features Is a Design Skill Most Builders Skip

Choose the feature cut: say what stays central, what gets removed and why the product becomes stronger because of that cut.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this feature cut is clear enough before you move forward.

Constraint:
The feature cut must be specific enough that two people would remove the same complexity from it.

Example of the standard:
Vague: "We should probably keep the search tool simple."
Sharp: "We are cutting query history from version one because the core test is whether a content creator can search with their saved context and act on a result in one session. History adds UI complexity without proving the context layer works."
The sharp version is specific enough that two people would remove the same complexity. The vague one is not.

Working draft:
Core path to protect: [what must stay central]
Feature to cut: [what gets removed]
Why the cut strengthens it: [why the product gets stronger because of that cut]

Task:
Decide whether this feature cut is specific enough that two people would remove the same complexity. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what stays central, what gets removed and why the product becomes stronger because of that cut?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 2.3.3 The One Metric That Proves This Works for Real Users

Define the proof metric: say what the metric is, what user behavior creates it and what threshold counts as enough.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this proof metric is clear enough before you move forward.

Constraint:
The proof metric must be specific enough that two people would make the same keep or cut decision from it.

Example of the standard:
Vague: "We will track engagement and adoption of the search tool."
Sharp: "We will track how many content creators act on at least one context-shaped search result in the same session. We will treat two out of three searches producing an actionable result as proof that the context layer is working."
The sharp version is specific enough that two people would make the same keep or cut decision. The vague one is not.

Working draft:
Metric: [what the metric is]
User behavior behind it: [what user behavior creates it]
Threshold: [what threshold counts as enough]

Task:
Decide whether this proof metric is specific enough that two people would make the same keep or cut decision. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what the metric is, what user behavior creates it and what threshold counts as enough?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

