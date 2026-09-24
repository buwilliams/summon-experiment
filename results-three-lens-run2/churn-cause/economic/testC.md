# churn-cause/economic/testC

Model: claude-opus-5-5 · 2026-09-24T15:31:04.011386+00:00

## Turn 1

**User:** Use profit maximization to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Which Churn Explanation Is Right? A Profit-Maximization Approach

## The short answer

Neither belief can be confirmed from the information given. Both VPs are describing a plausible mechanism, and each happens to recommend investing in their own function. A profit-maximizing approach replaces "who's right?" with a different question: **which dollar of investment recovers the most lifetime gross profit, soonest?**

That question can be answered with data you probably already have, in about 4–6 weeks. There is also a structural reason to fix the service side first while you gather evidence, explained below.

## Step 1: Frame the decision in profit terms

For each option (roadmap acceleration vs. onboarding/service overhaul), estimate:

**Expected profit recovered =** (Churned ARR attributable to that cause) × (probability the fix actually prevents it) × (gross margin) × (expected remaining customer lifetime) − (cost of the fix), discounted for how long the fix takes to land.

An illustration with made-up numbers: suppose you have $50M ARR and churn went from 8% to 16%. That's roughly $4M of additional ARR lost per year. At 75% gross margin and a 6-year average lifetime, each year of excess churn destroys about $18M in lifetime gross profit. That is the size of the prize, and it sets the budget ceiling for either fix.

Four implications fall out of this framing:

- **Attribution drives everything.** If 70% of excess churn traces to failed implementations, even a brilliant AI roadmap can recover at most 30% of the problem.
- **Time-to-impact matters.** Service fixes such as implementation playbooks, staffing, and rescue teams for at-risk accounts typically land in one or two quarters. Major AI and analytics features often take a year or more to ship and then must be adopted. Delay costs you churned renewals in the meantime.
- **Not all churn is equally costly.** If churned customers were small, heavily customized, and support-intensive, some of that churn may have raised profit. Measure lost gross profit, not just lost logos or ARR.
- **Features also affect new sales; service mostly affects retention.** If product gaps are also hurting win rates, the roadmap's profit case includes acquisition, not just churn. Check this before dismissing it.

## Step 2: Test the hypotheses against what each one predicts

Each hypothesis leaves a different fingerprint in your data.

| Evidence | Points to **product gaps** | Points to **implementation/service** |
|---|---|---|
| **Who churns** | Well-implemented, high-adoption customers | Customers with long implementations, low module adoption, or partial rollouts |
| **When they churn** | At renewal after years of healthy use | First or second renewal, often before full go-live value |
| **Where they go** | To specific competitors with stronger AI/analytics | Anywhere, including cheaper tools, in-house, or "no decision" |
| **Timing of the spike** | Coincides with competitor AI launches | Coincides with services changes: staff turnover, cuts, new methodology, backlog growth |
| **Support data** | Feature requests dominate tickets and QBRs | Rising ticket volume, slow resolution, escalations, low CSAT on implementation |
| **Sales data** | Win rates falling, AI cited in losses | Win rates stable (you still sell well but fail to deliver) |
| **Healthy accounts** | Even happy, adopted customers ask for AI in renewal talks | Adopted customers renew fine |

**The single most important cut:** plot churn rate against implementation duration and adoption depth.

- If churn is heavily concentrated among customers who never reached full adoption, the services hypothesis is largely confirmed.
- If fully adopted customers are churning at the same elevated rate, product gaps are real.

## Step 3: Check the explanations neither VP raised

Regional insurance carriers are a consolidating market. Before investing, rule out:

- **M&A.** Acquired carriers often migrate to the acquirer's system. No product or service fix prevents this, though it affects how you target and forecast.
- **Price and budget pressure.** Carriers facing loss-ratio pressure cut vendor spend.
- **Sponsor turnover.** Your champion left, and the new claims VP brought a preferred vendor.
- **A pricing or packaging change** made in the last 18 months.

