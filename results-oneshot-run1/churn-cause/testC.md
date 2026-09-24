# churn-cause/critical-rationalism/testC

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:51:36.625580+00:00

## Prompt

Use the method of conjectures and refutations (critical rationalism) to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

# Which Belief Explains Your Churn? A Conjectures-and-Refutations Approach

## Short answer

Neither belief can be declared right yet, and I'd resist anyone who claims certainty. Critical rationalism says we don't prove theories by piling up supporting examples. Both VPs can easily find churned customers who fit their story. We make progress by stating each theory sharply enough that it could be shown wrong, then trying hard to show it wrong. The theory that survives serious attempts at refutation earns provisional trust.

Your data can probably settle much of this in a few weeks. Below is how to set that up, and what to do while it runs.

---

## Step 1: Sharpen both conjectures until they can fail

As currently stated, both beliefs are nearly unfalsifiable:

- "Customers never get to full value" can explain any churn.
- "Competitors have better features" is true in some respect for almost any product.

**Ask each VP a Popperian question before looking at any data: "What evidence would convince you that you're wrong?"** Write the answers down. A belief whose holder can't name any refuting evidence isn't a diagnosis. It's a worldview. Committing in advance also stops people from reinterpreting results afterward.

Stated so they can fail, the conjectures become:

- **H1 (Product gaps):** Customers who successfully adopted the product are leaving because competitors offer superior analytics/AI capabilities they need.
- **H2 (Implementation/service):** Customers are leaving because they never reached full adoption and value, owing to long implementations and poor support.

## Step 2: Derive predictions where the two theories disagree

Evidence both theories predict is useless. Churned customers complaining is an example. Look for **risky, differential predictions**:

| Test | If H1 (product) is true | If H2 (service) is true |
|---|---|---|
| **Adoption split:** churn rate among well-implemented, heavily used accounts vs. poorly adopted ones | Well-adopted accounts churn at substantial rates too. They "outgrew" you. | Well-adopted accounts rarely churn. Churn concentrates in low-adoption accounts. |
| **Implementation duration** | Weak or no correlation with churn | Strong correlation. Long implementations predict churn. |
| **Destination:** where churned customers went | Mostly to competitors with demonstrably stronger analytics/AI | A mix, including competitors without better features, legacy systems, or in-house tools |
| **Cohort timing** | Churn spread across tenure. Long-tenured accounts leave too. | Churn concentrated at first renewal |
| **What changed ~18 months ago** | Competitor analytics/AI launches preceded the rise | Services capacity, staffing, backlog, or support metrics degraded before the rise |
| **New-business win/loss** | Win rates fell over the same period, with losses citing analytics/AI | Win rates roughly stable (prospects still like the product; customers dislike the experience) |
| **Support signals** in churned accounts | Feature requests dominate | Escalations, long resolution times, and low CSAT dominate |

**The adoption split is your single most decisive test.** Either result refutes one theory:

- If happy, fully adopted customers are leaving in meaningful numbers, H2 cannot be the main story.
- If they almost never leave, H1 is badly weakened. Competitors' AI features apparently aren't pulling away customers who get value from you.

**The timing test is the second most important.** Churn *doubled*, so something *changed*. Any adequate theory must explain the timing, not just the churn.

## Step 3: Treat stated reasons with suspicion

Exit interviews are weak evidence, and they're biased toward H1.

- "Your competitor has better AI" is a polite, face-saving reason. It's also what a buyer tells their own management to justify a switch.
- A customer who never implemented your analytics may truly believe the competitor's demo is superior. The real cause is still adoption.

So weight **behavioral data** over stated reasons: usage, time-to-go-live, ticket history, destination. When you do interview, use an independent party and ask for a **timeline** rather than a reason. "When did you first start considering alternatives? What was happening that month?" Chronology is much harder to rationalize after the fact than motives are.

Also note that each VP's data sources are filtered through their function. Product hears feature requests. Services hears implementation complaints. That's another reason to go to raw account-level data.

## Step 4: Generate rival conjectures

Critical rationalism warns against framing a problem as a two-way contest. The truth may be a third theory neither VP has considered. Test these too:

- **H3: Market consolidation.** Regional carriers are being acquired, and the acquirer standardizes on its own system. Check what share of churned ARR came from carriers that were merged or acquired. If it's large, neither roadmap nor onboarding fixes it.
- **H4: Suite bundling.** Core-system vendors bundle claims with policy and billing, so you're losing a platform decision, not a feature comparison. Check whether churned customers moved to a suite.
- **H5: Customer mix shift.** Sales pushed into poorer-fit segments 18–30 months ago, and those accounts churn. This would produce evidence that looks like *both* H1 and H2. Compare churn by segment and by sales cohort.
- **H6: Pricing.** A price increase or packaging change at renewal is a candidate. Check whether churn correlates with renewal uplift.
- **H7: Relationship loss.** Turnover among your CSMs or customers' internal champions may be driving exits. Check churn after CSM reassignment or champion departure.
- **H8: Interaction.** Implementations may run long *because* the product lacks configurability, so product gaps show up as service pain. In that case the fix sits in product, but not in analytics/AI.

Also rule out noise. If "doubled" means 6 logos became 12, examine each case individually rather than drawing statistical conclusions. Check whether the doubling holds for revenue churn as well as logo churn.

## Step 5: What to do

**This month:** Build one account-level dataset covering every churned and retained account over three or so years. Include:

- implementation duration and time-to-go-live
- adoption depth
- analytics module usage
- support metrics
- segment and sales cohort
- renewal price change
- M&A status
- destination

Run the tests above, with each VP's pre-committed refutation criteria on the table. The analysis will likely rule some theories out fast.

**Meanwhile, act in small, reversible, testable steps.** Popper called this "piecemeal engineering." Avoid a wholesale bet, and be especially wary of "accelerate the roadmap." It's slow and expensive, and with annual renewals you won't learn whether it worked for a year or more. Make every intervention an experiment:

- **Service test:** Run a structured "implementation rescue" for a subset of at-risk, low-adoption accounts. Stagger or randomize who gets it first, and compare leading indicators against similar accounts: usage, health score, renewal intent. You'll get signal within a quarter.
- **Product test:** Before a major roadmap push, try a cheap probe with a subset of accounts, such as a BI integration, a partner analytics tool, or a minimal feature. If well-adopted accounts still leave after getting it, the "AI gap" theory weakens considerably.

**Decision rule, set in advance:**

- If well-adopted accounts churn at comparable rates and customers go to feature-superior competitors, shift investment toward product, and target the specific gaps churned customers left for, not a generic "AI" roadmap.
- If churn concentrates in long-implementation, low-adoption, first-renewal accounts, fix onboarding first. More features won't help customers who never use the ones they have.
- If consolidation, bundling, or segment mix explains much of it, the answer lies in strategy or sales qualification, and both VPs' plans are partly beside the point.

## A note on priors

In enterprise B2B software, poor adoption is a common, strong predictor of churn, and "missing features" is a common stated reason for it. That makes H2 a slightly better opening bet in my view. But this is a prior, not a verdict, and your adoption-split and timing data can overturn it quickly.

The most valuable outcome isn't picking the winning VP. It's getting your leadership team into the habit of stating theories that can fail and then trying to make them fail.

## Summary (sent to Jev)

The response argues that neither VP's belief can be declared right yet, because both can find churned customers who fit their story. Drawing on critical rationalism, it recommends stating each theory sharply enough to be refuted and then trying to refute it. Each VP should say in advance what evidence would prove them wrong.

It reframes the beliefs as testable hypotheses. Under the product hypothesis, well-adopted customers leave for competitors with better analytics and AI. Under the service hypothesis, customers leave because long implementations and poor support keep them from full value. The most decisive test is the adoption split. If heavily used accounts churn substantially, the service theory weakens; if they rarely churn, the product theory weakens. The second most important test is timing, since doubled churn implies something changed. Further tests include:

- implementation duration
- where churned customers went
- tenure at churn
- new-business win rates
- support signals

Exit interviews deserve suspicion because "better AI" is a face-saving reason. Behavioral data should outweigh them, and any interviews should be run independently and ask for timelines rather than reasons.

The response also urges testing rival explanations: acquisitions of carriers, suite bundling, a shift toward poorer-fit customers, pricing changes, relationship loss, and product configurability gaps that surface as service pain. If the numbers are small, it suggests examining cases individually and checking revenue churn as well as logo churn.

For action, it proposes building an account-level dataset now and running small, reversible experiments in the meantime: an implementation rescue for some at-risk accounts and a cheap analytics probe. It cautions against a slow "accelerate the roadmap" bet and sets decision rules in advance. Its prior slightly favors the service explanation, but it stresses that this is not a verdict.
