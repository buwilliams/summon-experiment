# churn-cause/economic/testB

Model: claude-opus-5-5 · 2026-09-24T15:30:47.204701+00:00

## Turn 1

**User:** You are a world-class economist who studies how firms make profits.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Neither Belief Is Proven Yet, But You Can Test Them

Both VPs are offering hypotheses that happen to recommend investing in their own function. That doesn't make either one wrong, but it does mean you shouldn't settle this by who argues better. The two explanations make **different, testable predictions**, and you likely already have the data to check them.

## The economics of a renewal decision

A carrier renews when:

> **Value it actually realizes − your price  >  value of the best alternative − switching cost**

- **Product VP's claim:** the right-hand side rose. Competitors' offerings got better.
- **Services VP's claim:** the left-hand side is low. Customers never realize the value you sell.

These interact through a term people often overlook: **switching cost**. Claims systems are normally very sticky because they're embedded in workflows, integrations, adjuster habits, and reporting. A customer who never fully implemented hasn't built that stickiness. A poorly implemented customer is therefore both underwhelmed *and* cheap to lose, which makes them far more responsive to a competitor's AI demo. A deeply embedded, happy customer will tolerate a feature gap for years.

So the likely answer is not "one or the other." The two problems probably compound, and the question is **which one is the binding constraint**.

## What each hypothesis predicts

| Evidence | If it's a product gap | If it's implementation/value |
|---|---|---|
| **Who churns** | Well-implemented, high-adoption accounts | Accounts with long implementations, partial go-lives, low usage |
| **When they churn** | Any renewal, clustered after competitor launches | Disproportionately at first renewal |
| **Cohort pattern** | Old and new cohorts churn similarly | Recent cohorts churn much worse than older ones |
| **Where they go** | Specific competitors with stronger analytics/AI | Scattered destinations, including suite vendors or "anyone else" |
| **New-logo win rates** | Also falling; you're losing deals on features | Stable; you win deals but lose at renewal |
| **Leading indicators** | Healthy usage until a competitor appears | Low logins, few modules live, high tickets, low CSAT well before the renewal |

The **new-logo win rate** is a particularly clean test. If prospects still choose you in head-to-head evaluations, your product is competitive on paper, and the leak is in delivering value. If you're also losing new deals on analytics and AI, the product gap is real in the market.

## Be skeptical of exit interviews

Churned customers often say "you lacked AI/analytics features" because it's a polite, procurement-friendly reason. It's easier than saying "your implementation burned us out" or "we never got it working." **Weight behavior (adoption data) over stated reasons.** If "missing feature" churners never used the analytics you already have, that tells you something.

## Rule out the alternatives first

Doubling in 18 months suggests something *changed*. Check these before you fund either roadmap:

1. **Carrier M&A.** Regional carriers are consolidating. Acquired customers churn regardless of product or service.
2. **Suite displacement.** Carriers moving to an end-to-end core platform (e.g., Guidewire, Duck Creek) may drop point solutions, including yours.
3. **Mix shift.** Did sales expand into smaller carriers or new lines of business that fit less well? That shows up as churn but is really a targeting problem.
4. **Internal changes.** Implementation team turnover, a reorg, pricing changes, or a botched release in that window.
5. **Logo vs. revenue churn.** Losing many small accounts is a different problem from losing a few large ones.

## What I'd do

**Weeks 1–6: diagnose.** Pull every churned and at-risk account from the last two years. Tag each with cohort, implementation duration, go-live completeness, usage depth, support history, stated reason, destination, and whether it was acquired. Compare against retained accounts. Pull win/loss data on new deals over the same period. This is a spreadsheet exercise, not a consulting engagement.

**Now, in parallel: triage.** Build a simple risk score from adoption data and put your team on the accounts renewing in the next two quarters. Retention saves are worth more than either VP's long-term plan.

**Then fund the binding constraint.** My prior, based on how enterprise software in regulated industries usually fails, is that **implementation and value realization is more often the binding constraint.** A critical detail supports this: analytics and AI in claims run on clean, integrated, flowing data, and that depends on a *complete implementation*. Customers who aren't fully live can't benefit from better AI features. So even the Product VP's roadmap pays off only once the Services VP's problem is solved.

That's a prior, not a verdict. If the data shows well-adopted, deeply embedded customers leaving for competitors' features, and you're losing new deals on the same grounds, then the Product VP is right and speed matters. Either way, let the cohort data make the decision, not the internal debate.

## Turn 2

**User:** Our usage tracking is pretty patchy for accounts from more than a year ago, so how would I run this comparison if I can't reliably measure adoption for a lot of the customers who already churned?