Any churn explained by these factors should be removed from the attribution before you size either fix.

## Step 4: A caution on stated reasons

Exit interviews will likely over-report "missing features." It's the easiest, least confrontational reason for a departing customer to give, and it is often what the competitor pitched them on. Weight behavioral data (adoption, timing, destination) more heavily than stated reasons.

## Step 5: What to do now, while the diagnosis runs

**1. Start low-cost service fixes immediately.** Stand up a rescue program for accounts at risk of non-renewal that are stuck in implementation or show low adoption. This is cheap, fast, and protects near-term renewals regardless of which hypothesis wins. It also doubles as an experiment: if rescued accounts renew at markedly higher rates, you've measured the service effect directly.

**2. Don't make major new roadmap commitments until attribution is done.** Keep the existing roadmap moving, but hold significant acceleration spending until you know what share of churn it could plausibly recover.

**3. Recognize the dependency between the two.** In claims management, analytics and AI features depend on clean, complete data flowing through a fully implemented system. A customer who never got to full value can't benefit from better analytics. This means service fixes are often a prerequisite for feature investments to pay off, not a competing alternative. It's the main reason to lean toward fixing delivery first unless the data clearly contradicts it.

**4. Then allocate by marginal return.**

- **If churn is concentrated in poorly implemented accounts:** fund implementation redesign, services capacity, and time-to-value metrics. Consider tying part of the Services VP's goals to 12-month adoption, not just go-live.
- **If fully adopted customers are leaving for AI-strong competitors and win rates are falling:** the roadmap case is strong. Prioritize the specific features cited in losses, not a broad AI push.
- **If it's mixed, as it often is:** fund service fixes first because they are faster and cheaper and enable feature adoption. Then target roadmap spending at the gaps that drive losses among healthy accounts.

## Step 6: Align incentives

Each VP's hypothesis matches their budget interest. That doesn't make either wrong, but it's why the answer should come from a shared analysis with agreed-upon metrics rather than competing narratives. Consider having both VPs sign off on the attribution methodology before the data comes back.

## Bottom line

Neither belief can be declared right yet. Run a fast attribution analysis, anchored on churn versus implementation depth and on where churned customers went. Start the cheap service rescue work now, because it protects revenue and generates evidence. Then direct the larger investment wherever the attributed churn, recovery probability, speed, and margin produce the highest expected profit. If "customers never get to full value" turns out to be true, fix that first, because features customers can't reach won't retain them.

## Turn 2

**User:** Sticking with profit maximization, how should I weigh the risk that product gaps are also hurting our win rates on new deals?

**Assistant:**

# Weighing Win-Rate Risk in the Profit Calculation

## The short answer

Add the win-rate effect to the roadmap's side of the ledger, but value each new deal at its **realistic lifetime profit given your current churn**, not at a healthy-company LTV. That adjustment matters because the two problems interact: product gaps reduce how many deals you win, and service problems reduce how much each win is worth. Weighed properly, the win-rate risk usually argues for starting targeted product work sooner. It rarely argues for skipping the service fix.

## Step 1: Size the acquisition effect

**Annual profit at risk from product gaps in sales =** (Qualified pipeline per year) × (Win-rate decline attributable to product gaps) × (Average new ARR per deal) × (Gross margin) × (Expected customer lifetime)

An illustration with made-up numbers:

- 60 qualified opportunities per year, average $400K ARR
- Win rate fell from 30% to 22%, and win/loss analysis attributes 5 of those 8 points to analytics/AI gaps
- That's 3 lost deals per year, or $1.2M of new ARR
- At 75% margin and a 6-year lifetime, that's about **$5.4M in lifetime gross profit per year of lost deals**

Compare this with the roughly $18M per year of excess churn from the earlier example. The acquisition effect is meaningful but smaller. The ratio will differ for your business, and that ratio is what you need to know.

## Step 2: Adjust each new deal's value for the churn you actually have

