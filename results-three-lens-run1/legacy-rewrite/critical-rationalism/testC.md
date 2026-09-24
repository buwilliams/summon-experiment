# critical-rationalism/legacy-rewrite/testC

Model: claude-opus-5-5 · 2026-09-24T14:44:58.542326+00:00

## Turn 1

**User:** Use the method of conjectures and refutations (critical rationalism) to answer the following.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

# Rewrite vs. Incremental Modernization: A Conjectures-and-Refutations Analysis

Critical rationalism doesn't ask "which strategy can we justify?" It asks "which conjecture survives our best attempts to refute it, and which lets us discover our errors fastest?" So I'll treat both proposals as bold hypotheses, derive what each implies, and look for evidence that would kill them.

## Step 1: What problem are we actually solving?

Popper insisted that inquiry starts with problems, not solutions. You've described three symptoms:

1. Features take months.
2. Your best engineers leave.
3. Competitors market themselves as "cloud-native."

Both proposals quietly assume a shared causal theory: *the age and architecture of the codebase cause all three.* That is itself a conjecture, and it should be tested before you bet two years on it.

- **Slow features** might come from architecture. They might also come from missing test coverage, manual release processes, approval bottlenecks, or tangled product requirements. A rewrite fixes only the first. The others will follow you onto the new stack.
- **Attrition** might come from the legacy stack. It might also come from being perpetually on-call for a fragile system, from compensation, or from a sense that nothing ever improves. Exit interviews can distinguish these.
- **"Cloud-native"** might be costing you deals. Or it might be marketing language that P&C carriers, who buy on regulatory coverage, rating accuracy, and migration risk, weigh less than you fear. Check your lost-deal records: how many losses cited architecture versus features, price, or integrations?

If these tests show the architecture isn't the main cause, *both* proposals are partly refuted, and you've saved yourself a very expensive mistake.

Let's assume the architecture really is a major cause and test the two conjectures.

## Step 2: Testing Conjecture A, "Rewrite from scratch in two years"

**What it asserts:** Incremental change cannot escape the hole. A clean-slate system can be built, reach feature parity, migrate customers, and deliver faster development within about two years.

**Consequences we can check:**

**(a) It implies you can specify what the old system does.** A 20-year-old P&C policy admin system encodes state-by-state regulatory rules, rating algorithms, form logic, endorsement edge cases, and customer-specific behavior. Much of it exists *only* in code, and some of it exists only as bugs customers depend on. A rewrite must rediscover all of it. This is the most common way rewrites die: the old system is the only complete specification of itself, and it's written in the language you're trying to leave.

**(b) It implies the two-year estimate is reliable.** The base rate is poor. Large rewrites and core-system replacements, including many carriers' own policy-admin replacements, routinely run multiples over schedule. Famous cases include Netscape's rewrite and the FBI's Virtual Case File, and insurance has plenty of quieter ones. A two-year estimate made before the rediscovery work in (a) is a guess, not a forecast.

**(c) It implies the business can survive a feature freeze or a split team.** During the rewrite, either the old system stops getting features, and customers and competitors punish you, or it keeps getting them, and the rewrite chases a moving target. Either way you run two systems with one team's worth of people.

**(d) It implies feedback arrives late.** You won't learn whether the new architecture actually speeds up development, whether migration works, or whether customers accept it until near the end. In Popperian terms, this conjecture is structured to *resist* early refutation. That is a serious flaw, because it means errors compound for two years before you can see them.

**(e) It implies the new system won't become the next legacy.** A second system designed by people reacting against the first tends toward over-engineering (Brooks's "second-system effect"). The rewrite fixes today's pain but carries no mechanism that stops the new system from decaying the same way.

**Verdict:** Conjecture A isn't refuted outright, but it survives only under specific conditions. You'd need at least one of these:

- The platform is truly dead, for example an unsupported runtime or a vendor gone.
- The domain is small and well-specified.
- The system has no seams at all, so nothing can be carved off.

Absent those, the evidence weighs heavily against it.

## Step 3: Testing Conjecture B, "Modernize incrementally"

**What it asserts:** You can carve off capabilities one at a time (the "strangler fig" pattern), route traffic to new components, keep shipping features, and eventually hollow out the old system.

This conjecture deserves equally hard criticism. Its advocates often don't subject it to any.

**(a) It implies the system has seams.** If everything reads and writes one shared database schema with business logic in stored procedures and triggers, "carving off a capability" may be nearly impossible without first untangling the data. This is the strongest potential refutation of B, and it's testable now.

