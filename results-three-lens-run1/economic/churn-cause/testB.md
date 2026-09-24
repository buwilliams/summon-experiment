# economic/churn-cause/testB

Model: claude-opus-5-5 · 2026-09-24T14:52:42.842464+00:00

## Turn 1

**User:** You are a world-class expert: an economist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Short answer

Neither VP has shown they're right, and the question as framed ("product or service?") is probably wrong. Both are offering hypotheses that happen to justify more investment in their own function. The data you already have can settle this in a few weeks, and the two stories make different, testable predictions.

My prior, which I'd hold loosely, is that **time-to-value is the bigger lever for your recent cohorts, while product gaps are real but overstated in exit narratives.** Timing, though, is the strongest point in Product's favor, and you should take it seriously.

# The question that matters most: what changed?

Churn didn't just rise. It doubled in 18 months. So you're not explaining why customers churn; you're explaining **what changed about 18–24 months ago.**

- If implementations have always been long and painful, that alone can't explain a doubling. Services' story only works if implementation got *worse*. Possible causes include a new release that's harder to deploy, implementation staff turnover, selling to larger or more complex carriers, or scaling sales faster than delivery capacity.
- Product's story has a natural "what changed": the generative-AI wave. Starting around 2023, carrier boards began asking their CIOs "what's our AI strategy?", and AI-native claims vendors began marketing aggressively. That matches your window almost exactly.

So ask Services directly: *"Show me that implementation got worse, not just that it's bad."* If they can't, their story explains a baseline, not the spike.

# What each hypothesis predicts

Build a single dataset of every account that churned or renewed in the last 24–36 months. Then check which pattern it matches.

| Signal | Product-gap story predicts | Implementation story predicts |
|---|---|---|
| **Who churns** | Mature, fully live, well-adopted accounts | Recent cohorts, often at first renewal |
| **Go-live timing** | No relationship to churn | Late or overrun go-lives churn far more |
| **Adoption before exit** | High usage, then departure | Low usage, partial rollout, workarounds |
| **Where they went** | A named competitor with AI/analytics | Anywhere, including a core-suite bundle or back to legacy |
| **New sales** | Win rate also falling, losses cite features | Win rate stable; problem is post-sale |
| **Feature requests** | Requests for things you truly lack | Requests for things you *already have* but they never deployed |

That last row is the most useful single test. Pull churned customers' stated feature gaps and check how many already exist in the product. If a large share do, "missing features" is really "never reached value," and customers are rationalizing.

# Why exit interviews will mislead you

Customers who leave usually cite features, because it's a clean, blameless reason that procurement and the board accept. "We never finished implementing it" implicates their own team. Weight behavioral data (adoption, timing, destination) far above stated reasons.

# Two other explanations neither VP raised

1. **Market structure.** Regional carriers are consolidating. If a meaningful share of churn comes from acquired carriers moving onto the acquirer's platform, neither roadmap nor onboarding fixes it. Separate that out first, because it can distort everything else.
2. **Core-suite bundling.** When a carrier replaces its policy/billing core with a suite vendor, claims often comes along "for free." That's a platform-strategy problem (integrations, partnerships, pricing), not a feature or service problem.

Also check **executive sponsor turnover**. The departure of the champion who bought you is often the single best churn predictor in enterprise software.

# What I'd do

**Weeks 1–4: diagnose.**
- Build the churn file: cohort, ARR, time-to-go-live versus plan, adoption depth, escalations, sponsor changes, M&A events, and where each customer went.
- Run survival curves by cohort and by implementation duration.
- Have someone neutral own this, such as Finance, RevOps, or you. Not either VP.

**Meanwhile, no-regret moves:**
- Triage every renewal in the next two quarters. Low-adoption accounts get a value-recovery plan now.
- Define and measure one time-to-first-value milestone, such as first claims processed end-to-end, and track it for every new customer.
- On product, ship one or two narrow, credible AI/analytics capabilities that answer "what's your AI story?" in a renewal conversation. Claims triage or fraud and severity scoring are good candidates, and partnering is fine. You need to neutralize the objection, not win an arms race.

