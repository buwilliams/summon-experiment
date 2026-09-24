# legacy-rewrite/critical-rationalism/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:39:51.328985+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

## Response

# Rewrite vs. Incremental Modernization: Which Conjecture Survives Criticism?

## 1. What each belief actually claims

Both positions are claims about **where the cost of change lives**.

**The CTO's conjecture:** The cost is structural and pervasive. The coupling runs so deep (shared data model, tangled business logic, a runtime and deployment model that can't be isolated) that no clean seams exist. Any extraction drags half the system with it. Improving the parts can't fix the whole, so replace the whole.

It also carries a hidden second claim, usually the weaker one: **that your team can specify what the old system does well enough to rebuild it in two years.** In P&C policy admin, "what it does" means rating across states and lines, filings, out-of-sequence endorsements, mid-term changes, cancellations and reinstatements, audits, and 20 years of customer-specific quirks. Much of that exists only in the code and in the heads of people who have already left.

**Head of product's conjecture:** The cost is concentrated. It sits in hotspots, and the system has natural seams: document generation, billing integration, portals, reporting, perhaps rating for a single line. You can route around it capability by capability while the old system keeps earning. The hidden claim here is that **the organization can sustain two systems and split capacity** between migration and features for years without stalling in a permanent half-migrated state.

## 2. Differential predictions: what you'd see if each were true

| Observation | If the CTO is right | If product is right |
|---|---|---|
| Git co-change history | Changes for typical features touch many modules across the codebase, fairly uniformly | Changes cluster in a small number of hotspot files/modules |
| Data model | Core tables read and written from everywhere; no module "owns" anything | Some capabilities have identifiable data ownership or narrow interfaces |
| Timeboxed extraction of one real capability | Scope explodes; touches a large fraction of the system; can't reach production in ~2 months | Reaches production (or shadow traffic) with a bounded set of touchpoints |
| Feature lead time breakdown | Most elapsed time is spent in coding/rework caused by ripple effects | Coding time is modest; delays concentrate in specific areas |
| Bug patterns | Regressions appear far from where changes were made | Regressions are local to the hotspots |

If you can't name which column your system falls into, neither side has earned its confidence yet.

## 3. Where each explanation is easy to vary

**The CTO's view:**
- "Incremental fixes will never get us out of the hole" absorbs any outcome. A failed increment confirms it. A successful one "just delays the inevitable." An explanation no observation could embarrass isn't telling you much.
- "Two years" can't be checked until year two. Rewrites reliably look great early, because greenfield velocity is high and the easy 80% gets built first. They stall on the long tail of edge cases that only surface when you try to match production behavior. Early progress is therefore not evidence for the timeline.
- Rewrites have long feedback loops by design. The main hypothesis, that the new system correctly replaces the old, isn't tested against reality until cutover. That is a structural weakness: the plan resists criticism during exactly the period when criticism is cheapest.

**Head of product's view:**
- "One capability at a time" can absorb slow progress indefinitely ("we just need more time"). Strangler efforts commonly die in a permanent dual-system state that is worse than either endpoint.
- "While continuing to ship features customers are asking for" is aspirational. It's unfalsifiable unless someone commits to a capacity split and a migration rate.
- "Carve off a capability" quietly assumes seams exist. That is precisely what the CTO denies, and it hasn't been demonstrated.

**The fix for both:** make each side commit *in advance* to what would count as failure, including a number and a date.

## 4. Cheapest tests that could refute each soon

**Test A: Lead-time decomposition (days, nearly free; could refute both).**
Take the last 15–20 shipped features and break elapsed time into:
- requirements and waiting
- coding
- rework
- QA and regression testing
- release scheduling
- deployment
- regulatory or customer sign-off

If coding plus architecture-driven rework is a small share of "months per feature," then neither a rewrite nor a strangler addresses the main problem. A new stack with the same manual QA and quarterly release train will also take months.

**Test B: Change-coupling analysis (1–2 weeks).**
Mine version control for co-change patterns and hotspots (churn × complexity; tools like CodeScene or simple scripts work).
- Uniform, widespread coupling supports the CTO.
- Concentrated hotspots with loosely coupled regions support product.

This is cheap and hard for either side to argue with.

