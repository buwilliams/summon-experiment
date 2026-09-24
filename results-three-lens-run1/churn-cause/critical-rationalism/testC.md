# critical-rationalism/churn-cause/testC

Model: claude-opus-5-5 · 2026-09-24T14:47:55.943398+00:00

## Turn 1

**User:** Use the method of conjectures and refutations (critical rationalism) to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Which Belief Explains Your Churn? A Critical-Rationalist Analysis

## The short answer

Neither belief can be confirmed by piling up supporting anecdotes. Both VPs can easily find churned customers who "prove" their view. The useful question is different: **what evidence would show each belief to be false?** Go looking for that evidence. Whichever belief survives serious attempts to refute it earns tentative trust. Right now you don't have enough information to choose. You probably do have the data to find out within a few weeks, before you commit a roadmap or a reorganization.

---

## Step 1: Turn each belief into a bold, testable conjecture

Vague versions of each claim ("product matters," "service matters") can't be wrong, so they tell you nothing. Sharpen them:

**C1, Product Gap (VP Product):** Customers leave because competitors offer analytics or AI capabilities we lack. They would leave *even if* their implementation had gone well and they were fully using our product.

**C2, Implementation/Service Failure (VP Services):** Customers leave because they never reach full value. Long, painful implementations and weak support leave them under-deployed. Customers who *were* fully implemented mostly stay.

These make different predictions, so they can be tested against each other.

---

## Step 2: Derive predictions where the conjectures disagree

| Test | If C1 (product gap) is true | If C2 (implementation) is true |
|---|---|---|
| **Churn by implementation status** | Fully live, well-adopted customers churn at a meaningful rate | Churn is heavily concentrated in customers who went live late, partially, or never |
| **Churn by customer age** | Churn is spread across tenure, including long-standing, mature accounts | Churn clusters at the first or second renewal |
| **Implementation duration vs. churn** | Weak or no correlation | Strong correlation: longer implementations mean higher churn |
| **Where churned customers go** | Mostly to specific competitors known for analytics and AI | Scattered: competitors, legacy systems, in-house tools, anyone |
| **New-business win rates** | Also falling, with losses to the same competitors on feature grounds | Largely unchanged, since prospects haven't experienced implementation yet |
| **Feature complaints from churned customers** | They cite features we *don't have* | They cite features we *do have* but they never deployed ("we couldn't get reporting working") |
| **Timing of the churn increase** | Follows competitor AI/analytics launches | Follows a change on our side: sales outpacing services capacity, team turnover, a new product version, a shift in customer size |

The strongest single test is the **2×2 table**: fully implemented vs. not, crossed with renewed vs. churned.

- **If fully implemented customers churn at nearly the same rate as poorly implemented ones, C2 is badly damaged.** Fixing onboarding won't fix churn.
- **If fully implemented customers almost never churn, C1 is badly damaged.** The features apparently weren't the problem for customers who actually got the product working.

---

## Step 3: Guard against the usual ways these tests get fooled

**Exit interviews are weak evidence.** "Your competitor has better AI" is a polite, face-saving reason to give a vendor. "Your implementation was a mess and our team gave up" is awkward to say. Weight behavioral data (usage logs, go-live dates, ticket volume, destination) above stated reasons.

**Implementation failure can disguise itself as a product gap.** A customer who never got the analytics module configured will honestly say "your analytics are weak." Check whether the capabilities they miss actually exist in your product.

**Both VPs have an interest in their own answer.** Each theory conveniently assigns the fix to the other person's department's failure and the budget to their own. This doesn't make either wrong. It does mean the analysis should be done by someone neutral, with prediction criteria agreed in advance. Get both VPs to sign off *now* on what result would count against their view. This is the most important procedural step, because it stops either side from reinterpreting the data after the fact.

---

## Step 4: Take rival conjectures seriously

The debate is framed as a two-way choice, but churn doubling in 18 months could have other causes that neither VP has proposed. Test these too, because some can be checked in an afternoon:

- **C3, Carrier consolidation:** Regional carriers are being acquired, and the acquirer moves them onto its own system. *Test:* How many churned accounts were acquired or merged? Nothing you do to product or onboarding fixes this.
- **C4, Segment drift:** Sales began selling to carriers that are larger, smaller, or in different lines than the product fits. *Test:* Compare churn by customer profile and signing cohort.
- **C5, Pricing or contract change:** A price increase or renewal-term change about 18 months ago. *Test:* Look at churn by renewal price change.
- **C6, Champion loss:** Your internal sponsor left, and their successor chose differently. *Test:* Look at contact turnover before churn.
- **C7, Budget pressure:** A hard catastrophe-loss or reinsurance environment squeezed IT budgets. *Test:* Check whether churned customers downgraded or cut vendors broadly.

