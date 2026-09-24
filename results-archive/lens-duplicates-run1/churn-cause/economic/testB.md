# churn-cause/economic/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:58:23.561349+00:00

## Prompt

You are a world-class expert: an economist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

# Diagnosing Your Churn: Product Gaps vs. Implementation Pain

**Short answer:** Probably neither belief is right as stated. Both VPs are describing real problems, but each is proposing the fix their own organization delivers. That doesn't make either of them wrong. It does mean you shouldn't settle the question by debate. You can settle it with data you likely already have, in about six weeks.

The two hypotheses also aren't competitors. They interact, and the interaction is probably where your real answer lies.

## Why the framing is misleading

**1. Stated reasons are unreliable.** When a carrier leaves, "the competitor had better analytics and AI" is the easiest thing for a departing executive to say. It's impersonal, forward-looking, and doesn't imply their own team failed to adopt what they bought. "Our implementation took 20 months and we never trusted the data" is closer to the truth in many exits, but it's harder to say out loud. Exit surveys and CSM notes will systematically over-report product gaps.

**2. Poor time-to-value turns feature gaps into churn.** A carrier that went live on time, has adjusters using the system daily, and sees cycle-time improvements will tolerate missing features and wait for your roadmap. A carrier that never got full value will seize on a competitor's AI demo as the justification to leave.

So the same feature gap produces very different churn depending on implementation health. There's a second link too: analytics and AI features depend on clean, complete, well-integrated data. If implementations stall before integrations and data migration are finished, accelerating the AI roadmap delivers features that your struggling customers can't use.

**3. The churn you see today was decided 12–24 months ago.** Claims platforms run on multi-year contracts, and carriers typically start evaluating alternatives 12–18 months before renewal. So a doubling of churn over the last 18 months reflects conditions that existed two or three years ago. The cohort leaving now was mostly implemented three to five years ago.

## The question nobody has asked: what changed?

Churn doubled, so something shifted. Before blaming the roadmap or onboarding, list every candidate, including those that belong to neither VP:

- **Competitive:** Did a competitor launch a credible AI or analytics offering, or start targeting your installed base with migration incentives?
- **Services:** Did you lose senior implementation staff, outsource to a partner, or change your implementation methodology around the time the churning cohort went live?
- **Sales:** Was there a sales push three to five years ago that signed poorly fitting customers, or overpromised capabilities, who are now reaching renewal?
- **Pricing:** Did you raise renewal prices?
- **Market:** Regional carriers have been through hard years, with cat losses, bad combined ratios, and cost pressure. Consolidation is also removing logos through M&A. Some of your churn may be acquired customers moving onto the acquirer's platform, which no product or service fix would have prevented.
- **Board pressure:** Many carrier boards are asking "what's our AI strategy?" That triggers RFPs even at reasonably satisfied accounts. This supports the product hypothesis in a specific form: the loss happens at the evaluation stage, not because of daily usage pain.

## How to adjudicate: a six-week diagnostic

**Step 1: Decompose churn.** Separate logo churn from revenue churn and downsell. Then classify every lost account by root event:

- M&A
- Core system replacement, where a policy-admin vendor bundled claims
- Budget or distress
- Competitive displacement
- Other

Only competitive displacement is really in dispute between your VPs. It may be a smaller share than everyone assumes.

**Step 2: Line up churn against implementation and adoption data.** For every customer, churned and retained, pull:

- Implementation duration versus plan
- Time to first go-live
- Percentage of contracted modules and integrations actually live
- Active-user ratio
- Support ticket volume and severity in year one
- Executive sponsor turnover
- Whether they use your existing analytics

Then look at which evidence pattern your data matches:

| If churn is concentrated in... | That points to... |
|---|---|
| Accounts with long or overrun implementations, partial go-lives, low adoption, heavy early ticket load, regardless of which competitor won | **Time-to-value** (the Services thesis) |
| Well-adopted, healthy accounts losing to competitors in evaluations where analytics or AI was a stated decision criterion | **Product gaps** (the Product thesis) |
| Low-adoption accounts that cite features on exit, where the features they cite partly exist in your product but aren't turned on or lack the data to work | **The interaction**: poor implementation disguised as a product gap |
| A specific implementation vintage, sales cohort, or acquired-customer group | **A one-time cause**; fix the process that created it |

