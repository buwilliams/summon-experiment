# churn-cause/critical-rationalism/testC

Model: claude-opus-5-5 · 2026-09-24T15:29:56.799481+00:00

## Turn 1

**User:** Use the method of conjectures and refutations (critical rationalism) to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Which VP Is Right About Churn? Testing Both Theories

The short answer is that neither belief is established yet, and you can find out cheaply, mostly from data you already have. In critical rationalism you don't choose the theory that sounds most convincing or has the most senior advocate. You treat each one as a bold guess, work out what it forbids, and look for evidence that would kill it. The theory that survives serious attempts at refutation is the one you act on, provisionally.

## Step 1: Sharpen the conjectures so they can fail

As currently stated, both beliefs are too flexible. "Customers never reach full value" and "competitors have better features" can each explain almost any churned account after the fact. A theory that explains everything risks nothing. So restate each as a claim with consequences.

**H1, the product-gap conjecture.** Customers who successfully adopted the product are leaving for competitors because those competitors offer analytics or AI capabilities we lack.

**H2, the implementation and service conjecture.** Customers are leaving because they never reach full value: long implementations, low adoption, and poor support experiences. Better features wouldn't fix this, because they'd go unadopted too.

Also notice something both VPs need to explain: **churn doubled.** A theory must point to something that *changed* about 18 to 30 months ago. If implementations have always been long, H2 can't explain a doubling unless they got worse or the customer mix changed. If competitors have always had better analytics, H1 can't explain it unless something new launched.

## Step 2: Derive predictions that discriminate

The useful tests are the ones where the two theories predict *different* things.

| Observable | H1 (product gap) predicts | H2 (implementation/service) predicts |
|---|---|---|
| Adoption and usage of churned accounts before leaving | Healthy, even heavy use | Low adoption; features never activated |
| Tenure at churn | Spread across tenures, including mature accounts | Concentrated at first or second renewal |
| Implementation duration vs. churn | No meaningful correlation | Strong correlation; long or overrun implementations churn more |
| Where churned customers went | Competitors with the touted analytics/AI | Anywhere, including simpler tools or competitors *without* those features |
| Pre-churn signals | Feature requests, RFPs mentioning AI/analytics | Escalations, low CSAT, ticket backlogs, missed go-lives |
| New-business win rate against the same competitors | Also falling, citing the same features | Roughly stable |
| Timing of the rise | Follows competitor feature launches | Follows longer implementations, support staffing changes, or a new product version |
| Well-implemented, high-adoption accounts | Churning at elevated rates | Retaining at historical rates |

Two tests are especially sharp:

- **The crucial test.** Segment churn by implementation and adoption health.
  - If your healthiest, best-implemented accounts are churning at roughly double their old rate, H2 is in serious trouble.
  - If those accounts retain as before and churn is concentrated in troubled implementations, H1 is in serious trouble.
- **The "phantom gap" test.** List the specific features churned customers said they wanted. Check how many you actually have but they never turned on. A lot of overlap means the perceived product gap is really an adoption failure, which is a point for H2. No overlap, with the requested features genuinely absent, is a point for H1.

## Step 3: Don't limit yourself to two conjectures

Two VPs each proposing the fix that expands their own function is a warning sign that the option set is too narrow. Rival conjectures worth testing, each with a quick refutation check:

- **H3, carrier consolidation.** Regional carriers are merging, and acquired carriers migrate to the parent's system. *Check:* how many churned accounts were acquired?
- **H4, core-suite bundling.** Carriers are replatforming onto core suites (Guidewire, Duck Creek, etc.) that bundle claims management. *Check:* the destination of churned accounts.
- **H5, customer-fit drift.** About 2 to 3 years ago, Sales began selling to larger, more complex, or otherwise poorer-fit carriers. Both long implementations *and* feature complaints would then be symptoms, not causes. *Check:* churn by signing cohort, segment, and rep.
- **H6, pricing.** Renewal price increases or packaging changes. *Check:* churn vs. uplift at renewal.
- **H7, champion loss.** Your sponsor left, and the successor brought their preferred vendor. *Check:* contact turnover before churn.
- **H8, measurement artifact or noise.**
  - Did the churn definition change?
  - With a modest customer count, going from, say, 6 to 12 lost logos may be within noise.
  - Is the doubling in logos, revenue, or both?

  Rule this out first. It's the cheapest check.