Ask one question explicitly: **what changed about 18 months ago?** A doubling is a signal of a change, not a slow drift. Whichever conjecture best explains the *timing* deserves extra weight.

The likely outcome is that churn breaks into segments, with different causes dominating in different groups. That's fine, but insist on numbers: "about 50% implementation-related, 20% acquisitions, 20% competitive feature loss, 10% other." "It's a bit of everything" can't be falsified and can't guide investment.

---

## Step 5: What to do

**1. Spend 2–4 weeks attacking the conjectures before reallocating anything.** Pull every churned account from the last 18 months plus a comparison set of renewals. For each, record:
- implementation duration
- go-live completeness
- adoption and usage
- tenure at churn
- destination
- acquisition status
- price change
- support ticket history

Build the 2×2 table and the other tests above. Most of this data already exists in your CRM, product analytics, and implementation records.

**2. Agree on the refutation criteria first**, in writing, with both VPs.

**3. Meanwhile, make small, reversible bets instead of big irreversible ones.** This is Popper's "piecemeal engineering." Small bets let you learn from errors cheaply.
- *Testing C2:* Run a redesigned onboarding program (fixed scope, time-boxed go-live, a value milestone at 90 days) on the next several implementations. Compare time-to-value against recent cohorts.
- *Testing C1:* Take accounts at risk of leaving over features and show them a concrete analytics or AI roadmap commitment or prototype. See whether it changes renewal intent. If a credible feature promise doesn't move them, the features probably aren't the real reason.

**4. Keep a leading indicator for each surviving conjecture** so you learn quickly if you're wrong. Examples: time-to-go-live and 90-day adoption for C2, competitive loss rates for C1.

**5. Treat whatever survives as provisional.** Keep correcting as the market shifts. If competitors' AI features become table stakes, a theory that is false today could become true next year.

---

## One structural observation

The two conjectures aren't symmetric in how cheaply they can be tested. C2 can be largely confirmed or refuted from internal data you already own. C1 needs competitive intelligence and is easier to rationalize. Also, **if C2 is true, accelerating the roadmap could make churn worse.** More features mean longer, more complex implementations for customers who already aren't reaching value. The reverse risk is smaller: improving onboarding rarely hurts even if product gaps also matter.

That asymmetry doesn't tell you which belief is right. It does suggest where to aim your first and cheapest refutation attempt. Test the implementation hypothesis first, because it's quick to test and the cost of wrongly accelerating the roadmap is high.

## Turn 2

**User:** Suppose the 2×2 comes back muddy: fully implemented customers churn at roughly half the rate of poorly implemented ones, but still well above our historical baseline. Sticking with conjectures and refutations, how would you interpret that and what would you test next?

**Assistant:**

# Interpreting a Muddy 2×2

A muddy result is not a failed test. It has refuted something. You just have to be precise about what.

## Step 1: What the result refutes

Recall the two sharpened conjectures:

- **Strong C2** said fully implemented customers mostly stay. **Refuted.** They churn well above your historical baseline, so implementation failure cannot be the whole story.
- **Strong C1** said customers leave regardless of implementation. **Refuted.** A 2× difference by implementation status is too large to dismiss, *if* it holds up to the checks below.

So the either/or framing is gone. That is progress. It is not a license to conclude "it's both" and stop, because that claim explains everything and therefore nothing. The job now is to form new, sharper conjectures about *how much* each cause contributes and *why*, and then try to break those.

## Step 2: Don't trust the 2× gap yet

The result is correlational, and three readings would make it misleading.

**1. Selection.** Implementation quality wasn't randomly assigned. The customers with troubled implementations may differ in other ways: smaller carriers, thin IT teams, bad-fit segments, weak executive sponsorship. Those traits could drive both the poor implementation and the churn. In that case, fixing onboarding would help less than the gap suggests.

**2. Reverse causation.** Some customers may have stalled their implementations *because* they were already losing interest, were being acquired, or were evaluating a competitor. Then poor implementation is a symptom of churn, not a cause.

**3. A loose definition.** "Fully implemented" may mean "went live," not "uses the product deeply." If the category is full of shallow users, the fully implemented churn rate is inflated. The real effect of reaching value would then be *larger* than it looks.