**Assistant:**

# Running the Comparison Without Good Usage Data

Patchy telemetry is a real limitation, but it's less damaging than it looks. Only one of the six tests I suggested actually requires usage data, and even adoption can be reconstructed from records your company almost certainly keeps for other reasons.

## 1. Start with the tests that don't need usage data

These come from contracts, CRM, and project records, which are usually retained well:

- **Churn timing:** Did accounts leave at first renewal or later? First-renewal churn points to value realization.
- **Cohort curves:** Are recent cohorts churning faster than older ones at the same age?
- **Implementation duration:** Planned vs. actual go-live dates, from project plans or SOWs.
- **Destination:** Where did they go? Your sales team, press releases, LinkedIn, and competitor case studies often reveal this.
- **New-logo win/loss:** Are you losing new deals on features?
- **Acquisition status:** Were they bought?

If these point clearly in one direction, you may not need precise adoption data at all.

## 2. Reconstruct adoption from indirect sources

Look for records created for billing, operations, or support that indirectly reveal adoption:

| Source | What it tells you |
|---|---|
| **Your application database** | Claims created or processed per month. This is the best proxy, since the product stores its own transactions even when analytics weren't tracking. A carrier running most of its claims through you is embedded; one running a trickle isn't. |
| **Identity/SSO and license records** | Users provisioned vs. seats purchased, and last-login dates. |
| **Integration and API logs** | Whether data feeds (policy admin, payments, document management) were ever connected. Server-side logs often outlive product analytics. |
| **Contracts and billing** | Modules purchased vs. modules ever activated; expansions or downgrades; services overruns and change orders. |
| **Support tickets** | Volume and type. "How do I…" and integration tickets suggest incomplete implementation. Feature requests and competitor mentions suggest product gaps. |
| **Implementation records** | Milestones completed, phases descoped, whether "go-live" meant full or partial. |
| **CSM notes, QBR decks, health scores** | Rough but contemporaneous judgments of account health. |

## 3. Use a coarse measure

You don't need a precise adoption score. Classify each account into three buckets:

1. **Never fully live:** partial go-live, key integrations missing, low claims volume
2. **Live but shallow:** core workflow running, few modules or users
3. **Embedded:** most claims volume, integrations connected, broad usage

Write down the classification rules before you look at outcomes. Then have someone without a stake in the debate do the coding, ideally not either VP's team. Where records are thin, fill in with **short structured interviews** of the CSMs and implementation leads who ran those accounts. Ask about facts ("Was the payments integration ever live?") rather than opinions ("Why did they leave?").

## 4. Watch for bias from the missing data

The main risk is that your data gaps aren't random.

- **Compare like with like.** Compare churned and retained accounts from the same time period, so data quality is similar on both sides. Don't compare old churned accounts with patchy data to recent retained accounts with good data.
- **Make the last 12 months your primary test.** Your data is reliable there. Use older accounts as corroboration, not as the main evidence.
- **Check whether missingness itself is a signal.** Accounts with no usage records may be the ones that barely used the product. Record "unknown" as its own category and see how it behaves rather than dropping those accounts.

## 5. Call former customers

Talk to 10–15 former customers, ideally users or claims managers rather than the executive who signed the termination. Ask about behavior, not reasons:

- "What share of your claims ran through our system?"
- "Which parts did your adjusters actually use?"
- "What did you do in spreadsheets or other tools instead?"

These answers are more reliable than "why did you leave," which invites the polite "you lacked AI features" response.

## 6. Run a forward-looking test

Your current customers can be measured properly starting now. Instrument adoption, classify every active account using the same three buckets, and track which ones renew over the next two to three quarters. This gives you a clean test of whether adoption predicts retention, and it doubles as the risk score for your triage work.

## Judging the result

No single proxy will be conclusive. But if churn timing, cohort curves, claims volume, integration status, and ticket patterns all point the same way, that convergence is strong evidence. If they conflict, that tells you the answer is mixed, and you should look at which segments fit which explanation.

## Turn 3

**User:** How do I get both VPs to agree up front on what results would prove them wrong, so this doesn't turn into another argument once the data comes back?

**Assistant:**

# Getting Both VPs to Commit Before the Data Comes In

What you want is **pre-registration**: agreeing on the questions, definitions, evidence, and decision rules *before* anyone sees results. Once the data is in, every ambiguous number becomes a fight over interpretation. Beforehand, both VPs are uncertain, which is the only time they'll accept rules that might go against them.

## 1. Lower the cost of being wrong

People resist falsifiable commitments when losing the argument means losing budget, headcount, or status. Before you ask for predictions, change the stakes:

