# social/churn-cause/testB

Model: claude-opus-5-5 · 2026-09-24T14:58:06.612939+00:00

## Turn 1

**User:** You are a world-class expert: a sociologist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Neither Belief Is Right Yet, and the Framing Is Part of the Problem

**Short answer:** You don't yet know which belief is right, and neither do they. Each VP is offering a plausible hypothesis that happens to locate the cause in someone else's function and the solution in more investment in their own. That isn't cynicism on their part. It's how organizations make sense of bad news: people explain outcomes using the causes they can see and act on. Your job is to replace a debate between two plausible stories with evidence, and to do it fast.

## Why this isn't an either/or

In claims software for regional carriers, the two explanations are usually entangled, and the causal arrow often runs from services to "product gaps."

- **Failed implementations produce perceived product gaps.** A carrier whose implementation dragged on 14 months, went live with half the modules, and never configured the reporting layer will honestly tell you "your analytics are weak." They never experienced your analytics. The complaint is about the product; the cause is adoption.
- **Exit reasons are socially constructed.** When a carrier leaves, the stated reason has to be defensible to their board and CFO. "The competitor has better AI" is a respectable, forward-looking justification. "We lost confidence in the vendor relationship" is harder to put in a memo. So exit surveys systematically over-report feature reasons.
- **The reverse also happens.** A well-implemented customer can still leave if a competitor like Guidewire, Duck Creek, or a newer AI-native entrant shows them fraud detection or triage automation that moves their loss ratio. Good service doesn't save you from a real capability gap forever.

So the useful question isn't "product or services?" It is **"which customers are leaving, at what point in their lifecycle, and what was true about them before they decided to leave?"**

## First question: what changed 18 months ago?

A *doubling* of churn implies something shifted, not a slow drift. Before arguing about the roadmap, list every change in the relevant window:

- A new competitor or a competitor's AI launch in your segment
- Pricing or packaging changes, especially at renewal
- A surge in new-logo sales that overloaded your implementation team
- Loss of key implementation or support staff
- A major version upgrade or platform migration you forced on customers
- M&A among your customers (regional carrier consolidation is real, and an acquired carrier often moves to the acquirer's system regardless of your quality)
- Sales moving into a segment you don't serve well, such as larger carriers or new lines of business

Some churn may be neither product nor services. Separate out consolidation-driven and bankruptcy-driven losses so they don't pollute the analysis.

## A four-to-six-week diagnostic

**1. Build a churn dataset.** For every churned account over the last 24 months, and a comparable set of retained ones, pull:

- Signing cohort and tenure at churn
- Implementation duration: planned vs. actual time to go-live
- Modules purchased vs. modules actually live
- Usage depth (claims processed in-system, reporting and analytics usage, active users vs. licensed)
- Support ticket volume, severity, and time to resolution
- Executive sponsor changes
- Where they went (competitor, in-house, acquirer's system)
- Stated churn reason

**2. Read the patterns.**

| If you see... | It points toward... |
|---|---|
| Churners concentrated in recent cohorts, with long or troubled implementations and low module adoption | Services / time-to-value |
| Churners who were fully live and well adopted, leaving for specific competitors with specific capabilities | Product gaps |
| Churn clustered around a forced upgrade or pricing change | A specific event, not either VP's thesis |
| Churn following sponsor turnover, with no clear operational cause | Relationship and executive coverage |
| Churners citing features you already have | Adoption and enablement (services, disguised as product) |

That last row is often the most revealing. Check every "missing feature" cited in exit reasons against what the customer actually had licensed and deployed.

**3. Interview churned customers properly.** Use a neutral third party, not their account team. Talk to the economic buyer and the claims operations leader, not just the admin. Ask about the decision *process*: when they first started looking, what triggered it, who pushed for it. The trigger is usually a year or more before the stated reason. For a core claims system, nobody switches on impulse. They decide in their head long before they decide on paper.

**4. Look at new-business win/loss.** If you're also losing competitive deals on analytics and AI, where no implementation experience exists, that is strong evidence for the product thesis. If win rates are stable but retention is collapsing, the problem is post-sale.

## Handling the two VPs

Before the data comes back, get both VPs to write down **what evidence would change their mind**. This converts a turf dispute into a shared test and makes it much harder for either to reinterpret results afterward.

You're well placed to run this. You sit between the two functions and see the customer whole. Frame it as a joint diagnosis, not an adjudication.

## What to do while you wait

Don't freeze.

- **Stabilize at-risk accounts now.** Score current customers on the early signals: stalled implementations, low module adoption, sponsor changes, and renewals within 12 months. Put executive attention on the top tier immediately. Saving three accounts this quarter matters more than winning the argument.
- **Make no-regret moves.** Compressing time-to-value for new implementations is almost never wrong in enterprise software; stalled implementations poison renewals and references. On the product side, a targeted response to the analytics gap, such as better out-of-the-box claims dashboards or partnering with an established analytics or fraud vendor, may close most of the perceived gap far faster than a major roadmap acceleration.
- **Avoid the big irreversible bet** of reorganizing the roadmap or the services org until the diagnostic is done.

## My prior

If you forced me to bet on the two most common patterns I've seen in vertical enterprise software, I'd bet that the bulk of the increase traces to **post-sale failure: long implementations, partial adoption, and eroded executive relationships.** That churn then gets narrated as "product gaps" because that's the story customers can tell. On top of it sits a smaller but real and growing competitive AI gap that will matter more over the next two to three years.

That would mean fixing implementation and adoption first, while making a focused, credible move on analytics and AI so you aren't defenseless at renewal. But treat that as a hypothesis to test, not a conclusion. The whole point is to stop deciding this on priors, including mine.

## Turn 2

**User:** We've only lost maybe 15 or so customers in that period. Is that enough data to actually see these patterns, or will it just be noise?

**Assistant:**

# Fifteen Is Enough, If You Change the Method

Fifteen is too few for statistical modeling, but plenty for serious diagnosis. You just have to change how you analyze it. With 15 cases you're doing detective work, not statistics, and that's a well-established approach in its own right.

## First, check whether the doubling itself is real

Before explaining the increase, confirm it isn't noise. If you went from roughly 7 losses in the prior 18 months to 15, that jump is unlikely to be pure chance, but it's fragile:

- **Remove the non-diagnostic losses.** Take out churn driven by acquisitions, carrier insolvencies, or exits from a line of business. If three or four of the 15 were acquired carriers moving to the parent's system, your "doubling" may shrink to a modest increase.
- **Look at revenue as well as logos.** Did churn double by count, by ARR, or both? One or two large losses can make the trend look dramatic while telling you little about the broader pattern. Conversely, several small logos might hide a stable revenue base.

If the increase survives both checks, it's real enough to act on.

## What 15 cases can and can't tell you

**What they can't do:** support fine-grained percentages, multi-variable models, or subtle effects. Don't report that "33.3% of churn is product-related." With 15 cases, one account moving categories swings that by 7 points.

**What they can do:** reveal strong patterns, especially when you compare them against retained customers. The comparison group is essential. Without it, "10 of 15 churners had delayed implementations" means nothing, because maybe 10 of 15 retained customers did too.

To make this concrete, take 15 churned and 15 retained accounts:

- If 10 of 15 churners had implementation overruns versus 3 of 15 retained, that difference is unlikely to be chance (Fisher's exact test gives p ≈ 0.03). You can act on it.
- If it's 8 versus 5, you can't distinguish that from noise, and you should say so.

**The rule of thumb:** with small numbers, only large differences count, and that's fine. The factors that doubled your churn should be large. If they're subtle, they probably aren't what doubled it.

## Treat each loss as a case

Your real advantage is that every one of these 15 is a big, well-documented decision. A carrier replacing its claims system involves a buying committee, an RFP, a board-level justification, and months of deliberation. That makes each case rich enough to reconstruct in detail. For each account:

- **Build a timeline** from contract signing to non-renewal: implementation milestones, go-live, sponsor changes, escalations, and when the customer first started looking at alternatives.
- **Find the trigger**, not just the stated reason. What happened in the 6 to 18 months before they began evaluating competitors?
- **Place it against the other explanation.** For each case, ask what you would expect to see if the Product thesis were true, and what you'd expect if the Services thesis were true. Then check which expectations the evidence matches.

Done this way, 15 cases can be more convincing than 500 survey responses, because you understand the mechanism rather than just the correlation.

## Expand the evidence beyond the 15

You can also enlarge the dataset by looking at customers who haven't left yet but show the same early signals:

- **At-risk current accounts:** contraction, stalled implementations, falling usage, sponsor turnover, or known RFP activity
- **Competitive win/loss on new deals:** this tests the product thesis independently of your post-sale experience
- **Partial churn:** modules dropped or seats reduced
- **Close calls:** customers who nearly left but renewed, and what saved them

This gives you perhaps 40 to 60 relevant data points instead of 15. It also shifts your work from explaining the past to predicting the next round of losses, which is where you can actually change outcomes.

## One caution

Small samples invite compelling stories. One vivid exit interview ("your AI was years behind") can dominate everyone's thinking. Guard against this by having someone code each case against the criteria before the two VPs see the results, and by showing the full case-by-case table rather than a summary. Fifteen rows fit on one page, so let everyone see all of them.

## Turn 3

**User:** How should I pick the 15 retained customers to compare against, so the comparison is fair?

**Assistant:**

# Choosing a Fair Comparison Group

**The core principle:** the retained group should consist of customers who **faced the same decision under similar conditions and chose to stay.** You want the two groups to differ in outcome, not in circumstances you already know about. Then any remaining differences, like implementation experience or product usage, become candidate explanations.

## Match on renewal timing first

The most important matching variable is easy to overlook. Each churned customer left at a specific decision point, usually a renewal. For each one, draw your comparison from customers **whose renewal came up in roughly the same window and who renewed.**

This handles several problems at once:

- **Fair exposure.** A customer who signed six months ago hasn't had a chance to churn yet. Including them makes retained customers look artificially "fresh."
- **Same market conditions.** Both groups faced the same competitive landscape, pricing, and AI hype at the moment of decision.
- **Same company conditions.** Both experienced your organization at the same point, with the same support staffing and product version.

If contract terms vary, match on "reached a renewal or termination option in the same quarter or half-year."

## Then match on a few structural traits

Choose two or three characteristics that shape churn risk but that neither VP's hypothesis is about:

- **Size:** premium volume, claims volume, or contract value. Larger carriers have different buying committees, IT resources, and competitive options.
- **Tenure or signing cohort:** customers implemented in the same era got the same implementation methodology and product version.
- **Lines of business or product footprint:** a personal-auto carrier and a commercial or workers' comp carrier use claims software very differently.

Don't try to match on everything. With a small pool you'll run out of candidates. Pick the two or three factors most likely to confound the comparison, and use broad bands ("small / mid / large") rather than exact matches.

## Don't match on what you're testing

**Never match on the variables you're trying to evaluate:** implementation duration, modules adopted, usage depth, support ticket volume, sponsor changes, analytics usage. If you match on implementation length, you've guaranteed both groups look identical on it and erased the evidence for the Services thesis. The same applies to analytics usage and the Product thesis.

A useful test is to ask of any candidate matching variable, "Is this something one of the VPs thinks causes churn?" If yes, leave it unmatched and measure it instead.

## Selection procedure

The biggest risk to fairness is choosing retained customers you know. Account teams will naturally reach for their happiest, best-referenced accounts, and that makes almost any difference look dramatic.

1. **Write the matching rules down first**, and get both VPs to agree to them before anyone looks at the list. This prevents disputes later about a stacked comparison.
2. **Build the eligible pool mechanically.** For each churned account, filter your customer list to renewals in the same window, the same size band, and a similar product footprint.
3. **Pick randomly from within that pool.** If five retained customers match a given churned account, draw one at random rather than choosing.
4. **Keep the ones that look shaky.** Some retained customers will be unhappy or at risk. That's reality, not contamination. Removing them would make "retained" mean "healthy," and the comparison would overstate every difference.
5. **Apply the same exclusions to both groups.** If you removed acquired carriers from the churn list, remove customers currently being acquired from the retained pool too.

If a churned account has no good match (say, your only large workers' comp carrier), note that and either relax one criterion or leave it unmatched. Don't force a bad match.

## Two practical refinements

**Consider matching two to one.** If you have enough renewing customers, pick two retained accounts per churned account, about 30 total. Your conclusions become noticeably more stable, and you'll still be able to profile every account. Going beyond two to one adds little.

**Use your full customer base for simple metrics.** For measures that are easy to pull from systems, such as implementation duration or modules live, you don't need to sample at all. Compare the 15 churners against *all* retained customers who reached a renewal in the same period. Reserve the matched sample for the labor-intensive work: timelines, interviews, and reconstructing decisions.

## Blind the coding where you can

Have whoever gathers and codes the data (implementation overrun: yes/no, sponsor change: yes/no, and so on) work from account records with the outcome hidden where practical. Then reveal which accounts churned. It's surprisingly easy to read a support history as "clearly troubled" once you know the customer left.

Do these things and neither VP will be able to dismiss the results as a rigged comparison, which matters as much as the analysis itself.

## Turn 4

**User:** How do I get churned customers to actually agree to an interview, and who should I try to talk to there?

**Assistant:**

# Getting Churned Customers to Talk, and Choosing Whom to Ask

Most churned enterprise customers will talk to you if you ask the right way. The insurance world is small and relationship-driven, and people generally respect a vendor that wants to understand its failures. What kills participation is any hint that the conversation is a win-back attempt or a chance to argue with their decision.

## How to get a yes

**Make the ask come from someone senior, and make it personal.** A note from you, or better, from your CEO, lands very differently from a survey link. Keep it short and honest:

> "You made a considered decision to move on, and we respect it. We're trying to understand where we fell short so we can do better for other carriers. Would you give us 30 minutes? This is not a sales conversation, and nothing you say will be attributed to you or your company."

**Say explicitly that it is not a win-back.** Then honor it. No pitch, no "have you heard about our new release," and no account executive on the call. If they sense a sales agenda, you'll get polite, useless answers, and the story will spread among their peers.

**Use a neutral interviewer.** A third-party researcher, or someone internal who never touched the account, gets far more candor. Customers soften criticism when talking to people they worked with. You can still make the introduction yourself, then hand off.

**Guarantee confidentiality in writing.** Findings reported only in aggregate, quotes anonymized, nothing shared with the account team in identifiable form. People are more candid when they know criticism of your staff won't come back to individuals.

**Keep it short and easy.** Thirty to forty-five minutes, video or phone, scheduled around them. Offer to send the questions in advance.

**Offer something back, carefully.** Many carriers have gift and vendor-interaction policies, so cash honoraria can be awkward. Better options:
- A donation to a charity of their choice
- A summary of the aggregate findings, which interests peers across regional carriers
- Simple professional courtesy: "Your perspective will genuinely change how we serve carriers like you"

**Time it well.** The best window is usually a few weeks to a few months after the decision is final. Memories are fresh and emotions have cooled. Avoid the peak of their migration crunch. For customers who left a year or more ago, still ask. Recall is weaker, but the decision story is usually well rehearsed.

**Route through whoever has the best relationship.** Sometimes that's an implementation lead, a support engineer, or an executive who built rapport, not the account manager. Let that person make the introduction.

**Don't use leverage.** If they're still in a transition-assistance period, don't tie the interview to anything contractual. It will poison the conversation and your reputation.

## Whom to talk to

A claims system replacement is a committee decision, and different roles experienced different parts of the failure. Aim for **two or three people per account**, in roughly this priority order.

1. **The economic decision-maker.** Usually the COO, the VP or head of claims, or sometimes the CFO or CEO at smaller carriers. This person knows the real reason in the form that justified the spend to the board. They're the hardest to get and the most important.

2. **The operational claims leader.** The claims director or manager who lived with the system daily. This person knows whether the product failed, the implementation failed, or adoption never happened. They're often the most concrete and candid.

3. **The IT or implementation lead.** They know what the implementation was really like: delays, integration pain, data migration problems, support responsiveness. This is essential for testing the Services thesis.

4. **The original champion or sponsor, even if they've left.** This source is often overlooked and extremely valuable. If the person who bought your system has moved on, find them on LinkedIn. Former employees are frequently the most candid, since they have no stake in defending the decision, and a sponsor's departure may itself be part of the causal story.

5. **Whoever led the replacement evaluation**, if it differs from the above. They can tell you when the search began, what triggered it, which alternatives were considered, and what tipped the decision.

Procurement contacts are usually less useful. They know the process but rarely the underlying reasons.

## What to ask about

Focus on **reconstructing the decision**, not collecting opinions:

- "Walk me through the history, from when you selected us to when you decided to move."
- "When did you first start thinking about alternatives? What was happening then?"
- "Who pushed for the change, and who was hesitant?"
- "What did the new vendor show you that mattered most? Now that you're using them, is it delivering?"
- "Was there a point where we could have kept you? What would it have taken?"

Listen for the gap between the **trigger** ("our implementation was nine months late and we lost faith") and the **justification** ("they have better AI"). Both are true in a sense. The trigger is usually the more useful one.

Don't defend, correct, or explain, even when they get facts wrong. Note the misunderstanding; it's data too. If a customer believes you lack a feature you actually have, that tells you something important about adoption and enablement.

## Plan for gaps

Expect to reach perhaps half to two-thirds of the 15 accounts with real effort. Keep track of **who declined and why**, since non-response isn't random. The angriest customers and the most indifferent ones are the likeliest to decline. Fill gaps with internal sources such as support records, implementation notes, and interviews with your own staff who worked the account, and label those cases as lower confidence.

Finally, **run the same interview with your matched retained customers.** Otherwise you'll hear about implementation pain from churners and conclude it caused churn, without knowing whether retained customers suffered the same pain and stayed anyway. The comparison is what turns complaints into evidence.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do: A 90-Day Plan

You don't yet have the evidence to pick a side, so don't. What you should do is **stabilize the accounts at risk now, run a fast and fair diagnosis, make a few moves that pay off whichever VP is right, and decide on the big investments in about ten weeks** using rules everyone agreed to in advance.

## Weeks 0–2: Align and stabilize

**Get the two VPs to agree on the test before anyone sees data.** Meet with both and agree on:
- The churn list, with acquisition-driven and insolvency-driven losses removed
- The matching rules for the retained comparison group
- Most important, **what evidence would change each person's mind**, written down

That last step turns a turf fight into a shared experiment. Frame it as joint ownership of a retention problem, not you refereeing between them.

**Protect the customers you still have.** Score every current account on the early warning signs: renewal within 12 months, stalled or incomplete implementation, low module adoption, executive sponsor turnover, escalating support issues, and known RFP activity. For the top tier, assign an executive sponsor and hold a candid account review within 30 days. A few saved renewals this quarter are worth more than any analysis.

## Weeks 2–8: Run the diagnosis

- **Pull system data** on implementation duration, modules live, usage, and support history for all 15 churners and all retained customers who reached a renewal in the same period.
- **Build the matched comparison sample** of about 15 to 30 retained accounts using the pre-agreed rules and random selection.
- **Reconstruct each churn case** as a timeline, identifying the trigger rather than just the stated reason.
- **Interview churned and retained customers** with a neutral interviewer, targeting the economic buyer, the claims operations leader, and the IT lead.
- **Pull new-business win/loss data.** If you're losing competitive deals on analytics and AI before customers ever experience your implementation, that is independent evidence for the product thesis.
- **Code cases blind where possible**, and produce a single page showing all cases side by side.

## Moves to make now, regardless of the outcome

These pay off whichever VP turns out to be right, so start them without waiting.

1. **Put implementation stalls in front of executives.** Any implementation that slips a milestone by more than an agreed threshold goes to a monthly executive review. Stalled implementations lead to failed renewals in almost every enterprise software business.
2. **Close the "feature exists but isn't used" gap.** Audit current customers for purchased-but-unused modules, especially reporting and analytics. Run targeted enablement. Some of your "product gap" may simply be undeployed product.
3. **Scope a fast, limited analytics and AI response.** Don't overhaul the roadmap yet. Identify what could credibly ship in two quarters: better out-of-the-box claims dashboards, or a partnership with an established analytics or fraud vendor. That gives account teams something concrete at renewal and keeps the option open for bigger bets.
4. **Assign an executive sponsor to every strategic account**, and flag sponsor changes on the customer side as a risk event.

## Weeks 8–10: Decide, using pre-agreed rules

Present the case table to both VPs and your executive team, then apply the rules you agreed to up front.

| What the evidence shows | What to do |
|---|---|
| Churners had much worse implementations and adoption than retained customers, and new-business win rates are stable | **Services first.** Invest in implementation capacity, methodology, and time-to-value. Hold the roadmap roughly steady, plus the limited analytics response. |
| Churners were well implemented, left for specific competitor capabilities, and win/loss shows the same gap | **Product first.** Accelerate the analytics and AI roadmap, and use partnerships to close the gap faster than building alone. |
| Both patterns appear in different segments | **Split the response by segment.** Often newer, smaller carriers are hurt by implementation while larger, long-tenured ones are drawn away by competitor capability. |
| Churn clusters around a single event, such as a forced upgrade, a pricing change, or staff turnover | **Fix that specific cause.** Neither VP's broader thesis is the main issue. |
| No clear difference between the groups | Look harder at relationship and executive coverage, and at who you're selling to. You may be closing deals with carriers you can't serve well. |

My prior, from earlier, remains that **post-sale failure is likely the larger driver, with a real but smaller competitive AI gap growing behind it.** The data should settle that, not my prior.

## Make the fix permanent

Whatever the diagnosis shows, the underlying problem is that churn doubled over 18 months and your organization is only now debating why. Fix that:

- **Create a shared retention metric** owned jointly by Product and Services, so neither can win by blaming the other.
- **Run a quarterly churn and near-miss review**, reconstructing every loss and every close call. Fifteen cases a year is manageable to study in depth.
- **Track leading indicators, not just outcomes:** time-to-value, adoption depth, sponsor stability, and competitive mentions in account conversations.

## What not to do

- Don't reorganize the roadmap or the services team before the diagnosis is done.
- Don't let exit-survey language ("better AI") stand in for the real decision story.
- Don't let this become a verdict on either VP. If one is proven "wrong" in public, the next diagnosis will get less honest cooperation.

## Your role

You're the one person who sees the whole customer lifecycle, which makes you the natural owner of this diagnosis and the retention system that follows. Take that role explicitly. Bring the two VPs a shared problem and a fair test, not a ruling, and in ten weeks you'll have both an answer and a retention process that catches the next problem before it doubles.

## Outcome summary (sent to Jev)

The recommendation is not to side with either VP yet, because neither belief is established. Instead, stabilize at-risk accounts, run a fast, fair diagnosis over about ten weeks, start moves that pay off either way, and then decide on major investments using rules agreed in advance.

The two explanations are likely entangled. Failed or partial implementations often produce perceived "product gaps," and exit reasons like "better AI" are over-reported because they are easier to justify to a board. Real capability gaps can still drive well-served customers away.

First, identify what changed 18 months ago, and remove acquisition- and insolvency-driven losses. Fifteen churned accounts is too few for statistics but enough for case-based detective work, provided they are compared against retained customers. Those retained customers should be matched on renewal timing, size, and footprint, never on the variables being tested, and chosen randomly, keeping shaky accounts in the pool. Other steps:
- Pull system data on implementation, adoption, usage, and support.
- Reconstruct each churn timeline to find the trigger.
- Have a neutral interviewer speak with economic buyers, claims leaders, IT leads, and former sponsors, at both churned and retained customers.
- Check new-business win/loss.
- Code cases blind and show all cases on one page.

Both VPs should agree beforehand on what evidence would change their minds.

Several moves should start immediately:
- Score and protect at-risk accounts.
- Escalate stalled implementations to executives.
- Close gaps where customers have purchased features but don't use them.
- Scope a limited analytics and AI response, such as dashboards or partnerships.
- Assign executive sponsors to strategic accounts.

Afterward, create a shared retention metric, run quarterly churn reviews, and track leading indicators.

The assistant's prior is that post-sale failure drives most of the churn, with a smaller but growing AI gap. It stresses that this is a hypothesis for the data to settle. It also cautions against making irreversible reorganizations first and against letting the result become a public verdict on either VP.
