# independent-lab/economic/testD

Model: claude-opus-5-5 · 2026-09-24T15:21:16.069047+00:00

## Turn 1

**User:** I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

**Assistant:**

# Neither Pure Strategy Is Right

Framing this as "work within the system" versus "independent lab" hides the most important financial fact: **the company is losing money it already has faster than it can make new money.** Any strategy should be judged first by how quickly it stops that loss. By that test, the CEO's instinct is closer to right on timing, and yours is closer to right on structure. The best answer takes something from each.

Below I follow the money through each option using an illustrative company. Replace my numbers with your real ones. I've made the assumptions explicit so you can do that.

## Illustrative Baseline (Replace With Real Figures)

- $250M total revenue, of which $175M is recurring (subscription/maintenance)
- 12% gross annual revenue churn, so **~$21M of recurring revenue walks out every year**
- 65% gross margin on recurring revenue
- Thin operating margin, limited appetite for large new cash outlays
- Enterprise sales cycles of 9–24 months. Insurers are slow, risk-averse buyers with heavy compliance and integration demands.

Two properties of this business drive everything that follows:

1. **Retained revenue compounds.** Saving a $1M customer this year protects $1M next year, the year after, and so on. At typical B2B software multiples, each $1M of retained recurring revenue is worth several million in enterprise value.
2. **New products in insurance software are slow to monetize.** Even a great product needs pilots, security reviews, integration with policy/claims/billing systems, and reference customers before revenue scales.

## Strategy A: Innovate Within the Existing Organization (CEO's View)

**How it makes money**
- **Protects revenue:** Fixing the reasons customers leave, such as product gaps, implementation pain, service quality, or missing integrations.
- **Generates revenue:** Improving win rates and upselling with incremental features built on the existing platform.

**Investment and operating costs**
- Low incremental cash, perhaps **$3–6M/year** for a small central team, customer success capacity, tooling, and targeted product work.
- The larger cost is hidden: **reallocated capacity**. Engineers pulled onto innovation work stop doing something else, often roadmap commitments that customers were promised.

**Returns and timing**
- Cutting churn from 12% to 9% saves about $5M of recurring revenue in year 1. Because retained revenue stacks, that becomes roughly $10M protected in year 2 and $15M in year 3.
- **Returns begin in 6–18 months**, because renewals arrive on a known calendar. You can target specific at-risk accounts by renewal date.
- This is the fastest, most measurable return available to you.

**Risks that could wipe out returns**
- **The root cause is structural.** If customers are leaving because the core platform is legacy (on-prem, hard to configure, slow to upgrade) and competitors like Guidewire, Duck Creek, or cloud-native insurtechs are simply better, incremental fixes delay churn but don't stop it.
- **Organizational antibodies.** The same processes and incentives that produced the decline tend to absorb and dilute new initiatives. "Innovation" becomes a label on the existing roadmap.
- **Retention bought with margin.** Saving customers through discounts and bespoke customization protects revenue while destroying profit.

**Where spending grows without profit**
- Custom work for individual at-risk accounts that can't be productized.
- Replatforming or "modernization" programs with no fixed end, which are the classic enterprise money pit.
- Professional services headcount growing to paper over product weaknesses.
- Consultants brought in to "drive transformation."

**Control and accountability**
- Budget stays with existing department heads. Results are diffuse: if churn drops, sales, customer success, product, and you all claim credit. If it doesn't, no one owns the failure.
- **Nobody is positioned to stop spending**, because the spending is embedded in operating budgets and never appears as a discrete bet. This is the biggest governance weakness.

## Strategy B: Independent Innovation Lab (Your View)

**How it makes money**
- **Generates revenue** from new products, new segments, or new business models (for example, embedded insurance APIs, AI-driven underwriting or claims tools, or a cloud-native product for smaller carriers and MGAs).
- **Protects revenue only indirectly**, and only if lab output eventually reaches existing customers.

**Investment and operating costs**
- A credible lab of 30–50 people at fully loaded enterprise-software salaries costs **$6–12M/year**.
- Frequently missed costs:
  - **Go-to-market.** New products need their own sales, solutions engineering, and marketing, adding $3–5M/year once there's something to sell.
  - **Compliance and security.** Insurers require SOC 2, data residency, and regulatory review, which is expensive to rebuild outside the parent.
  - **Integration.** New products must eventually connect to the core platform or customers won't buy.
- Realistic 3-year spend: **$25–45M**.

