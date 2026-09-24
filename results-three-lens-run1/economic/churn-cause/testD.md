# economic/churn-cause/testD

Model: claude-opus-5-5 · 2026-09-24T14:53:23.184578+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

**Assistant:**

# Churn Analysis: Product Gaps vs. Implementation Experience

## Which belief is right

Without your data, I can't tell you which belief is right, and I'd be wary of anyone who could. Both VPs have a plausible theory, and both theories conveniently call for more investment in their own function. Before you commit, you can test which one is true in about four to six weeks.

Three features of your business make this question tricky:

1. **Churn is a lagging indicator.** Carrier contracts are typically multi-year. A customer who left last quarter probably decided 12–18 months ago, based on an implementation that happened 2–4 years ago. Today's churn reflects old decisions, and any fix will take a full renewal cycle to show up.
2. **Exit reasons are unreliable.** "Your competitor has better analytics" is a polite, blameless thing to tell a vendor. It's often said by customers who never adopted the analytics you already have. Stated reasons need to be checked against usage data.
3. **The two theories interact.** AI and analytics in claims depend on clean, well-integrated data. If implementations leave customers with partial integrations and messy data, new AI features will ship into accounts that can't use them. In that case the product strategy depends on the services fix first.

There's also a third possibility neither VP raised: **structural churn.** Regional carriers consolidate, get acquired, or move to their parent's platform. If a meaningful share of the lost ARR came from M&A, neither proposal will fix it.

## The diagnostic: settle the argument with data

| Question | Analysis | If it points to Product | If it points to Services |
|---|---|---|---|
| Where did churned customers go? | Win/loss on every churned account: competitor, in-house, acquired | Mostly to one or two competitors, citing specific capabilities | Mixed destinations, or "replaced with a simpler tool" |
| Did they reach value? | Time-to-go-live, % of modules live, integration completeness, active users vs. licensed | Churned accounts were fully live and heavily used, then left anyway | Churned accounts had long or stalled implementations and low adoption |
| Did they use what exists? | Usage of your current analytics and reporting among churners | Heavy users of existing analytics who outgrew it | Barely touched existing analytics |
| Cohort pattern | GRR by implementation cohort and by implementation duration | Churn rises across all cohorts, including well-implemented ones | Churn concentrates in cohorts with implementations over X months |
| Is it logo or dollar churn? | Separate a few large losses from broad attrition | Large, sophisticated carriers leaving | Many smaller carriers leaving |

Two quick checks are worth doing first:
- **Plot each churned account's implementation duration against its tenure at churn.** If long implementations predict churn, that's your answer for a large share of the problem.
- **Look at the next 12 months of renewals.** Score each account on go-live status, adoption, and competitive exposure. This tells you where the at-risk ARR sits, which matters more than explaining the past.

The likely answer is **segmented**. Newer and smaller carriers leave because they never got to value. Larger, mature accounts get poached on capability. The financial question then becomes how much ARR sits in each bucket.

## Following the money

The figures below are **illustrative assumptions**. Replace them with your actuals. The structure of the comparison is what matters.

**Assumed baseline:** $40M ARR, ~180 carriers, ~$220K average ACV, 78% subscription gross margin. Gross revenue retention fell from 92% to 84%, so annual churn went from $3.2M to $6.4M. The **excess churn is about $3.2M of ARR per year**, and it compounds, because every lost dollar is lost for all future years.

### Proposal A: Accelerate the product roadmap (analytics and AI)

**Revenue it could generate or protect**
- Retains accounts lost to competitive displacement. This only covers the share of churn that is truly capability-driven.
- Adds new revenue if AI and analytics are priced as add-on modules rather than bundled free.
- Improves new-logo win rates, which is real value but doesn't fix retention.

**Investment and operating costs**
- Build: roughly 15–25 engineers, data scientists, and ML engineers at about $200K fully loaded, or **$4–5M per year**.
- Ongoing maintenance: typically 15–25% of build cost every year, indefinitely.
- **Inference and data infrastructure costs land in cost of goods sold.** These lower your gross margin unless they're priced in.
- Regulatory and model governance: AI in claims decisions (triage, fraud, severity) draws state regulatory scrutiny, bias testing, and explainability requirements. Carriers will push these requirements onto you.

**When returns arrive**
- Roughly 9–18 months to ship something competitive.
- Then customers must implement and adopt it, through your implementation process.
- Then the renewal cycle has to pass.
- **Measurable retention impact: roughly 24–36 months out.**

**Risks that could wipe out the return**
- Features ship into poorly implemented accounts and don't get adopted.
- Competitors keep moving, so you pay for parity and never gain an advantage.
- Sales sells the roadmap, dates slip, and you create new churn from broken promises.
- AI features are bundled to "add value," adding cost of goods sold with no new revenue.

**Where spending grows without profit**
- Maintenance obligations accumulate.
- Custom features get built for one large account's renewal.
- Inference costs scale with usage while price stays flat.

### Proposal B: Fix implementation and support

**Revenue it could generate or protect**
- Retains accounts that churn from never reaching value.
- Rescues at-risk renewals in the next 12 months, which is the fastest money available.
- Faster go-lives pull forward revenue recognition and cash, especially if billing or ramps are tied to go-live.
- Frees implementation capacity, so you can convert more of your bookings backlog.
- Customers who reach value expand their licenses and modules.

**Investment and operating costs**
- Dedicated onboarding team, better CSM coverage, and an implementation methodology: **about $1.5–3M per year**.
- Some one-time costs: templates, data migration tooling, integration accelerators.

**When returns arrive**
- Rescue work on near-term renewals: 3–9 months.
- New implementations benefit immediately.
- **Measurable retention impact: roughly 6–18 months out.**