- **Frame the decision as allocation, not a verdict.** The question is "how should we split the next two quarters of investment," not "whose theory is right." Both functions will get some resources under any outcome.
- **Give each VP a role in the other's fix.** If the answer is implementation, Product likely owns things like data onboarding tools and in-product guidance. If the answer is product gaps, Services owns rolling out new features to existing accounts. Neither walks away empty-handed.
- **Get your executive sponsor (CEO or COO) to say this publicly.** It carries more weight from them than from you, and it signals the decision rules will actually be honored.

## 2. Hold a structured pre-registration session

Run a single 90-minute working session with both VPs, you, the analyst who'll do the work, and ideally the sponsor. Work through these steps in order:

**a. Each VP states their prediction in writing.** Use the prediction table from earlier as the starting point. Each VP fills in what they expect to see for churn timing, cohort pattern, adoption level of churners, destination, and win rates. Specific numbers are better than directions: "at least 60% of churned revenue will come from embedded accounts," not "embedded accounts will churn."

**b. Each VP states what would change their mind.** Ask directly: "What result would convince you that your explanation is not the main driver?" If someone can't name any result, their hypothesis isn't testable yet, and the group should sharpen it until it is.

**c. Each VP steelmans the other's case.** Have the Product VP describe what evidence would support the Services explanation, and vice versa. This surfaces hidden disagreements about definitions early and lowers the temperature.

**d. Agree on definitions.** Most post-hoc arguments are really definitional. Settle these now:
- What counts as churn: logo, revenue, or both? Partial downgrades?
- The three adoption buckets and the exact rules for classifying accounts
- How to treat acquired carriers (likely exclude them or analyze them separately)
- The time window and which accounts are in scope
- What "first renewal" means for multi-year contracts

**e. Agree on the data sources and how to handle gaps.** Specify which proxies you'll use, the 12-month window as the primary test, and how "unknown" accounts will be treated. Agree now that no one gets to add or drop data sources after seeing results.

**f. Run a quick pre-mortem.** Ask each VP to imagine the results came back against them and they're objecting. What would their objection be? Address those objections now, either by adjusting the method or by agreeing they won't be valid later.

## 3. Write decision rules, including for mixed results

Tie outcomes to actions in advance. A simple version:

| Result | Decision |
|---|---|
| Most churned revenue comes from accounts that were never fully live or were shallow, and new-logo win rates are stable | Prioritize implementation and value realization; roadmap proceeds at current pace |
| Most churned revenue comes from embedded accounts leaving for competitors' features, and new-logo win rates are falling on features | Accelerate the roadmap; Services focuses on rolling out features to existing accounts |
| Both patterns appear, in different segments | Split investment by segment, sized to each segment's share of churned revenue |
| Most churn comes from other causes (M&A, suite displacement, mix shift) | Neither VP's plan is the priority; address the actual cause |
| Results are inconclusive | Rely on the forward-looking adoption test and revisit in two quarters, with modest investment in both meanwhile |

**Plan explicitly for the mixed outcome, because it's the most likely one.** It's also where arguments tend to break out, since each side can point to the half that supports them. A pre-agreed rule like "weight by share of churned revenue" prevents this.

Keep thresholds reasonable rather than precise. You're using imperfect proxies, so a rule like "clear majority, roughly 60% or more" is more honest than pretending 51% versus 49% is meaningful.

## 4. Protect the analysis itself

- **Use a neutral analyst.** Someone from finance, RevOps, or strategy, not a member of either VP's team.
- **Have the account classification done blind where possible.** The person coding adoption levels shouldn't know which accounts churned. This isn't always feasible, but even partial blinding helps.
- **Share the method, not interim results.** Both VPs can review the process and challenge the methodology during the work, but no one sees partial findings until it's done. Early peeks invite lobbying.
- **Log any changes to the plan.** If the analyst has to deviate, for example because a data source turns out to be unusable, record the change and the reason, and share it with both VPs before results are revealed.

## 5. Put it in writing and get sign-off

Turn the session into a two-page document: the question, each VP's predictions, the disconfirming evidence each named, definitions, data sources, decision rules, and the timeline. Have both VPs and the sponsor sign off by email. When results come back, open the meeting by reading the document aloud before showing any data.

## 6. Present results against the predictions

Structure the readout around the pre-registered predictions. Show each prediction next to what the data showed. This keeps the discussion on "what did we agree this would mean" rather than a fresh debate.

If someone still objects, the test is simple: **is this an objection we anticipated and resolved in the pre-mortem?** If so, it's settled. If it's genuinely new and substantive, note it, but it doesn't override the decision rules. It becomes something to check in the forward-looking test.