H5 deserves special attention because it would make both VPs partly right and both proposed fixes partly wrong.

## Step 4: Guard against weak evidence

- **Exit interviews are weak.** "You lacked AI features" is a polite, face-saving reason to give a vendor. "Your implementation was a mess and our team gave up" is awkward to say. Weight *behavioral* evidence much more heavily: usage logs, ticket history, and where customers actually went.
- **Use a neutral interviewer.** If you interview churned customers, have a third party or someone outside CS, Product, and Services do it.
- **Win/loss data is independent corroboration.** Sales win/loss comes from a different team and a different moment, so check whether it tells the same story.

## Step 5: Make both VPs commit in advance

This is the most Popperian move available to you, and it also defuses the politics. Before anyone looks at the data, have each VP write down: *"If we find X, I will accept my theory is wrong or secondary."*

For example:
- **VP of Product:** "If high-adoption accounts retain at historical rates, product gaps aren't the main driver."
- **VP of Services:** "If implementation duration doesn't predict churn, onboarding isn't the main driver."

Without this, both will reinterpret whatever comes back as confirmation.

## What to do

**Weeks 1–3: Refutation sprint on existing data.** Assign an analyst who reports to neither VP.
1. Validate the churn number: definition, logos vs. revenue, and whether the rise exceeds noise (H8).
2. For every churned account in the last 24 months, record:
   - tenure
   - implementation duration vs. plan
   - adoption and usage trend
   - support and CSAT history
   - pre-churn feature requests
   - destination
   - acquisition status
   - price change at renewal
   - champion turnover
   - signing cohort and segment
3. Run the crucial test (healthy vs. troubled accounts) and the phantom-gap test.
4. Pull win/loss data for the same period.

**Week 4: Decide on the surviving conjecture.** Most likely it will be one dominant cause plus a secondary one, and the split tells you how to allocate effort. Possible outcomes:
- **H2 survives and H1 is refuted:** Pause the roadmap acceleration. Fix time-to-value first. New features shipped into failed implementations will also go unadopted.
- **H1 survives and H2 is refuted:** Accelerate the specific capabilities that show up in losses, not "AI" generically. Validate them with the customers who are asking.
- **H5 or H3/H4 survives:** The fix is in Sales targeting, pricing, or market strategy, and neither VP's plan addresses it.

**Ongoing: Keep testing forward, because backward-looking data can mislead.**
- **Onboarding test:** Take at-risk accounts approaching renewal and randomly give half an intensive adoption and service rescue. Compare renewals.
- **Product test:** Offer a beta of the most-requested analytics capability to a subset of accounts. Measure whether it changes renewal intent and usage.
- **Treat the choice as provisional.** Whichever conjecture you act on, define up front the metric that would tell you within 2 to 3 quarters that you were wrong.

**Until the data is in:** Make no large, irreversible bets in either direction. Do protect the renewals coming due in the next two quarters with account-level saves, since that helps regardless of which theory survives.

## My tentative read, held loosely

The timing slightly favors H1, since the recent AI wave roughly matches your 18-month window. Base rates slightly favor H2: regional carriers tend to be conservative adopters, and failed time-to-value is a very common churn driver in complex enterprise software.

My actual bet is that H5 or the phantom-gap pattern will explain a lot. That would mean customers who were poorly onboarded perceive a feature gap because they never saw what the product already does.

But that is a conjecture too. Three weeks of data can refute it, and you should let it.

## Turn 2

**User:** We pulled the data, and most churned accounts signed in the last two years had long implementations, but several had high adoption and still left for a competitor with AI features. Still using conjectures and refutations, how should we interpret that?

**Assistant:**

# Interpreting a Mixed Result

This is a useful result. It doesn't crown a winner, but it kills the strong versions of both theories and narrows what's left to test. Here's how to read it.

