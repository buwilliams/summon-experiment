# economic/churn-cause/testC

Model: claude-opus-5-5 · 2026-09-24T14:52:52.450402+00:00

## Turn 1

**User:** Use profit maximization to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Churn Diagnosis Through a Profit-Maximization Lens

## Reframe the question

Profit maximization doesn't ask which VP is right. It asks **where the next dollar produces the most retained gross profit, and how fast.** Both VPs are proposing investments in their own function, so neither has a neutral view. Your job is to make the data arbitrate.

The value of stopping a churned account is:

> **Retained profit = ARR × gross margin × expected additional years of life − cost of the intervention**

So the real questions are:

1. Which cause accounts for the most **churned gross profit**, not the most churned logos?
2. Which fix costs less per dollar retained?
3. Which fix pays back sooner?

## Tests that separate the two hypotheses

You can get most of this from data you already have (CRM, usage telemetry, implementation records, renewal history).

| Test | Points to **product gaps** if... | Points to **implementation/service** if... |
|---|---|---|
| **When customers churn** | At the 2nd or 3rd renewal or later, after they were fully live | At the first renewal, or before full go-live |
| **Adoption before churning** | Churned accounts used the product deeply, then left | Churned accounts had low usage, modules never activated, or were still partly on legacy systems |
| **Where they went** | To a named competitor with better analytics/AI | To the status quo, in-house tools, or their old vendor (a failure to realize value) |
| **New-logo win/loss** | You're also losing new deals on analytics/AI | Win rates are stable while churn rises. Buyers like the product; customers don't get value from it |
| **What changed 18 months ago** | A competitor launched AI/analytics features | Implementation staffing, process, partners, or deal mix changed (bigger or more complex carriers) |
| **Implementation duration vs. churn** | Weak correlation | Long implementations strongly predict churn |
| **Support signals** | Tickets are feature requests | Tickets are bugs, integration failures, slow response, or escalations |

**Discount stated exit reasons.** "Your competitor has better AI" is a socially easy reason to give, even when the real story is "we spent 14 months implementing and never got value." Behavioral data (usage, timing, destination) beats survey answers.

## Weight by dollars, not logos

Segment churned ARR by the pattern it fits. For example:

- 60% of churned ARR came from customers who churned at first renewal with less than 50% module adoption → **implementation problem**
- 25% came from fully adopted customers who left for a competitor's AI → **product problem**
- 15% came from M&A, budget cuts, or carrier consolidation → **not addressable**

Then compare the cost of each fix against the gross profit it could recover.

## My prior, and why

Absent your data, I'd expect the **implementation/service hypothesis to account for more of the churned profit**, for four reasons:

1. **Regional carriers** tend to have thin IT teams and complex policy-admin and core-system integrations. Long implementations hurt them especially, and they're rarely the most aggressive AI adopters.
2. **The two causes aren't independent.** A customer who never reaches full value can't benefit from better analytics. Features shipped to half-implemented customers don't retain them. Fixing onboarding raises the return on every future roadmap dollar. The reverse isn't true.
3. **Speed and cost.** Implementation fixes (methodology, templates, pre-built integrations, staffing, go-live criteria) typically take months and cost less than a feature race against better-funded competitors that are also moving.
4. **Hidden profit upside.** Shorter implementations pull revenue recognition forward, improve services margin, shorten CAC payback, and create referenceable customers who help sales.

**The case for product is stronger than it looks on churn alone.** Analytics and AI investment also affects new-logo win rate and pricing power. If win/loss data shows you losing new deals on those features, the product investment has a second revenue stream, and the retention-only math undervalues it. Count that in.

## What to do

**1. Run a 4–6 week diagnostic.** Owned by you or finance, not either VP. Produce the churned-ARR segmentation above, plus win/loss analysis and cohort curves by implementation duration.

**2. Make no-regret moves now, without waiting for the diagnostic.**
- Flag every in-flight implementation running past plan, and every live account with low adoption that renews in the next 12 months. These are your highest expected-value saves. Assign exec sponsors and recovery plans.
- Define "full value" concretely (for example, specific modules live, claims volume processed, a target cycle-time improvement) and start measuring time-to-value.