**Then set a decision rule in advance:**
- If churn concentrates in slow or low-adoption cohorts, fund implementation redesign first: productized deployment, fixed-scope launches, a deliberate CS handoff. It's cheaper, pays off within one renewal cycle, and makes any future features actually land.
- If healthy, well-adopted accounts are leaving for AI-forward competitors and win rates are falling, Product is right and the roadmap needs to accelerate.
- In practice you'll likely find a mix. Then allocate by revenue at risk, not by whoever argues better.

# One candid note

Implementation-to-adoption sits partly in customer success's lane, so this analysis may implicate your function too. Run it anyway, and present it as the neutral party. The executive who shows up with the data rather than a theory usually ends up setting the agenda.

## Turn 2

**User:** We've only lost about 25 accounts in that window. Is that enough data for the survival curves and cohort comparisons to actually tell us anything?

**Assistant:**

Partly. Twenty-five churn events is too few for the formal modeling I implied, but enough to answer your actual question if you change the method. I should have flagged this in my earlier answer.

# What 25 events can't do

- **Multivariate survival models.** A common rule of thumb is about 10 events per variable, so 25 churns support roughly two predictors. With more, you'll fit noise and get confident-looking nonsense.
- **Fine-grained cohort splits.** Slice 25 events by cohort, segment, and product module and you'll have cells with two or three churns each. Any "pattern" there is anecdote.
- **Detecting modest effects.** Suppose you have 25 churned and about 150 retained accounts. If 60% of churned accounts had overrun implementations versus 30% of retained, that gap is large enough to be unlikely to be chance. If it's 40% versus 30%, you can't distinguish it from noise.

# What they can do

- **Detect big effects, and those are the ones you care about.** If implementation pain drove a *doubling*, it should show up as a large gap, not a subtle one. If the difference between churned and retained accounts is too small to see at this sample size, it probably isn't what doubled your churn. A null result is informative here.
- **Support simple two-group comparisons.** Churned versus retained, late versus on-time go-live: use a simple 2×2 table with Fisher's exact test. Don't use regression.
- **Support rich case analysis.** With 25 accounts, you can study every one in depth, which beats thin statistics on a large sample.

# How I'd restructure the diagnostic

**1. Check that the doubling is real.** With small counts, "doubled" can be noise. Going from about 12 to 25 is very unlikely to be chance. Going from 5 to 10 could be. Also check whether it's driven by logos or revenue, and whether three or four acquisitions or one large account explain much of it. Settle this first.

**2. Replace survival curves with structured account autopsies.** Write a one-page case for each churned account covering:
- go-live timing versus plan
- adoption depth
- escalations
- sponsor changes
- M&A events
- where they went
- whether their stated feature gaps already exist in your product

Then code each account against the hypotheses: product gap, time-to-value, consolidation, suite bundling, sponsor loss, or mixed. Have two people code independently and reconcile, so no one's priors, including the VPs', drive the labels.

**3. Build a comparison group.** Autopsies of churned accounts alone will find problems everywhere, because every account has some. Run the same autopsy on 25 to 40 retained accounts, ideally similar in size and tenure. The question is whether churned accounts look different, not whether they had problems.

**4. Add more outcome events.** Treat downgrades, contracted seats, stalled rollouts, and currently at-risk renewals as additional signals. These are noisier, but they could triple your sample, and they tell you where the next 25 churns are coming from.

**5. Use sales data for the product question.** Win/loss records on new deals give you many more observations about competitive pressure than your churn list does. If Product is right, lost deals should also cite AI and analytics gaps.

**6. Extend the window cautiously.** Going back to 36–48 months adds churn events but mixes the pre-change and post-change periods. Use the older data as a baseline, not as part of the main analysis.

# How to use the results

You don't need statistical significance to make this decision. You need enough evidence to update a prior and allocate a budget. If 17 of 25 churned accounts share a clear pattern, like never reaching full deployment or leaving healthy for an AI-forward competitor, act on it.

Match your confidence to the evidence. Make reversible, staged bets, such as fixing the next six implementations or shipping one targeted AI capability, rather than a full reorganization or a roadmap overhaul. Then treat the next few quarters of renewals as your validation sample.

## Turn 3

**User:** Our records on go-live dates and usage are pretty spotty for the older accounts, so how do we piece that together reliably for the autopsies?

**Assistant:**

You won't get clean records back, but you don't need them. The goal is to place each account in the right broad category with a stated confidence level, not to recover exact dates. Triangulating from several imperfect sources does that well.

