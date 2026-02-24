# Conversation Retrospective — Portfolio Homepage Refinement

---

## 1. Pattern Recognition

### Pattern A: Logo Sizing Ping-Pong (5 rounds)
| Round | Request | Outcome |
|-------|---------|---------|
| 1 | "logo twice as big" | Applied (18px → 48px). Kept. |
| 2 | "Make the square.png twice its current size" | Redundant — already doubled. No-op. |
| 3 | "don't double the logo height, reload square.png" | User thought the image file was modified. It wasn't. |
| 4 | "reduce to 60% current size" | Applied (0.6 multiplier). **Undone by user.** |
| 5 | "reduce by 10%" | Applied (0.54 multiplier). **Undone by user.** |

**What I had to repeat:** Logo size intent was expressed 5 times without ever specifying a target pixel value.

### Pattern B: Width vs Height Misstatement (1 undo + correction)
| Round | Said | Meant |
|-------|------|-------|
| 1 | "same **width** as resume" | Claude made blog span all 5 columns. **Undone.** |
| 2 | "same **height** as resume" | Already true (both in 48px row). Minimal change needed. |

### Pattern C: Incremental Spec Delivery (5+ messages for one feature set)
Homepage redesign was spread across separate messages:
1. Sticky header + 2× logo + cards above fold + card text + remove footer
2. No-scroll + case study sticky header + contact/resume links + logo height
3. Logo size adjustments (×3)
4. Blog → Behavioral Design rename + Instagram link
5. Remove case study inner nav

Each message added constraints that affected already-completed work.

### Pattern D: Git Confusion (untracked file)
User asked to "reload all files from GitHub strictly." `git reset --hard origin/main` ran, but `outputs/index.html` was **never committed** and remained unchanged. Two more messages spent clarifying why.

### Pattern E: Compound Requests with Mixed Atomicity
Messages bundled 3–5 changes. When one change was wrong, the user had to undo ALL changes in the message, losing the correct ones too.

---

## 2. Root Cause Analysis

| Pattern | Root Cause | Category |
|---------|-----------|----------|
| **Logo ping-pong** | No absolute target size; relative adjustments stack unpredictably. No preview mechanism. | Underspecified constraint |
| **Width/height** | Typo in request. Claude correctly interpreted the literal word. | Ambiguous language |
| **Incremental spec** | User discovering requirements as they see results. Normal for visual work but expensive with wholesale AI edits. | Iterative discovery |
| **Git confusion** | User assumed all workspace files were tracked. Claude didn't proactively warn. | Missing context |
| **Compound requests** | Multiple independent changes in one message eliminate selective undo. | Workflow mismatch |

---

## 3. Improved Initial Prompt

### BEFORE (reconstructed from actual messages across the session)
> I need the header to be sticky... logo twice as big... cards above the fold... remove the footer...
>
> Make it so there is no scrolling... sticky header for case studies too... add this contact link... add this resume link... logo height matches header...
>
> Make the writing section same width as resume, rename it to Behavioral Design...
>
> Remove the case study inner nav...
>
> reduce the size of the current square.png to 60%... no wait, 10%...

### AFTER (single optimized prompt)

