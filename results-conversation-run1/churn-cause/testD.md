# churn-cause/testD

Model: claude-opus-5-5 · 2026-09-24T14:09:42.472487+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

**Assistant:**

# Testing Two Churn Hypotheses (and a Few Others)

I can't tell you which belief is right from what you've described, and anyone who claims to is guessing. What I can do is make each belief precise enough to fail, then show you how to find out quickly, mostly with data you already have.

## The constraint both beliefs must satisfy

Your key fact isn't "churn is high." It's **"churn doubled over 18 months."** Any explanation has to account for a *change*, not a level.

- **Product-gap** has a natural answer: the AI and analytics wave hit the market in roughly that window, and competitors shipped. But that only helps if you can name the specific competitor releases and show that the churn curve bends after them.
- **Services** has a harder problem. "Our implementations are painful" describes a standing condition. If they were equally painful three years ago, the pain can't explain the doubling. The Services VP needs to name what got *worse*: implementation team attrition, a sales push that brought in more complex carriers, a new product version that's harder to deploy, a support reorganization, longer queues.

Ask each VP to answer this in writing first: *"What changed ~18–24 months ago that your explanation says caused this?"* A vague answer is your first sign of an easy-to-vary theory.

## What each conjecture actually claims

**Product-gap:** Customers who are successfully using the product compare it to competitors, find it lacking in analytics or AI, and switch. The causal chain runs: competitor capability → customer perceives gap → switch.

**Services:** Customers never reach the value they bought. The product may be adequate, but they never get there. When renewal arrives, they have no sunk success to defend, so they leave. The causal chain runs: long or failed implementation → low adoption → weak value at renewal → churn.

These make different claims about **who** churns, **when**, **where they go**, and **when they started looking**.

## Discriminating predictions

| Observation | If Product-gap is true | If Services is true |
|---|---|---|
| **Churn among fully implemented, high-adoption accounts** | Elevated. Competitor AI tempts healthy customers too, and sophisticated users may hit the ceiling first. | Near historical baseline. Well-implemented customers mostly stay. |
| **Churn among slow or failed implementations** | Elevated, but not much more than among healthy accounts. | Strongly elevated. This is where the churn concentrates. |
| **Timing** | Spread across contract ages, tracking competitor launches. | Concentrated at first renewal. |
| **Where churners go** | Mostly to specific competitors with the AI and analytics features. | Mixed destinations: any competitor, back to legacy systems, in-house tools. They're fleeing, not chasing. |
| **When they started looking** | After a period of stable use, often triggered by a competitor demo. | During or soon after a troubled implementation. |
| **New-logo win rate** | Also falling. A product gap hurts acquisition as well as retention. | Roughly stable. The demo sells fine; delivery fails. |
| **Pre-churn signals** | Feature requests for analytics or AI, competitor mentions in QBRs. | Implementation delays, escalations, low login and module usage, CSM or champion turnover. |

The two most diagnostic cells are the first row and the new-logo row.

**The single most decisive cut is churn rate among customers who implemented well.**
- If those accounts are churning at roughly double their old rate, Services cannot be the primary explanation. Good onboarding didn't protect them.
- If they're retaining at historical rates while competitor AI is equally available to them, the strong form of Product-gap is in serious trouble. The features exist, and your healthy customers aren't leaving for them.

**Win rates act as a cross-check.** If you're losing more competitive deals on analytics or AI, that's independent evidence for a real product gap. Implementation pain can't affect deals that never reached implementation.

## Where each explanation is easy to vary

Both theories have escape hatches you should close before looking at data.

**Product-gap escape hatches:**
- "Competitors have better features" is always true of some feature. You can retrofit a gap onto any lost account.
- Exit interviews overweight features. "Your product lacks X" is the socially easy, blame-free reason to give a vendor. "Your team frustrated us for 14 months" is awkward to say. So "they cited features" is weak evidence unless it's specific.
- If healthy customers stay, the fallback is "they'll leave eventually." That's unfalsifiable on any useful timescale.
- **To make it hard to vary:** name the specific capabilities and the specific competitors, and predict that churn concentrates toward those competitors among accounts that used the relevant parts of your product.

**Services escape hatches:**
- "Never got to full value" is dangerously circular: they left, so evidently they didn't get value. Any churner fits unless "full value" is defined *before* you look.
- If well-implemented accounts churn, the fallback is "their implementation wasn't really good, or support failed later." That stretches to cover everything.
- **To make it hard to vary:** define implementation success operationally now. For example: go-live within X days of plan, Y% of purchased modules in production use, Z active adjusters. Then predict that churn concentrates below that line.

## The cheapest tests

