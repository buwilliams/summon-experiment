# legacy-rewrite/critical-rationalism/testC

Model: claude-opus-5-5 · 2026-09-24T15:24:25.656989+00:00

## Turn 1

**User:** Use the method of conjectures and refutations (critical rationalism) to answer the following.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

# Rewrite vs. Incremental Modernization: A Conjectures-and-Refutations Analysis

Critical rationalism doesn't ask "which strategy can be justified?" It asks which conjectures survive serious attempts to refute them, and which strategy lets us detect and correct our errors fastest. Let's apply that.

## Step 0: Start from the problem

You named three symptoms:

1. Features take months.
2. Your best engineers leave.
3. Competitors market themselves as "cloud-native."

Both proposals quietly assume these share one cause: the old codebase. That is itself a conjecture, and it could be false.

- Feature slowness might come from missing automated tests, manual regression cycles, release batching, or approval processes.
- Attrition might come from on-call pain, pay, or lack of career growth.
- "Cloud-native" might be losing you deals, or it might be marketing copy.

If the main cause lies elsewhere, both strategies fail. Hold that thought; it becomes the first test.

## Conjecture A: Rewrite from scratch in two years (CTO)

**What it implies:**
- The current architecture is the binding constraint.
- The team can reproduce 20 years of behavior in two years.
- The business can tolerate reduced feature delivery in the meantime.
- The new system will not accumulate the same problems.

**Attempted refutations:**

1. **Embedded knowledge.** A P&C policy admin system encodes two decades of state-specific rules, filed rating algorithms, form logic, endorsement edge cases, and fixes for incidents nobody remembers. Much of it lives only in code. Rated premiums on filed programs must reproduce exactly. You can't rewrite what you can't specify, and the spec is the old system.

2. **The moving target.** Customers keep demanding features and regulators keep changing requirements. You must either freeze the old system, which hands competitors two years, or build everything twice, which halves your capacity. Either way, parity keeps receding.

3. **Migration.** In-force policies, renewal histories, and billing states must move over mid-term without errors. This is often a project as large as the rewrite, and it usually comes last. So it comes when budget and patience are exhausted.

4. **No feedback until the end.** This is the decisive point in Popperian terms. A big-bang rewrite is what Popper called *utopian* or holistic engineering: so many variables change at once that when it goes wrong, you can't tell why. Mistakes surface only at cutover, when they are most expensive. The strategy is structurally hostile to error correction.

5. **Track record.** Large core-system replacements, especially in insurance, routinely overrun by multiples or get abandoned. "Two years" is not a measured figure; it is a hope.

6. **Does it address the cause?** If slow delivery comes from process and missing tests, the same organization will produce a new legacy system, just younger.

7. **Attrition.** A rewrite may excite engineers at first. But a two-year slog toward parity, while a skeleton crew maintains the old system, often drives people out.

**What survives:** The CTO is right that incremental fixes are often a euphemism for doing nothing, and that some architectural constraints can't be patched. A rewrite could be right if the stack is truly unhireable or unsupported, or if the market demands a capability the architecture can't support at all (such as multi-tenant SaaS). But "incremental fixes will never get us out" is an unfalsifiable prediction as stated. It needs to become testable.

## Conjecture B: Incremental modernization (Head of Product)

**What it implies:**
- The system has seams where capabilities can be separated.
- Carving them off yields real improvement.
- The effort will continue to completion rather than stall.

**Attempted refutations:**

1. **Strangler projects stall.** The common pattern: teams carve off the easy edges (documents, notifications, a portal) and never touch the hard core (the policy data model and rating engine). You end up running two systems forever, which is worse than one.

2. **Feature pressure eats the budget.** "Continue shipping features customers ask for" is a recipe for modernization always losing the quarterly priority fight.

3. **There may be no seams.** If everything shares one database, with triggers, stored procedures, and batch jobs touching every table, carving may be far harder than it sounds.

4. **It may be too slow for the market.** If competitors are actually winning deals on architecture, a decade-long strangle might be too slow.

**What survives:** The core structure. B keeps revenue flowing, gets production feedback every few months, and lets you learn where the real difficulty lies before committing everything. That is Popper's *piecemeal engineering*: small, reversible changes whose effects can be observed and corrected. But B as stated is too vague. It is vulnerable to refutations 1 and 2 and needs amendment.