## 1. What's been refuted

**H2 as the sole explanation is refuted.** The claim "customers leave because they never reach full value" is contradicted by high-adoption accounts that reached value and left anyway. This is Popper's asymmetry: no number of long-implementation churners can prove a universal claim, but a few solid counterexamples can refute it. Before accepting the refutation, confirm those accounts were genuinely high-adoption. They should show broad, sustained usage of core workflows, not just logins.

**H1 as the main explanation is under serious pressure.** H1 predicted that churned accounts would have healthy usage before leaving. Most didn't. A customer who never got the product working isn't primarily comparing your analytics roadmap to a competitor's. They're leaving a failed implementation.

So the pure versions of both VPs' beliefs are out. That's progress, but be careful about what comes next.

## 2. What hasn't been established yet

The finding that "most churned accounts had long implementations" is weaker evidence for H2 than it looks, for three reasons.

**The base-rate problem.** What share of *retained* accounts signed in the same period also had long implementations? If 80% of all recent signers had long implementations, then 80% of churners having them tells you nothing. You need the churn rate *conditional on* implementation length. Compare long vs. on-time implementations within the same signing cohort.

**The confounding problem (H5 again).** Long implementations may not *cause* churn. Complex or poor-fit customers may both take longer to implement and churn more for other reasons. Check whether implementation length still predicts churn after controlling for segment, size, integration complexity, and signing rep.

**The destination question.** Where did the *low-adoption* churners go?
- If many also went to the AI competitor, the picture changes. That competitor may be winning on faster implementation and easier time-to-value, with AI as the headline.
- Find out what that competitor actually pitches and how long its implementations take.
- If its advantage is really speed, part of what looks like "product gap" churn is actually H2 churn wearing an AI label.

## 3. Beware the tempting rescue

The obvious move now is a combined theory: implementation failures drive churn in recent cohorts, and AI gaps drive churn among mature accounts. That may well be true. But Popper warns specifically against this pattern. When evidence contradicts a theory, it's easy to add a clause that absorbs the counterexample. "Both matter" can fit any data, which means it risks nothing and guides nothing.

To make the combined theory a genuine conjecture rather than a truce, it has to be bold again. That means quantified, with predictions that could fail:

- **Share of churn.** State what fraction of churned ARR falls under each mechanism. Weight by revenue, not logos. High-adoption accounts are often larger and more strategic, so "several" might be a big share of lost revenue.
- **Contribution to the doubling.** Estimate how much of the *increase* each mechanism explains. The question was always why churn doubled, not just why customers leave.
  - Is the rise mostly recent-cohort implementation failures? That points to something that changed in what you sold or how you implement about two years ago.
  - Or is it the AI-driven losses among mature accounts? That points to a competitive shift.
- **Trend.** Are the high-adoption AI losses clustered in the last two quarters? If so, H1 may be minor today but growing. It could be a leading indicator that AI is becoming table stakes, and that would matter a lot for planning.
- **Forward prediction.** Using each mechanism's warning signs, predict which of the next 10 to 20 renewals are at risk. If the predictions fail, the theory is wrong.

## 4. Examine the "several" closely

A handful of cases can't carry statistical weight. They can carry a lot of *diagnostic* weight, so run a detailed case study on each:

- **Specific capability.** Did they ask for AI or analytics beforehand, in tickets, QBRs, or RFPs? Which specific capability? "AI features" is too vague to act on.
- **Existing features.** Did you already have an equivalent they didn't know about? This is the phantom-gap test applied to your strongest counterexamples.
- **The actual decision.**
  - Was the decisive factor the feature itself, or a new executive, a pricing offer, or a competitor sales push?
  - Did the competitor's AI actually exist and work, or was it a roadmap promise? If you win back or keep in touch with any of these accounts, see whether the promise holds up. That's a test of H1 too.

## 5. What to do now, provisionally

Act on what has survived, in proportion to its weight, and make each action able to show you're wrong:

1. **Fix time-to-value for new and recent cohorts.** Pending the base-rate check, this looks like the largest mechanism by count.
   - Set a target, such as cutting median implementation time by X% within two quarters.
   - Define in advance what result would show it didn't matter. For example, if on-time implementations churn at the same rate as long ones, the fix won't help retention.
2. **Mount a targeted AI response, not an across-the-board roadmap acceleration.** Build or partner for the *specific* capabilities the high-adoption churners cited. Validate demand with current healthy accounts before committing heavily.
3. **Defend your healthy accounts now.** H1's risk group is identifiable: high usage plus competitor contact, or AI-related requests. Put these accounts on proactive executive and roadmap engagement. They're your most valuable customers and, by this evidence, not immune.
4. **Investigate what changed about two years ago.** Look at sales targeting, implementation staffing, and product version. If long implementations are concentrated in recent signers, something shifted, and neither VP's plan addresses it yet.
5. **Rerun the analysis in a quarter** with conditional churn rates and revenue weighting. Let the relative size of the two mechanisms drive budget allocation, and let each VP's pre-committed refutation criteria do their job.

**Bottom line:** The evidence so far says the VP of Services is closer to right about *most* of your churn. The VP of Product has identified a real mechanism that may be small now and growing. Check the base rates before you believe the first point too firmly, and watch the trend before you dismiss the second.

## Turn 3

**User:** We ran the base-rate check, and retained accounts from the same cohorts had implementations nearly as long as the churned ones. Sticking with conjectures and refutations, what does that do to the implementation theory?

**Assistant:**

# What the Base-Rate Result Does to the Implementation Theory

It refutes the implementation theory in the form you measured it. If churned and retained accounts from the same cohorts had nearly the same implementation lengths, then implementation length can't be what separates customers who leave from customers who stay. A condition shared by almost everyone can't explain why only some leave.

That also undercuts my own earlier read that the VP of Services was closer to right about most of the churn. That conclusion rested on exactly the finding that just failed the base-rate check. The honest update is that the strongest evidence for H2 has collapsed.

Before you act on this, there are two moves to watch: one that saves H2 illegitimately, and one that condemns it too quickly.

## 1. The rescue: legitimate or ad hoc?

The VP of Services will likely say that duration was never the point. The point was whether customers reached value, and a long implementation that ends in real adoption is fine.

Popper's test for whether that retreat is acceptable:

- **It's ad hoc if** the new version is invented after the fact only to escape the refutation, and it predicts nothing new.
- **It's legitimate if** the new version was part of the theory's original content, and it makes a fresh prediction that could fail.

This retreat plausibly passes the first condition. The original claim was that customers "never get to full value," and duration was only a proxy for that. But it earns its place only by facing a new test. Within the same cohorts, adoption or value-realization must clearly separate churned accounts from retained ones.

To keep the test honest:

- **Define "reached value" before looking at the data.** Examples: percentage of claims processed in the system, active adjuster users, or key workflows live by month X. If you search many metrics until one separates the groups, you'll find a spurious winner.
- **Accept the outcome either way.** If a pre-specified adoption metric doesn't discriminate, H2 is refuted in its core form, not just its proxy form.

You already have one warning sign. Several high-adoption accounts left, so adoption is at best a partial predictor.

## 2. The surviving variant: a background condition

A weaker version of H2 could still be true. Long implementations may leave customers vulnerable without deciding who leaves. Some other trigger, such as a competitor pitch or a new executive, does the deciding.

That's a coherent idea, but in its current form it's nearly unfalsifiable, and it has to earn its keep with a testable prediction. For example:

- Accounts with short implementations should resist the same trigger better. When pitched by the AI competitor, they should churn less than long-implementation accounts facing the same pitch.
- If you can't find short-implementation accounts to compare against, perhaps because older cohorts implemented faster, the variant can't be tested yet. Say so explicitly rather than keep it as a comfortable default.

## 3. The doubling problem gets worse for H2

H2 always had to explain why churn doubled, not just why customers leave. The base-rate result sharpens that problem.

- **If implementation length within recent cohorts doesn't predict churn,** H2 can explain the rise only if recent cohorts implemented much more slowly than older, lower-churn cohorts, and that difference affected everyone.
- **Test that directly:** compare implementation length and adoption across cohorts, before and after the churn rise.
- **If implementation times have been long for years,** H2 can't explain the doubling at all.

