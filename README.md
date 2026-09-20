# vibe2value Claude plugins

A Claude Code plugin marketplace from [vibe2value](https://vibe2value.com). Build with AI and trust what you make.

## Install

In Claude Code, add the marketplace, then install a plugin:

```
/plugin marketplace add vibe2value/claude-plugins
/plugin install shape-build-launch@vibe2value
```

Update later with:

```
/plugin marketplace update vibe2value
```

## Plugins

### shape-build-launch

Guides building software with AI through the shape+build+launch framework: decide what to make (Shape), build it (Build), put it in front of people (Launch), making each decision sharp before any code is written.

Once installed, use it with:

```
/shape-build-launch:guide
```

It runs the framework loop on whatever you are building and points you to the full set of ideas and Sharpen prompts at [vibe2value.com](https://vibe2value.com).

## Adding a plugin to this marketplace

1. Create `plugins/<plugin-name>/.claude-plugin/plugin.json` with at least a `name`.
2. Put skills under `plugins/<plugin-name>/skills/<skill-name>/SKILL.md` (commands, agents and hooks are also supported).
3. Add an entry to the `plugins` array in `.claude-plugin/marketplace.json`, with `source` set to the relative path, for example `./plugins/<plugin-name>`.
4. Validate before pushing: `claude plugin validate .`