A new customer is worth its full LTV only if it stays. If you win deals and then put customers through the same long implementation that drives churn today, their expected lifetime is shorter than your historical average.

- At 8% annual churn, expected lifetime is roughly 12 years.
- At 16%, it's roughly 6 years.

**Doubling churn roughly halves the value of every deal you win.** This has two consequences:

1. The win-rate loss from product gaps is worth less than it looks while delivery remains broken.
2. The service fix raises the value of all future wins, not just retained customers. Credit it with that.

This is the core interaction: feature investment brings more customers into the funnel, and service investment determines whether they stay long enough to be profitable. Fixing only acquisition fills a leaky bucket faster.

## Step 3: Account for the long-lived nature of lost deals

Two features of your market make a lost deal more costly than a simple annual calculation suggests:

- **Long replacement cycles.** Carriers replace claims systems infrequently, often every 7 to 10 years or longer. A deal lost today may not come back to market for a decade.
- **A shrinking customer base.** Consolidation among regional carriers means fewer prospects over time, so each replacement opportunity carries more weight.

Treat each competitive loss as losing the account for a full replacement cycle. If product gaps are genuinely costing you deals, this pushes the value of fixing them up.

## Step 4: Verify the win-rate problem is real and product-driven

Sales teams, like both of your VPs, have a natural explanation that points away from themselves. "The product lacks AI" is an easy loss reason to record. Before crediting the roadmap, check:

| Evidence | Suggests product gaps are costing deals | Suggests something else |
|---|---|---|
| **Stage of loss** | Lost at shortlist or after technical demos | Lost at pricing, legal, or late-stage references |
| **Who wins** | The same AI-strong competitors repeatedly | Scattered winners, or "no decision" |
| **Buyer interviews** | Prospects (not your reps) cite analytics or AI | Prospects cite price, implementation risk, or references |
| **References** | Not a major factor | Prospects hear about long implementations from your customers |
| **Trend timing** | Decline tracks competitor launches | Decline tracks rising churn or reputation damage |

That last pair matters because **service problems can also hurt win rates.** Insurance carriers check references carefully, and a reputation for painful implementations costs deals even when the product is competitive. If losses cluster at the reference stage, part of the win-rate decline belongs on the service side of the ledger.

Use independent win/loss interviews with prospects wherever possible. They are far more reliable than CRM loss codes.

## Step 5: Distinguish table stakes from differentiators

Not all product gaps are equal in profit terms:

- **Table-stakes gaps** knock you out of RFPs or off shortlists. Each one can cost you entire deals, so closing them has high returns. Sometimes they can be closed more cheaply than a full build, through partnerships, integrations with analytics vendors, or a narrower first release that meets the requirement.
- **Differentiator gaps** make a competitor more attractive but don't disqualify you. Their effect on win rates is smaller and less certain. These are where it's easiest to overinvest.

Ask win/loss research specifically whether you were eliminated for a missing capability or merely outcompeted on it.

## Step 6: Handle the uncertainty with staged bets

Because the roadmap has a long lead time, waiting for perfect evidence carries its own cost. Treat product investment as a set of staged options rather than a single commitment:

1. **Now:** Fund discovery and small builds aimed at confirmed table-stakes gaps. This preserves the option to accelerate without committing the full budget.
2. **After win/loss data arrives (roughly one or two quarters):** Scale investment if the data shows real product-driven losses at the shortlist stage.
3. **Throughout:** Keep the service fix funded, because it raises the value of every deal the roadmap eventually wins.

## Decision rules

- **If product gaps cost you deals at the shortlist stage and the losses are large relative to excess churn:** accelerate targeted roadmap work in parallel with the service fix, not after it.
- **If losses cluster at references or pricing:** the win-rate problem is largely a service or pricing problem, and the roadmap case weakens.
- **If losses are real but modest:** fix delivery first, close only table-stakes gaps, and revisit in two quarters.

## Bottom line

