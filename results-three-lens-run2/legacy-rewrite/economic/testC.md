# legacy-rewrite/economic/testC

Model: claude-opus-5-5 · 2026-09-24T15:26:22.526642+00:00

## Turn 1

**User:** Use profit maximization to answer the following.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

# Short answer: modernize incrementally, but fund it like a real transformation

Judged by expected, risk-adjusted, discounted profit, the incremental strategy wins in most situations like yours. The full rewrite is the right call only under a few specific conditions, listed below. Your CTO is correct about the problem and wrong about the remedy.

## How to frame the decision

For each strategy, compare over roughly five years:

**Profit = revenue retained + new revenue won − engineering and migration cost − cost of failure × probability of failure**, discounted to today.

The two strategies differ less in their best-case outcome than in **when value arrives** and **how likely you are to get it at all**.

## Why the full rewrite scores poorly

**1. It puts your existing revenue at risk for two years.**
During a rewrite you either freeze features on the old system or staff two teams. A freeze invites churn and loses deals to the very competitors you're worried about. Two teams roughly doubles cost and splits your best people. Either way, you pay for two years while the revenue that funds the rewrite erodes.

**2. The payoff is all-or-nothing and back-loaded.**
A rewrite delivers almost no value until it's complete and customers have migrated. Discounting punishes this, and so does the lack of optionality. If you're 60% done when money gets tight, you own 60% of something nobody can use.

**3. The probability of failure is high, especially in your domain.**
A 20-year-old P&C policy admin system encodes a great deal that isn't written down:
- state-specific rating rules
- forms and filings
- endorsements, mid-term changes, and cancellation and reinstatement logic
- edge cases each customer depends on

A rewrite has to rediscover all of this. Large rewrites routinely run over schedule and budget or are abandoned. A realistic plan is closer to 3–4 years than 2.

**4. "Finished" isn't the end.**
Your customers are insurers. They must convert policy books, re-test, and sometimes re-file with regulators. Many will delay migration for years. You'll run both platforms far longer than planned, which is the worst cost position of all.

## Why incremental modernization scores better

- **Revenue is protected.** You keep shipping what customers ask for, so retention and win rates hold.
- **Value arrives continuously.** Each carved-off capability can pay back on its own: faster rating changes, a modern API layer, a better agent portal. Early payback compounds and improves NPV.
- **Risk is bounded.** A failed module costs one module, not the company. You can reprioritize, pause, or accelerate as you learn.
- **Migration is gradual.** Customers adopt new components without a big-bang conversion.

## The honest costs of incremental

These are real and belong in the math:
- Integration seams add overhead. Syncing data between old and new components is often the hardest part.
- It can stall into a permanent half-modernized state if it's treated as a side project.
- It may take longer to legitimately claim "cloud-native" across the whole product.

These are execution risks you can manage. The rewrite's risks are structural.

## Addressing the three pressures directly

- **Slow features:** Target first the areas where most change requests land, typically product and rating configuration and integrations. That's where speed gains turn into revenue fastest.
- **Engineer attrition:** Put new capabilities on the modern stack so your strongest engineers do modern work now, not in two years. A rewrite doesn't fix attrition for the people maintaining the old system during it.
- **Competitor "cloud-native" marketing:** This is partly a sales problem with a faster fix. You can offer the existing system as a managed, cloud-hosted SaaS offering and expose modern APIs within months. Insurer buyers weigh reliability, compliance, and conversion risk heavily, and "we won't make you migrate onto an unproven platform" is a strong counter-message.

## When the rewrite would actually be the profit-maximizing choice

Reconsider if any of these is true:
1. **The architecture has no seams.** For example, business logic lives in one tangled database and stored procedures, so nothing can be carved off without touching everything.
2. **Revenue is already collapsing.** If current customers are leaving fast regardless, protecting the status quo is worth little, and a bolder bet has less downside.
3. **You're targeting a different market.** A new segment, such as MGAs, insurtechs, or small carriers with simpler lines, could justify a greenfield product built alongside the legacy system rather than as a replacement for it.
4. **The functional core is much smaller than it looks.** If most of the codebase is dead weight, a rewrite is less risky than usual.

