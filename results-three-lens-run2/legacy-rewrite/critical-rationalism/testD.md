# legacy-rewrite/critical-rationalism/testD

Model: claude-opus-5-5 · 2026-09-24T15:24:46.172675+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

**Assistant:**

# Rewrite vs. Incremental Modernization: Which Conjecture Survives Criticism

Neither position is really a strategy. Each is a causal theory about why your system is slow and your people are leaving, with a plan attached. The plans only make sense if the theories are true, so the useful move is to state each theory in its strongest form and ask what would break it.

## 1. The CTO's conjecture: rewrite from scratch

**What it claims.** The cost of change is a *global* property of the system. Coupling is pervasive: a shared database, implicit contracts, global state, and a dated runtime. Any change touches everything, and improving one part doesn't make the next change cheaper because the drag comes from the whole. Hence "incremental fixes will never get us out."

The plan quietly depends on three further claims:
- The knowledge embedded in the old system (20 years of state-specific rules, rating edge cases, mid-term endorsement logic, customer-specific behavior) can be recovered and re-specified well enough to rebuild it.
- The in-force book of policies can be migrated to the new system at cutover.
- The business can survive two years of reduced feature delivery, or fund two teams.

**What we'd expect to observe if it's true:**
- Change cost is diffuse. A typical feature touches many modules across the codebase, and no small set of files accounts for most of the pain.
- Past attempts to improve one area didn't make later changes in that area faster.
- Most feature lead time is spent in coding and understanding code, not waiting in queues, manual QA, or release trains.
- Attempts to extract a bounded capability run into shared tables and hidden dependencies almost immediately.

**Where it's easy to vary:**
- "Never" is doing a lot of work. Every failed incremental effort confirms it, and every successful one gets dismissed as "lipstick on a pig."
- The two-year timeline is unfalsifiable in practice. When it slips, the story becomes "we underestimated, but we were right to start."
- The theory never states *what the new system will do differently* that prevents it from becoming slow in turn. "Modern stack" is not a mechanism. If the causes of slowness are organizational or product-related, a rewrite rebuilds them.
- It says nothing about the knowledge-recovery and migration claims. These are where rewrites historically fail, and they're the parts the theory doesn't expose to test.

**Cheapest refutation.** Take one representative slice that is hard but bounded, such as a mid-term endorsement with premium recalculation for one line of business in one state. Give a small team 4–6 weeks to rebuild it on the target stack. Measure parity by replaying real production transactions through both systems and diffing the outputs. Count the undocumented behaviors they discover.
- If they can't reach parity on a slice in weeks, the claim that the whole system can be rebuilt and migrated in two years is badly damaged.
- If they can, and the number of discovered behaviors is small, the knowledge-recovery claim survives, and that is real evidence for the CTO.

## 2. The head of product's conjecture: carve off capabilities incrementally

**What it claims.** Change cost is *concentrated*. There are seams (rating, document generation, billing, notifications, integrations) that can be isolated behind interfaces. Extracting them reduces cost locally, and the gains compound. Continuous delivery of customer value keeps revenue safe and exposes mistakes early.

**What we'd expect to observe if it's true:**
- A small number of modules account for most change activity and most delay. This is the usual hotspot pattern, where how often a file changes multiplied by how complex it is predicts where the pain lives.
- Changes within a capability area mostly stay within that area.
- An extracted capability can be stood up in weeks to a few months, and feature lead time in that area measurably drops afterward.
- The cost of integrating old and new systems is paid mostly once, not continuously.

**Where it's easy to vary:**
- "One capability at a time" accommodates any pace. If progress is slow, the answer is "we're still carving."
- There's no stated end state. The classic failure is the strangler that never strangles: you end up with two systems, double the operational surface, and the old core still owning the hard parts (policy lifecycle, the in-force book).
- "Keep shipping features customers ask for" can quietly absorb all capacity, so modernization never happens but the strategy is never declared failed.
- It assumes seams exist without checking. If the database is one giant shared schema that every module reads and writes, the seams may be illusory.

**Cheapest refutation.** Pick the most seam-like capability and give a team 8–12 weeks to extract it. Commit in advance to numbers:
- Before-and-after lead time for changes in that area.
- Integration effort as a fraction of total effort.
- Whether the extracted piece needed changes to shared tables.

