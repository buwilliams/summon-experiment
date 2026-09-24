# independent-lab/economic/testC

Model: claude-opus-5-5 · 2026-09-24T15:19:57.923742+00:00

## Turn 1

**User:** Use profit maximization to answer the following.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

# Short Answer

Neither pure strategy maximizes profit. Measured by profit, **the CEO is more right about where the money is, and you are more right about how breakthrough work gets built.** The profit-maximizing move is a staged hybrid:

1. Fix churn through the core organization first.
2. Fund a small, semi-autonomous team (not a fully independent lab) for opportunities the core demonstrably cannot deliver.
3. Measure everything in retained and new revenue, not "innovation" outputs.

## 1. Frame the Decision as a Profit Equation

**Profit impact = (Revenue retained + New revenue won) − (Cost of the initiative + Cost of disruption), adjusted for time and probability of success.**

Judge each strategy by how much it moves each term, how fast, and how reliably.

## 2. Follow the Money: Churn Is Probably Your Biggest Lever

In enterprise insurance software, switching costs are very high. Carriers endure painful multi-year migrations to leave a vendor. **If customers are churning anyway, something in the core offering is seriously broken**, such as product gaps, reliability, implementation, support, or an aging architecture.

Illustrative math:
- $400M in recurring revenue at 15% annual churn loses $60M per year.
- Cutting churn by 5 points saves about $20M per year, and that compounds, since retained customers also renew, expand, and serve as references.
- Winning $20M in *new* business typically costs far more in sales and implementation, takes 12–24 months in this industry, and is less certain.

**Implication:** The highest marginal profit per dollar and per month is usually retention. Retention fixes almost always live inside the existing product, systems, and customer-facing teams. An independent lab is structurally the wrong tool for that job.

## 3. Compare the Two Strategies

| Profit driver | Work within the core (CEO) | Independent lab (you) |
|---|---|---|
| **Impact on churn** | High, since it fixes what customers actually use | Low, since the lab builds new things and existing customers keep leaving |
| **Impact on new business** | Moderate; limited if the product is behind competitors | Potentially high if the gap is architectural (e.g., cloud-native, modern APIs) |
| **Time to revenue** | Faster; uses existing customers, sales, and distribution | Slower; must build, then find a path to market |
| **Cost** | Lower marginal cost | Higher; duplicate teams, infrastructure, leadership |
| **Probability of success** | Moderate; inertia can dilute results | Mixed; many corporate labs become "innovation theater" that never scales |
| **Revenue capture** | Built-in sales channel and customer trust | Often fails at transfer back to the core |
| **Upside ceiling** | Incremental | Step-change, if it works |

**Reading the table:** The core wins on near-term, risk-adjusted profit. The lab wins only on upside, and only if it can eventually reach customers through the core's distribution. Distribution is the biggest asset a large incumbent has.

## 4. Where Your Instinct Is Right

"Work within existing systems, procedures, and talent" has a real failure mode. If the processes and culture caused the decline, relying solely on them may produce incremental results at best. That is not the "outsized results" you were hired for. Separation is justified when:
- The needed product requires a different architecture or business model that the core would reject or slow-walk.
- Core incentives (quarterly targets, protecting legacy revenue) actively punish the new idea.
- Speed matters because a competitor is winning deals on capabilities you can't build fast enough internally.

## 5. The Profit-Maximizing Plan

**Phase 1 (first 90 days): Diagnose the revenue leaks.**
- Interview churned and at-risk customers and analyze lost deals. Find out why you lose, in dollars.
- Rank the causes by revenue at stake and cost to fix.
- This gives you data and credibility, and it tells you whether the problem is fixable inside the core.

**Phase 2: Deliver visible wins through the core.**
- Target the top two or three churn drivers with small cross-functional teams that have executive air cover.
- Early retention wins fund later bets and earn the CEO's trust.