## What I'd recommend doing

1. **Commit to the incremental approach with real funding.** Dedicate a meaningful share of capacity, on the order of 30–50%, and name a leader. Make it a strategic program, not spare cycles.
2. **Sequence by profit impact.** Rank capabilities by revenue at risk or unlocked versus extraction difficulty. Common early candidates are an API and integration layer, rating and product configuration, and customer- or agent-facing portals. Leave the policy core and data model for later.
3. **Neutralize the marketing gap quickly** with cloud hosting and SaaS operations for the current system.
4. **Set metrics and a checkpoint.** Track:
   - lead time for features
   - the share of transactions flowing through new components
   - engineer attrition
   - win and loss rates against the cloud-native competitors

   Review at 12–18 months. If a hard seam or evidence of condition 1 above appears, you can revisit a more aggressive replacement of that specific core, with far better knowledge than you have today.
5. **Give the CTO a meaningful role.** The CTO could own the target architecture that each carved-off piece conforms to. That way the incremental path converges on the modern platform they're rightly pushing for, rather than drifting.

## Questions that could change this answer

- Can you isolate business logic from the database today, even partially?
- What are your current churn and win-rate trends?
- How many customers would realistically migrate to a new platform within two years of launch?
- Can you afford to fund two teams for three or more years without harming current delivery?

If the answers are "no seams," "revenue collapsing," "most would migrate quickly," and "yes, easily," the rewrite becomes competitive. Otherwise, the incremental path is the higher expected-profit strategy.

## Turn 2

**User:** Sticking with profit maximization, how would you decide how much of our engineering capacity to put into modernization versus shipping customer features?

**Assistant:**

# Short answer: allocate until the last engineer-month in each bucket earns the same return

The profit-maximizing split is where **the marginal engineer-month spent on modernization produces the same expected profit as the marginal engineer-month spent on features**. If the next unit of modernization is worth more than the least valuable feature you're shipping, shift capacity toward modernization, and vice versa.

In practice you can't compute this precisely, but you can estimate it well enough to pick a defensible starting number and adjust it quarterly.

## Step 1: Recognize there are really three buckets, not two

Before splitting between modernization and features, measure what you're actually spending today:

1. **Mandatory work:** regulatory and rate changes, security, production support, bug fixes, contractual commitments. This isn't discretionary.
2. **Customer features:** new capabilities that win or retain revenue.
3. **Modernization:** work that makes future engineering cheaper and faster.

In 20-year-old systems, bucket 1 is often 30–50% of capacity. This matters because **one of modernization's main payoffs is shrinking bucket 1**. The real comparison is not just "features now vs. modernization now." It is "features now vs. more feature capacity later."

## Step 2: Estimate the value of the marginal feature

Rank your feature backlog by expected profit per engineer-month. Useful inputs:
- **Revenue tied to it:** deals in the pipeline that need it, weighted by probability of closing.
- **Retention risk:** renewals where customers have said this is a sticking point.
- **Cost of delay:** does value evaporate if it ships in 9 months instead of 6? Features tied to a specific deal or regulatory deadline have high cost of delay. Nice-to-haves usually don't.

The number that matters is not your *best* feature. It's the **features you'd cut** if you moved capacity to modernization. If the bottom third of your roadmap is low-conviction requests with no revenue attached, moving that capacity costs you little.

## Step 3: Estimate the value of the marginal modernization unit

Modernization pays off through several channels. Estimate each:

- **Velocity gain:** if carving off rating and product configuration cuts the lead time for rate and product changes from months to weeks, how much more feature work does that free up each year, forever?
- **Reduced mandatory load:** fewer incidents, less manual work, less effort per regulatory change.
- **Attrition savings:** replacing a senior engineer typically costs somewhere around 0.5–2× annual salary once you count recruiting, ramp-up, and lost knowledge. If modern work measurably reduces departures, that's real money.
- **Competitive win rate:** deals won or retained because you can credibly demonstrate modern capabilities.
- **Risk reduction:** lower probability of a major outage or of losing the few people who understand critical code.

Modernization's value is **cumulative and compounding**. Features mostly pay once. A velocity improvement pays every year after it lands.

## Step 4: A worked illustration

*These numbers are illustrative assumptions. Substitute your own.*

- 100 engineers at about $200k loaded cost, so roughly $20M/year of capacity.
- Today: 45% mandatory, 55% features, ~0% modernization.
- Proposal: move 30 engineers ($6M/year) to modernization for two years, reducing feature capacity from 55 to 25 engineers.

Assumed payoff:
- After two years, mandatory load drops from 45% to 30%. That frees 15 engineers, about $3M/year of capacity, permanently.
- Remaining feature work is about 1.5× faster on modernized components.
- Attrition among senior engineers falls enough to save about $1M/year.

Cost side: the feature work you gave up. If those 30 engineer-slots would have produced features worth, say, $4M/year in retained and new revenue, you're giving up about $8M over two years. You're also spending the same salaries either way; the question is purely which output they produce.

After year two, you have roughly 55 engineers' worth of effective feature capacity again (the original 25, the returning 30, and the 15 freed from mandatory work) running 1.5× faster. That's substantially more feature output than today, plus the attrition savings. Over a five-year horizon, the investment pays back comfortably under these assumptions.

**The sensitivity check matters more than the answer.** Ask what has to be true for this to break even. If it only works when velocity improves 3×, the case is weak. If it works even at a 20% improvement, it's robust.

## Step 5: Apply the constraints that override the math

Pure marginal analysis needs guardrails:

1. **A feature floor.** Protect renewals, contractual commitments, and deals that are close to signing. Losing a major carrier during modernization can wipe out years of efficiency gains. Set this floor from your actual pipeline and renewal calendar, not a round number.

2. **A modernization floor.** Modernization is lumpy. A half-extracted component delivers nothing and adds integration overhead. Below a certain staffing level, work spreads thin, nothing finishes, and the program stalls. Fund enough to complete one meaningful capability at a time with a dedicated team, rather than assigning engineers 20% here and there.

3. **Cash and margin constraints.** If your margins or investors can't tolerate a dip in near-term revenue growth, your effective discount rate is higher, and that favors features. Be honest about this rather than pretending the long-run math settles it.

4. **Absorption capacity.** Your organization, your customers, and your architecture can only absorb so much change at once. Doubling modernization staffing rarely doubles progress.

## Step 6: Look for work that counts twice

The highest-return capacity is work that serves both goals. When a customer requests something in an area you plan to modernize anyway, build it on the new component. You satisfy the customer and advance the migration with the same effort. Sequencing modernization to follow the feature roadmap raises the effective return on both buckets and reduces the tension between your CTO and head of product.

## Step 7: Set a starting number and adjust quarterly

Given what you've described (slow delivery, attrition, competitive pressure, but a system that still runs most of your revenue), a reasonable starting point for many companies in your position is **roughly 25–35% of total capacity on modernization**, with the feature floor set by your renewal and pipeline commitments. Treat that as a hypothesis to test, not a rule.

Review each quarter with a small set of signals:

| Signal | Suggests shifting toward |
|---|---|
| Lead time on modernized areas falling, mandatory load shrinking | Modernization is paying off; hold or increase |
| Win rate dropping, key renewals at risk over missing features | Features |
| Modernization milestones slipping repeatedly | Fix execution before adding capacity |
| Senior attrition continuing despite modernization work | Check whether the right people are on the new work |
| Low-value features filling the roadmap | Modernization |

## The bottom line