If it can't be done in that window, or lead time doesn't improve, the seams hypothesis is refuted. That is actually evidence *for* the CTO's diagnosis, though not necessarily for the CTO's remedy.

## 3. Observations that discriminate between them

| Observation | Predicted by CTO | Predicted by product | Predicted by neither (see §4) |
|---|---|---|---|
| Changes per feature spread across many modules, no hotspots | ✓ | ✗ | – |
| Most change activity concentrated in a few modules | ✗ | ✓ | – |
| Past local improvements made later changes faster | ✗ | ✓ | – |
| Most lead time is waiting, manual QA, release batching, or approvals | – | – | ✓ |
| Much effort goes to customer-specific variants or forks | – | – | ✓ |
| Engineers leave citing toil, fear of breaking things, slow feedback | – | – | ✓ |
| Engineers leave citing the stack itself or career stagnation | ✓ (weakly) | – | – |

Most of this can be measured in days from data you already have: version control history, your ticket system, deploy logs, exit interviews, and lost-deal notes.

## 4. A third explanation that may fit the facts better

Both views assume the binding constraint is the *code architecture*. There are two plausible alternatives that fit your facts at least as well, and neither strategy addresses them.

**A. The delivery-system hypothesis.** Features take months mainly because of the path from code to production, not the code itself: thin automated test coverage, manual regression cycles (common where rating errors have regulatory consequences), big-batch releases, and environment bottlenecks. Engineers leave because every change is frightening and feedback takes weeks. Under this theory:
- A rewrite would recreate the problem within a few years, because the same practices would build the new system.
- Carving off capabilities helps only as much as it also changes how testing and releases work.

**B. The product-variance hypothesis.** This is very common in policy administration. The system is slow because it is really N products. Each insurer customer has custom rules, configurations, or code branches, so every change has to be checked against every variant. Under this theory:
- Neither architecture fixes the problem.
- The fix is a product decision: a configuration model that replaces customization, plus a willingness to say no to some customers.
- A rewrite that must reach parity with every customer's variant would be enormous.

**Tests for the third explanation:**
- Break down elapsed time for the last 30–50 features: how much was spent in active development versus waiting, testing, and release. If coding is a small share, architecture is not the binding constraint.
- Measure what fraction of engineering effort goes to customer-specific work.
- Try one delivery intervention in one area and see how much lead time drops with no architectural change. A good candidate is an automated "golden transaction" regression suite built from replayed production policies.

## 5. Checking the "cloud-native" premise

Find out what the competitive threat actually is. Pull the loss reasons from recent deals.
- If buyers want vendor-hosted SaaS, modern APIs, and faster product configuration, much of that can come from rehosting, an API layer, and a configuration model, without rewriting the core.
- If deals aren't actually being lost on this, the urgency behind a two-year rewrite weakens considerably.

## 6. Where this leaves you

I can't see your codebase, so I can't settle the question. But I can say which conjecture is in better shape before testing.

**The rewrite theory, as stated, is the weaker conjecture.**
- It makes a universal claim ("never") that is easy to protect from disconfirmation.
- It offers no mechanism for why the new system won't decay the same way.
- Its riskiest assumptions, knowledge recovery and in-force migration, are exactly the ones it doesn't expose to test.
- Its failure mode is late and catastrophic: you learn you were wrong in year two, with a stalled product.

**The incremental theory is better but underspecified.** It survives mainly because its failures would show up early and cheaply. That's a real virtue, but it's a virtue of the *plan*, not proof that the diagnosis is correct. Without a committed end state and metrics, it can drift indefinitely.

**The explanation I'd bet on,** pending data, is that architecture is one cause among several. Delivery practices and customer-specific variance may matter as much or more. If so, the right strategy looks like the head of product's approach with teeth: incremental extraction, paired with investment in test and release automation and a product decision to curb customization, all measured against numbers committed in advance.

**What would change my mind toward the CTO.** Suppose the data shows diffuse coupling with no hotspots, lead time dominated by coding, a failed seam extraction, *and* a successful parity rebuild of a hard slice. Then the rewrite theory has survived real attempts to refute it, and you should take it seriously. At that point the argument shifts to *how* to rewrite: slice by slice, with production replay for parity and incremental migration, which ends up looking a lot like the incremental approach.

All of the tests above fit into roughly two months at a small fraction of the cost of committing to either path. The strongest recommendation I can make is to run them before deciding, and to have both leaders write down in advance which results would change their minds.

## Turn 2