**Phase 3: Stand up a small semi-autonomous unit, only where justified.**
- Build it around specific opportunities where the diagnosis showed the core is the constraint.
- Give it autonomy on process, tools, and hiring, but keep it tethered to the core's sales and customers.
- Fund it in stages, with explicit kill criteria (e.g., paying pilot customers by month 9).
- Measure it on revenue, pipeline, and retention, not prototypes or demos.

**Rough allocation:** Most resources go to core fixes, a meaningful minority to adjacent improvements, and a small, stage-gated slice to the autonomous unit. Shift the mix as evidence comes in.

## 6. Don't Ignore the Political Cost

The CEO hired you and holds the opposite view. Opening with "we need an independent lab" invites resistance and can stall everything. That is a real cost in the profit equation.

Instead, pitch in his terms: *"Here's $X in revenue at risk, here's how we recover it through the core, and here's a small, measured bet on the one area where the core can't compete."* That respects his thesis while creating room for yours.

## 7. What Would Change the Answer

Lean harder toward an independent unit if you find that:
- Churn is driven by a fundamental architecture gap the core cannot close (e.g., customers leaving for cloud-native platforms).
- Internal efforts repeatedly stall despite executive support.
- A market window is closing faster than the core can move.

Lean harder toward the CEO's approach if churn traces mainly to execution problems like support, implementation, reliability, or pricing. Those are fixable without new structures.

**Bottom line:** Start where profit is most recoverable (retention, through the core). Earn credibility with results. Then deploy a tightly measured autonomous team for the specific bets the core can't make.

## Turn 2

**User:** Still using profit maximization, how should I decide how big the semi-autonomous team's budget should be?

**Assistant:**

# Short Answer

Set the budget where **the expected profit from the next dollar spent on the team equals what that dollar would earn in the core business**, and release it in stages tied to evidence. In practice:

1. **Cap total spend** by the risk-adjusted value of the opportunity.
2. **Set a floor** at the minimum team that can actually learn fast enough.
3. **Fund in tranches**, releasing more money only when the team hits pre-agreed milestones.
4. **Charge the team the full cost** of the resources it uses, especially talent pulled from the core.

## 1. The Core Principle: Marginal Return vs. Opportunity Cost

Every dollar and engineer given to the new team is taken from somewhere else, most likely the churn fixes from Phase 1. So the hurdle is not "does the team generate a positive return?" but **"does it beat the risk-adjusted return of the best alternative use?"**

- If core churn fixes return $5 for every $1, the team must credibly beat that on a risk-adjusted basis.
- As the core's easiest fixes get done, their marginal return falls, and the case for the team strengthens.
- This is why the budget should be revisited each cycle, not set once.

## 2. Set the Ceiling: Risk-Adjusted Opportunity Value

Estimate what the opportunity is worth if it succeeds, then discount it by the probability that it does.

**Illustrative example: a cloud-native module for mid-size carriers**

| Component | Assumption | Annual profit at maturity |
|---|---|---|
| New business | 10 new carriers × $1.5M ARR × 75% margin | ~$11M |
| Retention | $8M of at-risk ARR saved × 80% margin | ~$6.4M |
| **Total** | | **~$17.5M/year** |

- Over a 5-year horizon, discounted, that is roughly **$50M in value if it succeeds**.
- At a realistic **30% probability of success**, expected value is about **$15M**.
- **Ceiling:** Total cumulative spend should stay well below $15M, ideally under half, to leave a margin for estimation error and a real return.

Be conservative. Internal opportunity estimates are almost always optimistic. Use your Phase 1 customer and lost-deal data rather than market-sizing slides.

## 3. Set the Floor: Minimum Viable Team

Underfunding is often worse than not funding. A team too small to learn quickly spends money with little chance of payoff, which produces the worst of both options.

For enterprise insurance software, a minimum credible early-stage team is typically:
- 1 product lead with decision authority
- 4–6 engineers, including at least one who knows the legacy systems
- 1 designer or UX lead
- 1 insurance domain expert, such as a former carrier operations or underwriting person
- 1 customer-facing lead to secure pilots and connect with the core's sales team

