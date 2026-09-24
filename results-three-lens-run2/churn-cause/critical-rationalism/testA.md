# churn-cause/critical-rationalism/testA

Model: claude-opus-5-5 · 2026-09-24T15:28:45.177397+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

Neither belief is proven yet, and you shouldn't pick one based on who argues more persuasively. Both are plausible, they aren't mutually exclusive, and they may be causally linked. For example, customers who never finish implementation never see your analytics, so they conclude the competitor's analytics are better. The good news is that you likely already have the data to settle this in a few weeks.

## Tests that separate the two hypotheses

**1. When in the lifecycle do customers churn?**
Plot churned accounts by time since contract signing and time since go-live.
- Churn clustered at first renewal, often among customers who never fully went live, points to **services**.
- Churn among customers live for 3+ years with healthy adoption, who then leave for a competitor, points to **product**.

**2. Does implementation experience predict churn?**
Compare churned and retained customers on implementation duration, overrun versus plan, time to first value (e.g., first claims processed end-to-end), number of escalations, and support ticket volume and CSAT. If long or troubled implementations churn at 2-3x the rate of smooth ones, that's strong evidence for Services.

**3. Did churned customers use the features you already have?**
This is the most decisive test for the Product argument. If churned customers barely touched your existing analytics or automation, better versions probably wouldn't have saved them. If they were heavy users who hit the ceiling, the product-gap story gains real weight.

**4. Where did they go?**
- A competitor known for AI and analytics supports **product**.
- A competitor known for fast deployment or better service supports **services**.
- A core suite's bundled claims module (e.g., consolidating onto Guidewire or Duck Creek) supports **neither**. That is platform consolidation, which requires a different response, such as integration depth, partnerships, or pricing.
- Acquisition of the carrier is structural churn, largely outside both VPs' control. Regional carrier M&A is active, so separate this out first.

**5. What changed about 18 months ago?**
A doubling suggests something shifted. Look for implementation team turnover or restructuring, a major release or re-platforming, a pricing change, a competitor launch, or a cohort of deals where sales promised roadmap features. The answer often points straight at the cause.

**6. What do new-deal losses say?**
If you're also losing new business on features in win/loss reviews, the product gap is real in the market regardless of churn. If you're winning new deals but losing them at renewal, the problem is post-sale.

## Cautions when interpreting

- **Stated exit reasons are unreliable.** "Missing features" is the diplomatic answer. It's easier to say than "your implementation was a mess." Have someone neutral, not the account's CSM, conduct structured exit interviews, and probe for when the relationship started going wrong.
- **Weight by revenue, not just logos.** The drivers for your largest carriers may differ from those for small ones.
- **Both VPs are seeing their own lever.** This isn't bad faith. Each naturally sees problems they can fix. That's why CS, as a relatively neutral party with access to the customer data, is well placed to own this analysis.

## What to do

**Next 4-6 weeks:** Run the analysis above on the last 18-24 months of churned accounts versus a matched set of retained ones. Present it jointly to both VPs and whoever arbitrates roadmap and headcount. Agree in advance what evidence would favor each side, so the result isn't relitigated.

**In parallel, take steps that are right either way:**
- Build a simple risk flag (stalled implementation, low adoption, rising tickets, executive sponsor change) and run save plays on at-risk accounts now.
- Re-engage recently churned or unhappy customers. Some will tell you candidly what happened.
- Check whether sales is selling roadmap. Over-promising creates both a "product gap" and a "failed implementation" at once.

**Likely outcome:** A mixed picture with one dominant driver. If it's mostly services, fix onboarding first, since new features won't help customers who never reach full value, and keep a targeted product investment for the gaps that genuinely cost you deals. If it's mostly product, accelerate the roadmap but make sure new capabilities are adoptable, or you'll recreate the services problem.

If you can share any of this data, such as churn timing, implementation durations, or where customers went, I can help you interpret it.

## Turn 2

**User:** How do I get both VPs to agree on the criteria upfront when each is already convinced they're right?

**Assistant:**

