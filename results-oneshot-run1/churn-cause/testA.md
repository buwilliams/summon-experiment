# churn-cause/critical-rationalism/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:50:09.216156+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

## The short answer

Neither VP can know yet, and neither can I. Both explanations are plausible, they predict different patterns in your data, and you can probably tell them apart in four to six weeks. The most likely outcome is that both are partly right and they interact. But "both" isn't a strategy, so you need to find out the *proportions* and the *causal order*.

Your role gives you an advantage: customer success sits between product and services and owns the churn data. You can be the neutral party that settles this with evidence instead of whoever argues more persuasively.

## Why you can't just ask churned customers

Exit reasons are notoriously unreliable here:
- "Your competitor has better AI/analytics" is a polite, blame-free reason to give. "Your implementation was a nightmare and we never trusted the system" is awkward to say.
- Churned customers often repeat the competitor's sales pitch, because that's what they used to justify the switch internally.
- A customer using 40% of your product will perceive gaps that a fully adopted customer wouldn't. Features you already have may be invisible to them.

So "customers told us it was features" isn't strong evidence for the product hypothesis. You need behavioral data.

## The tests that separate the two hypotheses

| Question | If Product is right | If Services is right |
|---|---|---|
| Did churned accounts reach full go-live and adoption before leaving? | Yes. They were healthy, got value, and still left. | No. Many were stuck in long implementations, partial rollout, or low usage. |
| How does churn correlate with implementation duration and overrun? | Weak correlation | Strong correlation: long or troubled implementations churn far more |
| What do *healthy, retained* customers say? | They're also asking for AI and analytics, and competitors are courting them | They're relatively satisfied. Feature requests exist but aren't urgent. |
| Where did churned customers go? | Mostly to named competitors with stronger analytics | Mixed: competitors, but also back to legacy or in-house systems, or suite vendors |
| Support ticket patterns before churn? | Feature requests, "can it do X?" | Bugs, configuration issues, escalations, long resolution times |
| Did churn rise for specific implementation cohorts? | No clear cohort pattern | Yes. Churn clusters around go-lives from a particular period (staffing change, methodology change, a hard integration type). |

**The single most useful analysis:** take every churned account from the last 18 months and classify it by implementation and adoption status at the time of the renewal decision. Then do the same for a matched set of renewed accounts. If most churners never reached full value, the services story dominates. If churners were well-adopted, the product story gains a lot of weight.

## Insurance-specific factors to check

**Lag effects.** Claims-system contracts are often multi-year and implementations can take 6 to 18 months. Churn you're seeing now may reflect implementations and sales decisions from two or three years ago. Look at *when those churned customers implemented*, not just when they left.

**Integration complexity.** Regional carriers' policy admin, billing, and legacy systems vary enormously. Check whether churn concentrates among customers with particular integration profiles. That would point to services, and possibly to product (integration tooling).

**Causes neither VP is naming.** Rule these out before committing:
- **Carrier M&A.** Regional carriers are consolidating. Acquired carriers often migrate to the acquirer's platform regardless of your product or service.
- **Suite bundling.** Vendors selling policy, billing, and claims together may be winning on platform consolidation, not analytics.
- **Pricing and budget pressure.** Catastrophe losses and reinsurance costs squeeze IT budgets.
- **Champion loss.** Did your executive sponsor leave before the churn?

If a big share of churn is M&A-driven, neither roadmap nor onboarding changes will fix it, and that's important to know.

## How the hypotheses likely interact

A common pattern in enterprise software:

1. The implementation runs long and the customer never reaches full adoption.
2. Leadership sees limited ROI and starts to doubt the purchase.
3. A competitor arrives pitching AI and analytics.
4. The customer leaves and cites features.

In that scenario, the feature gap is real but it's the *trigger*, not the *root cause*. Building AI features would help your sales team win new deals, but customers who never got value from your current product won't get value from new features either. Check whether this is the story before investing in either direction.

## What to do

**1. Run a structured diagnostic (four to six weeks).**
- Do the churn-versus-adoption analysis above, including every churned account and a matched renewed set.
- Run 15 to 25 win/loss interviews with churned *and* retained customers, ideally conducted by a third party or someone outside both the product and services orgs. Ask about the decision process, not just the reasons: who drove it, when doubt started, which alternatives they considered.
- Pull ticket data, implementation timelines, and usage data for the same accounts.

**2. Get both VPs to agree on the decision rules before seeing results.** For example: "If more than 60% of churned accounts never reached full adoption, services and onboarding get priority for the next two quarters." Pre-committing prevents each side from reinterpreting the data to fit its view. This is the most important political step.

**3. Take the no-regret actions now.** These make sense regardless of the answer:
- Build or refine account health scoring (adoption depth, time-to-value, ticket trends, sponsor engagement).
- Stand up a save motion for at-risk renewals in the next 6 to 12 months.
- Look for the fastest ways to shorten time-to-first-value in current implementations.

**4. Decide on allocation, not an either/or.** The realistic outcome is a portfolio decision: for example, a funded onboarding and service overhaul plus a targeted, smaller set of analytics features aimed at the gaps retained customers actually value. The diagnostic tells you how to weight those.

## One more thought

Churn doubling in 18 months is a sharp change. Sharp changes usually have identifiable triggers: a pricing change, a team reorganization, a new competitor entering your segment, a wave of acquisitions, a release that caused problems. Ask both VPs, and your own team, what changed about two years ago. The answer may shortcut much of the analysis.

If you can share what data you have access to (usage, implementation timelines, ticket history, exit reasons), I can help you design the specific analysis or the interview guide.

## Summary (sent to Jev)

The response says neither VP can know yet which explanation is right. Both are plausible, they predict different patterns in the data, and a four-to-six-week diagnostic can probably tell them apart. The likeliest outcome is that both are partly right and interact, so the task is to find their proportions and causal order. Customer success is well placed to settle the question neutrally because it owns the churn data.

It warns against relying on exit reasons. Citing a competitor's features is a polite, blame-free explanation, and poorly adopted customers see gaps a fully adopted customer wouldn't. Behavioral data is needed instead.

The key analysis is to classify every churned account from the last 18 months by implementation and adoption status at renewal, then compare against a matched set of renewed accounts. If most churners never reached full value, the services story dominates. Other tests include:

- how churn correlates with implementation overruns
- what retained customers want
- where churners went
- pre-churn ticket patterns
- whether churn clusters in particular implementation cohorts

Insurance-specific factors to check are lag effects from long contracts and implementations, integration complexity, carrier M&A, suite bundling, budget pressure, and loss of an executive champion. If M&A drives much of the churn, neither fix will help. A common pattern is that stalled adoption is the root cause and a competitor's AI pitch is merely the trigger.

The recommended steps are:

1. Run the diagnostic with 15 to 25 third-party interviews covering both churned and retained customers.
2. Have both VPs pre-commit to decision rules before seeing results.
3. Take no-regret actions now: health scoring, a save motion for at-risk renewals, and faster time-to-value.
4. Treat the outcome as a portfolio allocation rather than an either/or choice.

Finally, it suggests asking what changed about two years ago, since sharp changes in churn usually have identifiable triggers.