Win-rate risk belongs in the calculation, and in a market with long replacement cycles and shrinking prospect counts, each lost deal is expensive. But value those deals at your current, churn-reduced lifetime. Check whether losses are product-driven or reputation-driven, and focus on gaps that get you eliminated rather than merely outcompeted. In most scenarios the profit-maximizing answer is to run both in parallel: fix delivery at full speed, and make staged, targeted product bets whose size grows as the win/loss evidence comes in.

## Turn 3

**User:** Keeping with profit maximization, how much should I be willing to spend on the rescue program for at-risk accounts before the attribution data comes back?

**Assistant:**

# Sizing the Rescue Budget Before Attribution Data Arrives

## The short answer

Spend up to the point where the **expected gross profit saved** (plus the value of what you learn) equals the **full cost** of the program, including staff time, concessions, and opportunity cost. Because you don't yet know how effective rescue will be, size the budget using a conservative estimate of its impact, target accounts by expected value, and release more funding at checkpoints as evidence comes in. Under reasonable assumptions, this usually supports a meaningful but bounded budget, well short of the total ARR at risk.

## Step 1: Estimate the expected value of rescuing one account

**Expected value per account =** ARR × (Reduction in churn probability from rescue) × Gross margin × (Discounted expected remaining lifetime)

The critical input is the **reduction in churn probability**, not the churn probability itself. Rescue is worth only the renewals it changes. Accounts that would have renewed anyway, or that will leave regardless, generate little value.

An illustration with made-up numbers:

- Average at-risk account: $400K ARR
- Baseline churn probability without intervention: 40%
- Rescue reduces churn probability by **10 points** (conservative) to **25 points** (optimistic)
- Gross margin: 75%
- Discounted expected remaining lifetime if retained: about 4 years (a 6-year lifetime at current churn, discounted to present value)

| Scenario | Expected ARR saved per account | Expected lifetime gross profit per account |
|---|---|---|
| Conservative (10-pt reduction) | $40K per year | about $120K |
| Optimistic (25-pt reduction) | $100K per year | about $300K |

That gives a break-even spend of roughly **$120K to $300K per account**. Before you have evidence, anchor on the conservative end.

## Step 2: Count the full cost, not just the obvious spend

Rescue costs are easy to undercount. Include:

- **Direct costs:** dedicated staff, contractors, travel, executive time.
- **Concessions:** discounts, free services, or credits. A renewal discount reduces ARR for the rest of the customer's lifetime, not just one year, so value it that way.
- **Opportunity cost:** if you pull your best implementation staff onto rescue work, new implementations may slow down and produce the next wave of at-risk accounts. Price staff time at what it would earn elsewhere, not just at salary.

The opportunity cost matters most for you because your constraint is likely the same implementation capacity that caused the problem. If rescue work starves new implementations, you shift churn into future cohorts rather than preventing it.

## Step 3: Target accounts by expected value, not by size or noise

Rank at-risk accounts by the expected profit a rescue could recover. The best candidates are those where intervention can change the outcome:

| Account type | Rescue priority | Reason |
|---|---|---|
| Stuck in implementation, engaged sponsor, renewal in 2–3 quarters | **High** | Fixable problem, time to act, someone to work with |
| Low adoption but no stated intent to leave | **High to medium** | Early intervention is cheap and churn risk is rising |
| Already signed with a competitor or migrating after an acquisition | **Low** | Rescue is unlikely to change the outcome |
| Healthy, fully adopted | **Low** | Would likely renew without intervention |
| Small ARR, heavy customization, high support cost | **Low or case-by-case** | Rescue may cost more than the account's margin |

Concentrating spending on the high-priority group raises the average reduction in churn probability and makes the conservative estimate more likely to be exceeded.

## Step 4: Set the initial budget with a margin of safety

A practical rule: before evidence arrives, **budget up to about half of the conservative break-even value per targeted account.** Using the example numbers:

- Conservative break-even: about $120K per account
- Initial budget ceiling: about $60K per account
- For 20 targeted accounts: roughly **$1.2M total**, including costs of staff time and concessions