You don't need them to stop believing they're right. You need them to commit, before seeing the data, to what "right" would look like. People who are confident in their view are often willing to do that, because they expect to win. Use that confidence rather than fighting it.

## 1. Meet with each VP individually first

Don't open with a joint meeting where both defend positions in front of each other. One-on-one, ask each:

- "If you're right, what should we see in the churn data?"
- "What would you expect to see if the *other* explanation were driving it?"
- "What result would make you reconsider?"

Let them generate the predictions themselves. Criteria they wrote are criteria they'll accept later. You'll also learn whether their views are more nuanced than the public positions suggest. Often each privately concedes the other has a point.

## 2. Frame it as a resource decision, not a verdict

Positions harden when the question feels like "whose function is failing." Reframe it as: "We have limited budget and headcount. We need to know where the next dollar reduces churn the most." That makes a mixed result a normal outcome rather than a loss, and it's likely the true answer anyway.

Make it explicit that finding a problem in someone's area isn't an indictment. Implementation pain may stem from product complexity. Product gaps may stem from services never getting customers to adopt what exists. Both VPs have reasons to want the real answer.

## 3. Convert their predictions into a shared scorecard

Bring their inputs into one document before any analysis runs. For example:

| Test | Supports Services if... | Supports Product if... |
|---|---|---|
| Churn timing | Clusters at first renewal, before full go-live | Spread across mature, fully live accounts |
| Implementation vs. churn | Troubled implementations churn at much higher rates | Little difference between smooth and troubled |
| Adoption of existing features | Churned accounts barely used current analytics | Churned accounts were heavy users hitting limits |
| Destination | Competitors known for service or speed | Competitors known for AI or analytics |
| New-deal losses | Winning new deals, losing at renewal | Losing new deals on features too |

Include categories that support neither, such as M&A or suite consolidation, so the data isn't forced into a two-way choice.

Circulate it and ask each VP to sign off in writing: "Is anything missing? Is anything here unfair to your view?" Adjust until both agree. Their edits are a good sign, because they mean ownership.

## 4. Agree on the decision rule, not just the evidence

Criteria alone aren't enough. People can agree on evidence and still fight over what it means. Settle in advance:

- **What counts as meaningful?** For example, "Troubled implementations churn at least 1.5x the rate of smooth ones."
- **What happens with a mixed result?** For example, "Investment splits roughly in proportion to churned revenue attributed to each driver."
- **Who makes the final call** if the evidence is ambiguous?

## 5. Get an executive sponsor to endorse the process

Whoever arbitrates between them, whether the CEO, COO, or CRO, should approve the scorecard and state that decisions will follow it. This matters most as a commitment device. It's much harder to dismiss results you agreed to in front of your boss.

## 6. Make the analysis visibly neutral

- Have someone without a stake run the numbers: you, a revenue operations or data analyst, or finance.
- Share the raw data definitions with both VPs up front, such as how "go-live" and "churn" are defined.
- Let each VP nominate a few accounts they think illustrate their case, and include them. Also analyze the full population so cherry-picking doesn't dominate.
- Don't preview results to one side first.

## Handling resistance

- **If a VP won't name anything that would change their mind,** say so directly but gently: "If no result could change the plan, we don't need the analysis. But then we're deciding on conviction, and leadership should know that's what's happening." Most people back off at that point. If not, escalate to the sponsor.
- **If someone tries to change the criteria after results come in,** point back to the signed-off scorecard. You can allow genuinely new questions for a follow-up, but the original decision rule stands.
- **If the results are embarrassing for one side,** deliver them privately to that VP before the group readout, so they aren't surprised in public and have time to shape their response. This is different from giving a preview of the analysis. They see the finished results, just earlier.

## A possible opening line for the joint meeting

"You've both made strong cases, and I suspect you're both partly right. Rather than debate it, I'd like us to agree today on what the data would show under each explanation, and how we'd split investment depending on what we find. Then we run the numbers and let that decide."

That positions you as the person helping them both get to a defensible answer, which is a much easier role to play than referee.

## Turn 3