A warning about the third reading. It is exactly the argument the VP of Services will reach for: "those customers weren't *really* fully implemented." That move is legitimate only if the stricter definition is:

- stated in advance,
- measured independently (usage depth, modules active, users per seat), and
- tested for a dose-response pattern.

Otherwise it is an ad hoc rescue, redefining terms until the theory can't lose. Popper's line between the two is whether the auxiliary hypothesis makes *new testable predictions*. Here it does, so test it rather than argue about it.

## Step 3: Work out how much each cause could explain

Before running new tests, do the arithmetic. It sets an upper bound on what each explanation can account for. Here is an illustration with hypothetical numbers:

- Historical baseline churn: 8%. Current churn: 16%.
- Fully implemented customers now churn at 12%. Poorly implemented customers churn at 24%.
- Those figures imply about one-third of customers are poorly implemented.

Suppose you could magically make every implementation perfect, *and* the relationship is fully causal. Churn would fall to 12%. That recovers **at most half** of the increase. The remaining 4 points need a different explanation.

Run this with your real numbers. It tells you, before any further debate, the most an onboarding fix could achieve and how much churn remains unexplained.

## Step 4: Next tests, in priority order

### Test 1: Split the increase into mix shift and rate shift

Compare today's split with the historical one, using the same definitions. The doubling in churn could come from either of two sources:

- **Mix shift:** a larger *share* of customers are now poorly implemented, perhaps because sales outpaced services capacity or the customer base drifted to a different segment.
- **Rate shift:** churn rose *within* each group.

This test discriminates sharply:

- **If most of the increase is mix shift,** C2 explains the *trend* even though it doesn't explain all churn. Services capacity or segment drift is the story.
- **If within-group rates roughly doubled in both groups** while the roughly 2× ratio stayed stable, look for a *cross-cutting* cause that raised churn for everyone. Candidates include:
  - pricing changes,
  - carrier consolidation,
  - budget pressure,
  - a competitor that is pulling customers regardless of their implementation state.

  Onboarding fixes won't touch that increase.

### Test 2: Examine the fully implemented churners closely

This group is where the product-gap conjecture can be tested most cleanly, because the implementation explanation is weakest here. For each account, establish:

- where it went,
- whether it was acquired,
- whether it faced a price increase,
- whether it lost its internal champion,
- which capabilities it cited, and whether you actually have those capabilities.

Three patterns are possible:

- **They went to AI/analytics competitors, citing features you genuinely lack.** C1 survives a serious test for this segment. This is the strongest evidence the VP of Product could get.
- **They were mostly acquired or cut spending across all their vendors.** C3 or C7 takes the residual, and C1 is weakened.
- **They cite features you have.** Your definition of "fully implemented" is too loose. Go to Test 3.

### Test 3: Check for a dose-response relationship

Replace the binary split with a measure of adoption depth. Does churn fall steadily as adoption deepens? And do the most deeply adopted customers churn at roughly the historical baseline?

- **If yes:** C2 is strengthened, and the muddy 2×2 was partly a measurement problem.
- **If even your heaviest users churn above baseline:** something outside implementation is operating, and it's hitting your happiest customers.

Deep users leaving is the worrying result, and it points toward C1 or a market-level cause.

### Test 4: Establish the order of events for poorly implemented churners

Build timelines. Did the implementation stall because of *your* delays (resourcing, scope creep, defects), or *theirs* (lost sponsor, reprioritization, an acquisition announced)? Did disengagement come before or after the implementation trouble?

- If stalls were mostly on your side and came first, the causal story for C2 holds.
- If stalls were mostly on the customer's side and came after other warning signs, reverse causation explains much of the gap.

### Test 5: Test whether the two causes interact

Here is a new conjecture worth stating: *product gaps matter mainly to customers who never reached value.* A deeply adopted customer is hard to pry loose. A frustrated, half-implemented one takes the competitor's AI demo seriously.

It predicts that poorly implemented churners disproportionately went to feature-rich competitors, while fully implemented churners left for other reasons. If that pattern appears, it changes the strategy. Onboarding becomes your competitive defense, not just a service fix.

### Test 6: Check new-business win rates

As before, feature losses in competitive new deals are evidence for C1 that doesn't depend on implementation at all. This test matters more now that part of the churn is unexplained.

## Step 5: What to do while testing

