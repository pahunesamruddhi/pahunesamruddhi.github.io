# Portfolio Builder — Multi-Agent System
## Project: Samruddhi Pahune · AI Systems Designer Portfolio

---

## What This System Does

Five specialised agents collaborate to rebuild a portfolio from scratch.
Each agent has a single job. Each agent's output feeds the next.
No agent skips ahead. No agent does another agent's job.

---

## Agent Pipeline (run in order)

```
[1] strategist    → positioning-brief.md
[2] researcher    → evidence-gaps.md
[3] critic        → case-study-audit.md
[4] narrator      → final-copy.md
[5] designer      → index.html
```

---

## Positioning (never deviate from this)

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

## Source Material

- `source/existing-site-content.md` — scraped content from current portfolio
- `source/cs1-presentation.md` — Audit-Safe Conversations case study raw content
- `source/cs2-storytelling.md` — Designing for Panic storytelling brief
- `source/reference-image.jpg` — visual reference (Shaban Iddrisu site)

---

## Output Files (agents write here)

- `outputs/positioning-brief.md` — from Agent 1
- `outputs/evidence-gaps.md` — from Agent 2
- `outputs/case-study-audit.md` — from Agent 3
- `outputs/final-copy.md` — from Agent 4
- `outputs/index.html` — from Agent 5 (final deliverable)

---

## Rules All Agents Must Follow

1. Read your input files completely before writing output
2. Write to your designated output file only
3. Do not invent metrics — flag gaps instead
4. Positioning section above is immutable — do not rewrite it
5. The final site must NOT just transplant positioning sections as headers — it must embody the positioning in structure and tone