**Risks that could wipe out the return**
- If churn is really competitive, a smooth onboarding onto a product customers are leaving won't save them.
- The fix is headcount-heavy and scales linearly with customers, turning services into a permanent cost center.
- Account saves get bought with free services and discounts, eroding margin.

**Where spending grows without profit**
- Hiring people to manually work around product deficiencies.
- CSM coverage ratios creeping up.
- Free professional services given as concessions.

### Illustrative three-year comparison

| | Year 1 | Year 2 | Year 3 | Cumulative |
|---|---|---|---|---|
| **A: Product** – incremental spend | $5.0M | $5.0M | $3.0M | **$13.0M** |
| A: ARR retained or added (cumulative) | $0 | $0.5M | $3.6M* | |
| A: Gross profit from that ARR | $0 | $0.4M | $2.6M | **$3.0M** |
| **B: Services** – incremental spend | $2.5M | $2.5M | $2.0M | **$7.0M** |
| B: ARR retained (cumulative) | $0.8M | $2.4M | $4.0M | |
| B: Gross profit from that ARR | $0.6M | $1.9M | $3.1M | **$5.6M** |

*Includes about $1.5M of new AI add-on ARR at a lower (~65%) margin because of inference costs.

**How to read it:** Under these assumptions:
- Services pays back in roughly years 3–4, with less capital at risk.
- Product pays back in years 4–5+, and only if its adoption assumptions hold.
- Product has more long-term upside if you price AI as a paid module.

These conclusions reverse if your diagnostic shows most churn is competitive displacement from fully adopted accounts. That's why the diagnostic comes first.

## Governance: who controls, who owns, who stops

This is where I'd push hardest, because the incentives are misaligned:

- **VP Product** would control a larger team and budget but doesn't own the retention number. Nothing in the role forces a stop if features don't move churn.
- **VP Services** may benefit from long implementations. **If implementations are billed time-and-materials, slow implementations generate services revenue and make the services P&L look healthy while destroying subscription retention.** Check this. It may be one of the causes of your problem.
- **Nobody owns gross revenue retention end to end.** That gap is how churn doubled over 18 months without a forcing function.

Recommended structure:
1. **One executive owns GRR and NRR:** the CEO, COO, or a Chief Customer Officer, with you likely running the program. Both VPs are measured on it.
2. **Stage-gated funding.** Release money in tranches tied to leading indicators, not to project milestones:
   - Services: time-to-go-live, % of accounts fully live within X days, adoption depth, health scores of at-risk renewals.
   - Product: adoption of the new feature among target accounts within 90 days, competitive win rate, attach rate if priced.
3. **Kill criteria written before spending starts.** For example: "If feature adoption among fully implemented accounts is below 30% two quarters after launch, we stop expanding the team." The CFO holds the gate, not the function spending the money.
4. **Contract changes:** move toward fixed-fee or milestone-based implementations so services profits line up with speed to value.

## A third approach: targeted time-to-value

I'd recommend a sequenced, gated approach that spends product engineering on adoption rather than feature parity.

**Phase 0: Diagnose (weeks 0–6, about $0.1–0.2M)**
- Run the churn analysis above.
- Score every renewal in the next 18 months.

**Phase 1: Protect the ARR at risk (months 1–9, about $1M)**
- Run a rescue team on at-risk renewals: finish stalled integrations and get modules live.
- Set hard limits on free services concessions.
- This is the highest-return money you'll spend, because the ARR at risk is known and near-term.

**Phase 2: Productize implementation (months 3–18, about 8–10 engineers, ~$2M per year)**
- Point product engineering at the implementation bottleneck:
  - Data migration tooling
  - Prebuilt connectors to common policy administration and general ledger systems
  - Configuration templates for typical regional carrier setups
  - Out-of-the-box dashboards that deliver visible value in the first 60 days
- **This is where both VPs are partially right.** It's a product investment that fixes the services problem, and unlike hiring it gets cheaper per customer as you scale.

**Phase 3: Buy targeted competitive capability instead of building it (gated on the diagnostic)**
- If win/loss shows specific capabilities driving displacement, pick the one or two that matter most.
- Partner, embed, or OEM them (an embedded BI layer, a claims AI vendor) rather than building from scratch.
- Price them as add-ons so they carry their own cost of goods sold.
- Build in-house only where it's truly differentiating and your data position gives you an edge.

**Economics:**
- Year-1 spend: roughly $3–3.5M, close to Proposal B.
- The Phase 2 investment reduces ongoing services headcount needs instead of adding to them.
- Phase 3 capital is committed only once evidence justifies it.
- The business stays profitable because the largest bets are released in tranches.

## What to do Monday

1. Commission the churn analysis, and give it to someone neutral to both VPs.
2. Find out how implementations are billed, and how services margin moves when implementations run long.
3. Pull the list of renewals in the next 18 months, with dollar values and go-live status.
4. Propose single ownership of GRR, plus a gated funding process, to your CEO and CFO.

Bring the diagnostic results back to the leadership team in six weeks. The argument between your VPs will likely become a question of how to allocate between buckets rather than which person is right.

## Turn 2

**User:** If we switch implementations from time-and-materials to fixed-fee, how much services revenue and margin do we lose, and does the retained subscription ARR more than cover it?

**Assistant:**

# Switching from Time-and-Materials to Fixed-Fee Implementations

## Short answer

How much you lose depends almost entirely on two choices: **what price you set** and **whether delivery actually gets faster**. Changing the contract type alone doesn't make implementations faster. It only moves the cost of overruns from your customer to you.

- **Priced at your historical *estimates* with no delivery change:** you lose most of your services margin. Retained ARR does *not* cover it.
- **Priced at realistic scope, with delivery improvements:** services revenue drops modestly, services margin holds roughly flat, and the retained ARR is nearly pure upside.
- **Timing:** the margin effect is immediate, while the ARR benefit arrives at first renewal. With multi-year contracts, that could be 3+ years out.