**(b) It implies the effort will reach the core.** The typical failure is carving off easy peripheral pieces, such as document generation, notifications, or a new portal, while rating, policy lifecycle, and billing stay untouched forever. Five years later you have the old monolith *plus* a ring of new services *plus* integration glue: more complexity, not less. Engineers still leave, because the painful part never changed.

**(c) It implies the organization will sustain investment.** Incremental modernization competes with feature requests every quarter, and it usually loses. Without protected capacity it quietly dies.

**(d) It implies an interim integration tax.** Running old and new side by side requires routing, data synchronization, and consistency handling. That cost is real and must be counted.

**Where B does well:**

- **It is highly falsifiable, early.** Within one quarter you learn whether a capability can be extracted, whether development in the new component is actually faster, and what the integration cost really is.
- **Its errors are small and correctable.** A failed extraction costs you months, not the company.
- **It keeps revenue and customer trust intact** while you learn.
- **It gives engineers visible progress,** which may address attrition better than a distant promise of a rewrite.

**Verdict:** Conjecture B survives better, but only in a strengthened form that answers objections (a) through (c). The naive version ("chip away when we have time") is refuted by its own common failure mode.

## Step 4: The deeper criterion

Popper distinguished *utopian* engineering (redesign the whole system according to a blueprint) from *piecemeal* engineering (make targeted changes whose effects you can observe and correct). His argument wasn't that big changes are always wrong. It was that big-bang changes destroy your ability to learn from mistakes, because too many variables change at once and results arrive too late.

That is precisely the difference here. The CTO's plan is one large, slowly testable conjecture. The product lead's plan is a series of small, quickly testable ones.

Note also that the dichotomy is partly false. A well-run strangler migration *is* a sequence of rewrites, each scoped to one capability. The real question isn't "rewrite or not" but "how big is each bet, and how soon do we find out if it was wrong?"

## Step 5: Crucial experiments to run in the next 90 days

Rather than settling this by argument, design tests whose outcomes would change your mind:

1. **Root-cause test.** Measure where feature lead time actually goes: design, coding, testing, release, approvals. Review exit interviews and lost-deal notes. *Refutes both proposals if architecture isn't the dominant cause.*
2. **Seam test.** Have senior engineers map data and call dependencies for the core domains: rating, policy lifecycle, billing, forms. *Strongly supports A if nothing can be separated without touching everything.*
3. **Extraction pilot.** Carve off one capability that matters, deliberately *not* the easiest one, behind the existing system. Measure extraction cost, integration overhead, and development speed in the new component afterward. *Refutes B if extraction is prohibitively costly or brings no speedup.*
4. **Rewrite spike.** Have a small team rebuild one narrow vertical slice, such as one line of business in one state, end to end. Record how much undocumented behavior they discover and how their estimates change. *Refutes the two-year timeline if the slice takes far longer than projected.*

## Tentative conclusion

On current evidence, **incremental modernization is the conjecture that survives**, in a demanding form:

- **Target the core.** Include a central domain early, not just the periphery.
- **Protect the work.** Reserve a meaningful share of engineering capacity (say 25–40%) so modernization can't be traded away for features each quarter.
- **Fix the data first.** Treat data decoupling as the first-order problem, since it's where strangler efforts most often stall.
- **Allow bounded rewrites.** Where a capability is truly rotten, rewrite *that component* from scratch. Your CTO's instinct is right locally, even if wrong globally.
- **Set kill criteria in advance.** For example: "If after 12 months we haven't extracted at least one core domain and measured a real lead-time improvement, we revisit the rewrite option with what we've learned."

The full rewrite is not proven wrong, but it survives only if the seam test shows the system is truly indivisible, or the platform is dying under you. If the 90-day experiments show that, change course without embarrassment. That is what the method is for.

One final point for the conversation with your CTO and product head: the disagreement between them is valuable. Don't resolve it by authority. Resolve it by agreeing *in advance* on what evidence would prove each of them wrong, then going to get that evidence.

## Turn 2

**User:** Our CTO will say we've already been "chipping away" for five years with nothing to show for it, so incremental has already failed. Can you put that objection through the same method?

**Assistant:**

# Testing the Objection: "Incremental Has Already Failed"

This is the strongest argument your CTO has, and it deserves real scrutiny, not dismissal. Five years of experience is evidence. The question is *what* it is evidence against.

## Step 1: State the objection as a conjecture

> "We have tried incremental modernization for five years. It produced nothing meaningful. Therefore incremental modernization is refuted for us, and only a rewrite remains."