**3. Set the decision rule in advance, so the data decides rather than politics.**
- If most addressable churned profit is value-realization failure, **prioritize implementation and service.** Keep the roadmap focused on features that reduce implementation friction (integrations, configuration tooling, migration utilities).
- If most comes from fully adopted customers defecting to competitors, and win/loss confirms it, **accelerate targeted product investment.** Aim at the specific analytics/AI capabilities cited in losses, not a general feature race.
- If it's mixed, which is likely, **fund both in proportion to recoverable profit per dollar,** with implementation sequenced first because it multiplies the payoff of features.

**4. Track the right metrics.**
- Gross revenue retention by cohort
- Time-to-first-value and time-to-full-value
- Adoption depth at renewal
- Win rate on deals where analytics/AI is a stated criterion

**5. Revisit in two quarters.** If implementation fixes are working, first-renewal churn in new cohorts should fall first. If it doesn't, the product hypothesis gains weight.

## Bottom line

You can't know which belief is right without segmenting churned revenue by behavior. The evidence you've described (long implementations, customers never reaching full value) plus the dependency argument makes the service/onboarding fix the likelier first move.

**Fix time-to-value first, because every future feature depends on it, and let the churned-ARR segmentation tell you how much to put behind the roadmap.**

## Turn 2

**User:** Sticking with profit maximization, how should I decide how much to spend saving each of those at-risk renewals?

**Assistant:**

# How Much to Spend Saving Each At-Risk Renewal

## The core rule

Spend on an account only up to the **expected profit the intervention creates**, not the account's total value.

> **Maximum justified spend = Uplift × Value of the retained customer**

- **Uplift (ΔP)** = P(renew *with* intervention) − P(renew *without* it)
- **Value** = present value of the gross profit the customer generates over its remaining expected lifetime, if saved

Then spend where the return per dollar is highest, and stop when the next dollar earns less than your alternative uses of it, such as the onboarding fix.

## Step 1: Value each account correctly

Use **gross profit, not ARR**, over the remaining expected lifetime, discounted:

> **Value = Σ (ARR × gross margin + expected expansion − account-specific cost to serve) ÷ (1 + r)^t**

Adjust for factors specific to regional carriers:

- **Add** reference value. Regional carriers talk to each other, share consultants, and meet at the same conferences, so a public failure costs you pipeline. Estimate it conservatively: likely deals affected × win-rate impact × deal value.
- **Add** expansion potential if the carrier is growing, acquiring, or hasn't bought modules it needs.
- **Subtract** heavy cost to serve. Some accounts consume so much support and custom work that their true margin is thin or negative.
- **Subtract** consolidation risk. If the carrier is likely to be acquired, the expected lifetime is shorter no matter what you do.

## Step 2: Estimate uplift, not risk

This is the most common mistake. **High churn risk does not mean a high return on intervention.** Account types differ sharply:

| Account type | Baseline renewal | With intervention | Uplift | Implication |
|---|---|---|---|---|
| **Persuadable** (stalled implementation, fixable problems) | 40% | 75% | High | Invest heavily |
| **Lost cause** (new CIO has already chosen a competitor, carrier being acquired) | 10% | 15% | Low | Minimal spend; exit gracefully and protect the reference |
| **Sure thing** (happy, fully adopted) | 92% | 95% | Low | Don't spend save money here |
| **Unprofitable** (negative margin even if saved) | Any | Any | Negative value | Reprice or let go |

Estimate uplift from:

- Past save attempts. What happened to similar accounts when you intervened, versus when you didn't?
- The nature of the problem. Churn caused by a failed implementation is often fixable. Churn caused by a missing feature you won't ship in time usually isn't.
- CSM judgment, calibrated over time against actual outcomes.

## Step 3: A worked example

Assumptions: 10% discount rate. Annuity factors of 3.79 for 5 years and 2.49 for 3 years.

