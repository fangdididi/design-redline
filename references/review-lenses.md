# The ten review lenses — full checklist

Use this as the detailed companion to Step 4 of SKILL.md. For each lens, the questions are ordered
roughly by severity: a "no" near the top is usually a blocker or major, a "no" near the bottom is
minor or polish. You do not have to answer every question on every screen — skip what does not apply —
but read the list so you do not miss a class of problem.

## 1. Hierarchy & focus
- Does the eye land on the primary action first, unprompted?
- Is there exactly one focal point per view? (If three things are equally loud, there is none.)
- Do secondary and tertiary actions clearly read as lower priority?
- Is the most important information also the most prominent, or is a label louder than the data?
- Does size, weight, color, and position agree about what matters, or do they fight?

## 2. Layout & alignment
- Do elements align to a shared grid and shared edges, or drift by a few pixels?
- Are related items grouped (proximity) and unrelated items separated?
- Is there one clear reading path (usually top-down, left-right), not a scavenger hunt?
- Is the content width comfortable, or does a line of text run the full width of a wide screen?
- Are optical alignments handled (icons, round shapes, and punctuation often need nudging)?

## 3. Spacing & rhythm
- Is spacing drawn from a scale (4/8/12/16/24/32/48...) or are the gaps arbitrary?
- Is space *inside* a group tighter than space *between* groups? (If not, grouping reads wrong.)
- Are any controls cramped to the point of being hard to tap or read?
- Are any elements stranded by too much space, looking unrelated to their group?
- Is vertical rhythm consistent down the page, or does every section invent its own gaps?

## 4. Typography
- Is there a real type scale (a handful of deliberate sizes), or many near-duplicate sizes?
- Body line length 45-75 characters? Line height ~1.4-1.6 for body?
- Are headings clearly distinct from body, and distinct from each other by level?
- One or two typeface families with clear jobs, not three competing?
- In tables and figures, are numerals aligned (tabular) and decimals lined up?
- Is anything set in all-caps for long runs (hard to read) or justified with rivers of space?

## 5. Color & contrast
- Does every text/background pair meet WCAG AA? (Run `scripts/contrast.py`.)
- Do UI components, icons, input borders, and focus rings meet 3:1 against adjacent colors?
- Is there one accent color that reliably means "act here," or is accent sprinkled decoratively?
- Is color ever the *only* cue for a link, an error, a required field, or a state? (Fails colorblind users.)
- Is the palette coherent across the whole screen, including charts and illustrations?
- In dark mode (if present), are all pairs re-checked? Contrast does not carry over automatically.

## 6. States & edge cases
The usual home of "it looks unfinished." Check each that applies:
- **Hover** — clear but not distracting; does not shift layout.
- **Focus** — a visible focus indicator, 3:1 contrast, for keyboard users.
- **Active / pressed** — immediate feedback on tap/click.
- **Disabled** — visibly inactive, and ideally says why it is disabled.
- **Loading** — a skeleton or spinner, not a frozen or blank screen; no layout jump when data lands.
- **Empty** — a first-use / zero-items state that guides, not a blank box.
- **Error** — what went wrong and what to do next, near the thing that failed.
- **Success** — confirmation the action worked.
- **Overflow / extremes** — longest realistic string, zero items, thousands of items, tiny and huge numbers.

## 7. Motion & feedback
- Does every user action produce feedback within ~100ms?
- Are transitions short (~150-300ms) and purposeful, or decorative and slow?
- Does anything animate that should stay still, pulling attention from the task?
- Is `prefers-reduced-motion` respected for users who need it?
- Do loading and progress states communicate real progress, not fake motion?

## 8. Copy & microcopy
- Are button labels specific verbs ("Save changes", "Delete file") not generic ("OK", "Submit")?
- Do error messages name the cause and the next step, in plain language?
- Is the voice consistent (formality, person, tense) across the screen?
- Is there jargon or internal terminology the Step 1 viewer would not know?
- Are empty states and tooltips doing real work, or filled with filler?
- Is text concise — can any sentence lose words without losing meaning?

## 9. Accessibility (beyond contrast)
- Touch targets ~44x44px minimum, with enough spacing between them?
- Is everything reachable and operable by keyboard, with a logical focus order?
- Is the focus indicator always visible (never `outline: none` with no replacement)?
- Do meaningful images have alt text, and decorative ones have empty alt?
- Are form inputs tied to visible labels (not placeholder-as-label)?
- Are headings in order (h1 -> h2 -> h3), forming a real outline?
- Does the layout survive 200% browser zoom / text resize without loss of content?
- Is motion, autoplay, and timeout behavior controllable?

## 10. Responsiveness
Check at 360px, 768px, and 1280px at minimum:
- Does anything overflow horizontally or get clipped?
- Does text truncate in a way that loses meaning?
- Do multi-column layouts collapse into a sensible single column, not a jumble?
- Does the primary action stay visible and reachable at the smallest width?
- Are tap targets still large enough and well-spaced on the phone width?
- Do images and media scale without distortion or huge downloads on mobile?