## 4. Don't declare H1 the winner by elimination

The tempting inference is that implementation has failed, so it must be the product gap. That is exactly the move critical rationalism rules out.

Refuting one rival doesn't corroborate another. H1 hasn't yet passed a severe test of its own, and you still have rivals in play:

- **H3:** carrier consolidation, where acquired carriers migrate to the parent's system
- **H4:** core-suite bundling
- **H5:** customer-fit drift
- **H6:** pricing changes at renewal
- **H7:** champion turnover

H1 is now the leading candidate among those explicitly tested, but it's untested in its own right. Give it tests it could fail:

- **Competitor exposure should discriminate.** Within the same cohorts, churned accounts should show more contact with the AI competitor than retained accounts. That contact would show up as RFPs, sales intel, or mentions in QBRs.
- **Retained accounts that were pitched should be explicable.** If many retained accounts were pitched by the same competitor and stayed, find out why. If their reasons have nothing to do with AI parity, H1 weakens.
- **Specific capabilities should recur.** Churned accounts should cite the same concrete AI or analytics capabilities across cases, not a vague sense that the competitor is more modern. A vague, shifting grievance is weak support for a product-gap theory.
- **The timing should fit.** The churn rise should follow the competitor's launches.
- **Win/loss data should agree.** New-business losses against that competitor should show the same pattern.

## 5. The next analysis: find what does discriminate

You've learned that the discriminating variable isn't implementation length. So compare churned and retained accounts within the same cohorts on everything else you hypothesized:

| Candidate variable | Theory it tests |
|---|---|
| Pre-specified adoption / time-to-value metric | H2 (core form) |
| Competitor contact or evaluation | H1 |
| Acquired or merging carrier | H3 |
| Replatforming onto a core suite | H4 |
| Segment, size, complexity, signing rep | H5 |
| Renewal price change | H6 |
| Executive sponsor turnover | H7 |

Two cautions:

- **Watch your sample size.** With a modest customer count, a few accounts can create or erase an apparent pattern. "Nearly as long" might hide a real but small difference, or it might be noise. Report the actual numbers.
- **Look for separation, not just differences in averages.** The variable you want largely sorts leavers from stayers.

## 6. What changes in practice

1. **Stop justifying implementation investment as the churn fix.** Faster implementations may still be worth pursuing for customer satisfaction, services margin, or sales cycles. But the evidence no longer supports them as a retention lever, and budget requested on that basis should be reconsidered.
2. **Don't redirect everything into AI features yet.** Hold large roadmap commitments until H1 passes the tests above. These can be run on data you mostly have, in a few weeks.
3. **Keep defending high-adoption accounts at risk.** That mechanism is still the one directly observed to cause churn, and those accounts are valuable.
4. **Hold both VPs to their pre-committed refutation criteria.** The Services VP's criterion has now been triggered in its duration form. The fair response is for them to name, in advance, what adoption result would refute the core form of their theory.

**Bottom line:** The implementation theory has lost its main evidence. It survives only as a narrower claim about adoption, which faces an immediate test, and possibly as a background-condition idea that is currently untestable. The product-gap theory is the strongest remaining candidate, but only by default. The next step is to find out what actually separates the customers who left from the ones who stayed, rather than assuming it's whatever wasn't refuted.

## Turn 4

**User:** We checked competitor contact, and a lot of retained accounts were also pitched by the AI competitor and stayed. Still using conjectures and refutations, what does that mean for the product-gap theory?

**Assistant:**

# What Competitor Contact Tells You About the Product-Gap Theory

It does to H1 what the last result did to H2. It refutes the theory in the form you measured, while leaving a narrower version to test. If many retained accounts were pitched by the AI competitor and stayed, then being pitched isn't what separates leavers from stayers. The AI offering alone is not enough to pull customers away.

That's now the second leading theory to fail as a general explanation. Before drawing conclusions, check the result properly. Then look at what the pattern of refutations is telling you.

