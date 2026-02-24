# Final Portfolio Copy

## HOMEPAGE

### Hero

**Headline:**
I Build Automation That Knows When to Stop

**Subheadline:**
I define decision boundaries for financial AI — the logic that sits between what a user says and what a system is permitted to do. When to act. When to verify. When to escalate. When to refuse.

**CTA:**
View Case Studies

---

### What I Own

**Decision Boundaries & Intent Eligibility**
I define when a system can act autonomously vs. when it must ask for clarification. In financial services, this means building disambiguation funnels that verify intent before executing irreversible actions.

**Escalation Policies & Fallback Logic**
I specify the conditions under which automation must stop and transfer to human judgment. Not every escalation request is valid — I build the verification gates that separate legitimate from premature escalations.

**Compliance Architecture & Session Management**
I translate regulatory constraints into conversation state logic. NPCI TAT windows become cooling period gates. Async channel timeouts become stale consent prevention mechanisms. The system doesn't just follow rules — it enforces them structurally.

**Containment Criteria & Threshold Calibration**
I define confidence thresholds that balance risk against automation rate. Different user contexts (retail borrower vs. SME merchant) require different ambiguity tolerances. I build threshold differentiation, not one-size-fits-all flows.

---

### The Problems I Solve

**The gap between utterance and permission**
In banking, a user saying "money is missing" could mean six different scenarios with six different regulatory implications. Acting on ambiguous intent creates liability. I build the disambiguation logic that verifies system state before allowing escalation.

**When fast automation becomes expensive automation**
Speed optimizations that skip verification steps compound downstream. Incorrect service requests waste investigation effort. Premature escalations violate regulatory windows. I define the gates that protect operational correctness even when it slows user paths.

**Multi-context behavior without fragmented experiences**
Retail users in panic can't recall transaction IDs. SME merchants processing hundreds of payments need precision over guidance. I architect threshold differentiation — different session windows, different ambiguity tolerance, different escalation timing — because conflating risk profiles is operationally unsafe.

---

## CASE STUDY 1: Audit-Safe Conversations

### One-line summary (for card on homepage)
I built a dispute resolution system where only verified ledger state — not user panic — triggers escalation in a regulatory environment where mistakes compound.

### Hero headline
When Escalation Requires Proof

### Hero subheadline
Most banks let users escalate failed UPI debits on complaint alone. We didn't. We built a 5-gate verification funnel where only verified system state — not user emotion — triggers service request creation.

---

### Beat 1 — The Moment

A user opens WhatsApp. Types: "Money got cut but payment didn't go through."

The old system would immediately ask: "Would you like to raise a dispute?"

The new system asks a different question first: "Is this provably true?"

---

### Beat 2 — The System Problem

The surface problem looked like slow support. Users waiting, frustrated, wanting immediate resolution.

The real problem was permission architecture.

In financial dispute resolution, acting on unverified intent creates three failures:
- Incorrect service requests waste investigation effort
- Premature escalations violate regulatory TAT windows (auto-reversals happen during cooling periods)
- Ambiguous classification (failed UPI vs. recurring mandate vs. card subscription) routes to wrong resolution teams

The gap between what a user says and what a system is legally permitted to do — that gap is massive. And in banking, that gap has regulatory consequences.

---

### Beat 3 — What Everyone Else Would Do

Build a faster support bot.
Reduce wait times from 45 minutes to 5.
Make escalation frictionless — one tap, dispute raised.
Optimize for relief.

This is the obvious approach. Empathy-driven. User-centric.

It's also operationally dangerous.

Fast automation that acts on ambiguous data creates duplicate investigations, compliance exposure, and operational chaos that erodes the trust it was meant to protect.

---

### Beat 4 — The Pivot

We stopped building a support bot.

We built a verification funnel.

Escalation is no longer triggered by user complaint. It's triggered by verified system state.

---

### Beat 5 — The Architecture

#### The 5-Gate Verification Funnel

Every complaint enters a gated sequence. Not to slow users down — to prevent incorrect action.