**Returns and timing**
- Year 1: essentially zero revenue.
- Year 2: paid pilots, perhaps $0.5–2M.
- Year 3: $3–10M in recurring revenue *if* something hits.
- A reasonable probability of a meaningful hit is perhaps 20–30%. On a risk-adjusted basis, **expected value over 3 years is likely negative**, with upside concentrated in years 4–7.
- Meanwhile, churn continues. Over those three years the core loses roughly $60M+ of recurring revenue that the lab does nothing to stop.

**Risks that could wipe out returns**
- **Time and cash.** If the core business deteriorates faster than the lab matures, the CFO will cut the lab before it pays off. This is the most common way corporate labs die.
- **Sponsor risk.** The CEO doesn't believe in this model. Your lab would launch without its most important sponsor and would be the first thing cut in a bad quarter.
- **The transfer problem.** Labs routinely build things the parent can't absorb, sell, or support. The lab "succeeds" technically and fails commercially.
- **Distribution disadvantage.** A startup-like unit without the parent's customer relationships faces the same brutal sales cycles as a startup, without startup equity incentives to retain talent.
- **Cannibalization conflict.** If the lab's product competes with the core, the core sales force may quietly refuse to sell it.

**Where spending grows without profit**
- **Pilot purgatory.** Endless unpaid or cheap pilots that validate interest but never convert to contracts.
- Headcount creep: "we need our own designers, data engineers, DevOps, compliance lead..."
- Duplicated infrastructure the parent already has.
- Innovation theater: demos, hackathons, and showcases that generate enthusiasm but no revenue.

**Control and accountability**
- You control the budget, which is attractive but concentrates risk on you personally.
- Financial ownership is murky. If the lab's product is sold by the core sales team to existing customers, which P&L gets the revenue?
- Stop decisions tend to be made **reactively by the CFO during a budget crunch**, not deliberately against evidence.

## Side-by-Side Comparison (Illustrative)

| | A: Within the core | B: Independent lab |
|---|---|---|
| 3-year incremental cash | $10–18M | $25–45M |
| Primary value | Protects existing revenue | New revenue streams |
| Time to first returns | 6–18 months | 24–36+ months |
| Probability of meaningful return | Moderate–high | Low–moderate |
| Size of upside | Capped by core's competitiveness | Potentially large |
| Biggest risk | Root cause is structural; efforts get diluted | Cash/sponsor runs out before payoff |
| Hidden cost drain | Custom work, endless modernization | GTM, pilots, duplication |
| Who stops spending | No one (embedded in budgets) | CFO, reactively |

## A Third Approach: Protected but Connected, Funded in Stages

The better structure combines the core's speed to money with the lab's independence, and adds the missing piece: **explicit, evidence-based funding decisions.**

### Phase 1 (Months 0–6): Diagnose and Stop the Bleeding
- Analyze every lost customer and lost deal from the last 2–3 years. Interview churned customers directly. Segment churn by cause: product, service, price, platform, or competitor.
- Stand up a **small, cross-functional strike team of 8–15 people** that reports to you, with real authority to change product priorities for at-risk accounts.
- Target the top 20–30 accounts by renewal date and revenue.
- **Cost:** ~$2–4M. **Target:** measurable churn reduction within two to three renewal cycles.
- This buys you credibility with the CEO, gives you data, and funds what comes next.

### Phase 2 (Months 4–12): Launch a Venture Unit Aimed at Why You Lose
- Structurally protected: own budget, own hiring, own development process, exempt from the core's approval layers.
- Strategically tethered:
  - Builds on the core platform and data rather than from scratch.
  - Sells first to existing customers, which cuts sales cycles and reduces churn at the same time.
  - Targets problems surfaced in Phase 1, not ideas generated in a vacuum.
- Consider capital-light options before building: partnering with or white-labeling insurtechs, building an integration marketplace, or small acqui-hires. These can deliver capability in months rather than years.

### Phase 3 (Ongoing): Staged Funding With Kill Criteria
Fund each initiative in tranches, as a VC would:

| Gate | Evidence required | Typical tranche |
|---|---|---|
| 1. Problem | 10+ customer interviews confirm a costly problem tied to churn or lost deals | $250–500K |
| 2. Solution | Signed letters of intent or design partners | $1–2M |
| 3. Traction | Paid pilots converting to contracts | $2–4M |
| 4. Scale | Repeatable sales; revenue attributable to the unit | Full product/GTM budget |

**Kill rule:** If an initiative misses its gate evidence within a set window (for example, two quarters), funding stops by default unless the committee votes to continue. Making stopping the default removes the sunk-cost problem.

