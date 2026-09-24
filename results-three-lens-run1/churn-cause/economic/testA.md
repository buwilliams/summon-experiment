# economic/churn-cause/testA

Model: claude-opus-5-5 · 2026-09-24T14:52:06.897370+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

I can't tell you which belief is right because I don't have your data, and neither VP can know either without testing it. Both explanations are plausible, they aren't mutually exclusive, and there are other candidates neither has raised. The most useful thing you can do is replace a debate between opinions with a quick diagnostic that both VPs agree in advance will settle it.

## First, widen the hypothesis set

Before testing Product vs. Services, rule out causes that neither team owns:

- **Market consolidation.** Regional carriers get acquired or merge. If a churned customer was absorbed into a carrier that already had a claims system, no roadmap or onboarding fix would have saved it.
- **Platform bundling.** Carriers moving to core suites (policy, billing, and claims together) may drop point solutions regardless of quality.
- **Pricing or contract changes.** Did pricing, packaging, or renewal terms change around 18 months ago?
- **Champion turnover.** A sponsor leaves and the replacement brings their preferred vendor.
- **Something that changed internally.** Churn *doubling* over a defined window suggests a shift. What happened 18–30 months ago? A product release, a services reorg, a CS headcount cut, a new sales motion selling to a different customer profile, a competitor launch?

## Tests that actually distinguish the two main hypotheses

The key is to find evidence where the two explanations predict *different* things:

| Question | If Services is right | If Product is right |
|---|---|---|
| **When do customers churn?** | Disproportionately at first renewal | Spread across tenure, including long-time customers |
| **Did churners reach full adoption?** | Most never fully went live or used core workflows | Many were fully adopted and still left |
| **Implementation length vs. churn** | Longer implementations → sharply higher churn | Weak or no relationship |
| **Where did they go?** | Mixed, including to "simpler" vendors or back to legacy systems | Concentrated with competitors known for analytics/AI |
| **New sales win/loss** | Win rates steady; losses aren't feature-driven | Losing competitive deals on analytics/AI too |
| **Pre-churn signals** | Escalations, ticket volume, missed go-live dates, CSAT drops | Feature requests, questions about AI/analytics in QBRs, RFPs issued |
| **Implementation trend** | Implementations have gotten longer over the period | Implementation times flat |

Practical steps:

1. **Cohort your churned accounts** (probably dozens, not thousands, so this is feasible manually). For each, capture: tenure at churn, implementation duration, go-live status, adoption depth, destination, stated reason, and the account's history in the 12 months before churn.
2. **Don't trust stated exit reasons on their own.** "You're missing features" is a socially easy thing to tell a vendor, and "your implementation hurt" is harder. Compare what customers said at exit with what they were saying in tickets, QBRs, and escalations beforehand. If possible, have a neutral third party conduct 10–15 exit interviews.
3. **Look at retained customers too.** If your healthiest, longest-tenured accounts are asking about analytics and AI, that's an early warning even if it isn't what's driving current churn.
4. **Segment.** The answer may differ by carrier size, product line, or implementing team.

This should take 4–6 weeks, not a quarter.

## A likely synthesis worth testing

These hypotheses often interact. A customer who never reaches full value from the core product won't experience your analytics either, so at renewal they compare an under-delivering product against a competitor's demo and conclude "they have better features." In that case, building more features without fixing time-to-value adds capability that stalled customers never reach. Conversely, if fully onboarded customers are leaving for AI capabilities, service fixes alone won't hold them.

A useful framing for both VPs: **the shared problem is time-to-value.** Product contributes to it through complexity and configurability. Services contributes through process and staffing. That turns a budget fight into a joint metric.

## What to do now