**Gate 1: Confirm Amount Was Debited**
Users sometimes report failures before checking balance. The bot verifies amount debit explicitly. If not debited: dispute path closes immediately. No service request created.

**Gate 2: Confirm Transaction Channel**
"Payment didn't go through" could mean UPI, card, bank transfer, or IMPS. Each channel has different regulatory rails. The bot disambiguates before routing.

**Gate 3: Verify Transaction Status**
Real-time ledger polling. If status shows "pending," the transaction may still complete. If "failed" but not debited: ghost transaction (no action needed). Only "failed + debited + credited elsewhere" qualifies for escalation.

**Gate 4: Check Refund Completion**
Auto-reversals happen. System checks if refund already processed during regulatory window. If yes: closes case. No duplicate investigation.

**Gate 5: Check Regulatory TAT**
NPCI mandates cooling periods (T+1 for UPI disputes). During this window, auto-reversals are likely. Escalation is blocked. Users informed of TAT expectation.

Only if all five gates pass → Service request is offered.

#### [EXPAND: Why Each Gate Represents a Judgment Call]

Each gate isn't just a validation step — it's a refusal point.

**Gate 1 refusal:** "We refuse to raise disputes when no money was debited."
Why: Prevents ghost transaction tickets. Protects investigation team capacity.

**Gate 2 refusal:** "We refuse to use a single classification for all payment failures."
Why: UPI disputes follow NPCI rules. Card disputes follow different SLA. Misclassification causes routing errors and compliance exposure.

**Gate 3 refusal:** "We refuse to act on user-reported status alone — ledger truth governs action."
Why: Users misinterpret "pending" as "failed." Acting on perception instead of system state creates incorrect SRs.

**Gate 4 refusal:** "We refuse to open disputes for transactions already refunded."
Why: Duplicate investigations waste compliance review effort. Auto-reversals happen frequently — checking first prevents churn.

**Gate 5 refusal:** "We refuse to allow escalation during active regulatory windows."
Why: TAT-compliant auto-reversals are likely. Premature escalation creates operational noise. Regulatory alignment before user gratification.

#### Persona-Based Threshold Differentiation

Retail users and SME merchants can't share the same control model.

**Retail Context:**
- Users borrowing ₹2,000-10,000 for survival
- Under stress, limited banking terminology familiarity
- Need: recognition (carousel shows recent transactions) over recall (UTR entry)
- Session window: 15 minutes
- Ambiguity tolerance: higher (we infer more)
- Escalation timing: delayed (TAT education prioritized)

**SME Context:**
- Merchants processing 50+ daily transactions
- High precision need, comfortable with banking references
- Need: search control (direct UTR entry) over guidance
- Session window: 30 minutes
- Ambiguity tolerance: lower (we verify more)
- Escalation timing: earlier (business impact drives urgency)

This wasn't complexity for elegance. It was risk mitigation. Conflating these profiles would fail both.

#### [EXPAND: UI As Compliance Safeguard]

Every UI element serves a verification function — not just usability.

**Binary Quick Reply Buttons (Yes/No)**
Purpose: Eliminate ambiguous free-text responses.
Compliance rationale: Reduces interpretation risk. Audit logs become deterministic.

**Transaction List Carousel (Last 5 UPI)**
Purpose: Recognition-based selection vs. recall (asking for UTR).
Compliance rationale: Prevents data entry errors. Limits list to 5 to avoid overload while ensuring recent coverage.

**Confirmation Card Before SR Submission**
Purpose: Restates amount, date, merchant for explicit user verification.
Compliance rationale: Prevents stale consent in WhatsApp async channels. If user idle 15+ min, state is re-validated before action.

**Session Timeout Message**
Purpose: Enforces session boundaries after inactivity threshold.
Compliance rationale: Bot cannot act on outdated confirmations. Protects against compliance violations from delayed responses.

**Agent Transfer Button (Explicit)**
Purpose: Clear, user-driven escalation when automation reaches limits.
Compliance rationale: Ensures traceability of when automation stops and human handling begins. No silent handoffs.

#### [EXPAND: Multi-Dispute Disambiguation Taxonomy]