This has the form of a Popperian refutation: a prediction ("incremental will get us out") was tested and failed. If it holds, it's decisive, so let's check its logic.

## Step 2: What exactly was tested?

A failed test never refutes a hypothesis in isolation. It refutes the hypothesis *together with* every assumption bundled into the test (the Duhem–Quine problem). When an experiment fails, you must ask which part of the bundle broke.

The five-year effort tested something like: *incremental modernization + the way it was scoped + the capacity it was given + the targets chosen + how progress was measured + the organization's ability to sustain it.* Any of these could be the component that failed, and each implies something different.

In my previous answer I described a naive version of incremental ("chip away when we have time") and predicted it would fail. It would stall under feature pressure, stay on the periphery, and leave the core untouched. **If the last five years looked like that, the CTO's evidence doesn't refute the strengthened proposal. It confirms a prediction the strengthened proposal made.**

## Step 3: Guarding against an ad hoc rescue

There is a real danger here, and your CTO would be right to call it out. Popper warned against saving a theory by redefining it after it fails ("that wasn't *real* incrementalism"). If every failure can be dismissed as "not done properly," the theory becomes unfalsifiable and worthless.

A modification is legitimate rather than ad hoc if it meets three conditions:

1. **It was stated before the evidence was examined.** The strengthened version was specified in advance, with its protected capacity, core targeting, data-decoupling priority, and kill criteria.
2. **It makes new, testable predictions.** It does: extraction of a core domain within a set time, with measurable lead-time improvement.
3. **It accepts refutation if the past effort already met its conditions.** If the last five years *did* have protected capacity, *did* target the core, and *did* attack the data layer, and still failed, then the strengthened version is refuted too. You should say so plainly.

So the honest position is not "incremental can't have failed." It's "we need to find out which version was tried."

## Step 4: Diagnose the failure. Each cause points a different way

This is where the objection becomes useful. A short, blameless retrospective on the five years should answer these questions:

| What happened | What it implies |
|---|---|
| **No protected capacity.** Modernization lost to features every quarter. | An *organizational* failure. It refutes unprotected incrementalism, not incrementalism. It is also a warning about the rewrite (see Step 5). |
| **Only peripheral pieces were touched,** such as portals, notifications, or reporting. | A *targeting* failure. Fixable by aiming at a core domain. |
| **They tried the core but couldn't separate it,** because of a shared schema, stored-procedure logic, and everything coupled to everything. | Genuine *evidence for the rewrite.* This is the seam-test result arriving early. Take it seriously. |
| **Things were extracted, but development didn't get faster.** | Evidence that architecture may not be the bottleneck. This weakens *both* proposals and points back to the root-cause test. |
| **Nobody measured anything.** "Nothing to show" is an impression. | The claim itself is untested. Inventory what was actually delivered before drawing conclusions. |
| **No clear owner or target state.** | A *governance* failure. It would sink any strategy. |

Notice that only one row, the third, supports the CTO's conclusion directly. The others either leave the strengthened incremental proposal standing or undermine both options. The objection only works if the failure was *technical*: the system truly couldn't be decomposed.

## Step 5: The objection cuts both ways

If the main cause was organizational, meaning the company couldn't protect modest, ongoing modernization work against feature pressure, then ask what that predicts for a rewrite.

A rewrite needs a *larger* commitment, sustained for *longer*, with *less* visible payoff in the meantime, while customers keep asking for features on the old system. An organization that couldn't hold the line on 20% of capacity for incremental work has shown no evidence it can hold the line on a two-year, high-cost program. The common pattern is that the rewrite gets raided for "urgent" legacy work, slips, and ends with two half-maintained systems.

So an organizational failure in the last five years is *not* an argument for a rewrite. It's an argument that whatever you choose, the governance problem must be solved first. A rewrite doesn't escape it. It raises the stakes.

The only version of the objection that favors the rewrite is the technical one: "we tried to carve out the core and physically couldn't." That is a specific, checkable claim.

## Step 6: Turn the disagreement into a test

Rather than arguing about what the five years mean, find out. In two to four weeks:

1. **Inventory the five years.** What modernization work was attempted, on which capabilities, with what staffing, and what got finished?
2. **Classify each effort.** Did it touch a core domain or the periphery? Was capacity protected or borrowed? Was the data layer addressed?
3. **For anything that stalled, record why.** Was it technical impossibility, reprioritization, loss of key people, or loss of sponsorship?
4. **Check for measurable effects.** Did lead time change in any extracted area?

## What to say to your CTO

Something like:

> "You may be right. If we genuinely tried to extract core domains with protected capacity and hit a wall of coupling, that's strong evidence for a rewrite and I'll support it. But if what we did was peripheral work that kept getting deprioritized, then the last five years tell us our *governance* failed, and that would sink a rewrite even faster. Let's spend a few weeks finding out which it was, and agree now on what each answer would mean."

That framing treats his objection as what it is: a serious potential refutation that hasn't yet been checked. It also commits everyone, including the product lead, to accepting the result.

## Turn 3

**User:** Suppose the retrospective shows it was mostly the third row: we did try to pull policy lifecycle out and got stuck on the shared schema. Can you run that result through the same method and see what actually follows from it?

**Assistant:**

# Testing the Retrospective Result: "We Got Stuck on the Shared Schema"

This is the result that favors your CTO, so it deserves the most careful handling. The risk now runs the other way. Last time the danger was rescuing incrementalism ad hoc. This time the danger is over-reading a real refutation and concluding more than the evidence supports.

## Step 1: State precisely what was refuted

The retrospective shows that one specific attempt failed: **extracting policy lifecycle into a separate component while it still depended on the shared legacy schema.** That is a genuine refutation, and it should be accepted without hedging. Three things fall with it:

- **The code-level strangler, applied to the core, is refuted.** You cannot modernize the core by wrapping and re-routing code while the data stays entangled. Any plan that says "carve off services one at a time" without a serious answer for the data is dead.
- **The assumption that the core domains have usable seams in their current form is refuted.** At least for policy lifecycle, they don't.
- **My earlier advice needs correcting.** I said to target the core early, and I listed data decoupling as a priority. Your result shows data decoupling isn't one priority among several. It is the entire problem. Nothing in the core moves until it's solved.

Your CTO deserves credit here: the pessimism about piecemeal fixes was right at the level of code.

## Step 2: What was *not* refuted

A failed test refutes the bundle of assumptions it carried, so check which assumptions this one carried. The attempt tested roughly: *extract policy lifecycle + the particular data technique used + the scope attempted + the tooling available + the downstream dependencies.* Several things remain open:

**(a) Whether other data-decoupling techniques would work.** Established patterns exist for exactly this situation:

- Change-data capture from the legacy schema into a new model
- Anti-corruption layers that translate between models
- Expand-and-contract schema migration
- Keeping legacy as the system of record temporarily while a new model is built and reconciled alongside it

Was any of this tried, or did the team attempt a direct extraction and stop at the first wall? The answer matters.

**(b) Whether the entanglement is total or concentrated.** "Stuck on the shared schema" could mean hundreds of tables cross-written by every module. Or it could mean a handful of hub tables, such as policy, coverage, and transaction, that everything touches. These call for very different strategies.

**(c) Where the blockage actually came from.** In old systems, the killer is often not the application code but everything *else* reading the tables directly: reports, the data warehouse, carrier integrations, batch jobs, regulatory extracts. That's a dependency-inventory problem, not an architectural impossibility.

**(d) Whether policy lifecycle was simply the hardest possible starting point.** It is usually the most central, most coupled domain in a policy admin system. Failing on the hardest case tells you something real, but it doesn't tell you everything.

## Step 3: What follows for the rewrite

Here the result has an implication that is easy to miss.

**The shared schema doesn't go away in a rewrite. It moves to the cutover.**

A policy admin system holds policies in force. P&C policies have long tails: mid-term endorsements, renewals, cancellations and reinstatements, audits, claims adjudicated against old terms, and regulatory retention requirements. A rewrite has two options for that book of business:

1. **Migrate all in-force policies to the new data model.** This requires fully understanding the legacy schema: every field's meaning, every historical quirk, every derived value. That is the same understanding whose absence stalled the extraction. The rewrite hasn't escaped the problem. It must solve it all at once, at the end, for everything, with every premium reconciling to the penny.
2. **Run both systems until old policies run off.** Then you are operating old and new side by side for years. That is incremental coexistence, just with a bigger chunk.

So the refutation doesn't hit only incrementalism. **Any strategy must solve the data problem.** The real question is whether to solve it gradually, with feedback, or all at once at the riskiest possible moment.

The result genuinely shifts weight toward replacing the core rather than wrapping it. It does not shift weight toward a big-bang cutover.

## Step 4: A new conjecture that survives both refutations

Now we have two refutations on the table:

- **Code-level strangling** of an entangled core fails, from your retrospective.
- **Big-bang rewrite** carries unbounded, late-arriving risk, from the earlier analysis. The data problem makes this worse, because it concentrates at cutover.

A conjecture that survives both looks like this:

> **Rebuild the policy core as a new system with its own clean data model, and migrate the book of business in cohorts along insurance's natural boundaries.**

Insurance gives you an unusually good migration seam: the policy term. A common approach in carrier core replacements works like this:

1. **Start small.** Write new business for one line in one state on the new platform.
2. **Convert at renewal.** Move existing policies when they renew, rather than migrating them mid-term.
3. **Leave the rest in place.** Policies not yet renewed stay on the legacy system until they roll over.
4. **Expand gradually.** Add states and lines as each cohort proves out.

This takes the CTO's core insight seriously: the core needs a new data model, not a wrapper. It also keeps what mattered in the product head's position: feedback within months, revenue protected, features still shipping, and no single catastrophic cutover. It is a rewrite in *what* gets built and incremental in *how* it goes live.

This is also a conjecture, and it has its own weak points:

- **Coexistence costs.** Running two policy systems means dual operations, cross-system reporting, and billing and claims integrations that must talk to both.
- **Shared-customer friction.** Customers with policies on both platforms will see inconsistencies.
- **Staffing strain.** You need enough people to build the new platform while maintaining the old one.

## Step 5: Tests to run before committing

Each of these could refute the new conjecture, or point back toward one of the originals:

1. **Schema dependency map (2–4 weeks).** Map which modules and external consumers read and write which tables.
   - If coupling is concentrated in a few hub tables, targeted decoupling may still be viable.
   - If it's diffuse, that confirms the need for a new model.
   - Either way, the map becomes the migration inventory.
2. **Data migration spike (6–8 weeks).** Take one state's in-force policies for one line and migrate them to a draft new model. Reconcile every premium, coverage, and transaction history.
   - This is the most important test. **If it fails, both the rewrite and the cohort approach are in serious trouble,** and you need to know that before spending two years.
3. **New-business pilot scoping.** Estimate what it takes to write new business for one line in one state end to end, including rating, forms, billing handoff, and regulatory filings.
   - That estimate grounds the timeline in evidence instead of hope, and it's a direct test of the CTO's two-year figure.
4. **Technique audit.** Find out what data-decoupling approaches the original attempt actually used.
   - If they were crude, a better-equipped second attempt on a less-coupled domain may still be worthwhile in parallel.

## What actually follows

- **Refuted:** modernizing the core by extracting code while sharing the legacy schema.
- **Strengthened:** the case for building a new policy core with its own data model. Your CTO was right about this.
- **Not supported:** a big-bang, two-year rewrite with a single cutover. The data problem the retrospective exposed is exactly what makes that cutover so dangerous.
- **Surviving conjecture:** a new core platform, migrated cohort by cohort at policy renewal. It is provisional, pending the migration spike.

For the conversation with both leaders, you might put it this way:

> "The retrospective proved that we can't wrap our way out of the core, so we need a new policy platform. It also proved that the hardest part is the data, and a single cutover would make us solve that all at once, blind. Let's build the new core and bring the book over one renewal cohort at a time. First, let's prove we can migrate one state's policies cleanly, because if we can't do that, no plan works."

That framing gives your CTO the new platform he argued for. It gives your head of product the continuous delivery and feedback she argued for. And it makes the next decision depend on a test rather than on who argues better.

## Turn 4

**User:** What if the migration spike partly works: most policies reconcile cleanly, but a few percent carry legacy quirks nobody can explain. Can you run that through the same method and see what it means for the cohort approach?

**Assistant:**

# Testing the Spike Result: "Most Policies Reconcile, a Few Percent Don't"

This result is the hardest kind to reason about because it's ambiguous. It invites two opposite errors:

- **"95%+ reconciled, so the approach works. Push the rest through."** This treats the failures as noise when they may be the most important information the spike produced.
- **"We migrated policies we can't explain, so migration is unsafe. Stop."** This treats partial failure as total refutation, when the method asks which parts of the conjecture failed.

Last time I said that if the spike failed, both the rewrite and the cohort approach would be in trouble. The spike didn't fail, and it didn't pass. So we need to be precise about what it tested.

## Step 1: What the result refutes

**The assumption that the legacy system's behavior can be fully specified.** Earlier I noted that an old system is often the only complete specification of itself. The spike confirms this: a few percent of policies carry behavior that neither the schema, the documentation, nor the remaining staff can account for. Twenty years of knowledge has partly evaporated. This connects to your attrition problem: the people who knew why these quirks exist are likely gone.