**Test C: Timeboxed extraction spike (6–8 weeks; the direct test of product's view).**
- Pick a *representative* capability, not the easiest one. Document generation plus one integration is reasonable; rating for one line in one state is harder and more informative.
- Before starting, have product write down predicted touchpoints, scope, and what "in production" means (live or shadow traffic).
- If the team can't get it running against real traffic, or the touchpoint count blows past the prediction by a large factor, product's conjecture is seriously damaged.

**Test D: Specification recovery (6–8 weeks; the direct test of the CTO's timeline).**
- Pick one line of business in one state.
- Write characterization tests of current behavior, or rebuild that rating and policy logic on the new stack.
- Replay a sample of historical transactions (new business, endorsements, cancellations, out-of-sequence changes) through both and measure discrepancy rate and time to reach parity.
- Multiply by the number of states × lines × transaction types.

If one slice takes a small team two months to match, the two-year from-scratch plan is refuted by arithmetic. If it's fast and the discrepancies are few, the CTO's plan gains real credibility.

**Test E: Check the external facts (a week or two).**
- Pull win/loss data. Have you actually lost deals to the "cloud-native" competitors, and what did buyers say they wanted?
- Review exit interviews for why engineers left.

These facts are driving the urgency. They may not support either strategy as stated.

## 5. A third explanation that may fit the facts better

Look at the facts you gave: slow features, attrition, competitors' marketing. Both conjectures assume these are caused primarily by **code architecture**. A competing explanation:

**The bottleneck is mainly the delivery system and knowledge loss, not the architecture.** Candidate causes:
- no automated regression tests, so every change needs weeks of manual QA
- infrequent release trains
- environment and deployment friction
- business rules that only a few departing people understand
- the domain's *essential* complexity (state-by-state rules) that any stack will have

Engineers may be leaving because they can't ship, because on-call is painful, because the stack hurts their careers, or over pay. Those causes call for different fixes. "Cloud-native," for your buyers, may really mean SaaS delivery, APIs, and letting business users configure products and rates without code changes. You might deliver some of that without rewriting the core.

This explanation predicts specific things:
- Test A shows most lead time outside coding.
- Test B shows moderate, not catastrophic, coupling.
- Test D reveals that the scarcest resource is *knowledge of current behavior*.

If that's what you find, the first priorities are characterization tests, deployment automation, and capturing domain knowledge. They are prerequisites for *either* strategy. They also make the rewrite-vs-strangler question much cheaper to answer later.

Notice also that the dichotomy is partly false. A rewrite that ships to production in slices, with parallel runs against the old system, *is* a strangler. The real disagreement is how long you go without production feedback: weeks, or two years.

## 6. Which survives criticism right now

**The from-scratch, two-year, big-cutover rewrite survives worse.**
- Its central claims (that the old behavior can be specified and replicated on schedule) are the least tested and the hardest to test until late.
- The base rate for such rewrites of revenue-critical domain systems is poor.
- Its failure mode is severe and hard to reverse: years of frozen features, customer churn, and possibly two systems anyway.

**Head of product's view survives better, but only conditionally.** It rests on an unverified claim that seams exist and on an unenforced claim about capacity. Its main advantage is not that it's more plausible. It's that it produces short feedback loops, so you find out whether it's wrong quickly and cheaply.

**Suggested decision rule:**
1. Run Tests A, B, and E immediately. They take weeks and cost almost nothing.
2. Run C and D in parallel over the next quarter, each with predictions written down in advance by the person advocating that strategy.
3. Choose based on what the tests show:
   - If C fails badly and B shows pervasive coupling, the CTO's diagnosis is right. Even then, structure the replacement to reach production in slices, not as one cutover.
   - If C succeeds and D shows the spec-recovery cost is large, go incremental.
   - If A shows that most of the delay isn't in code, fix the delivery pipeline first, whatever else you decide.

## Summary (sent to Jev)

The response treats both positions as competing claims about where the cost of change lives. The CTO assumes coupling is pervasive, with no clean seams, and implicitly assumes the team can specify twenty years of P&C behavior well enough to rebuild it in two years. The head of product assumes the cost sits in hotspots with natural seams, and implicitly assumes the organization can run two systems and split capacity for years without stalling half-migrated.

The response criticizes both views as easy to vary. The claim that "incremental fixes will never get us out of the hole" can absorb any outcome. Rewrites look fast early but stall on edge cases and get no production feedback until cutover. "One capability at a time" can excuse endless slow progress, and "continuing to ship features" means nothing without a committed capacity split. Each side should commit in advance to failure criteria with numbers and dates.

It proposes cheap tests:
- **Test A:** break down lead time on recent features.
- **Test B:** mine version control for change coupling.
- **Test C:** a six-to-eight-week extraction spike on a representative capability, with predictions recorded beforehand.
- **Test D:** specification recovery for one line in one state, replaying historical transactions to measure time to parity.
- **Test E:** check win/loss data and exit interviews.

It offers a third explanation: the bottleneck may be the delivery system and lost domain knowledge rather than architecture. If so, characterization tests, deployment automation, and knowledge capture come first under either strategy. It also notes that a sliced rewrite with parallel runs is itself a strangler.

Its conclusion is that the two-year big-cutover rewrite survives criticism worse. The incremental approach survives better only conditionally, mainly because it gives fast feedback. The recommendation is to run Tests A, B, and E now and C and D over the next quarter, then decide based on the results, fixing the pipeline first if delay lies outside the code.
