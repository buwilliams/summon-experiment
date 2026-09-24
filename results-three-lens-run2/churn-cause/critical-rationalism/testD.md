# churn-cause/critical-rationalism/testD

Model: claude-opus-5-5 · 2026-09-24T15:29:58.208294+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

**Assistant:**

# Which Churn Explanation Survives Criticism?

**Short answer:** Neither belief survives in its current form, because as usually stated, neither can lose. Both can be sharpened into claims that *can* lose, and you can probably run the decisive tests in two to three weeks using data you already have. There are also at least two third explanations that fit "churn doubled in 18 months" as well as either VP's story, and they deserve a place in the test.

---

## Step 0: Check the fact before explaining it

Three quick checks, because each has sunk real analyses:

- **Size of the numbers.** Regional carriers are a small market. Going from 5 lost logos to 10 is "doubling" but may be noise or one bad cohort. Know the counts, not just the rate.
- **Logo vs. revenue churn.** If revenue churn doubled because of two large accounts, you need two case studies, not a strategy.
- **Voluntary vs. involuntary churn.** Separate customers who chose to leave from those who were acquired, merged, or went insolvent. Regional P&C has been consolidating, and a carrier absorbed by a larger one isn't rejecting you.

---

## Step 1: State each conjecture so it can be wrong

**Product-gap conjecture (VP Product)**
- **Claim:** Customers who got full value from our product still leave, because a competitor offers capabilities (analytics, AI triage, fraud scoring, etc.) that we lack and that matter to their buying decision.
- **Mechanism:** At renewal, carriers compare offerings, and ours loses on capability.
- **Implication:** Fixing onboarding won't save them. The product itself is losing the comparison.

**Service-experience conjecture (VP Services)**
- **Claim:** Customers leave because they never reached full value: implementations ran long, adoption stayed shallow, and support was painful. The product would have been sufficient if they'd gotten there.
- **Mechanism:** At renewal, the customer compares cost to *realized* value, and realized value is low.
- **Implication:** Customers who got fully implemented and adopted should mostly stay, despite competitor features.

Stated this way, the two make opposite predictions about one group: **well-implemented, heavily-adopted customers.** That group is where most of the discriminating power lives.

---

## Step 2: Discriminating predictions

| Observation | If product gaps | If service experience |
|---|---|---|
| Churn among fully-live, high-adoption customers | Elevated, similar to others | Low. Churn concentrated in slow or shallow implementations |
| Churn vs. time-to-go-live | Weak relationship | Strong relationship. Long implementations churn more |
| Where churned customers went | Concentrated among competitors with the cited features | Anywhere, including cheaper or simpler tools, or even competitors with *fewer* features but easier deployment |
| **New-logo competitive win rate** | Dropped too, because prospects see the gap before any implementation | Roughly stable, because the problem is post-sale |
| Timing of the churn rise | Follows competitor launches or market shifts in AI | Follows internal change, e.g. an implementation backlog, services reorg, or rising ticket volume/severity |
| What the decision-maker says drove the choice (via independent interviews) | Specific capabilities evaluated in an RFP | "We never got it working" or "we weren't using most of it" |
| Adoption of *existing* analytics features among churners | Adopted, but found insufficient | Never adopted in the first place |

The **new-logo win rate** test is especially clean and underused. Service pain can't hurt a prospect who hasn't been implemented yet, except through reputation. If your competitive win rate is flat while retention collapses, the product-gap story weakens considerably. If both fell together, it strengthens.

---

## Step 3: Where each explanation is easy to vary

**Product gaps.** "Better analytics and AI features" is elastic. Any lost customer lacked *some* feature, and "AI" can mean anything a competitor demoed. If a churner cites price, it becomes "we didn't justify the price with features." If they cite implementation, it becomes "the product should be easier to deploy." The explanation absorbs everything.
- *To harden it:* Name the specific capabilities, name the competitors, and predict that churners disproportionately moved to those competitors after evaluating those capabilities.