```markdown
## Homepage & Global Navigation Redesign

### Header (global — homepage + all case study overlays)
- `position: fixed`, always above content, never scrolls away
- Logo: `square.png` at **28px height**, auto width (preserve aspect ratio)
- Right side links only:
  - "Contact" → https://mail.google.com/mail/u/0/?fs=1&tf=cm&source=mailto&su=Let%27s+Connect&to=pahunesamruddhi@gmail.com (target _blank)
  - "Resume" → https://drive.google.com/file/d/1ddNeOfB12lvKfKnd0p1swr2TlEX51NjY/view?usp=sharing (target _blank)

### Homepage Grid
- **Zero vertical scroll.** Grid must fit `100vh` minus header. Use `fr` units.
- Keep grid positions, animations, colors, hover states unchanged.
- **Update card text** (copy below).
- **Rename "Writing" card** → label: "Instagram", title: "Behavioral Design"
  - Link: https://www.instagram.com/decisions_by_design/...
  - Horizontal strip layout matching resume (48px row height)
- **Remove footer** entirely (HTML + CSS + JS).

### Case Study Overlays
- **Remove inner case-study-nav** from all 6 overlays
- Overlay `top` starts below main header; main nav z-index stays above overlay

### Card Copy
1. UPI: "01 · Behavior Design · Banking AI" / "5-gate diagnostic engine..." / "Decision Boundaries"
2. SmartCoin: "02 · Fintech · Behavioral Systems" / "Restructured product behavior..." / "Product Behavior · Fintech"
3. Dottie: "03 · Voice AI · Speculative" / "Voice personality system..." / "AI Behavior Design"
4. ICICI: "04 · Production · Banking AI" / "70+ live transactional flows..." / "AI Systems · Production"
5. Vihar: "05 · Service Systems" / "80% of visitors missed key zones..." / "Systems Thinking"
6. Bhopal: "06 · Adoption Systems" / "500 bikes, 3% adoption..." / "Service Strategy"

### Constraints
- Do NOT modify: grid layout, card animations, card colors, hover effects
- Do NOT modify: case study content within overlays
- Do NOT change image sources or load external images
```

**Estimated reduction:** 10+ messages → 1–2.

---

## 4. CLAUDE.md Recommendations

Add this section to the existing CLAUDE.md:

```markdown
## Session Preferences — Visual Editing

### Sizing
- Always ask for **absolute pixel values** when the user requests size changes.
  If they say "make it bigger," respond: "What target height in pixels?"
- Never apply relative size changes (%, "twice", "half") without confirming
  the computed result first.

### Edit Granularity
- When a message contains 3+ independent changes, apply them as **separate
  atomic edits** (one replace per logical change) so the user can undo
  selectively.
- After each visual change, state the computed pixel/rem values so the user
  can validate without inspecting CSS.

### File Tracking
- `outputs/index.html` is NOT git-tracked. It is the working build artifact.
- Before any `git reset`, warn the user which files are untracked and will
  NOT be affected.
- The canonical deployed version lives in `docs/index.html`.

### Case Studies
- There are 6 case study overlays: cs2, cs-smartcoin, cs-dottie, cs-icici,
  cs-vihar, cs-bhopal
- Each overlay is a `position: fixed` div with `overflow-y: auto`
- The main `.nav` should always remain visible above overlays (z-index: 100 > overlay z-index)

### CSS Architecture
- Homepage grid: `.bento-page` > `.bento-grid` (5-column, 4-row)
- Header: `.nav` → `.nav-inner` (52px height) → `.nav-logo` + `.nav-links`
- Card structure: `.b-proj-num`, `.b-proj-name`, `.b-proj-desc`, `.b-proj-cat`
- Blog strip: `.b-blog-c` with `::after` wipe animation
- Resume strip: `.b-resume` (orange, horizontal)

### Visual Design Guide
- Always reference `visual-design-guide.md` for typographic tokens
- Typographic scale: Display → Section → Statement → Lead → Body → Aside
- All sizing uses `clamp()` for responsive scaling

### What NOT to Change (unless explicitly asked)
- Grid template areas / column ratios
- Card animations (b-breathe keyframes)
- Color palette (#0a0a0a, #FF5500, #ececec, #f5f5f5)
- Hover state behavior (wipe-up reveal, glow, pause animation)
```

---

## 5. Planning Template