That is roughly 8–10 people. Above about 12 in the early stage, returns diminish sharply. Coordination costs rise, and the constraint is learning speed, not headcount.

## 4. Release Money in Stages

Staged funding raises expected profit. You can stop before most of the money is spent if the evidence is bad, so the downside is limited while the upside stays intact.

| Stage | Goal | Illustrative budget | Gate to next stage |
|---|---|---|---|
| **1. Validate** (~6 months) | Confirm the problem and willingness to pay | $1–1.5M | 3+ carriers commit to paid pilots or signed LOIs |
| **2. Prove** (~9–12 months) | Working product with paying pilots | $3–4M | Pilots live, renewal intent, clear unit economics |
| **3. Scale** (12+ months) | Sell through the core's channel | $6–8M | Pipeline and win rate support ARR targets |

In this example, maximum total spend is about $11M. However, **only about $1.5M is at risk before you have real market evidence.** That is the figure to take to the CEO.

Define kill criteria before each stage starts. The most common failure is continuing to fund a team because of sunk costs.

## 5. Count the Full Cost

The budget line understates the true cost unless you include:
- **Borrowed talent:** Strong engineers pulled from the core carry the value of the churn fixes they would otherwise deliver. This is often the largest hidden cost.
- **Core support time:** Integration, security reviews, legal, and sales engineering.
- **Transfer costs:** Handing the product to core sales and support at Stage 3.
- **Management attention:** Yours and the CEO's.

If the full cost makes the opportunity marginal, it probably isn't worth separating from the core.

## 6. Decision Rules

- **Fund** if the risk-adjusted value clearly exceeds the full staged cost and beats the core's marginal return.
- **Start at the floor, not the ceiling.** Scale spending only as evidence reduces uncertainty.
- **Kill or merge back** any stage that misses its gate, and redeploy the people to the core.
- **Rebalance each quarter** as core returns change.

## 7. How to Present It to the CEO

*"This opportunity is worth about $15M in risk-adjusted value. We'll put $1.5M at risk over six months to test it, with clear kill criteria. More money is released only if paying customers show up. Meanwhile, most resources stay on the retention fixes."*

That framing puts the team in his terms: a small, disciplined bet with limited downside, measured in profit.

## Turn 3

**User:** Keeping with profit maximization, how should I decide which engineers to pull from the core onto the new team?

**Assistant:**

# Short Answer

Don't pull the *best* engineers. Pull the ones with the **highest net gain**: the value they create on the new team minus the value lost when they leave the core, minus transition costs. This is comparative advantage. An engineer who is excellent on the new team but irreplaceable on a churn fix may be the wrong pick. A strong engineer stuck on low-priority work may be the right one.

## 1. The Core Principle

**Net value of moving an engineer = Value on new team − Value lost in core − Transition costs**

- **Value on new team:** How much they increase the odds and speed of hitting the next stage gate.
- **Value lost in core:** What stalls without them, especially retention work, and how hard they are to replace.
- **Transition costs:** Backfill hiring, ramp-up time, disruption to their old team, and political friction.

Rank candidates by net value, not raw talent.

## 2. Estimate Each Engineer's Core Opportunity Cost

For each candidate, ask:
- **What are they working on?** Engineers on top-priority churn fixes have a very high opportunity cost. Engineers on low-priority maintenance or stalled projects have a low one.
- **How replaceable are they?** Could someone else or a new hire do their work within 3–6 months?
- **Knowledge concentration:** Are they the *only* person who understands a critical system? If so, moving them creates operational risk to existing customers, which is a direct churn risk.
- **Backfill cost:** Recruiting cost plus the months their old team runs short-handed.

## 3. Estimate Each Engineer's Value on the New Team

The value depends on the stage. In **Stage 1 (Validate)** you need:
- **Versatile builders** who can prototype quickly and work with ambiguity, rather than deep specialists.
- **Comfort with customers.** Engineers who can join carrier conversations speed up learning.
- **At least one legacy "bridge" engineer** who knows the core systems well enough to integrate. This person also makes the eventual handoff back to core sales and support far cheaper.
- **Modern-stack skills** if the opportunity depends on a new architecture.