## 1. Make sure the refutation is real

"A lot of retained accounts were pitched" is the mirror image of the base-rate problem from last round. It isn't yet the same as "exposure doesn't matter." Two checks will tell you:

- **Compare rates, not counts.** Calculate churn among pitched accounts versus unpitched accounts in the same cohorts. If pitched accounts churn at, say, three times the rate of unpitched ones, H1 is alive as a real risk factor, even though many pitched accounts stayed. If the rates are similar, exposure genuinely doesn't discriminate.
- **Control for renewal timing.** An account pitched mid-contract couldn't leave even if it wanted to. Restrict the comparison to accounts pitched within, say, 12 months of a renewal decision. Some "pitched and stayed" accounts may simply be "pitched and not yet able to leave," and they may still churn at their next renewal.

If both checks come back flat, H1 as a general mechanism is refuted.

## 2. What survives of H1

Some facts haven't gone away. Several high-adoption accounts left for this competitor. Any theory you end up with still has to explain them.

The legitimate narrower version of H1 is that the AI gap is decisive for a specific kind of customer, and that the kind can be identified in advance. As before, that retreat is acceptable only if it takes on new risk:

- **Name the subset before you look.** Candidates include carriers with a specific use case such as fraud detection or subrogation, carriers above a certain claims volume, or carriers whose leadership has an AI mandate.
- **Predict that pitched accounts in that subset churn much more than pitched accounts outside it.** If you can't define the subset in advance, "it matters for some customers" is unfalsifiable. Treat it as a hunch, not a theory.

## 3. Look at the pattern of refutations

Two single-variable theories have now failed the same way:

| Theory | Variable | Result |
|---|---|---|
| H2 | Implementation length | Common among retained accounts too |
| H1 | Competitor exposure | Common among retained accounts too |

Both failed theories were stories about your company: your implementations and your features. Both proposed a condition that turned out to apply broadly, to stayers as well as leavers. That points toward a different kind of conjecture.

**H9: something changes on the customer's side, and that makes them act on conditions that were already there.** Long implementations and competitor pitches are background conditions that almost everyone experiences. What differs is whether something inside the carrier turns that background into a decision to leave. Candidate triggers:

- **Leadership change (H7):** a new CIO or head of claims arrives with no loyalty to the incumbent vendor.
- **Strategic mandate:** the board or CEO demands an AI or modernization strategy. Switching vendors becomes a visible way to show progress, whatever your product does.
- **Structural change (H3, H4):** an acquisition, merger, or core-system replatforming forces a vendor review.
- **Budget pressure (H6):** a renewal price increase opens the question of alternatives.

H9 is falsifiable, which is what makes it worth taking seriously:

- **It predicts** that churned accounts will show one of these triggers before leaving much more often than retained accounts.
- **It is refuted if** trigger rates are similar between leavers and stayers.

Define each trigger before collecting the data, to avoid fitting the categories to the results.

## 4. The sharpest comparison available: pitched-left vs. pitched-stayed

You now have something like a natural experiment. Many accounts received the same stimulus, the competitor's pitch, and responded differently. Comparing accounts that were pitched and left with accounts that were pitched and stayed holds exposure constant and isolates what made the difference.

Compare the two groups on:

- **Pre-specified adoption metric:** tests the core form of H2.
- **Membership in the pre-defined AI-need subset:** tests the narrow form of H1.
- **Leadership change, strategic mandates, acquisition, replatforming, price change:** tests H9 and H3 through H7.
- **Segment, size, signing rep:** tests H5.

Also interview some of the accounts that stayed after being pitched. Asking "you evaluated them; why did you stay?" is often more informative than exit interviews. Stayers have less reason to be diplomatic, and their answers tell you what your actual retention advantage is. Be careful, though. If stayers consistently cite relationships or switching costs rather than product value, those are advantages that erode over time, not reasons to feel safe.

## 5. The doubling is still unexplained

Neither theory has yet explained why churn doubled. The remaining candidates must pass this test too.