"Money got deducted" doesn't map to one dispute type. It maps to five.

The system progressively narrows:

1. **Issue Timing:** Payment attempted now vs. noticed later → Routes to initiation issue vs. post-transaction
2. **Debit Status:** Amount actually debited? → If no, status check; if yes, debit analysis
3. **Charge Pattern:** One-time vs. recurring → Routes to transaction dispute vs. mandate dispute
4. **Payment Rail (one-time):** UPI / Card / Bank transfer → Different regulatory frameworks apply
5. **Debit Source (recurring):** Bank account / Credit card → NACH dispute vs. card subscription cancellation

Each fork prevents misclassification. Each classification change downstream costs operational effort to fix.

We built the disambiguation upfront, not as cleanup later.

---

### Beat 6 — The Tradeoffs

| What We Gave Up | What We Protected | Why The Trade Was Right |
|-----------------|-------------------|-------------------------|
| **Speed** → Users answer more questions before escalation | **Safety** → Incorrect SRs create downstream chaos | Fast automation that makes mistakes is more expensive than slow automation that gets it right |
| **Simplicity** → Retail vs. SME paths differ in thresholds | **Precision** → Risk profiles demand different control models | A single flow optimizes for neither; threshold differentiation protects both |
| **Convenience** → Users can't escalate during TAT window | **Auditability** → Compliance alignment prevents premature action | User impatience vs. regulatory exposure — regulatory risk wins |
| **Instant gratification** → Carousel limits to 5 transactions | **Accuracy** → Recognition over recall reduces selection errors | Cognitive ease reduces mistakes; limit prevents overload |
| **Flexibility** → Session timeout forces restart after 15min | **Integrity** → Prevents stale consent in async WhatsApp | Outdated confirmations create compliance violations; freshness protects legitimacy |

---

### Beat 7 — The Outcome

This system was built for a Tier I Indian bank's WhatsApp-based dispute resolution channel serving millions of customers.

Post-launch containment metrics and SR misclassification rates were tracked by operations. The decision logic — when to verify, when to block, when to allow — is the artifact of my work.

The architecture enforces: no service request creation without passing all five gates. No escalation during active regulatory windows. No single flow across incompatible risk profiles.

Correctness before speed. Verification before action. Truth before tickets.

---

### Beat 8 — The Reflection

If I rebuilt this today, I'd instrument each gate with dropout analytics from day one.

Which gate has highest abandonment? Is it friction or clarity?
Which persona completes faster? Is threshold calibration correct?
Do users who drop at Gate 3 (status verification) return later — or churn?

The gates were built on judgment and regulatory constraint. The tuning should be data-driven.

But the philosophy holds: in financial automation, the question isn't "how do we speed up support?" It's "under what conditions do we have permission to act?"

That question — permission architecture — is what separates automation from operational liability.

---

## CASE STUDY 2: The Diagnostic Engine

### One-line summary (for card on homepage)
I built a failed debit resolution system that refuses to act on user panic — only verified ledger state triggers escalation, because fast automation that guesses is more expensive than slow automation that knows.

### Hero headline
The Gap Between Panic and Truth

### Hero subheadline
In the three seconds after a payment fails and money leaves the account, a user enters biological panic. Mostbanks respond by speeding up human support. We built the opposite: a diagnostic engine that delays escalation until ledger truth is verified.

---

### Beat 1 — The Moment

Payment fails. Balance drops.

The user sees one signal: **money gone.**

The system sees six possible states:
- Debit never posted (ghost transaction)
- Credit leg failed downstream
- Auto-reversal already in motion
- Regulatory window still active
- Duplicate request (already resolved)
- Legitimate dispute requiring manual intervention

The moment of panic is also the moment of maximum ambiguity.

---

### Beat 2 — The System Problem

The surface problem looked like slow support. 45-minute wait times for human agents. Cryptic error messages.

Customer retention teams flagged failed debits as a recurring churn trigger — not because of the technical failure, but because of the opacity that followed.

The real problem was **inquiry-driven architecture.**

Old flow: User complains → System asks "What happened?" → User explains → System routes → Agent investigates → Resolution (maybe).

