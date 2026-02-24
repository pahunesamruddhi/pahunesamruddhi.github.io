# Case Study 1: Audit-Safe Conversations
## Failed UPI Debit and Multi-Dispute Resolution Flow

---

## The Stakes

**Financial Loss**
Mismanaged disputes can lead to significant financial losses for banks, impacting their bottom line and profitability. Proper handling is essential to mitigate these risks effectively.

**Regulatory Exposure**
Incorrect resolution of disputes exposes banks to regulatory scrutiny and penalties, adversely affecting their reputation and operations. Compliance with NPCI and RBI regulations is crucial to avoid potential legal consequences.

**WhatsApp Channel Delays / Stale Consent Risk**
Delays in WhatsApp communication can lead to stale consent, increasing the likelihood of disputes. Timely interactions are essential for maintaining user trust and ensuring accurate dispute resolution.

---

## Design Philosophy: Prioritizing Risk Reduction Over Speed

**Value of Safe Automation**

*Trust at Scale*
As automation replaces human judgment, trust becomes a design outcome. Systems that prioritise correctness create predictable, repeatable experiences that scale without eroding user confidence.

*Correctness Over Speed*
Fast automation that makes mistakes is more expensive than slow automation that gets it right. In financial systems, delaying an action is often safer than acting on incomplete or ambiguous information.

---

## Design Constraints

1. **Regulatory Mandates** — Compliance with NPCI and RBI regulations ensures design adheres strictly to legal requirements, minimizing risks of non-compliance and enhancing customer trust.

2. **Asynchronous Channel** — The limitations of WhatsApp's asynchronous nature require careful consideration, ensuring responses are timely and maintain user engagement while reducing stale consent risk.

3. **Zero Incorrect SR Creation** — A zero-tolerance policy for incorrect service request creation safeguards against potential financial repercussions and upholds the integrity of the banking experience.

**Explicit Decisions**
Every decision made during the banking conversation must be explicit, traceable, and auditable. This fosters accountability and minimizes risks, ultimately enhancing user confidence.

**Design Restraint — Deliberate Limits in the Design**
- Auto-raising disputes on user complaint alone
- Forcing UTR entry upfront for retail users
- Promising refunds or explaining root causes
- Using a single flow across all risk profiles

---

## Failed UPI Debit Intent

**Scope**
- Money debited
- Recipient not credited
- User seeks status or dispute assistance

**Critical Rule**
This intent is valid only after eliminating adjacent scenarios.

**Sample Utterances**
1. Money got cut but the payment didn't go through.
2. UPI failed but amount is gone from my account.
3. The shopkeeper says he didn't get the payment.
4. It said payment failed but the money hasn't come back.
5. I paid on UPI and it didn't reach the other person.
6. UPI money is stuck.

---

## 5-Step Disambiguation Process

1. Confirm amount was debited
2. Confirm transaction channel
3. Verify transaction status
4. Check refund completion
5. Check regulatory TAT

**Only if all five pass → SR can be offered**

---

## Persona Differences

**Control Thresholds**
Differences in user personas significantly impact their control thresholds. Retail users may tolerate ambiguity, while SMEs require precision and verification. This distinction is essential for effective risk management.

**Retail Focus**
The retail flow emphasises self-service through visual selection of recent transactions, reducing effort and input errors. It uses a 15-minute session window with graceful closure, tolerates higher ambiguity within TAT, and limits escalation through simplified, button-driven decisions.

**SME Focus**
The SME flow follows a verification-first approach, collecting UTR references early to ensure precision for high-value transactions. It preserves state for up to 30 minutes, applies stricter ambiguity thresholds, and enables earlier escalation with detailed confirmations for accuracy and compliance.

---

## Explicit Confirmation / Preventing Stale Consent

**Safety Lock**
Implementing explicit confirmation acts as a safety lock, ensuring users verify their intent before proceeding. This approach minimizes errors, protects both the bank and user, and enhances audit safety.