The margin of safety covers the chance that your estimate of rescue effectiveness is too high. If early results show the optimistic case is closer to reality, the break-even point rises and you can expand spending.

Adjust the numbers to your own ARR, margins, and churn rates. The structure matters more than these specific figures.

## Step 5: Add the value of the information you'll gain

Rescue also produces evidence for the larger decision between roadmap and service investment. If rescued accounts renew at much higher rates than similar accounts have historically, you have direct proof that the service hypothesis holds. That evidence could steer millions of dollars of later investment, so it has real value on top of the saved renewals.

To get usable evidence without giving up saves:

- **Avoid a strict holdout of at-risk accounts** if you can. Deliberately not helping four accounts in the example would cost about $480K in expected profit at the conservative estimate.
- **Use a staggered start instead.** Begin rescue with the accounts that renew soonest and compare early leading indicators against accounts that haven't started yet.
- **Compare against historical cohorts.** Match rescued accounts to similar past accounts (same implementation length, adoption level, and size) and compare renewal rates.
- **Track leading indicators.** Renewals take months to arrive, so measure go-live progress, adoption depth, sponsor engagement, and support escalations along the way.

## Step 6: Release funding at checkpoints

Treat the budget as staged rather than committed all at once:

- **Around 60 days:** Are leading indicators improving in rescued accounts compared with the matched baseline? If yes, keep going. If there's no movement, reassess whether the problem is actually service-related.
- **Around 90–120 days:** Are early renewal outcomes and stated renewal intent better than the baseline? If so, raise the per-account ceiling toward the optimistic break-even value and consider adding accounts.
- **When attribution data arrives:** Resize the program based on what share of churn traces to service failures and on the measured effectiveness of rescue.

## Decision rules

- **If early indicators improve clearly:** Expand funding toward the optimistic break-even point and extend rescue to medium-priority accounts.
- **If indicators are mixed:** Hold at the initial budget, narrow to the highest-priority accounts, and wait for attribution data.
- **If nothing moves after 60–90 days:** Scale back. Either the churn isn't primarily service-driven or the rescue approach isn't working, and both findings are valuable.
- **At every stage:** If rescue work is visibly slowing new implementations, cap it or add capacity, because otherwise you're creating future churn.

## Bottom line

Your willingness to spend should be set by the expected gross profit each rescue actually saves, discounted and measured at a conservative estimate of effectiveness, plus the value of what the program teaches you about the root cause. Target accounts where intervention can change the outcome, count concessions and diverted implementation capacity as real costs, and start with a budget of roughly half the conservative break-even value per account. Then increase or cut funding at 60- and 90-day checkpoints as evidence comes in.

## Turn 4

**User:** Still using profit maximization, should I hire more implementation staff now to protect new implementations from being slowed by the rescue work, or wait until the checkpoints?

**Assistant:**

# Hire Implementation Staff Now or Wait for the Checkpoints?

## The short answer

**Hire a portion now, cover the rest with flexible capacity, and make the remaining hires contingent on the checkpoints.** Two facts drive this. First, hiring lag and ramp time mean that capacity you decide to add at the 90-day checkpoint won't be productive for another six months or more. Second, much of the added capacity pays off whichever hypothesis wins, because new implementations must be delivered regardless. That makes part of the hire a no-regret move, while the portion sized to the rescue program still depends on evidence you don't yet have.

## Step 1: Confirm the constraint actually binds

Before hiring, check whether rescue work will really slow new implementations:

- **Who does rescue work?** If it's mostly CSMs, account executives, and executive sponsors, implementation capacity may not be affected much. If it requires your senior implementation consultants, it will be.
- **Current utilization and backlog.** If implementation staff are already fully booked and projects are waiting, any diversion delays go-lives immediately.
- **Upcoming new-implementation volume.** A heavy pipeline of signed deals starting in the next two quarters raises the cost of diversion.