Inquiry assumes user perception is data. It's not.

Language is a noise variable. "Money didn't go through" could mean:
- Failed UPI debit
- Recurring NACH mandate
- Subscription charge
- Pending refund

Acting on ambiguous descriptions creates:
- Duplicate investigations (ticket already resolved)
- Premature escalations (auto-reversal still likely during TAT)
- Misclassification (wrong resolution team, wrong SLA)

The system optimized for empathy. It needed to optimize for truth.

---

### Beat 3 — What Everyone Else Would Do

Reduce wait times. Build a faster bot. Make escalation one-tap easy.

"We hear your frustration. Let us raise a dispute immediately."

Empathy-first. User-centric. The obvious approach.

It's also the approach that creates operational chaos.

Because:
- Many failed debits auto-reverse during NPCI TAT windows (T+1 for UPI). Allowing immediate disputes creates duplicate work.
- "Money missing" complaints often have no ledger debit (user checked before transaction completed). Acting on perception wastes investigation capacity.
- Premature escalations during active reversal windows violate regulatory alignment. Compliance exposure compounds.

Speed without verification is noise amplification.

---

### Beat 4 — The Pivot

We stopped building a support bot.

We built a diagnostic engine.

Escalation is no longer triggered by user complaint.
It's triggered by **verified system state.**

Inquiry → Validation.
"What happened?" → "Here's what we see."

---

### Beat 5 — The Architecture

#### The 5-Gate Logic Funnel

Every complaint enters a verification sequence. Each gate represents a refusal point.

**Gate 1: Cooling Period Check**
**Why this gate exists:** Many UPI debits auto-reverse within 24-48 hours during NPCI TAT window. Allowing immediate escalation creates duplicate investigations — operational chaos and wasted compliance review.

**Decision:** Escalation blocked during active reversal window.

**Implementation:** Timestamp verification against NPCI T+1 rule. If transaction < 24hr old: user informed of TAT, escalation unavailable, instructed to return if unresolved after window.

**The cost of waiting:** User impatience.
**The cost of acting prematurely:** 10x worse (duplicate tickets, agent capacity wasted, compliance noise).

**Gate 2: Debit Verification**
**Why this gate exists:** Users sometimes report "money missing" before transaction settles. Perception ≠ ledger truth.

**Decision:** Real-time ledger polling. If no debit posted → case closed immediately.

**Implementation:** API call to bank ledger. Response states: posted / pending / not found. Only "posted" qualifies for next gate.

**What this prevents:** Ghost transaction tickets. Users often check balance mid-transaction. Ledger hasn't updated. Complaint is based on incorrect perception.

**Gate 3: Payment Classification**
**Why this gate exists:** "Money got deducted" could mean UPI / Card / IMPS / Recurring mandate. Each has different regulatory rails and resolution SLAs.

**Decision:** Progressive disambiguation before routing.

**Implementation:** Bot asks: "One-time payment or recurring charge?" Then: "UPI / Card / Bank transfer?" Classification determines which downstream rules apply.

**What this prevents:** Misclassification errors. UPI disputes follow NPCI TAT. Card disputes follow different SLA. Routing to wrong team delays resolution and violates compliance timelines.

**Gate 4: Regulatory Alignment**
**Why this gate exists:** Payment rails have mandated TAT windows. During these windows, auto-resolution is system responsibility. User escalation is inappropriate.

**Decision:** Escalation adapts to rail-specific regulatory constraints.

**Implementation:** For UPI: T+1 cooling period enforced. For card: different dispute window. System reflects constraints in real-time — no refund promises, no premature liability acknowledgment.

**What this prevents:** Compliance exposure. Banks can't allow user-driven escalation to override regulatory process. Architecture enforces this structurally.

**Gate 5: Explicit Confirmation**
**Why this gate exists:** WhatsApp is async. User starts dispute at 10am, responds at 12pm. In that time, auto-reversal may complete. Acting on stale intent creates incorrect SRs.

**Decision:** Before submission, restate merchant / amount / date. If idle > 15min, re-validate state.