So the retained ARR shouldn't be treated as the thing that funds the switch. The switch has to roughly pay for itself inside services, with retention as the upside.

## What you actually lose: overrun revenue

Under time-and-materials, the revenue at risk isn't your whole services line. It's the revenue from **hours beyond a reasonable scope**. That's the money you earn *because* implementations run long, which is the same thing driving the churn.

Illustrative model. **Replace these with your actuals.**

| Assumption | Value |
|---|---|
| New implementations per year | 20 |
| Original estimated hours per implementation | 1,000 |
| Actual hours per implementation (60% overrun) | 1,600 |
| Bill rate | $225/hr |
| Fully loaded delivery cost (incl. utilization and bench) | $150/hr |
| New ARR per implementation | $220K |
| Subscription gross margin | 78% |

**Current T&M baseline, per implementation:**
- Revenue: 1,600 × $225 = **$360K**
- Cost: 1,600 × $150 = **$240K**
- Margin: **$120K (33%)**

**Annual baseline:** $7.2M services revenue, $2.4M services margin.

### Three fixed-fee scenarios

| Scenario | Price | Hours delivered | Revenue per impl | Margin per impl | Annual services revenue | Annual services margin | Margin change vs. T&M |
|---|---|---|---|---|---|---|---|
| **1. Priced at estimate, delivery unchanged** | $225K (1,000 hrs) | 1,600 | $225K | –$15K | $4.5M | –$0.3M | **–$2.7M** |
| **2. Realistic price, delivery partly improves** | $315K (1,400 hrs) | 1,500 | $315K | $90K | $6.3M | $1.8M | **–$0.6M** |
| **3. Realistic price, delivery fixed** | $315K (1,400 hrs) | 1,300 | $315K | $120K | $6.3M | $2.4M | **$0** |

**Key points:**
- Scenario 1 is the common failure. Sales quotes the old optimistic estimate as a fixed price, and services absorbs every overrun.
- In Scenario 3, you give up $0.9M of revenue but no margin. The lost revenue was the overrun hours, which cost you as much to deliver as they earned.
- **Check your write-offs.** If you already discount or write off part of your overrun hours to keep customers calm, part of this "lost" revenue is already gone. Your real exposure is smaller than the table suggests.

## What the subscription side gets back

Fixed-fee pricing affects **new implementations and expansion projects**, not the installed base. The retention benefit therefore builds one cohort at a time:

- New ARR per cohort: 20 × $220K = **$4.4M**
- If faster, more complete go-lives cut first-renewal churn in that cohort by **10 percentage points**, you retain about **$440K ARR per cohort**.
- That's about **$343K of gross profit per year**, recurring for as long as those customers stay.
- At a typical retention profile, the lifetime value of that retained ARR is roughly 5× annual gross profit (discounted), or **about $1.7M per cohort**.

### Break-even: how much churn reduction do you need?

**Required churn reduction = annual margin lost ÷ (new ARR per cohort × subscription GM × lifetime multiple)**

The denominator is $4.4M × 78% × 5 ≈ $17.2M.

| Scenario | Annual margin lost | Churn reduction needed to break even |
|---|---|---|
| 1. Priced at estimate | $2.7M | **~16 points** (unrealistic) |
| 2. Partly improved | $0.6M | **~3.5 points** (achievable) |
| 3. Delivery fixed | $0 | **Anything above zero is profit** |

Your churn diagnostic should tell you how much higher first-renewal churn is in long-implementation cohorts. If long implementations carry 15–20 points of excess churn, Scenario 2 clears the bar easily. If the gap is only 3–4 points, Scenario 2 is marginal, and you need Scenario 3 delivery performance.

## Timing: the problem hidden in the averages

The margin loss starts with the first fixed-fee contract. The retention benefit arrives only at first renewal.

**Scenario 2 with 3-year initial terms (cumulative, illustrative):**

| Year | Services margin lost (cumulative) | Retained subscription GP (cumulative) | Net |
|---|---|---|---|
| 1 | –$0.6M | $0 | –$0.6M |
| 2 | –$1.2M | $0 | –$1.2M |
| 3 | –$1.8M | $0 | –$1.8M |
| 4 | –$2.4M | $0.34M | –$2.1M |
| 5 | –$3.0M | $1.03M | –$2.0M |
| 6 | –$3.6M | $2.06M | –$1.5M |
| 7 | –$4.2M | $3.43M | –$0.8M |
| 8 | –$4.8M | $5.15M | **+$0.4M** |

The cumulative benefit grows because each year adds another cohort of retained customers, while the margin loss stays flat.

This is why you can't rely on retention alone to justify the switch. If your initial terms are one year, the curve shifts left by about two years and the case improves sharply.

### Benefits the table leaves out

- **Earlier go-live.** If subscription billing starts at go-live, pulling go-live forward four months brings forward about $73K per customer. This is mostly a timing benefit, but it's real cash. If billing starts at signing, this benefit is zero, so check your contracts.
- **Freed delivery capacity.** Cutting 300 hours per implementation frees about 6,000 hours a year. If you have a backlog of signed customers waiting to start, that capacity converts bookings to revenue sooner.
- **Expansion.** Customers who are fully live buy more modules and users. This is often worth more than the churn reduction itself.
- **Win rates.** Carriers that have been burned by overruns value price certainty, and it can help close deals.

## Risks specific to fixed-fee

1. **Scoping becomes your balance-sheet risk.** Every estimating error is now your loss. Without a disciplined scoping and discovery phase, Scenario 1 is where you end up.
2. **Scope creep without change orders.** Carriers will ask for "one more integration." You need a clear statement of work and a change-order process that services actually enforces.
3. **Revenue recognition.** Fixed-fee services are typically recognized over time using a cost-to-cost method. If projected cost exceeds the fee, you may have to book the full expected loss immediately. Involve your controller before the first contract goes out.
4. **Cash timing.** Milestone billing can delay cash compared with monthly T&M invoices. Front-load a discovery or mobilization payment.
5. **Quality cutting.** Once overruns cost services money, teams may declare go-live early with integrations half-finished. That recreates the churn problem in a different form. **Define go-live by adoption criteria, not by the project closing.**

