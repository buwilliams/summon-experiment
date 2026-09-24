# churn-cause/testB

Model: claude-opus-5-5 · 2026-09-24T14:02:39.545550+00:00

## Turn 1

**User:** You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Diagnosing Your Churn: Product Gaps vs. Implementation and Service

**Short answer:** Neither belief can be confirmed yet, and the either/or framing is probably wrong. The two hypotheses make different, testable predictions, so you can settle this with your own data in about 4–6 weeks rather than by debate. Until then, don't reallocate major resources in either direction.

Both VPs have proposed a diagnosis whose remedy runs through their own organization. That doesn't make either of them wrong, but it's a reason to settle it with evidence both agreed to in advance.

## Step 1: Make sure you know what "churn doubled" means

Before testing causes, decompose the number. I've seen many "churn crises" turn out to be something else.

- **Logo vs. revenue churn.** With regional carriers, three or four large accounts can double a percentage.
- **Voluntary vs. involuntary.** Regional carriers consolidate constantly. A carrier acquired by a larger insurer that migrates to the parent's system is not a product or service failure. Strip these out.
- **Renewal calendar effects.** Did an unusually large cohort of multi-year contracts come up for renewal in this window?
- **Timing lag.** If yours is a core claims system, replacing it takes a carrier 12–24 months. Customers leaving now likely *decided* to leave 1–3 years ago. So look at what was happening then: implementations sold during that period, support reorganizations or staff attrition, a painful major release, a price increase. Today's roadmap gap relative to competitors' current AI features may postdate many of these decisions.

## Step 2: Test the predictions each hypothesis makes

| If the **product-gap** view is right, you'll see... | If the **service/implementation** view is right, you'll see... |
|---|---|
| Elevated churn among customers who were fully implemented and actively using the product | Churn concentrated among customers who never reached full value |
| Churners were heavy users who hit capability ceilings | Churners had low adoption and incomplete module rollout |
| Churners move specifically to competitors with stronger analytics/AI | Churners go to a mix of competitors, including ones without better AI |
| Churn is unrelated to implementation duration | Longer or troubled implementations strongly predict churn |
| New-business win rates are also falling, with losses citing analytics | Win rates are stable; the problem appears after the sale |
| Churn is spread across customer tenure | Churn clusters at the first renewal |

**The single most decisive analysis:** Define "reached full value" with concrete milestones (for example, live on all contracted modules, adjuster adoption above a threshold, key workflows in production). Split your customer base into those who reached it and those who didn't, then compare churn rates.

- **Churn concentrated in the never-activated group** points to implementation and service.
- **Activated customers also churning at elevated rates** means the product gap is real.
- **Both elevated** means you have two problems, and you'll know their relative size.

## Step 3: Be skeptical of stated churn reasons

CRM loss reasons and exit conversations are systematically biased toward "missing features."

- Citing a product gap is polite and politically safe for the buyer.
- It's also safe for the account team.
- A customer who never got value from you will find a competitor's polished AI demo very persuasive. That doesn't mean AI was the cause.

So weight behavioral data (telemetry, implementation records, support history) above stated reasons. If you do exit interviews, use a neutral third party and ask about the *history* of the relationship ("When did you first start considering alternatives? What was happening then?") rather than "Why did you leave?"

## Step 4: Consider the interaction between the two views

The most likely answer is that the hypotheses are connected.

- **Long implementations make you vulnerable to competitors.** A customer 14 months into a stalled rollout compares your unrealized promise with a competitor's pitch. Feature gaps become decisive only for customers who are already dissatisfied.
- **Long implementations may themselves be a product problem.** If your implementations run long because the product needs heavy configuration, custom integration, or data migration effort, the fix may be product investment, just not in AI. Configuration tooling, integration templates, and migration utilities could beat a new analytics module on ROI.

Also rule out other causes: pricing changes at renewal, turnover of executive sponsors at customer accounts, a competitor pricing aggressively to buy share, or support quality degrading after team attrition.

## What to do