Deep specialists and scaling expertise matter more in Stages 2 and 3. Add them when the gates are met.

## 4. Illustrative Scoring

Annual value figures are rough estimates in profit terms. Precision matters less than making the trade-offs explicit.

| Engineer | Current role | Value on new team | Value lost in core | Transition cost | Net | Decision |
|---|---|---|---|---|---|---|
| **A** | Star; sole expert on rating engine; leading a top churn fix | $1.2M | $2.0M | $0.2M | **−$1.0M** | Don't pull; use as a ~10% advisor |
| **B** | Strong; modern cloud skills; on low-priority maintenance | $0.9M | $0.2M | $0.1M | **+$0.6M** | Pull |
| **C** | Mid-level; knows legacy integrations; one of three experts on them | $0.6M | $0.2M | $0.1M | **+$0.3M** | Pull as the bridge engineer |
| **D** | Senior architect; widely respected | $0.8M | $0.9M | $0.2M | **−$0.3M** full-time | Part-time design reviews only |
| **E** | Talented but restless; likely to leave within a year | $0.7M | $0.1M* | $0.1M | **+$0.5M** | Pull |

*\*Engineer E's expected core value is low because they may quit. Moving them to more engaging work can keep someone who would otherwise leave, which is a real profit gain.*

## 5. Pull Internally or Hire Externally?

Compare the full cost of each source for each role.

| Pull from core when | Hire externally when |
|---|---|
| The role needs legacy system or insurance domain knowledge | The core lacks the skill entirely (e.g., cloud-native architecture) |
| The engineer's core opportunity cost is low | Every internal candidate has high core value |
| Credibility with core teams matters for later transfer | You need fresh thinking not shaped by legacy constraints |
| | An outside hire's 3–6 month ramp-up is cheaper than the lost core output |

A mix usually maximizes value: internal engineers for integration and credibility, external hires for missing capabilities.

## 6. Factors That Change the Math

- **Motivation:** Volunteers are markedly more productive than conscripts in ambiguous, early-stage work. Among candidates with similar net value, prefer those who want the assignment.
- **Political cost:** Taking a manager's best person without compensation creates resistance that slows the core and later handoffs. **Fund backfills from the new team's budget** so the full cost is visible and the core isn't penalized.
- **Return path:** Guarantee engineers a role back in the core if the team is killed at a stage gate. This lowers the perceived risk for strong candidates and keeps their knowledge in the company.
- **Staging:** Don't pull the full team on day one. Stage 1 needs fewer people. Add engineers as gates are met, which keeps core opportunity costs low while the bet is unproven.

## 7. Decision Rules

1. **Protect the churn fixes.** Engineers critical to top retention work stay put. At most, they give limited advisory time.
2. **Never create a single point of failure.** Don't move the only expert on a system existing customers depend on.
3. **Rank by net value,** favoring volunteers when values are close.
4. **Include one legacy bridge engineer** from the start.
5. **Hire externally for missing skills** rather than stripping the core.
6. **Charge backfills to the new team's budget.**
7. **Re-evaluate at each stage gate.** Opportunity costs change as core priorities shift.

## 8. How to Present It to Core Leadership

*"We're taking engineers whose move creates the most value and costs the core the least. No one critical to retention work is leaving, we're funding every backfill, and anyone can return if the team is shut down."*

That frames the moves as a disciplined allocation of scarce talent, not a raid on the core.

## Turn 4

**User:** Sticking with profit maximization, how should I set up incentives and compensation for the people on the new team?

**Assistant:**

# Short Answer

Pay people in proportion to the **profit they help create**, at the **lowest cost that attracts, motivates, and retains** them, and in a way that **doesn't damage the core**. In practice:

1. **Keep base salaries at parity with the core.**
2. **Pay team bonuses at each stage gate,** tied to profit-linked metrics that are hard to game.
3. **Offer a capped long-term share** of the product's profit, paid only if it succeeds commercially.
4. **Reward honest kill decisions** so people surface bad news early.
5. **Give core sales and support a stake** so the product actually reaches customers.

## 1. The Core Principle: Align Incentives With Profit, Not Activity

The company (principal) wants profit. The team (agents) will optimize whatever you measure and pay for. The risks are predictable:
- **Rewarding outputs** such as features shipped or demos built gets you outputs, not revenue.
- **Rewarding only success** encourages people to hide bad news and keep failing projects alive, which is the most expensive outcome.
- **Overpaying relative to the core** creates resentment that slows the core, the integration, and the eventual handoff.

**Test for any incentive:** Does it increase expected profit by more than it costs, including its effects on the core?

## 2. The Compensation Structure

| Component | Purpose | Design |
|---|---|---|
| **Base salary** | Attract and retain | Parity with core levels; market adjustments only for scarce external skills |
| **Stage-gate bonuses** | Speed toward evidence | Team-based, paid when gates are met |
| **Long-term value share** | Tie rewards to actual profit | Capped share of the product's gross profit, vesting over 2–3 years |
| **Kill-decision reward** | Stop wasting money early | Small bonus for evidence-based recommendations to stop or pivot |
| **Non-monetary rewards** | Low-cost motivation | Autonomy, visibility, and career advancement |

### Why base parity matters
- Engineers moving from the core are paid consistently, which makes the return path easy.
- Core staff don't see the new team as a privileged class.
- Upside comes from *results*, not from being assigned to the team.

External hires with scarce skills may need market premiums. Use sign-on bonuses where possible rather than permanently higher bases, and be transparent about why.

## 3. Choose Metrics That Track Profit and Resist Gaming

| Stage | Bad metric (gameable) | Good metric (profit-linked) |
|---|---|---|
| **1. Validate** | Number of customer interviews | Paid pilots or signed LOIs with budget attached |
| **2. Prove** | Features shipped | Pilots live, renewal intent, unit economics within target |
| **3. Scale** | Bookings | Net ARR after discounts, retained for 12+ months |

Guardrails:
- **Pilots must be paid.** Free pilots are too easy to get and say little about demand.
- **Measure revenue net of discounts** so the team can't buy growth.
- **Defer part of the payout** until customers renew, which aligns the team with retention.

## 4. Make Incentives Mostly Team-Based

Early-stage outcomes are collective. Individual metrics encourage people to optimize their own piece at the expense of the whole.
- Pay about **80% of variable pay on team results**.
- Keep about **20% for individual discretion**, judged by the team lead on contribution and collaboration.

## 5. Size the Incentive Pool

A reasonable rule is to spend **a small fraction, around 5–10%, of the value created** on incentives, paid mostly when that value materializes.

**Illustrative example** (9-person team, ~$180K average base, ~$1.6M total base):

| Component | Design | Payout if earned |
|---|---|---|
| Stage 1 gate bonus | ~10% of base | ~$160K |
| Stage 2 gate bonus | ~15% of base | ~$240K |
| Long-term share | 5% of product gross profit, years 2–4, capped at $3M | Up to ~$875K/year |
| Kill-decision reward | ~5% of base, only for timely, evidence-based calls | ~$80K |

- **If the product succeeds,** total incentives of about $3M are roughly 6% of the ~$50M value created, which is well within the target range.
- **If it fails early,** the company pays at most a small Stage 1 bonus or kill reward.
- **The cap** protects against windfalls driven by factors outside the team's control and limits resentment in the core.

Keep the kill reward well below the success rewards so it encourages honesty without making failure attractive.

## 6. Why Rewarding Kill Decisions Maximizes Profit

Staged funding only works if bad news surfaces quickly. Without protection, team members have every reason to keep a failing project alive: jobs, bonuses, and reputations depend on it.
- A team that recommends stopping after Stage 1 saves the company millions in Stage 2 and 3 spending.
- Pairing the kill reward with the **guaranteed return path** means honest reporting costs team members nothing.

