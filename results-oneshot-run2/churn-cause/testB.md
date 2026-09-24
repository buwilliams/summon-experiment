# churn-cause/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T13:04:03.979119+00:00

## Prompt

You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

# Neither Belief Is Proven Yet

Right now, neither belief is proven. Both VPs are offering a hypothesis shaped by where they sit. The either/or framing is the real trap: in enterprise vertical software the two causes are usually entangled, and you can separate them with data you probably already have, in about a month.

My prior, from watching this pattern many times: when implementations are long and customers never reach full value, **failed value realization is usually the primary driver, and "product gaps" is the stated reason.** A customer who never got full value from you will judge a competitor's AI demo against a product they barely use. "Your competitor has better analytics" is also a more comfortable thing to say at exit than "our rollout stalled and we gave up." But the generative-AI wave has genuinely shifted carrier buying criteria over roughly the same 18 months your churn doubled. So treat the product hypothesis as live, not as an excuse.

## Test Hypotheses That Make Different Predictions

Pull every churned account from the last 18 months and a comparable set of retained accounts, then check:

| Evidence | If it's mainly **service/value** | If it's mainly **product gaps** |
|---|---|---|
| Adoption before churn (modules live, % of claims in system, active adjusters) | Churned accounts were under-adopted or never fully live | Churned accounts were healthy, fully adopted users |
| When they started evaluating alternatives | During or soon after a troubled implementation | After a competitor launch or at renewal, despite being satisfied |
| Support escalations 6–12 months before churn | Elevated | Normal |
| Features cited as reasons for leaving | Often features you already have that they never adopted | Features you genuinely lack |
| Where they went | Anywhere, including simpler tools | Specifically to competitors with the cited capabilities |
| New-business win/loss | Mostly unaffected | You are also losing new deals on the same features |
| Implementation duration by cohort | Has lengthened in recent cohorts | Flat |

The first row carries the most weight. **Are healthy, fully adopted customers leaving?** If they are, you have a product problem. If churn is concentrated among accounts that never got to value, you have a service problem, and building features won't fix it. New features will just add scope to already-long implementations.

## Rule Out a Third and Fourth Explanation

Before crediting either VP, check two drivers that often explain regional-carrier churn and fit neither story:

1. **Core-suite consolidation.** Regional carriers modernizing their policy and billing systems often buy a suite (Guidewire, Duck Creek, etc.) and take claims along with it. If churned accounts moved to suites, you're losing a platform decision, not a feature comparison. That calls for a different response: partnerships, integrations, or repositioning.
2. **Carrier M&A.** Acquired carriers get absorbed into the acquirer's systems. That churn is structural and should be separated out so it doesn't distort the analysis.

Also remember contract lag. Claims software typically runs on multi-year contracts, so today's churn reflects implementations and experiences from 2–4 years ago. Ask what changed back then: implementation team turnover, a push into a new segment, discounting that brought in poorly fitting customers, or a release that broke things.

## Be Skeptical of Exit Interviews

Talk to both the economic buyer and the claims operations leads. They often give different reasons, and the ops leads usually know the truth. The most revealing question is: *"When did you first start seriously considering alternatives, and what was happening at that moment?"*

## What to Do Now

**1. Run a 30-day joint churn diagnostic, and own it yourself.** Customer success is the neutral party. Before looking at any data, have both VPs write down what evidence would change their mind. This pre-commitment keeps the exercise from turning into dueling anecdotes.

**2. Take "no-regret" actions immediately.** These make sense under either hypothesis:
- Triage every renewal due in the next 12 months by adoption health. Assign executive sponsors to the at-risk accounts.
- Define and instrument **time-to-value**, meaning a specific milestone such as "80% of claims processed in-system." Report it by cohort from now on. You can't manage what you don't measure, and I suspect you don't currently measure it.
- Do not freeze the roadmap or reorganize services until you have the data.

**3. Expect a mixed answer and sequence the response.** The most likely finding is that value failure drives most churn, while real feature gaps drive some churn and new-deal losses. If so:
- Prioritize fixing implementation and adoption for the installed base. Retention economics usually dominate here, and a customer who reaches full value is far less susceptible to a competitor's demo.
- Make targeted product bets on the specific gaps cited by healthy customers who left, not the general "we need AI" narrative.
- Favor product investments that serve both goals. AI-assisted data migration, configuration, claims triage, and in-product guidance shorten implementations *and* close the perceived innovation gap. That is where your two VPs' agendas converge, and it's a good way to end the argument with both of them owning the plan.

## The Bottom Line

The question to answer is not "features or service?" It is **"Are customers who got full value still leaving us?"** Answer that first, and the right allocation of investment will be clear.

## Summary (sent to Jev)

The response argues that neither VP's belief is proven. Each is a hypothesis shaped by where that VP sits, and the either/or framing is a trap because the two causes are usually entangled. They can be separated in about a month with data the company likely already has. The author's prior is that when implementations run long, failed value realization is usually the primary driver and "product gaps" is the stated reason. Still, the product hypothesis should stay live, because generative AI has genuinely shifted carrier buying criteria over the same period.

The proposed test compares churned and retained accounts on several measures: adoption before churn, when customers began evaluating alternatives, support escalations, which features they cited, where they went, new-business win/loss, and implementation duration by cohort. The decisive question is whether healthy, fully adopted customers are leaving. If they are, it is a product problem. If not, it is a service problem, and new features would only add implementation scope.

The response also says to rule out core-suite consolidation and carrier M&A, and to account for contract lag, since today's churn reflects experiences from two to four years ago. Exit interviews deserve skepticism. The author suggests interviewing both economic buyers and ops leads and asking when they first seriously considered alternatives.

Recommended actions:
- Customer success runs a 30-day joint diagnostic, with both VPs pre-committing to what evidence would change their minds.
- Take no-regret steps now: triage upcoming renewals by adoption health, assign executive sponsors to at-risk accounts, and define and track time-to-value.
- Avoid freezing the roadmap or reorganizing services until the data is in.

If the answer comes back mixed, the response advises prioritizing implementation and adoption fixes, making targeted feature bets, and favoring AI investments that both shorten implementations and close perceived gaps.
