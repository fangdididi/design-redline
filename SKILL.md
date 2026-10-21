---
name: design-redline
description: >-
  A disciplined design-review skill that turns "this looks off, but I can't say why" into a ranked,
  fixable redline. Point it at a screenshot, a live URL, a Figma frame, or a component, and it audits
  the interface against ten review lenses (hierarchy, layout & alignment, spacing rhythm, typography,
  color & contrast, states & edge cases, motion, copy & microcopy, accessibility, responsiveness),
  measures what can be measured, and returns issues graded blocker / major / minor / polish, each written
  as observation -> why it matters -> exact fix -> how to verify. Use it whenever someone asks you to
  critique, review, redline, QA, polish, or sign off on a UI; when a screen "looks generic / AI-made /
  unfinished"; before a design handoff or ship; or when you need an accessibility and contrast pass. It
  reviews work that already exists rather than inventing a new look, so it pairs with any build workflow
  and any stack (HTML/CSS, React, Vue, Svelte, SwiftUI, native).
---

# design-redline

Most design feedback dies as taste. "Make it pop." "It feels cramped." "Something's off at the top."
The maker cannot act on a feeling, so nothing changes, or the wrong thing changes, and the next review
repeats the same vague note. design-redline exists to convert that feeling into a list a maker can work
through in order and check off.

A redline is the old print-shop habit of marking a proof in red: every flaw circled, named, and told
what to become. This skill applies that habit to screens. It does not redesign the work and it does not
hand back a mood. It produces a document: each problem located precisely, rated by how much it hurts,
explained in one honest sentence, paired with a concrete change, and closed with a way to confirm the
change worked.

Two rules keep a review from drifting into opinion:

1. **Measure before you judge.** A gap is not "too tight," it is 8px where its siblings are 16px.
   Contrast is not "a bit light," it is 3.1:1 where AA needs 4.5:1. Measured notes survive an argument;
   adjectives do not. When a number is available, the review states it.
2. **Every note owes a fix.** A critique that only names the flaw moves the work backwards — the maker
   now feels judged and still does not know what to do. Each issue in a redline carries one specific,
   buildable change, and nothing ships in the report that you cannot tell the maker how to resolve.

## When to use this

- "Review / critique / redline / QA this screen" — a page, a flow, a component, a whole app.
- "It looks generic / templated / AI-made / unfinished / off and I don't know why."
- Before a design-to-engineering handoff, or before a release sign-off.
- An accessibility and color-contrast pass on an existing interface.
- A second opinion on your own work before you show it to anyone.
- A recurring design bar: run the same lenses on every screen so quality stops depending on who looked.

Do **not** use this to invent a fresh visual direction from nothing — this reviews what exists. If there
is no artifact yet, there is nothing to redline.

## What you need before you start

- **The artifact**, in one of these forms, best first: a live URL you can open in a browser; an exported
  screenshot (ideally at the three widths below); a component you can render; a static mock. A live page
  beats a screenshot because you can inspect real values and real states.
- **The intent**: what is this screen for, who uses it, and what is the one action it exists to get. A
  review with no intent grades decoration; a review with intent grades whether the screen does its job.
- **The reference bar**, if any: a brand, a design system, a competitor, or a sibling screen the work
  should sit beside without looking foreign.

If intent is missing, ask one question — "what is the single most important thing a user should do on
this screen?" — before reviewing. One sentence of intent changes most of the verdicts.

## The run

### Step 1 — Frame the review

Write three lines before you look hard: the screen's **job**, its **primary action**, and the **viewer**
you are reviewing as (first-time user, power user, someone on a phone on a train). Pick the viewer whose
experience matters most for this screen; you will return to it whenever a judgment is close.

### Step 2 — Capture the evidence

- A **live URL**: open it in a real browser at three widths — **360px** (phone), **768px** (tablet),
  **1280px** (desktop) — and capture each. Then probe the states in Step 6; a screenshot only shows one.