## 7. Extend Incentives to the Core

The new product earns profit only if the core helps sell, integrate, and support it. Those people need a stake too.
- **Core sales:** Pay commission on the new product at least equal to the legacy product, with an accelerator for the first few deals. Otherwise reps will keep selling what they know.
- **Bridge and advisory engineers:** Include part-time contributors in gate bonuses in proportion to their involvement.
- **Support and implementation teams:** Recognize or reward successful pilot deployments, since these drive renewal.

This keeps the new team from being seen as "the people who get rich," which lowers political friction.

## 8. Don't Overlook Cheap Motivators

For people who chose ambiguous, high-risk work, non-monetary rewards often deliver more motivation per dollar than cash:
- Real decision authority over product and process.
- Direct access to customers and to executives, including the CEO.
- Visible credit for results.
- Faster promotion paths for strong performers, whether they stay on the team or return to the core.

## 9. Practical Constraints

- **Work with HR and Finance early.** Large companies often have rigid pay bands and bonus rules. Phantom equity or product-level profit sharing may need legal and accounting review.
- **Document everything up front,** including metrics, payouts, caps, and what happens if the team is killed. Ambiguity breeds mistrust and gaming.
- **Review the plan at each stage gate** as metrics and team composition change.

## 10. Decision Rules

1. **Keep base salaries at core parity.** Pay for results, not assignment.
2. **Tie variable pay to paid, retained revenue**, never activity.
3. **Make most variable pay team-based.**
4. **Cap the upside** and keep total incentives around 5–10% of value created.
5. **Reward timely kill decisions** and guarantee a return path.
6. **Give core sales and support a stake** in the product's success.
7. **Use autonomy and visibility** as low-cost motivators.

## 11. How to Present It to the CEO

*"The team's base pay matches the core. They earn more only if the product generates real, retained profit, and total incentives are capped at a small share of the value created. We also reward them for stopping early if the evidence is bad, which protects our money. And core sales gets paid to sell it, so the product actually reaches customers."*

This presents the plan as disciplined, profit-aligned, and fair to the rest of the company.

## Turn 5

**User:** What should we do?

**Assistant:**

# Recommendation

**Don't build an independent lab. Start by fixing churn through the core, then place a small, staged bet with a semi-autonomous team only where the evidence shows the core can't compete.** This aligns with the CEO's thesis, gives you the structural freedom you believe breakthrough work needs, and puts money first where the profit is most recoverable.

The plan below brings the previous answers together into a sequence.

## Phase 1: Diagnose (Days 1–90)

**Goal:** Find out, in dollars, why customers leave and why you lose deals.

- **Quantify the leak:** Churned ARR, at-risk ARR, lost-deal value, and win rate by segment and competitor.
- **Talk to customers:** Interview 15–25 churned, at-risk, and lost-deal accounts. Ask why they left, what they chose instead, and what would have kept them.
- **Rank the causes** by revenue at stake and cost to fix.
- **Classify each cause:**
  - *Execution problems* (support, implementation, reliability, pricing): fixable in the core.
  - *Structural problems* (architecture gaps, missing capabilities competitors have): candidates for the new team.
- **Build relationships** with core leaders, especially sales, product, and engineering. You will need them in every later phase.

**Deliverable:** A one-page "revenue at risk" analysis presented to the CEO, with a prioritized fix list.

## Phase 2: Deliver Core Wins (Months 3–9)

**Goal:** Recover revenue quickly and earn credibility.

- Attack the top two or three churn drivers with small cross-functional teams that have executive support.
- Set explicit targets, such as cutting churn by 3–5 points or saving specific at-risk accounts.
- Report results in dollars retained.

**Why first:** Retention fixes typically have the highest return per dollar. Early wins also fund later bets and build the trust you need to propose something bolder.

## Phase 3: Launch the Semi-Autonomous Team (Months 4–6 onward, only if justified)

**Launch only if** Phase 1 shows a structural gap that is costing meaningful revenue and that the core can't close.

