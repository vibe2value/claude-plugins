# vibe2value Claude plugins

A Claude Code plugin marketplace from [vibe2value](https://vibe2value.com). Build with AI and trust what you make.

## Install

In Claude Code, add the marketplace, then install a plugin:

```
/plugin marketplace add vibe2value/claude-plugins
/plugin install decision-log@vibe2value
/plugin install shape-build-launch@vibe2value
```

Update later with:

```
/plugin marketplace update vibe2value
```

## Plugins

### decision-log

Keeps a running log of the decisions you make while building with AI, and the reason for each one, in a `DECISIONS.md` at your project root.

There is nothing to start or configure. Once installed it records what you chose, what you chose it over and why, as it happens — with the reasons you actually gave marked apart from the ones the AI worked out for itself.

It works entirely on its own. You do not need the framework below, and you do not need to have heard of it.

### shape-build-launch

Guides building software with AI through the shape+build+launch framework: decide what to make (Shape), build it (Build), put it in front of people (Launch), making each decision sharp before any code is written.

```
/shape-build-launch:guide
```

And the same framework run backwards, over decisions already made:

```
/shape-build-launch:review
```

## How they fit together

The framework asks you to make each decision sharp *before* you write code. In practice almost nobody does — they build first, and only later start wondering whether the thing is real.

So the two plugins split the job. **The log records; the framework interprets.** `decision-log` runs underneath the work rather than before it, and knows nothing about stages or ideas — it just captures the reasoning while it still exists. `/shape-build-launch:review` is the framework reading that log as evidence, at the moment someone actually cares about the answer.

That way the log stays installable by anyone, and the framework stays the only place the framework is defined.

Not everything you vibe makes it to production, and that is the point. Neither plugin asks you to finish anything.

## Adding a plugin to this marketplace

1. Create `plugins/<plugin-name>/.claude-plugin/plugin.json` with at least a `name`.
2. Put skills under `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` (commands, agents and hooks are also supported).
3. Add an entry to the `plugins` array in `.claude-plugin/marketplace.json`, with `source` set to the relative path, for example `./plugins/<plugin-name>`.
4. Validate before pushing: `claude plugin validate .`
