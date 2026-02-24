# Samruddhi Pahune — Portfolio Site

## Project Overview

Static HTML/CSS/JS portfolio for **Samruddhi Pahune** — AI Systems & Automation Behavior Owner (Fintech). Deployed via GitHub Pages from the `/docs/` directory.

- **Zero dependencies** — no npm, no build tools, no frameworks
- **Single monolithic page** — `docs/index.html` (~5,354 lines) with inline CSS + JS
- **GitHub Pages** — `main` branch → `/docs/` folder auto-deploys

---

## File Structure

```
pahunesamruddhi.github.io/
├── CLAUDE.md                      ← You are here
├── docs/                          ← LIVE SITE (GitHub Pages root)
│   ├── index.html                 ← The entire site (HTML + CSS + JS inline)
│   ├── Images/                    ← All site images (~95 files, ~24MB)
│   │   ├── Bhopal by Bike/
│   │   ├── Dottie/
│   │   ├── Smartcoin/
│   │   └── Vihar/
│   ├── Content/                   ← Static content assets
│   └── source/                    ← Source reference files
├── portfolio-agents/              ← Content generation pipeline (read-only reference)
│   ├── CLAUDE.md                  ← Pipeline config + positioning statement
│   ├── visual-design-guide.md     ← Typographic scale rules
│   ├── agents/                    ← 5 agent prompts (01-strategist → 05-designer)
│   ├── scripts/                   ← run-all.sh, setup-sources.sh, utilities
│   └── outputs/                   ← Generated content from agent pipeline
└── .claude/
    ├── agents/                    ← 7 local agents for this project
    ├── skills/                    ← 9 local skills for this project
    └── references/                ← Project context reference
```

---

## Deployment Workflow

1. Edit `docs/index.html` (or assets in `docs/Images/`, `docs/Content/`)
2. Test locally — open `docs/index.html` in a browser
3. `git add` + `git commit` + `git push origin main`
4. GitHub Pages auto-deploys from `/docs/`

No build step. No CI/CD pipeline. Push = deploy.

---

## Agent Content Pipeline

The `/portfolio-agents/` directory contains a 5-agent content pipeline run via `run-all.sh`. Each agent is a Claude prompt executed with `claude --print`:

| Agent | File | Output | Job |
|-------|------|--------|-----|
| 1. Strategist | `agents/01-strategist.md` | `positioning-brief.md` | Define positioning |
| 2. Researcher | `agents/02-researcher.md` | `evidence-gaps.md` | Flag evidence gaps |
| 3. Critic | `agents/03-critic.md` | `case-study-audit.md` | Audit case studies |
| 4. Narrator | `agents/04-narrator.md` | `final-copy.md` | Write final copy |
| 5. Designer | `agents/05-designer.md` | `index.html` | Build HTML site |

These agents are standalone prompts, NOT Claude Code agents. They stay as-is.

---

## Positioning (Immutable)

**Who:** Samruddhi Pahune — AI Systems & Automation Behavior Owner (Fintech)

**What she owns:**
- Decision boundaries and intent eligibility
- Confidence thresholds and fallback logic
- Escalation policies for high-risk scenarios
- Containment, resolution time, and failure categories
- Collaboration with engineering and data science on model outcomes

**Positioning statement:**
> "I build automation that knows when to stop."

**Three pillars:**
1. Behavior Ownership — AI systems must know when to act, when to ask, when to stop
2. Risk-Aware Automation — compliance alignment and escalation discipline before UX
3. Measurable Outcomes — containment rate, fallback reduction, resolution time

**Tone:** Consulting deck meets product spec. Structured. Calm. Precise. Editorial.
**Anti-tone:** No UX portfolio vibes. No playful microcopy. No cute illustrations.

---

## Design System

### Colors (CSS Custom Properties)
```
--color-bg:           #ffffff
--color-bg-alt:       #fafafa
--color-text:         #1a1a1a
--color-text-muted:   #666666
--color-accent:       #6366f1  (indigo)
--color-accent-hover: #4f46e5
--color-border:       #e5e5e5
```

### Typography
- **Font:** Inter (sans-serif), with system stack fallback
- **Body:** 17px / 1.6 line-height (16px on mobile)
- **H1:** 42px (30px mobile) | **H2:** 30px (24px mobile) | **H3:** 24px (20px mobile)
- **Hero headline:** 56px (38px mobile)
- **Section labels:** 14px uppercase, 500 weight, 0.1em tracking

### Case Study Typographic Scale (from visual-design-guide.md)
| Token | Size | Role |
|-------|------|------|
| Display | clamp(52px, 7vw, 82px) | Hero title — one per overlay |
| Section | clamp(36px, 5vw, 56px) | H2s — resets the reader's eye |
| Statement | clamp(26px, 3.5vw, 36px) | Shift-quotes — 2-3 per case study max |
| Subhead | 22px | H3s, functional headings |
| Pullquote | clamp(17px, 2vw, 20px) | Quoted insights |
| Lead | clamp(16px, 1.8vw, 19px) | Opening paragraphs |
| Body | 15.5px | Running paragraphs |
| Aside | 14px | Footnotes, captions |
| Label | 10.5px, 700, 0.2em tracking, uppercase | Section numbers, kickers |