**Weeks 0–6: run a joint diagnostic sprint.**
- Make both VPs co-owners. Before anyone sees the data, have them agree on what results would support each view and what resource shift would follow. Pre-committing to decision criteria prevents each side from reinterpreting ambiguous results as vindication.
- Pull these data sources: implementation duration and milestones, product usage data, support tickets and escalations, CSAT/NPS history, sponsor changes, competitor destination, and win/loss data.

**Meanwhile, take no-regrets actions.**
- **Protect upcoming renewals.** Build a simple health score, identify at-risk accounts renewing in the next 2–3 quarters, and assign executive sponsors. This pays off whichever hypothesis wins.
- **Triage stalled implementations.** Put a senior team on the currently stuck ones. Customers in trouble today are your churn 18 months from now.
- **Hold the roadmap steady.** Don't freeze it, but don't re-plan it wholesale either.

**After the diagnosis, allocate in proportion to the evidence.**
- **Mostly implementation and service:** fund onboarding and time-to-value work. Examine whether product investment in implementability belongs in that budget.
- **Mostly product gap:** accelerate the roadmap. Use churners' and lost deals' specific requirements to decide *which* analytics and AI capabilities to build, rather than matching competitors feature for feature.
- **Both:** sequence by where the churned revenue actually sits. Track leading indicators such as time-to-value, adoption, and health scores so you aren't waiting two years for churn numbers to tell you whether it worked.

**One final point:** carriers rarely rip out a claims system over a missing feature, because switching costs are enormous. When they do leave, it usually reflects accumulated dissatisfaction plus a trigger. That prior leans slightly toward the service hypothesis, or toward the interaction effect. But it's only a prior. Let your data decide.

## Turn 2

**User:** How do I actually define "reached full value" if our implementation records and usage data are patchy, and many older customers never had clear milestones tracked?

**Assistant:**

# Defining "Full Value" When Your Records Are Patchy

You don't need perfect data. You need a definition good enough to tell two hypotheses apart, applied consistently. Reconstruct a few simple, observable milestones from whatever evidence exists, record how confident you are in each classification, and check whether your conclusion holds across confidence levels.

## Step 1: Choose a few milestones you can observe after the fact

Skip abstract notions like "realized ROI." Use milestones that leave evidence behind:

1. **Live.** In production on the modules the customer contracted for.
2. **Volume.** Most of the carrier's claims actually flow through your system, not just one line of business or a pilot region.
3. **Breadth.** Most licensed users (adjusters, supervisors) are active.
4. **Integrated.** Core integrations are live, such as policy admin, payments, and general ledger.

Optionally, add a depth milestone: they use the automation, rules, or reporting features, not just basic claim intake.

Classify each customer as **Full** (all core milestones met), **Partial** (live but short on volume, breadth, or integration), or **Never** (not substantially live).

## Step 2: Mine indirect sources of evidence

Implementation records aren't your only source. Most companies have more evidence than they realize, scattered across systems:

- **Your production database.** The first production claim per module, or claim counts per customer over time, is often the best "go-live" record you have, even if nobody logged it.
- **Carrier size as a denominator.** Regional carriers file statutory statements, and NAIC data gives premium volume and, for some lines, claim counts. You can roughly estimate how many claims a carrier *should* be processing and compare that to what runs through your system. A carrier processing 20% of its expected volume isn't at full value.
- **Billing and contracts.** Services invoices that ran far past the original SOW, change orders, milestone payments, and fee disputes are all traces of troubled implementations.
- **Support tickets.** The first ticket about a module usually means it's live. Clusters of integration tickets show when integrations were attempted.
- **Seat and login data.** Compare active users to licensed users, even if you only have snapshots.
- **API and integration logs.** Recurring payment or policy-admin calls show an integration is actually running.
- **People.** Longtime CSMs, implementation consultants, and support leads remember a great deal. Run short structured interviews per account using the same milestone questions, not open-ended storytelling.
- **The customer.** For current customers, a short survey or CSM conversation ("Which lines of business run fully in the system?") fills gaps quickly.

## Step 3: Record your confidence in each classification