If rescue draws mainly on non-implementation staff and the backlog is manageable, you can wait. The rest of this answer assumes the constraint binds, which is likely given that long implementations are already a known problem.

## Step 2: Compare the cost of waiting with the cost of hiring early

### The timing problem

Implementation staff for claims-management software typically take two to three months to hire and three to six months to become fully productive, since they need to learn your product, carrier workflows, and integrations. The timeline looks like this:

| Decision point | Hire starts | Fully productive |
|---|---|---|
| Hire now | Month 2–3 | Month 5–9 |
| Hire at 90-day checkpoint | Month 5–6 | Month 8–12 |

Waiting for the checkpoint pushes new capacity out by roughly three months, and new implementations absorb the shortfall throughout that period.

### Illustrative numbers

**Cost of waiting (slowed implementations):**

- 15 new implementations starting over the next 12 months, averaging $400K ARR
- Rescue diverts senior staff enough to add about two months to each implementation
- Suppose that delay raises first-renewal churn probability by 5 points, consistent with long implementations being linked to churn
- Expected lost lifetime gross profit: 15 × $400K × 5% × 75% margin × about 4 discounted years ≈ **$900K**
- Plus any delayed revenue if billing or expansion depends on go-live, and reference damage that can hurt win rates

**Cost of hiring three implementers now:**

- Loaded cost around $180K each per year, so about $540K per year, plus roughly $30K each in recruiting
- Low productivity during ramp, so the first few months deliver limited capacity
- **Downside if they turn out to be unnecessary:** less than their full cost. You can redeploy them to customer success or support, slow backfills as others leave, or absorb them into pipeline growth. A reasonable estimate of the true regret cost is perhaps six months of loaded salary, about $270K

These numbers are illustrative. The logic is the comparison: the expected cost of slowed implementations (probability the constraint binds × harm per delayed implementation) against the regret cost of hires you might not need.

## Step 3: Separate the no-regret capacity from the contingent capacity

Not all of the hiring decision depends on the attribution data:

| Capacity need | Depends on attribution? | Recommended action |
|---|---|---|
| Existing backlog and signed new implementations | **No.** These must be delivered either way | Hire now |
| Reducing implementation duration, a known churn driver | **Mostly no.** Long implementations hurt even if product gaps also matter | Hire now or soon |
| Staffing a large, extended rescue program | **Yes.** Size depends on whether rescue works | Use flexible capacity now, convert to hires at checkpoints |
| Long-term expansion of the services organization | **Yes.** Depends on the share of churn traced to services | Decide after attribution |

Hiring for the first two categories is justified under both hypotheses, because even if product gaps prove to be the bigger issue, slow implementations still waste your investment in any features you build, since customers must be live to use them.

## Step 4: Use flexible capacity to bridge the uncertain portion

For the rescue-driven portion, buy capacity you can reverse:

- **Contractors or implementation partners.** They cost more per hour, often 1.3 to 1.5 times the loaded cost of employees, but you can end the arrangement if checkpoints show rescue isn't working. Paying a premium for that flexibility makes sense when the need is uncertain.
- **Assign contractors carefully.** Put your experienced staff on rescue accounts, where judgment and customer relationships matter most, and use contractors on well-defined parts of new implementations such as data migration, configuration, or testing. Doing it the other way around risks botching the accounts you're trying to save.
- **Reprioritize internally.** Pause low-value internal projects or nonessential customizations to free senior staff temporarily.

## Step 5: Make contingent hiring decisions at the checkpoints

- **At 60 days:** If rescue indicators are improving and contractors are fully used, open requisitions to convert contractor capacity into permanent hires, which cost less over time.
- **At 90–120 days:** If early renewal outcomes support the service hypothesis, expand hiring beyond the no-regret level to shorten implementation times structurally.
- **If rescue shows no effect:** End contractor arrangements, keep the no-regret hires working on new implementations, and move investment toward the roadmap.

## Decision rules