**Implementation:** Confirmation card shown. If session exceeds threshold, ledger re-polled silently. If state changed (e.g., refund completed), flow closes with update instead of opening ticket.

**What this prevents:** Stale consent violations. Async channels require freshness checks. Confirmation isn't UX polish — it's compliance safeguard.

#### [EXPAND: Retailvs. SME — Why One Flow Fails Both]

The system serves two incompatible contexts:

**Retail borrowers:**
- Borrowing ₹2,000-10,000 for survival
- Under acute stress (money is oxygen)
- Zero familiarity with "UTR," "transaction reference," banking terminology
- Cognitive state: panic narrows cognition, recall fails

**The solution they need:** Recognition over recall.
- Show carousel of last 5 UPI transactions → "Which one?"
- Binary buttons → "Was money debited?"
- Simplified language → No jargon
- Session window: 15 minutes (attention span under stress)
- Ambiguity tolerance: higher (system infers more)
- Escalation timing: delayed (TAT education prioritized over instant gratification)

**SME merchants:**
- Processing 50-100 payments daily
- High transaction volume, precision need
- Comfortable with UTR, transaction logs, banking references
- Cognitive state: business-mode, control preference

**The solution they need:** Precision over guidance.
- Direct UTR search field (they have references)
- Extended session window: 30 minutes (business context allows longer engagement)
- Lower ambiguity tolerance (verify more, infer less)
- Earlier escalation option (business impact drives urgency)
- Structured confirmation (B2B accountability standards)

**Why this complexity was necessary:**
A carousel for SME merchants is condescending (they know their UTR).
A UTR field for retail users is a blocker (they don't have it, can't recall it).

Behavioral architecture had to reflect risk profile differentiation. Not because it was elegant. Because conflating these contexts would operationally fail both.

#### [EXPAND: Session Re-Validation — Async Channel Safety]

WhatsApp is asynchronous. Disputes don't happen in one sitting.

User starts at 10:00. Responds at 10:08. Gets distracted. Returns at 10:42.

In those 42 minutes: auto-reversal completed. The problem resolved itself.

**Without re-validation:** System submits dispute based on stale intent. Creates unnecessary ticket. Wastes investigation effort. Violates operational correctness.

**With re-validation:** System checks ledger state every 15 minutes. If state changed → closes flow with update. If unchanged → resumes from last checkpoint.

The rule:
- **Retail: 15-minute window.** If exceeded, restart.
- **SME: 30-minute window.** Business context allows longer gaps.

This may feel restrictive. But async integrity requires freshness enforcement.

Stale consent isn't just bad UX. It's a compliance violation. The system protects itself by refusing to act on outdated confirmations.

---

### Beat 6 — The Tradeoffs

| What Everyone Else Optimizes | What We Optimized | Why |
|-------------------------------|-------------------|-----|
| **Escalation speed** — one tap, dispute raised | **Escalation correctness** — only verified state triggers action | Premature tickets waste 10x more effort than user wait time |
| **User empathy** — "We hear you, let's help immediately" | **System truth** — "Here's what the ledger shows" | Empathy without verification creates operational chaos |
| **Single flow** — same experience for all users | **Threshold differentiation** — Retail vs. SME contexts | One flow optimizes for neither; risk profiles demand distinct control models |
| **Friction reduction** — minimize questions | **Verification rigor** — progressive disambiguation | Questions aren't friction when they prevent mistakes; they're protection |
| **Instant gratification** — escalate now | **TAT alignment** — respect regulatory windows | Regulatory compliance before user impatience; architecture enforces this structurally |

**The meta-tradeoff:**
Speed → Safety. Convenience → Auditability. Inquiry → Validation.

We sacrificed the feeling of instant action to protect operational correctness.

---

### Beat 7 — The Outcome

This diagnostic enginewent live at a Tier I Indian bank and handles failed UPI debit resolution at scale.

The operational impact — containment rate, SR misclassification reduction, agent handle time, churn impact among affected users — was tracked by CX and operations teams post-launch. Those metrics are owned by the business.