| | **Account A** | **Account B** | **Account C** |
|---|---|---|---|
| ARR | $300k | $80k | $150k |
| Gross margin | 75% | 50% (support-heavy) | 75% |
| Annual gross profit | $225k | $40k | $112k |
| Remaining life if saved | 5 yrs | 3 yrs | 5 yrs |
| **Value (PV)** | **~$853k** | **~$100k** | **~$426k** |
| Baseline renewal | 40% | 20% | 90% |
| With intervention | 70% | 30% | 95% |
| **Uplift** | 30 pts | 10 pts | 5 pts |
| **Breakeven spend** | **~$256k** | **~$10k** | **~$21k** |

Breakeven is the ceiling, not the target, for two reasons: uplift estimates are uncertain, and the same money has other uses. Apply a **hurdle rate**. If you require a 3:1 expected return, Account A justifies roughly $85k of save effort, Account B roughly $3k, and Account C roughly $7k.

A does not get the most because it is the biggest account. It gets the most because it combines high value with high uplift. C is twice B's size but merits only modestly more.

## Step 4: Allocate under constraints

Your real constraint usually isn't cash. It's **scarce people**: senior implementation engineers, solution architects, executive sponsors' time.

1. List at-risk renewals and estimate the expected profit created per unit of the scarce resource: (Uplift × Value) ÷ hours or dollars required.
2. Rank accounts by that ratio.
3. Fund down the list until you run out of capacity or the next account falls below your hurdle rate.
4. Compare the marginal save against **systemic fixes**. If an engineer's hour spent on a reusable integration template prevents churn across ten future accounts, it may beat any single save. Don't let firefighting consume the capacity needed to fix the root cause identified in the diagnostic.

## Step 5: Price each intervention at its true cost

Save tactics differ a lot in true cost:

- **Discounts are the most expensive tactic and the most overused.** A 20% discount on a $300k account is $60k *per year*. It usually persists and anchors future renewals, so its PV over 5 years is roughly $227k. It also rarely fixes the problem if the customer isn't getting value. They simply churn next year at a lower price.
- **Services credits and implementation rescue** (free professional services, dedicated engineers, a go-live push) are one-time costs that address the actual cause. They usually deliver more uplift per dollar for value-realization churn.
- **Roadmap commitments** carry hidden costs: they distort your product priorities, and if you miss the date, you lose the customer and your credibility. Price them in.
- **Executive attention** is cheap in cash but limited. Reserve it for accounts at the top of your ranking.

## Step 6: Spend in stages to buy information

Uplift is uncertain, so don't commit the full budget at once.

1. **Diagnose cheaply:** an executive call, an adoption review, a health assessment. This refines your uplift estimate.
2. **Escalate** only if the diagnosis shows the problem is fixable and the customer is engaged.
3. **Set a stop-loss.** If milestones slip or the customer disengages, cut spend and shift to a graceful exit that protects the reference.

Early, cheap steps have option value. They tell you whether the big spend is worth making.

## Guardrails

- **Don't train customers to threaten churn.** If threatening to leave reliably produces discounts, more customers will threaten. Favor value-restoring concessions such as services and enablement over price concessions, and require something in return: multi-year terms, case studies, or adoption commitments.
- **Measure real uplift.** Track save outcomes against your predictions. Where feasible, compare similar at-risk accounts that did and didn't get intervention. Otherwise you'll credit saves to accounts that would have renewed anyway.
- **Let unprofitable customers go.** Profit maximization sometimes means reducing churn *spend*, not increasing it. An account with negative margin is cheaper to lose, or to reprice until it's profitable.

## Bottom line

For each at-risk renewal, ask: **"How much does our intervention change the odds, multiplied by what the customer is worth in gross profit?"** Spend up to a fraction of that set by your hurdle rate. Rank accounts by return on your scarcest resource. Favor fixes that address the root cause over discounts. And keep enough capacity for the systemic onboarding fixes that reduce the number of accounts needing rescue in the first place.

## Turn 3

**User:** Staying with profit maximization, how should I split my team's capacity between rescuing individual at-risk accounts and building the systemic onboarding fixes?

**Assistant:**

# Splitting Capacity Between Rescues and Systemic Fixes

## The core rule

Don't pick a ratio in advance. **Put every possible use of your team's time on one list, ranked by risk-adjusted, time-discounted profit per hour, and fund from the top down.** The split is whatever falls out.