**User:** What if the data shows we don't actually track things like go-live dates or feature usage reliably enough to run these tests?

**Assistant:**

This is very common, especially at companies that grew through sales before building customer operations. It doesn't stop the analysis. It changes how you do it. You'll likely end up with evidence that's directionally strong rather than precise, which is usually enough to make a resource decision.

## 1. Check what exists outside your official systems

Data that isn't tracked in the CRM often exists somewhere else. Look for proxies:

**For go-live and implementation quality:**
- Statements of work and project plans with milestone dates
- Professional services billing, since the point when implementation hours taper off roughly marks go-live
- Change orders and scope extensions, which signal troubled implementations
- Support ticket history, since tickets from production users mark when the system went live
- Kickoff and go-live emails or calendar invites
- Implementation leads' own spreadsheets, which often exist even when nothing official does

**For usage and adoption:**
- Application logs, database records, or login data your engineering team may have even if no dashboard shows them
- Claims volume processed through the system, which for claims software is arguably the best adoption measure
- Report or dashboard generation counts for the analytics features
- API call volumes if customers integrate

Ask engineering specifically what's logged. Product teams are often surprised how much usage data exists but has never been queried.

## 2. Hand-code a sample of churned accounts

If systems data is thin, do a structured manual review. Take 20-40 churned accounts, weighted toward the largest by revenue, and a similar number of retained accounts. For each, reconstruct a timeline from documents, tickets, emails, and interviews with the CSM, implementation lead, and account executive.

Use a consistent template for every account:
- Approximate go-live date, and whether they ever fully went live
- Implementation duration versus plan
- Major escalations or scope disputes
- Rough adoption level: minimal, partial, or full
- Features they asked for that you lacked
- Where they went and the stated reason
- The reviewer's judgment of the primary driver, with a confidence rating

Have two people code a subset independently to check that judgments are consistent. This takes effort but is often more revealing than systems data, because it captures context no dashboard shows.

**Include retained accounts.** Without them, you can't tell whether troubled implementations are common among customers who stay too. If everyone had a painful implementation, it doesn't explain who left.

## 3. Watch for bias in missing data

Missing data is rarely random. Records may be worst for exactly the accounts that went badly, such as implementations handed off repeatedly or customers who never engaged. If so, excluding accounts with incomplete data would make implementations look healthier than they were. Note which accounts have gaps, and treat "we can't even reconstruct this account's go-live" as a potential signal in itself.

## 4. Tell the VPs early and adjust the scorecard together

Don't let them discover the data problem from a thin final report. As soon as you know, bring it back to them:

"Some of the tests we agreed on can't be run cleanly because we don't track X. Here's what I propose as substitutes. Do these still reflect a fair test of your view?"

Then update the scorecard jointly, adding a confidence level for each test. Keeping them involved in the substitutions preserves the buy-in you built. If you swap methods on your own, whoever dislikes the result will attack the method.

Also agree on what you'll do if results are inconclusive. That might mean a provisional split of investment while better data accumulates, rather than defaulting to whoever argues hardest.

## 5. Recognize that the gap is itself a finding

If the company can't tell when customers went live or whether they use the product, nobody could see accounts slipping until the renewal conversation. That doesn't prove either VP right, but it explains why churn could double without an early warning, and it's worth stating plainly to leadership.

It also creates a step that's right under either explanation: start tracking now.
- Define go-live precisely and record it for every active account, backfilling where you can
- Instrument usage of key features, especially the analytics the Product VP is concerned about
- Track implementation milestones against plan
- Build a basic health score from these once data accumulates

Both VPs should support this, because it's the only way either of them can prove their case in six months. That shared interest can build goodwill for the harder decision.

## A realistic outcome

You may end up with something like: "Of 30 churned accounts reviewed, roughly 18 show a troubled or incomplete implementation as the primary factor, 7 show a genuine feature gap, and 5 were M&A or consolidation. Confidence is moderate because go-live dates are reconstructed." That isn't statistically rigorous, but it's far better than choosing based on conviction, and it's enough to decide where the next dollar goes while better measurement comes online.

