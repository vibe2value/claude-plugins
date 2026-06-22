# shape-build-launch

A Claude Code plugin that guides building software with AI through the vibe2value shape+build+launch framework.

The hard part of building with AI is no longer the code. It is judgement: knowing what to ask for, what to leave out and how to tell good output from output that only looks good. This plugin makes the next decision sharp before any code is written.

## Use

Once installed, the skill surfaces on its own when Claude judges you are working through a build decision (Claude Code loads its description at startup and pulls in the full skill when your request matches). Auto-surfacing is a per-message judgement, not a guarantee, so to apply it reliably to a piece of work, invoke it directly:

```
/shape-build-launch:guide
```

You can also just say "use the shape-build-launch skill", or add a line to your project's `CLAUDE.md` so it stays in play across a whole session.

The skill runs a simple loop on whatever you are building:

1. Find the stage (Shape, Build or Launch).
2. Pick the one idea that fits the moment you are in.
3. Sharpen that decision until two people would build the same thing from it.
4. Only then build.
5. Repeat for the next decision.

## What is included

All 27 ideas and their exact Sharpen prompts are bundled with the skill, grouped by stage:

```
skills/guide/
├── SKILL.md                 the loop, the Sharpen template, worked examples
└── reference/
    ├── shape.md             the 9 Shape ideas, each with its exact Sharpen prompt
    ├── build.md             the 9 Build ideas
    ├── launch.md            the 9 Launch ideas
    └── manifest.json        source and a content hash per idea
```

The reference files are generated from [vibe2value.com](https://vibe2value.com), the single source of truth, so the prompts here match what is published on the site. `manifest.json` records each idea's source slug, last-updated date and a content hash, so alignment can be checked rather than assumed.

## More

For the worked examples in full, the diagrams, and a free 1:1 working session to apply this to what you are building, see [vibe2value.com](https://vibe2value.com). The machine-readable index is at [vibe2value.com/llms.txt](https://vibe2value.com/llms.txt) and the same skill in paste-anywhere form is at [vibe2value.com/skill.txt](https://vibe2value.com/skill.txt).