With regional carriers, your churned-account count is probably dozens, not thousands. Statistics will be weak, but you can investigate every account individually, which is actually an advantage.

**1. Pre-register predictions (1 hour).** Have each VP write down, before seeing the data, what churn rate they expect in each segment and where churners went. This is the most important step. It stops both theories from absorbing whatever results come back.

**2. The 2×2 (a few days, existing data).** Take every account that came up for renewal in the last 18–24 months. Classify it by implementation outcome, using the pre-committed definition, and by renewal result. Compare churn rates across the cells, and against the same cut for the prior period.

**3. Destination audit (a few days).** For each churned account, find out what they moved to. Sales and CSMs usually know, or can find out with one call. The pattern you're looking for is concentration toward AI-capable competitors versus scattered exits.

**4. Decision-timeline interviews (2–3 weeks).** Have someone neutral, ideally a third party and not the account's CSM, call 10–15 churned customers. Don't ask why they left; that invites the socially easy answer. Instead ask:
- When did you first start considering alternatives?
- What was happening at that moment?
- Who pushed for the change?
- What did the replacement promise that you weren't getting?

"We started looking eight months into implementation" and "we were happy until their rep showed us the AI triage tool" point in opposite directions.

**5. Competitive win/loss (existing CRM data).** Has the loss rate on competitive deals, and specifically losses citing analytics or AI, changed over the same window?

Most of this needs no new build, no survey program, and no roadmap decision. It could be done in about three weeks.

## Third explanations worth testing

Several alternatives fit "churn doubled in 18 months" as well as either VP's story, and some would be refuted or confirmed by the same data.

**1. Carrier consolidation.** Regional insurers get acquired, and the acquired carrier migrates to the parent's system. That churn has nothing to do with your product or services.
- *Test:* check whether any churned accounts were acquired or merged. Cheap, and potentially large.

**2. A contract-cohort effect.** If you had a sales push three or so years ago on multi-year contracts, a wave of renewals is landing now. A bigger denominator plus a batch of possibly poor-fit customers can double observed churn without anything getting worse.
- *Test:* plot churn by signing cohort, not calendar period. Also check whether the renewal volume itself spiked.

**3. A sales-fit shift.** Pressure to grow may have pulled in carriers who are too small, too complex, or on the wrong core systems. That would look like implementation pain, but the cause sits upstream in qualification. Fixing onboarding wouldn't fully help, and neither would features.
- *Test:* compare churners and retainers on firmographics at the time of sale.

**4. Price or packaging changes.** Did renewal pricing, discounting policy, or bundling change in the window?

**5. The interaction hypothesis.** This may fit better than either pure story. Poorly implemented customers have no value to defend, so they're the ones who take the competitor's AI demo seriously. Churners would cite features, and the product VP would hear that. But the churn would still concentrate among weak implementations, which the services VP would see. Both VPs would be observing real but partial signals. This hypothesis makes its own sharp prediction:
- Competitor-driven churn concentrates among poorly implemented accounts.
- Healthy accounts hear the same pitches and stay.

If that's the pattern, the implication is specific. Shipping AI features onto a product customers haven't adopted won't retain them. Time-to-value is the lever, and features matter mainly for new-logo competitiveness.

## What to do now

1. **Don't pick a side yet.** Both remedies are expensive and slow. Choosing wrong costs you a year.
2. **Run the three-week diagnostic above**, with written predictions from both VPs first.
3. **Check consolidation and contract cohorts first.** They're the fastest checks and could explain a large share of the doubling on their own.
4. **In the meantime, do what's robust to every hypothesis:** identify upcoming renewals with weak implementation or adoption signals and run save plays on them. That helps under every explanation, and it generates more evidence as you go.
5. **Let the results decide.**
   - Healthy accounts churning to AI competitors, and win rates falling: accelerate the roadmap.
   - Churn concentrated in failed implementations, with destinations scattered: fix onboarding first.
   - The interaction pattern: fix time-to-value for retention, and treat features as an acquisition investment.

The belief that survives isn't the one either VP argues best. It's the one that made a risky, specific prediction beforehand and didn't fail.

## Turn 2

**User:** Your decisive test sorts accounts by whether they "implemented well," but couldn't that cut favor Services no matter the true cause? A customer who has quietly decided to switch for a competitor's AI would also let adoption slide in the months before renewal, and well-resourced, well-fit carriers are both easier to implement and less likely to leave for any reason. How would we fix the implementation-success measurement at a point early enough that it can't be an effect of the decision to leave, and what result from the 2×2 would the interaction hypothesis actually forbid, so it isn't just absorbing whatever pattern shows up?

**Assistant:**