## Turn 4

**User:** Who should I ask to help with the hand-coding, given that the CSMs and implementation leads who know these accounts best might also be the ones who look bad in the results?

**Assistant:**

The key is to separate two roles: **informants**, who supply facts, and **coders**, who make judgments. The people closest to the accounts are your best informants, and you need them. They just shouldn't be the ones deciding what drove each churn.

## Who should do the coding

Pick people with analytical skill and no stake in the outcome:

- **Revenue operations or business operations.** They know the systems, are used to messy data, and don't own the customer relationship.
- **Finance (FP&A).** They're neutral on product versus services and credible with leadership.
- **A data or strategy analyst,** if you have one.
- **An outside contractor or consultant.** This costs more, but it's worth considering if internal neutrality is hard to find or the politics are especially tense. An outsider's findings are also harder for either VP to dismiss.

Avoid coders who report to either VP. Even well-intentioned people from the product or services organizations will read ambiguous accounts through their own lens.

**A note on your own position:** If your CSMs report to you, customer success is also implicated. Poor account management or missed warning signs could turn out to be a driver. That doesn't mean you can't lead the effort, but it's a good reason not to code accounts yourself and to hand the coding to someone outside your organization. Acknowledging this openly to both VPs will strengthen your credibility as a neutral organizer.

## Getting honest input from the people closest to the accounts

**Ask for facts, not verdicts.** "When did they start processing claims in production?" and "What did the customer escalate?" are much easier to answer honestly than "Why did this customer leave?" Let the coders draw conclusions.

**Corroborate against documents.** Check what people say against tickets, emails, statements of work, and billing. Where accounts differ, go with the documents or flag the discrepancy.

**Make it explicitly not a performance review.** Tell participants the goal is to find systemic causes, results will be reported in aggregate, and no individual will be named. Then keep that promise. If anyone is disciplined based on this exercise, you'll never get candid input again.

**Frame systemic problems as systemic.** Most implementation failures reflect staffing, scoping, handoffs, or product complexity, not individual incompetence. Saying this upfront, and meaning it, makes people less defensive.

**Talk to more than one person per account.** Interview the CSM, the implementation lead, and the account executive separately. Each sees different parts of the story and has different blind spots.

## Additional sources worth using

- **Former employees** who worked on these accounts. They have less to protect, although some may have grudges, so weigh their input like anyone else's.
- **The customers themselves.** A neutral party can call former customers for short exit conversations. Customers who left are often surprisingly candid, especially if they aren't talking to their old account team.
- **Sales.** Account executives can speak to what was promised during the sale, which matters if over-promising turns out to be a factor.

## Design safeguards into the coding

- **Remove staff names** from account files where practical, so coders judge the account rather than the person.
- **Double-code a subset.** Have two coders independently review the same 8-10 accounts, compare their judgments, and resolve disagreements before coding the rest.
- **Record confidence and evidence** for every judgment, so anyone can see why an account was coded a certain way.
- **Let both VPs review the method,** including the template and the coder assignments, but not change individual codes. This keeps them bought in without letting them influence specific results.

## A practical team setup

For 40-60 accounts, a workable arrangement is two neutral coders, such as one from revenue operations and one from finance, plus you coordinating logistics and scheduling interviews. The CSMs, implementation leads, and account executives contribute through structured 30-minute interviews per account. That keeps the workload reasonable and the judgments independent, and it gives everyone who knows the accounts a voice without making them grade their own work.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the whole approach as one plan, roughly 8 weeks from start to decision.

## Week 1: Set up

- **Get an executive sponsor** (CEO, COO, or CRO) to endorse the effort and commit to acting on the results.
- **Meet each VP one-on-one.** Ask what they'd expect the data to show if they're right, and what would change their mind.
- **Take immediate action on current risk.** Identify at-risk accounts using whatever signals you have (stalled implementations, low engagement, escalations, upcoming renewals) and start save conversations now. Don't wait for the analysis to protect revenue.

## Week 2: Agree on the rules