## The surviving conjecture

The dichotomy is partly false. The real variable is not "rewrite vs. incremental." It is **the size of the unit of replacement and the length of the feedback loop.**

The conjecture that best survives criticism:

> **Modernize incrementally, but with teeth.**
> - Replace the system capability by capability, including large chunks rewritten on a modern stack.
> - Adopt one hard rule: no work stream goes more than about a quarter without something running in production against real traffic.
> - Fund modernization as a protected budget, not leftover capacity.
> - Sequence toward the core (rating and policy data), not away from it.
> - Consider a hybrid: new lines of business or new states launch on the new platform from day one, and in-force books migrate later, once the new platform has proven itself.

This gives the CTO most of what he actually wants: a modern stack, a path out, and permission to rewrite. It avoids the one feature of his plan that fails every test, which is two years of blindness.

## How to try to refute my conclusion

A critical rationalist doesn't stop at a conclusion. Here are tests you can run in six to ten weeks. Any of them could overturn what I've said.

1. **Diagnose lead time.** Trace five recent features from request to production and measure where the time went.
   - If most of it went to manual testing, release windows, or approvals, the codebase isn't the main problem. Fix that first, because neither strategy helps until you do.
   - If most of it went to fighting the code itself, the architectural hypothesis gains support.

2. **Run the seam test.** Pick one meaningful capability, ideally something near the core such as a rating component or one new state/program, and try to carve it out in 90 days.
   - If it proves nearly impossible because of coupling, that is real evidence for a more aggressive approach, perhaps a parallel core for new business only.
   - If it works, the CTO's "never" is refuted.

3. **Build a behavioral harness.** Capture production inputs and outputs (quotes, rates, forms, and transactions) into an automated comparison suite. You need this under *any* strategy, since no replacement is safe without it. How hard it is to build tells you how much hidden knowledge the system holds.

4. **Check the market claim.** Review lost deals from the past 18 months. Did "cloud-native" actually decide any of them, or did price, features, and implementation time? Also check whether hosting the current system as a managed cloud offering would neutralize the objection commercially.

5. **Check the attrition claim.** Reread exit interviews and talk frankly to people who stayed. Is it the stack, the toil, or the pay?

6. **Ask each advocate for a refutation condition.** Ask the CTO: "What result in the seam test would convince you incremental can work?" Ask your head of product: "What result would convince you it can't?" Anyone who can't answer holds a commitment, not a hypothesis.

## When the rewrite would win

I'd revise my answer if the evidence showed that:
- the seam test fails badly;
- the lead-time analysis puts most of the delay in the code itself;
- the stack is effectively unhireable or out of vendor support;
- lost deals trace directly to architectural limits that hosting can't fix.

Even then, the better form would be a new core for new business, grown alongside the old system, rather than a two-year blind replacement.

## Bottom line

The head of product's instinct is closer to right, but only if it is strengthened into protected, core-directed, production-every-quarter modernization. The CTO's diagnosis deserves testing, but his remedy fails the most important criterion: it maximizes the cost of being wrong and delays learning that you are. Run the tests above before committing. Let the evidence, not the org chart, settle it.

## Turn 2

**User:** Keeping with conjectures and refutations, how would you handle it if the lead-time trace comes back split roughly evenly between manual testing and fighting the code itself?

**Assistant:**

# When the Lead-Time Trace Comes Back Split Evenly

A 50/50 split is useful, but not in the obvious way. The obvious reading is "two problems, fix both." That reading assumes the two halves are independent, and they may well not be. The aggregate number hides the causal structure, so the next step is to form rival conjectures about that structure and find observations that discriminate between them.

## First, check the measurement

Before theorizing, try to refute the data itself:

- **Double counting.** When manual testing finds a regression, the fix is often logged as "fighting the code," and the retest as "testing." The same underlying problem then shows up in both columns.
- **A vague category.** "Fighting the code" should be split into:
  - understanding what the code does,
  - making the change safely,
  - fixing regressions the change caused.

  These point to very different remedies.