**The single-cutover rewrite, more decisively than before.** A few percent of one state's book is a manageable list. A few percent of your entire book, all hitting on cutover weekend, could mean thousands of policies with wrong premiums, wrong coverage, or failed renewals at once, each needing investigation while the old system is being shut down. The spike turns the big-bang risk from a theoretical worry into a measured one.

**Any plan that assumes migration is purely an engineering task.** Some of these cases will need underwriting, compliance, or legal judgment, not code.

## Step 2: What it does not refute

It doesn't show that the unexplained cases are unmigratable. "Nobody can explain it" is a statement about your current knowledge, not about the policies. So the next step is to form conjectures about what the quirks are:

| Conjecture | What it would look like | How to handle it |
|---|---|---|
| **Undocumented but legitimate rules:** grandfathered rates, underwriter overrides, old state filings, discontinued discounts still honored | Failures cluster by issue year, product version, state, or agent | Reconstruct the rule. Check whether it's a filing or contractual obligation. |
| **Legacy bugs that became contractual reality:** premiums computed "wrong" but issued and billed | Failures cluster around specific transaction types or code releases | What was issued is binding. Carry it forward and decide how to correct it at renewal. |
| **Data artifacts:** past migrations, manual database fixes, failed batch jobs | Failures look scattered, with impossible field combinations | Data remediation, possibly with customer or regulator notice |
| **Errors in the new model or migration code** | Failures correlate with features of the new implementation | Fix your side. This is the cheapest outcome. |
| **Effective-dating problems:** rules applied as of past dates, rate versions | Failures cluster around endorsements or mid-term changes | Model historical rate versions properly |

The first test is simple and cheap: **see whether the failures cluster.** Clustered failures suggest a hidden rule you can recover. Scattered failures suggest data corruption. The two lead to different work, and a week of analysis will tell you which you're facing.

Also measure the failures by what's at stake, not just by count. A few percent of policies with rounding differences is trivial. A few percent concentrated in large commercial accounts with material premium differences is a serious business risk.

## Step 3: Two points that change the picture

**First: you may not need to explain a quirk to migrate a policy.** For an in-force policy, the contractual truth is what was issued and billed, not what the rules should have computed. If you migrate the *outcome* (the issued coverage, the charged premium, the transaction history) as data, rather than re-deriving it from rules, many quirks become irrelevant until the policy is re-rated. The spike should distinguish these two failure types:

- **"We can't reproduce how this number was computed."** You can often carry these forward.
- **"We can't represent this policy in the new model at all."** You have a real design gap.

**Second: renewal is where the quirk must finally be decided, and that is a strength of the cohort approach.** At renewal, the policy gets re-rated on the new platform under current rules. Each quirk then forces an explicit choice:

- **Reproduce it,** which means you must understand it.
- **Discontinue it,** which is only allowed if the change complies with filed rates, notice requirements, and any premium-change caps.

That turns a vague unknown into a specific, per-policy decision at a predictable time. A big-bang cutover would face the same decisions all at once. It could only avoid them by re-deriving everything and hoping.

**Caution:** discontinuing a quirk that turns out to be a regulatory or contractual obligation, such as a grandfathered discount, can cause customer harm and regulatory trouble. Unexplained cases can't simply be dropped at renewal. They need a disposition.

## Step 4: What this means for the cohort approach

**It survives, and in one respect it's strengthened.** Small cohorts turn "a few percent of the book" into a countable handful per cohort, which people can investigate case by case. You can also order the cohorts deliberately, starting with the books that have the lowest quirk rates and building knowledge before tackling the older, messier ones.

**But the spike exposes a weakness the approach didn't account for: the tail.** The natural move is to quarantine unexplained policies on legacy until they're understood or run off. That's sensible, but it has a failure mode. If the quarantine pool doesn't shrink, the legacy system never retires. You end up paying for two platforms indefinitely while the old one runs a few thousand strange policies nobody understands.

So the conjecture needs refinement:

> **Migrate by renewal cohort, carrying issued outcomes forward as data. Assign every unexplained policy an explicit disposition: reproduce, carry forward, remediate with notice, or quarantine. Track the quarantine pool as a first-class metric with a retirement target.**

This refined version is refuted if either of two things happens:

- **The quirk rate rises as you move to older or more complex books** faster than your team can resolve cases.
- **The quarantine pool stops shrinking,** meaning quirks are accumulating rather than being understood.

Either outcome means legacy won't retire on this path. You'd then need to consider a harder choice, such as a negotiated run-off of the quarantined policies or a formal decision to re-underwrite them at renewal.

## Step 5: Use the legacy system while you still have it

