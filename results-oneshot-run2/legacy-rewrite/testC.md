# legacy-rewrite/testC

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T13:00:08.774102+00:00

## Prompt

Use the method of conjectures and refutations (critical rationalism) to answer the following.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

# Rewrite or Modernize Incrementally? A Conjectures-and-Refutations Analysis

Critical rationalism doesn't ask which proposal sounds most visionary or which executive is more senior. It treats each strategy as a **conjecture**: a bold guess about what is wrong and what will fix it. Then it tries hard to **refute** each one and tentatively keeps whatever survives. So the method is to state both theories precisely, expose their hidden claims, attack those claims, and design tests that could prove either side wrong.

## 1. Start with the problem

Popper insisted that inquiry starts from problems, not solutions. You've described three symptoms:

1. Features take months.
2. Your best engineers leave.
3. Competitors market themselves as "cloud-native."

Both proposals assume these symptoms share one cause: the old codebase. That is itself a conjecture, and it's the first thing to test (section 5). If it's false, both strategies could fail.

## 2. Conjecture A: Rewrite from scratch in two years

**Hidden claims.** For the rewrite to succeed, all of these must be true:

- **A1.** The codebase is the dominant cause of slow delivery and attrition.
- **A2.** Your team can reproduce 20 years of encoded business behavior in about two years.
- **A3.** Customers and the market will tolerate a long period of reduced feature delivery.
- **A4.** In-force policies can be migrated safely and in compliance with regulators.
- **A5.** The new system won't reacquire the old one's problems, even though the same organization is building it.

**Attempted refutations:**

- **Against A2: the old system is the specification.** In P&C, the hard part isn't the tech stack. It's the domain logic:
  - state-specific rules and filed rates
  - form versions
  - out-of-sequence and backdated endorsements
  - cancellation and reinstatement edge cases
  - audits, and ties to billing and claims

  Much of this is documented nowhere except in code and in the heads of people who have partly left. Rewrites routinely find that "simple" legacy behavior is load-bearing. Brooks's second-system effect and the long record of overrun core-insurance replacements are strong evidence against the two-year estimate. It's the most falsifiable prediction on the table, and base rates suggest it's likely wrong by a large factor.
- **Against A3: competitors keep shipping.** A rewrite usually means years of splitting effort between frozen legacy maintenance and a system that earns no revenue. The two cloud-native competitors don't pause while you rebuild.
- **Against A4: migration is a project of its own.** Moving policies with multi-year histories and regulatory obligations often needs parallel running and reconciliation. Two-year plans frequently leave this out.
- **Against A5: rewrites delay feedback.** A big-bang rewrite gets its decisive feedback at the end, when a live, full-scope cutover finally happens. Errors in architecture, scope, or domain understanding pile up undetected. This is Popper's critique of "utopian" engineering in *The Open Society*: blueprint plans can't be corrected mid-course, because you learn whether they work only when it's too late to change them cheaply.
- **Against the attrition rationale.** A rewrite may excite engineers at first. But the people left maintaining legacy become second-class, and when the rewrite slips, morale usually collapses harder than before.

**What survives of A.** One criticism aimed at B holds up: **incrementalism can become permanent drift.** The CTO is right that the hole is real and that cosmetic, feature-by-feature patching won't get you out. Keep this; it will reshape B.

## 3. Conjecture B: Incremental modernization ("strangler fig")

**Hidden claims:**

- **B1.** The system has seams where capabilities can be intercepted and replaced behind the existing system.
- **B2.** Each carved-off piece actually reduces the cost of changing the core.
- **B3.** The organization will keep funding modernization while also shipping customer features.
- **B4.** The effort will eventually retire legacy code, not just surround it.

**Attempted refutations:**

- **Against B1: the database may be the monolith.** If everything reads and writes the same tables, the real coupling is the data model, not the code. Carving off a service while sharing that database gives you distributed-system complexity with none of the independence.
- **Against B2 and B4: strangler efforts often stall at the easy edges.** Portals, document generation, and reporting get modernized. The hard core (rating, policy transactions, the endorsement engine) stays, and you end up running more systems than before. This is a real, common failure mode.
- **Against B3: "keep shipping features" can eat the modernization budget.** Product leadership has a structural incentive to trade next quarter's modernization for this quarter's customer request. Without protection, B quietly turns into "business as usual with a new slide deck."

**What survives of B.** Its core virtue holds up: **error-correctability.** Every slice goes to production, produces feedback, and can be stopped or reversed. This is Popper's "piecemeal engineering." The claim isn't that small steps are always better. It's that a plan you can falsify quarterly beats a plan you can falsify only after two years.

## 4. Conjecture C: A strengthened synthesis

Critical rationalism advances by replacing refuted theories with better ones, not by picking a winner. Folding the surviving criticisms into B gives a stronger conjecture:

> **Incremental modernization with a committed end-state, protected capacity, and decommissioning targets. Use greenfield builds where the domain allows it, especially for new business.**

Concretely:

