# design-redline

**English** · [简体中文](./README.zh-CN.md)

> Turn "this looks off, but I can't say why" into a ranked, fixable design redline.

**design-redline** is an agent skill for *reviewing* interfaces, not building them. Point your coding
agent at a screenshot, a live URL, a Figma frame, or a component, and it audits the design against ten
review lenses, measures what can be measured, and hands back a report where every issue is graded
**blocker / major / minor / polish** and written as *observation → why it matters → exact fix → how to
verify*. It is the design-review half of your workflow: it pairs with whatever you use to build.

Most design feedback dies as taste — "make it pop," "it feels cramped" — and a maker can't act on a
feeling. This skill converts the feeling into a list you can work through in order and check off.

## Why it's different

- **Measures before it judges.** A gap isn't "too tight," it's 8px where its siblings are 16px.
  Contrast isn't "a bit light," it's 3.1:1 where WCAG AA needs 4.5:1.
- **Every note owes a fix.** No issue ships without one specific, buildable change and a way to verify it.
- **Severity-first, not list-first.** It leads with a verdict and the one fix that matters most, so you
  don't drown in forty equal-weight notes while the real blocker survives.
- **Reviews, doesn't redesign.** It respects what you built and tells you exactly what to change —
  in any stack (HTML/CSS, React, Vue, Svelte, SwiftUI, native).

## Features

- **Ten review lenses** — hierarchy & focus, layout & alignment, spacing & rhythm, typography,
  color & contrast, states & edge cases, motion & feedback, copy & microcopy, accessibility, responsiveness.
- **The 5-second first-glance test** — catches hierarchy failures before detail blinds you.
- **Severity grading** — blocker / major / minor / polish, judged by impact on the screen's real job.
- **A WCAG 2.2 contrast checker** (`scripts/contrast.py`) — single pairs or a CSV batch, with AA/AAA
  and non-text (UI component) verdicts, no dependencies.
- **State & edge-case coverage** — hover, focus, disabled, loading, empty, error, success, overflow.
- **A ready report template** so every review comes back in the same, skimmable shape.
- **Full English and Chinese versions** of the skill and docs.

## Installation

Clone the repo, then make the skill available to your agent.

```bash
git clone https://github.com/fangdididi/design-redline.git
```

### Claude Code
Copy the skill into your skills directory (project-level or user-level):

```bash
mkdir -p .claude/skills/design-redline
cp -r design-redline/* .claude/skills/design-redline/
```

Claude Code discovers it automatically; invoke it by asking to "review" or "redline" a screen, or call
the skill by name.

### Codex
Place the folder where your Codex config loads skills/instructions from (e.g. a `skills/` directory it
reads), and reference `SKILL.md` in your prompt, or paste the skill content into your `AGENTS.md` /
project instructions.

### Cursor
Add the skill as a project rule or skill: drop the folder in your repo and reference `SKILL.md`, or
paste its guidance into `.cursor/rules`. Then ask Cursor to review a screenshot or a running page.

### Any other agent
`SKILL.md` is plain Markdown with YAML frontmatter. Give it to any agent that reads instructions, and
run the helper script with Python 3.

## Usage

Give the agent the artifact plus the screen's intent:

```
Review this signup screen against design-redline. It's for first-time visitors on mobile; the one
action that matters is "Create account." Here's the URL / screenshot.
```

The agent frames the review, captures evidence at 360/768/1280px, runs the 5-second test, walks the ten
lenses, grades every finding, and returns a `redline.md`.

### The contrast helper

```bash
# One pair
python3 scripts/contrast.py "#E57373" "#FFFFFF"

# Large text (>=24px, or >=19px bold)
python3 scripts/contrast.py "#767676" white --size 24

# A batch: CSV rows of  fg,bg[,label]
python3 scripts/contrast.py --pairs pairs.csv
```

It prints the contrast ratio and PASS/FAIL for normal text (AA 4.5:1 / AAA 7:1), large text
(AA 3:1 / AAA 4.5:1), and UI components & graphics (AA 3:1). Exit code is non-zero when a pair fails
normal-text AA, so you can gate a build on it.

## Examples

**Before:** "The signup page feels off and a bit hard to read."

**After (excerpt from the redline):**

```
Verdict: Does not ship yet. The primary action loses to a louder "Learn more" link, and the
password error is unreadable. 1 blocker, 2 major, 3 minor, 2 polish.

[BLOCKER] Color & contrast · Inline password error text
Observation: Error text #E57373 on #FFFFFF measures 2.9:1; AA needs 4.5:1.
Why it matters: The user who most needs the error is the least likely to read it, and may abandon signup.
Fix: Darken to #C62828 (5.6:1 on white) and add a non-color cue (leading "!" icon + bold label).
Verify: Re-run scripts/contrast.py on the pair; confirm >=4.5:1 and the icon shows with color removed.
```

## File structure

```
design-redline/
├── SKILL.md                      # The skill (English)
├── SKILL.zh-CN.md                # The skill (Chinese)
├── README.md                     # This file
├── README.zh-CN.md               # README (Chinese)
├── LICENSE                       # MIT
├── references/
│   ├── review-lenses.md          # Full per-lens checklist
│   └── report-template.md        # Copy-paste redline skeleton
└── scripts/
    ├── contrast.py               # WCAG 2.2 contrast checker
    └── test_contrast.py          # Tests for the checker
```

## License

MIT — see [LICENSE](./LICENSE).
