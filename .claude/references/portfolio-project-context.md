# Portfolio Project Context

Quick-access reference for Claude Code sessions editing this portfolio. Consolidates information from `/portfolio-agents/` so you don't need to read multiple files.

---

## Positioning Statement

**Who:** Samruddhi Pahune — AI Systems & Automation Behavior Owner (Fintech)

**Tagline:** "I build automation that knows when to stop."

**Three Pillars:**
1. **Behavior Ownership** — AI systems must know when to act, when to ask, when to stop
2. **Risk-Aware Automation** — compliance alignment and escalation discipline before UX
3. **Measurable Outcomes** — containment rate, fallback reduction, resolution time

**What she owns:**
- Decision boundaries and intent eligibility
- Confidence thresholds and fallback logic
- Escalation policies for high-risk scenarios
- Containment, resolution time, and failure categories
- Collaboration with engineering and data science on model outcomes

---

## Tone Rules

- **Tone:** Consulting deck meets product spec. Structured. Calm. Precise. Editorial.
- **Anti-tone:** No UX portfolio vibes. No playful microcopy. No cute illustrations.
- The final site must NOT just transplant positioning sections as headers — it must embody the positioning in structure and tone.
- Do not invent metrics — flag gaps instead.
- Positioning is immutable — never rewrite the tagline, pillars, or tone.

---

## CSS Design Tokens

### Colors
| Token | Value | Usage |
|-------|-------|-------|
| `--color-bg` | `#ffffff` | Page background |
| `--color-bg-alt` | `#fafafa` | Alternate section background |
| `--color-text` | `#1a1a1a` | Primary text |
| `--color-text-muted` | `#666666` | Secondary/muted text |
| `--color-accent` | `#6366f1` | Accent (indigo) — links, CTAs, labels |
| `--color-accent-hover` | `#4f46e5` | Accent hover state |
| `--color-border` | `#e5e5e5` | Borders and dividers |

### Typography
| Property | Value |
|----------|-------|
| Font family | `'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` |
| Mono font | `'DM Mono'` (loaded via Google Fonts) |
| Body size | 17px desktop / 16px mobile |
| Line height | 1.6 (body), 1.2 (headings) |
| H1 | 42px / 30px mobile |
| H2 | 30px / 24px mobile |
| H3 | 24px / 20px mobile |
| H4 | 19px / 17px mobile |
| Hero headline | 56px / 38px mobile |

### Spacing
| Token | Value |
|-------|-------|
| `--spacing-xs` | 8px |
| `--spacing-sm` | 16px |
| `--spacing-md` | 24px |
| `--spacing-lg` | 32px |
| `--spacing-xl` | 48px |
| `--spacing-2xl` | 64px |
| `--spacing-3xl` | 64px |

### Layout
| Token | Value |
|-------|-------|
| `--border-radius` | 8px |
| `--max-width` | 1200px |
| `--max-width-wide` | 1400px |
| `--shadow-sm` | `0 2px 8px rgba(0, 0, 0, 0.08)` |
| `--shadow-md` | `0 4px 16px rgba(0, 0, 0, 0.12)` |

---

## Typographic Scale (Case Studies)

From `visual-design-guide.md`. Minimum 5:1 range between largest and smallest elements.

| Token | Size | Role | Usage |
|-------|------|------|-------|
| **Display** | `clamp(52px, 7vw, 82px)` | Hero title | One per overlay |
| **Section** | `clamp(36px, 5vw, 56px)` | Chapter resets | H2s in case studies |
| **Statement** | `clamp(26px, 3.5vw, 36px)` | "Stop and think" beats | 2-3 per case study max |
| **Subhead** | 22px | Functional headings | H3s within sections |
| **Pullquote** | `clamp(17px, 2vw, 20px)` | Voice of authority | Key findings, quotes |
| **Lead** | `clamp(16px, 1.8vw, 19px)` | Topic sentence weight | Opening paragraphs |
| **Body** | 15.5px | Reading voice | Running paragraphs |
| **Aside** | 14px | Footnote energy | Captions, methodology |
| **Label** | 10.5px, 700, 0.2em tracking, uppercase | Whisper-loud | Section numbers, kickers |

**Key rules:**
- Skipping a level = intentional emphasis
- Use `clamp()` for anything above 22px; fixed px below 22px
- Data numbers get Statement tier or above, weight 900, -0.03em tracking
- Each case study: 1 Display, 2-3 Statement, unlimited Section moments
- Section padding = ~1.3x section heading size
- Mobile preserves ratios (58-67% of desktop), not absolute sizes

---

## Image Directories

All images live under `docs/Images/`:

| Directory | Content |
|-----------|---------|
| `Images/Bhopal by Bike/` | Bhopal by Bike project images |
| `Images/Dottie/` | Dottie project images |
| `Images/Smartcoin/` | Smartcoin project images |
| `Images/Vihar/` | Vihar project images |

Total: ~95 files, ~24MB. All paths are relative from `docs/index.html`.

---

## Key File Paths

| File | Purpose |
|------|---------|
| `docs/index.html` | The entire site — edit this |
| `docs/Images/` | All site images |
| `portfolio-agents/CLAUDE.md` | Positioning source of truth |
| `portfolio-agents/visual-design-guide.md` | Typographic scale specification |
| `portfolio-agents/agents/01-strategist.md` | Agent 1 prompt |
| `portfolio-agents/agents/05-designer.md` | Agent 5 prompt (HTML generator) |
| `portfolio-agents/scripts/run-all.sh` | Pipeline runner |
| `CLAUDE.md` | Project configuration for Claude Code |