## Recommended design

Don't flip everything to fixed-fee at once. Structure it so margin is protected while delivery improves:

1. **Paid discovery phase (T&M or small fixed fee).** Scope properly before quoting the fixed price for the main implementation.
2. **Fixed fee for standard scope, priced realistically.** Base the price on your actual historical hours for comparable carriers, less a modest target improvement. Don't use the optimistic estimate.
3. **Change orders for anything outside scope,** billed at T&M.
4. **Milestone billing tied to value:** mobilization, data migration complete, integrations live, and a final payment tied to **adoption criteria** (for example, X% of adjusters active for 30 days).
5. **Pair it with the delivery fix.** The tooling, templates, and connectors from the productization work are what move you from Scenario 2 to Scenario 3. Fixed-fee pricing without them only transfers risk.
6. **Pilot on the next 5–8 new implementations** before converting all new business.

## Measure the combined result, not the services line

Once you switch, the services P&L will look worse even if the company is better off. If your VP of Services is paid on services margin, you've built in resistance. Report and compensate on **contribution per customer cohort**:

**Cohort contribution = services margin + subscription gross profit over the first renewal cycle**

Track these leading indicators from the pilot:
- Actual vs. quoted hours per implementation
- Days to go-live, defined by adoption criteria
- Share of implementations requiring change orders, and how much they add
- 90-day adoption depth
- Write-offs and concessions, which should fall close to zero

**Stop rule:** if pilot implementations run more than about 15% over quoted hours after the first 3–4 projects, pause. Fix scoping and delivery before expanding. Continuing to sell fixed-fee at that point is the path to Scenario 1.

## Data to pull before deciding

1. **Actual vs. estimated hours** for the last 30–40 implementations, segmented by carrier size and modules. This sets realistic pricing.
2. **Write-offs and discounts** on implementation invoices. This shows how much overrun revenue you actually collect.
3. **First-renewal churn by implementation duration.** This is the size of the retention prize.
4. **Whether subscription billing starts at signing or at go-live.** This determines whether faster go-live brings cash forward.
5. **Initial contract term length.** This determines how long you wait for the retention payoff.

With those five numbers, you can replace every assumption above and get a real answer.

## Turn 3

**User:** If most of our overrun hours come from the carrier's own delays, like slow IT teams or late data, how much of the margin loss can we avoid by making customer-caused delays billable?

**Assistant:**

# Making Customer-Caused Delays Billable

## Short answer

Under reasonable assumptions, billing for customer-caused delays recovers roughly **35–45% of the margin loss** in the worst case (fixed fee priced at your old estimates). The hard ceiling is the share of overrun hours that are *truly* customer-caused, and you won't collect all of those. Two caveats matter more than the number:

1. **Don't double-count.** If you've already priced the fixed fee at realistic historical hours (Scenario 2 from before), those hours already include customer delays. Billing for delays on top of that charges carriers twice.
2. **The bigger value is deterrence, not collection.** A billable delay clause mainly changes carrier behavior. Fewer delays mean faster go-lives, which is what protects subscription ARR.

## Not every customer-caused hour is recoverable

"Customer delays" create cost in different ways, and each is recoverable to a different degree.

Illustrative assumptions, carried over from the earlier model:
- 600 overrun hours per implementation
- About 65% customer-caused (390 hours), about 35% vendor-caused (210 hours)

| Type of delay cost | Share of customer-caused hours | Hours | Billable? | Realistic recovery | Hours recovered |
|---|---|---|---|---|---|
| **Rework** from late, incomplete, or bad data | 40% | 156 | Yes, easy to document | ~80% | 125 |
| **Re-mobilization** after pauses (ramp-up, context switching) | 25% | 98 | Yes, if the contract has a re-mobilization fee | ~70% | 69 |
| **Extended project management** over a longer calendar | 25% | 98 | Hard, it's diffuse and contested | ~40% | 39 |
| **Idle or standby time** | 10% | 39 | Only with a standby clause; better to avoid by reassigning staff | ~50% | 20 |
| **Total** | | **390** | | **~65%** | **~253** |

**Recoverable: about 253 of 600 overrun hours (~42%).** The 210 vendor-caused hours are yours no matter what the contract says.

## The margin math

### Against the worst case (Scenario 1: fixed fee at the 1,000-hour estimate)

| | Per implementation | Annual (20 implementations) |
|---|---|---|
| Margin loss vs. T&M | $135K | **$2.7M** |
| Recovered via delay billing (253 hrs × $225) | $57K | **$1.14M** |
| Remaining loss | $78K | **$1.56M** |
| Theoretical ceiling (all 390 customer hours billed and collected) | $88K | $1.76M (65%) |

Delay billing helps, but it doesn't rescue a fixed fee priced at optimistic estimates. The vendor-caused overruns and the uncollectable delay costs still leave about $1.5M of lost margin.

### A better design: lean price plus billable delays

Delay billing is most useful when it lets you **price lower and more transparently**. Set the fixed fee at the realistic estimate plus a buffer for *your own* overruns, and route customer delays through change orders:

- Fixed fee: 1,200 hours × $225 = **$270K** (estimate plus a vendor-side buffer)
- Delay billing recovered: **~$57K**
- Revenue: **$327K**. Cost at 1,600 hours: **$240K**. Margin: **$87K**
- Margin change vs. T&M: **about –$0.66M per year**

That's roughly the same margin as Scenario 2 (realistic price at 1,400 hours), with three advantages:
- **A lower headline price** ($270K vs. $315K), which helps win deals.
- **Honest pricing:** carriers that deliver on time pay less than carriers that don't.
- **An incentive for the carrier** to staff its side of the project.