**User:** Both the parity rebuild and the seam extraction let each camp choose its own slice, so either could pick an easy one and pass. What criterion for selecting the slice would make a pass count as real evidence and a failure impossible to explain away as "we just picked a bad slice"?

**Assistant:**

# Choosing Slices So the Tests Can't Be Gamed

You've found a real flaw in the plan. The fix is to settle two questions *before* anyone knows the result:

1. **Which slices are eligible?** Define this by objective criteria, not by either camp's judgment.
2. **Who picks from the eligible set?** The camp whose theory is being tested should not be the one choosing.

A test counts as real evidence only if it is *severe*: likely to fail if the theory is false. And a failure is only hard to explain away if both parties agreed, in writing and in advance, that the slice was representative.

## 1. Eligibility criteria: define the pool mechanically

Build the candidate pool from data before anyone knows which slice goes to which test. A slice is eligible only if it meets all of these.

**It comes from where the work actually is.**
- It ranks in the top portion of historical change traffic (say, the top 30% of capabilities by commits and tickets over the last 2–3 years).
- It appears on the next 12 months of roadmap.

This blocks both games. A pass on a slice nobody changes says nothing about the strategy's value. A failure on it can't be dismissed as irrelevant, because this is the code you'll be changing regardless.

**Its coupling falls in a middle-to-upper band, not at the extremes.**
- Use change-coupling from version control: how often a module changes together with others, and how many shared tables it reads and writes.
- Require the slice to fall between roughly the 50th and 90th percentile.

Excluding the bottom removes the easy leaf, like email notifications with their own tables. Excluding the extreme top removes the pathological knot that either side could blame as an outlier. What remains is typical of the hard work you face.

**It contains the claim's riskiest assumption.** Each test should probe the part of the theory most likely to be wrong.
- **For the parity rebuild:** the slice must include stateful policy lifecycle behavior (in-force policies, mid-term changes, or renewals). It must also include at least one state-specific regulatory rule, at least one customer-specific variant, and migration of real in-force records into the new system. A rebuild that skips migration isn't testing the rewrite; it's testing whether engineers can write code.
- **For the seam extraction:** the slice must share data with the core rather than own its tables outright, and it must sit on the path of actual upcoming feature work. Extracting something peripheral tests nothing about whether the core can be dismantled.

**It is sized to fit the timebox.** Estimate each candidate's share of the system by change traffic, rule count, and table footprint. Record that share, because you'll need it for extrapolation (see §3).

## 2. Selection procedure: the rival chooses

Once the pool exists, use "one cuts, the other chooses":

- The **head of product picks the slice for the parity rebuild.** Their theory predicts it will be hard, so they'll pick the hardest eligible slice.
- The **CTO picks the slice for the seam extraction**, for the same reason.

The eligibility criteria stop either side from choosing an absurd slice, and adversarial choice makes the test as severe as the criteria allow.

If the relationship is too tense for that, draw at random from the pool instead. That's less severe but still immune to cherry-picking.

**Optional but valuable:** run both tests on one shared slice in addition to each camp's own. Rebuilding and extracting the same capability gives you a direct comparison. The extraction is essentially a rebuild plus integration with the old system, so the difference between the two isolates what integration costs.

## 3. Pre-register the interpretation, not just the slice

Agreeing on the slice isn't enough if people can still argue about what the result means. Before work starts, write down and have both leaders sign the following.

**Pass/fail thresholds.**
- **Rebuild:** parity rate on replayed production transactions; migration of the slice's in-force records with zero unexplained discrepancies; completion within the timebox.
- **Extraction:** before-and-after lead time for changes in that area; integration effort as a share of total effort; whether any shared-table changes were required.

**Extrapolation rules.** Record in advance how a slice result scales to the whole system.
- Example: if the slice is 4% of the system and took 6 weeks with a team of 4, that projects to about 150 team-weeks of work.
- Compare the projection against the two-year plan with an agreed safety margin.
- Also track the curve of undocumented behaviors discovered over time. If it's still rising linearly at the end rather than flattening, treat that as a failing signal regardless of the headline number, because the true scope is still unknown.

**Admissible excuses.** List in advance the confounds that would void a result, and allow nothing else afterward. Examples: losing a key engineer mid-test, or the team being pulled onto a production incident for more than N days. Also staff both tests with comparable teams, including at least one person who knows the old system well. That removes the "our team didn't know the domain" and "our team didn't know the stack" excuses.