# 1. Define the measures before you dig

Write short operational definitions so everyone reconstructs the same thing:

- **Go-live:** first real claim processed in production, not the contractual or announced date.
- **Full deployment:** the system handles most of the carrier's claims volume across the intended lines of business, for example 80% or more.
- **Overrun:** actual go-live against the date in the original statement of work.

Then use **coarse categories** rather than exact values:

- Go-live: on time, moderately late (up to ~3 months), severely late (more than 3 months), never fully live.
- Adoption: full, partial, minimal.

The effect you're looking for should be large, so broad buckets are enough, and they're much easier to fill reliably from messy evidence.

# 2. Mine the proxies

Most of this evidence exists somewhere even when no one recorded it as "go-live date."

**Financial records (often the most reliable, because Finance keeps everything)**
- Implementation invoices, especially milestone-based billing. A "go-live" milestone invoice is strong evidence.
- Change orders and statement-of-work amendments, which signal scope creep and delays.
- Services hours billed over time. A long tail of billed hours suggests a stalled implementation.
- Seat counts, module add-ons, or downgrades at renewal.

**System and technical evidence**
- Production environment provisioning dates.
- Claims volume in the production database over time. The first real transactions mark go-live, and the volume curve shows the ramp.
- Login, API, or integration logs, if they've been retained.
- Before you rely on these, check your contracts' data-deletion terms and ask Legal what you can use for churned accounts. Some data may survive in backups or a data warehouse even if the application records are gone.

**Support tickets**
- The first ticket referencing production issues is a good go-live proxy.
- Ticket topics tend to shift from configuration and data migration to workflow and "how do I" questions after go-live. Accounts stuck in configuration topics for a year are a telling sign.
- Escalation frequency and severity.

**Project and communication artifacts**
- Project plans, Jira or Smartsheet boards, status reports.
- Kickoff and go-live announcement emails, calendar invites for cutover weekends.
- Business review decks, CS notes, renewal-risk notes in the CRM.

**People**
- Current and former implementation managers, CSMs, and account executives. Short interviews recover a lot, but memory is the weakest source, so use it to fill gaps and interpret documents, not as primary evidence.
- Former customer champions or users, if relationships allow. Even a few 20-minute conversations can be very revealing.

**An outside check on adoption**
Regional carriers file annual statutory statements, and state filings or rating-agency data give rough claim volumes by line of business. Compare the claims volume running through your system with the carrier's approximate total. That gives you an independent estimate of penetration, which is useful when internal usage data is thin.

# 3. Grade every data point by confidence

For each field in each autopsy, record the value, its source, and a confidence grade:

- **A:** system data or financial records, such as production transactions or milestone invoices.
- **B:** documents, such as project plans, emails, or CRM notes.
- **C:** recollection only.

If sources conflict, record a range, for example "went live between March and June." Don't force a single point estimate. The confidence grades tell you how much weight each conclusion can bear.

# 4. Avoid the two biases that could sink this

**Unequal record quality between churned and retained accounts.** This is the biggest risk. Churned accounts may have purged data, or they may be *better* documented because they were escalated. Either way, you can manufacture a difference that isn't real. Reconstruct the retained comparison group with exactly the same method, sources, and effort.

**Knowing the outcome while coding.** Someone who knows an account churned will read its history more harshly. Where you can, have someone assemble the evidence packets and a different person code them without being told which accounts churned. Imperfect blinding still helps.

Also, **don't treat missing data as evidence of failure.** A thin file may reflect poor record-keeping at the time rather than a troubled account. Code it as "unknown."

# 5. Timebox and stress-test

- Budget about 3–4 hours per account. With 25 churned and 25–40 retained accounts, that's a few weeks of part-time work for two or three people.
- Run the analysis with all accounts, then again with only accounts graded A or B. Also flip the ambiguous cases to the less favorable category and see if the result holds. If the conclusion survives these tests, trust it. If it depends on a few C-grade accounts, treat it as a hypothesis, not a finding.

# 6. Fix the records going forward

This exercise will show you exactly which data you wish you'd had. Start capturing it now for every new customer:

- go-live against plan
- time to first value
- adoption depth, including the share of the carrier's claims volume in your system
- sponsor changes

Next year's version of this analysis will then take days instead of weeks, and you'll spot at-risk accounts before they reach renewal.