Don't pick a percentage by negotiation between the CTO and head of product. Have each quantify the marginal value of their bucket in the same units: expected profit per engineer-month, over the same horizon and discount rate. Compare the weakest item each would fund. That turns a political argument into an estimation problem, and estimation problems get better with data each quarter.

## Turn 3

**User:** Still looking at it through profit maximization, how should we decide which capability to carve off first?

**Assistant:**

# Short answer: pick the capability with the highest risk-adjusted return per unit of effort, with extra weight on what it teaches you

Each carve-off is an investment. Rank candidates by expected profit relative to cost and risk, as you would any portfolio. The **first** carve-off is special, though. Besides its own payoff, it builds the infrastructure, patterns, and credibility that make every later extraction cheaper. So the first choice should favor capabilities that are **valuable, cleanly separable, fast to deliver, safe to fail, and instructive**, even if a bigger prize exists elsewhere.

## Step 1: Find where the money is using data, not opinions

Before debating candidates, spend two to four weeks gathering evidence:

- **Change frequency:** From version control and your ticket system, find which parts of the codebase change most often. Frequent change combined with slow change is where velocity gains are worth the most.
- **Cost per change:** Estimate engineering hours and elapsed time for typical changes in each area. A rate update that takes three months is a very different problem from one that takes three days.
- **Revenue linkage:** Which areas come up in lost deals, renewal escalations, and competitor comparisons?
- **Mandatory load:** Which areas generate the most incidents, regulatory rework, and manual workarounds?
- **Attrition signals:** Which areas do engineers dread working in? Exit interviews often name them.

The value of modernizing an area is roughly **(how often you change it) × (how much each change costs now minus what it would cost after) + revenue unlocked + mandatory work eliminated**. Areas that rarely change are poor early candidates no matter how ugly the code is.

## Step 2: Estimate extraction cost and risk

For each candidate, assess:

- **Coupling:** How many other parts of the system call into it or share its data? Loosely coupled capabilities are far cheaper to extract.
- **Data entanglement:** Does it own its data, or does it read and write shared tables that the policy core also uses? Shared data is usually the hardest part of any extraction.
- **Correctness risk:** What happens if the new version is subtly wrong? In insurance, errors in premiums, forms, or cancellations can mean regulatory exposure and customer harm.
- **Reversibility:** Can you run the new component in parallel, compare outputs, and switch back instantly if something goes wrong?
- **Customer migration friction:** Can the new component slot in invisibly behind your existing interfaces, or do insurers have to convert, re-test, or re-file anything?

## Step 3: Add the value of learning

The first extraction forces you to build things every later extraction needs:
- an integration or facade layer that routes requests to old or new components
- data synchronization patterns between old and new stores
- deployment pipelines, observability, and testing for the new stack
- a playbook for parallel running and cutover

It also produces something harder to quantify: evidence for the board, customers, and engineers that modernization delivers. A successful first extraction raises the expected return of the whole program. A failed one can end it.

This means the first choice should be **valuable enough to matter but safe enough to finish**. Two common mistakes:

- **Starting with the hardest core to prove the approach works.** Tackling the policy core first concentrates maximum risk at the point where you know the least. If it stalls, the program loses credibility.
- **Starting with something trivial.** Extracting a low-value utility service succeeds but proves nothing, pays back little, and doesn't exercise the hard patterns, especially data synchronization.

## Step 4: Score the candidates

A simple scoring approach works well. Rate each candidate 1–5 on each dimension, weight the dimensions, and compare. Treat the scores as a structured argument, not precise math.

*Illustrative scores for typical P&C capabilities. Your data will differ.*