1. **Get both VPs to pre-commit.** Before the analysis, ask each: "What finding would change your mind?" Write it down. This is the single best way to keep the result from being dismissed by whoever it disagrees with.
2. **Take no-regret actions in parallel.** Identify currently at-risk accounts (stalled implementations, upcoming renewals, low adoption) and run save plays now. Don't wait for the diagnosis to protect revenue.
3. **Check your own function honestly.** CS sits between the two teams and can be a credible neutral broker, but look at whether CS coverage, account ratios, or renewal processes changed during this period. Being the first to examine your own team's role will make the exercise more credible.
4. **Let the data allocate investment.** You'll probably end up funding both, but the proportion and sequencing should follow the evidence. For example, you might pause a roadmap item to fund implementation tooling, or conversely prioritize one analytics capability that's showing up in both churn and lost deals.

If you share what data you have (churn list, tenure, implementation durations, destinations), I can help you design the cohort analysis or the exit interview guide.

## Turn 2

**User:** How do I get candid answers in exit interviews when most of these churned carriers are already annoyed with us and might not even take the call?

**Assistant:**

The core problem is that a churned customer has nothing to gain from talking to you and some reason to avoid it. You need to lower the cost of saying yes, make it clear this isn't a win-back pitch, and make candor feel safe and worthwhile.

## Who asks matters most

**Use a neutral third party if you can afford it.** Win/loss and churn research firms exist for exactly this, and customers are measurably more candid with them. They'll say "the implementation was a mess and your PM stopped returning calls" to an outsider, but not to you. If budget is tight, even an independent consultant or a researcher from outside CS, Product, and Services is better than someone either VP manages.

**If you do it in-house, don't use the account team.** The former CSM or implementation lead is the worst choice, since the customer may be criticizing them directly. A senior leader with no prior involvement, ideally someone above both VPs or you personally if you weren't close to those accounts, works better. Seniority signals that you take it seriously.

**Never let sales near it.** If the customer suspects a win-back attempt, they'll either decline or give polite non-answers.

## The ask

- **Be explicit that you're not trying to win them back.** "We're not calling to change your mind. We lost several carriers and want to understand what we got wrong."
- **Keep it short and specific.** Ask for 20 minutes, not "some time to chat."
- **Acknowledge the relationship ended badly if it did.** "I know the last year wasn't a good experience" disarms people. Pretending everything was fine does the opposite.
- **Offer confidentiality.** Say that responses will be summarized in aggregate and not attributed to individuals, especially to anyone they worked with. Then honor it.
- **Target the right person.** The executive who signed the contract often knows why the decision was made. The day-to-day users know why the product frustrated them. You want both, but the decision-maker is higher priority.
- **Consider an incentive.** A modest gift card or charity donation is common. Some senior insurance executives will find cash awkward, so a donation in their name often lands better.
- **Use your network.** Regional insurance is a small world. A warm introduction from a mutual contact, an industry association, or a board member gets a much better response than a cold email.

Expect a response rate well below half, especially among the most annoyed accounts, and plan for that. Ten to fifteen good conversations are usually enough to see patterns.

## Questions that surface real reasons

Stated exit reasons tend to be polite simplifications. Good question design gets underneath them.

- **Walk the timeline instead of asking "why did you leave?"** "Take me back to when you first started considering alternatives. What was happening?" People reconstruct events more honestly than they summarize reasons.
- **Ask about the moment of doubt.** "Was there a specific point where you started to feel this wasn't going to work?"
- **Probe the decision process.** "Who was involved in the decision? What did the evaluation look like? What did the alternative offer that we didn't?"
- **Follow up on generic answers.** If they say "missing features," ask "which ones, and when did that become a problem?" If they say "support issues," ask for an example.
- **Ask a counterfactual.** "If we'd done one thing differently, would you have stayed? What would it have been?" This is often the single most revealing question.
- **Close by giving permission.** "Is there anything you wanted to tell us but didn't feel you could?" People sometimes save the real answer for the end.

Avoid leading questions that favor either VP's hypothesis. "Were our analytics features a factor?" plants the answer. Let them raise topics unprompted, then probe.