## Turn 4

**User:** Both VPs will want a say in how accounts get coded, so how do I keep them involved without letting them skew the results?

**Assistant:**

Give them real influence over how the analysis is *designed*, and none over how individual accounts are *labeled*. Most bias enters when someone who already knows the outcome interprets ambiguous evidence. If both VPs shape the rules before anyone looks at the data, they get genuine ownership, and the coding itself stays neutral.

# Before anyone sees data: involve them heavily

**1. Have each VP state, in writing, what would prove them wrong.**
Ask each one: "What pattern in the data would convince you the other explanation matters more?" For example:
- Product might say: "If most churned accounts never fully deployed, I'd accept that implementation is the main problem."
- Services might say: "If healthy, well-adopted accounts left for AI-forward competitors, I'd accept that it's product."

This is the most important step. Once someone commits in advance to what would change their mind, it's much harder to explain away an unwelcome result later.

**2. Let them co-write the codebook.**
Both VPs review and sign off on the definitions (go-live, full deployment, overrun), the categories, and the evidence standards. Encourage each to add categories they think are missing. It's better to argue about the definition of "never fully live" now than about a specific account later.

**3. Let each nominate evidence sources.**
Product may point to lost-deal records and competitor mentions. Services may point to change orders and escalation logs. Include both, so neither can later claim the evidence was stacked.

**4. Agree the decision rule up front.**
Before any coding, agree roughly what results lead to what investment. For instance: "If most revenue-weighted churn traces to implementation failure, the next two quarters' incremental budget goes to onboarding." Get your CEO or COO to endorse this rule. That turns the exercise from a verdict on people into a budget decision both VPs have already accepted.

# During coding: keep them out of the labels

**5. Use neutral coders.**
Assign the coding to people without a stake, such as RevOps, Finance, a strategy analyst, or an outside contractor. Keep outcome-blinding where you can, as discussed earlier.

**6. Let the VPs check facts, not interpretations.**
Each VP can review the evidence packets for errors: a wrong date, a missing document, a misattributed ticket. They cannot propose or edit labels. Correcting facts improves accuracy. Arguing over labels brings back the bias you're trying to remove.

**7. Use a formal, symmetric challenge process.**
If a VP disputes a coding decision:
- The challenge must be in writing and cite specific evidence.
- A neutral person decides it and logs the decision.
- If the challenge exposes a rule problem, fix the rule and apply it to *every* account, not just the disputed one.
- Give both VPs the same challenge budget.

That last point matters: a rule change that helps one side on one account will often cut the other way on others, which discourages opportunistic challenges.

**8. Allow mixed causes.**
Code each account with a primary cause and contributing causes. Many churns really are mixed. For example, a stalled implementation leaves the customer open to a competitor's AI pitch. Allowing this reflects reality and makes coding less zero-sum.

# When reporting: make the result hard to dismiss

**9. Show the results under each VP's reading of the ambiguous cases.**
Run the analysis three ways: the neutral coding, the coding with ambiguous accounts resolved Product's way, and the coding with them resolved Services' way.
- If the conclusion holds in all three, the debate is essentially over.
- If it flips, the honest answer is that the evidence is mixed, which argues for a split or staged investment rather than an all-in bet.

**10. Present patterns, not blame.**
Frame findings as "where the revenue is leaking and what fixes it," not "who was right." Expect that both functions will probably come out with part of the answer and part of the budget. Say so from the start, which lowers the stakes for both VPs.

# One more thing: apply the rules to yourself

Customer success owns part of the path from implementation to adoption, so you have a stake too. Put yourself under the same rules: write down your own prediction in advance, stay out of the labeling, and let the neutral coders apply the codebook to accounts where CS may have fallen short. Visibly holding yourself to the process is what gives you the credibility to hold both VPs to it.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the whole plan in sequence: protect revenue now, run a fast and fair diagnosis, then make staged bets you can adjust as renewals come in.

# This week: set it up

1. **Get your CEO or COO to sponsor it.** Frame it as "we have two competing explanations for churn doubling; let's spend six weeks finding out before we commit major budget." Agree that the results will drive the next two quarters' incremental investment.
2. **Hold one meeting with both VPs.** Have each write down their prediction and what evidence would change their mind. Agree on definitions, categories, and the decision rule. Write your own prediction too.
3. **Name a neutral lead and coders**, from RevOps, Finance, or strategy, and give them the time.