The legacy system can serve as a test oracle even when nobody can explain it. Feed it inputs, record its outputs, and check the new system against those recorded results (sometimes called characterization or golden-master testing). You don't need to understand a quirk to detect whether the new platform reproduces it.

This fits the method closely. Popper argued that we never get certain justification for our theories, only better ways to detect our errors. You may never know *why* the legacy system computes a certain premium for a 2009 policy with a particular endorsement. You can still know whether your new system matches it.

This oracle only exists while the legacy system runs and a few people still know how to operate it. That argues for capturing its behavior systematically now, as a standing asset, rather than case by case later.

## Next tests

1. **Cluster analysis of the failures (1–2 weeks).** Break them down by issue year, product version, state, transaction type, and dollar impact.
2. **Classify each failure.** Is it "can't reproduce the computation" or "can't represent the policy"? The first can often be carried forward. The second requires model changes.
3. **Compliance review of a sample (in parallel).** Have underwriting and compliance examine a dozen unexplained cases to judge which might be filed obligations.
4. **A second spike on an older, messier book.** This tests whether the quirk rate stays roughly constant or climbs, which matters most for whether the cohort approach can finish.
5. **Set pre-committed thresholds now.** For example, proceed with the first live cohort if every unexplained policy has a disposition, and review the strategy if quarantine exceeds a set share of in-force premium or fails to shrink over a set number of cohorts.

## What follows

- **Refuted:** the idea that the legacy system can be fully specified, and, more firmly than before, the single-cutover rewrite.
- **Not refuted:** migration itself. Most of the book moves cleanly, and much of the rest may move as carried-forward data.
- **Surviving, with refinement:** cohort migration at renewal, now with explicit dispositions for every unexplained policy and a measured, shrinking quarantine.
- **New open question:** whether the tail stays manageable as you move into older books. The second spike answers it.

For the leadership conversation:

> "The spike showed the new platform can hold our business: most policies move cleanly. It also showed that our old system knows things we've forgotten. That rules out a single cutover, because we'd face every mystery at once. Cohort migration lets us face them a handful at a time, decide each one deliberately at renewal, and use the old system as a check while it's still running. The thing to watch is whether the unexplained cases shrink as we go. If they don't, we'll know early, and we'll know by how much."

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

**Commit to building a new policy core with its own data model, and migrate onto it cohort by cohort at renewal. Do not attempt a big-bang rewrite, and do not keep extracting code from the shared schema.** Treat the plan as a conjecture with pre-set tests, not a settled truth.

First, a correction to my own earlier analysis, in the spirit of the method. I've been reasoning as if you were a carrier migrating your own book. You're a software vendor, so the policies belong to your customers. That changes three things:

- **The migration unit is carrier × line × state,** not just line × state.
- **Every cohort needs a customer's agreement,** and filings and regulatory obligations are theirs. Their underwriting and compliance people must be involved in deciding what happens to the unexplained policies.
- **Some of the "unexplained quirks" are probably customer-specific configurations or customizations** from years past. That makes them more tractable, since the customer may know why they exist, but it also means each carrier's migration carries its own tail.

The overall strategy still holds. The execution needs a design-partner customer.

## Next 90 days: finish testing before the big spend

1. **Diagnose the failed policies.** Cluster them by issue year, product version, state, transaction type, carrier, and dollar impact. Separate "can't reproduce the computation" from "can't represent the policy."
2. **Run the second spike on an older, messier book.** This tells you whether the quirk rate stays flat or climbs, which is the biggest remaining threat to the plan.
3. **Capture the legacy system's behavior as a test oracle.** Record inputs and outputs systematically across products, states, and transaction types, while the system runs and the people who operate it are still here.
4. **Inventory everything that touches the schema.** Include reports, data feeds, customer integrations, batch jobs, and regulatory extracts. This becomes your migration checklist.
5. **Recruit a design-partner carrier.** Choose one that is relatively simple, reasonably modern in configuration, and motivated. Offer favorable terms in exchange for being first.
6. **Scope the first cohort concretely.** Pick one line, one state, one carrier, starting with new business. Estimate it end to end: rating, forms, billing, documents, integrations, and filings support.
7. **Check the original root-cause question.** If you haven't yet, confirm that architecture is really what slows features and drives attrition, and that "cloud-native" actually appears in lost deals. If other causes dominate, such as manual releases or weak tests, fix them in parallel, or they'll follow you onto the new platform.

## Organize to avoid repeating the last five years

The retrospective showed that the technical wall was real. Still, any long effort dies without protection, so build the protection in from the start.