- **The result already justifies some onboarding investment,** subject to the selection and reverse-causation checks. Size it to the bound from Step 3, not to the whole churn problem.
- **Don't commit the full roadmap acceleration yet.** Test 2 is the decisive evidence for or against C1, and it's cheap to run.
- **Write down the next round of refutation criteria before looking at the data.** For example: "If the heaviest-adopting quartile churns at more than 1.5× the historical baseline and mostly to AI competitors, we fund the analytics roadmap." Pre-committing is what keeps a muddy result from becoming a license for each VP to read the data their own way.

The muddy 2×2 has told you that the problem is layered. The next round of tests tells you what the layers are and how thick each one is.

## Turn 3

**User:** Say Test 2 shows most of our fully implemented churners went to one competitor, but half of them cited analytics features we actually have. Still using conjectures and refutations, what does that tell us and what should we check next?

**Assistant:**

# Interpreting Test 2: One Competitor, and Features "We Actually Have"

This result is informative because it breaks the product-gap conjecture into several distinct claims. Before interpreting it, check your sample size.

## Step 0: How many accounts is this?

Fully implemented churners are the *minority* of your churn. If that group is 15 accounts, "half" is 7 or 8 customers. At that size, treat Test 2 as a way to **generate sharper conjectures**, not as a verdict. Each account deserves a deep individual investigation rather than a percentage. Keep this in mind for everything below.

## Step 1: What the result tells you

**Concentration on one competitor is a strong signal.** If generic product inferiority were the cause, departures would be spread across several feature-rich rivals. Concentration points to something specific about *this* competitor. That could be its product, but also its pricing, its sales motion, or its position in the market. The claim that you're losing customers to competitors broadly has been narrowed. The claim that one competitor is pulling your customers now needs explaining.

**Half the customers cited features they could have had from you.** That undermines the product-gap belief as originally stated for those accounts, at least in its "we lack the features" form. Customers can't be leaving for capabilities you already ship, unless one of the following is true:

- **C1b, quality gap:** You have the feature on paper, but the competitor's version is meaningfully better: easier, faster, more automated, more AI-driven. Checklist parity isn't real parity.
- **C8, value-visibility gap:** The customers didn't know the features existed, or never adopted them. That would mean "fully implemented" still hides an adoption problem after go-live. It extends the services conjecture into ongoing customer success, not just onboarding.
- **C9, go-to-market pull:** The real draw was price, bundling, contract terms, integration with their core system, or a well-run sales campaign. "Better analytics" was the *story* the competitor gave them, and they repeated it in the exit interview.

**The other half cited features you genuinely lack.** For those accounts, the original product-gap belief (C1a) has survived a real test. This is the best evidence the VP of Product has had so far, though it's limited to a small group.

So "product gaps" now covers at least four rival explanations: a true capability gap, a quality gap, a visibility gap, and a go-to-market pull. They point to very different remedies, so they need to be separated.

## Step 2: Tests that discriminate among them

### Test A: Check usage logs for the half who cited features you have

This is the cheapest and sharpest test.

| Observed pattern | What it supports |
|---|---|
| **Never used** the feature | C8. It's a visibility or enablement failure, and building more won't help. |
| **Tried it, then abandoned it** | C1b. The feature exists but doesn't deliver. |
| **Used it regularly, then left anyway** | The cited reason probably isn't the real reason. Look to C9. |

Agree before looking at the data what share of each pattern would favor which conjecture.

### Test B: Run a head-to-head comparison on real use cases

Compare your analytics with the competitor's, using the workflows churned customers actually care about, not a feature checklist. Sources include:

- demos,
- win/loss reviews,
- former customers willing to talk,
- current customers who have evaluated both.

**If your version holds up on those tasks, C1b is refuted** and the answer shifts to C8 or C9. **If theirs is clearly better,** C1b survives and "we have that" was a comforting fiction.

### Test C: Examine the deal terms

Did the competitor offer steep discounts, multi-year price locks, free migration, or a bundle with policy administration or other core systems? Ask former customers, partners, or brokers. Look for the competitor's pricing in public records if any carriers are public entities.

**If terms were unusually aggressive, C9 gains weight.** No analytics roadmap would have prevented those losses.

### Test D: Line up the timing with the competitor's moves

What changed at this competitor about 18 months ago, when your churn began to double? Possibilities include:

- a product launch,
- new funding or an acquisition,
- a new pricing model,
- a dedicated campaign targeting regional carriers,
- a partnership with a core-system vendor.

Map each departure against the competitor's timeline. Losses that follow a pricing or partnership change rather than a feature launch favor C9.

### Test E: Identify who made the decision

