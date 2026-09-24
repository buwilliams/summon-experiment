# legacy-rewrite/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T13:01:16.166294+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

## Response

# Rewrite vs. Incremental Modernization: Treating Both as Conjectures

Both positions are really explanations of why change is slow, with remedies attached. If you evaluate them as remedies ("which plan sounds better?"), you'll get a debate. If you evaluate the explanations underneath, you can test them, fairly cheaply, within weeks.

## 1. What each conjecture actually claims

**The CTO's conjecture (rewrite):**
- **Cause:** The slowness is intrinsic to the architecture and stack. Coupling, obsolete technology, and accumulated cruft are spread so uniformly that no local improvement meaningfully lowers the cost of change.
- **No viable path:** There is no sequence of intermediate states that are each shippable and each cheaper to change than the last.
- **Feasibility:** Your team can reproduce 20 years of encoded behavior in about two years. That includes rating rules, state-specific variations, endorsements, cancellations and reinstatements, renewals, audits, forms, and regulatory edge cases.
- **Market:** Customers are choosing competitors because of architecture, not features, price, or implementation time.
- **Durability:** The new system won't decay the same way. This only holds if the decay was caused by technology rather than by process, staffing, or product decisions.

**The head of product's conjecture (incremental / strangler):**
- **Cause:** The cost of change is concentrated in identifiable hotspots, not spread evenly.
- **Seams:** The system has seams, or seams can be created, so capabilities can be extracted behind stable interfaces.
- **Value:** Each extraction pays for itself in faster change in that area while revenue keeps flowing.
- **Retention:** Engineers will stay if they work on the new parts.
- **Market:** Customer demand is primarily for features and responsiveness, which incremental work serves.

Notice what both conjectures share: **both assume the architecture is the main cause of slowness.** They disagree only on the remedy. That shared assumption is the least examined claim in the room (section 5).

The real crux between them is narrow: **does a viable incremental path exist?** The CTO claims it doesn't. The head of product claims it does. That can be tested directly.

## 2. Distinguishing predictions

If each were true, what would you observe that you wouldn't expect under the other?