```markdown
# Visual Change Request — Planning Brief

## Change Summary
<!-- One sentence: what is the end state? -->

## Scope
- [ ] Header / Navigation
- [ ] Homepage grid (layout)
- [ ] Homepage grid (content/text)
- [ ] Case study overlays
- [ ] CSS only (no HTML changes)
- [ ] JavaScript changes needed

## Exact Specifications
<!-- For EVERY visual property, provide absolute values -->
| Element | Property | Current Value | Target Value |
|---------|----------|---------------|--------------|
| .nav-logo img | height | 42px | 28px |
| .bento-page | padding-top | 64px | 62px |

## Links & URLs
| Label | URL | target |
|-------|-----|--------|
| Contact | https://... | _blank |

## Text Content Changes
<!-- Provide exact strings with HTML entities -->
| Card | proj-num | proj-desc | proj-cat |
|------|----------|-----------|----------|
| UPI | "01 · Behavior Design" | "5-gate diagnostic..." | "Decision Boundaries" |

## Constraints (do NOT touch)
<!-- List everything that must remain unchanged -->
- [ ] Grid layout
- [ ] Animations
- [ ] Colors
- [ ] Hover states
- [ ] Case study content

## Acceptance Criteria
- [ ] No vertical scroll on homepage (100vh)
- [ ] Header visible on all pages
- [ ] All links open in new tab

## Files Affected
<!-- List expected files so Claude can validate scope -->
- outputs/index.html (lines ~XX–YY)
```

---

## 6. Sub-Agent / Skill Breakdown

For this category of task (visual refinement of a built HTML file), the work splits into 3 specialized roles:

### Agent 1: Layout Architect
**Trigger:** Grid structure, overflow, viewport fitting, responsive breakpoints

**Prompt:**
> You are a CSS grid specialist. Given the current `.bento-grid` definition (5-col, 4-row), modify ONLY the grid-template-rows and container sizing to ensure zero vertical scroll within 100vh. Do not change grid-template-areas, column ratios, gap, or any card-internal styles. Output only the CSS changes needed.

### Agent 2: Content Updater
**Trigger:** Card text, link URLs, labels, aria attributes

**Prompt:**
> You are a content replacement agent. Given a mapping of card identifiers to new copy (proj-num, proj-desc, proj-cat), find and replace each card's text content in the HTML. Do not modify any CSS, JavaScript, or structural HTML. Do not change class names. Output the exact string replacements.

### Agent 3: Navigation Architect
**Trigger:** Header behavior, overlay z-index stacking, sticky positioning, link targets

**Prompt:**
> You are a navigation specialist. Make the `.nav` header persistent across the homepage and all 6 case study overlays. The overlays must render below the header (top offset = header height). Remove any inner `.case-study-nav` elements from overlays. Ensure z-index stacking: nav (100) > overlay (90). Output CSS and HTML changes.

### Reviewer Agent
**Workflow:** Run agents 1–3 in parallel (independent changes), then validate:

**Prompt:**
> Verify: (1) no vertical scroll on homepage, (2) all 6 overlays open below the header, (3) all card text matches the provided copy, (4) no broken HTML tags. Report pass/fail for each.

---

## 7. One-Page Best Practices

### 7 Principles for Prompting Claude on Visual HTML Tasks

1. **Specify absolute values, not relative.**
   Say "28px" not "twice as big." Relative adjustments compound unpredictably across rounds, and you can't preview the result before Claude applies it.

2. **One logical change per undo boundary.**
   If you need 5 changes, either send them as separate messages or explicitly ask Claude to apply them as atomic edits. Bundled changes = all-or-nothing undo.

3. **State constraints upfront, not after the first mistake.**
   "Do NOT change grid layout, animations, or colors" in the first message prevents a rework cycle. Constraints discovered through undo cost 2× the tokens.

4. **Provide exact copy in a structured table.**
   Free-text descriptions of card content lead to interpretation errors. A simple table (card → field → exact string) eliminates ambiguity.

5. **Declare the viewport contract early.**
   "No scroll" / "above the fold" / "100vh" should be the FIRST constraint, not discovered after the layout is built. It determines every sizing decision downstream.

6. **Know your git state.**
   If the working file is untracked, `git reset` won't help. Check `git status` before asking Claude to "reload from GitHub." Claude should warn, but you should know.

7. **Use the planning template for anything touching 3+ CSS rules.**
   The 2 minutes spent filling out the spec table saves 20 minutes of back-and-forth. Visual work is specification-heavy — the prompt IS the spec.