- **Averages hiding distribution.** An even split across five features might be three features that were mostly testing and two that were almost all code-fighting. Break it down by module. Most legacy systems have a few hotspots, areas with high change frequency and high complexity, where nearly all the pain concentrates.

If the split survives these checks, move on to the causal conjectures.

## Four rival conjectures

| Conjecture | Claim | Prediction if true |
|---|---|---|
| **C1: Independent problems** | Testing is slow for process reasons; the code is hard for architectural reasons. | Automating tests cuts testing time but leaves code-fighting time unchanged. |
| **C2: Code causes testing** | The code is untestable (tangled logic, shared database, no seams), so testing must be manual and exhaustive. | Automation is hard to build. Attempts stall on coupling. Testing time won't fall much until the code is restructured. |
| **C3: Missing tests cause code-fighting** | With no safety net, engineers spend enormous time reasoning defensively about every change. The code is ugly but not the binding constraint. | Once a solid regression suite exists, code-fighting time drops noticeably, even without architectural change. |
| **C4: Common cause** | Both stem from lost knowledge. Attrition means nobody knows what the system should do, so changes are slow and verification is exhaustive. | Both costs are highest where the original authors have left, and lowest where a long-tenured engineer remains. |

These have very different implications:

- **C2** strengthens the case for aggressive restructuring, even the CTO's.
- **C3** weakens it considerably. Much of the "code problem" would be a testing problem in disguise.
- **C4** means neither strategy works without deliberate knowledge recovery, and a rewrite would destroy the remaining knowledge fastest.

## The move that holds under every conjecture

Under all four conjectures, building an automated characterization suite (a capture-and-compare harness on real production quotes, rates, forms, and transactions) is worthwhile:

- **C1:** it fixes half the problem directly.
- **C2:** you need it before you can safely restructure anything.
- **C3:** it fixes most of the problem.
- **C4:** it recovers lost knowledge by recording what the system actually does.
- **Either strategy:** a rewrite needs it to prove parity, and a strangler needs it to prove each carved piece.

When one action is valuable under every live hypothesis, take it without waiting to know which hypothesis is true. Better still, taking it is also the experiment that tells you which one is true.

## Designing the discriminating test

Build the harness first in one or two hotspot modules, then measure lead time for the next several features that touch those modules. Compare against similar features in modules without the harness.

- **Testing time falls, code-fighting stays flat:** C1 survives. Run test automation and structural work as parallel efforts.
- **Both fall substantially:** C3 survives. The codebase is less of a villain than it looked. Scale the harness, and treat major restructuring as optional and targeted.
- **The harness is extremely hard to build because behavior can't be isolated:** C2 survives. That coupling is the architecture problem, now demonstrated rather than asserted. Restructure the hotspots, possibly by rewriting them as carved-out services.
- **Cost tracks ownership history more than module structure:** C4 survives. Pair any technical work with deliberate knowledge capture, and weigh retention of remaining experts as a first-order risk.

Also compare against the other test from before, the 90-day seam test. Run it in the same hotspot. If carving fails for the same reasons the harness struggled, the C2 evidence converges.

## What this does to the original question

The even split already weakens one position. The pure-rewrite conjecture implied the code was the dominant constraint. Half the time turned out to be elsewhere, and a rewrite doesn't remove the need for verification; it increases it, because you must prove parity.

But the split doesn't vindicate simple incrementalism either. If C2 survives, "carving off one capability at a time" will stall on precisely the coupling the harness exposed, and you'll need bolder moves in the core.

So the plan is:

1. **This quarter and next:** build the characterization harness in the hotspots.
2. **In parallel:** run the seam test in one of those hotspots.
3. **Refutation criteria, agreed in advance:**
   - If code-fighting time in harnessed modules hasn't fallen meaningfully after two quarters, C3 is refuted and the architecture argument gains weight.
   - If the harness can't be built in a hotspot within a quarter, C2 is corroborated.
4. **Then decide** how aggressive the structural work must be, based on which conjecture survived.

Getting the CTO and head of product to sign off on those criteria before results come in matters as much as the experiment. Otherwise each side will read the same numbers as confirmation, and you'll have gathered evidence without learning anything.

## Turn 3

**User:** Sticking with conjectures and refutations, what would you do if the CTO won't agree to any refutation criteria in advance?