| Capability | Value (change frequency, revenue) | Ease (coupling, data) | Safety (reversibility, correctness) | Time to value | Learning value | Customer friction (5 = invisible) |
|---|---|---|---|---|---|---|
| Rating engine | 5 | 4 | 4 (can shadow-run) | 3 | 4 | 5 |
| Document and forms generation | 3 | 4 | 4 | 4 | 3 | 5 |
| Agent and customer portals | 4 | 3 | 3 | 4 | 3 | 3 |
| Product configuration | 5 | 2 | 3 | 2 | 4 | 4 |
| Billing | 3 | 2 | 2 | 2 | 4 | 2 |
| Policy core and data model | 5 | 1 | 1 | 1 | 5 | 1 |

In this illustration, **rating** stands out. It often has high change frequency because rate filings, new states, and new programs come up constantly. Rating logic is relatively self-contained, since it takes inputs and returns a premium, which makes a clean seam. Above all, it can be **shadow-run**: the new engine calculates premiums in parallel with the old one, you compare every result, and you cut over only once they match. That turns a high-correctness-risk component into a low-risk extraction.

Your actual answer depends on your data. If your rating logic is spread through stored procedures and entangled with policy data, something like document generation may be the better first move.

## Step 5: Check the sequence, not just the first step

The first extraction shapes what comes next. Before committing:

- **Map dependencies.** Some capabilities are much easier to extract once others are out. For example, product configuration often becomes easier after rating has been separated, because much of product definition is rating structure.
- **Consider the enabling layer.** You'll almost certainly need an API or facade in front of the legacy system before any extraction works cleanly. It isn't a customer-facing capability, but it usually pays for itself quickly: it enables modern integrations customers want, and it helps answer the "cloud-native" pitch. Scope it to what the first extraction needs, rather than building a grand platform up front.
- **Sketch the next two or three extractions** so the first one builds patterns you'll reuse.

## Step 6: Define success and failure criteria before starting

Set these in advance, in profit-relevant terms:

- **Success:** For example, rate changes that took 10 weeks take 2; incidents in the area fall by half; the new component handles all production traffic for a line of business within a set time.
- **Kill or rethink triggers:** Cost or time running more than about 50% over estimate, shadow-run discrepancies that don't converge, or data synchronization proving much harder than expected.
- **Pilot scope:** Consider starting with one line of business, one state, or one willing customer before rolling out broadly. This limits the damage if something goes wrong and gives your sales team a reference story.

## The bottom line

Don't pick the first capability by what's most painful, most prestigious, or most exciting to engineers. Pick the one where frequent, costly change meets a clean seam and a safe path to cutover, and where success will teach you the patterns the rest of the program needs. In many P&C platforms that turns out to be rating, but your change-frequency and coupling data should make the final call. The first extraction's biggest job is to make the second one cheaper and more believable.

## Turn 4

**User:** Still using profit maximization, how should we handle the existing customers who may never want to move off the legacy components?

**Assistant:**

# Short answer: treat each holdout as its own profit decision, and make migration a non-event wherever you can

Customers who won't move aren't a single problem. Some are worth significant effort to migrate, some are worth keeping on legacy at a price that covers the cost, and a few may be worth letting go. The profit-maximizing approach has four parts:
- reduce the number of customers who ever have to "move" at all
- understand each remaining holdout's economics
- price legacy support to reflect its real cost
- plan sunsets component by component rather than for the whole platform at once

## Step 1: Shrink the problem by making most migration invisible

The strangler approach has a built-in advantage. If new components sit behind the same interfaces customers already use, many customers never experience a migration. You simply route their traffic to the new component once it's proven.

The rating example shows how this works. If you shadow-run the new engine until its outputs match the old one exactly, you can switch customers over without them changing anything. That matters in insurance because rate filings describe specific rating algorithms. Identical outputs generally mean customers shouldn't need to refile. Confirm this for each state and program with your customers' compliance teams, but it removes a major source of resistance.

Customers only become true holdouts when migration touches something they control or depend on:
- their integrations
- their workflows and staff training
- their data
- their regulatory filings
- their contract terms

Every design choice that avoids touching these shrinks the holdout population. That's usually the cheapest lever you have.

## Step 2: Use insurance's natural migration moment: renewal