- **H9 explains it** only if triggers became more frequent in the last 18 months. That's plausible: 2023–2024 saw a lot of executive pressure to "do something about AI," along with M&A among regional carriers. But it needs to be checked, not assumed.
- **Revisit H8 (noise).** If you have a modest number of logos and no variable cleanly separates leavers from stayers, run the numbers again and ask whether the doubling is outside what random variation would produce. Rule out this dull explanation before building strategy around an exciting one.

## 6. What you actually know now

Refutations are knowledge, even when nothing has been confirmed. Here is where things stand:

| Claim | Status |
|---|---|
| Implementation length explains churn | Refuted |
| AI competitor exposure explains churn | Refuted as a general explanation, pending rate and timing checks |
| Some high-adoption customers left for AI features | Established fact; any theory must account for it |
| Adoption (core H2) discriminates churn | Untested; pre-specify the metric |
| AI gap decisive for a definable subset (narrow H1) | Untested; define the subset first |
| Customer-side triggers (H9, H3–H7) | Untested; leading new candidate |
| Doubling exceeds noise (H8) | Unchecked; do this first |

## 7. What to do

1. **Put both big bets on hold as churn fixes.** Neither roadmap acceleration nor an onboarding overhaul has survived testing as the answer to churn. Each may be worth doing for other reasons, but neither should be funded on the claim that it will fix churn.
2. **Run the pitched-left versus pitched-stayed comparison**, with trigger variables defined in advance. This is the single most informative analysis available to you.
3. **Interview accounts that were pitched and stayed.** Their answers will tell you what is actually holding customers.
4. **Build trigger monitoring into customer success now.** It's cheap and useful under almost any surviving theory. Flag executive turnover, M&A announcements, AI mandates, and upcoming price increases at your accounts, and engage early when one appears. That way you're acting on the best current conjecture while testing it.
5. **Keep defending high-adoption accounts showing AI interest.** That mechanism is real, even if it isn't the main one.
6. **Report the scorecard to both VPs.** Each should see that their theory failed a test they could accept in advance as fair. Neither lost to the other; the data refuted both. That makes the next round of conjectures easier to test honestly.

**Bottom line:** The evidence no longer supports either VP's theory as the main explanation. Both identified real conditions, but conditions that stayers experience too. The most promising remaining idea is that something happening inside the customer decides whether those conditions lead to churn. You can test that directly by comparing accounts that faced the same competitor pitch and made opposite decisions.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

You don't yet know the cause, and you don't need to know it to act well. Critical rationalism's rule for acting under uncertainty is:

- act on what has survived testing;
- prefer actions that pay off under every theory still standing;
- keep big bets small and reversible until a theory earns them;
- design each action so it also tests something.

Here's what that means concretely.

## 1. Stop funding either VP's program as the churn fix

Neither the roadmap acceleration nor the onboarding overhaul survived testing as the explanation for churn.

- **Judge them on their own merits.** Faster implementations may still improve margins and sales cycles. AI features may still matter for winning new business. Evaluate them on those grounds instead.
- **Don't let either claim the retention budget** until the evidence supports it.

## 2. Settle the open questions in the next 3–4 weeks

Assign one analyst who reports to neither VP.

1. **Rule out noise first.** Test whether the doubling exceeds normal variation given your number of accounts. Check whether it shows up in revenue as well as logos. If it's within noise, most of this effort should stop.
2. **Tighten the competitor result.** Compare churn rates for pitched vs. unpitched accounts, counting only accounts pitched within 12 months of a renewal.
3. **Run the key comparison: pitched and left vs. pitched and stayed.** Compare the two groups on variables defined before you look at the data:
   - a specific adoption metric;
   - membership in a named "AI-need" segment;
   - executive turnover;
   - AI or modernization mandates;
   - M&A or replatforming;
   - renewal price changes;
   - segment and signing rep.
4. **Interview 8–10 accounts that were pitched and stayed.** Ask them why they stayed.

## 3. Start these now, because they help under every surviving theory