**Representativeness sign-off.** Each leader signs this statement: *"If this test fails, I will not argue the slice was unrepresentative."* This is the single most important step. Once someone has conceded representativeness in advance, "we picked a bad slice" is no longer available to them.

## 4. What this still doesn't fix

- **One slice is a small sample.** Even a well-chosen slice can be lucky or unlucky. If budget allows, run two slices per test: one chosen by the rival and one drawn at random. Agreement between the two strengthens the conclusion considerably.
- **Passing a slice doesn't prove the whole.** The rebuild test mainly tests whether the old system's knowledge can be recovered at the planned rate. It can't reveal problems that only appear at full scale, such as cutting over the entire in-force book or supporting all customer variants at once. Treat a pass as "the theory survived a serious attempt to refute it," not as confirmation.
- **The criteria themselves can be contested.** Settle disputes over percentile bands or definitions *before* anyone generates the pool. If you can't agree on the criteria, that disagreement is itself informative: it usually means the two leaders hold different, unstated theories about where the difficulty lives. Surfacing those theories is worth doing whatever the tests eventually show.

## Turn 3

**User:** Shouldn't we run the lead-time breakdown before either slice test, since a slice result can't tell architecture apart from delivery practices or customer variance if waiting, manual QA, or variant checking is what's actually slow? And what share of elapsed time spent in active coding would make both slice tests not worth running?

**Assistant:**

# Sequencing the Lead-Time Breakdown and Setting a Threshold

Yes, run the breakdown first. It's cheap (days to a couple of weeks, mostly from existing data), and it can make both slice tests unnecessary, which they can't do for each other.

But two amendments matter. Without them, the breakdown will mislead you in both directions.

## 1. Classify time by cause, not just by stage

"Active coding" understates how much of your lead time is architectural. Much of the time that looks like waiting or QA exists *because of* the architecture:

- **Manual regression cycles** often exist because the code has no seams where automated tests can attach.
- **Big-batch releases** often exist because deploys are risky in a tightly coupled system.
- **Variant checking** is slow partly because customer customizations live in code branches rather than configuration.
- **"Coding" itself** includes time spent understanding code, which is architectural, and time typing, which isn't.

So for each interval in a feature's timeline, record two things: the stage (coding, waiting, QA, release, variant checks) and a causal question: *would this interval shrink substantially if the architecture were good?* That yields three buckets:

| Bucket | Examples |
|---|---|
| **Architecture-attributable** | Understanding and changing coupled code; manual regression that exists because tests can't be automated at current seams; release batching driven by deploy risk |
| **Delivery-practice** | Queues, approvals, environment contention, handoffs, manual QA that would persist even with testable code |
| **Variance** | Checking and adapting changes across customer-specific variants |

Some intervals will be genuinely ambiguous. Split them 50/50 and report both the conservative and generous totals. If your decision is the same under both, the ambiguity doesn't matter.

**Practical cautions:**
- **Ticket timestamps are unreliable.** Tickets sit "in progress" while blocked. Reconstruct 25–40 recent features using commit, pull-request, and deploy timestamps, plus short interviews with the engineers involved. A small, accurate sample beats a large, noisy one.
- **Decide what "elapsed time" covers.** Measure from commitment to start work until the feature is in production. Report time spent in the backlog before commitment separately. That's a prioritization and work-in-progress problem, not an engineering one, and mixing it in will swamp everything else.
- **Run it partly in parallel.** Building the slice candidate pool uses the same version-control data, so prepare the pool while the breakdown runs. Just don't *start* the slice tests until it's done.

## 2. The threshold: derive it, don't guess it

There's no universal number, but you can derive yours from what the business needs. The logic is Amdahl's law: speeding up one part of a process can only improve the whole in proportion to that part's share.

Let **a** be the architecture-attributable share of lead time, and suppose modernization reduces that portion by a fraction **r**. The overall speedup is:

> **Speedup = 1 / (1 − a·r)**

Some worked values:

| Architecture share (a) | If modernization halves it (r = 0.5) | If it eliminates it entirely (r = 1, impossible ceiling) |
|---|---|---|
| 20% | 1.11× | 1.25× |
| 30% | 1.18× | 1.43× |
| 50% | 1.33× | 2.0× |
| 70% | 1.54× | 3.3× |
| 85% | 1.74× | 6.7× |