### Governance That Answers Your Control Questions
- **Budget control:** A small investment committee (CEO, CFO, you, heads of product and sales) meets quarterly and releases tranches against gate evidence.
- **Financial ownership:** Agree upfront on attribution. For example, the venture unit gets credit for new product revenue and for retention of accounts it directly engages, even if core sales books the deal. Consider shadow P&L credit for core sales teams so they are motivated to sell new products rather than block them.
- **Stop decisions:** Made by the committee against predefined criteria, not by the CFO in a crisis or by you out of attachment.

### Why This Offers Better Returns for the Capital at Risk
- **Capital at risk is smaller and staged.** You might commit $15–25M over three years, but only $3–5M is at risk before evidence justifies more.
- **Returns arrive earlier.** Phase 1 churn reduction starts paying within the first year.
- **Upside is preserved.** A winning venture bet can still become a meaningful new revenue line.
- **Profitability is protected** because spending scales only with demonstrated results.
- **It aligns with the CEO rather than opposing him.** You deliver early results inside the existing business, then use them to earn permission for more independence.

## What You Need to Know Before Committing

1. **Why are customers actually leaving?** This determines whether core fixes can work at all. If the answer is "the platform is obsolete," Strategy A alone fails and the venture unit becomes urgent.
2. **What is the real churn and win rate by segment?** Churn is rarely uniform. Some segments may be salvageable and others not.
3. **How much cash and patience does the company have?** Runway determines whether any bet longer than 18 months is survivable.
4. **What does the CFO consider an acceptable investment?** Get their hurdle rate and payback expectations early.
5. **What does the CEO mean by "outsized results"?** Clarify whether he wants revenue growth, churn reduction, a new market narrative for investors, or all three, and on what timeline.

## One Note on Positioning

You were hired by a CEO who has a stated view. Proposing a lab independent of "his" organization in your first months risks being read as a rejection of his judgment, and sponsor loss is the leading killer of corporate innovation units. Frame the third approach as **executing his strategy faster**: "We'll start inside the business, fixing churn with a dedicated team, and we'll build protected capacity for new products only where the evidence justifies it." You get the independence you believe is necessary, earned through results rather than requested upfront.

## Turn 2

**User:** Your Phase 1 strike team can reprioritize product work for the top 20–30 at-risk accounts, which sounds like the custom-work drain you warned about under Strategy A. After discounts, bespoke features, and delayed roadmap commitments, how much of that $5M in year-one retained revenue actually shows up as profit?

**Assistant:**

# Year One Is Roughly Breakeven at Best

You're right, and I understated this. I presented $5M as a return when it's revenue, and I didn't net out the strike team's own cost or the custom-work drain I'd warned about under Strategy A. Once you do that, **year one is roughly breakeven if run well and meaningfully negative if run badly.** The profit case depends on years two and three, and on a few specific rules that stop the strike team from becoming a custom-development shop.

## Why $5M of Retained Revenue Isn't $5M of Profit

Six things sit between retained revenue and profit:

1. **Deadweight.** Some "at-risk" accounts would have renewed anyway. Risk scoring is imprecise, and teams tend to claim credit for every renewal they touch. Typically 25–50% of saved revenue wasn't really at risk.
2. **Gross margin.** Only about 65% of retained revenue is gross profit. Hosting, support, and maintenance costs don't go away.
3. **Discounts.** Retention discounts of 10–20% come straight off profit. They're often given to accounts that would have stayed anyway, so they're pure loss on the deadweight portion.
4. **Bespoke engineering.** Custom features built for one account cost engineering time, then carry maintenance costs of roughly 15–25% of build cost per year. They also make every future upgrade harder.
5. **Roadmap delay.** Engineers working for at-risk accounts aren't building what prospects and other customers were promised. That can slow new bookings and create churn risk elsewhere.
6. **The strike team itself.** The $2–4M I estimated earlier has to come out of the same return.

## Year-One Profit: Two Scenarios (Illustrative)

Assume $5M of list-price recurring revenue across the targeted accounts renews, and costs of service run at 35% of list price regardless of discount.

| | Poorly run | Well run |
|---|---|---|
| Share that would have renewed anyway | 40% | 25% (tighter targeting) |
| Discount | 15% to every targeted account | 5%, only to truly at-risk accounts, traded for multi-year terms |
| Revenue with program | $4.25M | $4.81M |
| Gross profit with program | $2.50M | $3.06M |
| Gross profit without program (deadweight renews at full price) | $1.30M | $0.81M |
| **Incremental gross profit** | **$1.20M** | **$2.25M** |
| Strike team (non-engineering) | –$1.5M | –$1.5M |
| Engineering on account-specific work | –$1.8M (mostly one-off code) | –$0.8M (mostly roadmap work pulled forward) |
| Roadmap delay (lost or slipped bookings) | –$0.5M | –$0.2M |
| **Year-one incremental profit** | **≈ –$2.6M** | **≈ –$0.25M** |