You're right on both counts. As I framed it, the 2×2 was biased toward Services in two ways, and it couldn't separate the interaction hypothesis from pure Services at all. Here is how to repair both.

## Problem 1: Reverse causation

A customer who has decided to leave stops investing in the product, so adoption measured near renewal is partly an *effect* of the decision. That contaminates the cut.

**Fix: grade implementation at a fixed early milestone, using process records rather than enthusiasm.** Freeze each account's grade at go-live plus 90 days, or at the planned go-live date if it slipped. That is typically well over a year before first renewal. Use measures generated by your own delivery process, which a customer's private intentions can't easily move:

- Days late versus the go-live date in the signed plan
- Contracted scope actually delivered at go-live
- Escalations, change orders, and implementation PM swaps during delivery
- Whether go-live happened at all by the milestone

Pull these from records timestamped at the time: project plans, ticket history, SOW amendments. Don't reconstruct them from memory. Memory will be colored by knowing who left.

**Then check the ordering account by account.** Your decision-timeline interviews ask when each churner started looking. Two cases need handling:

- **Search began before the snapshot, triggered by implementation pain.** That isn't contamination. It's the Services mechanism working as claimed, so the account stays in.
- **Search began before the snapshot, triggered by a competitor.** Their early grade might reflect disengagement. Flag these accounts and run the analysis with and without them.

**Use the calendar as a natural experiment.** Some accounts finished implementation *before* competitor AI features existed. Their grades cannot be effects of AI temptation. If the early grade predicts churn in that subset, reverse causation isn't producing the result.

**Measure trajectory, not just the grade.** For accounts graded well at the snapshot whose usage later declined, date the decline. Declines that follow competitor launches or logged competitor contact support Product. Declines that follow a support failure, CSM turnover, or a champion leaving support a Services variant. Here the timing of disengagement becomes evidence rather than contamination.

## Problem 2: Confounding by customer quality

Well-resourced, well-fit carriers are easier to implement and less likely to leave. So "good implementation" may just be a marker of "good customer."

**Fix 1: measure fit at the time of sale and compare within strata.** Record carrier size, IT staff available to the project, core-system and data readiness, integration complexity, and number of lines of business. All should be taken from sales-stage records, not later assessments. Then ask whether implementation grade still predicts churn *among similar carriers*. With dozens of accounts this will be crude, perhaps just a high-fit/low-fit split, but crude is fine for a large effect.

If the grade's predictive power disappears within strata, that result points to the sales-fit explanation. Poor-fit customers churn regardless of how implementation goes. Fixing onboarding won't help much, and neither will features. Qualification is the lever.

**Fix 2: find variation in implementation quality that the customer didn't cause.** This is the stronger test. Look for sources such as:

- Which implementation team or PM was assigned, often driven by availability rather than customer traits
- Whether the project ran during a staffing crunch or attrition wave
- Whether a buggy release landed mid-implementation
- Partner-led versus in-house delivery, if assignment wasn't based on account difficulty

Suppose similar carriers churn at different rates depending on which team they drew, or whether they implemented during a bad quarter. That is causal evidence for Services that customer quality can't explain. Suppose instead those accidents don't matter while fit does. Then Services loses its causal claim, even if the raw correlation looks strong.

**The confound also cuts the other way, and that gives you a discriminator.** Product-gap predicts that sophisticated, well-resourced carriers with analytics teams are the *most* tempted by competitor AI, and the most able to switch. So the hypotheses disagree about the high-fit, well-implemented cell:

- **Product-gap:** among the most at risk
- **Services:** the safest accounts you have

## Problem 3: What the interaction hypothesis forbids

As I stated it, the interaction hypothesis could absorb almost anything. The 2×2 alone can't separate it from pure Services, because both predict churn concentrated among poor implementations. It needs to be sharpened until it prohibits outcomes.

**Precise statement:** Competitor AI is the *proximate trigger* of the churn increase. It works only on accounts that lacked established value, as judged by the early grade.

This commits it to three things beyond the 2×2:

- **A time dimension.** The rise begins after competitor AI reached your market.
- **A destination.** Churners go to AI-equipped competitors.
- **A trigger.** Searches start after competitor contact.

So the right design is a difference-in-differences. Compare the change in churn rate from before competitor launches to after, in poorly versus well-implemented accounts. Then check destinations and triggers.

### Results the interaction hypothesis forbids