- **If rescue draws on implementation staff and the backlog is already full:** Hire the no-regret portion now and bring in contractors for the rest. Waiting costs more than the regret of early hiring.
- **If rescue mainly uses CSMs and executives and the backlog is manageable:** Wait for the checkpoints and monitor go-live dates closely.
- **If you can't hire quickly or the talent market is tight:** Lean harder on partners and contractors, since the ramp lag makes waiting even more expensive.
- **At all times:** Track new-implementation duration as a leading indicator. If go-lives slip, the constraint is binding, and every month of delay adds churn risk to future cohorts.

## Bottom line

Hiring lags mean waiting for evidence costs months of slowed implementations, and those delays feed the churn you're trying to reduce. Capacity for existing backlog and faster implementations pays off under either hypothesis, so hire that portion now. Cover rescue-specific needs with contractors or partners you can release, and convert them to permanent staff only if the 60- and 90-day checkpoints show that rescue works and that service failures are driving churn.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do: An Integrated Plan

## The core decision

Put **delivery first, run the roadmap in staged parallel bets, and let evidence determine how much each side gets.** The reasoning from profit maximization:

- **Service fixes are fast, relatively cheap, and pay off under both hypotheses.** Customers who never reach full value can't benefit from new features, and slow implementations halve the lifetime value of every new deal you win.
- **Product gaps may be real, especially in sales, but the roadmap is slow and expensive.** Commit to it in stages as win/loss evidence confirms which gaps actually cost you deals.
- **Waiting for perfect information has its own cost.** Churned renewals and slipped implementations accumulate every month you delay, so act now on what's no-regret and stage the rest.

## The plan, in order

### Weeks 0–2: Set up

1. **Agree on the attribution method with both VPs before any data comes back.** Define the analyses, metrics, and decision thresholds jointly so the result settles the debate instead of starting a new one.
2. **Build the at-risk account list** and rank accounts by expected value of rescue: fixable problem, engaged sponsor, and renewal within two to three quarters. Deprioritize accounts that are already migrating, acquired, or healthy.
3. **Check whether rescue will draw on implementation staff** and review the current backlog and upcoming go-live schedule.
4. **Open requisitions for no-regret implementation hires** sized to the existing backlog and signed deals. These pay off regardless of which hypothesis wins.
5. **Engage an implementation partner or contractors** for flexible capacity to cover rescue-driven demand.

### Weeks 2–8: Act and diagnose simultaneously

**Launch the rescue program.**

- Budget up to about half the conservative break-even value per targeted account. In the earlier example, that was roughly $60K per account, or about $1.2M for 20 accounts. Replace these figures with your own ARR, margins, and churn rates.
- Count concessions and diverted staff time as real costs.
- Put experienced staff on rescue accounts and use contractors for well-defined new-implementation work.
- Start with the soonest renewals and stagger the rest so you can compare early indicators.

**Run the attribution analysis.**

- Plot churn against implementation duration and adoption depth. This is the most important single cut.
- Identify where churned customers went, and when the churn spike started relative to competitor launches and changes in your services organization.
- Strip out churn caused by M&A, budget cuts, or sponsor turnover, which neither fix can prevent.

**Run independent win/loss interviews with prospects.**

- Find out at what stage you lose deals, and whether you're eliminated for missing capabilities or merely outcompeted.
- Check whether prospects heard negative references about implementations.

**Start targeted product discovery.** Scope and begin small builds, partnerships, or integrations only for gaps that appear to be table stakes in RFPs.

### Around day 60: First checkpoint

Review leading indicators in rescued accounts compared with matched historical or staggered accounts: go-live progress, adoption depth, sponsor engagement, and escalations.

- **Indicators improving:** Continue rescue, extend it to medium-priority accounts, and begin converting contractor capacity into permanent hires.
- **Mixed:** Hold the budget flat and narrow to the highest-priority accounts.
- **No movement:** Reassess whether churn is really service-driven before spending more.

### Around days 90–120: Main decision point