P&C policies typically renew annually, and that gives you a lower-risk migration path than converting policies mid-term:
- **New business** goes onto the new components once a customer is ready.
- **Existing policies migrate at renewal**, so no in-force policy is converted mid-term.
- **The legacy book runs off** as policies expire.

Two cautions:
- Claims, audits, and record-retention requirements can last years after a policy expires. Legacy data must stay accessible, even read-only, long after new transactions stop.
- Mandatory regulatory updates must continue on legacy components as long as customers write business on them. You can't let compliance lapse to push people off.

## Step 3: Segment holdouts by value and migration cost

For each holdout customer, estimate:
- **Revenue and margin** from the account.
- **Incremental cost to serve them on legacy:** their share of the engineering, infrastructure, and support needed to keep legacy components running.
- **Migration cost:** your engineering and services effort, plus any incentives you'd offer.
- **Churn risk** under each option. How likely are they to go to market if pushed?
- **Strategic value:** reference potential, expansion opportunity, influence in their market.

The value of migrating a customer is roughly:

**Legacy cost saved + expansion revenue on the new platform + retention improvement − migration cost**

Then sort customers into four groups:

| | **Low migration cost or willing** | **High migration cost or resistant** |
|---|---|---|
| **High value** | **Early adopters.** Migrate first, co-design with them, make them reference customers. | **Invest to retain.** White-glove migration, subsidized conversion, executive attention. Losing them is expensive. |
| **Low value** | **Self-service.** Standard tooling and documentation, minimal custom effort. | **Price to cost, then sunset.** Charge what legacy actually costs to run. Accept that some will leave. |

The bottom-right group is where profit discipline matters most. Keeping low-margin, high-cost customers on legacy indefinitely often costs more than they're worth. Letting some of them go can be the profitable outcome, as long as you're deliberate about it.

## Step 4: Price legacy support to reflect real cost

Legacy components have a large **fixed cost** of engineers, infrastructure, security patching, and regulatory updates that doesn't shrink much as customers leave. As the legacy population falls, the **cost per remaining customer rises**. The last few holdouts end up carrying most of the cost of keeping the old system alive.

Options, from gentlest to firmest:

1. **Extended support pricing.** Charge a fee that reflects the true incremental cost of remaining on legacy components, and make it visible. This is standard practice in enterprise software.
2. **New features only on new components.** Legacy customers keep what they have, plus mandatory updates, but innovation happens on the new platform. This creates pull without forcing anyone.
3. **Migration incentives.** Credits toward conversion services, price protection for customers who move by a certain date, or early access to new capabilities.
4. **Announced sunset dates** per component, with long notice periods. Two to three years is common for enterprise insurance software, but check your contracts.

Watch price elasticity carefully. A price increase or sunset notice can trigger a competitive RFP, and your cloud-native competitors will be glad to bid. Set legacy pricing high enough to cover cost and signal direction, but not so high that it pushes valuable customers to reconsider their vendor entirely. For high-value accounts, a migration subsidy is often cheaper than the churn risk created by a price hike.

## Step 5: Know your contractual and regulatory obligations

Before making any sunset or pricing decision, review:
- **Support terms and SLAs** in existing contracts, which may commit you to supporting specific versions or components for defined periods
- **Notice periods** required for material changes
- **Regulatory obligations** tied to policies in force, record retention, and data access

These set the floor for how fast and how firmly you can act, and they differ by customer.

## Step 6: Track legacy costs per component and decide sunsets one at a time

Set up cost accounting for each legacy component: the engineering time, infrastructure, support, and compliance work it consumes. Then, for each component:

- **Sunset when the cost of keeping it alive exceeds what the remaining customers on it are worth**, after accounting for the churn risk of forcing the move.
- **Recheck regularly.** Each customer who migrates raises the cost per remaining customer, which can make the next sunset decision easier.

Component-level sunsets avoid a single high-stakes "turn off the old platform" date. You retire rating on legacy when rating's remaining users no longer justify it, then documents, then portals, and so on.