1. **Parallel rises.** If churn rose by a similar amount in both cells, the competitor effect doesn't depend on implementation. That's Product-gap plus a baseline Services effect, not an interaction.
2. **A larger rise in the well-implemented cell.** That pattern is Product-gap, possibly the ceiling effect among sophisticated users.
3. **A rise in the poor cell with scattered destinations.** If poor implementations are churning more but going to legacy systems, in-house tools, or non-AI competitors, competitor AI isn't the trigger. That's pure Services.
4. **Poor-cell searches that began during implementation with no competitor involvement.** Same verdict: pure Services.
5. **A rise among poor implementations where AI competitors aren't present.** If some regions, lines of business, or carrier sizes see little competitor AI selling, the hypothesis predicts poor implementations there did *not* get worse. A rise there refutes it.
6. **High poor-cell churn before competitor launches, with no increase after.** Then competitor AI explains none of the change.

### How the patterns map to the hypotheses

| Pattern in the data | Pure Product | Pure Services | Interaction | Sales-fit |
|---|---|---|---|---|
| Churn rise concentrated in poorly implemented accounts | Forbids | Requires | Requires | Allows |
| Similar rise in well-implemented accounts | Requires | Forbids | Forbids | Allows |
| Churners go mostly to AI-equipped competitors | Requires | Forbids | Requires | Allows |
| Rise begins after competitor launches | Requires | Allows, only if it names a coincident internal cause | Requires | Allows, via cohort timing |
| Grade predicts churn within fit strata | Allows | Requires | Requires | Forbids |
| Poor implementations churn more where AI competitors are absent | Forbids | Allows | Forbids | Allows |

Now every hypothesis has at least one cell it forbids. That's what makes the diagnostic worth running.

The remaining weak spot is **Pure Services on timing**. It survives a rise that begins after competitor launches only if it names an internal cause that happened at the same time, such as team attrition or a harder release. Make the Services VP name that cause before you look. Otherwise "something got worse around then" becomes the escape hatch.

## Revised procedure

1. **Pre-register.** Each VP fills in the table above for their hypothesis, including expected rates per cell and the concurrent cause they're relying on.
2. **Freeze early grades** from time-stamped delivery records at go-live plus 90 days.
3. **Record fit at sale** for every account.
4. **Date the competitor exposure:** market launches, plus logged competitor presence per account.
5. **Run the difference-in-differences**, stratified by fit, with and without accounts flagged for early competitor-triggered disengagement.
6. **Check destinations and search triggers** for every churned account.
7. **Look for accidental variation** in team assignment and delivery conditions.

With small numbers, treat the rates as a rough guide. Weight the account-level evidence heavily: grade timing, trigger, destination. A dozen well-documented churn stories that all show the same ordering of events will tell you more than a p-value on thirty accounts.

## Turn 3

**User:** Several of your "forbids" cells depend on churners going to AI-equipped competitors, but if nearly every serious competitor now markets some AI or analytics feature, a customer fleeing a bad implementation would land at an AI-equipped vendor anyway. So doesn't destination stop discriminating Services from Product and the interaction hypothesis? What observable could we record, ideally from the replacement vendor's contract scope, the churner's evaluation criteria, or what they actually deployed after switching, that would show whether the AI capability *pulled* them rather than just happening to be there?

**Assistant:**

Yes, you're right. If essentially every serious competitor markets AI, then "went to an AI-equipped vendor" is true of nearly every churner under every hypothesis. Evidence only discriminates if it is more likely under one hypothesis than another, so as I framed it, destination tells you almost nothing.

Two repairs are needed:

- **Separate two questions I blurred.** *What triggered the search?* is different from *what decided the selection?* AI can be incidental to either one.
- **Look for behavior a pain-driven switcher would have no reason to produce.** That means relative choices, costly commitments, and revealed priorities, not the mere presence of AI.

## Trigger versus selection

The three hypotheses make different claims about each stage:

| | Search triggered by | Selection decided by |
|---|---|---|
| **Pure Product** | Competitor AI, among satisfied or healthy accounts | AI capability |
| **Pure Services** | Implementation or support pain | Delivery credibility, price, fit. AI is incidental. |
| **Interaction** | Competitor AI, but only among accounts without established value | AI is often the stated reason, but the account's value deficit is what made it persuasive |

The decision-timeline interviews and early grades from before address the trigger. What follows addresses selection, and specifically whether AI pulled.

## Observables that show pull

### 1. The "already had it" test

This is probably your sharpest discriminator. Take each churner's must-have requirements, from their RFP, requirements list, or interview. Classify every requirement into one of three groups:

- **(a)** Capabilities you lack
- **(b)** Capabilities they bought from you but never deployed
- **(c)** Capabilities they deployed

What each hypothesis predicts:

- **Pure Services:** heavy in (b). They are re-buying what they paid you for and never got live. This pattern is hard for Product-gap to explain. If the gap were real, the requirements would sit in (a).
- **Product:** heavy in (a), specifically AI and analytics items.