With attribution results, win/loss data, and early renewal outcomes in hand, reallocate investment according to expected profit recovered per dollar:

| What the evidence shows | What to do |
|---|---|
| **Churn is concentrated in poorly implemented accounts** and rescue works | Scale the service overhaul: permanent hires, a redesigned implementation methodology, and time-to-value targets. Keep the roadmap focused on table-stakes gaps only. |
| **Fully adopted customers are leaving for AI-strong competitors** and you're losing deals at the shortlist stage | Accelerate the roadmap on the specific features cited in losses, in parallel with continued delivery fixes. |
| **Both are true** (the most common outcome) | Fund delivery fully, since it's faster and makes features usable, and scale product investment in proportion to confirmed deal losses. |
| **Losses cluster at the reference or pricing stage** | Treat the win-rate problem as a service or pricing issue, not a product gap. |

### Ongoing: Metrics and governance

Track a shared scorecard that both VPs own:

- Gross revenue retention and churn, by cohort and implementation duration
- Median time to go-live and time to full adoption
- Adoption depth among live customers
- Win rate and stage of loss, split by reason category
- Rescue program cost against renewals saved

Consider tying part of the Services VP's goals to adoption 12 months after go-live, and part of the Product VP's goals to win-rate recovery on the specific gaps the roadmap targets.

## What not to do

- **Don't launch a broad AI roadmap acceleration before win/loss data confirms which gaps cost deals.** That's where overinvestment is most likely.
- **Don't pull your best implementation staff onto rescue work without backfill.** You'll create the next wave of at-risk accounts.
- **Don't rely on exit interviews or CRM loss codes alone.** "Missing features" is the easiest thing for a departing customer or a losing rep to say.
- **Don't treat all churn as equally costly.** Some churned accounts may have been unprofitable.

## Bottom line

Start the rescue program and no-regret hires now, since those pay off regardless and waiting costs renewals. Run the attribution and win/loss analysis at the same time, with both VPs agreeing on the method in advance. Make small, targeted product bets on table-stakes gaps. At 60 days, adjust the rescue program; at 90–120 days, reallocate the larger investment toward whichever fix recovers the most lifetime gross profit per dollar. Most likely, that will mean fixing delivery at full speed while scaling product work to match the deal losses the evidence confirms.

## Outcome summary (sent to Jev)

The assistant recommends putting delivery first, running the product roadmap as staged parallel bets, and letting evidence decide how much each side ultimately gets. Neither VP's belief can be declared right yet. The guiding question is which investment recovers the most lifetime gross profit per dollar, soonest.

Its reasoning is that service fixes are fast, relatively cheap, and pay off under either hypothesis. Customers who never reach full value can't benefit from new features, and elevated churn roughly halves the lifetime value of every new deal won. Product gaps may genuinely hurt win rates, but roadmap work is slow and expensive. Meanwhile, waiting for perfect information costs renewals and slows implementations.

The proposed plan has these parts:

- **Agree on method first.** Both VPs sign off on the attribution method before any data arrives.
- **Launch a rescue program.** It targets high-value, fixable at-risk accounts, budgeted at about half the conservative break-even value per account. Concessions and diverted staff time count as costs.
- **Hire and bridge capacity.** No-regret implementation staff are hired for the existing backlog, with contractors or partners covering rescue-driven demand.
- **Test the hypotheses.** The key analysis plots churn against implementation duration and adoption depth, tracks where churned customers went, and strips out M&A, budget, and sponsor-turnover churn. Independent win/loss interviews run alongside.
- **Place small product bets.** These go only to table-stakes gaps.
- **Adjust at checkpoints.** The rescue program is adjusted at 60 days, and larger investment is reallocated at 90–120 days.

The assistant cautions against a broad AI push before win/loss data confirms which gaps cost deals. It warns against pulling senior implementers onto rescue work without backfill, relying on exit interviews or CRM loss codes, and treating all churn as equally costly. The illustrative figures should be replaced with the company's own numbers.
