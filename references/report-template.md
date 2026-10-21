# Redline report template

Copy this skeleton into `redline.md` and fill it in. Delete bracketed guidance as you go.
Keep the verdict and severity count at the very top — they are the part most people read.

---

# Redline — [screen / component name]

**Reviewed:** [date] · **Form:** [live URL | screenshot | mock] · **Widths checked:** [360 / 768 / 1280]
**Job of this screen:** [one line] · **Primary action:** [one line] · **Reviewed as:** [the viewer]

> If reviewed from a screenshot only, state here that state and responsive findings are inferred, not confirmed.

## Verdict
[Does this screen do its job today — yes / no / not yet. Then the single most important fix in one line.]

## Severity count
- Blocker: [n]
- Major: [n]
- Minor: [n]
- Polish: [n]

## Top 3 (if you fix nothing else)
1. [most important]
2. [...]
3. [...]

---

## Issues
List in order: all blockers, then majors, then minors, then polish. Within a severity, closest to the
primary action first. One block per issue:

### [BLOCKER] Lens · Location
- **Observation:** [what is there, measured when possible]
- **Why it matters:** [cost to the viewer and primary action, one sentence]
- **Fix:** [the specific change — values, not adjectives]
- **Verify:** [how to confirm it is fixed]

### [MAJOR] Lens · Location
- **Observation:**
- **Why it matters:**
- **Fix:**
- **Verify:**

[...continue for every issue...]

---

## What's working
[Name the good decisions worth keeping, so the next pass does not strip them. Three to five bullets.]

## Optional / taste
[Suggestions that are preference, not defects. Clearly labeled so the maker can tell a must-fix from a
nice-to-have.]