A churner whose "AI requirements" turn out to be analytics modules you already licensed to them is strong Services evidence, however they described their reasons.

### 2. Relative destination against a base rate

Destination stops discriminating when the question is "AI or not." It starts discriminating again when the question is "AI leader or AI laggard, compared to what the market would predict."

1. Rank the competitors your churners chose by AI and analytics strength.
2. Compare your churners' destination shares to those competitors' share of new regional-carrier deals generally. Your win/loss data and analyst reports give a rough baseline.

If AI leaders take a disproportionate share of your churners, that is pull. If churners distribute roughly like the market, or tilt toward vendors known for delivery, service, or fixed-price implementation, then AI was just present.

### 3. The shortlist and elimination reasons

Ask which vendors were considered and **why each one was eliminated.** Elimination reasons are specific and are less subject to after-the-fact rationalization than "why did you choose X."

- **Pull:** vendors strong on service but weak on AI were eliminated for AI weakness. Or they were never considered because AI was a gate.
- **Push:** vendors were eliminated for implementation risk, references, or price. The winner was middling on AI but won on delivery plan or guarantees.

### 4. Your own RFP response and debrief

Many churners run a formal re-bid. If you were invited, you probably have the RFP, its scoring weights, and possibly a debrief. Look at:

- **Whether you were invited at all.** Not being invited suggests the relationship broke, which is push. Being invited and scored down on AI specifically is pull.
- **The scoring weights.** Compare the weight on AI and analytics against implementation methodology, support SLAs, and references.
- **Document dates.** Were the AI requirements written before or after a competitor demo? A version history in which AI requirements appear right after the demo suggests the competitor shaped the RFP, which is pull via the interaction route.

This material sits in your sales team's files. It is nearly free.

### 5. Replacement contract scope

What they paid for is a costly signal. A few features to check:

- **Separately priced AI or analytics modules, or a premium tier bought for them.** This is pull. Paying extra is a commitment. Bundled AI they got for free is weak evidence.
- **Contract protections.** Fixed-fee implementation, go-live penalties, dedicated delivery teams, and hard support SLAs show what they were protecting against, which points to push.

**Where to get this:** churner interviews, competitor press releases and case studies (these often name the carrier and the modules), and former champions now working elsewhere who may speak candidly.

### 6. What they deployed, and in what order

This is the hardest signal to fake, because it is expensive revealed preference.

- **Pull:** AI capabilities in phase one, or early in phase two. If AI was the reason for switching, they lead with it.
- **Push:** core claims workflow first, stabilization prioritized, AI deferred to a vague "later phase" or never turned on.

Check 6–12 months after the switch. Sources include:

- Follow-up interviews with the churner
- Competitor case studies and conference talks
- The carrier's job postings, such as hiring for claims analytics or data science
- Integration partners
- Your former champions

Also check whether they deployed things you had. If their first-year deployment mostly reproduces capabilities they licensed from you and never used, that is Services.

### 7. Who drove the decision

- **Pull:** driven by an innovation, analytics, or CIO-level sponsor. Often a new executive with an AI or digital mandate. That is a trigger worth recording separately, since it is neither product nor services failure.
- **Push:** driven by claims operations leadership or the burned project sponsor, with complaints about workflow and support.

## Rank the signals by how easily they can be faked

Stated reasons are cheap. AI is also the respectable reason to give a board ("we're modernizing"), so interviews and even RFP language will tend to overstate pull. Weight the evidence roughly like this:

1. **Deployment sequencing and first-year usage.** Costly and behavioral.
2. **Separately priced contract scope.** Costly.
3. **The "already had it" classification.** Hard to rationalize away.
4. **Relative destination share against the market base rate.**
5. **Shortlist elimination reasons.**
6. **RFP weights and document timing.**
7. **Stated reasons.** Useful mainly for the trigger timeline, not for selection.

If the costly signals and the cheap ones disagree, believe the costly ones. A carrier that says "we left for AI" but deployed core workflow first, never turned on AI, and listed requirements you already licensed to them left because of implementation.

## Forward-looking: a test you can control

The observables above reconstruct the past. For the renewals coming up, you can manipulate the variable directly. Among at-risk accounts with similar early grades and fit, vary the save offer:

- Some get **service remediation**: a dedicated delivery team, a re-implementation of unused modules, SLA commitments.
- Some get **AI and analytics access**: roadmap previews, beta access, analytics services.
- Where feasible, some get both.

The predictions:

- **Pure Services:** remediation saves accounts and AI access doesn't.
- **Product:** the reverse.
- **Interaction:** remediation works on its own. AI access helps only for accounts that already reached value, or only when combined with remediation.