Did the claims staff who used your product drive the switch, or executives and IT who rarely touched it? If executives who never used the product cited missing analytics features, that citation is weak evidence of a real gap and fits C8 or C9. If heavy daily users drove the switch, their complaints deserve much more weight.

### Test F: Compare the two halves

Do the customers who cited real gaps differ from those who cited features you have? Compare size, lines of business, tenure, adoption depth, and decision-maker. A clean split would give you a segment map. For example, larger carriers might need analytics you lack, while smaller ones never discovered what you have. That map tells you whom each remedy is for.

### Test G: Run a small experiment with current customers

The tests above are all backward-looking. Run one forward-looking test of C8. Take a sample of current accounts that match the churned profile. Check whether they know about and use your analytics. Give half of them a targeted enablement effort: a walkthrough, a configured dashboard, a quarterly value review. Compare renewal-risk signals over the following months.

**If enablement measurably reduces risk, C8 is corroborated.** It's also a cheap, reversible action that pays off even if C8 turns out to be only part of the story.

## Step 3: Guard against rescuing a theory after the fact

Both VPs now have an easy escape route:

- **VP of Product:** "Customers say our analytics are worse, so they *are* worse, whatever the feature list says." This is legitimate only if Test B confirms it.
- **VP of Services:** "They never adopted the features, so it's a service problem." This is legitimate only if Test A shows non-use, not abandonment.

Hold both VPs to the same standard. Each auxiliary claim is welcome if it makes a prediction that could fail.

## Step 4: What to do while testing

- **Don't build features you already have.** For the half citing existing capabilities, a roadmap acceleration would duplicate them. Wait for Tests A and B before deciding whether the work is usability, enablement, or nothing.
- **Build a focused competitive retention play.** Identify current accounts that resemble the churned ones and match this competitor's target profile. Give them proactive attention now. This protects revenue whichever conjecture wins.
- **Size any analytics investment to the genuine-gap half,** and to the specific capabilities those customers named, not a broad AI roadmap.
- **Pre-commit to the next decisions.** For example: "If most feature-citers never used the feature, fund an analytics-enablement program before any new analytics development. If most abandoned it, fund usability work on the existing module. If deal terms explain most losses, review pricing and bundling, not product."

## Step 5: How the picture has changed

Across three rounds, a vague two-way argument has become a set of narrower claims. Implementation failure accounts for a bounded share of churn. Deep adoption protects customers, up to a point. The competitive threat is concentrated in one rival. "Missing features" appears to mean at least four different things.

None of these conclusions is proven, and each remains open to revision. Each is more specific and more testable than what you started with, and each one narrows where your next dollar should go.

## Turn 4

**User:** Suppose Test A shows most of the feature-citers tried our analytics and then abandoned it, but Test B finds our version roughly matches the competitor's on the core use cases. Still using conjectures and refutations, how would you make sense of that contradiction and what would you test next?

**Assistant:**

# Making Sense of the Contradiction

When two tests seem to contradict each other, don't quietly pick the one you prefer. In critical rationalism, a clash like this shows that at least one assumption behind your tests is false. That is useful: it points you to background assumptions you didn't know you were making.

## Step 1: State the contradiction exactly

- **Test A:** Churned customers tried your analytics and abandoned it. That suggests the feature failed them.
- **Test B:** Your analytics roughly match the competitor's on core use cases. That suggests the feature is fine.

Both can be true only if something differs between the conditions of Test B and the conditions customers actually experienced. So don't ask "which test is wrong?" Ask **"what did Test B hold constant that real life didn't?"**

## Step 2: List the hidden assumptions that could be false

Each hidden assumption becomes a candidate conjecture.

**H1. Test B measured the wrong use cases.** "Core use cases" may reflect what you or an analyst consider core, not what these carriers relied on. Parity on the standard reports says nothing about a specific report a claims manager needed every Monday.

**H2. Test B ran in demo conditions; customers lived in production.** The comparison was probably run by skilled people on clean data. Customers used the product with:
- their own messy data
- their own configuration
- their typical staff
- their real volume

In those conditions a feature can fail through slow queries, numbers that don't match other systems, awkward setup, or no fit with daily workflow, while still demoing perfectly well.

**H3. Customers compared unlike things.** This may be the most important possibility. Churned customers weighed *your product in production*, with all its accumulated frustrations, against *the competitor's product in a sales demo*. Test B compared demo against demo and found parity. That result is exactly what this conjecture predicts. Customers weren't wrong that their experience of your analytics was poor. They were wrong in assuming the competitor's would be better, or they may simply not have found out yet.