**Assistant:**

# When the CTO Won't Commit to Refutation Criteria

The refusal is itself an observation, and like any observation it has more than one explanation. The worst response would be to jump to the most flattering one for your side ("he knows he's wrong") and treat it as settled. That would be exactly the dogmatism you're trying to avoid.

So apply the method to the refusal itself: form rival conjectures about why he refuses, then find ways to tell them apart.

## Rival conjectures about the refusal

| Conjecture | What's going on | What it predicts |
|---|---|---|
| **R1: The test is biased** | He thinks the experiment is rigged. A two-quarter harness pilot measures incremental gains and can't show a rewrite's payoff, which arrives in year two. | He objects to the specific design, not to criteria as such. He'll engage if invited to redesign it. |
| **R2: Tacit expertise** | His conviction comes from pattern recognition he can't reduce to metrics ("I've seen systems like this; they don't recover"). | He can't name numbers, but he can describe scenarios that would surprise him. |
| **R3: Status and framing** | Agreeing to criteria proposed by the incrementalist side feels like conceding the frame, and the argument has become about standing, not software. | He'd accept identical criteria if they came from a neutral party or were phrased in his terms. |
| **R4: Distrust of metrics** | He's seen lead-time numbers gamed or misread, and expects the data to be spun. | He'll accept criteria if he controls or co-owns the measurement. |
| **R5: Genuine immunization** | The belief is held in a form no evidence could touch. Any outcome will be reinterpreted as support. | He rejects every formulation, including ones he writes himself, and has an answer ready for any hypothetical result. |

Only R5 is the problem you fear. R1 through R4 are ordinary and fixable, and R1 may simply be correct.

## Discriminating between them

Test these in conversation, ideally one-on-one rather than in front of the head of product:

1. **Invite him to redesign the test.** "If this experiment is unfair to your position, what would a fair one look like?" Engagement suggests R1. Take his objection seriously, because the pilot really does favor short-horizon gains.
2. **Ask for surprises instead of criteria.** "What would you be surprised to see in six months if you're right?" This often works where "refutation criteria" fails. It sounds like curiosity rather than a trap, and it suits R2.
3. **Ask the question in reverse.** "What result would convince you the incremental approach has failed?" People who resist stating how they could be wrong will often happily state how the other side could be. Those statements have logical content too. If incrementalism failing looks like X, then not-X counts against his position.
4. **Offer symmetry.** Both sides state criteria at once, sealed until results arrive. If he accepts when the head of product is equally bound, that points to R3.
5. **Offer ownership of the measurement.** Let his people define and collect the lead-time data, which addresses R4.

## Translating into language he already uses

Much resistance is to the phrase, not the substance. Every serious engineering leader accepts milestones, stage gates, and kill criteria for a large investment. So ask:

- "For your rewrite plan, what should exist at month 6, 12, and 18 for us to know it's on track?"
- "At what point would we stop and reassess?"

Milestones are refutation criteria in business clothing. A rewrite plan with no intermediate checkpoints is a plan nobody would fund, and he likely knows that.

## If he still refuses

If every formulation fails, R5 gains support, though it isn't proven. Then:

1. **Derive the predictions yourself.** Popper's point applies here: a theory's testable consequences don't depend on its proponent's consent. They follow from its content. "Incremental fixes will never get us out of the hole" implies things. For example, a characterization harness can't meaningfully cut code-fighting time, and carving a hotspot will fail or yield nothing. Write these down, show them to him, and ask whether they fairly represent his view. If he says they don't, ask what does. Either way you learn something.
2. **Keep a dated record** of predictions from both positions before the results arrive. This guards against reinterpretation later, on both sides, including yours.
3. **Proceed with the no-regret action.** The characterization harness doesn't need his agreement to criteria. It's valuable under every hypothesis, including a future rewrite, which needs it to prove parity. Frame it that way: "Whatever we decide, we need this first." Refusing it would require arguing against his own plan's prerequisite.
4. **Move the criteria to where the decision is actually made.** A two-year rewrite is a capital allocation bet, likely millions of dollars plus most of the company's revenue at risk. If the CEO or board decides, it is entirely normal for them to require stage gates and kill criteria for any option. This isn't going around the CTO. It's putting the requirement where it properly belongs. Present both options with the same scrutiny, so it's clearly a standard for any big bet, not a trap for his.

