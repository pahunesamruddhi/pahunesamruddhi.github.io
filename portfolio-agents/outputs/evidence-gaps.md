# Evidence Gaps Report

## Case Study 1: Audit-Safe Conversations

### Claims Inventory

| Claim | Classification | Notes |
|-------|---------------|-------|
| "Mismanaged disputes can lead to significant financial losses for banks" | ⚠️ VAGUE | No baseline loss quantified, no "after" state |
| "Zero incorrect SR creation" | 🔍 RETRIEVABLE | Stated as design constraint, but was this outcome achieved? Need: incorrect SR rate before/after |
| "Preventing stale consent" | 🔍 RETRIEVABLE | Mentioned as design goal, but: how many stale consent incidents prevented? Baseline rate? |
| "Reduces interpretation risk" (UI elements) | ⚠️ VAGUE | No measure of misinterpretation before vs. after |
| "Minimize ambiguous free-text responses" | ⚠️ VAGUE | By how much? Need: % reduction in clarification loops or agent escalations |
| "Avoids asking for UTR upfront" (reduces entry errors) | 🔍 RETRIEVABLE | Implied usability win, but: error rate with vs. without? Completion rate comparison? |
| "Prevents bot from acting on outdated confirmations" (session timeout) | ⚠️ VAGUE | How many prevented? What was the risk baseline? |
| "Ensures escalation is explicit, user-driven" | ❌ UNSUPPORTED | No measure of success: escalation appropriateness rate? User satisfaction? |
| "Reduces dropoffs vs open-ended questions" (quick reply buttons) | 🔍 RETRIEVABLE | Strong UX claim but no data: completion rate with buttons vs. without? |
| "Cognitively easier" (transaction list vs. recall) | ⚠️ VAGUE | Behavioral science principle stated, not measured. Time to selection? Error rate? |
| "Unified entry funnel facilitates efficient dispute categorization" | ⚠️ VAGUE | Efficient compared to what? Need: time to classify, accuracy of classification |
| "Progressive disambiguation allows thorough vetting" | ⚠️ VAGUE | Thoroughness measured how? Misclassification rate? |
| Persona differences (Retail vs. SME) | ❌ UNSUPPORTED | Were these actually implemented distinctly? Different outcomes by persona? |
| "15-minute session window" vs "30-minute session" for SME | ✅ EVIDENCED | Specific design decision stated |
| "5-step disambiguation process" | ✅ EVIDENCED | Structured process clearly defined |
| "Adjacent intents" disambiguation (Auto Debit, CC Subscription, Failed UPI) | ✅ EVIDENCED | Taxonomy clearly documented |

### Top 5 Metrics That Would Transform This Case Study

1. **SR misclassification rate reduction** — Before: X% of service requests were incorrectly categorized. After: Y%. This directly proves "zero incorrect SR creation" or shows how close the system got. Matters to buyers: prevents operational chaos and duplicate work.

2. **Containment rate by persona** — Retail: X% resolved without agent. SME: Y% resolved without agent. Proves persona-differentiated thresholds worked. Matters to buyers: shows sophisticated behavior logic, not one-size-fits-all.

3. **Stale consent incidents prevented** — Session management caught X outdated confirmations per month in WhatsApp async environment. Proves compliance safeguard effectiveness. Matters to buyers: regulatory exposure mitigation is measurable.

4. **Completion rate through 5-step funnel** — X% of users who entered disambiguation completed all steps. Shows friction vs. thoroughness trade-off was calibrated correctly. Matters to buyers: proves progressive disclosure didn't cause abandonment.

5. **Agent escalation rate change** — Before: X% of disputes escalated to human. After: Y%. Subset of containment rate but focuses on "when to stop" positioning. Matters to buyers: direct proof automation knows its limits.

### Context Gaps

