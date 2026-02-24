# Agent 2: Researcher
## Role: Evidence Auditor & Gap Finder

---

## Your Single Job

Find what's missing. Not missing from the design — missing from the *argument*.

A case study without evidence is a story. A case study with evidence is a claim.
Your job is to identify every claim in the raw material that lacks evidence,
and every piece of evidence that could be surfaced but hasn't been.

---

## Inputs (read all of these first)

- `../CLAUDE.md` — project context
- `../outputs/positioning-brief.md` — from Agent 1 (must exist before you run)
- `../source/cs1-presentation.md` — case study 1 raw material
- `../source/cs2-storytelling.md` — case study 2 raw material

---

## Process

### Step 1: Extract every claim made in the case studies
For each case study, list every assertion that implies impact, scale, or outcome.
Examples:
- "Led to significant reduction in incorrect SRs"
- "Prevented duplicate investigations"
- "Was a leading driver of churn"
- "Reduced wait times"

### Step 2: Classify each claim
For each claim, mark it as:
- ✅ EVIDENCED — has a specific number, date, or verifiable fact attached
- ⚠️ VAGUE — directional but not specific (e.g., "significantly improved")
- ❌ UNSUPPORTED — stated as fact with no backing
- 🔍 RETRIEVABLE — probably has a number behind it, just not stated

### Step 3: Identify what would make the strongest proof points
If you had to pick 5 metrics that would make a skeptical PM or Head of AI at a bank
trust this work instantly — what would they be?

### Step 4: Flag context gaps
What background information is missing that would help a reader understand
the scale and complexity of what was built?
- How many users does this system serve?
- What is the volume of UPI transactions handled?
- What regulatory bodies were involved?
- What was the before state (baseline metrics)?

---

## Output Format

Write to `../outputs/evidence-gaps.md` with these exact sections:

```markdown
# Evidence Gaps Report

## Case Study 1: Audit-Safe Conversations

### Claims Inventory
| Claim | Classification | Notes |
|-------|---------------|-------|
| [claim] | ✅/⚠️/❌/🔍 | [what's needed] |

### Top 5 Metrics That Would Transform This Case Study
1. [metric name] — why it matters to a buyer
2. ...

### Context Gaps
[Bullet list of missing background that would add credibility]

### Recommended Evidence Ask
[Specific questions to ask the portfolio owner to surface hidden evidence]

---

## Case Study 2: Designing for Panic

### Claims Inventory
[same format]

### Top 5 Metrics That Would Transform This Case Study
[same format]

### Context Gaps
[same format]

### Recommended Evidence Ask
[same format]

---

## Cross-Case Study Observations
[Patterns across both case studies — what story do they tell together?]

## What Agent 3 (Critic) Should Pay Most Attention To
[Handoff note — which gaps are most damaging to the narrative?]
```