### The behavioral effect

Once delays cost carriers money, many will escalate internally and put people on the project. Suppose customer-caused hours drop 30% (390 → 273):

- Delay billing revenue falls, because there's less to bill: about $40K recovered instead of $57K.
- Delivery cost falls too: about 1,483 hours instead of 1,600, or $222K.
- **Margin stays about the same (~$88K)**, but go-live is weeks earlier and about 117 hours of delivery capacity are freed per implementation.

So the clause is roughly margin-neutral once behavior changes. The gains show up as retention, capacity, and time-to-value. If you have a backlog of signed customers waiting to start, those freed hours are worth more than the billed hours, because each blocked week is a week your team can't start the next implementation.

## The churn risk of billing delays

A delay invoice goes to exactly the carriers most at risk of churning: the ones whose implementations are stuck. A carrier billed for "its" delays that still hasn't reached value is a strong candidate to leave. If the invoice saves $15K of services margin and costs $220K of ARR, it was a bad trade.

Ways to get the deterrent without damaging relationships:
- **Prevent first.** Before the project starts, require a readiness gate: named IT resources, data extract samples, and access provisioned.
- **Pause rather than bill.** After X business days blocked, the project formally pauses and your team is reassigned. The carrier pays a re-mobilization fee and gets the next available start slot. This avoids idle cost and makes the consequence obvious without a surprise invoice.
- **Escalate before invoicing.** Delays go to the carrier's executive sponsor first. The fee is the backstop, not the opening move.
- **Consider a prepaid delay allowance.** The carrier prepays a small buffer that's refunded if unused. This turns the penalty into a reward for staying on schedule.
- **Govern waivers.** Individual project managers shouldn't quietly waive fees. Waivers should be a joint services and customer success decision, tracked and reported as concessions. The churn risk score for the account should inform the call.

## Contract terms that make this enforceable

Delay billing only works if dependencies are defined before the project starts:
- **Customer dependencies with dates:** data extracts, environment access, integration endpoints, named resources and their time commitments.
- **Data specifications:** format, completeness, and quality thresholds. "Late" and "bad" need objective definitions.
- **Deemed acceptance:** deliverables are accepted if not rejected within, say, 10 business days.
- **Delay mechanics:** notice requirements, a standby rate, a re-mobilization fee, and schedule reset rules.
- **Revenue recognition:** delay fees and change orders are contract modifications or variable consideration. Have your controller define the treatment before the first contract.

## Verify the attribution first

"Most overruns come from the carrier's delays" is the claim everything here depends on. It's also the claim most likely to be inflated, because it usually comes from the team whose performance is being measured.

Many delays that look customer-caused start on the vendor side:
- Data templates or specifications sent late or unclear
- Requirements changes you accepted without a change order
- Poor sequencing that left the carrier's IT team waiting on you, then you waiting on them
- Underestimating how thin a regional carrier's IT staff is

**How to check:**
1. **Audit 10 recent implementations independently,** with someone outside services reconstructing the timeline from emails, tickets, and status reports. Tag each overrun block by root cause.
2. **Start logging delay causes when they happen,** with the carrier confirming at each status meeting. Attribution reconstructed after the fact is unreliable, and carriers won't pay invoices based on it.
3. **Look for patterns.** If the same delay (such as slow data extraction from legacy policy systems) happens on most projects, it isn't really a customer failure. It's a predictable feature of your market.

That last point matters strategically. If thin carrier IT teams cause delays on nearly every project, billing each carrier for it penalizes customers for being typical regional carriers. The better-return fix is to **remove the dependency**: vendor-managed data extraction, prebuilt connectors to common legacy systems, and data-cleansing tooling. That's the productization investment from earlier, and it removes the delays themselves rather than recovering their cost.

## Bottom line

| Approach | Margin recovered | Effect on time-to-value | Churn risk |
|---|---|---|---|
| Bill delays on a fixed fee priced at estimate | ~40% of the loss | Modest | Medium to high |
| Lean price plus billable delays, with pause and escalation mechanics | Margin roughly matches the realistic-price scenario | Meaningful: carriers staff up | Low to medium |
| Remove recurring carrier dependencies through tooling | Prevents most delay hours from occurring | Largest | Lowest |

Use billable delays as the contractual backstop and pricing tool. Use the pause clause and readiness gates as the main behavior lever. Invest in removing the recurring delays, because that's what both recovers margin and gets carriers live fast enough to renew.

## Turn 4

**User:** If we offered vendor-managed data extraction and cleansing as a paid add-on instead of absorbing it or billing delays, would that earn more margin than delay billing, and would thin-IT carriers actually pay for it?

**Assistant:**

# Vendor-Managed Data Extraction as a Paid Add-On

## Short answer

**On margin:** a paid add-on beats delay billing only if you can deliver it repeatably. That means tooling or connectors for the legacy systems your carriers commonly run, and ideally a lower-cost data team.
- **Without tooling:** the add-on earns about the same margin as delay billing, uses more of your delivery capacity, and carries more risk.
- **With tooling:** it earns roughly **50–60% more margin per buyer** than delay billing. It also shortens go-live, which is worth far more than the services margin.

**On willingness to pay:** thin-IT carriers are the natural buyers, because IT capacity is exactly what they lack. But they'll only pay under certain conditions:
- It's sold **at deal time, inside the original budget**, not after signing.
- It's priced against their real alternative: consultants, delay, and paying your subscription while getting no value from it.
- It's tiered, so small carriers with simple data aren't overcharged.

Many carriers already pay consultants for this work. You can check that in your own deal history, and you can test the price in your next 10–15 proposals before investing heavily.

## Why an add-on can outperform delay billing