## Guarding against your own dogmatism

Before concluding he's immunizing his view, run the same check on yourself and the head of product. Have you stated what would make you abandon incrementalism? Did the earlier answer (a failed seam test, a harness that can't be built) actually make it into the criteria you proposed? If your side's criteria are vague and his are demanded, the refusal might be a reasonable response to an asymmetric process.

Also recall that Popper didn't hold that unfalsifiable ideas are worthless, only that they must be criticized by argument rather than tested by experiment. Even if the CTO's view stays untestable, you can still examine it:

- Does it explain why the previous two decades of maintenance failed?
- Does it account for the migration and parity problems?
- Does it predict anything that the incremental view doesn't?

## Bottom line

Treat the refusal as a problem to diagnose, not a verdict on him. Try redesign, surprise questions, symmetry, shared measurement, and milestone language first. Most refusals dissolve under one of these.

If none work, write down the predictions his position implies, keep a dated record, proceed with the harness because it serves every option, and let the executive level require stage gates for any large bet. You don't need his agreement to learn from reality. You only need to make sure no one, including you, can rewrite the predictions after reality answers.

## Turn 4

**User:** Staying with conjectures and refutations, what should I do if the CEO sides with the CTO and green-lights the rewrite before the harness pilot even produces results?

**Assistant:**

# When the Decision Goes the Other Way

Once the CEO decides, the problem changes. It's no longer "which strategy is right?" It's "given that we're doing a rewrite, how do we make it as correctable as possible?" Popper's objection to utopian engineering was never that large plans are forbidden. It was that they must be built to expose their own errors early. You can pursue that aim inside the rewrite rather than against it.

But first, apply the method to the decision itself.

## Rival conjectures about why the CEO decided

Don't assume the CEO acted irrationally or was simply persuaded by rank. Consider the alternatives:

| Conjecture | What's going on | Implication |
|---|---|---|
| **D1: Information you lack** | Deal losses you haven't seen, a key customer threatening to leave, a partner requiring a modern platform. | Your analysis may rest on a false premise. Find out. |
| **D2: A different objective** | An acquisition, fundraising, or exit within a few years, where a "modern platform" story affects valuation more than delivery speed does. | The rewrite might serve a goal your framework never measured. Your criteria were aimed at the wrong target. |
| **D3: Trust and fatigue** | The CEO trusts the CTO's judgment and wanted the debate over. | The decision is more revisable than it looks, if new evidence arrives through the right channel. |
| **D4: Timing** | Waiting two quarters for pilot results felt like a cost in itself. | The disagreement was about the cost of delay, not about the strategy. |

Ask directly: "Help me understand what tipped it, so I can execute well." That's a legitimate question from the person who has to deliver.

If D1 or D2 is true, your earlier conclusion may be refuted, or at least aimed at the wrong problem. Update accordingly. A critical rationalist who learns that the goal was different should revise the analysis, not defend it.

## Disagree once, in writing, with predictions

Before committing, state your dissent once, clearly, and in a form that could prove you wrong:

- **What I expect to go wrong:**
  - Parity milestones slipping as undocumented rules surface.
  - Migration discovered late to be as hard as the build.
  - The old system starved of attention while it still carries the revenue.
  - Continued attrition among the people who hold legacy knowledge.
- **What would show I was wrong:** For example, the first real product slice in production within 9 months, rating parity demonstrated on actual policies within 12, and the delivery schedule holding within a stated margin.

Then commit. The purpose isn't to set up "I told you so." It's to create the dated record that keeps everyone honest, including you, when results arrive. Stating your refutation conditions also shows that you hold your view as a hypothesis, which earns you credibility later if the evidence turns your way.

## Make the rewrite correctable from inside

This is where your leverage is greatest. Most of what made the incremental approach sound can be built into the rewrite without reopening the decision. Present all of it as protecting the CEO's bet, because that's exactly what it does.