For each customer and milestone, note how the call was made:

- **High:** direct system or record evidence.
- **Medium:** strong indirect evidence, such as tickets, invoices, or consistent staff recollection.
- **Low:** best guess.

Then run the churn comparison three ways: high-confidence accounts only, high plus medium, and everyone. If the answer is the same each way (for example, churn concentrated in "Never/Partial" regardless), you can trust it despite the patchy data. If it flips depending on the subset, you've learned the data can't answer the question yet, which is also worth knowing.

## Step 4: Guard against the biases that most often sink this analysis

**Measure at a fixed point in time.** Assess value status at a set point, say 12–18 months after contract signing, and well before the renewal decision window. Customers who have already decided to leave stop adopting, so measuring near churn will make low adoption look like a cause when it's really a symptom.

**Classify without knowing the outcome.** Where possible, have people who don't know which customers churned do the coding, or at least fix the definitions and thresholds before anyone looks at churn status. Otherwise ambiguous cases drift toward whichever story the coder believes.

**Watch for missing data that tracks churn.** Churned customers' data may have been purged under contract terms, and troubled implementations are often the ones with the worst records. If missingness is concentrated among churners, say so explicitly and don't quietly exclude those accounts. Check whether "we have no records" itself correlates with churn, and interpret it cautiously.

**Sample if you have to.** If full reconstruction is too costly, code all churned accounts from the relevant period plus a comparable sample of retained customers, matched by signing year and size. Sixty to eighty well-coded accounts beat three hundred poorly coded ones.

## Step 5: Start tracking properly now

Whatever the diagnosis shows, this exercise will have defined your value milestones. Make them standard fields for every new and current implementation, reviewed quarterly as part of account health. In 12–18 months you'll have clean, leading data on time-to-value instead of reconstructing history from invoices and memory.

A realistic timeline is two to three weeks for a small team (an analyst, a CSM lead, and someone who can query the production database). That's well within the diagnostic window.

## Turn 3

**User:** We only lost about 20 to 25 customers over the last 18 months. Is that enough to draw any real conclusions from this comparison, or will the numbers be too small to mean anything?

**Assistant:**

# Is 20–25 Churned Customers Enough?

It's enough to detect a **large** difference, not a subtle one. That's more useful than it sounds, because the decision you face mostly hinges on whether there's a big, obvious pattern.

## Why small numbers can still be decisive

The statistical power of this comparison depends on the gap between the groups, not just the number of churned customers. Suppose you have about 170 customers in the relevant window and 22 churned. Here are two illustrative scenarios.

**Scenario A: a large effect.**

| Group | Customers | Churned | Churn rate | 95% range |
|---|---|---|---|---|
| Never/Partial value | 60 | 15 | 25% | ~16–37% |
| Full value | 110 | 7 | 6% | ~3–13% |

The ranges don't overlap. A standard test for small samples (Fisher's exact test) gives p ≈ 0.001, meaning a gap this size would almost never arise by chance. Twenty-two churners are plenty to conclude that value attainment matters a lot.

**Scenario B: a modest effect.** If churn were 17% versus 11%, the ranges would overlap heavily. You couldn't distinguish that from noise.

The practical implications:

- **A strong pattern is trustworthy.** If churn is heavily concentrated in one group, you can act on it.
- **"No difference" is not a finding.** A null result means "not a huge effect," not "no effect." Don't let either VP claim a null result as proof the other is wrong.
- **Decide your primary comparison in advance.** With small numbers, slicing the data many ways (by region, size, module, year, CSM) will produce spurious patterns. Pick one primary comparison beforehand and treat everything else as exploratory.

## How to extract more information from the same data

**1. Review every churned account in depth.** Small numbers let you do what large-scale analysis can't. Build a timeline for each account: signing, implementation milestones, escalations, sponsor changes, first sign of competitor contact, renewal decision. Then code each case against both hypotheses. When 16 of 22 timelines show the same sequence (a stalled rollout, then frustration, then a competitor evaluation), that's compelling evidence even without a p-value.

