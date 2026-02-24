Here are the rules, structured as a design system specification:

---

## Typographic Scale Rules for Case Study Pages

### 1. The Scale Must Have a Minimum 5:1 Range

The largest element on any page should be at least 5× the body text size. A 3:1 range (like 48px → 15px) creates no tension — everything reads at the same visual weight. A 5:1 range (82px → 15.5px) creates distinct "voices" on the page.

### 2. Every Step in the Scale Must Have a Job

| Token | Size | Role | When to use |
|---|---|---|---|
| **Display** | clamp(52px, 7vw, 82px) | Hero title — the one moment per page that earns maximum scale | Case study title only. One per overlay. |
| **Section** | clamp(36px, 5vw, 56px) | Resets the reader's eye at each new chapter | Section H2s. Should feel like turning a page. |
| **Statement** | clamp(26px, 3.5vw, 36px) | "Stop and think" beats — shift-quotes, swap words, before/after moments | Sparingly. 2–3 per case study maximum. |
| **Subhead** | 22px | Workmanlike subdivision — clearly smaller than Section, clearly bigger than Body | H3s, functional headings within sections. |
| **Pullquote** | clamp(17px, 2vw, 20px) | Voice of authority between subhead and body | Quoted insights, key findings. |
| **Lead** | clamp(16px, 1.8vw, 19px) | Topic sentence weight — heavier than body, lighter than pullquote | Opening paragraph of a section, thesis statements. |
| **Body** | 15.5px | The reading voice — comfortable, never competes with anything above it | All running paragraphs. |
| **Aside** | 14px | Footnote energy — quieter than body | Supporting details, methodology notes, captions. |
| **Label** | 10.5px, 700 weight, 0.2em tracking, uppercase | Whisper-loud — tiny but typographically heavy | Section numbers (01 / The Problem), kickers, tags. |

**Rule: Skipping a level = intentional emphasis.** Jumping from Body (15.5px) directly to Statement (36px) signals that the content demands attention. Jumping from Label (10.5px) to Display (82px) creates the hero entrance rhythm.

### 3. Use `clamp()` Not Breakpoints for Display Sizes

Any element above 22px should use `clamp(min, preferred, max)` so it scales fluidly with viewport width. Fixed px values at large sizes create jarring jumps at breakpoints. The preferred value (in `vw`) controls how quickly the text shrinks.

- Display: `clamp(52px, 7vw, 82px)` — aggressive scaling
- Section: `clamp(36px, 5vw, 56px)` — moderate scaling
- Statement: `clamp(26px, 3.5vw, 36px)` — gentle scaling
- Below 22px: fixed `px` values are fine — body text shouldn't shift with viewport

### 4. Data as Typography

Numbers that represent findings (perception splits, timeline counts, stat blocks) get their own typographic treatment at the **Statement** tier or above: `clamp(36px, 5vw, 48px)`, weight 900, tight letter-spacing (-0.03em). They should feel like they could be pulled out and put on a poster. Never render data at body text size.

### 5. Dramatic Moments Are Rationed

Each case study gets exactly:
- **1** Display-scale moment (the title)
- **2–3** Statement-scale moments (shift-quote, swap words, final words)
- **Unlimited** Section-scale moments (one per chapter is natural)

If everything is big, nothing is big. The Statement tier is the scarcest resource.

### 6. The Final Section Gets Its Own Budget

The closing section (`.cs2-final`) is a separate typographic context:
- Final words: `clamp(48px, 8vw, 80px)` — nearly Display scale, because this is the second-most memorable moment
- Final quote: `clamp(19px, 2.5vw, 24px)` — Lead-to-Pullquote range, italic
- Vertical padding: 88px — generous but not a full viewport

### 7. Spacing Follows Typography, Not the Other Way Around

Section padding should be roughly 1.3× the section heading size: a 56px H2 gets ~72px section padding. This creates proportional breathing room. The original's 96px padding with a 48px heading created a 2:1 ratio that felt empty. At 72px with 56px, the ratio is ~1.3:1 — the heading fills its space.

### 8. Accent Elements Scale to Their Context

- Swap arrows: 30px (same visual tier as the swap words they connect)
- Inquiry arrows: 28px
- Observation icons: 22px
- Pain list ×: 18px

These should never be larger than the text they annotate.

### 9. Background/Atmosphere Type Lives in Its Own Layer

The `.cs2-bg-word` watermark uses `clamp(140px, 20vw, 240px)` at near-zero opacity (0.022). It should be felt, not read. It never competes with content because it exists on a different perceptual plane — scale alone doesn't create competition, contrast does.

### 10. Mobile Preserves Ratios, Not Absolute Sizes

At ≤900px, every tier drops proportionally:
- Display: 48px (from 82px — ~58% of desktop)
- Section: 36px (from 56px — ~64%)
- Statement: 24px (from 36px — ~67%)
- Swap words: 28px (from 42px — ~67%)
- Final words: 48px (from 80px — ~60%)

The ratio between tiers stays roughly constant. The mistake is dropping everything to the same compressed range on mobile.