This gives you a decision rule:

1. **Decide the required speedup, S.** What improvement actually solves the business problem? If features take four months and you need to compete at six weeks, S ≈ 2.7.
2. **Assume a realistic r.** Halving architecture-attributable time (r = 0.5) is already optimistic for a modernization.
3. **Compute the minimum share needed:** **a_min = (1 − 1/S) / r**.

For S = 2.7 and r = 0.5, a_min ≈ 1.26. That's over 100%, which means architecture work alone *cannot* deliver the target, no matter what the breakdown shows. Even with r = 1, you'd need a ≥ 63%.

**The threshold:** if the measured architecture share, using the generous total, is below a_min, neither slice test is worth running as evidence about lead time. Neither strategy can close the gap, so the priority becomes delivery practices and variance.

In practice, I'd expect most teams in your position to fall below a_min. If so, the breakdown won't just rule out the slice tests. It will tell you that **delivery and variance work is required under every scenario**, and the only remaining question is whether architecture work is *also* required.

Pre-register S, r, and the threshold before the data comes in, for the same reason you pre-registered the slice interpretation. Otherwise a disappointing number will quietly trigger a revised estimate of what the business "really" needs.

## 3. What a low number doesn't kill

A low architecture share refutes the *lead-time* argument for modernization. It doesn't refute every argument:

- **Attrition.** If exit interviews show people leaving because of the stack itself or career stagnation, that's a separate case for modernization. Test it directly with exit-interview and recruiting data, not with lead time.
- **Competitive positioning.** If lost deals cite hosting model or API capability, that argues for rehosting and an API layer. Neither requires a rewrite, and neither depends on lead time.
- **Knowledge fragility.** If only three people understand the rating engine, that's a risk whatever your lead time is. The parity rebuild still has value here, because it measures how recoverable that knowledge is. Rerun it later if this becomes the live question.

So the sequence becomes:

1. Breakdown first.
2. If the architecture share is below the pre-registered threshold, shift investment to delivery practices and variance. Keep only the parts of modernization justified by attrition, competitive, or knowledge-risk evidence.
3. If it's above the threshold, run the slice tests, ideally alongside one delivery intervention so you can compare the gains from each.

## Turn 4

**User:** The "would this interval shrink with good architecture?" judgment decides which bucket manual regression and release batching fall into, and each camp would answer it differently. Couldn't we replace that counterfactual guess with a cheap intervention, like trying to build the golden-transaction regression suite against the current code, and classify by whether it succeeds?

**Assistant:**

# Replacing the Counterfactual With an Intervention

Yes. That's a better design. It turns a judgment each camp would make differently into an observation neither can easily dispute. But it needs three refinements, or the same argument will reappear in a new form.

## 1. Classify by what happens to elapsed time, not by whether the suite gets built

A golden-transaction suite is a black-box test: capture real inputs, replay them, and compare the outputs. Black-box replay largely bypasses internal structure. You mostly need to capture inputs and make the system deterministic, by controlling dates, sequence numbers, and calls to external services. So it will usually be *buildable* even against badly coupled code.

That makes "did we build it?" a test biased toward the delivery-practice explanation. Architecture shows up less in whether the suite can exist than in whether it's *usable*:

- **Diff noise.** In a coupled system, an intended change produces output differences in many unrelated transactions. Every one must be triaged before the new outputs can be accepted as the baseline.
- **Localization.** The suite tells you *that* something broke, not *where*. In tangled code, finding the cause can take as long as the manual testing it replaced.
- **Run time and flakiness.** If whole-system replay takes hours, or results vary between runs because of hidden state, people stop trusting it and manual testing creeps back.

So measure the outcome that matters: **does manual regression time actually shrink over the next several releases?** That gives a quantitative split instead of a yes-or-no answer:

- **The portion of manual regression that disappears** was delivery practice. Nothing about the architecture forced it.
- **The portion that persists *and* is traceable to architectural failure signatures** (see §2) is architecture-attributable.
- **Anything that persists for other reasons** stays unresolved. Report it separately rather than assigning it to either camp.

Pre-register the usability thresholds you'll accept, such as maximum run time, maximum flake rate, and maximum triage hours per release, just as you did for the slice tests.

## 2. Pre-register failure signatures so a failure can't be blamed on execution

If the suite fails, the CTO will say it proves the architecture is the problem. The head of product will say the team didn't try hard enough. Settle this in advance by listing observable signatures for each kind of failure and logging which ones actually occur.