1. **Keep the harness, renamed.** It's now the rewrite's parity oracle. No new rating engine can go live without proving it reproduces filed rates on real policies. The CTO can't reasonably oppose this; his plan needs it more than yours did.
2. **Get to production early.** Push for the first slice of the new platform to handle real traffic within 6 to 9 months, not at year two. The best candidates:
   - **A new line of business or new state** on the new platform, with the in-force book left on the old system.
   - **Shadow mode:** run the new rating engine in parallel with the old one on live quotes, compare outputs, and act on nothing yet. This gives continuous, painless evidence of parity.
3. **Rehearse migration from the start.** Migrate a small, real slice of in-force policies in test environments within the first few months. Migration is where rewrites quietly die, so surface its difficulty while there's still time to respond.
4. **Stage gates the CEO owns.** Hold reviews at 6, 12, and 18 months against criteria set now. Frame them as standard governance for a major investment, not a referendum on the CTO. Define in advance what triggers re-scoping, such as falling back to a hybrid (new platform for new business only, old system for in-force).

Do all four and you've converted a big-bang rewrite into a staged replacement with early feedback. That's most of what the incremental strategy offered, achieved without relitigating anything.

## Protect what pays the bills

The old system carries the revenue for at least two more years, likely longer. Specifically:

- **A dedicated sustaining team,** with real status and pay, not a penalty box for whoever wasn't picked for the exciting project.
- **Retention of legacy-knowledge holders.** Consider retention bonuses tied to the rewrite's parity milestones, so their knowledge flows into the new system instead of out the door.
- **A modest, explicit feature budget** on the old system for customer and regulatory needs, so the rewrite doesn't cost you the customers it's meant to keep.

## Guard against your own bias

You now have a stake in the rewrite failing, and that is dangerous for someone leading its execution. Protect against it deliberately:

- Let neutral parties define and collect the milestone measurements.
- Execute as if you want it to succeed, because the company's revenue depends on it.
- If the rewrite hits its early milestones, say so plainly, and update your view in writing just as specifically as you stated your dissent.

The dated record binds you as much as anyone.

## When to raise it again, and when to leave

Decisions are conjectures too, and they can be revised. Reopen the question if:

- Pilot results arrive showing large gains from the harness. Bring them forward as new evidence, not as an "I told you so."
- A stage gate is clearly missed.
- A fact comes to light that undermines the premise of the decision.

Raise it through the same channel the decision came from, framed around the evidence.

If the rewrite goes ahead without stage gates, without any way to raise evidence, and you believe it puts the company at serious risk, you face a harder personal question about whether you can lead it in good conscience. Keep that distinction clear: disagreeing with a decision is normal and not grounds to leave; being unable to correct a decision's errors is a more serious matter.

## Bottom line

Find out why the CEO decided, because you may learn something that changes your own view. Dissent once, in writing, with conditions under which you'd be proven wrong. Then put your effort into making the rewrite correctable: a parity oracle, early production traffic, shadow mode, migration rehearsals, and stage gates the CEO owns.

You lost the argument about which strategy to pursue. You haven't lost the more important one, about whether the company will learn quickly when it's wrong.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

I'll assume no decision has been made yet. If the CEO has already green-lit the rewrite, skip to "If the decision is already made" at the end.

My best current conjecture, held tentatively: **modernize incrementally with teeth, and be ready to escalate to a new core for new business if the evidence demands it.** Don't commit to either full strategy yet. Spend the next quarter running the tests that decide between them, and structure everything so you learn quickly whichever way it goes.

## Next two weeks: set up the decision

1. **Recast the debate as a hypothesis test.** Take this framing to the CTO one-on-one before any group meeting: "We both want off this platform. Let's find out fast which route gets us there." Invite him to shape the tests, so he co-owns them rather than being judged by them.
2. **Get written predictions from both leaders.** Each states what they expect the diagnosis and pilot to show, and what result would change their mind. Date the document. If the CTO resists, ask for milestones and "what would surprise you" instead.
3. **Brief the CEO early.** Ask the CEO to wait for about one quarter of evidence before approving either path, and to require stage gates on whatever is chosen. This heads off a premature green light.

## Weeks 1–6: diagnose