At the optimum, the last hour spent on rescue and the last hour spent on systemic fixes earn the same return. If rescue hours earn more at the margin, shift capacity toward rescue. If systemic hours do, shift it the other way.

The two kinds of work pay off differently, so they need to be measured on a common basis.

## Step 1: Value rescue hours

You already have this from the renewal ranking:

> **Rescue value per hour = (Uplift × Account value) ÷ Hours required**

Rescue returns are:
- **Front-loaded.** The payoff arrives at the renewal date.
- **Fairly certain.** You know the account, the problem, and the deadline.
- **Steeply diminishing.** The top few accounts are worth a lot per hour, and the tail is worth little.

## Step 2: Value systemic hours

Systemic fixes include integration templates, go-live criteria, implementation playbooks, configuration tooling, and time-to-value tracking. Their value comes from many future accounts, so the formula has more terms:

> **Systemic value = P(fix works) × discount for delay × [Future accounts affected × Churn reduction per account × Account value + Other profit gains + Avoided future rescue cost]**

Divide by the hours required to get value per hour.

The "other profit gains" and "avoided rescue cost" terms are easy to forget and often large:
- **Other profit gains:** shorter implementations pull revenue recognition forward, improve services margin, and shorten CAC payback.
- **Avoided rescue cost:** every account that onboards well is one you won't need to rescue in 18 months. This is how systemic work compounds.

Systemic returns are:
- **Delayed.** They start with the next implementation cohort and show up in renewals a year or more later.
- **Uncertain.** The fix might not work as designed.
- **Durable and reusable.** One build pays off across every future cohort.

## Step 3: A worked example

Assume 10 FTEs, roughly 16,000 productive hours per year, and an average account value of about $400k in PV gross profit.

**Systemic fix: pre-built policy-admin integration template**
- 1,500 hours to build
- Affects 12 new implementations per year for 3 years, so 36 accounts
- Cuts churn probability by 8 points per account: 36 × 0.08 × $400k ≈ $1.15M
- Faster go-live and lower implementation cost: +$300k
- Avoided future rescues: +$150k
- Subtotal: about $1.6M
- × 60% probability it works × 0.85 delay discount ≈ **$815k**
- **≈ $540 per hour**

**Combined ranking (illustrative):**

| Use of capacity | Hours | Expected profit | $/hour |
|---|---|---|---|
| Go-live criteria + implementation playbook (systemic) | 300 | $350k | ~$1,170 |
| Account A rescue | 400 | $256k | ~$640 |
| Integration template (systemic) | 1,500 | $815k | ~$540 |
| Account D rescue | 250 | $110k | ~$440 |
| Configuration tooling (systemic) | 2,500 | $700k | ~$280 |
| Account B rescue | 150 | $10k | ~$67 |
| ... | | | |

Fund down the list until you run out of hours. In this example, the top systemic fixes outrank most rescues. That's common when first-renewal churn from failed implementations dominates, as the diagnostic likely showed. Your numbers will differ. The method is what matters.

## Step 4: Price the cost of delay

Rescues have hard deadlines, so they feel urgent. Systemic fixes feel like they can wait. **They can't, for free.** Every quarter you delay, another cohort onboards the old way.

> **Cost of delay per quarter = New implementations per quarter × Churn reduction × Account value**

Example: 4 implementations per quarter × 0.08 × $400k ≈ **$128k per quarter**, plus the extra rescue work those accounts will need later.

Write this number down. It makes the invisible cost of postponing systemic work as concrete as a named account's renewal date.

## Step 5: Correct for the firefighting bias

Organizations systematically over-invest in rescue, because rescue work is:
- **Visible:** a named account, a known executive, a date.
- **Rewarded:** saves get celebrated; prevented churn is invisible.
- **Urgent:** deadlines pull capacity away from important-but-not-urgent work.

This creates a trap. Too little systemic work means more accounts go bad, which means more rescues, which leaves even less capacity for systemic work. Churn stays high while the team works harder. Your doubled churn may be partly a symptom of this cycle.