## A realistic expectation

This won't eliminate disagreement entirely, and it shouldn't. What it does is change the argument from "whose story is right" to "did we follow the rules we agreed on," which is a much easier conversation to resolve. It also builds a habit your team can reuse for the next major investment decision.

## Turn 4

**User:** What if one of the VPs just refuses to put specific numbers on their predictions, or keeps hedging so nothing could prove them wrong?

**Assistant:**

# When a VP Won't Commit to Falsifiable Predictions

Hedging usually has a reason behind it, and the right response depends on which reason it is. Figure that out first, ideally in a private one-on-one before the group session, where the VP can speak candidly without losing face.

## 1. Diagnose why they're hedging

| Likely reason | What it sounds like | What helps |
|---|---|---|
| **Genuine uncertainty** | "I really don't know what the numbers will be." | Ask for ranges or comparisons instead of point estimates |
| **Distrust of the data** | "The usage data is too patchy to prove anything." | Fix or agree on the method, so their concern is addressed up front |
| **Fear of consequences** | "Let's not box ourselves in." | Lower the stakes; reinforce that both functions keep a role |
| **They believe it's "both"** | "It's obviously a mix of factors." | Have them quantify the mix |
| **Strategic evasion** | Shifting goalposts, vague answers no matter how the question is framed | Make the cost of vagueness explicit; escalate if needed |

Most hedging falls into the first four categories, and each has a constructive fix. Assume good faith until repeated attempts rule it out.

## 2. Make it easier to be specific

Many people resist point estimates because they feel like a test they can fail. Change the format of the question:

- **Ask for ranges.** "Not an exact number. What share of churned revenue would you expect from fully embedded accounts: under 25%, 25–50%, or over 50%?"
- **Ask comparative questions.** "Do you expect accounts from the last year to churn faster or slower than older cohorts?" Direction alone is often enough to be falsifiable.
- **Ask about surprise instead of prediction.** "What result would genuinely surprise you?" People who won't say what they expect will often say what they don't expect, and that's the disconfirming evidence you need.
- **Use the other VP as an anchor.** "Your counterpart predicts most churned accounts were never fully live. Do you agree or disagree with that?" Reacting to a claim is easier than generating one.
- **Ask what they'd bet.** "If you had to put your own budget on it, which way would you bet?" This cuts past diplomatic hedging.
- **Offer the "it's both" framing and ask them to size it.** "Suppose it's a mix. Roughly what share would you attribute to product gaps versus implementation?" A 70/30 view and a 30/70 view lead to different decisions, so the split itself is a testable prediction.

## 3. Address legitimate concerns about the method

If the hedge is really "the data won't be good enough," treat it as a valid contribution, not an obstacle:

- Ask what evidence they *would* trust, and build it into the plan.
- Add the forward-looking adoption test as a backstop, so imperfect historical data isn't the only evidence.
- Agree on what "inconclusive" looks like and what happens in that case.

Once the method includes their preferred evidence, it's much harder to justify refusing to commit.

## 4. Make clear that vagueness doesn't exempt anyone from the rules

If gentler approaches fail, state plainly, and without accusation, how the process works:

- **The decision rules apply regardless.** "Whether or not you give specific predictions, we'll decide using the agreed rules. Specific predictions just let your view shape the criteria."
- **An untestable hypothesis is a weak basis for investment.** "If no result could show that product gaps aren't the main driver, then the data can't show that they are, either. That makes it hard to justify accelerating the roadmap based on this analysis."
- **Silence becomes a default position.** "If we don't hear a specific prediction by Friday, we'll use the thresholds in the draft, and those will be the benchmarks for your hypothesis too."

This reframes specificity as being in the VP's own interest. A VP who commits has more influence over the criteria than one who doesn't.

## 5. Escalate if it continues

If a VP is still evasive after good-faith attempts, bring in your executive sponsor. The sponsor can:

- State that pre-committing to predictions is an expectation for anyone requesting significant investment
- Set a deadline for submitting predictions
- Make the final call on decision rules if the VPs can't agree

Frame the escalation around the decision, not the person: "We need the sponsor to set the criteria because we couldn't reach agreement," rather than "The VP won't cooperate." This keeps the relationship intact for the work that follows.

## 6. Check whether the hedging is itself informative

Sometimes a VP hedges because, on reflection, they realize their confidence was overstated. That's a useful result. If the Product VP can't name any evidence they'd expect to see, that suggests the belief in feature gaps may rest more on intuition or anecdote than on observed patterns. The same holds for the Services VP. You don't need to point this out, but it's worth factoring into how much weight their position carries.

## One caution

