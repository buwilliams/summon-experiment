# churn-cause/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T13:05:42.023590+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

## Response

## The short answer

Neither belief can survive criticism yet, because neither is stated sharply enough to be refuted. Both are compatible with almost any churn pattern in their current form. Once you sharpen them, they make **opposite predictions about which customers leave**, and you can check that in two to four weeks with data you already have. There are also at least two third explanations that could make both remedies wasteful. Rule those out first.

## 1. What each conjecture actually claims

**Product gap (VP Product).** Customers get the product working, use it, and then find that competitors offer materially better analytics and AI. The gap became decisive recently, so customers leave for those competitors.
Mechanism: *adopted → compared → outclassed → switched.*

**Service failure (VP Services).** Customers never get the product fully working. Implementations drag, integrations stay unfinished, adjusters never fully adopt it, and support is painful. At renewal, the customer has paid for years without seeing the promised outcome and leaves.
Mechanism: *bought → stalled → never realized value → left.*

Notice that the causal chains diverge at step two. One says churners *succeeded* with the product, the other says they *never did*. That divergence is your test.

## 2. Discriminating predictions

| Observation | Product gap predicts | Service failure predicts |
|---|---|---|
| Adoption depth of churned accounts before notice | High: fully live, broad user base | Low: partial modules, stalled integrations |
| Implementation overrun vs. retention (controlling for account size) | Weak or no correlation | Strong correlation |
| When in lifecycle they churn | Later renewals, mature accounts | First or second renewal |
| Support signals in the 12 months before notice | Normal | Rising escalations, falling CSAT, reopened tickets |
| Feature requests logged before churn | Specific analytics/AI asks, repeated | Few, or requests for things the product already does |
| Where they go | Competitors with demonstrably better analytics/AI | Anyone. Often a vendor promising a smoother rollout, or a suite |
| Did they use our *existing* analytics? | Yes, found it inadequate | Rarely. Data never flowed well enough to try |
| What changed ~18–24 months ago | Competitor AI launches (the 2023 GenAI wave) | Implementation performance got worse: staffing, backlog, process change |

The last row matters most. **Churn doubled, so something changed.** Each theory must explain the timing, not just the churn.

The product story has a natural candidate for timing: competitors shipped AI features and carriers' boards started asking about AI. The service story needs evidence that implementation or support *got worse* in that window. If your implementations have been long and painful for five years at a steady level, a constant cannot explain a doubling. The service theory would then need an auxiliary claim, such as "customers tolerated it until alternatives appeared." That claim quietly borrows from the product theory.

## 3. Where each is easy to vary

**Product gap.**
- "Competitors have better features" is always true of *some* feature, so any lost customer can be retrofitted with a missing capability.
- If well-adopted customers stay, the theory can say they "valued different things." If poorly adopted ones leave, it can say "they saw no reason to push through because the product was behind."
- "Accelerate the roadmap" names no specific features, so there is no failure condition. Any post-launch churn becomes "we didn't ship enough."
- **Exit interviews are biased toward this theory.** Citing a feature gap is the polite, RFP-friendly reason. It doesn't blame the person who championed you, and it matches the justification document the buyer wrote for their switch.

**Service failure.**
- "Never got to full value" is close to a tautology. Any churned customer, by definition, didn't find enough value to stay.
- Unless "full value" is defined in advance, this theory cannot lose. Examples of a definition: specified modules live, more than X% of adjusters active weekly, integration with the policy system complete, one measured outcome such as cycle time reported.
- It can also absorb a feature-driven exit: "if we'd implemented them properly, they'd have seen the analytics."

**Hard-to-vary versions you should force each VP to commit to:**
- *Product:* "Accounts with high adoption churn at a meaningfully higher rate than two years ago. Most churned accounts went to vendors with specific capabilities A, B, and C that we lack, and had asked for them."
- *Service:* "Implementation overrun and low adoption, defined in advance, predict churn after controlling for size and segment. Implementation performance deteriorated in the window before churn rose."

## 4. Third explanations that could beat both

Check these first. They are cheap to test, and if true they make both proposed remedies expensive misdirection.

**A. Market structure.** Regional carriers are consolidating, and suite vendors (Guidewire, Duck Creek, and similar) bundle claims into policy and billing replacements. An acquired carrier adopts the acquirer's system. A carrier replacing its core system takes the bundled claims module.
- *Predicts:* churn tied to M&A events or full core-system replacements, destinations skewed toward suite vendors, and little correlation with either adoption or support history.
- *Refuted if:* most churned accounts were independent and replaced only the claims system.

**B. Cohort or fit.** A sales push three to five years ago brought in smaller carriers, unusual lines of business, or heavily discounted multi-year deals. Those contracts are now expiring.
- *Predicts:* churn concentrated in one sign-date cohort or segment, with older cohorts retaining at historical rates.
- This would also explain why *both* VPs see evidence. Bad-fit customers implement badly and find the product lacking.
- Related checks: price increases at renewal, and whether "doubled" is logo churn from a small base or revenue churn driven by a few large accounts.

**C. Interaction.** A slow implementation leaves data pipelines and integrations incomplete, so your analytics run on thin or dirty data and look weak. Meanwhile, AI hype gave dissatisfied customers a respectable exit story.
- Under this explanation, the "product gap" is partly an *implementation gap wearing a feature costume*.
- *Predicts:* among fully integrated accounts, your analytics usage is healthy and churn is low. Among partially integrated accounts, analytics complaints and churn are both high.
- *Refuted if:* fully integrated, heavy-analytics users are leaving at similar rates.