Even the well-run version roughly breaks even in year one. The poorly run version loses money while reporting a $5M "win."

## Over Three Years, the Two Scenarios Diverge Sharply

Assume a new cohort of at-risk accounts is treated each year with similar economics.

- **Well run:** Fixes address root causes, so saved accounts mostly stay (about 90% per year). One-off code is minimal.
- **Poorly run:** Root causes persist, so saved accounts keep drifting back to at-risk (about 70% per year). Maintenance of custom code grows each year.

| Incremental profit | Poorly run | Well run |
|---|---|---|
| Year 1 | –$2.6M | –$0.25M |
| Year 2 | –$2.2M | +$1.7M |
| Year 3 | –$2.0M | +$3.4M |
| **3-year cumulative** | **≈ –$6.8M** | **≈ +$4.8M** |

The well-run version becomes profitable because retained revenue recurs while the cost of productized fixes doesn't. The poorly run version stays negative indefinitely because it buys each renewal with fresh discounts and custom code. The poorly run column also excludes **discount contagion**: other customers learn that threatening to leave gets a price cut.

## What Makes the Difference

The two biggest levers are **how much deadweight you pay for** and **whether engineering work is reusable.** These rules address both.

**1. Reusable or refused.** The strike team can build only features that are already on the roadmap, or that at least three other customers or prospects need. Everything else is solved through configuration, services, or not at all. This rule most directly prevents the custom-work drain.

**2. Try non-product fixes first.** Many churn causes aren't missing features. They're failed implementations, poor support, painful upgrades, or a lost executive relationship. These are the cheapest problems to fix and often the highest return. The team should exhaust them before touching engineering.

**3. Discounts only in exchange for something.** Every discount should buy a multi-year term, a price escalator, an added module, or a reference commitment. Cap discounts, and require CFO approval above a threshold.

**4. Measure incremental retention, not touched renewals.** Compare treated accounts against a holdout group or against historical renewal rates for similar risk scores. Otherwise deadweight will make the program look far better than it is.

**5. Cap the engineering draw.** Limit the strike team to a fixed share of engineering capacity, perhaps 15–20%. Publish what gets delayed as a result, and have the product leader sign off so roadmap costs are visible.

**6. Let some accounts go.** Calculate contribution margin by account. Some customers cost more to keep than they're worth, and the team needs explicit permission not to save them.

**7. Report profit, not just revenue.** The headline metric should be incremental contribution profit from retained accounts, with net revenue retention alongside it. Retained revenue alone rewards exactly the behavior that destroys profit.

**8. Set a stop rule.** If incremental contribution is still negative and not improving after two renewal cycles, shut the program down or restructure it.

## Revising the Pitch

The honest version for the CEO and CFO is: **Phase 1 costs about $2–3M and roughly breaks even in year one. It becomes profitable in years two and three if we enforce these rules, and we'll know within two renewal cycles whether it's working.**

The strike team's most valuable output may be information rather than year-one profit. Seeing why 20–30 accounts nearly left shows which problems are cheap service fixes, which belong on the core roadmap, and which reveal a structural platform gap that justifies the Phase 2 venture unit. The rules above keep that learning from being paid for with margin.

## Turn 3

**User:** If most contracts renew annually, "two renewal cycles" means about two years and most of the $5M-plus already spent. What early signal could tell us within six months whether we're in the well-run or poorly-run column, and how much would we have committed by then?

**Assistant:**

# Six Months Is Enough, Because Most Losses Come From Decisions You Can See Immediately

Look back at what separated the two columns. Most of the gap came from **choices**: discounts to accounts that would have stayed, one-off code, and roadmap delays. Those show up in contracts, engineering tickets, and discount approvals within weeks. Only one question genuinely requires renewals: **do saved accounts stay saved?** Even that can be pulled forward.

By month six, you can know with reasonable confidence which column you're in on *process*, and directionally on *outcomes*. You'll have spent roughly **$1.2M if run well, $1.7M if run badly**, with total exposure including forward commitments of about **$1.5M versus $3–4M**.

## The Six-Month Scorecard

Set thresholds before you start, so no one can reinterpret results afterward.

