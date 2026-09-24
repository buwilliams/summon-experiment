# churn-cause/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T13:03:27.134095+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

I can't tell you which one is right from here, and neither VP can yet either. Both are plausible, both hypotheses conveniently point toward each VP's own function, and the two explanations probably interact. The good news is that they make **different, testable predictions**, and you likely already have most of the data to test them in a few weeks.

## Why this is hard to call by intuition

- **Stated churn reasons are unreliable.** "Your competitor has better AI/analytics" is a polite, blameless exit reason. "Your implementation took 14 months and we never trusted the data" is awkward to say to the vendor. Product gaps tend to be overreported in exit conversations.
- **The explanations compound.** A carrier that never got full value from your core product is far more receptive to a competitor's AI pitch. In that case, the product gap is the trigger, but the implementation failure is the vulnerability.
- **Churn is a lagging indicator.** Customers churning today likely signed two to four years ago. Their experience reflects your implementation process, team, and product *as they were then*, not now.

## What each hypothesis predicts

| If it's mainly **product gaps**, you'd expect... | If it's mainly **implementation/service**, you'd expect... |
|---|---|
| Churned customers were fully live, with healthy usage before leaving | Churned customers had long time-to-go-live, partial rollouts, or low adoption |
| Churn spread across tenure, including long-happy customers | Churn concentrated at the *first* renewal |
| Churned customers go to specific competitors known for analytics/AI | Churned customers go to whoever pitched them, back to legacy, or build in-house |
| Churn rise lines up with competitor launches | Churn rise lines up with changes in implementation duration, staffing, or scope |
| New-sales win/loss data also cites analytics/AI | New sales win fine; the problem appears post-sale |
| Churned accounts had open feature requests for these capabilities | Churned accounts had high ticket volume, escalations, poor CSAT, or unfinished integrations |

## The diagnostic (roughly 4–6 weeks)

**1. Cohort analysis on churned vs. retained accounts.** For every account up for renewal in the last 18 months, pull:
- Contract start date, go-live date, and **time-to-value** (days to go-live, or to whatever milestone signals real value, like first claims processed end-to-end or key integrations complete)
- Adoption depth: active users vs. licensed, modules in use, % of claims volume flowing through your system
- Support history: ticket volume, severity, escalations, CSAT
- Segment, size, CSM and implementation lead assigned
- Churn destination, where known
- Logo vs. revenue churn, including downsells

Then ask: does churn rate differ sharply by implementation duration or adoption level? If customers who went live in under six months churn at a fraction of the rate of those who took over a year, that's strong evidence for the Services view. If churn is flat across implementation quality and fully adopted customers leave for AI-forward competitors, that favors Product.

**2. Independent churned-customer interviews.** Interview 10–15 recently churned customers plus 5–10 at-risk current ones. Have someone neutral run them, not a sales rep or either VP's team, and ideally a third party. Ask about the whole journey, not just the final decision: "Walk me through the first year. When did you start evaluating alternatives? What would have had to be true for you to stay?"

**3. Check win/loss on new business.** If you're winning competitive deals at normal rates, product gaps are less likely to be the primary churn driver. If win rates are also falling against the same competitors, that's a meaningful signal for Product.

**4. Look for what changed ~18–24 months ago.** Did implementation timelines lengthen? Did you lose experienced implementation staff? Did deal scope or customer size shift? Did a competitor launch something? A sharp doubling usually has an identifiable cause.

## What to do while you're diagnosing

Don't wait on the analysis to protect current revenue:
- **Score your renewal pipeline** for the next 12 months using the risk signals above (stalled implementations, low adoption, heavy support load) and run executive-level save plays on the highest-risk accounts.
- **Avoid big irreversible bets** in either direction. Don't reorganize Services or commit the next year of roadmap to AI until you have data.
- **Frame it as a joint question for both VPs.** Agree upfront, in writing, on what evidence would confirm or refute each hypothesis. That keeps the result from becoming a political win for one side and makes it easier for the "losing" VP to accept.

## How to act on what you find

- **Clearly implementation-driven:** Prioritize reducing time-to-value. Standardize implementation packages for regional carriers, pre-build common integrations (policy admin, payments, document systems), set go-live milestones with customer accountability, and trigger CS intervention when an account stalls. Product can contribute here too, since onboarding friction is often a product problem.
- **Clearly product-driven:** Accelerate the specific capabilities that churned customers left for, not "AI" generically. In regional insurance, practical wins like fraud flags, reserve recommendations, claims triage, and operational dashboards often matter more than flashy features.
- **Both (the most likely outcome):** Sequence it. Fix time-to-value first for new and at-risk accounts, because new features don't help customers who aren't fully live. Meanwhile, ship a targeted set of analytics capabilities aimed at the gaps customers actually cited, and make sure they're easy to adopt, or you'll reproduce the same value gap.

One last point: as head of CS, you sit between these two teams and own the post-sale relationship, which makes you well placed to lead this analysis. It's worth asking honestly whether anything in how CS engages at-risk accounts has contributed as well.

## Summary (sent to Jev)

The response declines to say which VP is right, arguing that neither can know yet. Both hypotheses conveniently favor each VP's own function and probably interact, but they make different, testable predictions that existing data can likely settle within a few weeks. Intuition is unreliable for three reasons. Exit reasons overstate product gaps because "better AI" is a polite, blameless excuse. The explanations compound, since a poor implementation leaves customers vulnerable to a competitor's pitch. And churn lags, reflecting conditions from two to four years ago.

A product-gap explanation would predict churn among fully live, healthy-usage customers across all tenures, departures to specific AI-forward competitors, timing aligned with competitor launches, and weak new-sales win rates. An implementation explanation would predict churn concentrated at first renewal among customers with long go-lives, low adoption, and heavy support loads.

The proposed four-to-six-week diagnostic has four parts:
- a cohort analysis comparing churned and retained accounts on time-to-value, adoption depth, support history, segment, assigned staff, churn destination, and logo versus revenue churn
- neutral, ideally third-party interviews with 10–15 churned and 5–10 at-risk customers about their whole journey
- a check of new-business win/loss data
- a search for what changed 18–24 months ago

Meanwhile, the company should score its renewal pipeline and run save plays on high-risk accounts. It should avoid big irreversible bets, and it should have both VPs agree in writing on what evidence would decide the question.

The recommended action depends on the findings. If churn is implementation-driven, the company should cut time-to-value. If it is product-driven, it should build the specific capabilities customers left for. If both, which is most likely, it should fix onboarding first while shipping targeted, easy-to-adopt analytics. The response also suggests the head of CS lead the analysis and examine CS's own contribution to churn.