**2. Use continuous measures, not just categories.** Plot churn against implementation duration or percentage of claim volume in the system. If churn rises steadily as implementations lengthen, that pattern is more convincing than a single split and less sensitive to where you draw the line.

**3. Add related outcomes to enlarge the sample.** Churn is only the most extreme outcome. Also count:
- customers who downgraded or dropped modules
- renewals that were saved only with heavy discounts or escalation
- current customers who have issued RFPs, taken competitor meetings, or are flagged at risk

This can double or triple your usable cases. Keep these results separate from the churn results, then check whether they tell the same story.

**4. Weight by revenue.** Twenty-two logos may represent very different ARR. Report both logo counts and dollars, since the dollars drive the business decision.

**5. Check new business too.** Win/loss data on recent deals tests the product-gap hypothesis independently. If you're losing competitive deals on analytics and AI, that's evidence regardless of what churn shows.

## Watch for confounders

With small samples, one hidden variable can create a false pattern. The most likely one here is carrier size. Small carriers may have thinner IT teams, which slows implementation. They're also more likely to be acquired or to cut costs. Churn could then track implementation difficulty without implementation being the cause. Remove acquisitions and other involuntary churn first. Then check whether the pattern holds within rough size bands and signing-year cohorts. If it does, you can be much more confident it's real.

## The right standard of evidence

You're not publishing a paper. You're choosing where to put the next few quarters of investment, under uncertainty, with the option to adjust. Ask whether the evidence is strong enough to justify shifting resources, and whether you'll learn quickly if you're wrong.

Given that, the most useful thing to do is agree with both VPs, before looking, what results would move the decision. For example: "If churn among Never/Partial customers is at least three times the Full rate, and most case timelines show stalled implementation before competitor contact, we prioritize time-to-value." Small numbers become a problem mainly when nobody has agreed what counts as convincing, so every ambiguous result becomes a new argument.

Then start the leading-indicator tracking from the last answer. Your churn history is small and fixed, but milestone data on current customers builds every quarter, and within a year you'll have a much larger, cleaner dataset to confirm or revise whatever you decide now.

## Turn 4

**User:** How do I get both VPs to actually agree on those decision thresholds up front when each of them is already convinced they're right?

**Assistant:**

# Getting Two Confident VPs to Agree on Decision Rules

You don't need them to agree on who's right. You need them to agree on **how the question will be decided**. Their confidence makes that easier: someone sure they're right should welcome a fair test, because they expect to win it. Your job is to make the test feel fair to both and to make losing it survivable.

## 1. Secure a sponsor first

You run customer success, so you're probably their peer, not their boss. Before approaching either VP, get the CEO, COO, or whoever owns resource allocation to endorse the approach: "Before we reallocate, we'll run a six-week diagnostic, and the three of you will agree up front how results translate into decisions." That turns your request from a favor into an expectation and gives you somewhere to escalate if someone stalls.

## 2. Meet each VP separately before bringing them together

In a joint meeting, each will argue their position. One-on-one, you can ask questions that are hard to answer defensively:

- **"What result would change your mind?"** If they can name one, write it down; that's the seed of a threshold. If they can't, point out gently that a belief no evidence could change isn't a strategy, and ask again.
- **"What do you expect the data to show?"** Ask for specifics: roughly what churn rate among customers who never reached full value versus those who did, and what share of churned accounts they expect to show stalled implementations. Confident people usually give confident predictions, and written predictions are hard to disown later.
- **"What would convince the other VP?"** This makes them think about what fairness looks like to the other side.

You'll often find their predictions are closer than the debate suggests. The Services VP may concede that some fully implemented customers left for better analytics. The Product VP may concede that customers who never went live weren't leaving over missing AI.

## 3. Make the outcomes positive-sum

People resist decision rules when the stakes are all-or-nothing. Before anyone sees data, map every plausible result to a proportionate response, including the likely middle outcomes:

| If the diagnostic shows... | Then we... |
|---|---|
| Churn heavily concentrated in Never/Partial customers, with timelines showing stalled implementation first | Prioritize time-to-value; Product contributes implementability work (configuration, integration, migration tooling) |
| Elevated churn among fully implemented customers, with churners moving to AI/analytics competitors | Accelerate the analytics roadmap, targeted at the specific gaps churners cited |
| Both patterns are material | Split investment roughly in proportion to churned ARR attributable to each |
| Results are inconclusive | Keep current allocation, fund no-regrets moves, rerun with leading-indicator data in two quarters |

This does several things:

- **Nobody loses everything.** Even in the Services-favored outcome, Product owns meaningful work, and vice versa.
- **A "both" outcome becomes a legitimate result**, not a messy compromise.
- **The inconclusive row removes the incentive to argue ambiguous data into a win.** Everyone knows in advance what happens.

Keep the thresholds simple: one primary comparison, one ratio, one case-review criterion, as in the earlier example.

## 4. Have both VPs shape the analysis

People attack evidence they didn't help design. So before any data is pulled, ask each VP to review the value milestones, the data sources, and how churn causes will be coded, and to raise every objection then. Tell them explicitly: "If you have concerns about the data or the method, now is the time. After we look, we're not relitigating the method."

Then have a neutral party run the analysis, such as a finance or business-operations analyst, or an outside firm. Neither VP's team should do the classification, and neither should you, if you're seen as aligned with Services.

## 5. Put it in writing

Summarize the agreement on one page:

- the primary comparison
- the thresholds
- the outcome-to-action table
- the method for coding churned accounts
- each VP's written prediction

Have both VPs and the sponsor sign off by email. It sounds bureaucratic, but people tend to move the goalposts when results arrive, often without realizing it, and a written record prevents that.

## 6. Handling resistance

- **"The data's too patchy to mean anything."** Agree that it's imperfect, point to the confidence ratings and the inconclusive row, and ask what additional evidence would satisfy them. Then add it, within reason.
- **"This is obviously a product problem, we don't need a study."** Frame the diagnostic as cheap insurance: "If you're right, six weeks of analysis will prove it and give you a stronger case for more roadmap investment. If we're wrong, we'll have spent a year building the wrong thing."
- **Refusing to commit to any threshold.** That's the point to use your sponsor. Someone unwilling to state what would change their mind is asking for a decision based on advocacy rather than evidence, and the executive team should know that.

## 7. Manage your own position

Customer success sits close to implementation and support, so the Product VP may assume you already favor Services. Counter that openly. State your own prediction, acknowledge where the product-gap view is likely right, and make sure the analysis setup is visibly neutral. Your credibility as an honest broker is what makes the whole approach work.

Present the effort as a way to reduce customer churn, not as a contest between the two VPs. When the results come in, describe them in terms of what customers experienced and what to do next, not in terms of which VP was right.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do: A 90-Day Plan

Don't pick a side yet, and don't wait passively for data either. Protect revenue now, settle the diagnosis in six weeks with agreed rules, then commit resources decisively. If I had to bet, you'll find mostly an implementation and time-to-value problem, with a real but smaller product gap on top. Plan for that, but let the evidence decide.

## This week

1. **Get your sponsor.** Take a one-page proposal to your CEO or COO: a six-week diagnostic, pre-agreed decision rules, a neutral analyst, and no major reallocation until it's done. Ask them to announce it so it isn't seen as your personal initiative.
2. **Meet each VP one-on-one.** Get their written predictions and their answer to "what result would change your mind?"
3. **Clean the churn number.** Separate logo from ARR churn, remove acquisitions and other involuntary losses, and check for renewal-cohort effects. You may find the problem is smaller, or differently shaped, than "churn doubled" suggests.

## Weeks 1–2: Agree on the rules and start the no-regrets moves

**Finalize the decision agreement:**
- the value milestones (live, volume, breadth, integrated)
- one primary comparison and threshold
- the outcome-to-action table
- how churned accounts will be coded

Both VPs review the method and raise every objection now, then sign off in writing.