## When they won't take the call

For non-responders, you still have options:

- **A short written survey** (five questions, mostly open-ended) that can be completed anonymously.
- **Former employees of churned carriers.** People who have since changed jobs are often more candid, and they're reachable through LinkedIn.
- **Your own records.** Tickets, QBR notes, escalation logs, and emails from the final year are data that doesn't require their cooperation, and they're less prone to after-the-fact rationalization.
- **Partners and implementers.** If you work with system integrators or consultants, they often know exactly why a carrier left.

## Making the results credible

- **Share the interview guide with both VPs before you start.** If either thinks the questions are biased, fix it now rather than having them dismiss the findings later.
- **Record and transcribe where permitted**, so conclusions rest on customers' words rather than an interviewer's summary.
- **Code responses systematically**, tagging each conversation for root causes, triggers, and decision factors, and compare with the cohort data from your records.
- **Close the loop.** A short thank-you note, and later a message about what you changed, costs little. In a small industry, a former customer who sees you took their feedback seriously may speak more kindly of you, and occasionally comes back.

If helpful, I can draft the outreach email and a 20-minute interview guide tailored to regional carriers.

## Turn 3

**User:** How should I handle it if the exit interviews and our internal data point in different directions, like customers saying "missing features" while their ticket history shows stalled implementations?

**Assistant:**

Treat the disagreement as a finding in its own right rather than a contradiction to resolve by picking one source. Stated reasons and behavioral data measure different things, and the gap between them often tells you more than either alone.

## Why the two sources can diverge

There are several explanations, and they have different implications:

1. **The features exist but were never implemented.** This is common and often the single most important thing to check. Customers stuck in long implementations may never have seen the reporting, dashboards, or automation you already offer. From their side, those features are genuinely "missing." Compare the specific features they cite against your product and against what was configured for them.
2. **Different people, different vantage points.** The executive who made the decision talks about capabilities and strategy. The users who filed the tickets experienced the implementation. Both accounts can be accurate descriptions of different parts of the same failure.
3. **Face-saving.** "Missing features" is an impersonal, low-conflict explanation. "Your team never got us live" is a direct criticism that's harder to say, especially to someone at the vendor.
4. **A causal chain.** The implementation stalls, the customer never reaches value, and at renewal a competitor's polished analytics demo looks far better than the half-working system they have. The feature comparison was the trigger for leaving, but the stall was the root cause.
5. **A real product gap, with the stall as a symptom.** Sometimes implementations stall because the product can't do what the customer needs without heavy customization or workarounds. In that case the tickets and the exit reason point to the same underlying problem.
6. **Two independent problems.** Some accounts may have both a painful implementation and a genuine competitive gap that would have driven them away anyway.

## How to work out which explanation applies

**Reconcile at the account level, not in aggregate.** For each churned account, lay out a single timeline: contract signed, planned vs. actual go-live, adoption milestones, ticket spikes, escalations, first mention of competitors or features, RFP issued, churn date. Sequence reveals a lot. If feature complaints appear only after the implementation stalled, that points toward explanations 1 or 4. If they appear early and the stall follows attempts to work around a limitation, that points toward 5.

**Map cited features against reality.** For each feature customers say was missing, classify it: existed and was configured, existed but was never implemented, partially existed, or genuinely didn't exist. This one exercise can shift the whole debate.

**Use fully implemented accounts as a control.** Look at churned customers who went live on time and reached solid adoption. If they also cite missing analytics or AI, the product gap is real. If feature complaints come almost entirely from stalled accounts, the implementation is the more likely root cause.

**Check where they went.** If stalled customers moved to competitors known for strong analytics, the competitive gap mattered at least as a trigger. If they moved to simpler tools or back to legacy systems, they were probably escaping complexity rather than seeking features.