| | Delay billing | Paid add-on |
|---|---|---|
| When revenue is agreed | After the fact, often disputed | Up front, in the contract |
| Collection risk | High; often waived to protect the account | Low; it's a planned line item |
| Who controls the work | Carrier (you wait on them) | You (you control the schedule) |
| Effect on overruns | Recovers some of their cost | Removes most of them |
| Relationship effect | Adversarial, and lands on at-risk accounts | Carrier bought help, and gets it |
| Time-to-value | Modest improvement | Large improvement |
| Delivery capacity | Uses no extra hours | Uses additional hours |

The last row is the tradeoff. An add-on replaces wasted waiting hours with productive paid hours. If your team is already capacity-constrained, those hours have to come from somewhere, either new hires or a separate data team.

## Per-implementation margin comparison

Illustrative figures, continuing the earlier model. **Replace them with your actuals.**

**Assumptions:**
- About 254 data-related overrun hours per implementation today: rework from late or bad data, plus the data-driven share of re-mobilization and project management time.
- Delivery cost is $150/hour and the bill rate is $225/hour.
- Add-on price: **$75K**, set against the carrier's alternatives:
  - Internal IT they don't have.
  - Consultants at roughly $75–100K.
  - Delay, which extends dual-running and legacy maintenance costs and wastes subscription fees if billing started at signing.
- **Without tooling:** the add-on requires about 400 delivery hours.
- **With tooling:** about 250 hours, using connectors and cleansing scripts for common legacy systems.
- Once you control the data work, the add-on removes about 70% of data-related overrun.

All options are compared against the **absorb baseline**: a fixed fee where you eat the data overrun.

| | Absorb | Delay billing | Add-on, no tooling | Add-on, with tooling |
|---|---|---|---|---|
| Data-related revenue | $0 | $40K (~179 billable hrs) | $75K | $75K |
| Add-on delivery cost | — | — | –$60K | –$37.5K |
| Data overrun cost | –$38K | –$38K | –$11.4K | –$11.4K |
| **Net data margin** | **–$38K** | **+$2K** | **+$3.6K** | **+$26.1K** |
| **Improvement vs. absorb** | — | **+$40K** | **+$42K** | **+$64K** |
| Net extra delivery hours | 0 | 0 | ~+224 | ~+74 |

**What the table shows:**
- Without tooling, the add-on and delay billing earn about the same margin. The add-on uses more capacity, but it's easier to collect and speeds go-live.
- With tooling, the add-on earns about **$24K more per buyer** than delay billing.
- Staffing the add-on with a lower-cost data team (offshore or nearshore data engineers at about $90/hour instead of $150) adds roughly another $15K per implementation.

## Annual economics and the tooling investment

Not every carrier will buy it. Carriers who decline keep the delay-billing clause, which becomes more defensible because they *chose* to own their data work.

| | 30% attach | 50% attach | 70% attach |
|---|---|---|---|
| Buyers per year (of 20) | 6 | 10 | 14 |
| Extra margin vs. delay billing alone (with tooling) | $0.14M | $0.24M | $0.34M |
| Add-on revenue | $0.45M | $0.75M | $1.05M |

**Tooling investment:**
- Build connectors and cleansing pipelines for the 3–4 legacy source systems most common among your carriers: about **$0.6–0.8M up front** (3–4 engineers for 9–12 months), plus about **$0.2M per year** to maintain.
- **Payback on services margin alone: roughly 3–4 years at 50% attach.** That's not compelling by itself.

**Adding retention changes the case.**
- Data is usually the longest item on an implementation's critical path. Removing it can cut go-live by two to three months and produces more complete migrations.
- Suppose buyers' first-renewal churn falls 10 points. On 10 buyers × $220K ACV, that's about $0.86M of lifetime gross profit per annual cohort. This uses the same lifetime assumptions as before.
- On that basis, the tooling pays back within about two cohorts once renewals arrive.

The tooling is also the same investment recommended earlier as the productization fix. The add-on gives it a revenue line, so it isn't purely a cost.

## Will thin-IT carriers actually pay?

### Reasons they will

- **They already pay for it in some form.** Regional carriers commonly hire consultants for migrations, or pull IT staff off other priorities. Check your last 30 deals for how often a third party did the data work. That's evidence of willingness to pay.
- **Their alternative is expensive and visible.** Each month of delay means:
  - Running two systems in parallel
  - Legacy maintenance fees they hoped to stop paying
  - Claims staff working in the old system
  - Your subscription fees with no value, if billing starts at signing

  At $220K ACV, that last item alone is about $18K per month. A two-to-three-month acceleration covers most of a $75K add-on.
- **Claims leaders own the business case, and they care about go-live.** The IT team may be the constraint, but the budget holder is often the claims executive who wants the project finished.

### Reasons they won't

- **Budgets are fixed at purchase.** An add-on offered after signing competes for money that doesn't exist. **Sell it in the original proposal**, ideally as a default line item the carrier can opt out of.
- **"Shouldn't this be included?"** Procurement may see it as padding. Frame it as a choice: the carrier can own extraction (with clear data specifications and delay terms), or you can own it at a fixed price.
- **Price sensitivity at the small end.** A $75K add-on on a $120K ACV deal is a hard sell. Tier the price by source-system complexity and data volume, not one flat fee.
- **Data security and access concerns.** Claims data includes personal information, and sometimes medical information in workers' comp and bodily injury lines. Some carriers restrict vendor access to source systems. For them, offer a split model: they run your extraction tool, and you do the cleansing and validation.

## Packaging and pricing

Offer three options in every proposal:

| Option | Carrier does | You do | Commercial terms |
|---|---|---|---|
| **Standard** | Extraction and cleansing to your data specification | Load and validate | Included; delay clause applies |
| **Assisted** | Runs your extraction tool | Cleansing, mapping, validation | Mid-tier fixed price |
| **Managed** | Grants access, approves results | Full extraction, cleansing, reconciliation | Top-tier fixed price, tiered by source system |