# Right away, in parallel: no-regret moves

These make sense whichever VP turns out to be right.

- **Triage the next two quarters of renewals.** Any account with low adoption, an incomplete rollout, or a lost sponsor gets a value-recovery plan and executive attention now.
- **Start measuring the basics for every new and in-flight customer:** go-live against plan, time to first value, share of claims volume in the system, and sponsor changes.
- **Give renewal conversations a credible AI story.** Identify one or two narrow capabilities you can ship or partner for quickly, such as claims triage or severity scoring. The aim is to neutralize the objection, not to overhaul the roadmap yet.

# Weeks 1–6: diagnose

1. **Confirm the doubling is real.** Check whether it holds by logo and by revenue, and separate out churn from acquisitions and core-suite bundling, since neither VP's fix touches that.
2. **Autopsy all 25 churned accounts and 25–40 retained ones.** Use the same methods and sources for both, grade each data point by confidence, and keep coders blind to outcomes where possible.
3. **Pull win/loss data from new sales** to test the competitive-gap story on a larger sample.
4. **Stress-test the results**: all data versus high-confidence data only, and ambiguous cases resolved each VP's way.

# Around week 7: decide and invest in stages

Apply the rule you agreed up front:

- **If churn concentrates in stalled or low-adoption accounts:** lead with implementation redesign. That means standardized, fixed-scope launches, a clear handoff to customer success, and a time-to-value target. Pilot it on the next five or six implementations, then scale what works.
- **If healthy, well-adopted accounts are leaving for AI-forward competitors, and new-deal losses say the same:** accelerate the roadmap on the specific capabilities cited in lost deals, not a broad AI push.
- **If it's mixed, which is likely:** split incremental budget in proportion to revenue at risk from each cause, and revisit quarterly.

In every case, **use upcoming renewals as your test.** Set targets for retention and time to value, and check them each quarter. Shift investment based on what the numbers show, not on the original debate.

# My lean, for what it's worth

I expect the diagnosis to show that **time to value is the bigger and faster lever**, especially for recent customers, and that **product gaps are real but mainly matter when customers compare you with competitors**, both at renewal and in new sales. If so, fix implementation first, because it pays back within one renewal cycle and makes any new features actually land, while shipping enough targeted AI to stay credible.

That's my prior, though, not a conclusion. Run the six weeks and let the evidence decide.

## Outcome summary (sent to Jev)

Neither VP's explanation is established. The question isn't really "product or service" but what changed 18–24 months ago to double churn. The assistant recommends a six-week, CEO- or COO-sponsored diagnosis, run by a neutral lead from RevOps, Finance, or strategy, while taking no-regret steps in parallel.

The no-regret steps are:
- Give every renewal in the next two quarters with low adoption, incomplete rollout, or a lost sponsor a value-recovery plan.
- Start tracking go-live against plan, time to first value, share of claims volume in the system, and sponsor changes.
- Ship or partner for one or two narrow AI capabilities, such as claims triage or severity scoring, to neutralize the objection at renewal.

The diagnosis first confirms the doubling holds by logo and revenue, and separates out churn from acquisitions and core-suite bundling. Twenty-five churn events are too few for survival models, so it relies on structured autopsies instead. It covers all churned accounts plus 25–40 comparable retained ones, using identical methods. Coarse categories and confidence-graded evidence come from invoices, system data, tickets, documents, interviews, and statutory filings. Coders stay neutral and, where possible, blind to outcomes. Win/loss data from new sales tests the competitive-gap story.

Each VP helps design the codebook, states in writing what would prove them wrong, and agrees to a decision rule in advance. They may check facts but not assign labels. Results are stress-tested using high-confidence data only and with ambiguous cases resolved each VP's way.

The decision rule:
- If churn concentrates in stalled or low-adoption accounts, pilot fixed-scope implementations.
- If healthy accounts are leaving for AI-forward competitors, accelerate the specific capabilities cited in lost deals.
- If causes are mixed, split budget by revenue at risk.

The assistant leans toward time to value as the bigger, faster lever, but calls this a prior rather than a conclusion. It advises staged, reversible bets validated against upcoming renewals, and notes that customer success itself may be implicated.