### Spacing Tokens
```
--spacing-xs:  8px    --spacing-sm:  16px   --spacing-md:  24px
--spacing-lg:  32px   --spacing-xl:  48px   --spacing-2xl: 64px
--spacing-3xl: 64px
```

### Layout
```
--border-radius:  8px
--max-width:      1200px
--max-width-wide: 1400px
--shadow-sm:      0 2px 8px rgba(0, 0, 0, 0.08)
--shadow-md:      0 4px 16px rgba(0, 0, 0, 0.12)
```

---

## JavaScript Features

All JS is inline at the bottom of `index.html`. Key systems:

| Feature | Description |
|---------|-------------|
| **Bento cursor glow + 3D tilt** | Mouse-tracking gradient + perspective tilt on bento cards |
| **Case study overlays** | Full-screen overlays opened via `openCaseStudy(id)` / `closeCaseStudy(id)` |
| **Headline word-split reveal** | Per-word cascade animation on hero headline |
| **Nav auto-hide** | Hides nav on scroll down, reveals on scroll up |
| **Reading progress bars** | Injected into case study sticky navs |
| **Scroll reveals** | IntersectionObserver-based reveals inside overlays (pullquotes, images, personas, final quotes) |
| **Stat count-ups** | Animated number counting for `.cs2-perception-big` and `.cs2-tl-time` elements |
| **Expandable sections** | Accordion-style expand/collapse via `toggleExpandable()` |
| **Smooth scroll** | Anchor link smooth scrolling |
| **Reduced motion** | All animations respect `prefers-reduced-motion: reduce` |
| **Keyboard nav** | Case study cards, blog cards support Enter/Space activation; ESC closes overlays |

---

## Local Agents (Auto-Delegate)

7 agents are defined locally in `.claude/agents/`. When a task matches the patterns below, **delegate to the agent automatically** — do not answer directly.

| Task Pattern | Agent | File |
|-------------|-------|------|
| HTML structure, CSS styling, JS features, responsive layout, bento grid, overlay system, inline code changes | `frontend-developer` | `.claude/agents/frontend-developer.md` |
| Visual design, color palette, typography, component aesthetics, spacing, layout composition | `ui-designer` | `.claude/agents/ui-designer.md` |
| Meta tags, OG tags, structured data, sitemap, search rankings, keyword optimization | `seo-specialist` | `.claude/agents/seo-specialist.md` |
| WCAG, ARIA, contrast, keyboard nav, screen reader, a11y | `accessibility-auditor` | `.claude/agents/accessibility-auditor.md` |
| Image compression, page speed, lazy loading, Core Web Vitals | `performance-optimizer` | `.claude/agents/performance-optimizer.md` |
| GSAP, scroll animations, transitions, micro-interactions, motion | `motion-designer` | `.claude/agents/motion-designer.md` |
| Code review, code quality, best practices | `code-reviewer` | `.claude/agents/code-reviewer.md` |

---

## Local Skills

| Skill | Trigger |
|-------|---------|
| `/lighthouse-audit` | Lighthouse audit, performance score, site audit |
| `/asset-optimizer` | Optimize images, compress assets, convert to WebP |
| `/seo-checklist` | SEO audit, meta tag review, search optimization |
| `/accessibility-check` | Accessibility audit, WCAG check, a11y review |
| `/browser-testing` | Browser testing, cross-browser check, responsive testing |
| `/favicon-og-generator` | Favicon setup, OG image, social sharing images |
| `/website-launch-checklist` | Launch checklist, pre-launch check, go-live validation |
| `/frontend-design` | Build web components, pages, UI design |
| `/design-token-extractor` | Extract design tokens, create design variables |

---

## Project Rules

1. **No npm, no node_modules, no package.json.** This is a zero-dependency static site.
2. **No frameworks.** No React, Vue, Tailwind, or any CSS/JS framework.
3. **Do not split the monolith.** All HTML, CSS, and JS live in `docs/index.html`. Do not extract into separate files unless explicitly asked.
4. **Do not modify `/portfolio-agents/` contents.** That pipeline is reference material and standalone tooling.
5. **All image paths are relative** from `docs/index.html` (e.g., `Images/Dottie/hero.webp`).
6. **Preserve the positioning.** The tagline, three pillars, and tone rules in the Positioning section above are immutable. Never rewrite them.
7. **Respect `prefers-reduced-motion`.** All animations must check for reduced motion preference.
8. **Keyboard accessibility.** All interactive elements must be keyboard-navigable (Tab, Enter, Space, Escape).
9. **Test at 320px minimum.** The site must work on iPhone SE width.
10. **Use CSS custom properties** for any new colors, spacing, or layout values. Never hardcode.
11. **Inline everything.** New CSS goes in the `<style>` block; new JS goes in the `<script>` block. Both inside `index.html`.
12. **Images in WebP/AVIF.** All new images should be in modern formats with explicit width/height attributes.