**Service experience.** "Never got to full value" is equally elastic. Every churned customer, by definition, didn't find enough value to stay. If a well-adopted customer leaves, it becomes "they adopted, but not *deeply* enough."
- *To harden it:* Define "full value" in advance with a measurable adoption threshold (modules live, active adjuster users, claims volume processed). Predict that customers above the threshold churn at a materially lower rate. Commit to the threshold before looking at outcomes.

**A confound both sides will exploit:** Low adoption could be *caused* by product gaps, with customers not using the product because it's weak. So "churners had low adoption" doesn't settle anything by itself. To break the confound, look at adoption of core workflows that competitors also have, such as FNOL, reserving, and payments. Shallow adoption of commodity features points to implementation. Deep adoption of core workflows followed by departure for analytics points to product.

**Exit-reason data is weak evidence for both sides.** "Missing features" is the polite, blame-free reason customers give vendors. Customers also tend to tell each function what that function asks about. Interviews should be run by someone neutral, and should reconstruct the decision process (who decided, what alternatives were evaluated, when the decision was really made), not just collect the stated reason.

**Motive caveat:** Each hypothesis prescribes more investment in its proponent's organization. That doesn't make either one false, but it's a reason to have someone outside both teams pre-register the predictions and run the analysis.

---

## Step 4: Third explanations that may fit better

Each of these explains an 18-month doubling without requiring either VP to be right.

**1. Platform consolidation.** Regional carriers are replacing core policy/billing systems, and suite vendors (Guidewire, Duck Creek, Majesco, etc.) bundle claims. The claims decision gets made as part of the core replacement.
- *Predicts:* Churn clusters around core-system replacement projects. Churned customers go to suite vendors. The decision is made by the CIO, not claims leadership. Neither better onboarding nor better AI would have saved them.
- *Implication:* Integration and partnership strategy, or repositioning, not roadmap or services.

**2. Carrier M&A and market stress.** Consolidation, combined ratio pressure, cat losses, and reinsurance costs drive vendor consolidation and cost cutting.
- *Predicts:* Churners are disproportionately acquired or financially stressed carriers, and many don't adopt a better competitor at all.

**3. Cohort or fit effect.** A batch of customers signed roughly 3 to 4 years ago (typical contract length) is now renewing. That batch may have been sold into a new segment, sold by particular reps, heavily discounted, or oversold on capabilities.
- *Predicts:* Churn concentrated in one signing cohort, segment, or sales team. Renewal price increases correlate with churn.
- *Note:* This would also explain long implementations, since poor-fit customers are hard to implement. The services team could be seeing a symptom rather than the cause.

**4. Value-gap synthesis.** Customers compare realized value (lowered by slow implementation) against competitor *promised* value (raised by AI demos).
- *Predicts:* An interaction effect. Churn is highest where adoption is low *and* a competitor actively pitched. Well-adopted customers resist competitor pitches, and poorly-adopted customers with no competitor pitch linger.
- *Why it matters:* This is a legitimate hypothesis with its own predictions, not a diplomatic compromise. Only accept it if the interaction actually shows up in the data.

---

## Step 5: Cheapest tests, roughly in order of cost

1. **Pre-register predictions (1 day).** Have each VP write down what their hypothesis predicts for the tests below, including what result would count against it. This single step removes most of the easy-to-vary problem.
2. **Churn decomposition from existing data (1 to 2 weeks).** For every account up for renewal in the last 24 to 36 months, churned or retained, pull:
   - time-to-go-live and implementation overrun
   - adoption depth
   - support ticket volume, severity, and CSAT
   - signing cohort, segment, and sales rep
   - renewal price change
   - M&A status and core-system events
   - destination vendor

   Compare churn rates across these splits. With small numbers, look for large, obvious differences rather than significance tests.
3. **Destination analysis (days).** Where did each churned customer go? This alone may kill one or more hypotheses: an AI-forward competitor, a suite vendor, an acquirer's incumbent system, or nothing.
4. **Competitive win-rate trend (days).** New-logo win rates against the specific competitors named, over the same 18 months.
5. **"What changed 18 months ago?" timeline (days).** List internal changes (services headcount, implementation backlog, pricing, sales territory or ICP changes, support reorg) and external ones (competitor launches, suite bundling, M&A wave). The churn inflection should line up with a cause.
6. **Independent win/loss interviews (2 to 4 weeks).** Target 8 to 12 churned customers plus a few at-risk and retained accounts, conducted by a third party. Reconstruct the decision.