The most informative single test: **are your healthy, fully implemented customers churning?** If they mostly aren't, the product gap is not the primary driver yet. If they are, it's real and urgent.

**Step 3: Run independent loss interviews.** Have someone neutral interview 10–15 churned customers and 10 retained ones. That could be you, a third party, or someone with no roadmap or services budget at stake. Don't ask "why did you leave?" Reconstruct the decision:

- When did you start looking?
- What triggered it?
- Who drove it?
- What did the competitor's demo show that you believed you couldn't get from us?
- Did you know we had X?

Interview the claims operations people as well as the executive who signed.

**Step 4: Agree on the decision rule before seeing results.** Get both VPs in a room and agree in advance what evidence would favor each thesis and how investment will shift in response. This pre-commitment is the most important governance move. Without it, each side will read ambiguous data as confirmation. With it, the analysis actually decides something.

## My prior, for what it's worth

In enterprise vertical software with heavy integration requirements, like claims platforms for regional carriers, I have usually found that time-to-value is the root cause and product gaps are the stated cause. I would expect your data to show churn heavily concentrated in accounts that never fully got live.

However, the AI shift is a real change in how carriers evaluate vendors. I would expect a secondary, growing pattern where product gaps are costing you evaluations. That pattern will matter more over the next three years than the last three.

Treat that as a hypothesis to test, not a conclusion.

## What to do now, before the diagnostic finishes

These moves are worth making under either hypothesis:

1. **Triage your renewal pipeline.** Score every account renewing in the next 24 months on adoption depth, go-live completeness, and sponsor stability. For the at-risk ones, launch "get-to-value" interventions now: finish stalled integrations and assign senior staff. This is the fastest churn reduction available, because product changes won't ship in time to save those renewals.
2. **Measure time-to-value as a company metric.** Track it jointly across Product and Services, from contract to meaningful value. That could mean the first claims processed end-to-end, or the analytics dashboards in use.
3. **Build AI and analytics features that ride on data you know customers have**, and treat data readiness as part of implementation scope. This is where the two VPs' agendas converge rather than compete.
4. **Arm your CSMs for AI-driven evaluations.** Give them a credible roadmap narrative and proof points to use when a customer's board forces an RFP. This matters at every account, including healthy ones.

## After the diagnostic

Shift investment based on what the data shows, likely something like:

- **If the time-to-value pattern dominates:** Redesign implementation. Phase go-lives, standardize integrations, and scope smaller and faster. Hold roadmap acceleration until fully implemented accounts are the norm.
- **If healthy accounts are losing to competitors:** Accelerate the specific capabilities that show up in lost evaluations, not a generic "AI roadmap."
- **In most cases:** Some of both, sequenced so that product investment lands on customers able to use it.

Your role here is the neutral party who owns the data on what customers actually experience. That makes you the right person to run the diagnostic and to insist that the decision rule is set before anyone sees the answer.

## Summary (sent to Jev)

The response argues that neither VP's belief is likely right as stated. Both describe real problems, but each proposes the fix their own organization delivers, and the two hypotheses interact rather than compete. It recommends settling the question with existing data in about six weeks instead of by debate.

Its reasons are that stated exit reasons over-report product gaps because they are easier to say than admitting adoption failures. Poor time-to-value turns tolerable feature gaps into churn, and AI features depend on clean, integrated data that stalled implementations never deliver. Because of multi-year contracts, today's churn was decided 12 to 24 months ago. It urges asking what changed, including competitive moves, services staffing or methodology, past sales pushes, pricing, carrier M&A and distress, and board pressure for an AI strategy that triggers RFPs.

The diagnostic has four steps. First, decompose churn by root event, since only competitive displacement is truly disputed. Second, line up churn against implementation and adoption data. The key test is whether healthy, fully implemented customers are churning. Third, have a neutral party run loss interviews that reconstruct the decision. Fourth, have both VPs agree on a decision rule before seeing results.

The author's prior is that time-to-value is the root cause and product gaps the stated cause, with a growing secondary AI-evaluation effect. The author frames this as a hypothesis, not a conclusion. Immediate steps are to triage renewals and launch get-to-value interventions, track time-to-value jointly, build AI on data customers actually have, and equip CSMs for AI-driven RFPs. Afterward, investment should shift according to the findings, likely toward a sequenced mix. Customer success, as the neutral owner of the data, should run the diagnostic.
