# churn-cause/critical-rationalism/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:52:34.681312+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

## Response

# Product Gaps vs. Implementation Pain: Which Explanation Survives Criticism?

Neither belief currently survives criticism, because neither has been stated in a form that could fail. That's fixable in a few weeks. Here's how to make each one falsifiable, what would distinguish them, and a third explanation you should test first because it could make the debate moot.

## First, a constraint both explanations must meet

Your churn didn't just exist. It **doubled over 18 months**. A good explanation must account for the *change*, not just the level. "Competitors have better AI" and "implementations are painful" may both have been true three years ago, when churn was half what it is now. So each conjecture must name what changed around 18–24 months ago:

- **Product view:** a specific competitor launch, a specific capability that became table stakes, or a shift in what carriers demand.
- **Services view:** implementations got longer, the services team changed (turnover, reorg, offshoring), implementation scope grew, or the product got harder to deploy.

If a VP can't point to a change with a date, their explanation is describing background conditions, not the cause of the increase.

Also check the size of the numbers. Regional carriers means your customer base is probably in the dozens or low hundreds. If churn went from 5 logos to 10, you're reasoning from a handful of cases. Then a careful case-by-case review of every churned account beats any statistical segmentation.

## What each conjecture actually claims

**Product-gap conjecture:** Customers got the product working, used it, compared it to alternatives, and concluded a competitor's capabilities were worth the substantial cost of switching claims systems. The mechanism runs through *comparison*.

**Implementation conjecture:** Customers never reached a working, valuable state. At renewal they faced an unfinished, expensive system and left, often citing features as the reason. The mechanism runs through *unrealized value*.

These imply different kinds of churned customer: satisfied-but-outgunned versus never-successful.

## Discriminating predictions

| Observation | Product-gap predicts | Implementation predicts |
|---|---|---|
| Implementation status of churned accounts | Fully live, decent adoption | Late, partial go-live, low adoption |
| When in lifecycle they churn | Any tenure, including long-standing accounts | Concentrated at first or second renewal |
| Cohort pattern | Older cohorts churning too | Recent cohorts churn more; older ones stable |
| Where they go | Specific competitors with the cited features | Anywhere, including status quo, in-house, or competitors with similar features |
| Cited "missing" features | Genuinely don't exist in your product | Often exist but were never deployed or adopted |
| **New-logo win rate** | **Declining, losing to the same competitors** | **Largely unaffected, since prospects haven't experienced implementation** |
| Leading indicators before churn | Competitor evaluations, RFPs, feature requests | Escalations, missed milestones, falling usage, CSAT decline |
| Timing correlation | Follows competitor launches | Follows implementation duration or services changes |

The **new-logo win rate** is the sharpest discriminator. The product-gap view predicts you're losing new deals to the same competitors for the same reasons. The implementation view doesn't predict that at all, since prospects haven't suffered your onboarding. If win rates are flat while churn doubled, the product-gap story is badly damaged. If win rates collapsed to the same competitors, the implementation story can't explain it alone.

The **"phantom gap"** test is the second-sharpest. Take every churn reason that cites a missing capability and check whether the product actually has it. If a meaningful share already exists, customers are describing an adoption failure in feature language, which supports the services view.

## Where each explanation is easy to vary

**Product-gap is easy to vary because:**
- Churned customers almost always cite features. It's the socially easy exit reason, and it's what they tell vendors they're leaving. Exit reasons are weak evidence.
- "Better analytics and AI" is a moving target. Any loss can be attributed to some gap, and any feature you ship can be declared insufficient.
- It has no stated failure condition. What churn pattern would convince the VP of Product that features aren't the cause?

**To make it hard to vary:** name the specific capabilities and the specific competitors, and commit in advance that churned and at-risk accounts will be ones that evaluated those competitors for those capabilities.

**Implementation is easy to vary because:**
- "Never got to full value" is true of nearly every enterprise software customer, including the ones who renew. Churn gets explained backward: they left, so they must not have gotten value.
- Long implementations can be blamed on anything: scope, customer IT, data migration.

**To make it hard to vary:** define a time-to-value or adoption metric *before* looking at outcomes (e.g., go-live within X months, Y% of adjusters active, Z claims processed), and predict that accounts below the threshold churn at a materially higher rate than accounts above it, controlling for size.

**One structural caution.** Each explanation prescribes investment in the proposer's own organization. That doesn't make either wrong. But it means neither VP has a natural incentive to find the refuting evidence, so someone neutral should run the analysis. That someone could be you, with one caveat: customer success is itself a candidate cause (coverage ratios, CSM turnover, renewal process). Include your own function in the scrutiny.

## Cheapest tests, roughly in order

