# Shape (decide what to make)

The full 9 shape ideas, each with its exact Sharpen prompt. Find the one that fits the decision, paste its prompt, and run it until the decision is sharp. Generated from vibe2value.com; do not edit by hand.

### 1.1.1 If You Can't Name the User, You're Guessing What They Want

Name the user definition: say who the user is, what starts the need and what result they are trying to reach.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this user definition is clear enough before you move forward.

Constraint:
The user definition must be specific enough that two people would make the same product decision from it.

Example of the standard:
Vague: "This is for people who want to search the web with AI."
Sharp: "This is for a content creator who manages a website and needs to find gaps in what they have published so they can decide what to write next."
The sharp version is specific enough that two people would make the same product decision. The vague one is not.

Working draft:
User: [name one real user]
Trigger: [what starts the need]
Outcome: [what they are trying to reach]

Task:
Decide whether this user definition is specific enough that two people would make the same product decision. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state who the user is, what starts the need and what result they are trying to reach?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

**Worked examples:** subCancel (https://github.com/vibe2value/subcancel/blob/main/knowledge-base/shape-build-launch/shape/user.md) · ghostMarketingFlow (https://github.com/vibe2value/ghost-marketing-flow/blob/main/knowledge-base/shape-build-launch/shape/user.md) · flowRun (https://github.com/vibe2value/flow-run/blob/main/knowledge-base/shape-build-launch/shape/user.md)

### 1.1.2 Describe the Pain Without Mentioning the Solution

Describe the pain statement: say who is affected, what happens right before the pain appears and what it costs the user or the team.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this pain statement is clear enough before you move forward.

Constraint:
The pain statement must be specific enough that two people would frame the same problem from it.

Example of the standard:
Vague: "Users struggle to get useful results from AI search."
Sharp: "A content creator searches for what to write next but gets generic suggestions because the tool does not know what they have already published. They waste time filtering irrelevant results instead of writing."
The sharp version is specific enough that two people would frame the same problem. The vague one is not.

Working draft:
Affected user: [who is affected]
Trigger: [what happens right before the pain appears]
Visible cost: [what it costs the user]

Task:
Decide whether this pain statement is specific enough that two people would frame the same problem. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state who is affected, what happens right before the pain appears and what it costs the user?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 1.1.3 The One-Line Promise That Keeps Your Build Honest Throughout

Write the one-line promise: say who it is for, what result it creates and what it is deliberately not trying to do.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether the one-line promise is clear enough before you decide what to build.
Constraint:
The one-line promise must be specific enough that two people would position the product the same way from it.
Example of the standard:
Vague: "This helps people get better results from AI search."
Sharp: "This helps an organic paid content creator find gaps in what they have already published so they can decide what to write next, without giving generic content advice."
The sharp version is specific enough that two people would position the product the same way. The vague one is not.
Context:
User: [name one real user]
Promised outcome: [name one promised outcome]
Boundary: [name one thing this does not promise]
Task:
Decide whether this one-line promise is clear enough to guide the product. If it already is, say so. If it is vague, rewrite it so you can name one user, one promised outcome and one clear boundary on what is not promised.
Check:
- Does it name one real user instead of a broad audience?
- Is the promised outcome specific enough that two people would describe the same value from it?
- Is the boundary clear enough to stop the promise from expanding?
Return:
- Verdict: clear, or needs work
- The corrected one-line promise, the three lines, or the original if already clear
- What was vague, and the one change that fixed it
```

### 1.2.1 Can You Explain This in 30 Seconds Without Mentioning the Tech?

Explain the 30-second explanation: explain who it is for, what problem it fixes and what useful result appears without adding a second paragraph.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this 30-second explanation is clear enough before you move forward.

Constraint:
The 30-second explanation must be specific enough that two people would describe the same product from it.

Example of the standard:
Vague: "This is an AI search tool that helps people find better answers."
Sharp: "This helps a content creator find gaps in what they have already published so they can decide what to write next, using AI search shaped by their saved context."
The sharp version is specific enough that two people would describe the same product. The vague one is not.

Working draft:
User: [who it is for]
Problem: [what problem it fixes]
Useful result: [what useful result appears]

Task:
Decide whether this 30-second explanation is specific enough that two people would describe the same product. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Does it meet this bar: You can explain who it is for, what problem it fixes and what useful result appears without adding a second paragraph

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 1.2.2 What Does "Success" Actually Mean for the First Version You Ship?

Define the version one success definition: say what has to happen, how it will be measured and what number or threshold counts as enough.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this version one success definition is clear enough before you move forward.

Constraint:
The version one success definition must be specific enough that two people would make the same go or no-go call from it.

Example of the standard:
Vague: "Users find the AI search results useful and keep coming back."
Sharp: "A content creator completes three searches using their saved context, and at least two of those searches return results they act on within the same session."
The sharp version is specific enough that two people would make the same go or no-go call. The vague one is not.

Working draft:
Outcome: [what has to happen]
Metric: [how it will be measured]
Threshold: [what number counts as enough]

Task:
Decide whether this version one success definition is specific enough that two people would make the same go or no-go call. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what has to happen, how it will be measured and what number or threshold counts as enough?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 1.2.3 The Risks You're Avoiding Naming Are the Ones That Bite You

Name the named risk: say what might fail, who or what it would affect and what action will reduce the damage.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this named risk is clear enough before you move forward.

Constraint:
The named risk must be specific enough that two people would prepare for the same failure from it.

Example of the standard:
Vague: "There are some risks around whether the AI search results will be useful."
Sharp: "If a content creator’s saved context is too narrow, AI search returns the same results every time and the tool feels broken. The user stops trusting the results before they have tested enough to see the value."
The sharp version is specific enough that two people would prepare for the same failure. The vague one is not.

Working draft:
Likely failure: [what might fail]
Affected user or workflow: [who or what it would affect]
Mitigation: [what action reduces the damage]

Task:
Decide whether this named risk is specific enough that two people would prepare for the same failure. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what might fail, who or what it would affect and what action will reduce the damage?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 1.3.1 The One Outcome That Makes This Build Worth Doing in the First Place

Choose the main outcome: say what changes for the user, why that change matters and what signal will show it is real.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this main outcome is clear enough before you move forward.

Constraint:
The main outcome must be specific enough that two people would prioritize the same work from it.

Example of the standard:
Vague: "This creates more value for users of the AI search tool."
Sharp: "A content creator completes a search using their saved context and acts on at least one result in the same session, instead of leaving to search elsewhere."
The sharp version is specific enough that two people would prioritize the same work. The vague one is not.

Working draft:
User outcome: [what changes for the user]
Why it matters: [why that change matters]
Proof signal: [what signal will show it is real]

Task:
Decide whether this main outcome is specific enough that two people would prioritize the same work. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what changes for the user, why that change matters and what signal will show it is real?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 1.3.2 What This Will Not Do (On Purpose) Is Half the Decision

Set the scope boundary: say what stays in, what stays out and why the cut protects the core path.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this scope boundary is clear enough before you move forward.

Constraint:
The scope boundary must be specific enough that two people would cut the same feature from it.

Example of the standard:
Vague: "Version one will stay focused and not do too much."
Sharp: "Version one will help a content creator search using their saved context. It will not support multiple saved contexts per user yet because that would complicate the core search flow before it is proven."
The sharp version is specific enough that two people would cut the same feature. The vague one is not.

Working draft:
Keep in: [what stays in scope]
Leave out: [what stays out]
Why the cut helps: [why the cut protects the core path]

Task:
Decide whether this scope boundary is specific enough that two people would cut the same feature. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Can you state what stays in, what stays out and why the cut protects the core path?

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

### 1.3.3 Describe One Main Path First, Then Ignore Everything Else

Describe the main path: describe the user, what starts the flow and the exact steps that lead to the outcome.

**Sharpen prompt** (paste into AI chat, replace the bracketed lines):

```
You are checking whether this main path is clear enough before you move forward.

Constraint:
The main path must be specific enough that two people would design the same flow from it.

Example of the standard:
Vague: "Users can explore the search tool in a few different ways."
Sharp: "A content creator opens the app, enters a question about what to write next, sees results shaped by their saved context and acts on one result in the same session."
The sharp version is specific enough that two people would design the same flow. The vague one is not.

Working draft:
User: [who the path is for]
Trigger: [what starts the flow]
Path to outcome: [the exact steps that lead to the outcome]

Task:
Decide whether this main path is specific enough that two people would design the same flow. If it already is, say so. If it is vague, rewrite it to meet the standard in the example above.

Check:
- Would two people interpret this the same way?
- Does it stay concrete enough to guide the next step?
- Does it meet this bar: You can describe the user, what starts the flow and the exact steps that lead to the outcome

Return:
- Verdict: clear, or needs work
- The corrected three lines, or the original three if already clear
- What was vague, and the one change that fixed it
```