- **Lead-time trace.** Five to ten recent features, with time broken into testing, understanding code, making changes, fixing regressions, and waiting. Break it down by module, not just in aggregate.
- **Hotspot analysis.** Find the modules with the most change and the most complexity. The pain is almost certainly concentrated there.
- **Lost-deal review.** Check the last 18 months of lost deals: did architecture or "cloud-native" actually decide any of them?
- **Attrition review.** Reread exit interviews and talk honestly with the people who stayed. Is it the stack, the toil, or the pay?

## Weeks 2–12: the no-regret work

- **Build the characterization harness** in one or two hotspots: capture real production quotes, rates, and transactions, and compare outputs automatically. It's valuable under every strategy, including a rewrite, which needs it to prove parity.
- **Run the seam test** in the same hotspot: try to carve one real capability out and into production within 90 days.
- **Protect knowledge now.** Identify the three to five people who understand the legacy system best and secure their retention. Losing them damages every option.

## Around day 90: decide by the evidence

| What you find | What to do |
|---|---|
| Delay is mostly testing and process; the harness also cuts code-fighting | Scale test automation and restructure hotspots selectively. No rewrite needed. |
| Harness and seam work, but code-fighting persists in the core | Strangler with teeth: a protected budget, work directed at rating and the policy model, production every quarter. |
| Harness or seam fail on coupling, or deals are clearly lost to architecture, or the stack is unsupportable | New core for new business: new lines and states launch on a modern platform, and in-force policies migrate later, once it has proven itself. |
| Pain tracks knowledge loss more than code structure | Any of the above, paired with deliberate knowledge capture and retention as a top priority. |

Some results, especially whether harness coverage reduces code-fighting, may need a second quarter to show. If so, extend the pilot rather than guess.

## Whichever path you choose

- Something real in production within six to nine months.
- The harness serves as the parity oracle for anything replacing existing behavior.
- Stage gates at 6, 12, and 18 months, owned by the CEO, with re-scoping triggers agreed in advance.
- A properly staffed and respected team keeping the revenue-carrying system healthy.
- A public, dated record of predictions, checked honestly against results, including by you.

## If the decision is already made

Ask the CEO what tipped it, since you may learn something that changes your view. Record your dissent once, with the conditions under which you'd be proven wrong. Then make the rewrite correctable:

- The harness becomes its parity oracle.
- New business and shadow-mode rating go first.
- Migration rehearsals start early.
- Stage gates are owned by the CEO.

## The short version

Don't bet the company on a conjecture you haven't tested when you can test it in a quarter at low cost. The work that tests it is work you need anyway. Decide around day 90 based on the evidence, and whichever path you take, build it so it tells you early when you're wrong.

## Outcome summary (sent to Jev)

The assistant's tentative conjecture is to modernize incrementally "with teeth," ready to escalate to a new core for new business if the evidence demands it, rather than commit to a two-year from-scratch rewrite. A big-bang rewrite is structurally hostile to error correction. It must reproduce twenty years of undocumented rating and regulatory behavior, chase a moving target, and leave in-force policy migration for last. It also surfaces mistakes only at cutover, when they cost the most. The feature slowness and attrition may not even stem mainly from the code. Incremental work keeps revenue flowing and gives production feedback, though strangler efforts often stall at the easy edges or lose priority fights.

The steps it proposes:
- Get dated, written predictions and refutation conditions from the CTO and head of product. Where "criteria" meets resistance, phrase them as milestones or surprises.
- Ask the CEO to wait about a quarter for evidence and to require stage gates on any path.
- Trace lead time by category and module, find hotspots, and review lost deals and exit interviews.
- Build a characterization harness in the hotspots. It is valuable under every strategy and serves as a rewrite's parity oracle.
- Run a 90-day seam test and secure retention of key legacy experts.

Around day 90, choose by the evidence: test automation with selective restructuring, a strangler with protected budget aimed at the core, or a new platform for new lines and states with later migration. Whatever the path, it wants production traffic within six to nine months, CEO-owned stage gates at 6, 12, and 18 months, and a respected team sustaining the old system.

The assistant's caveats are these. Some results may need a second quarter. The CEO may hold information or goals that change the analysis. If a rewrite is already approved, dissent once in writing, then make it correctable through shadow-mode rating, new business first, early migration rehearsals, and stage gates.