- A **screenshot only**: note that you are reviewing a single frozen state and that state/responsive
  findings are inferred, not confirmed. Say so in the report so no one trusts a check you could not run.
- Record the real type sizes, colors, and spacing when you can read them (dev tools, the file, the
  export). Measured evidence is what separates this from a vibe.

### Step 3 — First-glance test (5 seconds)

Look for five seconds, then look away and answer from memory: *What is this? What should I do? What drew
my eye first?* If the answer to any is wrong or blank, that is your first and probably highest-severity
finding — hierarchy is failing before any detail matters. Record it before you study the screen, because
once you know the screen you can never un-know it, and the five-second truth is the one your users live.

### Step 4 — Walk the ten lenses

Go through each lens in order. For each, note what works (briefly — makers need to know what to keep) and
what is wrong. Pull every flaw into the issue format in Step 7; do not fix inline.

1. **Hierarchy & focus.** Does the eye land on the primary action first? Is there exactly one clear
   focal point per view, or do three things shout at once? Secondary and tertiary actions should read
   as such. A screen where everything is bold has no hierarchy.
2. **Layout & alignment.** Do elements share edges and a grid, or drift by a few pixels? Are related
   things grouped and unrelated things apart (proximity)? Is there one clear reading path, not a maze?
3. **Spacing & rhythm.** Is spacing from a scale (e.g. 4/8/12/16/24/32) or arbitrary? Does space inside
   a group read tighter than space between groups? Cramped controls and lonely orphaned elements both
   break rhythm. Generous, consistent space reads as "designed"; random gaps read as "assembled."
4. **Typography.** How many type sizes and weights — is there a real scale or a pile of near-duplicates?
   Line length 45–75 characters for body? Line height comfortable (~1.4–1.6 body)? Numerals aligned in
   tables? One typeface family doing a clear job, not three competing.
5. **Color & contrast.** Is color used with intent (one accent that means "act here"), or sprinkled?
   Does every text/background pair meet contrast (run `scripts/contrast.py`)? Is color ever the *only*
   signal for a link, an error, or a state (fails colorblind users)? Is the palette coherent across the
   screen?
6. **States & edge cases.** This is where polished work separates from demos. Check: hover, focus
   (visible focus ring, 3:1), active, disabled, loading, empty, error, success, and the long/overflow
   case (longest realistic name, zero items, 9,999 items, no network). Most "unfinished" screens are
   unfinished here.
7. **Motion & feedback.** Does every action give feedback within ~100ms? Are transitions purposeful and
   short (not decorative, not janky)? Does anything move that should hold still? Respect reduced-motion.
8. **Copy & microcopy.** Are labels specific ("Save changes" not "Submit")? Do errors say what happened
   and what to do? Is the voice consistent? Is there jargon the viewer from Step 1 would not know?
9. **Accessibility.** Beyond contrast: target size (~44px touch), keyboard reachability and visible
   focus order, alt text for meaningful images, labels tied to inputs, headings in order, and not
   relying on color alone. See `references/review-lenses.md` for the full checklist.
10. **Responsiveness.** Across the three widths: does anything overflow, truncate badly, or collapse into
    a tap-hostile mess? Does the primary action stay reachable (not below a mobile fold with no cue)?
    Does text reflow to 200% zoom without loss?

### Step 5 — Grade every finding

Assign each issue one severity, using impact on the Step 1 primary action and viewer, not how annoying it
is to you:

- **Blocker** — the screen fails its job or excludes users: primary action unusable, broken state, a
  contrast or keyboard failure that locks someone out. Must fix before ship.
- **Major** — the screen works but a real user is likely to stumble, misread, or distrust it: weak
  hierarchy on the main action, a confusing error, a missing empty state.
- **Minor** — noticeable to a careful user, small cost: inconsistent spacing, an off-scale type size, a
  slightly low-contrast caption.