1. **Pre-registration (one meeting, free).** Ask each VP to write down what the data below would show if they're wrong. This is the single most valuable step. It converts the debate from advocacy into conjecture.
2. **Churned-account autopsy (1–2 weeks).** For every account lost in 18 months, record implementation duration, go-live completeness, adoption at renewal, tenure, cohort, destination, stated reason, whether the cited features exist, escalation history, acquisition status, and whether the champion or economic buyer changed. Do the same for a matched sample of renewed accounts. Without the renewed comparison you can't tell causes from universal conditions.
3. **Win/loss trend (days).** New-logo win rates and loss reasons over the same period, by competitor.
4. **Neutral exit interviews (2–4 weeks).** Use a third party, not the account team. Ask *when* they started looking and what triggered it, not just why they left. A trigger at month 9 of a stalled implementation and a trigger at a competitor's demo are very different stories.
5. **Forward test (one or two quarters).** Take at-risk accounts with low adoption and give a subset intensive re-onboarding. If renewal intent improves relative to the others, the implementation view gains real support. This is slower, but it's the only test above that is experimental rather than observational.

## Third explanations that may beat both

Several alternatives would produce the same surface facts, with customers citing features and complaining about implementation, while making both VPs' remedies misdirected.

- **Customer mix shift (strongest candidate).** If sales moved into a different segment 18–30 months ago (larger carriers, different lines of business, more complex claims operations), those customers would hit harder implementations *and* find more capability gaps, then churn at first renewal. This explains why *both* VPs see supporting evidence. Test: compare churn by segment and fit criteria, and check whether churn is concentrated in customers sold after a sales-strategy change.
- **Market consolidation.** Regional carriers get acquired. If churned logos were absorbed by carriers standardizing on another system, neither features nor onboarding matter. This is cheap to check and could refute both VPs at once.
- **Suite consolidation.** Carriers moving to core-platform vendors that bundle claims with policy and billing. The loss is to "platform," not to "better analytics." Win/loss destination data will show this.
- **Pricing and renewal terms.** Price increases, packaging changes, or discounts expiring on early deals.
- **Product quality regression.** Reliability, performance, or bug-rate deterioration isn't a feature gap or an onboarding failure, but customers will describe it as both.
- **Interaction effect.** Long implementations mean customers are live on fewer modules, so they perceive gaps. Adding features increases implementation complexity. If this is true, accelerating the roadmap makes churn *worse*. That's worth knowing before committing.

## What to do

Don't pick a side yet. Run the pre-registration and the autopsy now. They cost a few weeks and will likely refute at least one conjecture outright. Then act on what survives:

- **Churn concentrated in low-adoption, first-renewal, recent-cohort accounts, win rates flat, many phantom gaps:** fix implementation and time-to-value first. Keep the roadmap, but don't accelerate it.
- **Churned accounts were well adopted, left for named competitors over real capabilities, win rates declining to the same competitors:** the product gap is real. Invest, targeting the specific capabilities identified, not "AI" generally.
- **Churn concentrated in a segment, in acquired carriers, or at price changes:** the fix is ICP, pricing, or account strategy, and both proposed investments would be expensive misfires.
- **Evidence supports both in different segments:** that's a legitimate finding, but only if the data shows it. It shouldn't be the default compromise.

The goal isn't to decide which VP is right. It's to reach the point where the data could have proven either of them wrong, and see which explanation is still standing.

## Summary (sent to Jev)

The response argues that neither VP's belief yet survives criticism because neither is stated in a form that could fail. It recommends not picking a side until a few weeks of testing have been done. Any explanation must account for why churn *doubled* over 18 months, so each VP should name a dated change, such as a competitor launch or a shift in the services team. With a customer base likely in the dozens or low hundreds, a case-by-case review of every churned account beats statistical segmentation.

The two views predict different churned customers: satisfied but outgunned, versus never successful. The sharpest discriminator is the new-logo win rate. The product-gap view predicts losses to the same competitors, while the implementation view does not. The second test is the "phantom gap" check: whether features customers cite as missing actually exist. Each view is currently easy to vary. Exit reasons usually cite features, and "never got to full value" applies even to renewers. Each should be made hard to vary through named competitors and capabilities or a pre-defined adoption threshold. Because each VP's remedy funds their own organization, a neutral party should run the analysis, and customer success itself should be scrutinized.

The proposed tests, in order, are:
1. Have each VP pre-register what would prove them wrong.
2. Conduct a churned-account autopsy with a matched sample of renewed accounts.
3. Review the win/loss trend.
4. Run third-party exit interviews focused on what triggered the search.
5. Run a forward re-onboarding experiment.

Alternative explanations include customer mix shift (the strongest candidate), carrier acquisitions, suite consolidation, pricing changes, quality regression, and an interaction effect where adding features worsens churn. The response recommends acting on whichever explanation survives and treating "both" as valid only if the data shows it.