Counter it structurally:
- **Ring-fence systemic capacity.** Assign named people with protected time. Set an explicit rule for when rescue can borrow from them, such as only for accounts above a set $/hour threshold, and require VP sign-off.
- **Make every rescue produce a reusable asset.** When you fix a stalled integration for Account A, turn the fix into a template, checklist, or known-issues entry. This turns rescue spending into partial systemic investment.
- **Credit prevention.** Report time-to-value and first-renewal retention for new cohorts alongside saves.

## Step 6: Shift the split over time

The optimal split isn't static.

- **Now:** If you face a renewal cliff with many high-value, high-uplift accounts, rescue may deserve a large share. Still, fund the cheapest, highest-return systemic fixes (go-live criteria, playbooks) immediately. They cost little and start the compounding.
- **Next 2–3 quarters:** As the rescue backlog clears and systemic fixes prove out in new cohorts, shift capacity toward systemic work.
- **Steady state:** Rescue demand should fall because fewer accounts go bad. The rescue share shrinks naturally.

Re-rank the combined list every quarter using updated renewal risk, uplift estimates, and early results from systemic pilots.

## Step 7: Account for real-world frictions

- **People aren't interchangeable.** Your best rescuers (relationship-heavy, calm under pressure) may not be your best builders (methodical, product-minded). Allocate by comparative advantage, not just headcount.
- **Context switching is costly.** Someone splitting time between both rarely does either well. Where possible, assign people mostly to one track and rotate periodically so builders see real customer pain.
- **Pilot systemic fixes before scaling.** Test the integration template on the next two or three implementations. This raises the "probability it works" term cheaply before you commit the full build.

## Step 8: Question the fixed-capacity assumption

The split question hides a scale question. If the marginal hour on *both* tracks earns well above the fully loaded cost of an hour, **you're under-resourced**, and profit maximization says to add capacity.

- **Contractors or partners for rescue surges.** This is temporary, deadline-driven work.
- **Permanent hires for systemic work.** Institutional knowledge matters there.

Bring the ranked list to your CFO. Showing that the next 2,000 hours would earn $400+ per hour against a cost of about $100 per hour makes a strong case.

## Bottom line

Rank rescues and systemic fixes on a single list by risk-adjusted, discounted profit per hour, and fund from the top. Price the cost of delaying systemic work so it competes fairly with deadline-driven rescues. Ring-fence capacity to resist the firefighting trap, and expect the balance to shift toward systemic work as fixes prove out and rescue demand falls. If both tracks earn well above what an hour costs, the answer isn't a better split. It's more capacity.

## Turn 4

**User:** Still using profit maximization, how do I get my CFO to fund the extra capacity instead of pushing us to just reprioritize within the team we have?

**Assistant:**

# Getting Your CFO to Fund Extra Capacity

## Start from the CFO's perspective

Your CFO isn't resisting for no reason. "Reprioritize within the team" is the correct answer whenever the marginal hour earns less than it costs, or less than the same dollars would earn elsewhere in the company. Headcount requests often come with inflated benefits, and teams rarely prove they've squeezed out low-value work first.

So don't argue for more resources. Show that under the CFO's own profit-maximization logic, **funding this capacity beats both reprioritizing and the company's other uses of the money.** To agree, the CFO has to believe five things:

1. You've already reprioritized, so the extra capacity isn't covering inefficiency.
2. The incremental work earns well above its cost.
3. The numbers are credible, not advocacy.
4. The downside is limited if you're wrong.
5. You'll be accountable for results.

Build the case around those five.

## 1. Prove you've already reprioritized

Lead with this. It disarms the default objection. Show:

- **The ranked list and the cut line.** Here is everything we could do, ranked by profit per hour, and here is where our current capacity runs out.
- **What you stopped doing.** Low-uplift rescues you've dropped, low-value activities you've cut (routine check-ins with healthy accounts, custom reports nobody reads), discounts you've refused.
- **How you're capturing leverage.** Rescues now produce reusable assets. Systemic capacity is ring-fenced.

The message: we've done the reprioritizing. What's left below the line is still valuable work that isn't getting done.

## 2. Make the case on marginal returns, not averages

Don't cite average ROI for customer success. Show the **specific work the new capacity would do**: the items just below the cut line, with the expected return on each.