| Observation | Expected if CTO is right | Expected if Product is right |
|---|---|---|
| Distribution of change cost across the codebase | Roughly uniform. Even "simple" changes in quiet areas take months. | Concentrated. A few modules absorb most of the effort and defects; changes elsewhere are fast. |
| Git history (churn × complexity) | Change and defects are spread widely; no small set of hotspots explains most pain. | A small fraction of files accounts for most churn and bugs. |
| Data coupling | Many modules write to the same core tables (policy, transaction, coverage) directly or via stored procedures. No capability can be isolated without touching the shared model. | Some capabilities read and write mostly their own data, or can be put behind an interface without rewriting the core model. |
| Attempts to extract one capability | Stall on coupling: every interface you define leaks, and the "extracted" piece keeps needing core changes. | Extraction is hard but finishes, and change speed in that area measurably improves afterward. |
| Past incremental efforts | Failed for structural reasons (you couldn't decouple it). | Failed for organizational reasons (deprioritized, understaffed, no end state) or haven't really been tried. |
| Lost deals | Prospects cite architecture, hosting, APIs, or scalability. | Prospects cite missing features, implementation time, or price. |

Two observations would hurt **both** conjectures:
- **Lead time dominated by waiting.** If most of the "months" per feature is queues, manual regression, release trains, compliance sign-off, or requirements churn, neither a rewrite nor a strangler addresses the actual bottleneck.
- **Attrition driven by something else.** If exit interviews say people left over pay, management, on-call burden, or lack of autonomy, a new stack won't fix that.

## 3. Where each explanation is easy to vary

An explanation is weak when it can absorb any outcome.

**The CTO's position:**
- **"Incremental fixes will never get us out of the hole" is unfalsifiable as stated.** Any incremental success can be dismissed as "just delaying the inevitable." Any rewrite slip can be explained as "we needed more time and people." Ask: *what incremental result, by what date, would make you abandon the rewrite?* If the answer is "none," it's a commitment, not a conjecture.
- **"Two years" is unanchored.** It's not derived from an inventory of the behavior that must be replicated. It's a number that sounds tolerable. Rewrites of core insurance systems are notorious for multi-year overruns. That base rate isn't proof, but it shifts the burden of evidence.
- **"Modern stack" is unspecified.** Unless it's tied to a specific mechanism (e.g., "product configuration without code changes," "per-tenant deployment," "automated regression that runs in an hour"), it can mean whatever makes the plan look justified.
- **The "cloud-native competitors" premise is borrowed from their marketing.** It hasn't been shown that customers are leaving for that reason.
- **The hidden cost is flexible too.** During a rewrite, either the old system freezes (customers wait two years for features) or the team splits and the rewrite chases a moving target. The plan rarely specifies which.

**The head of product's position:**
- **"Incremental" can absorb slow progress indefinitely.** "It's a marathon" explains any pace. Without a target architecture and dated milestones, a strangler becomes a permanent second system: two stacks, two sets of expertise, same core.
- **"One capability at a time" doesn't say which, or how the data problem is solved.** In policy administration, the hard part is usually the shared policy and transaction data model, not the application code. A strangler that only peels off the periphery (documents, notifications, reporting) can declare success while the core stays untouched.
- **No kill criterion.** What result would show the strangler approach can't reach the core? If there isn't one, it's as unfalsifiable as the rewrite.

**Bottom line on falsifiability:** the CTO's position makes more claims, bigger claims, and currently vaguer ones. The head of product's position makes fewer, more modest claims, but in its current form it is also too easy to vary. Neither survives criticism as stated. Product's survives better, provided it's sharpened.

## 4. The cheapest tests that could refute each soon

All of these fit in roughly 6–8 weeks, most in parallel.

**Test A: Lead-time decomposition (about 1–2 weeks; hits both)**
- Take the last 15–25 shipped features.
- For each, split the elapsed time into active engineering, waiting for QA or regression, compliance or regulatory validation, release scheduling, requirements rework, and environment or deployment issues.
- **Refutes the shared assumption** if active coding and design is a minority of elapsed time. Then the architecture isn't your main bottleneck.

**Test B: Hotspot analysis (about 1 week; discriminates CTO vs. Product)**
- Run a churn × complexity and defect-density analysis on version control history.
- **Refutes Product** if pain is spread widely with no concentration.
- **Refutes CTO's "uniform decay" claim** if a small fraction of the code explains most of the cost.

**Test C: Time-boxed extraction spike (6–8 weeks; tests Product directly)**
- Pick one capability that is both high-demand and plausibly separable, ideally closer to the core than documents or notifications (e.g., rating, or quote/bind APIs).
- Fix success criteria in advance: a defined interface, production traffic (even shadowed), and measurably faster change in that area.
- **Refutes Product** if you can't define a non-leaking interface because of shared writes to the core model. Note what this would and wouldn't show: it supports the CTO's coupling claim, but says nothing about whether a two-year rewrite is feasible.

**Test D: Vertical-slice rewrite (6–8 weeks for a scoped estimate; about 3 months to execute; tests CTO directly)**
- Before committing two years, have the rewrite advocates first *inventory* the behavior: products, states, rating rules, form variations, transaction types.
- Then estimate and build one complete vertical slice in the new stack, e.g., one line of business in one state, covering quote, issue, endorse, cancel, reinstate, and renew.
- Compare actual effort against the estimate, then extrapolate.
- **Refutes the two-year plan** if the slice runs substantially over, or if the inventory implies far more than two years at the observed rate. This is the single most important test, because it replaces an intuition with a measured rate.

**Test E: Loss and churn analysis (about 2 weeks; tests the market premise shared by the CTO's urgency)**
- Review deals lost and customers churned in the last two to three years, and interview around 10 customers or prospects.
- Separate "cloud-native" into what they actually want: vendor-hosted SaaS, faster product and rate changes, modern APIs, shorter implementations, or lower IT burden.
- **Refutes the CTO's urgency** if losses trace to features, price, or implementation time. And if "cloud" turns out to mean "you host it and we don't run infrastructure," some of that demand could be met by offering managed hosting of the existing system, far sooner than any rewrite.

**Test F: Attrition review (about 1 week)**
- Re-read exit interviews and talk to recent departures if possible.
- Distinguish "the stack is miserable" from "every change is terrifying because nothing is tested" and from pay, management, or career-growth reasons. Each points to a different remedy.

## 5. A third explanation that may fit the facts better

**Conjecture:** *The primary cause of slowness is not the architecture itself but the absence of fast, trustworthy feedback, combined with erosion of knowledge.*

In practice that means some combination of:
- **No automated safety net.** Few characterization or regression tests, so every change needs long manual regression and regulatory validation.
- **Knowledge concentrated in a shrinking group.** Each departure makes the next change slower and scarier, which drives further departures. This is a loop, not a one-off problem.
- **Product behavior hardcoded rather than configured.** In policy administration, much of "feature work" is really insurers wanting new products, rates, forms, or state variations. If those require vendor code changes instead of configuration, every customer request becomes an engineering project. Configurability is often the real competitive capability behind "modern" competitors.

**What this predicts, distinctly from both other conjectures:**
- Lead time is dominated by testing and validation rather than coding (Test A).
- Changes made by long-tenured engineers are much faster than the same kinds of changes made by newer ones.
- Lead time steps up after key departures.
- A large share of feature requests are product, rate, or form variations.
- Exit interviews mention fear of breaking things, pager burden, or being stuck as "the only one who knows X."

**Why it may explain the facts better:**
- It accounts for *all* of your facts, including why the system works (the behavior is correct) and why good engineers leave (the work is high-risk and low-autonomy). The architecture-centric conjectures don't explain the attrition loop well.
- It explains why a rewrite is riskier than it looks. The new system needs an oracle to prove parity, and the people who understand the old behavior are the ones leaving.
- It implies a **no-regret first move either way:** build a characterization test harness that replays real production transactions through the system and records outputs. That harness is a prerequisite for a strangler (to verify extracted pieces match), a prerequisite for a rewrite (to prove parity), and a remedy on its own if this third conjecture is correct. Building it also tests the conjecture. If lead time barely improves in the areas it covers, the third conjecture is weakened.

## 6. So which strategy survives?

**As currently stated:**
- **The CTO's rewrite** makes the most claims and the least tested ones. Its specific form ("from scratch, two years") is contradicted by base rates and unsupported by any inventory of the behavior to be replaced. It should not be adopted on current evidence.
- **The head of product's strangler** survives criticism better, because its claims are smaller and it keeps revenue and customer trust intact while you learn. But it only deserves to be called a strategy once it has a target architecture, an explicit plan for the core data model, dated milestones, and a kill criterion.
- **The third explanation** is plausible enough, and cheap enough to check, that it should be tested alongside the other two.

**A decision rule based on the test results:**

| If the tests show... | Then... |
|---|---|
| Lead time mostly waiting and validation; attrition driven by fear or knowledge silos | Lead with test harness, release automation, and configurability. Architecture work comes second. |
| Pain concentrated in hotspots; extraction spike succeeds | Adopt the strangler with a defined end state and a core-data plan, targeting hotspots first. |
| Pain uniform; extraction spike fails on core data coupling; vertical-slice rewrite hits its estimate | The rewrite case is now real. Do it as an incremental replacement, one line of business and one state at a time with parallel running, never as a big-bang cutover. |
| Losses driven by hosting and ops burden, not features | Offer managed or SaaS hosting of the current system as a near-term competitive answer, independent of the longer-term architecture decision. |

Even in the case most favorable to the CTO, the evidence wouldn't support a big-bang rewrite. It would support a replacement delivered in slices, which is closer to the head of product's method with the CTO's end state.

**The most useful thing you can do now** is get both leaders to agree, in writing, which test outcomes would change their minds before the results come in. Whoever can't name a result that would refute their position is holding a preference, not a conjecture.

## Summary (sent to Jev)

The response treats both positions as testable explanations of why change is slow, not as competing plans. The CTO's rewrite assumes slowness is spread uniformly through the architecture, that no incremental path exists, that 20 years of behavior can be rebuilt in two years, and that customers leave over architecture. The head of product's strangler assumes cost is concentrated in hotspots, that seams exist or can be created, and that extractions pay for themselves. Both share an unexamined assumption that architecture is the main cause, and the real crux is whether a viable incremental path exists.

Both positions are criticized as too easy to vary. "Incremental fixes will never work" is unfalsifiable, and "two years" is unanchored against base rates of overruns. The strangler lacks a target architecture, a plan for the shared policy data model, milestones, and a kill criterion.

It proposes cheap tests over about 6–8 weeks:
- decomposing lead time for recent features
- hotspot analysis of version history
- a time-boxed extraction spike on a near-core capability like rating
- an inventory plus a vertical-slice rewrite of one line of business in one state, which it calls the most important test
- analysis of lost deals and churn
- an attrition review

It offers a third explanation. Slowness may stem from missing fast, trustworthy feedback, eroding knowledge, and hardcoded product behavior. This implies a no-regret first step: a characterization test harness that replays production transactions.

It concludes that the rewrite should not be adopted on current evidence. The strangler survives better but only once sharpened. Even if the CTO is vindicated, replacement should proceed in slices, never as a big-bang cutover. Both leaders should agree in writing beforehand which outcomes would change their minds.