With small numbers this won't give you statistical significance, and you may not be comfortable assigning offers arbitrarily. Even assignment by rotation or by CSM will tell you more than any amount of retrospective interviewing, because you set the cause rather than inferring it.

## Turn 4

**User:** Doesn't your top-ranked signal, deployment sequencing, suffer the same flaw as destination, since almost any claims migration must stand up core workflow and clean data before AI can run, so "AI deferred" is expected under pull and push alike? And in the "already had it" test, how would we tell a licensed module that went undeployed because implementation stalled from one the customer shelved because it was inadequate, which is itself a product gap? What record, dated before the renewal decision, would separate those two cases?

**Assistant:**

Yes on both counts. And the second problem exposes a category that neither VP's framing covers.

## 1. Deployment sequencing is confounded by technical dependency

Most AI in claims needs core workflow live and clean historical data first. So "AI came later" is expected under pull and push alike, and I ranked that signal too high. The observable of "was AI deployed early" has to be replaced with measures the dependency chain doesn't dictate.

**Measure plans, not execution order.** The replacement vendor's SOW or project plan is written at signing, before any dependency has played out. Look at how AI appears in it:

- **Pull:** AI capabilities appear as dated milestones with acceptance criteria and a named business outcome, such as leakage reduction, fraud referral rate, or cycle time.
- **Push:** AI appears as "optional phase 2, scope TBD," or not at all.

Committing to a date for something you can't deploy yet is a statement of priority.

**Look at whether they paid for AI's prerequisites.** Some implementation work exists only to make AI possible:

- Backloading years of historical claims beyond what operations needs
- Data labeling
- Integrating third-party data sources such as medical bills, telematics, or fraud databases
- Standing up a data warehouse feed
- Hiring data or analytics staff

A push-switcher has no reason to fund these early. A pull-switcher does. They are dated, costly, and not dictated by sequencing.

**Measure the lag against the vendor's own baseline.** The question isn't whether AI came after core. It's how long after core go-live AI was activated, compared with that vendor's typical customer. Competitor case studies and references give a rough baseline. A pull-switcher should activate near the vendor's fastest pace. A push-switcher should trail it, or never activate.

**Use shallow-dependency features as a probe.** Some AI features need little or no customer history, because they run on vendor-pretrained or pooled models. Examples include document intake and extraction, FNOL triage, and correspondence drafting. These can go live at or near core go-live. If such features were available and left off, that is push evidence, with most of the dependency confound removed.

Deployment evidence still has a place, but in this form: planned commitment, prerequisite investment, and lag against baseline.

## 2. Stalled versus shelved

A module the customer shelved because it was inadequate is a product gap, not Services evidence. The distinction rests on one principle: **a customer can only judge a module inadequate if they were exposed to it.** So the key dated record is whether and how far each module got through configuration, testing, and use before it stopped.

### Records that separate the cases

These are all dated before the renewal decision, and most live in your own systems.

**Implementation project artifacts.** Project plans, status reports, RAID logs, and change orders that removed the module from scope.

- *Stall:* the module was deferred with reasons such as resourcing, timeline, or an upstream dependency that slipped. Check the dependency chain. If the prerequisite data integration or core configuration never finished, the module never had a chance to be judged.
- *Shelved:* the module was descoped with a stated reason like "does not meet requirement X."

**UAT and test-environment records.**

- *Stall:* the module never reached UAT. There are no executed test cases and no sandbox configuration or usage.
- *Shelved:* the module reached UAT or a pilot, users exercised it, and it was rejected.

**Defect classification.** If the module was rejected in UAT, have the product team classify each logged defect. This matters because a module can look inadequate when it was really misconfigured.

- *Configuration defect:* fields not mapped, data not loaded, rules not set up, reports not built. This is Services.
- *Works as designed but doesn't meet the need:* this is a genuine capability gap, which is Product.

**Production telemetry.**

- Never switched on points to stall.
- Switched on, used, and then decayed means the customer tried it and abandoned it. That still needs the next check to classify.

**Support tickets and enhancement requests tagged to the module.**

- *Stall or adoption failure:* how-to questions, configuration help, "blocked by" issues, training requests.
- *Inadequacy:* "doesn't do X," enhancement requests, idea-portal votes, comparisons to a competitor.

**Workaround evidence.**

- Data export requests
- BI tool licenses the customer bought
- Analysts hired to build reports from extracts

Timing is what matters here. A workaround built *after* using your module suggests inadequacy. A workaround built *before* your module ever reached them suggests stall: they needed the capability and you didn't deliver it.