The architecture is my artifact:
- 5-gate verification funnel that blocks escalation until all conditions met
- Persona-based threshold differentiation (15min vs. 30min session windows)
- Ledger-truth validation replacing inquiry-driven routing
- Async channel stale consent prevention through re-validation logic

The outcome measurement I can state definitively: the system refuses to create service requests during active NPCI TAT windows. It refuses to act when no ledger debit is verified. It refuses to use the same ambiguity threshold for retail borrowers and SME merchants.

Those refusals **are** the outcome. They represent decision architecture, not feature execution.

---

### Beat 8 — The Reflection

The hardest thing wasn't building the gates. It was defending the gates.

Stakeholders wanted faster escalation. "Why make users wait 24 hours?"

Engineers wanted simpler logic. "Why build two personas when one flow could cover 80% of cases?"

CX teams wanted empathy-first language. "Why does the bot sound like it's doubting the user?"

Each question had the same answer: **because the alternative is operationally more expensive.**

- Waiting 24 hours feels bad. Creating 1,000 duplicate tickets per month **is** bad.
- Building one flow is simpler. Serving neither persona correctly **is** complexity — just deferred to support agents.
- Empathy language feels warmer. Acting on unverified claims **erodes trust faster** than cold precision.

If I rebuilt this, I'd do one thing differently: I'd create a simulation dashboard that showed stakeholders the cost of each gate removal.

"Here's what happens if we skip Gate 3: 40% misclassification rate, routing delays, SLA violations."

The gates weren't arbitrary rules. They were operational protections. Making that cost visible would have shortened the defense cycle.

But the philosophy holds: in financial automation, the question isn't "can we make this faster?"

It's "under what conditions do we have permission to act?"

And sometimes — often — the right answer is: "Not yet. Verify first."

---

## ICICI BANK VOICEBOT

### One-line summary (for card on homepage)
I defined conversation logic and escalation policies for transactional voice banking at scale — 70+ live use cases where one misstep in utterance disambiguation or fallback strategy becomes liability.

### Project Context

**What it is:**
ICICI Bank's production NLP-powered voicebot handling transactional banking over phone. Not an FAQ assistant. Transactional: payments, card blocks, security resets, dispute initiation — high-stakes flows where mistakes have financial and regulatory consequences.

**Scale:**
70+ live use cases. Call: 1800 1080 to experience it.

**My role:**
Lead on conversation logic architecture. I defined:
- Intent disambiguation hierarchies ("block card" vs. "stop card" vs. "card is gone" → same intent, different ASR patterns)
- Mandatory confirmation loops (prevent action on misheard amounts, card numbers, account selections)
- Escalation policies (when bot must stop vs. when it can proceed)
- Fallback strategies (gentle re-prompts vs. agent transfer triggers)
- Micro-copy that builds confidence in voice-only, high-anxiety contexts

**The constraint:**
Phone banking removes visual confirmation. Users can't "see" what they're about to do. Everything is auditory. One misheard digit in a payment amount, one wrong card selected from multiple — and trust is gone.

The system had to know when to act (user intent is clear, verified, confirmed) and when to stop (ambiguity detected, high-risk action, user confusion).

**The collaboration:**
Worked with ML engineers on intent training and ASR error pattern handling. With compliance teams on mandatory confirmation language and audit trail requirements. With solution architects on API orchestration and latency constraints.

This wasn't solo design work. It was behavior specification in a cross-functional environment where my artifact was decision logic, not mockups.

**The outcome:**
One of India's first transactional voicebots. 70+ use cases live. Dramatic reduction in call center dependency for repetitive-but-urgent requests.

The specific containment metrics and call deflection rates are owned by ICICI operations. The conversation architecture —when to verify, when to block, when to escalate — is my work.

---

## ABOUT

I'm Samruddhi Pahune. I build automation that knows when to stop.

My work sits in the gap between what users say and what systems are permitted to do — particularly in financial services, where that gap has regulatory and operational consequences. I don't design conversation flows. I define decision boundaries: disambiguation funnels that verify intent before action, escalation policies that know when automation must pause, and verification gates that translate compliance constraints into conversation state logic.