**H4. The abandoned version isn't the version you tested.** If you improved analytics recently, or these customers were on older releases, Test B tested a product they never had.

**H5. The abandonment was misread.** Usage may have moved rather than stopped: exports to Excel, data pulled into their own BI tool, API access. Or the usage may be naturally periodic, such as monthly reporting, and look like abandonment in a weekly view.

**H6. Abandonment came from causes outside the feature.** Possible causes:
- dashboards never configured for the customer's needs
- a data-quality problem that destroyed trust in the numbers
- the one trained user left
- nobody from your side helped after go-live

This refines the services conjecture: the problem isn't that customers never adopted, it's that adoption went unsupported and collapsed.

These are not mutually exclusive. But they predict different things, so they can be separated.

## Step 3: Tests that discriminate among them

### Test 1: Check whether Test B is valid before building on it

Find out:
- who ran it
- which use cases were chosen, and by whom
- on what data
- which versions were compared
- by what criteria

If your product team ran it with its own use cases on demo data, it tested H1 and H2 very weakly.

Then re-run it more severely:
- Use the use cases churned customers actually named.
- Use realistic, messy data, anonymized from a real customer if possible.
- Have typical claims staff do the work, not experts.
- Measure more than whether the output matches: setup effort, time to first useful insight, and speed at realistic volume.

If parity survives this harder version, H1 and H2 are seriously weakened. If it collapses, you have found the gap. It's in the experience around the feature, not the feature's nominal capability.

### Test 2: Reconstruct each abandonment

For each account that abandoned the analytics, work out what happened before usage dropped:

- **Error logs and query performance:** did things break or slow down?
- **Support tickets about reports or data discrepancies:** did they lose trust in the numbers?
- **Configuration state:** were dashboards ever set up for them, or left at defaults?
- **Staff changes:** did the main user leave?
- **Post-go-live contact:** did anyone from your side engage with them about analytics?
- **Version:** which release were they on? (tests H4)
- **Exports and API activity:** did usage move elsewhere? (tests H5)

The patterns point in different directions:

| Pattern | Supports |
|---|---|
| Errors and slow queries | H2 (production-condition failure; a product engineering problem) |
| Default configuration, no post-go-live support | H6 (unsupported adoption; a services/CS problem) |
| Data-discrepancy tickets | H2 or H6, depending on whether the fault was in your product or in their data integration |
| Old versions | H4 (an upgrade and migration problem) |
| Heavy exports | H5 (no real abandonment; revisit the Test A reading) |

### Test 3: Compare successful and failed users among current customers

Find current customers who use your analytics heavily and compare them with customers who abandoned it. Look at configuration, data quality, version, the size of the customer's own team, and how much your staff engaged after go-live.

This comparison can refute H2. If successful users run the same product in similarly messy real-world conditions, "the product fails in production" is weakened, and H6 gains weight.

### Test 4: Test H3 directly, the unlike-comparison conjecture

H3 makes a bold, checkable prediction: **customers who switched will struggle with the competitor's analytics too**, once they're in production with it.

Look for evidence through:
- former customers still on speaking terms
- mutual partners or implementation consultants
- user communities
- carriers that have moved away from the competitor

Did the switchers actually get more from the competitor's analytics? If they did, H3 is refuted, and the competitor genuinely delivers something in production that you don't. That would send you back to H1 and H2 with a sharper question: what exactly do they do differently?

Also examine the competitor's post-sale model. Do they bundle analytics configuration, data onboarding, or a managed reporting service? If so, their advantage may be services wrapped around a comparable product. That would corroborate a blend of H3 and H6.

### Test 5: A forward-looking intervention

Take current accounts showing the same abandonment pattern. For a sample:
- fix the configuration
- resolve data issues
- assign someone responsible for analytics outcomes

Compare re-adoption and renewal-risk signals against similar accounts that don't get the treatment. If this revives usage, H6 is corroborated and you have a remedy already tested at small scale. If the treated accounts abandon again anyway, the problem lies deeper in the product (H2), not in the support around it.

## Step 4: Guard against convenient escapes

The contradiction offers each side a tempting way out:

- **"Test B was flawed, so the product gap is real."** This is acceptable only if Test 1 shows the flaw independently. You can't discard a test because its result was inconvenient.
- **"Customers were just misinformed by the competitor's sales pitch."** H3 is a legitimate conjecture, but only because Test 4 can refute it. Without that test, it is a story that blames customers.