---

## Step 6: What to do with the results

Decide the decision rules in advance:

- **High-adoption customers churn at similar rates, they go to feature-leading competitors, and new-logo win rates dropped:** Product gaps survive. Fund the roadmap, specifically the capabilities that showed up in lost decisions, not "AI" generally.
- **Churn concentrates in slow or shallow implementations, well-adopted customers stay, and win rates are flat:** Service experience survives. Fix onboarding and time-to-value first.
- **Churners go to suite vendors, or were acquired, or cluster in one cohort:** Both VPs are wrong about the main driver. The response is partnership, integration, positioning, or sales qualification.
- **The interaction pattern appears:** Do both, sequenced. Protect at-risk low-adoption accounts with value-realization work, and target roadmap investment at the capabilities competitors are using to pitch them.

**No-regret moves while you test:**
- Flag currently at-risk accounts using the obvious signals (low adoption, long implementation, competitor contact, core-system project underway).
- Assign executive sponsors to the largest of those accounts.

These are cheap, they don't commit you to either theory, and they buy time.

The most important move is the first one: get both VPs to commit in writing to what would prove them wrong. Whichever one resists doing that is telling you something about their hypothesis.

## Turn 2

**User:** You called the new-logo win rate test especially clean, but in a small regional carrier market where prospects call references, wouldn't a reputation for painful implementations also depress win rates, so the service conjecture could absorb a drop just as easily? What would actually separate the two there, such as the reasons lost prospects gave or whether losses happened before or after reference calls?

**Assistant:**

You're right, and the concession matters. In a market this small, a prospect's decision is shaped by what peers say, not just by demos. A reputation for painful implementations would depress win rates, so a drop in new-logo wins is ambiguous. I overstated how clean the test is.

## What the win-rate test still does

The test is asymmetric:

- **A drop in win rate** is compatible with both conjectures. On its own it discriminates nothing.
- **A flat win rate** is more damaging to the product-gap story than to the service story. Prospects see feature gaps directly in demos and RFP scoring, so a real capability gap should show up in new deals quickly. The service conjecture can survive a flat rate by arguing that reputation hasn't spread yet. That argument is weaker in a small market where word travels fast, but it isn't absurd.

So the aggregate rate only tells you something in one direction. To separate the hypotheses when win rates fall, look inside the lost deals.

## What separates them inside lost deals

**1. Where in the funnel you lost**

The two conjectures predict losses at different stages:

| Stage | Product gap predicts | Service reputation predicts |
|---|---|---|
| Shortlist / RFP response | Excluded for failing capability requirements | Excluded less often on requirements |
| Demo and scripted scenarios | Lower functional scores, losses here | Competitive scores here |
| Reference / due diligence | Losses less concentrated here | Losses concentrated here, or late (after strong demo scores) |
| Contract negotiation | Normal terms | Unusual demands on delivery risk |

Timing relative to reference calls is a useful signal, but it has a flaw. In regional insurance, reputation travels informally before any formal reference call: state associations, mutual networks, industry conferences, and selection consultants. A prospect may have heard about your implementations before you were even shortlisted. So "lost before references" doesn't rule out reputation. The sharper version is to ask whether you lost on scored capability or on judged risk, wherever in the process that judgment happened.

**2. The scoring itself**

Many carriers run structured selections with separate scores for functionality, implementation approach, cost, and vendor viability. Many will give a debrief if asked, and selection consultants often share more. A pattern of competitive or high functional scores combined with low implementation-risk scores points to reputation. The reverse points to product.

This evidence is better than stated loss reasons, for the same reason as with churners. "You lacked the AI features we needed" is the polite way to say no. A scorecard is harder to soften after the fact.

**3. What prospects negotiate for**

Deal behavior reveals concerns that prospects may not state:

- **Delivery-risk signals:** fixed-price or fixed-timeline implementation, go-live penalties, milestone-based payments, requests for longer proofs of concept, or insisting on talking to customers you didn't nominate.
- **Capability signals:** added AI/analytics requirements in RFPs, roadmap commitments written into contracts, or specific competitor features used as benchmarks.