Illustrative ask: **3 FTEs plus contractor budget, about $550k per year fully loaded, adding roughly 5,500 hours.**

| Work unlocked (currently below the line) | Hours | Risk-adjusted profit | $/hour |
|---|---|---|---|
| Configuration tooling (systemic) | 2,500 | $700k | ~$280 |
| Next 8 mid-tier rescues | 1,800 | $540k | ~$300 |
| Time-to-value instrumentation + early-warning system | 1,200 | $360k | ~$300 |
| **Total** | **5,500** | **~$1.6M** | **~$290** |

Against a cost of about $100 per hour, that's roughly **3:1 in year one**. The systemic items keep paying in later years.

Use the actual next items on your list, not your best ones. Your best items should already be funded. If you present the top of the list as the reason for new capacity, a sharp CFO will notice.

## 3. Make the numbers credible

Your uplift and value estimates are the weakest part of the case, and the CFO knows it. Take these steps:

- **Co-build the model with FP&A.** Use finance's gross margins, discount rate, and churn baselines, not your own. A model finance helped build is one finance defends.
- **Use conservative inputs.** Haircut uplift estimates and use the low end of account value. Say so explicitly.
- **Show sensitivity and breakeven.** "Even if uplift is half our estimate, the investment returns 1.5:1. It breaks even if uplift is only a third of what we expect." This is often the most persuasive line in the whole case, because it doesn't require the CFO to trust your point estimate.
- **Show your track record.** How accurate were your past save predictions? If you've been tracking actual outcomes against estimates, as suggested earlier, use the data. If you haven't, start now and acknowledge it.
- **Show early evidence.** If the go-live criteria or playbook are already in use, share early results from the first cohort, even if they're partial.

## 4. Translate into the CFO's metrics

Customer success metrics mean little to a CFO. Restate the case in terms they own:

- **Gross and net revenue retention.** Show the current trajectory and the projected improvement. In SaaS, GRR and NRR drive valuation multiples, so a few points of retention can be worth far more in enterprise value than the annual profit alone suggests.
- **Forecast reliability.** High, unpredictable churn makes revenue forecasts miss. Reducing it makes the CFO's forecasts more reliable.
- **Revenue recognition and cash.** Faster implementations bring revenue in sooner and improve services margin.
- **CAC payback and LTV:CAC.** Every churned customer wastes the acquisition cost already spent on them. Retention improves the economics of the whole go-to-market budget.

## 5. Price the cost of doing nothing

The CFO's real comparison isn't "fund vs. don't fund." It's "fund vs. the trajectory we're on." Make that explicit:

- **The churn trend.** Churn has doubled in 18 months. What does another 12 months look like if it holds or keeps rising? In ARR, gross profit, and GRR.
- **The cost of delaying systemic fixes.** From the earlier example, about $128k per quarter, plus the extra rescue work those accounts will need later.
- **The compounding.** Under-resourced teams firefight, systemic fixes stall, more accounts go bad, and the problem grows. Reprioritizing inside a team that's already over capacity can make the long-run problem worse.

## 6. Lower the risk of saying yes

CFOs fund reversible, staged bets far more readily than permanent headcount. Structure the ask accordingly:

- **Stage it.** Ask for phase 1 now (e.g., contractors plus one FTE) with a gate at 2 quarters. Phase 2 unlocks only if leading indicators hit agreed targets.
- **Favor variable cost first.** Contractors or implementation partners for rescue surges can be cut quickly if results don't appear. Reserve permanent hires for systemic work, where institutional knowledge matters.
- **Set kill criteria up front.** "If time-to-value in the new cohort hasn't improved by X% by Q3, we'll scale back." Pre-committing to stop is what makes a CFO comfortable starting.
- **Offer partial self-funding where possible.** Examples: repricing unprofitable accounts, charging for premium implementation or rescue services, or tightening discount policy. Even a partial offset shows you're treating the money as an investment, not a cost.

## 7. Commit to accountability

Propose the scorecard yourself, before the CFO asks:

| Horizon | Metric |
|---|---|
| **Leading (monthly)** | Time-to-first-value, implementation duration, adoption depth in new cohorts, save rate on targeted accounts |
| **Mid (quarterly)** | Rescue outcomes vs. predictions, rescue demand volume (should fall), first-renewal retention in early cohorts |
| **Lagging (annually)** | GRR, NRR, churned gross profit |