- **Hold a joint meeting** to finalize the scorecard: the tests, what result supports each explanation, and categories that support neither, such as M&A or suite consolidation.
- **Set the decision rule** in advance: what counts as meaningful, how investment splits if results are mixed, and who decides if evidence is ambiguous.
- **Get written sign-off** from both VPs and the sponsor.

## Weeks 2-3: Assess the data

- **Inventory what exists,** including proxies: statements of work, services billing, support tickets, application logs, and claims volume processed.
- **Tell the VPs early** if some tests can't be run as planned, and agree on substitutes together.
- **Start tracking go-live dates and feature usage now,** for every active account. This is right regardless of the outcome.

## Weeks 3-6: Run the analysis

- **Assign neutral coders,** such as one from revenue operations and one from finance, not from your organization or either VP's.
- **Review 20-40 churned accounts and a similar number of retained ones,** weighted by revenue, using a consistent template.
- **Interview the people closest to the accounts** for facts, not verdicts, and check what they say against documents.
- **Call former customers** through a neutral party for short exit conversations.
- **Double-code a subset** to check consistency, and record confidence for every judgment.
- **Pull any systems data** you can, such as churn timing, implementation duration, and new-deal win/loss reasons.

## Weeks 7-8: Decide

- **Preview findings privately** with any VP whose area looks bad, so they aren't surprised in the group readout.
- **Present results jointly** against the scorecard both VPs signed.
- **Apply the decision rule** and allocate investment accordingly.

## What the decision will likely look like

- **Mostly services:** Fix onboarding first. That might mean smaller implementation scopes, clearer go-live criteria, better handoffs, or more implementation staff. Fund only the product gaps that are clearly costing deals.
- **Mostly product:** Accelerate the roadmap, but tie new features to adoption support so you don't recreate the implementation problem.
- **Mostly structural,** such as M&A or suite consolidation: Neither VP's plan fully addresses it. Consider integration partnerships, pricing, or targeting carriers less likely to consolidate.
- **Mixed,** the most likely case: Split investment in proportion to churned revenue attributed to each driver, and revisit in two quarters when better tracking data is available.

## Steps worth taking regardless of the result

- Track go-live, adoption, and implementation milestones for every account.
- Build a basic health score so at-risk accounts surface months before renewal.
- Check whether sales is promising roadmap features, since that creates both product and implementation problems.
- Repeat a lighter version of this review every quarter so churn never doubles again without warning.

Your role throughout is organizer and honest broker. You're not trying to prove either VP right. You're making sure the company invests where it will actually reduce churn, and that both VPs trust the answer enough to act on it.

## Outcome summary (sent to Jev)

Neither VP's belief is proven. The two explanations aren't mutually exclusive and may be causally linked, since customers who never finish implementation never see the existing analytics. Rather than picking a side, the company should run a roughly eight-week evidence-based review, with customer success acting as organizer and honest broker, and let the results decide where investment goes.

First, get an executive sponsor to endorse the process. Meet each VP individually to learn what they'd expect the data to show and what would change their mind. Then jointly agree on a signed scorecard and decision rule in advance: what counts as meaningful, how investment splits if results are mixed, and who decides ambiguous cases. The scorecard should include categories that support neither view, such as carrier M&A or suite consolidation.

The core tests are:
- when in the lifecycle customers churn
- whether troubled implementations predict churn
- whether churned customers used existing features
- where they went
- what changed 18 months ago
- whether new deals are also being lost on features

Where tracking is weak, use proxies like statements of work, services billing, tickets, logs and claims volume. Neutral coders from revenue operations and finance should review 20–40 churned and a similar number of retained accounts, weighted by revenue. People close to the accounts are interviewed for facts, not verdicts, and their answers are corroborated against documents.

Stated exit reasons are unreliable, and missing data may hide the worst accounts. Data gaps are themselves a finding.

Regardless of outcome, the company should:
- run save plays on at-risk accounts now
- track go-live and usage
- build a health score
- check whether sales is overpromising roadmap features
- repeat a lighter review quarterly

The most likely result is mixed, with investment split in proportion to churned revenue.