Apply the same standard to both VPs. If one faces pressure to be specific while the other's vague predictions are accepted, the process will look rigged, and the outcome won't be trusted no matter what the data shows. Consistency is what makes the eventual result stick.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

We've covered a lot of ground, so here's the whole plan in one place, with a clear recommendation at each step. The key point is that you don't have to wait for the diagnosis to start acting. Some moves make sense under either explanation.

## Start this week, regardless of who's right

**1. Protect upcoming renewals.** List every account renewing in the next two quarters. Rank them by risk using whatever signals you have: claims volume, integrations live, ticket history, CSM judgment. Put your strongest people on the top 10–15 revenue accounts. Every save here is worth more than anything else on this list.

**2. Start measuring adoption properly.** Instrument claims volume, active users, modules live, and integrations connected for every current account. This fixes your data gap going forward, feeds the risk ranking, and sets up the forward-looking test.

**3. Freeze big bets for about six weeks.** Don't approve a major roadmap acceleration or a services overhaul until the diagnosis is in. Normal work continues; large new commitments wait.

## Weeks 1–2: set up the diagnosis

**4. Hold the pre-registration session.** Get both VPs to write down predictions, what would prove them wrong, definitions, and the decision rules, including the rule for mixed results. Have your sponsor sign off. Keep it to one meeting and a two-page document.

**5. Assign a neutral analyst** from finance, RevOps, or strategy to own the work.

## Weeks 2–6: run it

**6. Do the analysis in this order:**
- Rule out other causes first: acquisitions, suite displacement, and shifts in the customer mix
- Run the tests that don't need usage data: churn timing, cohort curves, implementation duration, destination, and new-logo win rates
- Classify accounts into the three adoption buckets using database records, integration logs, contracts, and tickets
- Interview 10–15 former customers, asking about behavior rather than reasons

## Week 6: decide

**7. Present results against the predictions, and follow the decision rules.** Then commit resources for the next two quarters and revisit using the forward-looking data.

## My expectation

If I had to bet, I'd bet the diagnosis points mostly to **implementation and value realization**, with product gaps as a real but secondary factor. Three reasons:

- Claims systems are normally very sticky. Churn doubling suggests many customers never got embedded enough to be sticky.
- Customers commonly cite missing features as a polite exit reason, even when the real problem was never getting value.
- The AI and analytics features the Product VP wants depend on clean, integrated data, which requires a complete implementation. Better features won't help customers who aren't fully live.

If that's what the data shows, the plan is to shorten implementations, define "fully live" and hold the team to it, and track time to value as a core metric. Product's roadmap should focus on work that speeds onboarding and adoption.

But that's a bet, not a conclusion, and a cheap six-week test is far better than a two-quarter mistake in either direction. If the data shows embedded customers leaving for better features and you're losing new deals on those grounds, accelerate the roadmap without hesitation.

## If you only remember three things

1. **Save the renewals in front of you now.** That doesn't depend on the diagnosis.
2. **Get both VPs to agree on what would prove them wrong before the data comes back.**
3. **Let a six-week analysis, not the louder argument, decide where the next two quarters of investment go.**

## Outcome summary (sent to Jev)

The assistant recommends acting immediately on moves that make sense under either explanation, then settling the Product-versus-Services question with a short, pre-agreed diagnosis rather than internal argument. This week, the company should protect renewals due in the next two quarters by ranking accounts on available risk signals (claims volume, live integrations, ticket history, CSM judgment) and assigning its strongest people to the top 10–15 revenue accounts. It should also begin instrumenting adoption for current customers, and freeze major roadmap or services commitments for about six weeks.

In weeks one and two, a pre-registration session should have both VPs write down specific predictions, the results that would prove them wrong, shared definitions, and decision rules, including one for mixed results such as weighting investment by share of churned revenue. A sponsor signs off, and a neutral analyst from finance, RevOps, or strategy owns the work. In weeks two through six, the analyst rules out acquisitions, suite displacement, and customer-mix shifts. Next come tests that don't need usage data: churn timing, cohort curves, implementation duration, destinations, and new-logo win rates. Accounts are then sorted into three adoption buckets using database, integration, contract, and ticket records, and 10–15 former customers are interviewed about behavior rather than stated reasons. In week six, results are presented against the predictions and the rules are followed.

The assistant's bet is that implementation and value realization is the main driver. Its reasons are that claims systems are normally sticky, that "missing features" is a polite exit excuse, and that AI and analytics require fully implemented, clean data. It stresses that this is a bet, not a conclusion. If embedded customers are leaving for competitors' features and new deals are being lost on those grounds, the company should accelerate the roadmap.