Leading indicators matter most. Retention results take a year or more to show up in renewals, and the CFO needs a way to judge progress at the phase 1 gate before then.

## 8. Be honest about alternatives

The CFO is comparing your ask against every other use of the money: sales hires, the product roadmap, margin targets. Acknowledge this directly:

- Compare your expected return to the company's hurdle rate and, where you can, to the other investments competing for the same budget.
- If the product team's AI investment is also competing, point out that retention fixes raise the return on product investment, because features only retain customers who are live and getting value.
- **Be willing to lose the argument if the math doesn't support you.** If a sales hire earns more per dollar, profit maximization says fund that instead. Arguing this way openly builds the credibility you'll need for the next request.

## 9. Package the ask

Bring a one-page memo, with the model behind it:

1. **The problem:** churn doubled, churned gross profit, trajectory if unaddressed.
2. **What we've already done:** reprioritization, cut line, things we stopped doing.
3. **The ask:** phase 1 cost and structure (staged, contractor-heavy).
4. **The return:** marginal work unlocked, conservative expected profit, breakeven sensitivity.
5. **Risk controls:** gates, kill criteria, variable-cost structure.
6. **Scorecard:** leading and lagging metrics and review dates.

Pre-wire it. Walk the FP&A partner through the model before the meeting, and share the draft with the CFO ahead of time so objections surface privately rather than in the room.

## If the answer is still no

Ask for the smallest version that lets you prove the case:

- A single contractor for one quarter, pointed at the highest-return item below the line
- Approval to reinvest a share of saved or repriced revenue into capacity
- An agreed review date to revisit with actual data

A small, measured win is often the fastest route to the full budget.

## Bottom line

Don't ask for more people. Show that you've already reprioritized, and that the specific work sitting below your cut line earns several times its cost even under conservative assumptions. Present it in the CFO's terms: retention, forecast reliability, valuation. Structure the investment as a staged, reversible bet with clear kill criteria and a scorecard you own. That turns the request from a cost into an investment decision the CFO can defend, and one you're accountable for delivering.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do: The Action Plan

Here's the full recommendation turned into a sequenced plan. The logic throughout: **put every dollar and hour where it earns the most retained gross profit, and let the data, not the loudest VP, decide.**

## Weeks 1–2: Start the diagnosis and stop the bleeding

**Launch the churn diagnostic.** Co-own it with FP&A, not either VP. Segment the last 18 months of churned ARR by:
- Timing (first renewal vs. later)
- Adoption depth before churning
- Destination (competitor vs. status quo)
- Implementation duration
- What changed 18 months ago

Pull new-logo win/loss data too.

**Triage upcoming renewals.** List every account renewing in the next 12 months. For each, estimate account value (gross profit, not ARR) and uplift (how much intervention changes the odds). Assign executive sponsors to the top of the list now. Those renewal dates won't wait for the diagnostic.

**Ship the cheap, no-regret systemic fixes.** Define go-live criteria and "full value" milestones, and put a basic implementation playbook into use for every new implementation starting now. They cost little and start compounding immediately.

**Stop low-value work.** Drop low-uplift rescues, routine check-ins with healthy accounts, and reflexive discounting. Freeing capacity also strengthens your later case to the CFO.

**Start tracking your predictions.** Record every save estimate so you can compare it with actual outcomes. You'll need this track record for credibility.

## Weeks 3–6: Build one ranked list

- **Finish the churned-ARR segmentation** and quantify how much churned gross profit each cause accounts for.
- **Build a single ranked list** of rescues and systemic fixes by risk-adjusted, discounted profit per hour. Include the cost of delaying each systemic fix.
- **Ring-fence systemic capacity.** Assign named people with protected time and a clear rule for when rescue work can borrow them.
- **Make every rescue produce a reusable asset,** such as a template, checklist, or known-issues entry.
- **Build the financial model with FP&A,** using finance's margins, discount rate, and churn baselines.

## Weeks 6–8: Decide and ask