- **Explicit Confirmation** — Through explicit confirmation of transaction details, stale consent is prevented, ensuring user approval is both valid and relevant at time of request.
- **Timely Interactions** — Delays can lead to outdated consent, increasing risk during crucial banking conversations on WhatsApp.
- **Session Management** — Strict session management with timeouts guarantees user information is refreshed, minimizing stale consent risks.

---

## UI Safety — Reducing Risk in Banking Conversations

**Open Text Risks**
Open text inputs can lead to ambiguity and errors, increasing the risk of incorrect service requests and miscommunications that can escalate disputes unnecessarily.

**Closed UI Benefits**
Closed UI design minimizes ambiguity, ensuring clear user intent while providing a structured interface that enhances compliance and maintains an accurate audit trail throughout the conversation.

**UI Element Rationale Table:**

| UI Element | Where Used | Why This Element (Design + Risk Rationale) |
|---|---|---|
| Plain Text Message | Greeting, explanations, status outcomes | Non-actionable info. Allows precise, compliant phrasing ("as per guidelines," "usually"). Avoids implying guarantees. Safest for explaining TATs without encouraging premature escalation. |
| Quick Reply Buttons (Binary) | Yes/No questions (debit confirmation, raise SR) | Reduce interpretation risk. Eliminate ambiguous free-text responses. Enforce clear intent capture before irreversible actions like SR creation. Standardises audit logs. |
| Quick Reply Buttons (Choice-based) | Selecting "Just tried to pay" vs "Noticed later" | Help bot disambiguate initiation issues vs post-transaction issues early. Prevent incorrect dispute flows. On WhatsApp, reduce dropoffs vs open-ended questions. |
| Transaction List / Rich Card | Selecting one of the last 5 UPI transactions | Recognition-based selection is cognitively easier than recall. Avoids asking for UTR upfront. Reduces data entry errors. Limits to 5 prevents overload. |
| Text Input Field (Controlled) | UTR, date, amount (fallback only) | Free text is intentionally fallback, not default. Reduces error rates. For SMEs, enables precision when they have references. |
| Loading Indicator | While fetching transaction status | Signals backend dependency. Prevents repeated inputs. Manages impatience. Critical in financial contexts to maintain trust. |
| Structured Confirmation Card | Before raising service request | Restates key details (amount, date, merchant) to prevent stale or mistaken consent. Compliance safeguard in async channels. |
| Escalation Buttons | Out-of-TAT or high-value cases | Ensures escalation is explicit, user-driven. For retail: delayed. For SME: offered earlier due to business impact. Same UI, different timing. |
| Session Timeout Message | After inactivity threshold | Prevents bot from acting on outdated confirmations. Enforces session boundaries. Avoids compliance violations from delayed responses. |
| Agent Transfer Button | Edge cases, high-value failures | Clear, explicit transfer avoids silent handoffs. Preserves user control. Ensures traceability of when automation stops and human handling begins. |

---

## Multi-Dispute Resolution

**Prevent Misclassification**

*Unified Entry Funnel*
A unified entry funnel facilitates efficient dispute categorization, minimizing chances of misclassification before escalation begins.

*Progressive Disambiguation*
Implementing progressive disambiguation allows thorough vetting, ensuring each case is assessed accurately based on its specific nuances.

**Agent Fallback**
Users should have the confidence that they can reach a live agent whenever necessary. This assurance enhances user experience and mitigates risks associated with automated service failures.

---

## Adjacent Intents (Multi-Dispute)

**Auto Debit / NACH**
User reports an unexpected or unauthorised recurring debit from their bank account, usually monthly, via auto debit / mandate / NACH.

Sample utterances:
- Money is getting deducted from my account every month.
- Some amount keeps going from my bank account automatically.
- I don't know why money is being cut regularly from my account.
- Every month some money goes out of my account without asking.
- An auto payment is happening from my account and I don't know about it.
- Why is money being deducted again and again from my account?

**CC Subscription**
These users usually recognise the pattern but not always the merchant, and often mention cancelling.