## Step 7: Don't let holdouts dictate your architecture

A few resistant customers shouldn't force you to maintain two full versions of every capability indefinitely. Keep the new components compatible with legacy interfaces through your facade layer, so even holdouts can be moved to new components behind the scenes. That way the legacy code shrinks even while some customers never consciously "migrate."

## Other options for the long tail

If a small group of holdouts remains after most customers have moved, you can:
- **Offer a limited-change "sustain" tier:** stable, compliant, no new features, priced to cover its costs.
- **Outsource legacy maintenance** to a specialist firm, if that's cheaper than keeping in-house expertise.
- **License the legacy code** to customers who want to self-support. This is rare, but it sometimes suits very large insurers.
- **Negotiate a managed exit** for customers who will never move, including data export and transition help. This preserves goodwill and your reputation in a market where references matter.

## The bottom line

Most customers should never experience migration as an event. Route them to new components invisibly, and use renewal cycles for anything that can't be invisible. For the true holdouts, calculate each account's economics:
- Invest heavily to migrate high-value customers.
- Price legacy support to its real cost for the rest.
- Retire legacy components one at a time as the remaining customers on each no longer justify its fixed cost.

The goal isn't to get every customer off legacy. It's to stop paying more to keep legacy alive than those customers are worth.

## Turn 5

**User:** What should we do?

**Assistant:**

# What I'd do in your position

Commit to incremental modernization as a funded, board-level program. Put roughly a third of engineering capacity behind it. Close the "cloud-native" gap commercially within months. Carve off the capability your data says has the best return, likely rating. Make migration invisible for most customers and price legacy support to its real cost for the rest.

Here is how that turns into action.

## Decisions to make now

1. **Choose incremental modernization over the full rewrite.** It protects the revenue that funds everything else, delivers value continuously, and caps your downside. Revisit only if you find the system truly can't be separated into pieces, or that revenue is collapsing regardless.
2. **Fund it at about 25–35% of engineering capacity**, with a firm floor for features tied to renewals and live deals. Staff it as dedicated teams, not spare time.
3. **Give the CTO ownership of the target architecture** and make the program jointly accountable with the head of product. The CTO's diagnosis is right, and this puts it to work. Product keeps revenue protected. Both leaders are measured on the same outcomes.
4. **Agree on one decision rule:** capacity, sequencing, and sunset choices are made by comparing expected profit in the same units, over the same horizon. This turns future disagreements into estimation questions rather than turf battles.

## First 90 days

**Gather the data that drives everything else:**
- Measure the current split between mandatory work, features, and modernization.
- Pull change-frequency and cost-per-change data from version control and your ticket system.
- Map coupling and shared data for the top candidate capabilities.
- Link lost deals, renewal escalations, and exit interviews to specific areas of the system.
- Build rough per-customer economics: revenue, margin, cost to serve, and churn risk.

**Close the competitive gap quickly:**
- Launch or firm up a cloud-hosted, managed offering of the current system.
- Start a thin API layer in front of it, scoped to what customers want for integrations and what the first extraction needs.
- Give sales a clear message: modern capabilities, no forced platform migration.

**Pick and scope the first extraction:**
- Score candidates on value, ease, safety, time to value, learning value, and customer friction.
- Rating is the likely front-runner because it changes often, has a clean seam, and can be shadow-run. Let the data confirm it.
- Set success metrics and kill criteria before starting.
- Choose a pilot scope, such as one line of business, one state, or one willing customer.

**Protect your people:**
- Staff the first extraction with engineers you're most at risk of losing.
- Tell the whole team about the plan openly. A credible path forward is itself a retention tool.

## Months 3–12