- **Trigger monitoring.** Customer success should flag executive turnover, M&A news, AI mandates, and upcoming price increases at every account, then engage early when one appears. This is also a live test of the customer-side-trigger theory, since you'll see whether flagged accounts churn more.
- **Save plays for renewals in the next two quarters.** Hold executive-level conversations with every account up for renewal, not just the ones that look at risk. Some of the high-adoption customers who left looked safe.
- **Protect high-adoption accounts showing AI interest.** This mechanism is confirmed. Offer roadmap briefings, early access, and direct contact with the product team.
- **A modest AI story for customers.** Many carriers are being asked by their boards what their AI strategy is. A credible answer from you costs little, whether or not missing features turn out to be the cause. That answer can include:
  - a clear roadmap;
  - partnerships;
  - AI capabilities you already have but customers don't know about.

## 4. Decide in advance what each finding will trigger

Agree on these rules with both VPs before the results arrive. The whole leadership team should pre-commit.

| If the analysis shows... | Then... |
|---|---|
| Doubling is within noise | Stop the investigation, keep monitoring, and revisit in two quarters |
| Customer-side triggers separate leavers from stayers | Make trigger response the core retention strategy. Fund executive relationship programs and early-warning playbooks. |
| A defined AI-need segment churns much more when pitched | Build the specific capabilities that segment needs, validated with current customers, not a general roadmap acceleration |
| A pre-specified adoption metric separates leavers from stayers | Fund a value-realization program aimed at low-adoption accounts, which is not the same as shortening implementations |
| Nothing separates them | Treat churn as having many causes. Build an account-level risk score from all the signals and manage retention account by account. |

Each rule should come with its own failure condition. For example: if trigger response doesn't reduce churn among flagged accounts within two to three quarters, the trigger theory is wrong.

## 5. Change how the organization handles this

- **Keep ownership neutral.** Churn diagnosis should sit with you or an analyst who isn't tied to either program.
- **Hold a monthly scorecard review.** List each theory as tested, refuted, or surviving, and assign the next test for each.
- **Make pre-commitment normal.** Anyone proposing a churn explanation should state up front what evidence would change their mind.

## What to tell your executives

"We tested both leading explanations for the churn increase, and neither holds up as the main cause. Long implementations and competitor pitches are common among customers who stayed, too. We're now testing whether changes inside the customer, such as new leadership, AI mandates, or M&A, determine who leaves. We'll have an answer in about a month, with decision rules already agreed. In the meantime, we're protecting upcoming renewals and our best accounts, and we're holding off on large investments justified as churn fixes until the evidence supports them."

This is a strong position to present. You've eliminated two expensive wrong answers, you have a sharp test for the next candidate, and you're acting sensibly while it runs.

## Outcome summary (sent to Jev)

The assistant recommends acting without yet knowing the cause of churn. It follows four rules: act on what has survived testing, prefer actions that pay off under every theory still standing, keep big bets small and reversible, and design each action so it also tests something.

First, stop funding either the roadmap acceleration or the onboarding overhaul as the churn fix. Both failed as explanations: long implementations and AI-competitor pitches were just as common among customers who stayed. Each program should be judged on other merits, such as margins, sales cycles, and new business.

Second, over three to four weeks, an analyst reporting to neither VP should:
- check whether the doubling exceeds normal variation and shows up in revenue as well as logos;
- compare churn rates for pitched and unpitched accounts, limited to accounts pitched within 12 months of renewal;
- compare accounts that were pitched and left with those pitched and stayed, on variables defined in advance, including adoption, a named AI-need segment, executive turnover, AI mandates, M&A or replatforming, price changes, segment, and signing rep;
- interview 8–10 accounts that were pitched and stayed.

Third, start now on actions that help under any surviving theory:
- monitor customer-side triggers and engage early when one appears;
- hold executive conversations with every account renewing in the next two quarters;
- protect high-adoption accounts showing AI interest, a confirmed mechanism;
- offer customers a modest, credible AI story.

Fourth, agree in advance with both VPs which finding triggers which program. Each rule needs its own failure condition, such as trigger response not reducing churn within two to three quarters.

Finally, keep churn diagnosis under neutral ownership, review a monthly scorecard of theories, and make pre-committing to refutation criteria the norm.