My prior, which is not a conclusion: C or a segment-split version is common in vertical SaaS, and A is a real force in regional insurance right now. Your data should overrule this prior.

## 5. The cheapest tests

**Test 1: Churn autopsy (2–3 weeks, existing data, highest value).**
Take every account that churned or gave notice in the last 18 months, plus a matched sample of retained accounts of similar size and segment. For each, code the following:
- Sign date, segment, contract terms, and price change at renewal
- Implementation planned vs. actual duration, modules live, integrations complete
- Adoption: active users as a percentage of licensed seats, and usage of analytics specifically
- Support escalations and CSAT in the 12 months before notice
- Feature requests logged, and which ones
- Destination vendor and whether it was a point solution or a suite
- Triggering event: M&A, core replacement, leadership change, price, or none

Two conditions make this test honest:
- **Pre-register.** Before anyone sees results, each VP writes down what pattern they expect and what result would change their mind. This one step prevents both theories from absorbing whatever comes back.
- **Code blind.** Have someone who reports to neither VP do the coding, from a rubric written before looking.

**Test 2: Timeline interviews (runs in parallel, ~10 churned accounts).**
Don't ask "why did you leave?" Ask a neutral third party to reconstruct the timeline instead:
- When did you first start looking at alternatives?
- What happened that week?
- Who initiated it?
- What was on the evaluation scorecard?

The trigger usually differs from the stated reason, and the trigger is what you can act on.

**Test 3: Timing check (a day).**
Plot churn rate against three things: implementation cycle times and support metrics by quarter, competitor AI launch dates, and M&A or core-replacement events among your customer base. Only one of these may line up with the inflection.

**Refutation criteria:**
- **Product gap is in trouble if** most churners had low adoption or incomplete integrations, well-adopted accounts churn at roughly historical rates, destinations don't have clearly superior analytics or AI, or pre-churn records show few requests for those features.
- **Service failure is in trouble if** overrun and adoption don't predict churn after controls, well-implemented accounts churn about as often, or implementation performance didn't worsen before churn rose.
- **Both are in trouble if** churn clusters around M&A or core replacements, or in one sales cohort.

## 6. What to do

1. **Freeze major reallocation for three to four weeks.** Don't shift roadmap priorities or headcount until the autopsy is done. A month of delay is cheap compared with a year of building the wrong thing.
2. **Take no-regret actions now.** Use the autopsy criteria to score your *current* base. Find live accounts that look like the churned ones and put them in an intervention program. You'll need this under any theory.
3. **Use a decision rule agreed in advance:**
   - *Churners are well-adopted and left for better analytics/AI:* accelerate the specific features they left for, not "AI" generally.
   - *Churners are poorly adopted, and overrun predicts churn:* fix time-to-value first. Also consider a value-recovery sprint for stalled accounts, randomized across half of them so you learn whether it works.
   - *Interaction pattern:* fix integration and data completeness first, since that is what makes your existing analytics credible. Then build.
   - *Market structure:* neither remedy addresses the core issue. The questions become positioning against suites, partnerships, M&A early-warning, and possibly which segments to serve.
   - *Cohort pattern:* tighten qualification and fix renewal economics. The problem may already be shrinking.
4. **Expect a segmented answer.** The most likely outcome is that different explanations hold in different segments. For example, small carriers may churn on service while larger ones churn to suites. Plan for a split resolution rather than crowning one VP.

The point of this process isn't to referee between your VPs. It's to turn two unfalsifiable stories into two falsifiable ones, and to let your own churn data eliminate whichever is wrong.

## Summary (sent to Jev)

The response argues that neither VP's belief can be judged yet, because each is too loosely stated to be refuted. Sharpened, they make opposite predictions: the product-gap theory says churners adopted the product fully and then left for competitors with better analytics and AI. The service theory says churners never fully implemented or adopted it. Adoption depth, correlation between implementation overrun and churn, lifecycle timing, support signals, feature requests, and destination vendors should distinguish them. Timing matters most. Churn doubled, so something changed, and a constantly painful implementation cannot explain a doubling unless service actually worsened.

It warns that each theory is easy to retrofit. Exit interviews favor feature-gap explanations, and "never got to full value" is nearly tautological unless defined in advance. Each VP should commit to a specific, refutable version. Three alternative explanations should be checked first: market consolidation and suite vendors absorbing claims systems, a bad-fit sales cohort whose contracts are expiring, or an interaction where incomplete integrations make analytics look weak and AI hype supplies an exit story. The response's prior leans toward the interaction or segment-split explanations and market structure, but it says data should overrule that prior.

The proposed tests are:
- A two-to-three-week churn autopsy comparing churned and matched retained accounts, with each VP pre-registering predictions and blind coding by someone reporting to neither.
- Neutral timeline interviews with about ten churned accounts, focused on triggers rather than stated reasons.
- A quick plot of churn against service metrics, competitor AI launches, and M&A events.

Meanwhile, the company should freeze major reallocation for three to four weeks, start interventions for at-risk accounts, apply a pre-agreed decision rule for each outcome, and expect a segmented answer rather than crowning one VP.