**Go back to the customers.** Where you have a follow-up opportunity, ask directly without leading: "You mentioned reporting was a gap. Did you have access to our reporting module during implementation?" or "If you'd been fully live a year earlier, would the feature gap still have been decisive?"

**Watch for systematic source differences.** If executives consistently say "features" and users consistently describe implementation pain, that's a pattern worth reporting on its own. It suggests your sales and executive messaging may be setting expectations your delivery doesn't meet.

## How to present it to the two VPs

- **Report the chain, not a verdict.** "Most churned accounts stalled in implementation, never activated reporting, and then left for a competitor whose analytics impressed their executives" is more accurate and more useful than "Services was right" or "Product was right."
- **Quantify each category.** For example: "Of 20 churned accounts, 11 cited features we have but never implemented, 4 cited genuine gaps, 3 were acquired, 2 were unclear." Numbers keep either side from generalizing from the account that fits their view.
- **Show both sources side by side.** Present stated reasons next to behavioral evidence for each account so neither VP can dismiss one source.
- **Refer back to the pre-agreed criteria.** If you set "what would change your mind" thresholds at the start, now is when that investment pays off.

## What it means for action

The mix you find determines the response:

- **Mostly unimplemented features:** Invest in time-to-value, meaning faster implementations, phased go-lives that deliver reporting early, and making existing analytics more visible and easier to activate. Product can contribute by simplifying configuration rather than adding new capabilities.
- **Genuine gaps driving stalls:** Product work is warranted, but aim it at the specific capabilities causing workarounds, not at the general AI roadmap.
- **Two independent problems:** Fund both, sequenced by how much churn each explains.
- **A causal chain:** Fix the root cause first, but a targeted product response to the competitive trigger, such as a strong analytics demo or quick-start package, may buy time on renewals.

One caution: with a small sample, some accounts will remain ambiguous. That's fine. Report them as unclear rather than forcing them into a category, and use the leading indicators from your current customers to keep testing the conclusion as you act on it.

## Turn 4

**User:** What leading indicators should I track with our current customers so we can tell early whether whatever we change is actually reducing churn?

**Assistant:**

Because your contracts are likely annual or multi-year, churn itself is a lagging signal. A change you make today may not show up in renewal numbers for 12 to 24 months. Leading indicators let you see whether you're on track long before then, but only if you choose ones that actually predict churn for your customers.

## Step one: validate indicators against your churned accounts

Before relying on any metric, check whether it would have flagged the customers you already lost. Using the account timelines you built during the churn analysis, look back 6 to 12 months before each churn and compare churned accounts with retained ones. An indicator is useful only if it separated the two groups early enough to act.

This protects you from tracking metrics that seem sensible but don't predict anything, and it tells you which indicators deserve the most weight.

## Indicators by lifecycle stage

**Implementation (tests the Services hypothesis)**
- Actual vs. planned go-live date, and days of slippage
- Time to first value: days until the customer processes live claims in the system
- Milestone completion rate against the implementation plan
- Open implementation blockers and how long they stay open
- Scope changes and customization requests during implementation, which can signal a product fit problem

**Adoption and value realization**
- Share of the customer's claims volume running through your system, which is probably your strongest single signal
- Active users as a percentage of licensed adjusters and supervisors
- Breadth of use: which modules and workflows are live, especially reporting and analytics
- Depth of use: workflows automated, reports scheduled, integrations live
- Workarounds: exports to spreadsheets, shadow processes, parallel legacy systems still running

**Support and relationship health**
- Ticket volume and severity trends, especially repeat issues
- Escalations to management
- Time to resolution
- Executive sponsor engagement, such as QBR attendance and responsiveness
- Champion changes: sponsor departures, reorganizations, new leadership
- Sentiment from surveys or CSM assessments, used as a supplement rather than a primary signal