- **Define a target architecture and a sunset date for legacy.** This answers the CTO's drift objection. Measure progress in **legacy capability retired**, not in new services launched.
- **Protect modernization capacity** (for example, a fixed share of engineering) so feature pressure can't eat it. This answers B3.
- **Attack the data model early**, not just the UI edges. Introduce events or change-data-capture so new components can own their data.
- **Consider "new business on new platform" by line of business.** This pattern is common in insurance: write new policies for one line in one or a few states on a new stack, and migrate the in-force book at renewal rather than all at once. It captures much of what the rewrite promises (modern stack, clean domain model, a real cloud-native offering) while keeping feedback loops short and migration risk bounded. It is effectively a rewrite, but one done in falsifiable increments.
- **Fix the delivery pipeline now**: automated regression tests around legacy behavior, CI/CD, and cloud hosting where feasible. These pay off whichever architecture wins. Tests that capture current behavior are also the specification any replacement will need.

## 5. Tests that could prove me wrong

A conjecture worth holding says what would refute it. Run these over the next 60–90 days, and have each leader **write down predictions in advance**:

| Test | What it checks | Result that would weaken C |
|---|---|---|
| **Value-stream map of 3–5 recent features.** Where did the months actually go? | The shared assumption that code is the bottleneck | If most lead time is regulatory filing, approvals, or requirements churn, *neither* architecture strategy is the main fix. Process is. |
| **Seam spike.** Carve off one meaningful capability (e.g., rating for one line) behind the old system within a quarter. | B1: decomposability | If even one slice proves nearly impossible because of data coupling, the case for a line-of-business greenfield, or even a fuller rewrite, gets much stronger. |
| **Rewrite calibration.** Have the CTO's team build one complete thin slice (one line, one state, including out-of-sequence endorsements and a sample migration) and compare actual effort to their estimate. | A2: the two-year plan | If they hit their estimate closely, the rewrite's central claim survives a real test and deserves more weight. |
| **Win/loss analysis on recent deals** | Whether "cloud-native" actually costs you revenue | If you aren't losing deals over it, competitive urgency is lower than assumed, which favors lower-risk paths. |
| **Structured exit and stay interviews** | Whether attrition is about the stack or about pay, on-call load, and being seen as a maintenance team | If the stack isn't the driver, a rewrite won't fix retention. |

## 6. When the rewrite would be right

My conclusion should be abandoned if any of these turn out to be true:

- The platform's runtime, language, or infrastructure is losing vendor support, or can't meet security and compliance requirements, so staying isn't an option.
- The seam spike shows the system truly can't be decomposed.
- The rewrite calibration shows the team estimates accurately and can deliver full domain parity quickly.
- The business is small or narrow enough that one product line covers most revenue, which shrinks the rewrite's scope.

## Tentative verdict

Neither leader's position survives criticism unchanged.

- **The CTO's big-bang rewrite** makes the boldest and most falsifiable claim, parity in two years. The evidence and base rates weigh heavily against it, and its long feedback loop means you'd learn it failed only after the money is spent.
- **The head of product's incremental approach** survives better because it can correct its own errors. In its naive form, though, it's vulnerable to drift and to feature pressure eating the budget.

The best-surviving conjecture is **incremental modernization hardened by the CTO's critique**:

- a committed end-state
- protected capacity
- decommissioning metrics
- early work on the data model
- greenfield new-business platforms by line of business where feasible

Hold it tentatively, and let the tests in section 5 decide rather than seniority or conviction. Asking both leaders to state in advance what evidence would change their minds may also be the most valuable thing you do: it turns a political standoff into a shared inquiry.

## Summary (sent to Jev)

The response treats both strategies as conjectures to be tested and tentatively recommends neither in pure form. Instead it favors incremental modernization strengthened by the CTO's critique. It first notes that both proposals assume slow delivery, attrition, and competitive pressure all stem from the old codebase, and that this assumption itself needs testing.

It argues the big-bang rewrite fails on several hidden claims. The legacy system is effectively the specification for twenty years of P&C domain logic, including state rules, forms, out-of-sequence endorsements, and cancellations, so the two-year estimate is likely wrong by a large factor. Competitors keep shipping during a rewrite, migrating in-force policies is a project in itself, and errors surface only at final cutover, echoing Popper's critique of utopian engineering. It keeps the CTO's valid point that incrementalism can become permanent drift.

The incremental approach is vulnerable because a shared database may be the real monolith, strangler efforts often stall at easy edges, and feature pressure can consume the modernization budget. Its strength is error-correctability.

The recommended synthesis combines several elements:
- a committed target architecture and a legacy sunset date
- protected engineering capacity
- progress measured by legacy capability retired
- early attacks on the data model
- "new business on new platform" by line of business, with the in-force book migrated at renewal
- immediate investment in regression tests and CI/CD

Over 60 to 90 days, it proposes value-stream mapping, a seam spike, a rewrite calibration slice, win/loss analysis, and exit and stay interviews, with each leader writing predictions in advance. The rewrite would be right if the platform is losing vendor support or can't meet compliance requirements, if the system proves undecomposable, if the team estimates accurately, or if the business is narrow.
