# churn-cause/social/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:54:16.034855+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

Neither VP can be shown right by argument alone. Both stories are plausible, both are probably partly true, and each is conveniently aligned with its owner's function and budget. The good news is that **the two hypotheses make different, testable predictions**, and you likely already have the data to tell them apart in a few weeks.

## 1. Start with "what changed 18 months ago?"

Churn doubling is a change, so look for a change that explains it. A persistent condition like "our implementations have always been long" explains high churn, not *rising* churn. Ask:

- Did a competitor launch or aggressively reprice analytics/AI features around then? (Supports Product)
- Did implementation volume spike, a key services team turn over, the delivery model change, or the typical customer's complexity increase? (Supports Services)
- Did something external happen: carrier consolidation, core-system replacements (Guidewire, Duck Creek, etc.) bundling claims modules, budget pressure, a price increase on your side?

Most churn debates skip this step. It often settles the question or reveals a third cause.

## 2. The predictions that separate the hypotheses

| If Product is right... | If Services is right... |
|---|---|
| Churned customers were often fully implemented and actively using the product before leaving | Churned customers disproportionately had long, troubled, or incomplete implementations |
| Churn is spread across tenure, including mature, well-adopted accounts | Churn concentrates in early-life cohorts (first renewal) |
| Losses go to specific competitors, and deals cite analytics/AI | Customers leave for many vendors, or for "anything but you" |
| Prospects cite the same gaps in lost *new* deals | New-deal win rates are fine; problems start after signing |
| Healthy accounts also request these features | Healthy accounts are the ones that got live quickly |

## 3. The analysis to run (4–6 weeks)

Pull every account that churned in the last 18 months and compare it against retained accounts of similar size and tenure:

1. **Implementation data:** planned vs. actual go-live duration, scope delivered vs. sold, escalations. Plot churn rate by implementation duration bucket.
2. **Time-to-value and adoption:** modules live, active users vs. licensed seats, usage trend in the 6 months before renewal.
3. **Support experience:** ticket volume, severity, time-to-resolution, CSAT, escalations to executives.
4. **Where they went:** named competitor, in-house, core-system vendor, acquired/merged, unknown.
5. **Feature signals:** did churned accounts request analytics/AI features *before* deciding to leave, or only in the exit conversation?

The single most useful cut is often **churn rate among customers who reached full adoption.** If it's low, Services' story dominates. If well-adopted customers are also leaving, Product has a real case.

## 4. Watch for the interaction and the traps

- **Failed adoption masquerades as feature gaps.** A customer who never got your reporting module configured will honestly say "your analytics are weak." Check whether the "missing" features actually exist in your product but weren't deployed.
- **Exit interviews are biased toward features.** "Your competitor has better AI" is a polite, impersonal reason. "Your implementation was a mess and we lost trust" is harder to say. Weight behavioral data over stated reasons.
- **Buyer vs. user.** Carrier executives may be pulled by AI narratives even when claims adjusters' pain is operational. Both can be true simultaneously, with different fixes.

## 5. What to do while you analyze

**Get both VPs to agree in advance on what evidence would change their minds.** This converts a turf war into a shared test. For example: "If churn among fully adopted accounts is under X%, we prioritize onboarding. If above Y%, we accelerate the analytics roadmap."

In the meantime, take some no-regret actions:
- **Rescue at-risk accounts now.** Identify current customers with stalled implementations or declining usage and assign senior attention. This helps under either hypothesis.
- **Run structured interviews with 10–15 recently churned customers**, conducted by someone neutral (you, or a third party), not by Product or Services.
- **Audit the "missing features" list** against what already ships.

## 6. The likely shape of the answer

In B2B vertical software, the most common pattern is **mostly Services, with Product as the accelerant.** Customers who struggle to reach value become vulnerable, and a competitor with a shinier story then gives them a reason to leave. If that's what you find, the right move is usually to fix time-to-value first, because new features shipped into a broken onboarding motion won't get adopted either. Then invest selectively in the specific capabilities that show up in *competitive* losses among well-adopted accounts.

But let the data make that call, not the pattern. As the person who owns the customer relationship, you're in the best position to run this analysis and be the honest broker.

## Summary (sent to Jev)

The response argues that neither VP can be proven right by argument. Both explanations are plausible and probably partly true, and each conveniently matches its owner's function and budget. Because the two hypotheses make different, testable predictions, existing data can likely separate them within weeks.

It recommends first asking what changed 18 months ago, since a persistent condition like long implementations explains high churn but not rising churn. Candidates include:

- competitor launches or repricing of analytics and AI features
- implementation spikes, services turnover, or rising customer complexity
- external factors such as carrier consolidation, core-system vendors bundling claims modules, or a price increase

If Product is right, churned customers were often fully implemented, churn spans all tenures, losses go to specific competitors citing analytics or AI, and the same gaps appear in lost new deals. If Services is right, churn concentrates among customers with troubled implementations and at first renewal, and customers leave for many vendors.

The proposed four-to-six-week analysis compares churned and similar retained accounts on implementation duration and scope, adoption and usage, support experience, destination, and whether feature requests preceded the decision to leave. The single most useful cut is churn among fully adopted customers: low favors Services, high gives Product a real case.

Its caveats are that failed adoption can masquerade as feature gaps, exit interviews are biased toward polite feature reasons, and executive buyers and adjuster users may have different pains.

Meanwhile, the response suggests:

- getting both VPs to agree in advance on decisive evidence
- rescuing at-risk accounts
- having a neutral party interview 10–15 churned customers
- auditing the "missing features" list against what already ships

The likely pattern is mostly Services with Product as an accelerant, meaning fix time-to-value first. Still, the data should decide, with the customer success leader acting as honest broker.