| Decision | Approach |
|---|---|
| **Budget** | Cap total spend well below the risk-adjusted opportunity value. Put only Stage 1 funding (e.g., ~$1–1.5M) at risk up front. |
| **Stages** | Validate → Prove → Scale, with kill criteria agreed before each stage |
| **Team** | 8–10 people. Pick engineers by net value, not raw talent. Include one legacy bridge engineer. Hire externally for missing skills. Never pull someone critical to churn fixes or a sole expert. |
| **Backfills** | Charged to the new team's budget |
| **Compensation** | Base pay at core parity. Team bonuses at stage gates. A capped long-term profit share. A reward for honest kill calls. A guaranteed return path. |
| **Core ties** | Core sales earns full commission on the new product. Advisory engineers share in gate bonuses. |

## Ongoing: Govern by Profit

Review a simple dashboard each quarter with the CEO:

- **Core:** Churn rate, ARR retained, win rate, and progress on top fixes.
- **New team:** Stage-gate status, paid pilots, renewal intent, net ARR, and spend against the cap.
- **Reallocation:** Is the next dollar worth more in the core or the new team? Shift resources accordingly.

## Your Next Two Weeks

1. **Meet the CEO.** Don't lead with the lab. Say something like: *"I want to start by quantifying exactly where we're losing revenue and why. In 90 days I'll bring you a prioritized plan to recover it, mostly through the core, plus any areas where we may need a different approach."*
2. **Request data** on churn, at-risk accounts, lost deals, and win/loss by competitor.
3. **Schedule customer conversations,** starting with recently churned accounts.
4. **Meet core leaders** in sales, product, engineering, and customer success to understand their view of the problems and to identify potential allies.
5. **Quietly note candidate engineers** and possible opportunities, but make no moves until the diagnosis is done.

## What Would Change This Plan

- **Structural problems dominate churn and lost deals** (e.g., customers leaving for cloud-native platforms): Move up the semi-autonomous team and fund it more aggressively.
- **Churn is mostly execution:** Keep resources in the core and delay or skip the new team.
- **Core efforts repeatedly stall despite executive support:** Strengthen the case for more autonomy.
- **The CEO resists any separate structure:** Run the new team's Stage 1 as a "special project" inside the core and let the results make the case.

## Bottom Line

Start where profit is easiest to recover, prove results in dollars, and use that credibility to place a disciplined, staged bet on the future.

## Outcome summary (sent to Jev)

The assistant recommends against an independent innovation lab. Instead, fix churn through the core organization first, then place a small, staged bet on a semi-autonomous team only where evidence shows the core cannot compete. The CEO is more right about where the money is, and the user is more right about how breakthrough work gets built.

The main reason is profit per dollar and per month. Switching costs in insurance software are high, so churn signals something seriously broken in the core offering. Retention fixes usually offer the highest, fastest, most reliable return, and they live inside the existing product and teams. Leading with a lab would also provoke the CEO's resistance.

The plan has three phases:

- **Diagnose (first 90 days).** Quantify churned and at-risk revenue and lost deals, interview 15–25 customers, and rank causes by revenue at stake. Classify each cause as an execution problem (fixable in the core) or a structural one.
- **Deliver core wins (months 3–9).** Target the top churn drivers and report results in dollars retained.
- **Launch a semi-autonomous team, only if justified.** Keep it to 8–10 people, tethered to core sales. Cap spending below the risk-adjusted opportunity value and put only about $1–1.5M at risk initially. Fund it in stages with pre-agreed kill criteria.
  - Pick engineers by net value, never pulling sole experts or people critical to churn fixes, and charge backfills to the team's budget.
  - Keep base pay at core parity, with team stage-gate bonuses, a capped profit share, rewards for honest kill calls, a guaranteed return path, and full commission for core sales.

Caveats: if structural gaps dominate, fund the team sooner and more aggressively. If churn is mostly execution, delay or skip it. If core efforts stall, push for more autonomy. If the CEO resists, run Stage 1 as an internal special project.