- Build the first extraction, shadow-run it against the legacy system, and cut over once outputs match.
- Confirm with customers' compliance teams whether rating changes require refiling in the relevant states.
- Keep shipping committed features. Where a requested feature falls in an area being modernized, build it on the new component so it counts twice.
- Set up cost accounting for each legacy component so later sunset decisions rest on real numbers.
- Begin segmenting customers by value and likely migration difficulty, and recruit two or three high-value early adopters as design partners and references.

## Months 12–24

- **Checkpoint at 12–18 months** against your metrics: feature lead time, share of traffic on new components, mandatory load, senior attrition, and win and loss rates against the cloud-native competitors.
- If the first extraction paid off, extract the next two or three capabilities in the sequence your dependency map suggests.
- If it struggled, fix execution before adding capacity.
- Introduce extended-support pricing for legacy components and a "new features on the new platform" policy. Give long notice, and check contract terms first.
- Move policies to new components at renewal where migration can't be invisible.

## Year 2 onward

- Retire legacy components one at a time, when each one's cost exceeds what its remaining customers are worth.
- Invest in white-glove migration for high-value holdouts. Price to cost, or manage an orderly exit, for low-value ones.
- Leave the policy core and data model for last. By then you'll have the patterns, tooling, and credibility to tackle them.

## Metrics to report to leadership quarterly

| Metric | What it tells you |
|---|---|
| Lead time for changes in modernized vs. legacy areas | Whether modernization is buying speed |
| Mandatory work as a share of capacity | Whether you're freeing capacity for growth |
| Share of transactions on new components | Real migration progress |
| Senior engineer attrition | Whether the talent problem is easing |
| Win and loss rates against cloud-native competitors | Whether the market gap is closing |
| Legacy cost per remaining customer, by component | When to sunset each component |
| Renewal rate and net revenue retention | Whether revenue is protected during the transition |

## What would change this recommendation

- **The discovery work shows no workable seams.** A more aggressive replacement of the core becomes worth modeling.
- **Churn is accelerating regardless of what you ship.** Protecting the status quo is worth less, and a bolder bet has less to lose.
- **A distinct new segment is within reach**, such as MGAs or smaller carriers. A separate greenfield product alongside modernization could be justified.
- **Cash or margins can't absorb a temporary dip in feature output.** You'd start closer to 20% on modernization and ramp up as early wins free capacity.

## The one-sentence version

Stop debating rewrite versus incremental and start measuring. Fund incremental modernization seriously, prove it on the capability with the best return, keep revenue protected throughout, and let each quarter's data decide how fast to go.

## Outcome summary (sent to Jev)

The assistant recommends incremental modernization over a full rewrite, run as a funded, board-level program with roughly 25–35% of engineering capacity in dedicated teams and a firm floor protecting features tied to renewals and live deals. Judged by expected, risk-adjusted, discounted profit, incremental work protects the revenue that funds everything, delivers value continuously, and caps downside. A rewrite puts existing revenue at risk, pays off only at the end, carries a high failure probability given undocumented P&C rules, and forces years of running two platforms.

The CTO should own the target architecture, jointly accountable with the head of product. Capacity, sequencing, and sunset decisions should all compare expected profit in the same units and horizon.

In the first 90 days the company should:
- measure the split between mandatory work, features, and modernization
- pull change-frequency and cost-per-change data
- map coupling and shared data
- link lost deals and exit interviews to system areas
- build per-customer economics

It should also launch a cloud-hosted managed offering and a thin API layer to answer "cloud-native" competitors. The first extraction, likely rating because it changes often, has a clean seam, and can be shadow-run, should be scored against alternatives, given success metrics and kill criteria, piloted narrowly, and staffed with at-risk engineers. Features requested in areas being modernized should be built on new components.

Migration should be invisible for most customers or done at renewal. Legacy support should be priced to cost, high-value holdouts migrated with white-glove help, and components retired individually, leaving the policy core last. There should be a 12–18 month checkpoint on lead time, mandatory load, traffic share, attrition, and win rates.

This changes if no seams exist, churn is accelerating regardless, a distinct new segment appears, or cash constraints require starting near 20%.