**Hold the roadmap decision meeting** with the VP of Product and VP of Services. Before the data comes in, agree on this rule:

| If most addressable churned profit is... | Then... |
|---|---|
| Customers who never reached full value | Prioritize implementation and service. Point the roadmap at features that reduce implementation friction. |
| Fully adopted customers leaving for competitors' analytics/AI (confirmed by win/loss) | Accelerate targeted product investment in the specific capabilities cited in losses. |
| Mixed, which is most likely | Fund both in proportion to recoverable profit per dollar. Sequence onboarding first, because it raises the payoff of every feature. |

**Take the phase 1 capacity ask to the CFO** if work below your cut line still earns well above its cost. Make it staged, contractor-heavy, with kill criteria, a breakeven sensitivity analysis, and a scorecard you own.

## Quarters 2–3: Execute and prove it

- Pilot systemic fixes on the next two or three implementations before scaling them.
- Run rescues from the top of the ranked list, favoring implementation rescue over discounts. When you concede anything, get something back: multi-year terms, references, or adoption commitments.
- Report leading indicators monthly: time-to-first-value, implementation duration, new-cohort adoption, and save rate against predictions.
- At the phase 1 gate, show results. Scale up if the indicators hit targets, and cut back if they don't.

## Quarter 4 onward: Rebalance

- Re-rank the combined list every quarter.
- Expect capacity to shift toward systemic work as rescue demand falls.
- Track first-renewal retention in the new cohorts. It's the clearest sign the root cause is fixed.
- Reprice or release accounts that stay unprofitable even when saved.

## What not to do

- **Don't start a broad feature race** before you know product gaps drive the churn. Features don't retain customers who never went live.
- **Don't default to discounts.** They cost you every year, anchor future renewals, and rarely fix a value problem.
- **Don't let firefighting consume all your capacity.** That's the loop that doubled churn.
- **Don't wait for perfect data** before acting on renewals that are coming due.

## If you do only three things

1. **Run the churned-ARR diagnostic with FP&A** and agree on the decision rule before the results come in.
2. **Fix time-to-value now** with go-live criteria, a playbook, and protected capacity for systemic work.
3. **Rank every rescue and fix by profit per hour,** spend on the top of the list, and bring the CFO a staged, measurable case for anything valuable left below the line.

**Your likely answer:** the VP of Services is closer to right on what to fix first, and the VP of Product may be right about what comes next. Make both prove it in retained gross profit.

## Outcome summary (sent to Jev)

The assistant's likely answer is that the VP of Services is closer to right about what to fix first, and the VP of Product may be right about what comes next. It recommends fixing time-to-value first while letting a churned-ARR diagnostic, co-owned with FP&A rather than either VP, decide how much to put behind the roadmap.

Its reasoning rests on putting every dollar and hour where it earns the most retained gross profit. Regional carriers have thin IT teams and complex integrations. Features don't retain customers who never went live, so fixing onboarding raises the payoff of every future feature. Implementation fixes are also cheaper and faster than a feature race.

The diagnostic would segment churned ARR by:
- renewal timing
- adoption depth
- where customers went
- implementation duration
- what changed 18 months ago

It would be paired with win/loss data. The decision rule is agreed before results arrive:
- If most churn comes from value-realization failure, prioritize implementation and service.
- If it comes from fully adopted customers defecting to competitors, make targeted analytics/AI investments.
- If it's mixed, fund both in proportion to recoverable profit, with onboarding sequenced first.

Immediate actions:
- Triage upcoming renewals by uplift times gross-profit value.
- Ship go-live criteria and a playbook.
- Stop low-value work.
- Track prediction accuracy.
- Rank rescues and systemic fixes on one list by risk-adjusted profit per hour.
- Ring-fence systemic capacity, and make each rescue produce a reusable asset.
- Bring the CFO a staged, contractor-heavy capacity request with kill criteria, breakeven sensitivity, and a scorecard.

Its caveats are to discount stated exit reasons and to avoid a broad feature race. It also warns against defaulting to discounts, letting firefighting consume capacity, or waiting for perfect data. Unprofitable accounts should be repriced or released. Product investment may also earn returns through new-logo wins.