**Design rules:**
- **Price after a data assessment.** Include a short paid data assessment in discovery, then quote a fixed price. Homegrown or undocumented source systems go to a higher tier or to time-and-materials.
- **Define acceptance.** Set reconciliation thresholds for record counts, financial totals, and open reserves. The carrier signs off. Claims history and reserve data errors have financial and regulatory consequences, so cap your liability and make the carrier's approval explicit.
- **Set exclusions:** data that doesn't exist, history beyond a set number of years, and third-party systems you can't access.
- **Restrict discounting.** The biggest risk is sales giving it away to close deals. That puts you back to absorbing the cost under a different name. Require finance approval for any add-on discount above a set threshold.

## Risks

1. **Adverse selection.** Carriers with the worst data are the most eager buyers. The data assessment and tiered pricing are your protection.
2. **Source-system variety.** Tooling only pays off if your carriers cluster on a few legacy platforms. Before building, check source systems across your last 40 implementations. If fewer than about 60% run on 3–4 platforms, the tooling payback weakens considerably.
3. **Security and compliance costs.** Taking on data handling expands your security and audit scope, increases carrier vendor-risk reviews, and may affect your cyber insurance. Budget for it.
4. **Capacity and hiring.** Data engineers are a different skill set from implementation consultants. Hiring slowly can make the add-on the new bottleneck.
5. **Liability for data errors.** A mis-migrated reserve or payment history can surface in a regulatory exam or financial audit. Acceptance sign-off and liability caps matter here.

## Test before building

**Phase 1: Price test (next 10–15 proposals, minimal investment)**
- Include all three options in every proposal. Deliver Managed with existing staff even if margins are thin.
- Track:
  - Attach rate by carrier size
  - Discount pressure on the add-on
  - Win rate compared with recent proposals
  - Go-live time for buyers vs. non-buyers

**Phase 2: Build tooling (only if the test passes)**
- Go-ahead criteria:
  - Attach rate of at least 35% at a price of at least $60K
  - Win rate unchanged
  - Source systems concentrated enough to justify connectors
- Build connectors for the top platforms first.

**Kill criteria:**
- Attach rate below 25%, or
- More than half of sold add-ons discounted over 30%, or
- Managed-tier delivery running more than 20% over quoted hours after the first 4–5 projects.

If any of these hit, fall back to Standard with delay terms, and put the tooling budget into readiness gates and data specifications instead.

## How this connects to your VP debate

Data extraction and cleansing is where your two VPs' strategies meet:

- **For new customers,** it's the fastest path to go-live, which is the services thesis.
- **For the installed base,** many existing carriers probably have incomplete migrations: history not loaded, fields unmapped, poor-quality data. A **data remediation offering** for current customers is a retention play for at-risk accounts.
- **For the product roadmap,** analytics and AI features only work on clean, complete data. Remediated accounts are the ones that can actually adopt and pay for the analytics and AI modules. This is the product thesis, made viable.
- **For recurring revenue,** consider a **managed data quality service**: ongoing feeds, reconciliation, and monitoring for carriers that lack the staff to do it themselves. It turns a one-time services fee into subscription revenue.

Of all the options discussed so far, this may be the only one that improves services margin, time-to-value, retention, and adoption of new features at the same time. It depends on two facts you can check in about a month: how concentrated your carriers' source systems are, and whether carriers accept the price in the proposal test.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

## The recommendation

**Don't pick a VP. Spend six weeks finding out where the churn actually comes from. Meanwhile, start the no-regret moves that pay off whichever VP is right. Then release larger investments in tranches, tied to evidence.**

Across everything we've worked through, the pattern is consistent:
- The fastest and most certain money is protecting renewals already at risk.
- The best return on new capital is anything that gets carriers live faster and more completely: realistic fixed-fee pricing, readiness gates, and data tooling.
- The largest and slowest bet, competitive AI and analytics, should wait until the data shows it's the real driver. Even then, partner or embed first and price it as an add-on.

## The plan

### Weeks 0–6: Diagnose and stop the bleeding (~$0.3M)

| Action | Owner | Output |
|---|---|---|
| Churn diagnostic: win/loss, cohort churn by implementation duration, adoption of churned accounts, M&A share | Neutral analyst reporting to you and the CFO | Split of lost ARR across implementation-driven, competitive, and structural causes |
| Score every renewal in the next 18 months | You (CS) | Ranked at-risk ARR list |
| Pull the five numbers: estimated vs. actual hours, write-offs, first-renewal churn by implementation duration, billing start trigger, contract term length | Services + Finance | Real inputs to replace my illustrative model |
| Independent audit of 10 implementations to tag delay root causes | Someone outside Services | True customer-caused vs. vendor-caused split |
| Check legacy source systems across the last 40 implementations | Services + Product | Whether data tooling is viable |

**Also start now, since it's no-regret:** stand up a rescue team for the at-risk renewals with the most ARR. Finish stalled integrations and get modules live. Cap free-services concessions, with any waivers approved jointly by you and Finance.

### Months 2–6: Fix the commercial model and run pilots (~$1–1.5M)

1. **Fixed-fee pilot on the next 5–8 new implementations.**
   - Paid discovery phase first.
   - Price at realistic historical hours plus a buffer for your own overruns.
   - Customer dependencies, readiness gates, and a pause-and-re-mobilize clause written into the SOW.
   - Final milestone tied to adoption, not just go-live.
2. **Three-option data offer (Standard, Assisted, Managed) in the next 10–15 proposals.** Deliver the Managed tier with existing staff. Track attach rate, discount pressure, and win rate.
3. **Rescue program continues** through the next two quarters of renewals.
4. **Product team:** reassign a small squad to time-to-value work: implementation templates, out-of-the-box dashboards, and scoping for the top source-system connectors. Hold competitive feature expansion until Gate 1.