- **Scale**: How many users does this WhatsApp system serve? Daily/monthly transaction volume?
- **Regulatory body involvement**: Which specific NPCI/RBI regulations were constraints? Any audit outcomes?
- **Team structure**: Was this solo work or collaborative? Engineering team size? Compliance stakeholders?
- **Implementation timeline**: How long to build? Phased rollout or big bang?
- **Channel specifics**: WhatsApp Business API? Session windows enforced how (technically)?
- **Baseline state**: What did dispute resolution look like before? Manual agent handling? Email tickets? Call center?
- **Geographic/user segment**: All India? Specific bank customer segments (urban/rural, language distribution)?
- **Current status**: Is this live in production today? For how long?

### Recommended Evidence Ask

1. **To source from analytics/dashboards:**
   - SR creation volume and misclassification rate (month-over-month pre/post launch)
   - WhatsApp session analytics: completion rates, timeout frequency, re-engagement rates
   - Containment rate: % of conversations resolved without human transfer
   - Agent escalation volume trend

2. **To source from compliance/ops teams:**
   - Regulatory audit outcomes (zero violations claim?)
   - Stale consent risk incidents (should be tracked if it was a design concern)
   - Before/after operational load (agent handle time, ticket volume)

3. **To source from product/engineering:**
   - Persona implementation: were Retail vs. SME thresholds actually coded differently?
   - A/B test results (if any) on UI elements (quick replies vs. open text, transaction list vs. UTR entry)
   - API performance: ledger polling latency, transaction status verification success rate

4. **To clarify:**
   - Was "zero incorrect SR creation" the design goal or the achieved outcome?
   - What does "WhatsApp Channel Delays / Stale Consent Risk" quantitatively refer to?

---

## Case Study 2: Designing for Panic

### Claims Inventory

| Claim | Classification | Notes |
|-------|---------------|-------|
| "Leading driver of customer churn" (failed debits) | 🔍 RETRIEVABLE | Strong claim, but no churn rate data. Need: % attribution, before/after churn metrics |
| "45-minute wait times for a human agent" | ✅ EVIDENCED | Specific baseline established |
| "In the three seconds after payment fails... biological panic" | ⚠️ VAGUE | Narrative framing, not measurable (though compelling) |
| "Many failed debits auto-reverse during regulatory window" | ⚠️ VAGUE | "Many" = how many? Auto-reversal rate? |
| "Preventing duplicate investigations" | 🔍 RETRIEVABLE | Stated benefit but not quantified. How many prevented? Cost savings? |
| "Every 15 minutes: ledger is silently rechecked" | ✅ EVIDENCED | Specific technical design decision |
| "Carousel anchors memory" (vs. UTR recall) | ⚠️ VAGUE | UX principle but not measured: selection time? error rate? |
| "Recognition replaces recall" | ⚠️ VAGUE | Cognitive science claim, no usability metrics |
| "Faster resolution doesn't come from speed. It comes from clarity." | ❌ UNSUPPORTED | Philosophical statement. Need: actual resolution time before/after? |
| "Escalation is no longer triggered by emotion. It is triggered by verified system state." | ✅ EVIDENCED | Core design shift clearly articulated (but outcome not measured) |
| "5-gate logic funnel" | ✅ EVIDENCED | Structured approach documented (cooling period, debit verification, classification, regulatory alignment, confirmation) |
| "We stopped building a support bot. We built a diagnostic engine." | ✅ EVIDENCED | Clear strategic pivot statement |
| "Retail: 15-minute session reset" vs "SME: 30-minute session reset" | ✅ EVIDENCED | Persona differentiation specified |
| "Cooling period" active during regulatory window | ✅ EVIDENCED | Compliance-first design constraint articulated |
| "Binary buttons replace free text" | ✅ EVIDENCED | UI strategy clearly stated |
| "Auto-reversal may succeed" during cooling period | ⚠️ VAGUE | Acknowledged as system behavior but: what's the auto-reversal success rate? |