**Architectural signatures:**
- State can't be captured or restored without snapshotting shared tables that many modules write to.
- Nondeterminism, such as system clock calls or external services, is scattered throughout the code with no single place to intercept it.
- Intended changes routinely cause output differences in transactions unrelated to the change.
- Diagnosing a differing output routinely requires tracing through many modules.

**Execution signatures:**
- Production transactions weren't captured in enough volume or variety.
- The test environment wasn't provisioned or maintained.
- The team was pulled onto other work beyond an agreed limit.

Only failures showing architectural signatures move time into the architecture bucket. Failures showing execution signatures void the result, and the test is rerun. That's the same rule as for the slice tests.

## 3. Release batching needs its own intervention, and may reveal a fourth cause

The suite addresses manual regression. It doesn't directly test release batching. Batching in your market may not be caused by architecture or delivery practice at all. Insurers often *require* controlled release windows because of their own acceptance testing, regulatory filing cycles, or contract terms. That's a customer or market constraint, and neither modernization strategy removes it.

The intervention for batching is to ship one small, low-risk change out of cycle, ideally to one willing customer, and record what stands in the way:

- **Deploy risk or tangled dependencies** point to architecture.
- **The release process or approvals** point to delivery practice.
- **Customer acceptance testing or contractual release windows** point to a **fourth bucket: external release constraints.** Track it separately, because the remedies are commercial (contract terms, release models customers can opt into), not technical.

## 4. Sequencing: when you need the intervention, and why to build it anyway

The intervention takes weeks to months, longer than the breakdown. So:

1. **Run the breakdown first.** Classify uncontested intervals directly and flag the contested ones. Mostly these will be manual regression and release batching.
2. **Compute the architecture share twice:** once with contested intervals counted as architectural, once without.
3. **If both versions lead to the same decision** against your pre-registered threshold, the intervention isn't needed to *decide*. The contested intervals don't change the answer.
4. **If the decision flips** depending on how contested intervals are counted, the intervention becomes necessary for classification.

But build the suite regardless. It's the same artifact as the parity harness from the rebuild test, where replayed production transactions were the pass/fail check. It's also the safety net that seam extraction needs, and the first delivery improvement under every scenario. Both camps need it whatever they believe. That makes it the rare test that costs nothing extra if it confirms your views and is highly informative if it doesn't.

## The remaining limit

This intervention tells you whether the *current* architecture blocks a practice. It doesn't tell you how much a *new* architecture would help. That's fine: classifying intervals only needs the first question. The second, how large r is, the fraction of architecture-attributable time a modernization would actually remove, is what the slice tests measure. Each piece of evidence answers the question it's suited for, and none has to rest on either camp's judgment.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

**Don't commit to either strategy yet.** Spend the next quarter running a structured evidence phase, then decide at a pre-scheduled meeting using rules both leaders agreed to beforehand. Keep shipping features throughout.

This isn't a delay. Almost everything in the evidence phase is work you'd need under any outcome, so the real cost is small.

## Week 0–2: Get the agreement in writing

Draft a one-page decision charter and have the CTO and head of product sign it. It should state:

- **The required speedup (S)**, derived from the business problem, and the assumed effectiveness of modernization (r = 0.5 unless someone argues convincingly otherwise).
- **The threshold** for the architecture-attributable share of lead time, computed from S and r.
- **The slice eligibility criteria**, the rival-picks rule, and the pass/fail thresholds for each slice test.
- **Failure signatures** for architectural versus execution failures.
- **The decision rules** below, and who makes the final call. That should be you, or the CEO, not either camp.

Present it to each leader as taking their view seriously. To the CTO: if your diagnosis is right, this produces the evidence to fund a rewrite with much better odds than one launched on conviction. To the head of product: a vague incremental plan won't pass either, so yours needs a committed end state and metrics.

## Start now: no-regret moves

These make sense whatever the evidence shows:

1. **Build the golden-transaction regression suite** on one representative area. It serves as the regression test for classifying contested time, the parity check for a rewrite, the safety net for extraction, and your first delivery improvement.
2. **Cap customer-specific variance.** From now on, any new customer-specific behavior goes into configuration or requires executive sign-off with its long-term cost stated. This stops the variance problem growing while you measure it.
3. **Collect attrition and competitive evidence.** Code the last two years of exit interviews and lost-deal notes. Separate "the stack itself" from "toil and fear of breaking things," and "cloud-native" as marketing from specific buyer requirements like vendor hosting or APIs.