### Gate 1 (around month 6): Decide the big money

Use the diagnostic results and the pilot data to route the next tranche:

| If the diagnostic shows... | Then... |
|---|---|
| **Churn is mostly implementation- and adoption-driven** (most likely) | Fund data tooling (~$0.6–0.8M) and the time-to-value squad (~$2M/yr). Roll fixed-fee pricing out to all new business. Launch data remediation for the installed base. |
| **Churn is mostly competitive, from fully adopted accounts** | Fund the 1–2 capabilities that drive displacement. Partner or embed first, price as add-ons, and require adoption kill criteria. Keep the services fixes smaller. |
| **Churn is mostly carrier M&A** | Neither proposal fixes it. Focus on change-of-control terms, multi-entity pricing, and selling to acquiring parents. |
| **Mixed** | Allocate budget in proportion to the ARR in each bucket, with a gate on each tranche. |

### Months 6–18: Scale what worked

- Build connectors for the top legacy platforms, if source systems are concentrated and the attach rate is at least 35%.
- Offer data remediation to installed-base accounts with incomplete migrations. These accounts become the first candidates for analytics and AI modules. That makes the Product VP's roadmap depend on this work rather than compete with it.
- Consider a recurring managed data quality service for carriers without the staff to maintain their data.
- Revisit competitive AI and analytics once you have a base of clean, fully adopted accounts to sell into.

**Budget shape:** about $1.5M committed in year one. Another ~$2–2.5M is released only if Gate 1 is met. That's less capital at risk than either VP's proposal, with the fastest returns funded first.

## Governance

- **One executive owns GRR and NRR.** That should be you, or a Chief Customer Officer, with the CEO as sponsor. Both VPs are measured on it.
- **The CFO holds the funding gates.** The kill criteria are agreed now, before anyone spends.
- **Change Services compensation** from services margin to **cohort contribution** (services margin plus subscription gross profit through first renewal). Otherwise fixed-fee pricing will be resisted, because it makes the services P&L look worse while helping the company.
- **Product owns time-to-value engineering outcomes:** days to go-live, adoption, and connector coverage. It's measured on adoption, not features shipped.
- **Leading indicators, reviewed monthly:**
  - Health of at-risk renewals
  - Days to go-live, defined by adoption
  - Actual vs. quoted hours
  - Add-on attach rate and discounting
  - 90-day adoption

## Kill criteria

- **Fixed-fee pilot:** more than 15% over quoted hours after 3–4 projects → pause and fix scoping.
- **Data add-on:** attach below 25%, most deals discounted over 30%, or Managed delivery more than 20% over → fall back to Standard with delay terms.
- **Any competitive feature:** adoption among target accounts below 30% two quarters after launch → stop expanding the team.
- **Rescue program:** saved ARR under 2× program cost after two quarters → narrow it to the top-tier accounts.

## What not to do

- **Don't approve the full roadmap acceleration now.** It's the slowest payback and most exposed to non-adoption. It depends on implementation quality you don't yet have.
- **Don't switch to fixed-fee at your old estimates.** That's the scenario that loses about $2.7M a year of margin.
- **Don't lead with delay invoices** on at-risk accounts. Use the pause clause and escalation first.
- **Don't let sales give away the data add-on.** A free add-on means you're absorbing the cost under a new name.

## How to frame it for your leadership team

Say to both VPs: **"You're both partly right, and we're going to find out how much in six weeks. Meanwhile, we're doing the things that pay off either way."**

- The Services VP gets fixed-fee pricing, readiness gates, and the data offer, but is now measured on retention, not services margin.
- The Product VP gets time-to-value engineering now, and a funded path to competitive features, gated on evidence. The installed-base data remediation turns their analytics and AI into something customers can adopt.

For the CEO and CFO: a gated plan with about $1.5M committed, clear kill criteria, the fastest returns funded first, and one person accountable for the churn number.

**Monday:** commission the diagnostic, pull the renewal list, and ask Finance how implementations are billed. Those three things will tell you most of what you need.

## Outcome summary (sent to Jev)

The assistant recommends not choosing between the two VPs. Instead, spend six weeks diagnosing where churn actually comes from, start no-regret moves that pay off either way, and release larger investments in tranches tied to evidence. The fastest, most certain money is protecting renewals already at risk. The best return on new capital is getting carriers live faster and more completely. Competitive AI and analytics is the slowest, most adoption-exposed bet, so it should wait for proof.

**Weeks 0–6 (about $0.3M):**
- A neutral analyst splits lost ARR into implementation-driven, competitive, and M&A causes.
- Every renewal in the next 18 months is scored for risk.
- Finance and Services pull actual versus estimated hours, write-offs, churn by implementation duration, billing triggers, and contract terms.
- Someone outside Services audits delay root causes.
- The team checks how concentrated carriers' legacy systems are.
- A rescue team starts work on high-value at-risk renewals, with free-services concessions capped.

**Months 2–6:**
- Pilot fixed-fee implementations at realistic historical hours, with paid discovery, readiness gates, a pause clause, and adoption-based final milestones.
- Test a three-tier data extraction offer (Standard, Assisted, Managed) in upcoming proposals.
- Redirect a small product squad to time-to-value work.

**Around month 6:** A gate routes the next roughly $2–2.5M to data tooling, competitive capabilities (partnered and priced as add-ons), or M&A defenses, depending on what the diagnostic shows.

**Governance:**
- One executive owns gross and net revenue retention.
- The CFO holds funding gates, with kill criteria agreed in advance.
- Services is paid on cohort contribution rather than services margin.

**Caveats:**
- The figures are illustrative.
- Fixed-fee pricing at old estimates would lose about $2.7M a year.
- Delay invoices shouldn't lead on at-risk accounts.
- Sales must not give away the data add-on.
