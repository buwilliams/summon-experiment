# churn-cause/economic/testC

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:59:17.264414+00:00

## Prompt

Use profit maximization to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

# Diagnosing Churn Through a Profit-Maximization Lens

## The short answer

Neither belief can be confirmed from what you've described. Both VPs are proposing expensive, slow investments based on a causal story, and the most profitable move right now is to **buy information cheaply before committing capital**. That said, the profit logic tilts toward fixing services first, and there is a good chance both VPs are partly right in a specific way.

## Reframe the question

The question isn't "who's right." It's this: **where does the next dollar reduce the most churn-weighted gross profit, and how fast?**

The value of any retention intervention is roughly:

> **Value = (ARR at risk that this cause explains) × (share of that churn the fix can prevent) × gross margin × expected remaining customer lifetime − cost of the fix**, discounted for time-to-impact.

Here is an illustration with made-up numbers. Suppose you have $50M ARR, churn went from 8% to 16%, and gross margin is 75%. The extra 8 points cost you about $4M ARR a year, or $3M in gross profit, compounding every year it persists. Each point of churn you win back is worth about $375K in gross profit per year, and several times that over a customer's lifetime. That is the size of the prize you're allocating against.

## Why the services-first case is stronger on profit logic, pending data

1. **Faster payback.** Onboarding and support fixes can affect accounts in flight within a quarter. Analytics and AI features take quarters to build, then quarters more to adopt. Discounting matters.
2. **Lower cost and lower variance.** Process fixes, implementation playbooks, and targeted headcount are cheaper and more predictable than roadmap bets.
3. **Complementarity.** Features only create value for customers who are fully live. If many customers never reach full value, new features land on accounts that won't use them. Fixing onboarding raises the ROI of every future feature. The reverse isn't true.
4. **Switching costs.** Claims systems are sticky once embedded. A regional carrier that never fully implemented has low switching costs, so a competitor's AI demo can pull it away easily.

This points to a likely synthesis. **Product gaps may be the reason customers give, while poor implementation is the reason they're vulnerable.** Exit interviews tend to overstate feature gaps, because "your competitor has AI" is a more comfortable thing to say than "your team never got us live."

## The diagnostic: 30–45 days, cheap and decisive

Pull every account that churned in the last 18 months, weighted by ARR, and test these signals:

| Signal | Points to **Services** | Points to **Product** |
|---|---|---|
| Implementation duration / time-to-first-value | Churners had much longer implementations than retained accounts | No difference |
| Adoption depth before churn | Churners never reached full usage (modules, users, claims volume) | Churners were fully adopted, then left |
| Cohort timing | Churn spike concentrated in cohorts onboarded after a services change (growth outpacing capacity, team turnover) | Spike across all cohorts, coinciding with competitor AI launches |
| New-logo win/loss | You still win new deals on features | You're losing new deals on analytics/AI too |
| Where churners went | Mixed destinations, or back to legacy/in-house | Concentrated at one or two AI-forward competitors |
| Support data | Churners had high ticket volume, long resolution times, escalations | Support metrics similar to retained accounts |

Also separate out **non-addressable churn**, such as carrier mergers and acquisitions, which is common among regional carriers, and insolvency. Don't spend money trying to solve churn no intervention could prevent.

This analysis costs a few analyst-weeks. Compare that with a misallocated roadmap acceleration that could cost millions. The value of the information is very high.

## What to do now

**No-regret moves (start immediately):**
- Triage accounts currently in implementation or below target adoption. These are your highest-risk, highest-recoverable ARR.
- Set a time-to-value metric and a target, and report it alongside churn.
- Run a health-score sweep of top-ARR accounts, with executive outreach to the at-risk ones.

**Don't freeze the roadmap. Re-rank it:**
- Prioritize features by retention impact on at-risk ARR, not by competitive parity.
- For analytics and AI, evaluate partnering or embedding a third-party solution. Faster time-to-market improves the payback math considerably.

**After the diagnostic, allocate by marginal return:**
- Estimate what share of excess churn each cause explains. Fund each lever until its marginal return per dollar roughly equals the other's.
- A plausible outcome is a services-heavy near-term budget with a narrower, retention-targeted product investment. Let the data set the ratio.

**Set decision criteria up front** so the debate doesn't become political. For example: "If more than 60% of churned ARR came from accounts that never hit full adoption, services gets priority funding."

## Bottom line

Take the VP of Services' diagnosis seriously first. It's cheaper to fix, pays back faster, and makes product investment more valuable. But don't declare a winner yet. Spend a month confirming which story the churned-account data supports, then allocate budget where each additional dollar protects the most gross profit.

## Summary (sent to Jev)

The response argues that neither VP's belief can be confirmed from the information given. Because both propose expensive, slow investments based on a causal story, the most profitable step is to buy information cheaply before committing capital. It reframes the question as where the next dollar reduces the most churn-weighted gross profit, and how fast. With illustrative numbers ($50M ARR, churn from 8% to 16%, 75% margin), it estimates about $3M in yearly gross profit lost, or roughly $375K per churn point.

Pending data, it leans toward fixing services first, for four reasons:

- **Faster payback:** these fixes affect in-flight accounts within a quarter.
- **Lower cost and variance:** they are cheaper and more predictable than roadmap bets.
- **Complementarity:** features only create value for fully live customers.
- **Switching costs:** carriers that never fully implemented are easy for competitors to pull away.

Its likely synthesis is that product gaps are the reason customers give, while poor implementation is why they are vulnerable. Exit interviews tend to overstate feature gaps.

It proposes a 30–45 day diagnostic of ARR-weighted churned accounts. This would compare implementation duration, adoption depth, cohort timing, new-logo win/loss, where churners went, and support metrics against retained accounts. Non-addressable churn such as mergers and insolvency should be excluded.

Immediate no-regret moves include:

- triaging accounts in implementation or below target adoption
- setting a time-to-value metric
- running health-score sweeps with executive outreach

The roadmap should be re-ranked by retention impact rather than frozen, and partnering on AI and analytics is worth considering. After the diagnostic, budget should go to each lever until marginal returns equalize, using decision criteria set up front to avoid politics. The bottom line is to take the services diagnosis seriously first, without declaring a winner until the data confirms it.
