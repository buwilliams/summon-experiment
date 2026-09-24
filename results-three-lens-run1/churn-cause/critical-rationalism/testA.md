# critical-rationalism/churn-cause/testA

Model: claude-opus-5-5 · 2026-09-24T14:46:51.226582+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

I can't tell you which VP is right from the outside, and neither can they yet. Both explanations are plausible, both VPs are arguing from their own vantage point, and the answer is probably "some of each, in proportions that matter a lot." The good news is that **the two hypotheses make different, testable predictions**, so you can settle this with data in a few weeks rather than by who argues more persuasively.

## First: what changed 18 months ago?

Churn doubling is a change, so look for a cause that also changed. Candidates:

- **A competitor launched** a meaningful analytics/AI capability (supports Product).
- **Implementation or support capacity changed**: team attrition, a shift to a partner, a new methodology, a hiring freeze (supports Services).
- **Sales started selling into a different segment**: larger carriers, different lines of business, customers with messier legacy integrations (supports neither; it's a fit problem).
- **Pricing or packaging changed** at renewal.
- **Market consolidation.** Regional carriers get acquired, and the acquirer often migrates them to its own system. This churn has nothing to do with product or service.

**Contract lag matters here.** If your contracts are multi-year, customers churning now made their decision based on implementations from 2 to 4 years ago. Look at what was happening then, not just recently.

## How to tell the hypotheses apart

| Signal | Points to **product gaps** | Points to **implementation/service** |
|---|---|---|
| Adoption before churn | Churned customers used the product deeply, then left | Churned customers never reached full adoption or full go-live scope |
| Implementation history | Normal duration, on-scope go-live | Long, over-budget, or de-scoped implementations |
| Where they went | Named competitors known for analytics/AI | Any competitor, back to legacy, or in-house |
| Customer profile | Larger, more sophisticated carriers | Clustered by implementation team, partner, or integration complexity |
| Support history | Normal ticket patterns | Escalations, high ticket volume, unresolved issues |
| Healthy customers | Also want AI features and are showing pressure | Stay despite the same feature set |

That last row is especially telling. If your retained customers have the exact same product and are happy, "missing features" is a weaker explanation for why others left.

## Be skeptical of stated exit reasons

"Competitor has better AI" is the easiest, least awkward thing for a departing customer to say. It's impersonal and sounds strategic. "We never got the thing working and your team frustrated us" is harder to say. Also, **a customer who never adopted your core workflow cannot really be leaving over missing advanced analytics.** If churned accounts were using 40% of what they bought, the feature gap was probably the stated reason, not the root cause.

## What I'd do

**1. Run a 4 to 6 week churn diagnostic, jointly owned by both VPs.** Build one dataset of every churned and every retained account from the past 2 to 3 years with:
- implementation duration vs. plan, scope delivered vs. sold
- time to first value / go-live
- adoption depth (modules and features in active use, user counts vs. licensed)
- support tickets and escalations
- segment, size, lines of business, integration complexity
- implementation team or partner
- destination after churn, if known
- whether they were acquired

**2. Do 15 to 20 structured interviews**, split between churned and at-risk/retained customers. Ask about the timeline ("walk me through the first 90 days"), not just "why did you leave." Have someone neutral conduct them, not someone from either VP's team.

**3. Agree on decision criteria before the data comes back.** Get both VPs to commit in writing: "If we see X, I'll accept that the primary driver is Y." This prevents each side from reinterpreting the results to fit its prior.

**4. Start no-regret moves now, without waiting:**
- An at-risk program for every account renewing in the next 12 months, with health scoring and executive outreach.
- A rescue review of in-flight implementations that are behind schedule. These are next year's churn.
- Tracking time-to-value as a company-level metric if you don't already.

**5. Then allocate based on what you find.** Likely outcomes:
- **Mostly service-driven:** Fix onboarding first. Accelerating features that customers can't reach will make things worse, because more complexity means longer implementations.
- **Mostly product-driven:** Prioritize the specific capabilities that show up in competitive losses, not "AI" generically.
- **Segment-driven:** You may be selling to customers you can't serve well. That's a sales and ideal-customer-profile conversation.
- **Mixed (most likely):** Pick the bigger lever for the majority of churned revenue, and sequence the other.

## A final thought

My prior, for what it's worth: in complex enterprise software sold to insurers, poor time-to-value is very often the underlying driver, and product gaps are the reason customers give on the way out. But that's a prior, not a conclusion. Your data could easily show otherwise, particularly if a competitor made a real leap recently. The most valuable thing you can do as head of CS is replace the debate with evidence both sides agreed to in advance.

## Turn 2

**User:** How do I get two VPs who both think they're already right to actually agree on those decision criteria in advance?

**Assistant:**

Their confidence is actually your lever. People who are sure they're right are usually willing to name the evidence that would prove it, as long as the process feels fair and the stakes don't feel like public humiliation. Your job is to design for both.

## 1. Get a sponsor above both of them

If you're a peer or below, you can facilitate but you can't compel. Go to whoever they both report to (CEO, COO, GM) and ask them to own the question: "Churn has doubled, we have two competing explanations, and I want to resolve it with evidence rather than advocacy." Ideally the sponsor kicks off the process and tells both VPs that resourcing decisions will follow the findings. That turns participation from optional to expected.

## 2. Address your own perceived bias up front

As head of CS, you may look like a natural ally of Services, since you both live with unhappy customers. Say this out loud to the Product VP: "I know I might look like I'm on the Services side. That's exactly why I want the criteria locked before either of us sees data." Having a neutral analyst run the numbers, or someone from finance or bizops, helps a lot.

## 3. Meet with each VP separately first

Don't open with both in a room, where each will perform certainty for the other. In one-on-ones:

- Let them make their full case. Take it seriously and write it down.
- Then ask: **"If you're right, what should we see in the data?"** They'll happily answer, because they're describing their own win.
- Follow with: **"And what would you expect to see if you were wrong?"** This is harder, but it's the same question from the other side.
- Ask: **"What would make you doubt this analysis?"** This surfaces objections like "exit surveys are unreliable" or "the adoption data is incomplete" before results exist, when they're cheap to fix.

You'll come out with each person's own predictions, in their own words.

## 4. Turn their predictions into shared criteria

Draft a one-page document combining both sets of predictions, with each prediction attributed to the person who proposed it. Share it with each VP separately for edits, then bring them together to finalize. Because every criterion came from them, you're asking them to ratify their own thinking, not accept yours.

Include:
- The specific metrics and cuts (adoption depth among churned accounts, implementation overruns, competitive loss destinations, and so on)
- What result points toward which explanation
- What counts as a meaningful difference, stated roughly
- Known data limitations both accept
- How decisions will follow, such as "the larger driver by churned revenue gets priority in next quarter's investment"

## 5. Make "both partially right" the expected answer

Winner-take-all framing makes people defensive. Present the question as **"what share of churned revenue is driven by each factor?"** rather than "who's right?" That way nobody loses outright, and the result becomes an allocation input, not a verdict. It's also probably the truth.

## 6. Give each of them a reason to want this

- **For Product:** If feature gaps are the driver, this gives them hard evidence for the roadmap acceleration and headcount they want, which is far stronger than competitive anecdotes.
- **For Services:** If implementation is the driver, this finally justifies investment in onboarding that they've likely struggled to get funded.

Each should see the analysis as their best chance to win the budget argument.

## 7. Watch for unfalsifiable positions

If one VP responds with something like "customers won't admit it's features, so interviews won't show it" and "adoption data doesn't matter because they'd have adopted if the product were better," they're describing a belief that no evidence can touch. Gently name it: "If nothing we could find would change your view, then we're not really testing anything. What would?" If they still can't answer, that's something your sponsor needs to know.

## 8. Lock it in

Get the final criteria in writing, with both VPs and the sponsor signed off, before any data is pulled. When results come in, open the readout by revisiting the agreed criteria, then show the data against them. Reinterpreting results after the fact is much harder when everyone's prior commitments are on the first slide.

## If one of them refuses

Don't force it. Proceed with the analysis using the criteria the other VP and the sponsor approved, and note that the holdout was invited to shape them. Most people would rather help set the rules than be judged by rules they skipped.

## Turn 3

**User:** What if the data we need doesn't exist? We never tracked implementation timelines or adoption depth consistently.

**Assistant:**

This is very common, and it doesn't sink the effort. You're not trying to publish a study. You're trying to make a better resourcing decision than you'd make on opinion alone. **Approximately right beats precisely nothing.** You'll reconstruct what you can from what exists, accept coarser categories, and start proper tracking now.

## 1. Reconstruct implementation history from records you do have

The data wasn't tracked on purpose, but it often left traces:

- **Contracts and SOWs:** signed date, planned go-live, scope sold.
- **Billing records:** services milestone invoices, change orders, and extensions often mark real progress and overruns. Change orders are a strong signal of a troubled implementation.
- **Project tools and shared drives:** old project plans, status reports, kickoff and go-live decks.
- **Support system:** the first production-related ticket is often a decent proxy for actual go-live. Escalation history shows pain.
- **CRM notes and email:** go-live announcements, escalation threads, renewal-risk notes.
- **Calendar invites:** kickoff meetings, go-live cutovers, steering committees.

## 2. Extract adoption from the product itself

Even without product analytics, your application database almost certainly records usage as a side effect:

- Claims created or processed per customer over time
- Active user accounts vs. licensed seats
- Which modules have any records in them at all
- Login or session records, if retained

"Did this carrier process most of its claim volume through us, or only a fraction?" is a powerful adoption measure, and an engineer can often pull it in days. Ask what's retained for churned customers before deprovisioning scripts delete it.

## 3. Use structured recall from the people who were there

Implementation managers, consultants, CSMs, and support leads remember a lot. Capture it systematically:

- Build a short rubric with defined categories, such as implementation: **on time / moderately late (under 3 months) / badly late or de-scoped**; adoption: **full / partial / minimal**.
- Have people rate accounts against the rubric, not tell stories.
- **Reduce bias:** where possible, have raters score accounts without being told whether they churned, or mix churned and retained accounts in the same list. Get two raters for important accounts and reconcile differences. People's memories bend toward "of course that one churned."

## 4. Sample rather than trying to cover everything

You don't need every account. A well-reconstructed set of, say, 25 churned and 25 retained accounts, weighted toward the largest by revenue, will tell you more than a patchy census. Prioritize accounts where records and knowledgeable people still exist.

## 5. Adjust the decision criteria to match the data

Tell both VPs, ideally before reconstruction starts, that the criteria need to be coarser. For example, "churned accounts were more than twice as likely to have badly late implementations" instead of precise duration comparisons. This protects the pre-commitment. If you change the rules after seeing results, you lose the whole point.

## 6. Lean more on interviews

With weaker quantitative data, customer interviews carry more of the load. Timeline-focused questions ("when did you go live, on what scope, what happened in the first six months?") partially fill the gap, since former customers often remember their implementation vividly.

## 7. Treat current customers as a forward-looking study

Your in-flight implementations and upcoming renewals are data you can capture properly starting now. Within two or three quarters, you'll see whether troubled implementations and low adoption predict risk, with clean data.

## 8. Start tracking now, minimally

Don't build an elaborate system. Record for every account:
- Contracted go-live date and actual go-live date
- Scope sold vs. scope live
- A monthly adoption measure, such as share of claim volume processed or active users vs. licensed
- Health score and renewal date

## One more point worth making to leadership

The fact that a claims-software company never tracked whether customers finished implementation or used what they bought is itself a finding. It doesn't prove the Services VP is right, but it does mean no one could have seen an onboarding problem coming if there was one. Whatever the diagnosis shows, the tracking gap is worth fixing.

## Turn 4

**User:** How many former customers will actually agree to an interview, and how do I get them to talk honestly once they've already left?

**Assistant:**

Expect a meaningful minority to say yes, not most. Rough ranges, which vary a lot with relationships and how long ago they left:

- **Cold outreach from someone they don't know:** often 10–20%
- **Personal ask from someone they trusted:** often 30–50%
- **Recently churned, left on decent terms:** higher
- **Left angry, or left 2+ years ago:** lower

For 15–20 interviews, plan to contact **60–100 people**, not 20 accounts. That means multiple contacts per account.

## Getting more people to say yes

**Ask more than one person per account.** The executive sponsor, the claims operations lead, the IT or integration lead, and the internal project manager each saw something different. Middle managers who did the daily work are often more willing and more candid than executives.

**Find people who've since left the carrier.** Former champions and project leads who've changed jobs have no relationship to protect and often speak most freely. LinkedIn makes them easy to find.

**Have the right person ask.** A note from the CSM or implementation lead they liked works far better than a generic email. For accounts where relationships soured, an ask from your CEO or a neutral third party can work better than anyone they associate with the problem.

**Promise explicitly that it's not a sales call, and keep that promise.** Many will assume you're trying to win them back. Say plainly: "We're not trying to sell you anything. We're trying to understand what we got wrong." Nothing destroys trust faster than a learning interview that turns into a pitch.

**Make it small.** Ask for 30 minutes, offer flexible times, and let them choose phone or video.

**Offer a modest thank-you.** A donation to a charity of their choice is often the cleanest option. Insurance carriers can have strict gift policies, so a charity donation avoids compliance awkwardness.

**Appeal to their influence.** Many people like being asked for their expertise: "You saw our implementation up close, and your perspective will directly shape how we change." Regional insurance is a small industry, and some will appreciate a vendor genuinely trying to improve.

## Getting honest answers once they're talking

**Use an interviewer who isn't part of the story.** Customers soften criticism when talking to someone who might have caused the problem or who they'll see at industry events. A third-party firm gets the most candor. If that's not possible, use someone neutral inside your company, not someone from Product, Services, or their former account team.

**Offer confidentiality and mean it.** Tell them comments will be reported in aggregate, not attributed by name, unless they give permission. Ask permission to record, and keep recordings within the analysis team.

**Ask about the timeline, not the reason.** "Why did you leave?" gets a tidy, rehearsed answer. Instead, walk through the story:
- "Take me back to when you first signed. What were you hoping to get?"
- "How did implementation go? When did you go live, and on what scope?"
- "What did the first six months look like for your team?"
- "When did you first start thinking about alternatives? What was happening then?"
- "Who pushed for the change internally, and what convinced them?"

The moment they started looking is usually more revealing than the reason they gave at the end.

**Probe the easy answers.** If they say "the competitor had better AI," follow up gently:
- "When did that become important? Was it part of why you started looking, or something you found during the evaluation?"
- "If we'd had those features, would you have stayed?"
- "How much of our current product were you using at the time?"

This isn't about catching them out. It's about separating the trigger from the justification.

**Don't defend, explain, or correct.** Even if their account seems unfair or wrong, just take notes and ask follow-ups. One defensive reaction and they'll switch to polite generalities for the rest of the call.

**Give permission to criticize.** Something like "The most useful thing you can tell us is what frustrated you. You won't hurt anyone's feelings" helps.

**Ask a counterfactual near the end:** "If you could go back and change one thing we did, what would have made you stay?" People often give their most honest answer here.

**Ask about the new vendor:** "What's different now?" This reveals what they actually valued. If they say "their team got us live in four months," that's telling.

## Two more things

**Interview current and at-risk customers too.** Those conversations are easier to get, and they tell you whether the frustrations of churned customers are shared by customers who stayed, which helps separate cause from coincidence.

**Close the loop.** Send a thank-you, and later, a short note on what you changed. It's the right thing to do, it keeps goodwill in a small industry, and occasionally a former customer comes back because they saw you listen.

## Turn 5

**User:** What should we do?

**Assistant:**

Pulling everything together, here's the plan I'd run, in order.

## Weeks 1–2: Set up the decision

1. **Get a sponsor.** Bring the CEO or COO in to own the question and state that resourcing will follow the findings.
2. **Meet each VP separately.** Capture their case, what they'd expect to see if right, what they'd expect if wrong, and what would make them distrust the analysis.
3. **Lock the decision criteria.** Combine their predictions into a one-page document, adjusted for the coarse data you'll actually have, and get written sign-off from both VPs and the sponsor before any data is pulled.
4. **Assign neutral owners.** A bizops or finance analyst runs the data, and a third party or neutral internal person runs interviews.

## Weeks 1–6: Protect revenue now, regardless of the answer

These are worth doing whichever VP turns out to be right:

- **At-risk renewals:** review every account renewing in the next 12 months, score health, and start executive outreach on the shakiest ones.
- **Implementation rescue:** review every in-flight implementation that's behind schedule or de-scoped. These are next year's churn.
- **Minimal tracking going forward:** contracted vs. actual go-live, scope sold vs. live, a monthly adoption measure, health score, and renewal date for every account.

## Weeks 2–6: Gather the evidence

- **Reconstruct history** for roughly 25 churned and 25 retained accounts, weighted by revenue, using contracts, change orders, support tickets, product database usage, and structured, partly blinded ratings from staff.
- **Check for other causes:** acquisitions, pricing changes, segment shifts, competitor launches, and team changes in the period when churned customers were implementing.
- **Run 15–20 interviews,** contacting 60–100 people across roles, including former champions who've changed jobs, plus a handful of current and at-risk customers for comparison.

## Week 7: Read out and decide

- Open the readout with the pre-agreed criteria, then show results against them.
- Frame the answer as **share of churned revenue by driver**, not a winner.
- Allocate accordingly:
  - **Mostly implementation and adoption:** fix onboarding first, and slow feature expansion that adds implementation complexity.
  - **Mostly product gaps:** accelerate the specific capabilities that show up in competitive losses, not "AI" generally.
  - **Mostly fit or external:** tighten who sales targets, and treat consolidation churn separately.
  - **Mixed:** fund the bigger driver first and sequence the other, with named owners and metrics for both.

## Ongoing: Make sure you never have to do this blind again

- Review churn drivers quarterly using the new tracking.
- Use in-flight implementations as a live test of whether time-to-value predicts renewal.
- Close the loop with interviewees on what changed.

## If you need to place a bet before the data comes in

Put your first dollars into onboarding and adoption for current customers. It protects near-term renewals, it's rarely wasted even if product gaps matter too, and new features can only help customers who get far enough to use them. But hold that loosely, and let the evidence you've agreed on make the real call.

## Outcome summary (sent to Jev)

The assistant recommends settling the product-versus-service dispute with evidence rather than choosing a side, because both explanations are plausible and make different, testable predictions. The likely answer is some mix, so the question should be framed as what share of churned revenue each driver explains.

In the first two weeks, a CEO or COO sponsor should own the question and commit to letting resourcing follow the findings. Each VP should be interviewed separately to capture what they would expect to see if right or wrong. Their predictions become one-page decision criteria, coarsened to fit the limited data, and both VPs and the sponsor sign off before any data is pulled. A neutral analyst runs the numbers and a third party or neutral insider conducts interviews.

No-regret moves start immediately: health scoring and executive outreach for renewals in the next 12 months, rescue reviews of late or de-scoped implementations, and minimal ongoing tracking of go-live dates, scope, monthly adoption, health, and renewal dates.

From weeks two to six, the team reconstructs history for about 25 churned and 25 retained accounts from contracts, change orders, tickets, usage data, and partly blinded staff ratings. It also checks for acquisitions, pricing changes, segment shifts, competitor launches, and team changes. It runs 15 to 20 timeline-focused interviews, which requires contacting 60 to 100 people.

At week seven, results are presented against the agreed criteria. Resources go to onboarding, specific competitive capabilities, targeting, or the larger driver first if the picture is mixed.

If a bet is needed early, it should go to onboarding and adoption, held loosely until the evidence decides.