## Weeks 1–5: Lead-time breakdown

- Reconstruct 25–40 recent features from commits, pull requests, deploys, and short interviews.
- Classify time into architecture, delivery practice, variance, and external release constraints. Flag contested intervals.
- Attempt one out-of-cycle release to a willing customer to find what actually forces release batching.
- Build the slice candidate pool from the same data.

**Decision point 1, around week 5:** compare the architecture share, computed with and without contested intervals, against the threshold.

- **Clearly below:** skip the slice tests. Put the investment into delivery practices and reducing variance. Fund modernization only where the attrition, competitive, or knowledge-risk evidence independently justifies it.
- **Above, or decision depends on contested intervals:** run the slice tests, weeks 5–13, with slices picked by the rival camp. The regression suite resolves the contested intervals in parallel.

## Week ~13: Decision meeting

Apply the pre-agreed rules:

| Evidence | Strategy |
|---|---|
| Architecture share below threshold | **Delivery and variance program**, plus targeted fixes like hosting or an API layer if lost deals demand them |
| Architecture share high, extraction passes | **Incremental modernization with a committed end state**, a sequence of capabilities, and lead-time targets per quarter, plus delivery work |
| Architecture share high, extraction fails, rebuild passes and projects within plan | **Rewrite**, but delivered slice by slice, with replay parity and incremental migration of in-force policies, never a big-bang cutover |
| Architecture share high, both fail | **Reduce scope first**: retire variants, sunset little-used features, simplify the product. Then revisit. Neither strategy works on a system whose scope you can't recover or separate. |

## Resourcing

Roughly 4–8 engineers for a quarter, including at least two who know the old system deeply. Everyone else keeps shipping the features customers are asking for.

## What I expect, held loosely

Based on how systems like yours usually turn out, I'd expect delivery practices and customer variance to account for more of your lead time than either leader assumes. The likely result is some version of the head of product's plan, with a firmer end state and more delivery investment than they've proposed. But the point of this plan is that you don't have to take my expectation, or either leader's, on trust. In about three months, you'll know which view survived.

## Outcome summary (sent to Jev)

The assistant recommends not committing to either the rewrite or incremental modernization yet. Instead, run a quarter-long evidence phase while continuing to ship features, then decide at a scheduled meeting using rules both leaders sign in advance. You, or the CEO, make the final call. Neither camp does.

**Why:**
- The rewrite conjecture is weaker. Its "never" claim is easy to protect from disconfirmation, and it offers no mechanism against the new system decaying the same way. It also hides its riskiest assumptions: knowledge recovery and migration of in-force policies.
- The incremental plan is better but underspecified.
- Delivery practices and customer variance may matter more than architecture.

**Steps:**
1. **Decision charter.** Record the required speedup S, an assumed modernization effectiveness r of 0.5, and a threshold for the architecture share of lead time derived through Amdahl's law. Add slice eligibility criteria, rival-picks selection, pass/fail thresholds, failure signatures, and decision rules.
2. **No-regret moves.**
   - Build a golden-transaction regression suite.
   - Cap new customer-specific variance.
   - Code exit interviews and lost-deal notes.
3. **Lead-time breakdown.** Reconstruct 25–40 features into four buckets: architecture, delivery practice, variance, and external release constraints. Attempt one out-of-cycle release to see what forces batching.
4. **Slice tests, only if needed.** Run them if the architecture share exceeds the threshold, or if contested intervals decide the outcome. Use about 4–8 engineers, including two with deep legacy knowledge.

**Decision rules:**

| Evidence | Strategy |
|---|---|
| Architecture share below threshold | Delivery and variance program, plus hosting or an API layer if lost deals demand it |
| Extraction passes | Incremental modernization with a committed end state and quarterly lead-time targets |
| Extraction fails, rebuild passes and projects within plan | Rewrite, delivered slice by slice with replay parity and incremental migration, never a big-bang cutover |
| Both fail | Reduce scope first, then revisit |

**Caveats:** One slice is a small sample, and passing a slice doesn't prove the whole system can be rebuilt. A low architecture share doesn't refute the attrition, competitive, or knowledge-fragility arguments. The assistant loosely expects a firmer version of the head of product's plan to win.