**CSM success plans and steering committee minutes.** "Analytics deferred until integration complete" reads very differently from "customer evaluated reporting, feels it lacks predictive scoring." CSM notes are the softest of these records, but they are dated and were written without knowing the outcome.

### The category neither VP owns

Suppose a stall record says the module was blocked by a product defect, a missing integration capability, or configuration too complex to complete. That isn't a Services failure, and it isn't the AI feature gap either. It's a **product implementability** problem.

Code stall reasons into three bins:

- **Waiting on customer resources:** partly fit, partly Services
- **Waiting on our staffing or delivery:** Services
- **Blocked by product limitations:** implementability

If implementability dominates, the Product VP is right that the product is the problem, but wrong about which part. The fix would be better integration APIs and configuration tooling, not more AI.

### Decision table

| Exposure | Record pattern | Classification |
|---|---|---|
| Never reached UAT | Stall reasons: staffing, delivery, customer resourcing | Services (or fit) |
| Never reached UAT | Blocked by product defect or integration limit | Product implementability |
| Reached UAT, rejected | Defects mostly configuration | Services |
| Reached UAT, rejected | Defects mostly "works as designed, doesn't meet need" | Product gap |
| Deployed, then decayed | How-to and training tickets | Services / adoption |
| Deployed, then decayed | Enhancement requests, competitor comparisons, later workaround | Product gap |

### Two safeguards

**Code retained accounts too.** Retained customers also have undeployed modules. The prediction is comparative:

- **Services:** churners have more *stalled* modules than retainers.
- **Product gap:** churners have more *shelved-as-inadequate* modules.

Also check whether customers who fully deployed a given module kept using it. If even successful deployers abandoned it, it is inadequate, whatever happened to the churners.

**Classify blind.** Write the coding rules before starting. Have someone who doesn't know renewal outcomes classify every account from the records. Otherwise ambiguous cases will drift toward whatever the classifier already believes.

## Revised ranking

1. **Module-exposure classification** from your own dated records: project artifacts, UAT, defect types, telemetry, tickets. It is pre-decision, under your control, and applies to churned and retained accounts alike.
2. **The replacement vendor's plan and prerequisite spend at signing:** AI milestones with dates and acceptance criteria, AI-specific data work, analytics hires.
3. **Relative destination share** against the market base rate.
4. **Shortlist elimination reasons and RFP scoring weights.**
5. **AI activation lag** against the vendor's baseline, especially for shallow-dependency features.
6. **Stated reasons.** Useful mainly for dating the trigger.

The top signal is now evidence you already hold and can code in a few weeks. It also separates three explanations rather than two: Services, feature gap, and implementability. Of those, implementability is the one most likely to be mistaken for whichever story the observer already believed.

## Turn 5

**User:** What should we do?

**Assistant:**

Run a six-week diagnostic before committing either VP's budget. Protect at-risk revenue while it runs, and fix your record-keeping so this is easier next time. Here's the plan.

## Week 0: Set it up so the answer can't be argued away

**1. Put someone neutral in charge of the analysis.** Choose someone who reports to neither VP, such as CS ops, finance, or an analyst from outside both orgs. You can sponsor it, but the coding shouldn't be done by anyone with a stake in the answer.

**2. Pre-register, in writing, signed off by your CEO or COO.** Each VP commits to:
- Their predicted pattern in the tests below
- The specific change 18–24 months ago that their explanation depends on
- What result would make them concede

**3. Agree the decision rules now** (see the table below). Choosing the rules before seeing results is what turns this from a debate into a test.

**4. Hold irreversible commitments, not everything.** Don't sign a major AI partnership, do a big product reorg, or announce a services restructuring for six weeks. Normal roadmap and delivery work continues.

## Weeks 1–2: Fast checks that could explain the doubling on their own

- **Consolidation:** how many churned accounts were acquired or merged?
- **Renewal volume:** did the number of contracts reaching renewal spike, for example from an earlier multi-year sales push?
- **Pricing:** did renewal pricing, discounting, or packaging change in the window?
- **Competitive win rates:** is new-logo win/loss worsening, and specifically on analytics or AI?

If consolidation plus cohort timing accounts for most of the doubling, neither VP's story is the main event. You can stop there, apart from fixing forecasting and qualification.

## Weeks 1–4: Code the evidence you already hold

Cover every account that reached renewal in the last 24 months, **churned and retained alike**. Classify blind to the renewal outcome, using rules written in advance:

- **Early implementation grade:** frozen at go-live + 90 days, from dated delivery records
- **Fit at sale:** size, IT capacity, core system, integration complexity
- **Module exposure:** each undeployed module classified as stalled (with reason: our delivery, customer resources, or product limitation), rejected for configuration defects, rejected for capability gaps, or deployed then abandoned
- **Competitor exposure:** dated from CRM notes and market launches

