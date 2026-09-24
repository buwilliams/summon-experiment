# churn-cause/testC

Model: claude-opus-5-5 · 2026-09-24T14:05:17.351341+00:00

## Turn 1

**User:** Use the method of conjectures and refutations (critical rationalism) to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Diagnosing Your Churn by Conjecture and Refutation

## Short answer

Neither belief can be declared right yet, and choosing between them by argument would be a mistake. They are **two conjectures**, and they make **different predictions** about data you already have. The critical-rationalist move is to:

1. State what would refute each one.
2. Look hardest for evidence that would kill them.
3. Keep whichever survives, provisionally.

The comparison can be run in a few weeks, mostly from existing data. Below is how.

---

## 1. Restate the beliefs as falsifiable conjectures

A conjecture is useful only if it forbids something. Vague versions ("product matters," "experience matters") can't be wrong, so they can't teach you anything.

**C1 (Product gap):** Customers leave because competitors' analytics/AI capabilities exceed ours. Churners had working, adopted implementations and still left for a better product.
- *This conjecture forbids:* well-adopted customers churning at the same rate as poorly adopted ones for reasons unrelated to features, and churners leaving for competitors *without* stronger analytics/AI.

**C2 (Implementation/service):** Customers leave because long implementations and weak support keep them from reaching full value.
- *This conjecture forbids:* customers who reached full value churning at high rates, and churn being unrelated to implementation duration, adoption depth, or support experience.

## 2. Add rival conjectures

Popper's warning: the most dangerous error is testing only the hypotheses you walked in with. Notice also that each VP's theory points to the other VP's budget being the solution. That doesn't make either wrong, but it is a reason to test severely.

Plausible rivals for *regional insurance carriers*:

- **C3 (Market consolidation):** Regional carriers are being acquired or merged. The acquirer standardizes on its own claims system. The "churn" is really logo loss from M&A.
- **C4 (Suite bundling):** Core-platform vendors (policy/billing/claims suites) are bundling claims with deals you can't match. Carriers leave for integration and a single vendor, not for AI features.
- **C5 (Price/economic pressure):** Carriers under loss-ratio pressure are cutting costs, or a pricing or renewal-term change 18–24 months ago triggered re-evaluations.
- **C6 (Cohort/contract timing):** A large cohort signed 3–5 years ago is hitting renewal simultaneously. The underlying churn *propensity* may not have changed much.
- **C7 (Something broke internally):** Loss of experienced CSMs or implementation staff, a switch to an implementation partner, a disruptive release, or a support reorganization.

**A key clue:** churn *doubled* over a defined window. Gradual product obsolescence usually produces gradual erosion. A doubling suggests something *changed*. Examples:
- A competitor shipped something (C1).
- Your delivery capacity degraded (C2, C7).
- The market shifted (C3, C4, C5).

Build a timeline of events from roughly 12–30 months ago before anything else.

## 3. Derive discriminating predictions

Evidence both conjectures predict (e.g., "churned customers were unhappy") is useless. Look for places where they **disagree**:

| Observable | C1 (Product) predicts | C2 (Service) predicts |
|---|---|---|
| Adoption depth of churners before exit (modules live, active users, claims volume in system) | High; they used it fully, then left | Low; never reached full use |
| Churn rate by implementation duration/cohort | Flat across implementation length | Rises sharply with long or troubled implementations |
| Churn among customers who reached "full value" milestones | Still elevated | Low |
| Where churners went | Competitors with stronger analytics/AI | Anywhere, including simpler competitors, suites, or in-house/legacy |
| Features cited in exit reasons | Features you genuinely lack | Often features you *already have* but they never deployed |
| Support tickets/CSAT in final 12 months | Unremarkable | Elevated escalations, low CSAT, long resolution times |
| New-logo win/loss vs. same competitors | Win rate also falling, losses cite AI/analytics | Win rate stable (prospects haven't felt the implementation pain yet) |
| Which customers churn | Larger, more sophisticated carriers wanting advanced analytics | Customers with thin internal IT, complex integrations, or particular implementation teams |

Two of these tests are especially severe because they draw on **independent evidence**:

- **The "features we already have" test.** Take the feature gaps churners cited and check them against your actual product. If a large share already exists in some form, C1 takes a heavy hit and C2 gains. Poor implementation often *masquerades* as product gaps.
- **The new-business test.** Prospects evaluate you before experiencing your implementation. If you're losing competitive deals on analytics/AI too, that corroborates C1 in a way C2 cannot explain. If new-logo win rates are healthy, C1 is weakened as the main driver.

Checks for the rivals:
- **C3:** Tag every churned account for M&A activity.
- **C4:** Record the destination vendor for every churned account.
- **C5:** Map churn against any pricing changes.
- **C6:** Compare the churn *rate per renewal opportunity* with the raw count.
- **C7:** Break churn down by implementation team, CSM tenure, and the release timeline.

## 4. Guard against weak evidence

- **Exit-interview reasons are the least trustworthy data.** "Your competitor has better AI" is a polite, face-saving reason. "Your implementation failed us and we gave up" is awkward to say. Weight *behavior* over *stated reasons*: adoption logs, ticket history, destination vendor, timing.
- **Write refutation criteria before you look.** Get both VPs to agree up front. For example:
  - "If churned customers had adoption at or above the retained-customer median, C2 is substantially refuted as the primary cause."
  - "If fewer than a third of churners went to vendors with materially stronger analytics/AI, C1 is substantially refuted as the primary cause."
  
  This prevents after-the-fact reinterpretation, which is how both theories could "survive" any data.
- **Expect a mixed answer, but make it specific.** "Both matter" is unfalsifiable and unactionable. A useful mixed answer sounds like: "Among fully adopted accounts, churn is driven by X. Among poorly adopted accounts, by Y. The split is 70/30."

## 5. What to do

**Weeks 1–3: Churn autopsy.** For every churned account in the last 18–24 months, plus a matched sample of retained accounts, pull:
- Implementation duration vs. plan
- Go-live scope vs. contracted scope
- Adoption metrics
- Support/CSAT history
- Destination vendor
- M&A status
- Renewal timing
- Pricing changes
- Cited reasons, cross-checked against actual product capability

Run the discriminating comparisons above. Also pull competitive win/loss from sales.

**In parallel: a causal test on the service conjecture.** Correlation between low adoption and churn could run either way. A weak product might *cause* low adoption. So:
1. Take currently at-risk accounts with low adoption.
2. Randomly assign half to an intensive value-realization intervention: re-implementation of unused modules, executive business review, dedicated support.
3. Track renewal intent, adoption, and eventually renewal against the other half.

If the intervention measurably lifts retention, C2 is corroborated causally. If adoption rises and customers still leave, C2 is refuted as sufficient and C1 gains weight.

**For the product conjecture:** Present your roadmap's analytics/AI capabilities (demos, early access) to at-risk accounts and to churned customers willing to talk. Ask one concrete question: would these have changed your decision? Stated intent is weak evidence, but a firm "no, the problem was never features" is a meaningful refutation signal.

**Low-regret moves while you test.** These are sensible under almost any surviving conjecture:
- Instrument time-to-value and adoption as leading churn indicators, if you haven't already.
- Stop any bleeding in active implementations that are running over plan.
- Avoid large irreversible bets (a major roadmap reprioritization *or* a big services headcount expansion) until the autopsy is done. It's a few weeks.

**Decision rules once evidence is in:**
- **C2 survives, C1 is refuted:** Fund implementation and onboarding redesign. Measure it by time-to-value and adoption, and hold the roadmap roughly steady.
- **C1 survives, C2 is refuted:** Accelerate the specific capabilities cited by *adopted* churners and competitive losses. Don't build a generic "AI" program.
- **A rival survives (M&A, suite bundling, pricing):** Neither VP's plan addresses it. You may need partnerships, integration work, pricing changes, or acquirer-account playbooks.
- **Segment-specific answer:** Allocate by segment share of lost revenue.

## 6. Hold the conclusion provisionally

Whatever survives is the *best current explanation*, not the truth. Set up ongoing monitoring that could refute it later, such as quarterly churn autopsies and a live adoption-vs-churn dashboard. Revisit if the data shifts. Churn drivers change as the market changes, especially in a consolidating, AI-hyped sector like insurance tech.

**My prior, stated so it can be refuted:** The "features we already have" pattern shows up often enough in enterprise software that I'd give C2 a slight edge. That goes double if your churners show low adoption and your new-logo win rates are holding up. But I'd also tag every lost account for M&A before trusting either VP. Regional carrier consolidation could be quietly explaining a large share of the doubling. Let the autopsy prove me wrong.

## Turn 2

**User:** We pulled some early numbers: churned accounts had roughly the same adoption as retained ones, but about 40% of them came through implementations that ran six-plus months late, and around a quarter were acquired by larger carriers. Sticking with the same approach, what does this knock out, what's still standing, and what should we test next?

**Assistant:**

# Round Two: What the Early Numbers Refute

## The headline

- **Knocked out:** The Services conjecture *as originally stated*: customers leave because they never reach full value.
- **Corroborated:** Market consolidation (C3) is real and material. It explains a large chunk of churn that neither VP's plan addresses.
- **Still standing but unproven:** The Product conjecture (C1). It survived, but only because this data didn't really test it.
- **The open question:** What the 40% late-implementation figure means. It is ambiguous until you know the base rate.

Here's the reasoning, and the tests that will resolve what's left.

---

## 1. What's refuted: C2 in its original form

C2 claimed churners *never got to full value*, which meant it predicted **lower adoption among churners**. You found roughly equal adoption. That is the refutation criterion we set in advance. By our own rules, the adoption mechanism is out as the primary cause.

Two cautions keep this honest in both directions:

- **Don't rescue C2 by questioning the metric after the fact.** If "adoption" means logins, it may miss depth (modules live, share of claims volume in the system). It's legitimate to check that you measured what C2 was actually about. But decide *now* which metric counts. Then accept the result whichever way it goes. Reaching for a better metric only because the result disappointed is exactly the immunizing move Popper warns against.
- **Don't treat this as a win for Product.** Refuting C2's mechanism does not establish C1. Equal adoption is *consistent* with C1, since C1 predicted adopted customers leaving anyway. But it's also consistent with M&A, pricing, suite bundling, and several other explanations. A test that many conjectures pass corroborates none of them much.

## 2. What's corroborated: C3, market consolidation

A quarter of churned accounts were acquired. That's a bold, specific prediction that could easily have come back near zero, and it didn't. Three follow-ups sharpen it:

- **Revenue share.** Are acquired accounts a quarter of *lost revenue*, or just of logos?
- **Contribution to the doubling.** If churn went from, say, 8% to 16%, and M&A losses rose from about 1 point to about 4, consolidation explains roughly 3 of the 8 points of *increase*. That's far more important than "a quarter of churn" suggests. Check whether M&A-driven losses grew over the window or were always there.
- **Do acquired accounts ever stay?** If some did, what distinguished them? Possibilities include the acquirer having no claims system, a weak incumbent, your system being better integrated, or relationships at the acquirer.

**Methodological consequence:** M&A churn is structural and largely involuntary. It should be **removed from the sample** before judging C1 and C2. Mixing it in dilutes every signal. All further analysis of product versus service should run on *voluntary* churn only.

## 3. What's ambiguous: the 40% late-implementation figure

On its own, "40% of churners had implementations six-plus months late" tells you nothing. The number that matters is: **what percentage of retained accounts had late implementations?**

| If retained accounts were late... | Interpretation |
|---|---|
| ~40% | No signal. Lateness is just common, and C2 takes another hit. |
| ~15% | Strong association. Late implementations predict churn, even though adoption doesn't. |

This will be tempting for the VP of Services to cite as vindication. Without the base rate it's confirmation, not a test.

### If the association is real: a modified conjecture

If late implementations do predict churn, you'd need a new explanation, because the adoption mechanism is already refuted. Candidate **C2′ (trust/relationship damage):**

> Late implementations don't reduce usage. They damage the relationship. The executive who bought you was embarrassed, the champion left, and the carrier's leadership concluded you're a risky vendor. At renewal, they leave despite using the product.

**Is this a legitimate revision or an ad hoc rescue?** Popper's test: a modified theory is acceptable only if it makes *new, independently testable predictions*, not just if it re-explains the data that sank its predecessor. C2′ passes, because it predicts things you haven't looked at yet:

- Churners from late implementations show more **executive sponsor or champion turnover** during or after implementation.
- They have **worse relationship or NPS scores and more executive escalations**, even with normal adoption.
- They churn disproportionately at **first renewal**, not later. If late-implemented accounts stayed through two or three renewals and *then* left, the causal story weakens badly.
- Their exit reasons emphasize **confidence and vendor risk**, not missing capabilities.

If those predictions fail, C2′ is refuted too, and Services has no surviving mechanism.

### A rival explanation for the same correlation (C8: complexity confound)

Late implementations may simply be a **marker of complex customers**: heavy integrations, legacy core systems, thin internal IT. Complexity itself might drive churn. For example, those customers might be most attracted to suite vendors offering pre-integrated claims (C4).

C8 predicts that:
- Late-implementation churners go disproportionately to **suite vendors**.
- The association **shrinks or vanishes** once you control for integration complexity.

C2′ predicts it persists. That's a clean discriminating test.

## 4. The next round of tests, in priority order

1. **Late-implementation base rate among retained accounts.** Cheap and decisive. Nothing about the 40% can be interpreted without it.
2. **Rerun everything on voluntary churn only,** excluding acquired accounts. Recompute adoption comparisons and late-implementation rates on the cleaned sample.
3. **Decompose the doubling.** Split the change in churn rate into buckets: M&A, voluntary with late implementation, voluntary with on-time implementation. Ask which buckets grew. The one that grew is what you're explaining.
4. **C2′ versus C8 on the late-implementation cohort:**
   - Sponsor and champion turnover
   - Relationship scores and escalations
   - Timing (first renewal or later)
   - Destination vendor
   - Integration complexity as a control
5. **Finally test C1 properly on voluntary, on-time churners.** This residual group is where a product-gap story has its best chance, and where it has a real chance of being refuted. Check three things:
   - **Destination vendor:** do they go to competitors with materially stronger analytics/AI?
   - **The "features we already have" check:** are cited gaps actually missing from your product?
   - **New-logo win/loss against the same competitors:** are you losing new deals on analytics/AI too?

   C1 hasn't faced a severe test yet. Give it one before anyone funds a roadmap acceleration.
6. **M&A deep dive:**
   - Did any acquired customers stay, and why?
   - Which acquirers are active in your segment?
   - Do your contracts have change-of-control terms?

## 5. What to do now, provisionally

- **Start an M&A playbook.** This is the best-corroborated finding, and neither VP's plan touches it:
  - Flag customers likely to be acquired.
  - Build relationships at likely acquirers.
  - Prepare the case for being the consolidated platform rather than the one displaced.
  - Review renewal and change-of-control terms.
- **Keep fixing chronically late implementations, but don't oversell the rationale.** Six-plus-month overruns are worth fixing on cost and sales grounds alone. Just don't claim yet that it will cut churn. That depends on the base-rate test and on C2′ surviving.
- **Still hold off on a major roadmap acceleration.** C1 is standing, but only because it hasn't been properly tested. Survival without a severe test isn't corroboration.

**Where this leaves the original question:** so far, the most important thing the evidence has done is **shrink the territory both VPs are fighting over**. A quarter of churned logos, and possibly a large share of the doubling, belongs to neither of them. The remaining voluntary churn is where the product-versus-service question gets settled, and the next round of tests is built to settle it.

## Turn 3

**User:** Okay, the base rate came back: about 15% of retained accounts had implementations that ran six-plus months late, and after stripping out the acquired accounts, the late-implementation churners mostly left at their first renewal and a noticeable chunk went to suite vendors. Keeping to the same approach, how does that shake out between C2′ and C8, does C1 look any different now, and what's the next test that could actually kill whichever one is still standing?

**Assistant:**

# Round Three: C2′ vs. C8, and Where C1 Stands

## The headline

- **The late-implementation association is real and strong.** Neither C2′ nor C8 is knocked out. Most of the new evidence fits both of them, so it doesn't discriminate between them.
- **They may not be exclusive.** Complexity could cause lateness, and lateness could then cause trust damage. What matters for your decision is whether *fixing lateness would reduce churn*. That question has a clean test.
- **C1's territory has shrunk further, but it still hasn't faced a severe test.** It now has a well-defined arena where it can be.

---

## 1. What the base rate establishes

40% of churners had late implementations versus 15% of retained accounts. That gives an odds ratio of about 3.8. At typical churn rates, late-implemented accounts churn at **roughly three to four times the rate** of on-time accounts. The association is not noise.

One bookkeeping caveat: the 40% was computed *before* removing acquired accounts. Recompute it on voluntary churn only.
- If acquired accounts were mostly on-time, the late share among voluntary churners is *higher* than 40%, and the association is stronger.
- If acquired accounts were mostly late, the association is weaker.

This is unlikely to reverse the finding, but get the number right before it anchors decisions.

## 2. Scoring the two new observations against C2′ and C8

Evidence only counts if one conjecture predicted it and the other forbade it or made it unlikely.

**Leaving at first renewal.** C2′ predicted this explicitly. But first renewal is the *first exit opportunity for anyone*. A complex customer lured by a suite vendor (C8) would also leave at first renewal.
- The discriminating comparison: **do on-time voluntary churners also leave mostly at first renewal?**
  - If yes, timing tells you nothing.
  - If on-time churners leave later and late churners cluster at first renewal, that favors C2′.
- As it stands, C2′ passed a test that C8 would probably also have passed. That's weak corroboration.

**A noticeable chunk went to suite vendors.** C8 predicted this. But C2′ doesn't forbid it. A burned carrier might choose a suite *because* it wants a safer, single-vendor bet after a bad experience.
- The discriminating comparison: **suite-vendor share among late churners versus on-time churners.**
  - A markedly higher share among late churners favors C8.
  - Similar shares mean the destination is about market dynamics, not lateness.
- Also: "a noticeable chunk" isn't most. Find out where the rest went.

**Scorecard:** mild, unconfirmed tilt toward each on one observation. Neither is refuted. This is the point where the temptation is to declare a winner based on which story feels better. Resist it.

## 3. Why the distinction matters

Both could be partly true. The decision question is **causal**: is lateness a *mediator* of churn or just a *marker*?

- **C2′ says the chain is complexity → lateness → trust damage → churn.** Cutting lateness cuts churn.
- **C8 says complexity drives both lateness and churn.** Lateness is a symptom. Fixing it won't move churn much. You'd instead need to:
  - address integration with core systems,
  - partner with or position against suites,
  - or qualify and price complex deals differently.

Same correlation, opposite investment implications.

## 4. The test that can kill one (or both): separate lateness from complexity

You need cases where lateness and complexity *come apart*. Build a 2×2 on your implementation history:

| | **Low complexity** | **High complexity** |
|---|---|---|
| **On time** | Baseline | C8 predicts **elevated** churn; C2′ predicts **baseline** |
| **Late** | C2′ predicts **elevated** churn; C8 predicts **near baseline** | Both predict elevated |

The two off-diagonal cells are where the conjectures make **opposite** predictions:

- **High-complexity, on-time accounts churning near baseline refutes C8 as the main driver.** Complexity alone isn't the problem.
- **Low-complexity, late accounts churning near baseline refutes C2′.** Lateness alone doesn't damage the relationship enough to matter.

### An even sharper version: cause of lateness

Code *why* each implementation was late:

- **Customer-side causes:** scope changes, data quality, customer IT capacity, integration surprises.
- **Vendor-side causes:** your staffing shortages, implementation partner problems, release defects, team turnover.

Vendor-side lateness is close to a natural experiment. It's lateness that complexity didn't cause.
- If vendor-side-late accounts churn at elevated rates, C2′ is strongly corroborated. Trust damage from *your* failures is doing the work.
- If they churn at baseline while customer-side-late accounts churn heavily, C2′ is refuted and C8 is corroborated.

### Rules to keep the test honest

1. **Define complexity before looking at outcomes.** Use measurable features fixed at contract signing, for example:
   - number of integrations,
   - legacy core platform type,
   - lines of business,
   - data migration volume,
   - customer IT headcount.
   
   Don't use implementation duration. That's the thing you're trying to separate from.
2. **Code the cause of lateness blind to outcome.** Whoever reads project records shouldn't know which accounts churned. Otherwise, late churners will "obviously" have been vendor-side failures, or customer-side ones, depending on who's coding.
3. **Write kill criteria in advance.** For example: "If low-complexity, vendor-side-late accounts churn at less than 1.5× baseline, C2′ is refuted as a primary driver."
4. **Check sample sizes.** Some cells may be small. If so, say so, and treat results as suggestive rather than decisive.

### Supporting tests (mechanism checks for C2′)

These were proposed last round and still apply. C2′ also predicts, among late accounts:
- executive sponsor or champion turnover,
- worse relationship scores,
- more executive escalations,

all *despite normal adoption*. If late churners show none of this, C2′'s mechanism is missing even if the 2×2 favors it. You'd then need yet another explanation for why lateness matters.

## 5. A timing test: does lateness explain the *doubling*?

Everything so far explains *which* accounts churn. Your original question was why churn *doubled*. The lateness family (C2′ or C8) makes a risky, specific prediction:

> The share of late implementations rose in the cohorts whose first renewals fell in the last 18 months.

- If late implementations spiked two to three years ago (perhaps from a staffing crunch, a partner switch, or a surge in complex deals), the doubling's timing is explained. You'd also learn whether the spike was vendor-side (C2′) or a shift toward complex customers (C8).
- If the late-implementation rate was flat across cohorts, lateness is a steady-state churn driver, not the cause of the increase. Something else changed.

## 6. How C1 looks now

**Its territory has shrunk.** Roughly:
- a quarter of churned logos were acquired,
- and a substantial share of voluntary churn is tied to late implementations.

What remains for C1 is **voluntary churn among on-time implementations**. That's still potentially a large group, perhaps 40% or so of churned logos depending on overlap, so C1 is far from dead.

**One piece of evidence cuts against it at the margin.** Customers leaving for suite vendors are mostly buying integration and consolidation, not superior AI or analytics. That's weak evidence against C1 *in the late-implementation segment*. Check whether those suites actually do have stronger analytics before leaning on it.

**It still hasn't faced a severe test.** Run these kill tests on the on-time voluntary churners specifically:
- **Destination:** if most went to vendors *without* materially stronger analytics/AI, C1 is refuted for that segment.
- **Features-we-already-have:** if most cited gaps already exist in your product, C1 is refuted and it points to an enablement problem instead.
- **New-logo win/loss:** if you're winning competitive deals against the same vendors at stable rates, C1 is badly weakened.

If C1 survives all three, it earns real corroboration and a real claim on roadmap budget, focused on the specific capabilities cited.

## 7. What to do meanwhile

- **In-flight late implementations approaching first renewal:** start an executive recovery program (sponsor meetings, remediation plans, commercial concessions where warranted). This is low-regret. It also doubles as a test.
  - If you can't randomize for ethical or commercial reasons, stagger the rollout.
  - C2′ predicts the recovered accounts renew at higher rates.
  - C8 predicts little effect.
- **Fixing vendor-side causes of lateness** is justified on cost and sales grounds regardless. Just hold off on promising that it will cut churn until the 2×2 comes back.
- **Continue the M&A playbook.** It remains your best-corroborated finding.
- **Still no major roadmap acceleration.** C1 has a defined arena now. Test it there first.

**Where this leaves the two VPs:** the Services VP's *instinct* (implementation matters) has survived, but their original *explanation* (customers never reach value) was refuted. Whether the surviving version is really about service or about customer complexity is exactly what the 2×2 will decide. The Product VP's conjecture is alive but untested, and it now has a clear, bounded place to be tested.

## Turn 4

**User:** We ran the 2×2: high-complexity on-time accounts churned only slightly above baseline, low-complexity vendor-side-late accounts churned at about 2.5× baseline, and most of the late implementations bunched up in cohorts signed right after we switched implementation partners. Meanwhile, about half of the on-time voluntary churners went to competitors with stronger analytics, but sales says our new-logo win rate against those same vendors has held steady. Sticking with the same approach, where does that leave C2′, C8, and C1, and what would you try to refute next?

**Assistant:**

# Round Four: Where C2′, C8, and C1 Stand

## The headline

- **C8 (complexity) is refuted as the main driver.** It survives only as a minor contributor.
- **C2′ (vendor-caused lateness damages trust) passed its most severe test so far.** Combined with the partner-switch timing, it now offers a strong candidate explanation for the *doubling*, not just for which accounts churn.
- **C1 (product gap) is weakened as an explanation for the doubling.** It survives as a possible steady-state contributor in one segment. Its best new evidence has a base-rate problem.
- **Next:** try hard to kill C2′, which is now the leading conjecture. It needs to face its most severe tests before it drives major decisions.

---

## 1. C8: refuted as the primary driver

C8 predicted that high-complexity, on-time accounts would churn well above baseline. They churned only slightly above it. By the kill criterion set last round, complexity alone is not the engine.

The "slightly above" is worth keeping. Complexity probably adds a modest independent effect, possibly through the suite-vendor pull. But it can't account for a 3–4× churn difference, and it can't account for the doubling. Its policy implications drop accordingly: suite positioning and complex-deal qualification are secondary concerns, not the main fix.

## 2. C2′: severely tested, and survived

This was the cell where C2′ could most easily have died. Low-complexity accounts made late by *your* side had no complexity story to lean on. C2′ predicted elevated churn there; C8 predicted near baseline.
- Result: **2.5× baseline**, well clear of the 1.5× kill threshold.
- Popper's point applies: corroboration counts most when the test was one the theory could genuinely have failed. This was one.

**The partner-switch clustering adds a second, independent corroboration.** Last round's timing prediction was that late implementations would concentrate in cohorts whose first renewals fell in the last 18 months. They did, and there's a concrete cause: the partner switch. This moves C2′ from explaining *who* churns to plausibly explaining *why churn doubled*.

**Corroborated is not proven.** Four gaps remain:

1. **Lateness or partner quality?** The partner switch caused lateness, but it may have caused other damage too: sloppy configuration, poor data migration, bad handoffs, abrasive staff. Those could harm trust independently of timing. Call this rival **C2″ (partner quality)**. It differs from C2′ in one testable way:
   - If on-time accounts implemented by the new partner also churn at elevated rates, the problem is the partner, not lateness per se.
   - If only the new partner's *late* accounts churn heavily, lateness is the mechanism.
   
   The fix differs. Faster timelines won't help if the partner's work is the problem.
2. **The mechanism still hasn't been observed directly.** The sponsor turnover, relationship scores, and escalation data from earlier rounds haven't come back. A causal story whose mechanism is never seen stays vulnerable.
3. **Other changes around the switch.** Cohorts signed right after it may differ in other ways: a sales push, a pricing change, a product release, different customer types. The 2×2 controls for complexity, but not for everything. List what else changed in that window.
4. **Sample size in the key cell.** Low-complexity, vendor-side-late accounts may be a small group. A 2.5× ratio on small numbers is suggestive, not decisive. Check the confidence interval before treating it as settled.

## 3. C1: weakened, but not dead

**Evidence for C1:** About half of on-time voluntary churners went to competitors with stronger analytics.

**Why that's weaker than it looks:** it needs a base rate. What share of your segment's replacement market do those competitors hold?
- If stronger-analytics vendors win about half of all switching deals regardless of reason, then "half went there" is just market share and tells you nothing.
- If they hold 20% of the market but got 50% of your on-time churners, that's real evidence for C1.

**Evidence against C1:** Your new-logo win rate against those same vendors has held steady. Prospects compare features head-to-head. If your analytics gap were decisive, you should be losing more of those deals. You aren't.

**Two caveats before treating this as a refutation:**
- **"Sales says" is not data.** Verify it from CRM records. Check whether deal mix shifted. You might be winning more simple, non-analytics-focused deals while quietly losing the analytics-driven ones. A stable overall rate can hide that.
- **A legitimate C1 variant: C1′ (customers outgrow you).** Prospects may not weigh analytics heavily, while mature customers do after years of use. This counts as a real revision, not an ad hoc rescue, only because it makes new predictions:
  - Analytics-destination churners are longer-tenured than other churners.
  - They were heavy users of your reporting/analytics features.
  - They cited specific capabilities that are *genuinely absent* from your product.
  
  If those predictions fail, C1′ goes too.

**The decisive point about C1 and the doubling:** even if C1 survives, it explains the doubling only if on-time voluntary churn *rose* over the window, or if competitor analytics launches line up with the rise. If on-time voluntary churn stayed roughly flat, C1 is at most a steady-state contributor. It can't be the answer to your original question.

## 4. What to try to refute next

Priority goes to attacking C2′, since it now carries the most weight in your decisions.

**1. Separate partner quality from lateness (C2′ vs. C2″).**
- Compare churn for new-partner on-time accounts with old-partner on-time accounts.
- **Kill criterion for C2′-as-mechanism:** if new-partner on-time accounts churn at 2× baseline or more, the problem is the partner's work, not lateness itself.

**2. Dose-response.**
- Among vendor-side-late accounts, C2′ predicts churn rises with the severity of the delay. A 12-month overrun should do more damage than a 6-month one.
- A flat relationship would be hard for C2′ to explain. It's a risky prediction, which is what makes it useful.

**3. Observe the mechanism.**
- Pull sponsor/champion turnover, relationship scores, and executive escalations for late versus on-time accounts at equal adoption.
- If late churners show no sign of relationship damage, C2′ needs a different mechanism or it's in trouble.

**4. Make an out-of-sample prediction. This is the strongest test available.**
- Everything so far explains the past. Using what you now know, predict first-renewal churn for the next two to four quarters, account by account or cohort by cohort, based on partner, lateness, and complexity.
- **Write it down and timestamp it before the renewals happen.**
- C2′ also predicts that churn should **peak and then fall** as post-switch cohorts cycle through first renewal, provided new implementations are running on time.
- If churn stays elevated after those cohorts pass, something else is going on and C2′ is refuted as the explanation for the doubling.

**5. Watch the recovery-program results.**
- Set the kill criterion in advance: if recovered accounts renew at the same rate as comparable unrecovered ones, C2′'s *actionable* version fails.
- Also decide in advance what that would mean. It could mean trust damage isn't the mechanism, or that it's real but irreversible by renewal time. Settle the interpretation now so you can't choose it after seeing the result.

**6. Close out C1 in its segment.**
- Get the market-share base rate for destination vendors.
- Run the features-we-already-have check on analytics churners.
- Verify the win rate from CRM data, segmented by deal type.
- Check the trend in on-time voluntary churn over the window.
- Test the C1′ predictions: tenure, analytics usage, genuinely missing features.

## 5. What to do now

The evidence now justifies acting with more confidence, though still provisionally:

- **Address the implementation partner problem directly.** Options include remediating, replacing, or bringing critical implementations in-house. This is the best-corroborated lever on churn, and it matches the doubling's timing. Test 1 (C2′ vs. C2″) tells you *what* to fix: timelines, work quality, or both.
- **Prioritize the recovery program by renewal date** for post-switch cohorts that ran late, especially those with first renewals in the next two or three quarters. Under C2′, these are your highest-risk accounts, and the window to act is closing.
- **Keep the M&A playbook running.** It's independent of everything above.
- **No broad roadmap acceleration.** C1 has not been shown to drive the doubling. If it survives the segment tests, fund the *specific* capabilities analytics churners cited, not a general AI push.

## Back to your original question

**Neither VP was right as stated.**

- **Services VP:** the instinct that implementation drives churn has held up well. But the stated reason (customers never reach full value) was refuted early. The best-corroborated cause is narrower and more fixable: **a specific operational change, the partner switch, produced a wave of vendor-caused delays that appear to damage customer trust. Those customers leave at first renewal even when they use the product.**
- **Product VP:** not refuted outright, but so far unable to explain the doubling, and contradicted by stable competitive win rates.
- **Market consolidation:** accounts for a quarter of churned logos, and belongs to neither of them.

That's the current best explanation, not the final word. The out-of-sample prediction in test 4 is where it earns real trust. If you write it down now and the next few quarters of renewals behave as it says, you'll have much stronger grounds for your decisions than any argument between the two VPs could have given you.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

**Bottom line:** Treat this primarily as an **implementation-partner failure that is damaging customer trust**. Fix it at the source, and try to save the accounts it has already put at risk before their first renewals. Handle M&A losses as a separate problem. Hold off on a broad product acceleration.

Build checkpoints into the plan so you'll know quickly if this explanation is wrong.

---

## 1. Save the accounts already at risk (start this week)

This is the most time-sensitive action. Every quarter you wait, more at-risk accounts hit first renewal.

**Owner:** Customer Success, with Services support.

- **Build the at-risk list.** Include post-switch accounts whose implementations ran late for vendor-side reasons. Sort by renewal date, then by ARR.
- **Run an executive recovery play on each, starting with the nearest renewals:**
  - A senior leader contacts the customer's executive sponsor and **explicitly owns the delay**. Under C2′, the damage is to trust, and acknowledgment is part of the repair.
  - Assign a named technical owner and a written remediation plan for any unfinished scope.
  - Offer commercial goodwill where warranted, such as service credits or flexible renewal terms. Size it against the ARR at risk.
- **Keep it measurable without sacrificing revenue.** Don't withhold help from high-value accounts for experimental purity. The rollout will naturally be staggered by renewal date. Compare renewal rates against the historical rate for similar late accounts.
- **Quantify the stakes.** Have Finance calculate the ARR in this cohort. That number sizes how much the recovery effort is worth.

## 2. Fix the source: the implementation partner (decide within 30 days)

**Owner:** VP of Services.

- **Run the C2′-vs-C2″ test first.** It takes a couple of weeks with existing data: compare churn for the new partner's *on-time* accounts with the old partner's on-time accounts.
  - **If the new partner's on-time accounts churn normally,** the problem is lateness. Fix timelines through staffing, SLAs, and escalation.
  - **If they churn at elevated rates,** the partner's work itself is the problem. Replace the partner or bring critical implementations in-house. Faster timelines won't be enough.
- **Before the test comes back:**
  - Audit every in-flight implementation. Flag any running behind plan.
  - Pause assigning new high-value deals to the partner until the audit is done.
  - Tie future partner contracts to on-time delivery.
- **Make lateness a churn signal.** Any implementation more than 30 days behind plan escalates to a named executive. Add implementation delay and sponsor turnover to your account-health score. Report on-time implementation rate monthly, alongside churn.

## 3. Treat M&A losses as a separate program

**Owner:** Customer Success, with Sales.

These losses are a quarter of churned logos, and neither VP's plan touches them.

- Flag customers likely to be acquired.
- Build relationships at the acquirers active in your segment.
- Prepare the case for your platform being the one the combined company keeps.
- Review change-of-control and renewal terms in contracts.
- Study the acquired accounts that stayed. Find out what they had in common and replicate it.

## 4. Keep the roadmap steady and close out the product question

**Owner:** VP of Product, with Sales.

- **Don't freeze or accelerate the roadmap.** Keep normal cadence. The evidence doesn't show product gaps driving the doubling.
- **Finish the C1 tests within about 30 days:**
  - What share of the replacement market do the stronger-analytics competitors hold?
  - Are the features analytics churners cited actually missing from your product?
  - Does the win rate hold up in CRM data, broken down by deal type?
  - Did on-time voluntary churn rise over the window?
  - Do the "customers outgrow you" predictions (C1′) hold?
- **If C1 survives,** fund the *specific* capabilities that churners and lost deals cited. Don't launch a general AI program.

## 5. Write down your prediction (this month)

**Owner:** You, with RevOps.

- Using partner, lateness, and complexity, forecast first-renewal churn for the next four quarters.
- Share it with the executive team as a dated forecast.
- The plan assumes churn will peak as post-switch cohorts renew, then fall. For that to happen, new implementations must run on time and recovery efforts must save some accounts.

This forecast doubles as your budget case and your most rigorous test of the explanation.

## 6. Decide in advance what would change the plan

Agree on these with both VPs now, so no one reinterprets results later:

| Checkpoint | If you see this... | ...then change course |
|---|---|---|
| ~30 days | New partner's on-time accounts churn at 2× baseline or more | The problem is partner quality. Replace or insource, not just faster timelines. |
| ~30 days | C1 passes the segment tests | Add targeted analytics investment for that segment. |
| ~90 days | Recovered accounts renew no better than comparable unrecovered ones | Shift money from recovery to prevention and accept losses in that cohort. |
| 2–4 quarters | Churn stays elevated after post-switch cohorts have renewed | The explanation is wrong or incomplete. Reopen the investigation, with C1 and new rivals. |
| Ongoing | Implementations stay late after the partner fix | The fix failed. Escalate before the next cohort's renewals. |

## 7. Handling the two VPs

Don't frame this as one VP winning.

- **The VP of Services** was right that implementation drives churn, but the cause is narrower than they said. They should own the partner fix and the recovery program, jointly with you.
- **The VP of Product** owns closing out the product question. If the tests show a real gap, they get targeted investment.
- **Review the checkpoints monthly, together.** Both of their original conjectures had to change in response to evidence. Say so openly. That's what keeps the next disagreement a question of testing rather than advocacy.

---

## In one sentence

**Save the late post-switch accounts before their first renewals, fix or replace the implementation partner, run M&A as its own program, keep the roadmap steady while closing out the product question, and write down a forecast that will tell you within a few quarters whether you've got it right.**

## Outcome summary (sent to Jev)

The assistant recommends treating the churn increase mainly as an **implementation-partner failure that damages customer trust**. It advises fixing that failure at the source, saving already-endangered accounts before their first renewals, handling M&A losses separately, and holding off on any broad product acceleration.

**Reasons**
- Churned and retained accounts had similar adoption, so the "never reached full value" explanation fails.
- Vendor-caused delays on low-complexity accounts produced about 2.5× baseline churn. Complexity alone added little.
- Late implementations clustered in cohorts signed right after the partner switch, which matches the timing of the doubling.
- About a quarter of churned logos were acquired, a loss neither VP's plan addresses.
- Steady new-logo win rates against analytics-strong competitors weaken the product-gap story as the cause of the doubling.

**Actions**
- **At-risk accounts:** Customer Success builds a list of late post-switch accounts sorted by renewal date and ARR. It then runs executive recovery plays: explicit ownership of the delay, remediation plans, and commercial goodwill where warranted.
- **Partner diagnosis:** Within 30 days, Services compares the new partner's on-time accounts against the old partner's. The result decides between fixing timelines and replacing or insourcing the partner.
- **Implementation controls:** Audit in-flight work, pause high-value assignments to the partner, and add delay and sponsor turnover to health scores.
- **M&A:** Run a separate acquisition playbook.
- **Product:** Keep the roadmap at normal cadence while finishing the product tests, and fund only specific cited capabilities if a real gap appears.
- **Forecast:** Write down and date a four-quarter churn forecast.

**Caveats**
The conclusion is provisional. Kill criteria should be agreed in advance with both VPs. Churn that stays elevated after the post-switch cohorts renew would mean the explanation is wrong or incomplete. Recovery that fails to lift renewals should shift spending toward prevention. Neither VP should be framed as having "won."