Sample utterances:
- My credit card is getting charged every month.
- I cancelled this but my card is still getting charged.
- Why is my card being charged again?
- A subscription fee is getting deducted from my card.
- I forgot what this subscription is but it keeps charging my card.
- There's a repeated charge on my credit card.

---

## Intent Disambiguation Flow

1. **Issue Timing** — Identify whether the issue is with a payment being attempted now or a past transaction.
2. **Debit Status** — For past transactions, confirm whether the amount was actually debited.
3. **Charge Pattern** — Determine whether the debit is one-time or recurring.
4. **Payment Type (One-Time)** — Classify one-time debits by rail: UPI, card, or IMPS/NEFT.
5. **Debit Source (Recurring)** — Classify recurring debits by source: bank account or credit card.

---

## Disambiguation Decision Matrix

| Decision Stage | Retail Bot Prompt | SME Bot Prompt | UI Widget | Routing Outcome |
|---|---|---|---|---|
| Entry | "I can help with payment or charge issues. Let's understand what happened." | "I'll help identify the transaction issue." | Text | Enter transaction funnel |
| 1. Attempt vs Past | "Is this about a payment you just tried to make, or something you noticed later?" | Same as Retail | Quick replies | Initiation issue or Post-transaction |
| 2. Debit Confirmation | "Was the amount deducted from your account or card?" | Same as Retail | Quick replies | Status check or Debit analysis |
| 3. One-time vs Recurring | "Was this a one-time charge, or is it happening repeatedly?" | Same as Retail | Quick replies | One-time debit or Recurring debit |
| 4A. Payment Rail (One-time) | "How did you make this payment?" (UPI / Card / Bank transfer) | "Please confirm the payment type." | Quick replies | Failed UPI / Card / IMPS-NEFT |
| 4B. Debit Source (Recurring) | "Where is this recurring deduction happening from?" (Bank / Card) | Same as Retail | Quick replies | NACH dispute or Card subscription |
| 5. Routing Acknowledgement | "Got it. I'll check this for you." | "Understood. Proceeding." | Text | Enter resolution flow |

---

## Disambiguation Scenarios

**Scenario 1 — One-time:**
User: Money is getting deducted wrongly.
Bot: I can help. Is this a one-time charge or is it happening repeatedly? [One-time] [Recurring]
User: One-time
Bot: Thanks. Where was this payment made from? [UPI] [Card] [Bank Transfer]
→ Routed to: Failed UPI / Card / IMPS-NEFT

**Scenario 2 — Recurring:**
User: Every month some amount goes from my account.
Bot: Got it. Is this deduction happening repeatedly? [Yes] [No]
User: Yes
Bot: Where is this recurring charge coming from? [Bank Account] [Credit Card]
→ Routed to: Auto Debit / NACH or Credit Card Subscription

**Scenario 3 — Dual intent:**
User: I paid today but also something gets deducted every month.
Bot: Understood. Let's take this one issue at a time. Are you asking about a payment you just tried, or a regular deduction? [Just tried to pay] [Regular deduction]
→ Prevents accidental routing to recurring dispute

**Scenario 4 — Ambiguous:**
User: I'm not sure, I just noticed money missing.
Bot: No problem. Let's check step by step. Did this happen once, or have you noticed it more than once? [Once] [More than once]
User: More than once
Bot: Thanks. Is this deduction from your bank account or credit card? [Bank Account] [Credit Card]
→ Ambiguity resolved without forcing technical terms

---

## Language Handling

- **Mid-conversation detection** — System detects language switches during an active conversation and does not assume user intent or preference.
- **Explicit user choice** — When a switch is detected, the bot offers clear language options instead of auto-translating, preserving clarity and consent.
- **Fail loudly, not silently** — If translation services are unavailable, the bot clearly communicates the limitation rather than degrading silently or producing partial responses.

---

## Design Trade-Offs

- Speed → Safety: Verification before escalation
- Simplicity → Precision: Persona-based control threshold
- Convenience → Auditability: Mandatory explicit confirmation