### Top 5 Metrics That Would Transform This Case Study

1. **Churn attribution & reduction** — Failed debits contributed to X% of churn. After diagnostic engine: Y% churn reduction in affected cohort. This proves the "leading driver" claim and shows measurable business impact. Matters to buyers: ties automation behavior to revenue.

2. **False escalation prevention rate** — Before: X% of escalated disputes were duplicate/premature (during active reversal window). After: Y%. Proves "truth before tickets" philosophy worked. Matters to buyers: operational savings and reduced backlog.

3. **Resolution time distribution** — Before: X% resolved in <5min, Y% in 5-45min, Z% required human. After: new distribution showing shift to faster resolutions. Proves "clarity over speed" led to actual speed gains. Matters to buyers: customer experience + operational efficiency.

4. **Debit verification accuracy** — X% of "money missing" complaints had no ledger debit posted. System immediately closed these "ghost transactions." Prevents wasted investigation effort. Matters to buyers: proves ledger-truth architecture value.

5. **Session re-validation impact** — In async WhatsApp environment, X% of sessions exceeded 15min window. Of those, Y% had state changes (auto-reversal completed). System prevented Z stale-consent escalations. Matters to buyers: async channel safety is measurable.

### Context Gaps

- **Scale**: Transaction volume handled daily/monthly? User base size?
- **Bank identity**: "Tier I Indian Bank" — which one? (If NDA-restricted, state as "confidential" but specify Tier category)
- **System architecture**: Real-time ledger polling — what latency? API reliability?
- **Before state**: What did failed debit support look like? IVR tree? Email forms? Agent-only?
- **Rollout details**: Pilot phase? Geographic rollout? Language support?
- **Regulatory context**: Specific RBI/NPCI TAT windows referenced (e.g., T+1 for UPI disputes)?
- **Current status**: Is this live? For how long? Any post-launch iterations?
- **Team/role clarification**: "We built" — team size? Cross-functional model? Reporting structure?
- **Cost context**: What does a duplicate investigation cost operationally? Agent time? Compliance review?

### Recommended Evidence Ask

1. **To source from business/CX analytics:**
   - Customer churn rate among users who experienced failed debits (before/after system)
   - CSAT or NPS delta for users who used diagnostic engine vs. previous flow
   - Volume of failed debit complaints (absolute numbers, trend over time)

2. **To source from operations:**
   - Duplicate investigation rate: how many tickets were opened for disputes already resolved or ineligible?
   - Agent handle time for escalated disputes (before/after system triage)
   - Cost per ticket / cost savings from reduced false escalations

3. **To source from engineering/data:**
   - Auto-reversal success rate during regulatory cooling period (proves "many auto-reverse" claim)
   - Ledger polling accuracy: % of user-reported "debit" that verified as true debit
   - Session state change frequency: how often did 15-min re-check catch resolved disputes?

4. **To source from product:**
   - A/B test results (if carousel vs. UTR entry was tested)
   - Completion rate through 5-gate funnel (dropout at which gate?)
   - Escalation appropriateness: of escalated cases, what % were valid (passed all gates correctly)?

5. **To clarify:**
   - "Archive protects trust" — what does this mean operationally? (Architecture detail in narrative but unclear)
   - Was the 45-min baseline measured across all dispute types or specifically failed debits?

---

## Cross-Case Study Observations

### Patterns Across Both Case Studies

**1. Regulatory-first thinking is consistent:**
Both CS1 and CS2 center on compliance constraints as design drivers. This isn't accidental — it's the positioning differentiator. But neither case study quantifies regulatory outcomes (zero violations, audit pass rates, exposure prevented). This is the strongest evidence gap.

**2. "Verification before action" philosophy is the through-line:**
- CS2: "Truth before tickets" — ledger verification blocks ghosttransactions
- CS1: 5-step disambiguation — each gate verifies state before allowing escalation
- This is the "automation that knows when to stop" positioning in practice