| Signal | Readable by | Well-run column | Poorly-run warning |
|---|---|---|---|
| **Risk-model accuracy** (backtest your risk scores against last year's actual renewals) | Weeks 2–4 | High-risk accounts churned at 3x+ the rate of others | Scores barely predicted churn, so deadweight will be high |
| **Root-cause mix** from diagnosing the first 20–30 accounts | Months 2–3 | Majority fixable by service, configuration, or existing roadmap items | Majority need custom features or reflect platform gaps the team can't fix |
| **Engineering reuse rate** (share of hours on roadmap items or features 3+ customers need) | Monthly from month 2 | 70% or more | Under 50%, trending down |
| **Discount discipline** | From first deals, months 2–4 | Average under 5%; 70%+ of discounts traded for multi-year terms, escalators, or add-ons | Average 10%+; discounts given without anything in return |
| **Roadmap slippage** | Monthly | Few committed items delayed; no pipeline deals citing missing features | Growing list of delays; sales reports deals stalling on promised features |
| **Treated vs. holdout health** (usage, support severity, executive engagement) | Months 3–6 | Treated accounts improve measurably relative to holdout | No difference, meaning the team's effort isn't changing outcomes |
| **Re-risk rate** (saved accounts sliding back to at-risk within 90 days) | Months 4–6 | Low | High, meaning the team is patching symptoms rather than fixing causes |
| **Actual renewals in the window** | Months 1–6 | Renewal rate well above the historical rate for similar risk scores | At or near the historical rate |

The first two signals are the most valuable because they're cheap and arrive before significant engineering spend. If the risk model can't predict churn, you'll pay for deadweight no matter how well the team performs. If most root causes are platform gaps, the strike team can't fix them, and that's an early argument for Phase 2 rather than more Phase 1 spending.

## Pulling the Renewal Signal Forward

Three design choices convert a two-year question into a six-month one:

**1. Target by renewal date.** If the first cohort is weighted toward accounts renewing in months 1–9, a third to half of them reach a real decision inside the window. The sample is small, perhaps 8–15 accounts, so treat results as directional rather than conclusive.

**2. Offer early renewals.** Approach at-risk accounts renewing in months 7–18 with an early multi-year renewal in exchange for specific commitments: a named fix, an implementation review, or modest terms traded for length. A signed early renewal is a hard outcome. A refusal is also a strong signal. Either way, you learn in months rather than waiting for the contract date.

**3. Run a holdout from day one.** Randomly leave a portion of at-risk accounts on normal treatment, perhaps 20–30%. Without a comparison group, no amount of time will tell you whether the team caused renewals or just stood near them. Holding out at-risk customers feels uncomfortable. Choose accounts where the downside is tolerable, and accept that without a holdout you'll be making a multi-million-dollar decision on anecdote.

## What You'll Have Committed by Month Six

**Spent** is what's gone. **Committed** also includes obligations that continue after you stop: discounts written into multi-year contracts, custom features promised in writing, and hires that are costly to unwind.

| | Well run | Poorly run |
|---|---|---|
| Strike team (half-year) | $0.75M | $0.75M |
| Engineering on account work | $0.4M | $0.9M |
| Discounts realized so far | ~$0.05M | ~$0.2M |
| **Spent by month six** | **≈ $1.2M** | **≈ $1.85M** |
| Forward discount obligations in signed contracts | ~$0.2M | ~$1.1M (15% locked into multi-year renewals) |
| Custom features promised but not built, plus maintenance | ~$0.1M | ~$0.8M |
| **Total exposure** | **≈ $1.5M** | **≈ $3.5M** |

In the poorly run version, nearly half the damage at month six is already locked into contracts and promises. Stopping the program at that point doesn't recover it.

## Limiting Irreversible Commitments in the First Six Months

Structure Phase 1 so that stopping at month six is cheap:

- **Gate engineering behind diagnosis.** Spend weeks 0–8 on the backtest, holdout design, baselines, and root-cause interviews. This costs roughly $0.3M. Release engineering capacity only after the root-cause mix is known.
- **Staff with secondments and contractors, not new hires.** Borrow people from existing teams and return them if the program stops.
- **Keep discounts time-limited.** Prefer one-year concessions or discounts that expire unless tied to multi-year terms with escalators.
- **Promise roadmap items, not contract clauses.** Commit to "this is on the roadmap for Q3," not a contractual obligation to build a custom feature.
- **Require sign-off on anything that outlives the program.** Any multi-year discount or written feature commitment above a threshold goes to the CFO.

These steps can cap poorly-run exposure near $2M, because the worst decisions get caught before they're signed.

## The Month-Six Decision

Agree on the rules before starting:

- **Continue** if process metrics are in the well-run column and treated accounts show measurable improvement over the holdout.
- **Restructure** if outcomes look promising but process is slipping, such as rising discounts or falling reuse. Tighten the rules, replace team leadership if needed, and reassess at month nine.
- **Redirect** if the root-cause mix is dominated by platform gaps. The strike team can't fix those. Shift budget toward the Phase 2 venture unit or a platform investment, and keep only the cheap service-fix work.
- **Stop** if treated accounts perform no better than the holdout. The team isn't changing outcomes, and more time won't fix that.

## What Six Months Won't Tell You

Process metrics predict the profit gap well, because that gap was mostly created by visible decisions. Retention durability is weaker. With 8–15 real renewals and a few months of health data, you'll know the direction but not the magnitude. A result like "treated accounts renewed at 85% versus 70% for the holdout" is meaningful. A difference of a few points is noise at this sample size.

That's acceptable. The month-six decision isn't about proving the full three-year return. It's about confirming you're in the column where that return is possible, before committing the remaining 75% of the budget.

## Turn 4

**User:** What's the expected revenue we'd lose by deliberately leaving 20–30% of our at-risk accounts untreated, and is a cleaner measurement worth more than those renewals?

**Assistant:**

# A Six-Month Holdout Costs Little, but It Measures the Wrong Accounts

The expected loss is smaller than it first appears: probably **$0.3–0.5M in lifetime profit** for a six-month holdout, versus $1.5–2M if you withheld treatment permanently. But the bigger problem isn't cost. **A holdout drawn from only 20–30 accounts is too small to tell you much.** You'd be paying real money and risking real customer relationships for weak evidence. A better design gets cleaner measurement at lower cost.

## What the Holdout Actually Costs

Three points shrink the number.

**1. Holdout accounts still get normal service.** You're not abandoning them. You're withholding the *extra* effort. So you lose only the treatment's incremental effect, not the accounts' whole revenue.

**2. The loss exists only if treatment works.** If the strike team isn't changing outcomes, holding accounts out loses nothing. In the poorly run column, it actually *saves* money, because treatment was profit-negative. The expected cost depends on how confident you are that treatment works, and that confidence is exactly what you're trying to measure.

**3. The holdout doesn't have to be permanent.** If you treat holdout accounts after month six, only those renewing inside the window are exposed.

Using the well-run assumptions, where treatment adds about $3.6M in retained revenue across the cohort:

| Design | Revenue forgone | Net lifetime profit forgone* | Probability-weighted** |
|---|---|---|---|
| Permanent holdout, 25% of top accounts | ~$0.9M per year | ~$1.5–2M | ~$0.8–1M |
| Six-month holdout, then treat | ~$0.35M (only accounts renewing in the window) | ~$0.6–0.8M | ~$0.3–0.5M |
| Holdout from a lower-value at-risk tier | ~$0.1–0.2M | ~$0.2–0.4M | ~$0.1–0.2M |
| Staggered rollout (treat in waves before each renewal) | Near zero | Near zero; the cost is delay | Near zero |

\* After subtracting treatment costs you avoid on holdout accounts, such as engineering and discounts, and assuming saved accounts stay several years.
\*\* Assuming roughly even odds that treatment works as modeled.

**These costs depend on the large treatment effect I assumed earlier.** The well-run column implied that only about 20% of targeted accounts would renew without help and more than 80% would with it. Accounts flagged as at-risk often renew at 50–70% on their own. If that holds here, the true treatment effect is smaller, the holdout costs less, and the program's return is lower than my earlier tables suggested. That uncertainty is the strongest argument for measuring at all.

## What the Measurement Is Worth

A cleaner measurement is valuable only if it changes the month-six decision.

That decision is whether to commit the remaining $4–5M. A wrong call is expensive either way:

- **Continuing an ineffective program** costs roughly $5–7M over three years (the poorly run column).
- **Stopping a working program** forgoes roughly $5M (the well-run column).

Without a comparison group, the natural fallback is comparing treated accounts against historical renewal rates. That comparison flatters the program. Accounts flagged at their worst moment tend to recover partly on their own, a statistical effect called regression to the mean. The team will also sincerely attribute every renewal it touched to its own work. This could mean a 30–40% chance of the wrong call.

If a good comparison cut that to 15–20%, the value would be roughly 15–20 percentage points times a $5–6M error, or **about $0.8–1.1M**. That exceeds the $0.3–0.5M cost of a six-month holdout, so measurement looks worthwhile.

**The catch is sample size.** A 25% holdout of 25 accounts is six or seven accounts, and only three or four would renew within six months. No reasonable analysis can separate a real effect from noise with four data points. One large customer churning for unrelated reasons, such as an acquisition or new CIO, would swing the result. A top-account holdout costs real money and relationships and delivers almost none of that $0.8–1.1M value.

## A Better Design: Protect the Top Accounts, Measure Where You Have Numbers

**1. Treat all top 20–30 accounts.** Don't hold out your largest or most strategic customers. The sample is too small to justify it, and account executives will fight it, reasonably.

**2. Run a randomized test on the next tier.** Take the next 60–100 at-risk accounts, perhaps $30–100K each, and randomly assign half to a lighter-touch playbook of implementation reviews, support escalation, and executive outreach. No custom engineering and no discounts. This tests the question that matters most for profitability: do the cheap, non-product fixes work? With 30–50 accounts per group, you have a real chance of detecting a meaningful effect, and the revenue at risk is small.

**3. Randomize the expensive levers within the top accounts.** Instead of withholding all treatment, randomize one costly component, most usefully discounts. For example, offer term-for-discount trades to half the top accounts and non-price concessions to the other half. Every account still gets help, but you learn whether discounts buy retention or just give margin away. Discounts are where the poorly run column lost the most money.

**4. Stagger the top accounts instead of holding them out.** Treat them in waves ordered by renewal date, each wave well before its renewal. Accounts not yet treated serve as a rough comparison group for health metrics like usage, support severity, and executive engagement. This gives weaker evidence than randomization but costs almost nothing.

**5. Use a modeled baseline for the top tier.** Your risk-model backtest from weeks 2–4 gives an expected renewal rate for each risk band. Compare treated top accounts against that expectation, discounted for regression to the mean. This isn't clean, but it's better than raw historical rates.

**Cost of this design:** roughly $0.1–0.2M in expected lifetime profit, mostly from the next-tier test. It produces statistically meaningful evidence on the cheap interventions and direct evidence on whether discounts work.

## When Not to Bother Measuring

Measurement is worth paying for only when the process metrics are ambiguous.

If by month three the engineering reuse rate is under 50% and discounts are averaging 15%, you're in the poorly run column regardless of what any holdout shows. Fix the process or stop. If reuse is high, discounts are disciplined, and root causes are mostly cheap to fix, you're likely in the well-run column. The measurement then mainly tells you *how large* the return is, which matters for sizing the budget but not for deciding whether to continue.

The measurement pays off in the middle case: process looks healthy, but it's unclear whether the team is actually changing renewal outcomes. That case is common enough to justify the next-tier test, but not a holdout among your most important customers.

## Turn 5

**User:** What should we do?

**Assistant:**

# The Recommendation

**Don't build the independent lab now, and don't simply work through existing processes either.** Run a tightly governed six-month program with a hard cap of about $2M. It should answer three questions that decide everything else: why customers are leaving, whether cheap fixes keep them, and whether the underlying problem is the platform itself. Use the answers to decide at month six whether to scale up, redirect money toward a new-product unit, or stop.

This risks about $1.5–2M instead of $25–45M. It starts protecting revenue within months. And it positions you as executing the CEO's strategy with discipline rather than opposing it.

## Days 1–30: Get Real Numbers and Agree on the Rules

Spend almost nothing until these are done. Budget: about $0.3M.

**Replace my illustrative figures with real ones:**
- Churn by segment, product, and cause over the last 2–3 years
- Win/loss reasons for the last 2–3 years of deals
- Renewal calendar for all at-risk accounts
- Contribution margin by account, so you know which customers are worth saving

**Test your ability to target:** Backtest the risk scores against last year's renewals. If they didn't predict churn, fix targeting before anything else.

**Talk to customers:** Interview 15–20 churned and at-risk customers yourself. Don't delegate this. It's the fastest way to learn whether the problem is service, product, or platform.

**Agree on governance with the CEO and CFO before spending more:**
- An investment committee (CEO, CFO, you, heads of product and sales) that meets monthly during this phase
- The month-six scorecard, with thresholds written down in advance
- Discount policy: discounts only in exchange for multi-year terms, escalators, or add-ons, with CFO approval above a set level
- The reuse rule: no custom engineering unless it's on the roadmap or at least three customers need it
- A cap of 15–20% of engineering capacity
- Pre-agreed triggers for continuing, restructuring, redirecting, or stopping

If the CEO won't agree to this governance, treat that as the most important finding of the first month. Without it, the program will likely drift into the poorly run column.

## Months 2–6: Run the Program

Budget: about $1.2M spent, total exposure capped near $1.5M.

**Top 20–30 accounts:**
- Treat all of them, in waves ordered by renewal date
- Try service, implementation, and relationship fixes first
- Release engineering only after the root-cause mix is known, around week 8
- Offer early multi-year renewals to accounts renewing in months 7–18, to pull outcomes into the measurement window
- Randomize the discount lever: term-for-discount trades for half, non-price concessions for the other half

**Next tier of 60–100 at-risk accounts:**
- Randomly assign half to a light-touch playbook: implementation reviews, support escalation, and executive outreach, with no custom engineering and no discounts
- This is your clean measurement of whether cheap fixes work

**Staffing:** Use secondments and contractors, not new hires, so stopping is cheap.

**Reporting:** Report monthly to the committee on incremental profit alongside retained revenue, using the scorecard.

## In Parallel: Prepare for the New-Product Unit Without Funding It

Budget: about $0.2M, with 2–3 people at most.

- Tag every churn and lost-deal reason that points to a structural platform gap
- Map partners, insurtechs, and small acquisition targets that could close those gaps faster than building
- Draft a stage-gated plan for the venture unit, ready to present at month six

This way, a "platform gap" finding at month six leads straight to action instead of starting a new six-month planning cycle.

## Month 6: Decide Using the Pre-Agreed Triggers

| If you see | Then |
|---|---|
| Disciplined process (reuse ≥70%, discounts ≤5% and traded for term) plus measurable improvement in treated accounts | **Scale** retention work to the next cohorts and fund Phase 2 at Gate 1 |
| Promising results but slipping discipline | **Restructure:** tighten the rules or change team leadership, then reassess at month nine |
| Root causes dominated by platform gaps | **Redirect:** keep the cheap service fixes, shift money to the venture unit or a partnership or acquisition |
| Treated accounts no better than comparison accounts | **Stop** the strike team, keep whatever service fixes proved useful, and rethink |

## How to Present This to the CEO

Something like: *"You're right that we should start inside the business. I'll run a six-month program capped at $2M that targets our at-risk accounts, with rules that protect margin and a clear scorecard. At month six, I'll bring you evidence on what's driving churn. If it points to the platform, I'll have a staged plan ready to address it. If the program isn't working, I'll recommend stopping it."*

Proposing your own stop conditions will build more credibility with a skeptical CEO and CFO than any projected return.

## What Would Change This Plan

- **If the first 30 days show most losses going to cloud-native competitors on platform grounds,** start Phase 2 immediately at Gate 1 funding, alongside a smaller retention effort. Incremental fixes won't hold customers who are leaving for a better architecture.
- **If cash is very tight,** cut back to service fixes and the light-touch playbook. Skip custom engineering entirely.
- **If the real numbers show churn is concentrated in a few segments,** focus there and consider whether some segments should be deprioritized.

The one thing that shouldn't change is the sequence: get real data, agree on rules, make small reversible bets, and let evidence decide when to spend more.

## Outcome summary (sent to Jev)

The recommendation is neither to build an independent innovation lab now nor to work simply through existing processes. Instead, run a tightly governed six-month program capped at about $2M. It should establish why customers leave, whether cheap fixes keep them, and whether the platform itself is the problem. At month six, the evidence decides whether to scale, redirect money to a new-product venture unit, or stop.

The main reasons are exposure and timing. This approach risks roughly $1.5–2M instead of the $25–45M a lab would need. It begins protecting recurring revenue within months, while a lab would produce little before years two or three. It also positions the effort as executing the CEO's strategy rather than opposing it, since losing the sponsor is the leading killer of innovation units.

The first 30 days, costing about $0.3M, go to gathering real churn, win/loss, renewal and account-margin data, backtesting risk scores, and personally interviewing 15–20 customers. The CEO and CFO must also agree on governance: an investment committee, a written scorecard, discounts traded only for multi-year terms, a rule of no custom engineering unless reusable, a 15–20% cap on engineering capacity, and pre-set triggers. Months two through six then proceed:

* All top 20–30 accounts are treated in waves.
* Early renewals are offered to pull outcomes into the measurement window.
* Discounts are randomized, with half the accounts getting term-for-discount trades and half getting non-price concessions.
* The next 60–100 accounts are randomly split for a light-touch playbook.
* Staffing comes from secondments and contractors.
* Monthly reports focus on incremental profit.

In parallel, a small team prepares a stage-gated venture plan.

There are three caveats. If losses go to cloud-native competitors on platform grounds, Phase 2 should start immediately. If cash is tight, custom engineering should be skipped. If the CEO refuses the governance, that refusal is the key finding.