**Start protecting revenue in parallel.** These pay off whichever hypothesis wins:
- Build a simple health score and list every account renewing in the next three quarters. Assign an executive sponsor to each at-risk account.
- Stand up a small senior team to unblock currently stalled implementations. Today's stuck customers are your churn in 18 months.
- Hold the roadmap steady. Don't freeze it, and don't re-plan it.

## Weeks 2–6: Run the diagnostic

A neutral analyst leads, supported by a CSM lead and someone who can query production data.

- **Classify all customers by value attained**, measured 12–18 months after signing, with a confidence rating on each classification.
- **Build a full timeline for each churned account.** With 20–25 accounts, you can review every one.
- **Add related outcomes:** downgrades, heavily discounted saves, and current at-risk accounts.
- **Check win/loss data** on recent competitive deals for evidence of a product gap.
- **Test whether the pattern holds** within carrier-size bands and signing-year cohorts.

## Week 6–7: Decide

Present the results against the pre-agreed table, in terms of what customers experienced, not which VP was right. Then commit.

**If it's mostly implementation and time-to-value, which I expect:**
- Set a time-to-value target, such as live on core modules within a fixed number of months, and make it an executive metric.
- Aim Product investment at implementability: configuration tooling, integration templates, and migration utilities. This is probably the highest-ROI product work available to you.
- Fix the handoff from sales to implementation. Long implementations often start with overselling or underscoped statements of work.

**If there's a material product gap:**
- Fund the specific analytics and AI capabilities that churners and lost deals actually cited, not a broad effort to match competitors.
- Prioritize features that help customers who are already live get more value, since they're the ones who can adopt them.

**If it's both:** split investment roughly by the churned ARR attributable to each.

**If it's inconclusive:** keep the no-regrets moves running and decide in two quarters using the leading-indicator data you're now collecting.

## Ongoing: Make this permanent

- Track value milestones for every implementation and review them quarterly.
- Report time-to-value, milestone attainment, and account health alongside churn. They'll show problems roughly a year before churn does.
- Revisit the allocation in two quarters with better data.

## Why this is the right approach

It stops the damage immediately, costs only six weeks before a decision, avoids a year of building the wrong thing, and replaces an unresolvable argument between two senior leaders with a process both have agreed to. It also leaves your company able to catch the next churn problem early, which matters more than winning this particular debate.

## Outcome summary (sent to Jev)

Neither VP's belief should be adopted yet, and the either/or framing is likely wrong. The company should protect revenue immediately, settle the diagnosis with its own data in about six weeks using pre-agreed decision rules, and then commit resources decisively. The expected finding is mostly an implementation and time-to-value problem with a real but smaller product gap, but the evidence should decide.

The two hypotheses make different, testable predictions. Stated churn reasons are biased toward "missing features." Carriers rarely rip out a claims system over one feature because switching costs are huge. Long implementations may themselves be a product problem.

This week, the CS leader should secure a CEO or COO sponsor and meet each VP separately to collect written predictions and what would change their minds. The churn number needs cleaning: separate logo from ARR churn, strip out acquisitions and other involuntary losses, and check renewal-cohort effects.

Next, both VPs should agree in writing on:
- value milestones (live, volume, breadth, integrated)
- one primary comparison and threshold
- an outcome-to-action table that includes "both" and "inconclusive" rows

In parallel, the company should take no-regrets actions:
- build a health score
- assign executive sponsors to at-risk renewals
- put senior staff on stalled implementations
- hold the roadmap steady

A neutral analyst should then classify customers by value attained 12–18 months after signing, with confidence ratings. The diagnostic should also build timelines for every churned account, add downgrades and discounted saves, check win/loss data, and control for carrier size and signing cohort.

If implementation dominates, the company should set time-to-value targets, aim product work at implementability, and fix the sales-to-implementation handoff. If there is a product gap, it should build only the capabilities churners actually cited. If both, it should split investment by attributable churned ARR. If inconclusive, it should revisit in two quarters.

The caveats are that 20–25 churners detect only large effects, and a null result proves nothing. Milestone tracking should become permanent.