This data is already sitting in your CRM notes and redlined contracts.

**4. Network exposure**

This test takes advantage of the small market. Map each lost prospect's connections to your customers, especially unhappy ones: same state, same mutual or reinsurance group, same selection consultant, same TPA, or former employees who moved between carriers.

- **Reputation predicts** that losses cluster among prospects close to churned or struggling customers.
- **Product gap predicts** that losses are roughly independent of that proximity, because the gap is visible to anyone who demos.

With small numbers this won't be statistically clean, but a strong clustering (or clear absence of it) is informative.

**5. Uncontaminated segments**

Look for prospects who can't have heard much about your implementations: new states, new lines of business, carriers outside your usual networks, or deals run by consultants who haven't handled your installations. If you lose these at the same rate as everywhere else, reputation can't be doing the work. If you win them at a noticeably higher rate, it probably is.

**6. Lag structure**

The two stories predict different timing for the win-rate drop:

- **Reputation** should lag your implementation problems. Bad implementations happen first, customers become unhappy, and then win rates fall months later as word spreads.
- **Product gap** should track competitor launches and the appearance of new requirements in RFPs, regardless of your internal delivery performance.

If the win-rate decline started before implementations deteriorated, the reputation explanation is in trouble.

**7. What the winner offered**

Check who beat you and on what basis. A reputation story predicts competitors winning with less capability and a more credible delivery plan: faster timelines, fixed prices, a strong implementation partner. A product story predicts competitors winning with visibly superior features even when their implementation plans are comparable or worse.

## A caution on the evidence

With a small deal count, none of these tests will be decisive alone. What you're looking for is convergence. If funnel stage, scorecards, negotiation behavior, network exposure, and uncontaminated segments all point the same way, you can act with confidence. If they split, you likely have a genuine mixture, and you should weight investments by where the losses actually occurred.

Two procedural points from before apply even more strongly here:

- **Pre-register what each VP predicts** for these specific tests before anyone pulls the data. Both hypotheses have now shown they can absorb an ambiguous aggregate, so commitments at this level of detail are what make them testable.
- **Have someone neutral run the lost-prospect debriefs.** A sales rep asking "why did we lose?" will hear a different answer than a third party reconstructing how the selection committee scored and decided.

## Turn 3

**User:** Given how few lost deals a regional market produces, aren't these win-rate tests a sideshow next to the churn data, and what adoption threshold should we lock in before looking so the service conjecture can't just redefine "full value" if some well-adopted accounts still left?

**Assistant:**

# Win-Rate Tests vs. Churn Data, and Locking the Adoption Threshold

## Are the win-rate tests a sideshow?

Mostly, yes. The churn data has a structural advantage: every renewal is an observation, not just every loss. If you have 150 customers and 60 renewals in the window, you have 60 data points, including all the accounts that stayed. Competitive new-logo losses in a regional market might total 10 to 25 over the same period, split across several explanations. The churn analysis should carry the decision.

The win-rate work still earns two small roles:

1. **Covering what churn data can't reach.** Churn data only includes customers who experienced your implementation, so it can never fully separate product gaps from service pain. Prospects evaluate the product without that history. That's why a flat win rate is still meaningful evidence against the product-gap story.
2. **Tie-breaking.** If the churn analysis comes back inconclusive, convergent evidence from lost deals can tip the balance.

So keep it cheap. Pull CRM notes, redlined contracts, and a handful of debriefs. Don't commission a large study, and don't let it delay the churn analysis.

## Locking the adoption threshold

The goal is to make "full value" a measurement fixed before anyone knows who churned, so it can't be redefined after the fact.

### 1. Measure adoption at a fixed point before the renewal decision

Customers who have decided to leave stop investing in the product. If you measure adoption at renewal, you'll find churners had low adoption regardless of what caused it.

Pick a fixed point, such as **12 months after go-live** or **9 to 12 months before the renewal date** (whichever falls earlier, roughly before any notice period). Use that snapshot for every account.

### 2. Define adoption in terms of use, not outcomes

"Did they get ROI?" or "Did claims cycle time improve?" are too elastic and too hard to measure consistently. Define adoption by whether the product is actually running the business. For claims software, something like:

| Component | Example threshold (calibrate, don't copy) |
|---|---|
| Contracted scope live | All contracted lines of business and modules in production |
| Volume coverage | ≥80% of claims in contracted lines processed in the system |
| User coverage | ≥70% of licensed adjusters active weekly |
| Core workflow use | FNOL, reserving, payments, and diary/task management all in regular use |
| Key integrations live | Policy admin, payments, and document management connected |

An account is **"fully adopted"** only if it meets all five. Accounts meeting none or one are **"low adoption."** Everything in between is **"partial."** Three tiers let you check for a dose-response pattern, not just a binary split.

**Calibrating without contamination:** Look at the distribution of these metrics across accounts to set sensible cut points. For example, if only 3 accounts would hit 80% volume coverage, the threshold is too strict to test anything. But do this calibration with churn status hidden. Have an analyst who doesn't know which accounts left set the cut points and classify every account into a tier. Then join the churn data.

### 3. Split service into implementation and support before looking

This is the escape hatch you're most likely to face. If well-adopted accounts churn, the service camp can say, "They adopted, but support was painful." That's a legitimate part of their conjecture, but it has to be declared as a separate prediction up front, not introduced afterward.

Define support experience separately, measured over the 12 months before the renewal window:

- Count of Sev1/Sev2 tickets
- Median time to resolution on those tickets
- Number of executive escalations
- Support CSAT, if you collect it

Set a "poor support" threshold the same way: calibrated blind, then locked.

Then the service conjecture must commit to one of these in writing:

- **(a) Adoption is the driver.** Fully adopted accounts churn much less, regardless of support.
- **(b) Adoption and support are both required.** Fully adopted accounts with acceptable support churn much less. Fully adopted accounts with poor support churn at rates closer to low-adoption accounts.

Whichever they choose, the prediction is locked. If they pick (a) and the data shows (b), that counts as a partial refutation that has been noticed and recorded, not a quiet revision.

### 4. Lock the exclusions too

Exclusions are another place to rescue a hypothesis. Decide now which churned accounts are removed from the analysis, and apply the rule mechanically:

- Acquired by or merged into another carrier
- Insolvent, or exited the lines of business the product served
- Moved to a core suite as part of a policy/billing replacement (analyze these separately under the platform-consolidation hypothesis, not as evidence for or against either VP)

Anything not on the list stays in. No case-by-case judgment after the fact.

### 5. State predictions with refutation bands

Both VPs sign a one-page document. With small numbers, precise significance tests aren't realistic, so use rough bands instead, set before looking:

- **Service conjecture supported:** Voluntary churn among fully adopted accounts is less than half the rate among low-adoption accounts, with partial adoption in between.
- **Service conjecture refuted as the primary driver:** Fully adopted accounts churn at 70% or more of the low-adoption rate.
- **Inconclusive:** Anything in between, or fewer than about 10 accounts in the fully adopted tier.

The product conjecture gets matching bands. Its prediction is roughly the mirror image: similar churn across adoption tiers, with churned fully adopted accounts going disproportionately to the feature-leading competitors.

The confound from the first answer also gets locked here. The product camp's likely escape is "low adoption was caused by the product gaps." To block it, the product conjecture must predict that low-adoption churners were shallow on the core workflows competitors also offer (FNOL, reserving, payments) for reasons the product camp attributes to capability. If low-adoption churners never got core workflows running because of implementation delays, that points to service, and the product camp agrees in advance to accept that reading.

### 6. Accept that "inconclusive" is a real result

With your numbers, the retrospective analysis may land in the middle band. If it does, the right move is to extend the test forward, not to reinterpret. Keep the definitions frozen and apply them to every renewal over the next two or three quarters. Meanwhile, act on the no-regret measures: protect at-risk low-adoption accounts and assign executive sponsors to the largest ones.

Freezing the definitions matters more than getting them perfect. A slightly wrong threshold applied consistently gives you a test. A better threshold chosen after seeing the results gives you a story.

## Turn 4

**User:** If the dose-response pattern shows up, doesn't the poor-fit cohort explanation predict it too, since oversold customers would both adopt shallowly and churn? What cheap check would tell us whether slow implementations were caused by our delivery, which onboarding fixes could address, or by the customer's fit, which they couldn't?

**Assistant:**

Yes. Dose-response is exactly what the poor-fit explanation predicts. Oversold or mis-targeted customers would implement slowly, adopt shallowly, and churn, and onboarding fixes wouldn't save most of them. So the pattern alone doesn't favor the service conjecture. It favors "something about these accounts made implementation hard," and fit is one candidate.

Two structural facts let you pull the explanations apart:

1. **Fit is determined before implementation starts.** Every oversold or mis-targeted account left traces in documents dated before go-live work began. You can score fit from those documents without using anything the implementation produced.
2. **Delivery quality varies in ways unrelated to fit.** Which team you got, whether a key consultant quit mid-project, and whether you started during a backlog are largely accidents of timing. If those accidents predict duration and churn among similar-fit customers, delivery is doing real work.

These give three cheap checks, all using records you already have.

## Check 1: Score fit from pre-implementation documents, then stratify

Have an analyst who doesn't know churn status or implementation outcomes score each account's fit using only documents from the sale and the start of the project (discovery notes, the proposal, the SOW, the signed contract).

Candidate fit indicators (lock them before scoring):

- **Promised capability not in the product:** roadmap commitments, "gap lists," or custom development written into the SOW or contract
- **Customization load:** number of required customizations or configuration exceptions in the SOW
- **Proven territory:** lines of business, states, or carrier size outside the range where you have successful reference customers
- **Integration complexity:** number and age of legacy systems to integrate
- **Customer capacity:** dedicated project staff and IT resources committed by the customer
- **Deal pressure:** unusual discounting, compressed sales cycles, quarter-end signing

Combine these into a simple good-fit / poor-fit classification. The small number of accounts rules out anything finer.

Then look at the adoption-churn relationship within each fit group:

- **Adoption still predicts churn among good-fit accounts:** Delivery is contributing. These customers were implementable and still got stuck.
- **The pattern mostly disappears within fit groups:** Fit is doing the work. Adoption was mostly a marker of fit.
- **Poor-fit accounts churn heavily regardless of adoption:** Fit is a direct cause, and onboarding won't reach it.

With small numbers, a 2×2 table (fit × adoption, with churn rate in each cell) is about as fine as the data can support.

## Check 2: Code the causes of delay from project records

Every delayed implementation leaves a trail: change requests, status reports, delay logs, and escalation emails. Have someone neutral code each delay against categories fixed in advance:

| Vendor-side (delivery) | Customer-side (fit or capacity) | Scope-gap (overselling) |
|---|---|---|
| Our staffing shortages or turnover | Customer staff unavailable | Custom work to deliver something the product didn't do |
| Our configuration errors or defects | Poor legacy data quality | Requirements discovered after signing that the product didn't meet |
| Our integration work late | Customer decision delays | Features promised by sales, not delivered |
| Rework caused by our mistakes | Customer-driven scope expansion | |

Don't rely on the project managers' own attributions. They have an obvious interest in blaming the customer, and customers blame the vendor. Read the dated records and code what happened.

The third column matters. "Oversold" often means **sold features the product doesn't have**. That's a product gap, just located in sales promises rather than competitor comparisons. If scope-gap delays dominate, both VPs are partly right, and the most direct fix may be sales qualification and honest scoping, not either of their proposals.

## Check 3: Use accidental variation in delivery

Pull staffing and scheduling records to find variation in delivery quality that had nothing to do with the customer:

- **Team assignment:** Which implementation lead, team, or partner ran the project, if assignment was driven mainly by availability
- **Mid-project disruption:** Whether key vendor staff left during the implementation
- **Backlog timing:** Whether the project started during a period when your services team was overloaded

Compare similar-fit accounts that got different delivery conditions:

- **Similar-fit customers with disrupted or overloaded delivery ran longer and churned more:** Strong evidence for delivery as a cause, because the customer didn't choose those conditions.
- **Delivery conditions make little difference once fit is accounted for:** The service conjecture loses much of its force.

Check first whether assignment was truly by availability. If your best teams were deliberately assigned to the hardest accounts, the comparison is confounded and you'd need to account for that.

One related trend check is nearly free. Plot implementation duration over time, split by fit group. If durations lengthened for good-fit and poor-fit accounts alike, starting around the same date, something changed in delivery. If only poor-fit durations grew, and the share of poor-fit accounts rose (for example, because sales moved into new segments), that points to fit.

## Reading the results together

| Pattern | Likely cause | What to do |
|---|---|---|
| Good-fit accounts with slow delivery churn; vendor-side delays dominate; delivery accidents predict outcomes | Delivery | Fix onboarding and services, as VP Services proposes |
| Churn concentrated in poor-fit accounts regardless of delivery; customer-side delays dominate | Fit or targeting | Tighten sales qualification, redefine who you sell to, and consider managed exits for poor-fit accounts |
| Scope-gap delays dominate | Overselling | Fix sales promises and scoping; close the specific product gaps salespeople kept promising |
| Both vendor-side and fit effects show up | Mixture | Fix delivery for good-fit accounts, and fix qualification to stop adding poor-fit ones |

The fit story also needs its own test, so it can't absorb every result the way the original two conjectures could. Fit makes a checkable prediction: poor-fit accounts should be visible in the pre-implementation documents. If the blind scorer can't distinguish churned accounts from retained ones using those documents, the fit explanation fails.

Pre-register as before. Lock the fit indicators, the delay categories, and the predicted pattern for each hypothesis, and have all three camps sign before anyone joins the data to churn outcomes.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

We still can't know which VP is right. What you can do is run a six-week diagnosis with the decision rules agreed in advance, while taking a few cheap steps that pay off no matter which explanation wins. Here's the plan.

## This week: set it up so the answer can't be argued away

**Get executive sponsorship for the decision rules, not just the analysis.** Take the plan to your CEO or COO and get agreement that budget follows the results. Without that, a clear finding just becomes one more opinion in the next planning meeting.

**Pick a neutral owner.** Retention is your number, so you have a stake too. Have a finance or BI analyst run the analysis, with you as sponsor. Budget roughly one analyst for six weeks plus a small fee for third-party interviews.

**Write the pre-registration document.** Keep it to two pages, signed by VP Product, VP Services, and your sales leader (who owns the fit hypothesis). It should lock:

- The definitions: adoption tiers, support tiers, fit indicators, delay categories, exclusions
- What each hypothesis predicts
- The refutation bands for each hypothesis
- What decision follows each result

**Hold off on big, irreversible bets for six weeks.** Don't approve a major AI roadmap acceleration or a large services hiring plan on the basis of exit-survey reasons. Normal work continues.

## Weeks 1–2: fast checks that may settle a lot

1. **Sanity-check the churn itself.** Get raw counts, logo vs. revenue churn, and voluntary vs. involuntary. If the doubling comes from a handful of accounts, you're investigating those accounts, not a trend.
2. **Destination analysis.** Find out where every churned customer went: a feature-leading competitor, a core suite vendor, an acquirer's incumbent system, or nothing. This is the cheapest test you have and it may rule out whole explanations.
3. **Build a "what changed 18 months ago" timeline.** List internal changes (services staffing, backlog, pricing, sales segments, support reorganization) and external ones (competitor launches, suite bundling, carrier M&A). Line them up against the month churn started rising.

## Weeks 2–5: the core analysis

4. **Blind coding.** The analyst, without knowing churn status:
   - Classifies each account's adoption tier at the fixed snapshot point
   - Classifies support tier
   - Scores fit from pre-implementation documents
   - Codes the cause of each implementation delay from project records
   - Notes delivery accidents: team assignment, mid-project staff turnover, backlog timing
5. **Join to outcomes and read against the pre-registered bands.** Key outputs:
   - Churn by adoption tier, within good-fit and poor-fit groups
   - Delay causes split into vendor-side, customer-side, and scope-gap
   - Delivery-accident comparisons among similar-fit accounts
   - Implementation duration trends by fit group
6. **Third-party interviews with 8–12 churned customers.** Reconstruct how the decision was made: who decided, which alternatives were evaluated, and when the decision was really made.
7. **Light review of lost deals.** Use CRM notes, redlined contracts, and any debriefs or scorecards you have. Treat this as a tiebreaker only.

## Week 6: decide

Apply the rules you signed in week one:

- **Delivery wins:** good-fit accounts with slow delivery churned, vendor-side delays dominate, and delivery accidents predict outcomes. Fund the onboarding and services fixes, aimed at the specific delay causes you coded.
- **Product wins:** well-adopted accounts churned to feature-leading competitors. Fund the specific capabilities that appeared in those decisions, not "AI" in general.
- **Fit wins:** churn is concentrated in poor-fit accounts regardless of delivery. Tighten sales qualification and redefine who you sell to. Plan honestly for poor-fit accounts, which may mean managed exits.
- **Overselling wins:** scope-gap delays dominate. Fix sales promises and scoping, and close the gaps salespeople kept promising.
- **Platform consolidation or M&A dominates:** pursue integration and partnerships with suite vendors, and reposition. Neither VP's plan addresses this.
- **Mixture:** allocate investment in proportion to where the churn actually came from.
- **Inconclusive:** keep the definitions frozen, apply them to every renewal over the next two to three quarters, and decide then.

## Start now, whatever the answer

These steps are cheap and useful under every explanation:

- **Triage at-risk accounts.** Use the frozen definitions to flag accounts with low adoption, poor support, active competitor contact, a core-system replacement underway, or recent M&A. Give the largest ones an executive sponsor and a value review before their renewal window opens.
- **Stop adding poor-fit and oversold customers.** Put any deal that includes roadmap promises, custom gap lists, or unproven lines of business through a deal-desk review. This costs almost nothing, and if fit turns out not to matter, you've lost little.
- **Make the evidence routine going forward.** Record adoption metrics at fixed points after go-live, have project managers code delay causes in the tracker as they happen, and collect structured loss reasons with a neutral debrief on every competitive loss. The next time this question comes up, the data will already exist.

## Why this approach

The pre-registration step matters more than any single analysis. Both VPs' explanations, and the fit explanation as well, turned out to be able to absorb almost any result until their predictions were pinned down. Once you lock the definitions and decision rules in advance, the next six weeks will tell you which explanation survives, or show you that it's a mixture. Six weeks of diagnosis is inexpensive compared with spending a year funding the wrong fix.

## Outcome summary (sent to Jev)

Neither VP's belief can yet be declared right, because as stated each can absorb almost any result. The recommendation is a six-week diagnosis with decision rules agreed in advance, alongside cheap moves that pay off under any explanation.

First, get the CEO or COO to agree that budget follows the results. A neutral finance or BI analyst, not customer success, should run the work. VP Product, VP Services, and the sales leader sign a two-page pre-registration locking:

- adoption and support tiers
- pre-implementation fit indicators
- delay categories and exclusions
- each hypothesis's predictions, refutation bands, and resulting decisions

Major AI roadmap acceleration or services hiring waits for six weeks.

Weeks one and two cover three checks:

- **Churn itself:** raw counts, logo versus revenue, voluntary versus involuntary.
- **Destinations:** where each churned customer went.
- **Timeline:** what changed internally and externally eighteen months ago.

Weeks two through five are the core analysis. The analyst codes adoption at a fixed pre-renewal snapshot, support quality, fit, delay causes, and delivery accidents without knowing churn status, then joins the results to outcomes. Third-party interviews with 8–12 churned customers run in parallel. Lost-deal review serves only as a tiebreaker, since the market produces too few losses.

In week six, funding goes where the signed rules point:

- onboarding fixes if delivery drove churn
- specific capabilities, not generic "AI," if product did
- sales qualification and possibly managed exits if fit did
- honest scoping if overselling did
- suite-vendor partnerships if consolidation or M&A dominates
- proportional investment if it's a mixture
- frozen definitions applied to future renewals if results are inconclusive

Starting now, flag at-risk accounts and assign executive sponsors. Deal-desk review should cover deals with roadmap promises or unproven lines of business. Adoption, delay causes, and loss reasons should become routine data.

Caveats: small numbers may yield inconclusive results, and dose-response patterns alone can't separate delivery from fit.