## Weeks 2–5: Reconstruct what churners actually did

Have a third party interview 10–15 churned customers. For each account, gather:
- When the search started, and what triggered it
- The shortlist, and why each vendor was eliminated
- Your RFP response and any debrief, pulled from sales files
- The replacement vendor's plan: dated AI milestones, AI-specific data work, analytics hires
- Destination share compared with the market base rate

## Starting now: The forward test

For renewals in the next two quarters, triage at-risk accounts using the early-grade and exposure signals. Among comparable accounts, vary the save offer by rotation:
- **Service remediation:** dedicated team, re-implementation of unused modules, SLAs
- **AI/analytics access:** previews, betas, analytics services
- **Both**

This protects revenue immediately and gives you the only evidence where you set the cause rather than inferring it.

## Week 6: Readout against the pre-agreed rules

Assign each churned account a primary cause, weighted by ARR. With small numbers, "what share of lost revenue does each cause explain?" is more useful than significance tests.

| Dominant finding | Action |
|---|---|
| Consolidation or contract cohort | Not a product or service crisis. Fix forecasting and qualification. Modest spend. |
| Poor fit at sale drives churn within strata | Tighten sales qualification. Change how sales is compensated on fit. |
| Stalls from our delivery; grade predicts churn among similar carriers | Fund onboarding and time-to-value first. Hold AI acceleration to what win rates require. |
| Stalls blocked by product limitations | Product investment, but in integration and configuration tooling, not AI. |
| Capability-gap rejections; healthy accounts churning; AI leaders over-represented; win rates falling | Accelerate the analytics and AI roadmap. |
| Interaction pattern | Fix time-to-value for retention. Treat AI as an acquisition investment. Sell or activate AI only after accounts reach value. |
| Mixed | Split investment in proportion to ARR share by cause. |

If results are ambiguous, prefer reversible moves and let the forward save test keep generating evidence.

## Your own move: Fix the instrumentation permanently

Whatever the answer, you had to reconstruct the evidence for this because nobody recorded it in usable form. As head of CS, you can own the fix:
- A standard implementation grade frozen at go-live + 90 days
- Mandatory reason codes whenever a module is descoped or deferred
- Classifying UAT defects as configuration vs. capability
- Logging competitor presence in the CRM at each touchpoint
- A dated trigger-and-destination record for every churn

Next time the question comes up, you'll answer it in a week rather than six.

## Handling the two VPs

Present this as deciding where the next dollars go, not as deciding who's right. Both co-authored the predictions, so both can accept the result. There's a real chance both are partly right: the implementability and interaction findings would each vindicate part of each view. That outcome is more likely than a clean win for either, and it's the one that best protects retention.

## Outcome summary (sent to Jev)

The assistant recommends a six-week diagnostic before committing either VP's budget. Neither belief can be declared right from the facts given, and any explanation must account for a *change* in churn, not a standing condition. It advises holding irreversible commitments (a major AI partnership, a product reorg, a services restructuring) while normal work continues.

**Setup.** A neutral analyst, reporting to neither VP, runs the analysis. Each VP pre-registers in writing, signed off by the CEO or COO:
- their predicted pattern
- the specific change 18–24 months ago their theory depends on
- what result would make them concede

Decision rules are fixed in advance.

**Fast checks.** Consolidation, renewal-volume spikes from earlier multi-year cohorts, pricing changes, and competitive win rates could explain the doubling on their own.

**Coding existing records.** Every renewal from the last 24 months, churned and retained, is coded blind to the outcome:
- implementation grade frozen at go-live plus 90 days from dated delivery records
- fit at sale
- competitor exposure
- module exposure: stalled (with reason), rejected for configuration defects, rejected for capability gaps, or deployed then abandoned

**Churner interviews.** A third party interviews 10–15 churners about their search trigger, shortlist eliminations, RFP details, and the replacement vendor's dated AI commitments.

**Forward test.** For renewals in the next two quarters, save offers are varied by rotation: service remediation, AI access, or both. This protects revenue and sets the cause directly.

**Readout.** Churn is attributed by ARR share against the pre-agreed table. Possible findings include consolidation, poor fit, delivery stalls, product implementability, capability gaps, an interaction pattern, or a mix. Mixed results mean investment split proportionally, and ambiguity favors reversible moves.

**Caveats.** Small numbers make statistics weak. Costly behavioral signals outweigh stated reasons. Both VPs are likely partly right.

**Permanent fixes.** CS should institutionalize grades, descoping reason codes, defect classification, competitor logging, and churn records.