**Competitive and product-gap signals (tests the Product hypothesis)**
- Feature requests tied to analytics or AI, and whether they concern capabilities you already have
- Customers asking about the roadmap or competitor capabilities in QBRs
- RFPs issued, consultants hired, or reference checks on competitors
- Activity among fully adopted customers, since competitive pressure there points to a genuine gap rather than an implementation problem

**Account-level risk factors**
- Merger or acquisition activity involving the carrier
- Budget or leadership changes
- Contract terms, such as auto-renewal vs. an open renewal decision

## Connecting indicators to each hypothesis

Map each change you make to the indicators it should move. If you invest in implementation, you should see shorter time to first value, less go-live slippage, and higher early adoption within the first few months. If you invest in product, you should see higher use of the new capabilities, fewer related feature requests, and less competitive activity among adopted customers.

Write these expected effects down before launching the change, including how much movement you'd consider success and by when. Otherwise it's easy to interpret any movement as proof that the change worked.

## Measuring whether changes are working

- **Establish baselines now.** Capture current values for your key indicators before changes take effect.
- **Compare cohorts.** Compare customers who went through the new implementation process with those who went through the old one, at the same point in their lifecycle. Compare the same stage, not the same calendar date.
- **Stage rollouts where possible.** If you pilot a new onboarding approach with some customers first, the others provide a rough comparison group. It won't be a perfect experiment, but it's much better than a before-and-after on everyone.
- **Keep checking that the indicators still predict churn.** As renewals occur, confirm that accounts with strong indicators actually renewed. If the relationship weakens, adjust.

## Health scores: useful, with caveats

A composite health score can summarize these signals for your CSMs, but be careful:
- Weight inputs by how well they predicted churn in your historical data, not by intuition.
- Keep the individual components visible. A single score can hide what's actually going wrong.
- Don't make the score a target for CSMs. Once people are evaluated on a metric, they'll find ways to move it without improving the underlying reality, such as encouraging logins that don't reflect real use.

## Cadence and reporting

- **Weekly:** implementation status, escalations, and red-flag events such as sponsor departures, RFPs, or M&A news, so at-risk accounts get attention quickly
- **Monthly:** adoption and support trends by cohort
- **Quarterly:** a review with both VPs covering whether the changes are moving the expected indicators, how at-risk accounts are trending, and what renewals have confirmed or contradicted

## Pitfalls to watch

- **Small numbers.** With a customer base of regional carriers, a few accounts can swing percentages. Look at individual accounts alongside aggregates.
- **Survivorship.** Your current customers are the ones who didn't leave. Indicators drawn only from them may miss what drove the churners away.
- **Over-reliance on satisfaction scores.** Customers often report reasonable satisfaction right up until they leave. Behavioral data is usually more predictive.
- **Confounding changes.** If you change onboarding, pricing, and CSM coverage at the same time, you won't know which one helped. Stagger changes where you can, or at least record when each took effect.

If it's useful, I can help you sketch a first version of the indicator list with target thresholds, or a simple dashboard layout for the quarterly review with both VPs.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the plan pulled together into a sequence you can act on. The short version: protect revenue now, run a fast diagnostic that both VPs agree to in advance, and let the evidence decide how investment is split between Services and Product.

## Weeks 1–2: set up and stop the bleeding

- **Align both VPs on the process, not the answer.** Get agreement that you'll run a time-boxed diagnostic, and have each write down what evidence would change their mind. Ideally get your CEO or COO to sponsor it so the result carries weight.
- **Triage at-risk accounts.** Flag current customers with stalled implementations, low adoption, sponsor changes, or renewals in the next 6–9 months. Assign each a named owner and a save plan. This protects revenue while you diagnose.
- **Freeze the debate on big commitments.** Avoid major new roadmap bets or services reorganizations until the diagnostic is done, unless they're clearly no-regret.

## Weeks 2–6: diagnose