I've built behavior architecture for AI systems at a Tier I Indian bank (transactional voice banking, 70+ live flows), for WhatsApp-based dispute resolution (failed UPI debits, multi-intent disambiguation), and across contexts where regulatory alignment, operational correctness, and user anxiety intersect. The through-line across all this work: the question isn't "how do we automate faster?" It's "under what conditions do we have permission to act?"

I collaborate with engineering teams, data science, compliance, and product to turn that question into structured logic: thresholds, gates, fallback criteria, session boundaries. I think in containment rates, false positive reduction, and escalation appropriateness — not bounce rates and NPS. If you're building AI systems where mistakes compound, where regulations constrain action, or where user utterances don't map cleanly to system permissions, this is the layer I own.

---

## COPY NOTES FOR AGENT 5 (Designer)

### Visual Hierarchy Notes

**Homepage Hero:**
- Headline "I build automation that knows when to stop" should be largest text on page
- "Decision boundaries for financial AI" subheadline should be visually distinct but secondary
- Three capability cards need consistent treatment — equal visual weight

**Case Study Cards:**
- One-line summaries are critical — these are the "hook" on the homepage
- Need hover states that preview depth (maybe pull the "beat 1" moment text on hover?)

**Pull Quotes / Callouts:**
These lines should get visual treatment (larger text, different color, or card treatment):

CS1:
- "We stopped building a support bot. We built a verification funnel."
- "Escalation is no longer triggered by user complaint. It's triggered by verified system state."
- "Fast automation that makes mistakes is more expensive than slow automation that gets it right."

CS2:
- "We stopped building a support bot. We built a diagnostic engine."
- "Language is a noise variable. The ledger is truth."
- "Inquiry → Validation. 'What happened?' → 'Here's what we see.'"

**Expandable Sections:**
These "[EXPAND: title]" sections need interactive treatment — collapsed by default, expand on click, smooth transition:

CS1:
- "Why Each Gate Represents a Judgment Call"
- "UI As Compliance Safeguard"
- "Multi-Dispute Disambiguation Taxonomy"

CS2:
- "Retail vs. SME — Why One Flow Fails Both"
- "Session Re-Validation — Async Channel Safety"

**Tables:**
The tradeoff tables in both case studies are structural — need clear visual treatment:
- 3 columns: "What We Gave Up" | "What We Protected" | "Why The Trade Was Right"
- Zebra striping or alternating background colors for readability
- Mono or semi-bold for headers

**The "Reflection" Sections:**
These should feel distinct from the main narrative — maybe slightly different background shade or italicized? They're personal, reflective, different tone from the rest.

**ICICI Section:**
This is shorter/simpler than the main case studies. Could work as an inline project block or a sidebar "additional work" panel. Don't give it the same visual weight as CS1/CS2 main studies.

**About Section:**
Three short paragraphs. Clean, readable, not decorative. This should feel like "the person behind the work" but still professional-systems-thinker tone, not creative-portfolio vibe.

**Word to Visual Mappings:**
- "5-gate funnel" → Could be a vertical visualization: 5 numbered nodes with connector lines
- "Retail vs. SME" tables/comparisons → Side-by-side cards with subtle divider
- "Before / After" language → Use visual contrast (left column | right column, or color differentiation)

**Key Positioning Preservation:**
The homepage should communicate "I build automation that knows when to stop" without literally repeating the positioning doc language. The visual structure + copy should embody it:
- Hero section = immediate clarity on what she owns
- Capability section = systems-level thinking (not "I design flows")
- Case study cards = problems-worth-solving (not deliverables-I-shipped)

**Do NOT:**
- Add decorative illustrations
- Use playful microcopy
- Make the design "delightful" — make it precise, structured, confident
- Hide depth behind "learn more" CTAs that go to separate pages — use progressive disclosure (expand sections) within the same view

**DO:**
- Use whitespace generously
- Make typography do the work (hierarchy through size/weight, not color overload)
- Ensure case studies are scannable — someone should understand the surface in 60 seconds, depth available on demand
- Make the tradeoff sections visually prominent — they're the strongest proof of judgment over execution