- **Dedicate a team to the new platform.** Staff it with people who aren't pulled back for legacy emergencies. Protect its capacity in the budget, not just in intentions.
- **Split ownership by strength.** Your CTO owns the platform build and architecture. Your head of product owns cohort sequencing, customer commitments, and the rule for where new features get built. Both argued for something the plan needs, so give each authority over that part.
- **Set a feature rule for the legacy system.** New capabilities for lines scheduled to migrate get built on the new platform. On the old one, fix defects and meet regulatory requirements only. Otherwise you'll keep enlarging the thing you're trying to retire.
- **Keep your legacy experts.** The few people who understand the old system are your most important knowledge source. Offer them retention incentives, pair them with platform engineers, and have them help explain unexplained policies. Losing them now would be very costly.
- **Rotate engineers onto the new platform.** Visible, modern work with real progress is likely your best attrition remedy. It also spreads knowledge in both directions.

## Decide in advance what would change the plan

Write these down and get both leaders to sign off on them now, before results come in.

**Gate 1 (around 90 days): proceed to build?**

- *Proceed* if unexplained policies cluster into recoverable rules or carry-forward data, the older-book spike shows a stable or slowly rising quirk rate, and the first-cohort estimate is credible.
- *Rethink* if failures are scattered and unrepresentable, or the quirk rate climbs steeply with book age. That would point toward treating legacy policies as run-off and focusing the new platform on new business only.

**Gate 2 (first new-business cohort live, likely 9–15 months): is the platform delivering?**

- Measure feature lead time on the new platform against legacy for comparable work.
- *Rethink the architecture* if the new platform isn't clearly faster to change. The whole premise rests on that.

**Gate 3 (first renewal conversions): does migration scale?**

- Track the share of the cohort that converts cleanly, the time to resolve each unexplained case, and the size of the quarantine pool.
- *Rethink* if quarantine grows or stops shrinking across successive cohorts, since legacy won't retire on that trajectory.

## Report a few numbers every quarter

- **Migration progress:** share of customers' in-force premium on the new platform.
- **Feature speed:** lead time for changes on new versus legacy.
- **Tail health:** quarantine pool size and resolution rate.
- **Retention:** regretted engineering attrition.
- **Competitive impact:** deals won or lost where architecture was cited.

If these move the wrong way, the plan is being refuted. Adjust it rather than defending it.

## The market message

Don't claim "cloud-native" before you have it. Once the first cohort is live, you'll have something better to sell to risk-averse carriers: a modern platform with a proven, low-disruption migration path, where books move at renewal and nothing breaks. Competitors who rewrote from scratch still have to explain how they'll move a carrier's 20-year book. You'll have done it.

## Honest caveat

This recommendation rests on the scenario we've built step by step: a genuine schema wall, and a spike that mostly worked. If your real results differ, the reasoning above shows which way to move. The durable advice holds regardless: make the bets small enough to learn from, decide your kill criteria before you see the results, and keep the old system as your source of truth until the new one has proven it can replace it.

## Outcome summary (sent to Jev)

The recommendation is to build a new policy core with its own clean data model and migrate onto it cohort by cohort at policy renewal. Both a big-bang two-year rewrite and continued code extraction from the shared legacy schema should be rejected. The plan is a conjecture to be tested, not a settled truth.

Extracting the core while it still depends on the entangled schema was refuted, so the core needs a new data model. The data problem doesn't disappear in a rewrite; it concentrates at cutover. The migration spike showed most policies reconcile cleanly but a few percent carry unexplained quirks. A single cutover would surface all of them at once, while small cohorts make them a countable handful. Because the company is a vendor, the migration unit is carrier × line × state. Each cohort needs customer agreement, and a design-partner carrier should go first.

For the next 90 days:
- Cluster and classify the failed policies.
- Run a second spike on an older, messier book.
- Capture legacy behavior as a test oracle.
- Inventory everything that touches the schema.
- Scope a first new-business cohort.
- Recheck whether architecture really causes slow features and attrition.

Organizationally:
- Dedicate a protected platform team.
- Give the CTO ownership of the build and the head of product ownership of sequencing and customers.
- Restrict legacy work to defects and regulatory requirements.
- Retain legacy experts and rotate engineers onto the new platform.

Three pre-agreed gates govern progress: quirk patterns and cohort estimates at about 90 days, feature lead time once the first cohort is live, and a shrinking quarantine pool during renewal conversions. Quarterly metrics should track migration share, lead time, tail health, attrition, and architecture-cited deals.

The main caveats are that unexplained policies can't simply be dropped, the quarantine pool may fail to shrink, and "cloud-native" shouldn't be claimed prematurely.