Both test results stand until one of them is undermined on grounds other than its conclusion.

## Step 5: What this implies for action

- **Pause any analytics feature-building aimed at these accounts.** The evidence now points away from missing capability. The candidates are the production experience, the configuration, the support, or the comparison customers made.
- **Don't treat this as a pure onboarding problem either.** The failures happened *after* go-live, among customers counted as fully implemented. An onboarding redesign alone would miss them.
- **Consider that the gap may sit between the two departments.** Here is a candidate conjecture worth testing: no one in your organization owns *whether customers get value from analytics in production*. Product ships the capability and Services gets customers live. The stretch where abandonment happens may belong to neither. Tests 2 and 5 will show whether that's true. If it is, the answer to your original question is neither VP's belief as stated. It is a responsibility neither team holds.
- **Pre-commit the next decision.** For example:
  - If the severe re-test finds a real-world gap, fund usability and performance work on the existing analytics module.
  - If abandonment traces mainly to configuration and missing post-go-live support, create an analytics-adoption function and measure it on sustained usage.
  - If Test 4 shows switchers doing no better with the competitor, invest in competitive positioning and retention, not product changes.

## Where the investigation stands

You started with a clash between two broad beliefs. You now have a narrow, testable question: why does a feature that performs at parity under controlled conditions fail in customers' hands? That is progress in the sense Popper intended. You haven't proven anything, but each refutation has shown you more precisely where you were wrong, and the remaining uncertainty now sits in a few specific, testable places.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

## The verdict on the original question

Neither VP was right, and each was partly right. Both strong claims have been refuted by the results you've described:

- **"It's product gaps"** fails. Poorly implemented customers churn at twice the rate of fully implemented ones. Half of the feature complaints concern analytics you already have. And that analytics matches the competitor's in controlled comparison.
- **"It's implementation"** fails too. Fully implemented customers still churn well above your baseline, mostly to one competitor. Some of them cite capabilities you genuinely lack.

**The best-surviving conjecture:** churn comes from three separate failures, in rough order of evidence:

1. **Poor implementation** drives a bounded but real share.
2. **A value-in-production gap** after go-live. Customers try the analytics, fail to get value in real conditions, and abandon it. No one in your organization is clearly responsible for preventing this.
3. **A narrow genuine capability gap**, exploited by one specific competitor.

Critical rationalism doesn't ask you to wait for certainty. It asks you to act on the best-tested theory you have, and to set up your actions so that you'll find out quickly if the theory is wrong. So here is a plan built that way.

## The plan

### 1. End the either/or debate and assign ownership of value realization

This matters most, and it costs nothing. Share the findings with both VPs. Present them as what survived testing, not as a win for either side.

Then give one person clear responsibility for **whether customers get sustained value after go-live**, measured on:

- sustained analytics usage
- adoption depth at 6 and 12 months
- renewal outcomes

This is the gap your tests exposed. Product ships the capability and Services gets customers live, but no one owns what happens after that.

A caution: you run customer success, so this function naturally lands with you. That is exactly why it should be held to the pre-committed metrics below rather than to your judgment or mine. The theory that favors your department is the one you should test hardest.

### 2. Start with at-risk accounts: a post-go-live analytics rescue (first 30–60 days)

Find current accounts that show the abandonment pattern. That means they tried the analytics, their usage dropped, and they match the profile of the customers who churned. For a sample of them:

- configure dashboards for the workflows they actually run
- resolve data-quality problems that undermine trust in the numbers
- assign a named person responsible for their analytics outcomes

Hold a comparable group back as a control. This is both your fastest way to protect revenue and your test of whether the value-in-production conjecture holds. If treated accounts re-adopt and their risk signals improve, expand the program. If they abandon again anyway, the problem is in the product, and budget should shift toward product fixes.

### 3. Run a defensive program against the one competitor (immediately)

Identify accounts that fit this competitor's target profile, especially those with shallow adoption. Engage them proactively at the executive level before renewal conversations start.

Base your competitive positioning on what your tests found: comparable analytics capability, with the real difference showing up in production. Give prospects a production-realistic evaluation rather than a demo-versus-demo comparison, and offer references from customers who use your analytics heavily. This protects revenue no matter which remaining conjecture turns out right.

### 4. Fix implementation, sized to its share of the problem (next 1–2 quarters)