**3. Persona differentiation is architected, but outcomes by persona are missing:**
Both case studies specify Retail vs. SME thresholds (session length, ambiguity tolerance, escalation timing). But there's no evidence these distinctions produced different outcomes. A skeptical buyer will ask: "Was this actually implemented or just designed?"

**4. Edge case handling is well-documented, but edge case frequency is not:**
Language switching (CS1), stale consent in async channels (both), auto-reversal timing (CS2) — all handled thoughtfully. But without knowing how often these edge cases occur, we don't know if this is over-engineering or essential risk mitigation.

**5. UI as compliance safeguard is a unique positioning angle:**
The framing of button types, transaction carousels, and confirmation cards as regulatory protection (not just UX) is strong. But needs proof: did closed UI reduce compliance violations measurably?

**6. The "diagnostic engine vs. support bot" framing is the strongest strategic pivot:**
CS2's reframe from "helping users complain" to "verifying system state before acting" is the clearest expression of behavior ownership. This should lead the portfolio.

### What Both Case Studies Are Missing (Same Gaps)

- **Baseline operational state**: What did these systems replace? Manual flows? Simpler bots? Email forms?
- **Scale context**: How many users? Transactions? Conversations per day?
- **Team structure**: Was this solo systems design work or collaborative with 10-person engineering team?
- **Implementation evidence**: Are the refined designs (session timeouts, persona thresholds) actually deployed in production or still design specs?
- **Post-launch learnings**: Any iteration after launch? What broke? What assumptions were wrong?

---

## What Agent 3 (Critic) Should Pay Most Attention To

**1. Lead Burial Risk:**
The strongest strategic insight — "We built a diagnostic engine, not a support bot" (CS2) — appears midway through a long narrative. Agent 3 should check if this gets surfaced early enough in the final copy.

**2. Evidence Vagueness Pattern:**
Claims like "significant financial losses," "leading driver of churn," "prevents duplicate investigations" are stated as facts without backing. Agent 3 should ensure Agent 4 (Narrator) either:
- Sources these metrics if available, OR
- Reframes them as design goals/hypotheses rather than proven outcomes

**3. Persona Differentiation Skepticism Risk:**
Retail vs. SME thresholds are architecturally elegant but lack outcome proof. Agent 3 should flag if this reads as "over-designed" without evidence of different containment rates by persona.

**4. Compliance Outcomes Are the Biggest Missing Trust Signal:**
For a "risk-aware automation" positioning, the absence of regulatory audit outcomes, compliance violation rates, or exposure mitigation metrics is glaring. Agent 3 should check that Agent 4 addresses this either by:
- Surfacing compliance proof if it exists, OR
- Acknowledging it as "designed to ensure zero violations" (vs. claiming it achieved that without proof)

**5. The "Why" Behind Technical Choices Needs Foregrounding:**
Both case studies are rich in "what" (5 gates, 15-min timeout, closed UI) but the "why" (regulatory risk, operational cost, liability exposure) is sometimes buried. Agent 3 should ensure Agent 4 inverts this: decision rationale first, implementation detail second.

**6. Scale Ambiguity Hurts Credibility:**
Without scale context (user volume, transaction volume), sophisticated design choices could read as over-engineering. Agent 3 should flag places where Agent 4 needs to add scale context even if specific metrics are unavailable (e.g., "Tier I bank serving millions of customers" vs. no context).

**Key Recommendation for Agent 4 (Narrator):**
Do not invent metrics. Where evidence is missing, reframe claims as design intent or architectural decisions. Example:
- Weak: "This reduced churn significantly."
- Strong: "Failed debits were identified as a churn driver. The diagnostic engine was architected to prevent premature escalations by verifying ledger state before creating tickets — eliminating the operational chaos that erodes trust."

This preserves analytical rigor (the "why") while being honest about missing outcome data (the "how much").