- **Build account timelines for churned customers.** Tenure, implementation duration, go-live status, adoption, ticket and escalation history, destination, and stated reason.
- **Run exit interviews** with a neutral interviewer, targeting 10–15 conversations, using a guide both VPs have reviewed.
- **Check the "missing" features.** Classify each cited gap as implemented, available but never implemented, partial, or truly absent. This single exercise may settle much of the argument.
- **Rule out outside causes** such as acquisitions, suite consolidation, and pricing changes, and identify what changed internally around when churn started rising.

## Weeks 6–8: decide

- **Present findings as a causal chain with counts.** For example: "11 of 20 stalled and never activated reporting; 4 left for real gaps; 3 were acquired; 2 unclear."
- **Allocate investment by evidence.** Most likely you'll fund both areas, but the proportions and sequence should follow what explains the most churn.
- **Make time-to-value a shared metric** owned jointly by Product and Services, so it stops being a turf fight.

## Months 3–12: act and measure

- **Launch changes with stated expectations.** For each change, write down which indicators should move, by how much, and by when.
- **Pilot before scaling where possible**, such as a new onboarding approach with a subset of new customers.
- **Track validated leading indicators:** time to first value, share of claims volume in the system, module adoption (especially reporting), escalations, sponsor stability, and competitive signals among fully adopted customers.
- **Review quarterly with both VPs** and adjust as renewals confirm or contradict the indicators.

## If I had to bet before seeing your data

Long implementations are a well-known weakness in claims software, and customers who never reach full value often explain their departure in terms of features. So I'd expect the evidence to show time-to-value as the bigger driver, with competitive AI and analytics acting more as the trigger at renewal. That's a prior, not a conclusion. If your fully implemented, long-tenured customers are also leaving for competitors, the product gap is real and deserves priority.

## Your role

As head of CS, you're well placed to run this as the neutral party. Neither VP owns the outcome, you hold the customer relationships, and you'll own the leading indicators afterward. Be ready to examine CS's own contribution too, such as coverage, renewal process, and early warning, since that credibility is what will make both VPs accept the result.

If you'd like a next step, I can draft the one-page proposal to take to your CEO and the two VPs, laying out the diagnostic, timeline, and decision criteria.

## Outcome summary (sent to Jev)

The assistant does not declare either VP right. Instead it recommends protecting revenue immediately, running a fast, time-boxed diagnostic that both VPs agree to in advance, and letting the evidence decide how investment is split between Services and Product. Both explanations are plausible and not mutually exclusive, and other causes such as acquisitions, suite consolidation, pricing changes, champion turnover, or an internal shift around when churn began may be involved.

**Weeks one to two**
- Have each VP write down what evidence would change their mind, ideally with CEO or COO sponsorship.
- Triage at-risk accounts with named owners and save plans.
- Hold off on major roadmap bets or services reorganizations unless they are clearly no-regret.

**Weeks two to six**
- Build timelines for each churned account.
- Run 10–15 exit interviews through a neutral interviewer using a guide both VPs have reviewed.
- Classify every "missing" feature customers cite as implemented, available but never implemented, partial, or truly absent.
- Use fully implemented churners as a control, and reconcile stated reasons with behavioral data account by account.

**Weeks six to eight**
- Present findings as a causal chain with counts, not a verdict.
- Allocate investment by what explains the most churn, most likely funding both areas.
- Make time-to-value a shared metric owned jointly by Product and Services.

**Months three to twelve**
- Launch changes with written expectations for which indicators should move, by how much, and by when.
- Pilot before scaling.
- Track validated leading indicators such as time to first value, share of claims volume in the system, reporting adoption, escalations, sponsor stability, and competitive signals among adopted customers.
- Review quarterly.

The assistant's prior is that time-to-value is the bigger driver, with AI and analytics acting as a renewal trigger. It stresses this is not a conclusion: if fully implemented, long-tenured customers are also leaving, the product gap deserves priority. The CS leader should run this as the neutral party while honestly examining CS's own contribution.