- **Polish** — correct and usable; this is the gap between "fine" and "considered": refined rhythm,
  tighter copy, a nicer empty state. Worth doing when the blockers and majors are gone.

Be honest about the split. A review that is all polish on a screen with a broken primary action has
missed the point; a review that is all blockers on a solid screen is just harsh.

### Step 6 — Probe the states (live only)

If you have a live page, actually trigger the states from lens 6: tab through it for focus order, submit
an empty form for errors, feed it the longest and the emptiest data, throttle or kill the network for
loading and offline. Write down what you find; inferred state bugs become confirmed ones here, and new
ones appear that no static frame could show.

### Step 7 — Write the redline

Produce the report in the structure below. Every issue is one block:

```
[SEVERITY] Lens · Location
Observation: what is there, measured when possible.
Why it matters: the cost to the Step 1 viewer and action, in one sentence.
Fix: the specific change to make — values, not adjectives.
Verify: how to confirm it is fixed.
```

Order the report by severity (blockers first), and within a severity by how close the issue sits to the
primary action. Open with a two-line verdict (does this screen do its job today, yes/no, and the single
most important fix) and a count by severity. Close with "what's working" so the maker keeps the good
parts. Save it as `redline.md` beside the artifact, or paste it back, as the user prefers.

## Severity-first, not list-first

The most common way a review fails is volume: forty notes of equal weight, the maker fixes the easy ten,
and the blocker is still there. Lead with the verdict and the one fix that matters most. If you could
send only three lines, which three would change whether this screen should ship? Put those first; the
long list supports them, it does not replace them.

## Worked example (condensed)

Screen: a SaaS signup page. Job: get a new visitor to create an account. Primary action: "Create
account." Viewer: first-time visitor on a phone.

```
Verdict: Does not ship yet. The primary action loses to a louder "Learn more" link, and the
password error is unreadable. 1 blocker, 2 major, 3 minor, 2 polish.

[BLOCKER] Color & contrast · Inline password error text
Observation: Error text #E57373 on #FFFFFF measures 2.9:1; AA needs 4.5:1.
Why it matters: The user who most needs the error — one who just failed — is the least likely to read it,
and may abandon signup.
Fix: Darken to #C62828 (5.6:1 on white) and add a non-color cue: a leading "!" icon and bold label.
Verify: Re-run scripts/contrast.py on the pair; confirm >=4.5:1 and the icon shows with color removed.

[MAJOR] Hierarchy & focus · Hero CTA vs. "Learn more"
Observation: "Create account" and "Learn more" are the same size and weight; the link sits above the fold,
the button below it.
Why it matters: On a phone the first tappable thing a visitor sees is the wrong one for the page's job.
Fix: Make "Create account" the only filled, full-width primary button; demote "Learn more" to a text link
below it. Move the button above the fold at 360px.
Verify: 5-second test at 360px — the account button is the first thing a new viewer names.
```

See `references/report-template.md` for the full skeleton and `references/review-lenses.md` for the
complete per-lens checklist.

## Tips

- **Review as the viewer, not as yourself.** You know where everything is; your user does not. The
  five-second test and "first-time user" lens exist to borrow their eyes.
- **Count severities out loud.** If the report has no blockers or majors on a screen the team is worried
  about, re-check hierarchy and states — you may be grading polish on a broken screen.
- **Measure one of everything before you trust your eye:** one gap, one type size, one contrast pair.
  You will usually find the eye was right about *which* was wrong and wrong about *by how much*.
- **Three widths, always.** Most real failures hide at 360px, where desktop layouts fold badly.
- **Separate taste from defect.** "I'd use a serif here" is taste; "the caption fails contrast" is a
  defect. Label taste as optional so the maker can tell a must-fix from a suggestion.
- **End with what's working.** A redline that only cuts makes the maker defensive and strips good
  decisions in the next pass. Name what to keep.
