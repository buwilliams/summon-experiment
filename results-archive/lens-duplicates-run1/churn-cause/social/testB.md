# churn-cause/social/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:54:47.836918+00:00

## Prompt

You are a world-class expert: a sociologist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

## Short answer

Neither belief is proven yet, and framing it as either/or is the first thing to fix. From the outside I can't tell you who's right. But I can tell you how these situations usually turn out and how to find out quickly in your case.

## Why both diagnoses are suspect as stated

**Each VP is describing the problem their own function can solve.** Sociologists call this Miles' Law: "where you stand depends on where you sit." It doesn't make either of them wrong. It means neither diagnosis counts as evidence yet. Both are hypotheses shaped by organizational position.

**Churned customers' stated reasons are unreliable.** "Your competitor has better analytics and AI" is the most socially comfortable exit story a customer can tell. It's impersonal, it's forward-looking, and it doesn't require admitting that their own team never adopted the product or that they chose poorly. Exit interviews systematically overweight feature explanations. If your Product VP's case rests mainly on what departing customers said, discount it.

**The two explanations are probably entangled.** A customer who never finishes implementation never uses your existing analytics. To them the product really is feature-poor, and a competitor's demo looks transformative. Poor onboarding can produce the perception of product gaps. The reverse also happens: a genuinely weaker product makes every implementation delay feel less tolerable.

## Hypotheses neither VP has raised

A doubling of churn within 18 months usually has a discrete cause. Check these before accepting either story:

- **Cohort effects.** Claims software often runs on multi-year contracts. Did churn rise when contracts signed 3–4 years ago came up for renewal? If sales pushed hard then (new territory, discounting, a new sales leader), you may be losing badly fit customers who were never going to succeed.
- **Market structure.** Regional carriers are consolidating. Some churn may be acquisitions, where the acquirer standardizes on its own stack. That is neither a product nor a service failure.
- **Suite bundling.** Core-platform vendors increasingly bundle claims with policy and billing. You may be losing to a procurement logic ("one vendor"), not to a better point solution.
- **Something internal changed around 18 months ago.** Examples: CSM or implementation staff turnover, a reorganization, a price increase, a support model change, a key integration that broke.
- **Buyer expectations shifted.** Since 2023, carrier boards and CIOs have been asking "what's our AI strategy?" AI may be a procurement checkbox more than a used capability. That partially supports your Product VP, but it changes what you'd build: visible, credible AI at renewal time, not a broad analytics overhaul.

## How to find out (4–6 weeks, not a quarter)

**1. Build a churn dataset from behavior, not testimony.** For every account that churned in the last 18 months, and a matched set that renewed, pull:

- implementation duration vs. plan, and whether it ever went fully live
- time-to-first-value (define a concrete milestone, e.g., first claims processed end-to-end)
- adoption depth, especially usage of your existing analytics
- support ticket volume, severity, and escalations
- champion or executive-sponsor turnover
- contract origin (sales rep, year, discount level)
- where they went: named competitor, suite vendor, acquisition, in-house

**2. Run the decisive comparisons.**

| If you find... | It points to... |
|---|---|
| Churners had long or stalled implementations and low adoption, regardless of destination | Services |
| Churners barely used the analytics you already have | Services, and it undercuts the feature-gap story |
| Fully implemented, well-adopted accounts left for competitors with better AI or analytics | Product |
| Churn concentrated in one sales cohort, rep, or discount tier | Go-to-market fit |
| Churners went to acquirers or suite vendors | Market structure; neither VP's fix helps much |

The single most informative cut is this: **did healthy, fully implemented customers leave?** If almost none did, your problem is mainly services or fit. If many did, the product gap is real.

**3. Commission third-party win/loss interviews.** Talk to 10–15 churned customers and 5–10 lost prospects, conducted by someone outside the company. Ask about the decision process, not reasons: who initiated the review, when, what triggered it, what alternatives were considered. Triggers ("our new CIO," "the implementation was 9 months late," "the board asked about AI") are far more diagnostic than stated reasons.

**4. Look forward, too.** Score current accounts with the same variables. If stalled implementations predict risk in the live book, you have your answer and a rescue list.

## What to do now, before the data is in

Some moves pay off under any diagnosis:

- **Triage every account currently mid-implementation or behind schedule.** Assign executive sponsors and fix the worst cases. This is cheap and immediately protective.
- **Run a value-realization push on existing analytics.** Show at-risk accounts what they already own. If adoption rises and risk falls, that is itself evidence.
- **Build one visible, narrow AI capability** that you can demo at renewal, such as claim triage, document extraction, or a fraud flag. Don't reorganize the roadmap around it yet. It neutralizes the checkbox objection while you learn whether it matters.
- **Instrument time-to-value as a company-level metric** owned jointly by Product and Services.

## Your role

You're the natural neutral broker. Customer success sits between both functions and owns the outcome both are arguing about. Don't adjudicate between the VPs. Propose a shared diagnostic with decision rules agreed in advance: "if we find X, we prioritize services; if Y, we accelerate roadmap." That converts a political contest into an empirical question. It also protects you from being seen as siding with either camp, and it forces each VP to state what evidence would change their mind. A VP who won't answer that is telling you something.

My prior, for what it's worth: in enterprise software serving conservative buyers like regional carriers, churn usually starts with failed time-to-value and gets narrated as a product gap. The product gap then becomes real at renewal because a competitor exploits it. So I'd expect to find mostly a services problem with a product-perception layer on top. But I've been wrong on this before, and a few weeks of data will settle it for your company.

## Summary (sent to Jev)

The response says neither VP's belief is proven and that treating the question as either/or is the first mistake. Each VP is describing a problem their own function can solve (Miles' Law), so both diagnoses are hypotheses rather than evidence. Churned customers' stated reasons are unreliable because "competitors have better AI" is a comfortable exit story. The two explanations are likely entangled: customers who never finish implementation never use existing analytics and so perceive product gaps.

It raises other possible causes: cohort effects from contracts signed during an aggressive sales push, carrier consolidation, suite bundling by core-platform vendors, an internal change around 18 months ago, and AI becoming a procurement checkbox.

To find out within four to six weeks, it proposes:

- Build a behavioral dataset comparing churned and renewed accounts on implementation duration, time-to-first-value, adoption of existing analytics, support tickets, sponsor turnover, contract origin, and where customers went.
- Run decisive comparisons. The key question is whether healthy, fully implemented customers left.
- Commission third-party win/loss interviews focused on decision triggers rather than stated reasons.
- Score current accounts on the same variables.

Actions worth taking now under any diagnosis:

- Triage delayed implementations.
- Push adoption of the analytics customers already own.
- Build one narrow, demoable AI capability without reorganizing the roadmap.
- Make time-to-value a metric jointly owned by Product and Services.

The response advises the customer success leader to act as a neutral broker, proposing a shared diagnostic with decision rules agreed in advance. Its stated prior is that churn in this market usually starts with failed time-to-value and gets narrated as a product gap. It expects mostly a services problem with a product-perception layer, while acknowledging it could be wrong and that the data will settle the question.