Introduce fixed-scope, time-boxed implementations with a defined value milestone at around 90 days. Check whether sales volume has been outrunning services capacity. That is a common hidden cause, and if it applies, adding capacity or pacing new deals may matter more than redesigning the process.

Measure time to go-live and adoption at 90 days. Size this investment to the share of excess churn that implementation actually explains, using the ceiling calculation from earlier. Don't size it to the whole churn problem.

### 5. Invest in product narrowly, not broadly

- **Build the specific capabilities** that the genuine-gap customers named. Those, not a general AI roadmap acceleration.
- **Fund usability and performance fixes** on your existing analytics wherever the abandonment investigation points to failures in production conditions: slow queries, painful setup, or friction with customers' existing workflows.
- **Hold off on broad acceleration of analytics and AI work.** The evidence doesn't support it yet. If implementation or post-go-live adoption is the binding constraint, more features could make things worse by lengthening implementations and increasing complexity.

### 6. Finish the two open tests in parallel (next 30–45 days)

These are cheap, and their results should move budget:

- **Re-run the head-to-head comparison more severely.** Use churned customers' actual use cases, realistic messy data, and typical users rather than experts. Measure setup effort and time to first useful insight, not just whether the outputs match.
- **Reconstruct why each account abandoned the analytics.** Look at errors, query performance, configuration state, data-discrepancy tickets, version, staff turnover, and whether anyone engaged with them after go-live.

Also complete the mix-versus-rate breakdown from earlier. It tells you how much of the doubling came from more customers being poorly implemented and how much from churn rising within both groups.

## Commit in advance to what would change the plan

Write these down now and get both VPs to agree to them:

| If we find… | Then we… |
|---|---|
| The rescue program revives usage and reduces risk | Scale it to all accounts past go-live and make it a permanent function |
| Treated accounts abandon again despite the help | Shift budget from services toward usability and performance work on existing analytics |
| The severe re-test reveals a real production gap versus the competitor | Prioritize fixing the existing analytics module over building new features |
| Switchers do *better* with the competitor's analytics in production | Take the product-gap conjecture seriously again and investigate what they do differently |
| Most of the churn increase is mix shift | Treat services capacity and sales pacing as the main lever |
| Churn rose across all segments at once | Look for a cross-cutting cause, such as pricing, consolidation, or budgets, before spending more on product or services |

## Watch leading indicators, not churn

Annual churn tells you about a decision 12 months after it's too late to change it. Track these instead:

- time to go-live
- analytics adoption depth at 90 days and 6 months
- re-adoption rates among rescued accounts
- the rate at which accounts drop analytics after first use
- competitive losses to this specific rival

Review the plan at **90 days** against the pre-committed criteria, and again at **6 months**. Expect to change parts of it. That is the method working, not the plan failing.

## In one sentence

Stop arguing about product versus service, make one person responsible for whether customers get value after go-live, rescue at-risk accounts while testing whether that rescue works, defend against the one competitor, fix implementation and product only to the extent the evidence supports, and decide in advance what results would make you change course.

## Outcome summary (sent to Jev)

Neither VP's belief holds as stated. The best-surviving explanation is that churn comes from three separate failures. Poor implementation drives a bounded but real share. A value-in-production gap after go-live leaves customers who try the analytics unable to get value in real conditions, so they abandon it, and no one owns preventing this. A narrow genuine capability gap is being exploited by one competitor. The reasons are that well-implemented customers churn at half the rate of poorly implemented ones yet still above baseline, and that half the feature complaints concern analytics that matches the competitor's in controlled comparison.

The first step is to end the either/or debate and give one person responsibility for sustained post-go-live value, measured by analytics usage, adoption depth at 6 and 12 months, and renewals. Next, run a rescue program on at-risk accounts that shows the abandonment pattern: configure dashboards, fix data-quality problems, and assign a named owner, with a control group to test whether the rescue works. At the same time:

- Defend proactively against the one competitor, offering production-realistic evaluations.
- Fix implementation with fixed-scope, time-boxed rollouts and a 90-day value milestone. Check whether sales volume has outrun services capacity, and size the investment to implementation's share of churn.
- Build only the specific missing capabilities and the usability and performance fixes the evidence supports, not a broad AI acceleration, which could worsen churn.

Three tests still need finishing: a more severe head-to-head re-test, reconstruction of each abandonment, and a mix-versus-rate breakdown.

Both VPs should pre-commit to results that would change the plan. The plan should track leading indicators rather than annual churn and be reviewed at 90 days and 6 months. Because the ownership function favors customer success, it should be tested hardest.
