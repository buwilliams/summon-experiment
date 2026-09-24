# critical-rationalism/churn-cause/testB

Model: claude-opus-5-5 · 2026-09-24T14:47:29.919703+00:00

## Turn 1

**User:** You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Short answer: you can't tell yet, and neither can they

Both VPs are offering plausible stories, and each story conveniently directs budget to its author's organization. That doesn't make either wrong, but it means neither belief should be accepted on conviction. The good news is that the two hypotheses make **different, testable predictions**, and you probably already have most of the data to test them within a few weeks.

My prior is that the answer is **"both, interacting, in different segments."** The useful question isn't which VP is right. It's *which customers are leaving for which reason, and what fixes the largest share of lost revenue fastest.*

## Four traps to avoid first

**1. Stated exit reasons are unreliable.**
Customers leaving a claims platform very often say "the competitor has better AI and analytics." That reason is easy to defend to their own leadership and procurement. "We never got your product working" implicates their own team, so it goes unsaid. A customer who never reached full value will *experience* your product as feature-poor. Product gaps and adoption failure can look identical in exit interviews.

**2. Look for the lag.**
Claims software is extremely sticky. Contracts often run 3–5 years, and switching is expensive. A sudden doubling of churn in a sticky category usually has one of two causes:
- **A cohort effect.** Customers signed and implemented badly 3–5 years ago are now hitting renewal. Check whether there was a big sales push, a pricing change, or services turnover back then. If so, today's churn reflects past implementation quality, not today's roadmap.
- **An external trigger.** Something changed in the market about 18 months ago.

**3. Consider hypotheses nobody has raised.** Regional carrier churn is often driven by:
- Carrier M&A (the acquirer standardizes on its own system).
- Core-suite vendors bundling claims into a policy/billing/claims platform deal.
- Budget pressure from catastrophe losses.
- Champion turnover.
- A competitor discounting aggressively.

None of these is fixed by features *or* onboarding. Rule them out before choosing between the VPs.

**4. You need a control group.**
"Churned customers had long implementations" means nothing if retained customers did too. Every analysis should compare churned against retained accounts.

## How the hypotheses make different predictions

| Evidence | Implementation/value is the driver | Product gaps are the driver | Structural (M&A, suites, budget) |
|---|---|---|---|
| **When customers churn** | Mostly at first renewal | Also among long-tenured, mature customers | Uncorrelated with tenure |
| **Adoption before churn** | Never ramped: low usage, modules never live | Healthy adoption, then departure | Varies |
| **Implementation duration** | Churned accounts had much longer or troubled go-lives than retained ones | No meaningful difference | No difference |
| **Where they go** | Scattered, or a like-for-like rip-and-replace | Concentrated on 1–2 competitors known for analytics/AI | Acquirer's system or a suite vendor |
| **Support history** | Rising tickets and escalations 6–12 months before churn | Feature requests and roadmap questions dominate | Little signal; decisions made above your contacts |
| **New-logo win/loss** | Win rates roughly stable | Losing competitive deals on the same named capabilities | Losing to suites |

The new-logo row is especially valuable. Prospects have no implementation experience with you. If you're also losing *new* deals on analytics and AI, the product-gap hypothesis gains real weight. If win rates are fine, the gap is more likely a post-sale value problem.

## What to do: a four-to-six-week diagnostic, then decide

**Step 1 (week 1): Agree on the rules before seeing the data.**
Get both VPs in a room and ask each one: *"What evidence would convince you that you're wrong?"* Write the answers down using the table above. This is the single most important step. It turns a political fight into an empirical question, and it prevents either side from reinterpreting the results afterward.

**Step 2 (weeks 1–4): Run the analysis.** For every account that churned or downsold in the last 24 months, plus a matched sample of retained accounts, pull:
- Revenue lost, not just logo count. A few large losses may tell a different story than the count does.
- Tenure at churn, and whether it was their first renewal.
- Signing date, implementation duration, and go-live status by module.
- Usage and adoption trends over the prior 12 months.
- Support ticket volume and escalations.
- Destination: which vendor, and whether M&A or a suite deal was involved.
- Gross revenue retention broken out by segment (size, line of business, region, product edition).

Add new-logo win/loss for the same period.

**Step 3 (weeks 2–5): Run neutral exit interviews.**
Have 10–15 recently churned customers interviewed by someone outside Product and Services: you, a third party, or an executive sponsor. Ask about the *decision process*, not just "why." Useful questions:
- Who initiated the change?
- When did you start looking?
- What did the winning vendor promise that we couldn't?
- What percentage of our product were you actually using?

**Step 4 (week 6): Segment the losses and allocate effort.** The likely output looks something like: "X% of lost ARR is first-renewal, low-adoption customers; Y% is mature customers lost to Competitor Z on analytics; W% is M&A." Invest in proportion to those shares.

## No-regret moves to start now

**Triage upcoming renewals.** Score every renewal in the next 12 months for adoption and health. Put the at-risk accounts through executive sponsorship and a "value recovery" engagement. Reach full value on what they've already bought before pitching anything new. This saves revenue regardless of which hypothesis wins.

**Sequence carefully.** New AI features delivered to customers who can't adopt your current product will not reduce churn. They land on the same broken adoption path. Conversely, fixing onboarding only helps customers who are still early in their lifecycle. It won't retain mature accounts that are genuinely outgrowing you. That is why segmentation matters more than picking a side.

**Look for the bridge.** Analytics built on claims data customers *already* have in your system can often be delivered with little implementation burden. A packaged reporting/insights layer or a targeted AI use case (triage, fraud flags, reserve suggestions) can address the competitive perception and demonstrate value to struggling accounts at the same time. Ask Product whether a thin version is possible in one or two quarters instead of a full roadmap acceleration.

## What to tell your leadership

"We have two credible hypotheses that predict different things. We'll test them against churned and retained accounts over six weeks, using criteria both VPs agree to in advance. In the meantime we're running a retention sprint on at-risk renewals. At the end, we'll allocate investment according to where the lost revenue actually came from."

That position is hard to argue with. It also makes you the person who resolved the conflict with evidence rather than the person who picked a side.

## Turn 2

**User:** What if our usage data is spotty or we never tracked implementation timelines consistently? Can we still run this analysis?

**Assistant:**

Yes. Imperfect data is the normal case, not the exception. You're not trying to publish a paper. You're trying to learn which hypothesis explains most of the lost revenue, and coarse evidence from several sources is usually enough for that. You just have to be more deliberate about how you gather it.

## 1. Reconstruct what you didn't track

Implementation and adoption histories leave traces across your company even if nobody recorded them directly.

**Implementation timelines:**
- **Contracts, SOWs, and change orders.** Signed date, planned go-live, and scope changes. A pile of change orders is itself a signal of trouble.
- **Billing records.** Services hours billed, milestone payments, and when subscription billing started (often tied to go-live).
- **CRM and project tools.** Opportunity close dates, project records, handoff dates to CS.
- **Support tickets.** The first production ticket is a decent go-live proxy. Tickets that shift from "setup and configuration" to "how do I" mark the transition.
- **Email, calendars, and status decks.** Steering committee meetings and escalation threads, especially for the accounts that matter most.

**Adoption and value:**
- **System data, even without product analytics.** If you host the software, you probably know claims processed per month, active user accounts, modules enabled, and integrations live. Claim volume in your system relative to the carrier's actual volume is an excellent adoption proxy.
- **Support ticket mix.** Tickets about basic functionality years after go-live suggest shallow adoption.
- **QBR decks and CSM notes.** Uneven, but often candid.
- **Churned customers themselves.** In exit interviews, ask what percentage of claims ran through your system and which modules they actually used.

## 2. Use coarse categories instead of precise numbers

You don't need exact implementation days. Three or four buckets per account are enough:
- **Implementation:** on time / moderately late / severely late or never fully live.
- **Adoption:** broad / partial / minimal.
- **Tenure at churn:** first renewal / later renewal.
- **Destination:** named competitor / suite vendor / acquirer / unknown.

The patterns you're looking for are big ones, such as "most lost revenue came from accounts that were never fully live." Coarse categories reveal patterns like that fine. Precision matters only when the effects are subtle, and if the effects are subtle, neither VP's story is the main driver anyway.

## 3. Shrink the sample and go deep

Don't try to reconstruct the full customer base. Take:
- The churned and downsold accounts that together make up roughly 80% of lost revenue. For most companies this is 15–30 accounts.
- A matched set of retained accounts of similar size, segment, and signing date.

Thirty to sixty well-researched accounts will tell you more than hundreds of accounts with missing fields. Assign someone, ideally a neutral analyst or a small team, to build a one-page profile of each account from all the sources above.

## 4. Guard against hindsight bias

When people fill gaps from memory, they tend to remember churned accounts as having been troubled all along. That can manufacture the exact pattern you're testing for.

- **Prefer documents to memory.** Use recollection only to fill gaps, and flag it as such.
- **Code the accounts blind where you can.** Have someone rate implementation and adoption from the documents without being told which accounts churned.
- **Use two raters on a subset.** If they disagree often, your categories are too subjective. Tighten them.
- **Record a confidence level for each data point** (documented / inferred / remembered). Check whether your conclusions still hold using only the documented data.

## 5. Treat missing data as information, carefully

Two cautions pull in opposite directions:
- **The gaps may themselves be a finding.** If you can't determine whether a customer ever went fully live, then nobody at your company knew during the relationship either. That supports the Services VP's argument that customers aren't being guided to value, independent of the churn analysis.
- **Missingness may be biased.** Troubled projects sometimes generate *more* documentation because of escalations. Smooth ones sometimes generate less because nobody needed to write anything down. Or it can be the reverse. Check whether missing data is concentrated among churned or retained accounts before drawing conclusions.

## 6. Rely on triangulation

No single imperfect source should settle the question. But if three weak signals all point the same way, you can act with reasonable confidence. For example:
- billing shows long implementations,
- tickets show basic-usage questions late in the relationship, and
- exit interviews mention never getting fully live.

Also remember that several parts of the original plan don't depend on usage data at all:
- tenure at churn,
- competitor destination,
- M&A and suite-vendor involvement, and
- new-logo win/loss.

Those alone may substantially narrow the question.

## 7. Adjust expectations and start tracking now

**Set expectations with both VPs.** Tell them the analysis will produce directional conclusions with stated confidence, not precise measurements. That is enough to allocate investment. If the result is ambiguous, you can make a smaller, reversible bet and measure it.

**Fix the tracking going forward.** Start recording, for every new implementation:
- signed date, planned go-live, actual go-live, and scope changes;
- modules live; and
- claim volume in your system at 6 and 12 months.

Even a simple spreadsheet maintained by the implementation leads will make the next version of this analysis far easier. Instrumenting value realization is also something both VPs should support, whichever of them turns out to be more right.

## Turn 3

**User:** How do I get churned customers to actually agree to an exit interview, and be honest in it, when they've already left and have no reason to help us?

**Assistant:**

Many churned customers will say yes, and more of them than you'd expect will be candid. People generally like being asked for their expertise, especially when the request is respectful, short, and clearly isn't a sales pitch. The regional insurance world is also small. Carriers talk to each other, people change jobs, and claims leaders know they may cross paths with your company again. Most people want to leave on professional terms.

The key is designing the ask and the conversation so that helping you is easy, safe, and a little bit gratifying.

## Getting them to say yes

**1. Choose the right person to ask.**
The ask should not come from the account's CSM or sales rep. Those relationships may be strained, and the customer will reasonably suspect a win-back attempt. Better options:
- **A senior executive**, such as your CEO or head of customer success, writing personally. A request from someone senior signals that the answer matters.
- **A neutral third party**, such as a research firm or independent consultant. This usually produces the most candor, because the interviewer has no stake in defending your company.

A good combination is an executive invitation followed by a third-party interview.

**2. State plainly that this is not a sales call.**
Something like:
> "You've made your decision, and we respect it. This isn't an attempt to win you back. We've lost more customers than we should have, and we want to understand where we fell short so we can fix it. Your perspective would genuinely help. Thirty minutes, by phone, at your convenience."

Then honor that. If anyone pitches during the interview, you lose credibility with that customer and with anyone they talk to afterward.

**3. Get the timing right.**
The best window is usually 30–90 days after the decision. By then emotions have cooled, but memories are still fresh.

Be careful about asking during a transition. If they still depend on you for data extraction or cutover support, a request can feel like implied pressure. Make explicit that the transition support is unaffected by whether they participate. Or wait until the cutover is done.

**4. Make it easy.**
- Thirty minutes or less.
- Phone or video.
- Scheduled around their calendar.
- No prep required.
- A short, clear, human email, not a survey link.

**5. Offer something appropriate in return.**
- **Aggregated findings.** Many claims leaders are interested in what's happening across carriers.
- **A charitable donation in their name.** This works better than a gift card. Insurers are regulated and often have strict gift policies.
- **Genuine acknowledgment.** A follow-up note from the executive about what you changed because of their input.

**6. Ask more than one person per account.**
Different roles know different parts of the story:
- The executive decision-maker knows why the switch was approved.
- The claims operations lead knows what daily use was actually like.
- IT knows about integration pain.
- Procurement knows what the competitor offered.

Also look for **former employees** of churned carriers who have moved to other companies. They are often the most candid people you can find, because they have no loyalty to protect.

## Getting honest answers

**1. Use a neutral interviewer and promise aggregation.**
Tell participants that individual comments won't be attributed to them, and that findings will be reported in aggregate. Customers are more candid with an outsider. This matters especially if the honest answer implicates their own team, such as "we never staffed the implementation properly."

**2. Give permission to criticize, and don't defend.**
Open with something like: "We suspect we made real mistakes, so please don't soften anything." Then don't argue, explain, or correct them during the interview. If they sense defensiveness, they'll retreat to polite generalities.

**3. Ask about the decision process as a story, not "why did you leave."**
"Why did you leave?" gets the tidy, defensible answer, which in your situation is often "better AI." A chronological narrative gets closer to the truth. Useful prompts:
- "When did you first start thinking about alternatives? What was going on at the time?"
- "Who raised it first, and what prompted them?"
- "Walk me through the evaluation. Who else did you look at?"
- "What did the vendor you chose show you that made the difference?"
- "At what point was the decision effectively made?"

The early moments are the most revealing. If the story starts with "our go-live slipped and our claims team never trusted the system," that tells you something different from "we saw a competitor's AI demo at a conference."

**4. Ask for specifics.**
Vague impressions are easy to rationalize. Concrete facts are harder to shade:
- "Roughly what percentage of your claims ran through our system?"
- "Which modules were you actually using day to day?"
- "How many support tickets or escalations would you say you had in the final year?"
- "Were there features you had but didn't use? Why not?"

**5. Probe stated reasons with counterfactuals.**
This is how you tell a real reason from a convenient one:
- "If we'd had the analytics capability you wanted, would you have stayed?"
- "If your implementation had gone smoothly, would the AI gap have mattered as much?"
- "What would we have had to do, and by when, to keep you?"

If someone says the product gap was decisive but hesitates on the first question, you have learned something important.

**6. Include one open-ended closing question.**
"Is there anything we should have asked but didn't?" This sometimes produces the most important insight of the whole interview.

## What to expect, and what to do about non-response

With a well-designed executive ask and a third-party interviewer, getting a third to half of churned accounts to participate is realistic. That's enough for directional conclusions across 15–30 accounts.

Keep **non-response bias** in mind, though. The people who agree may be systematically different from those who refuse. They might be less angry, or more invested in explaining themselves. Some ways to compensate:
- **Talk to others who saw the decision.** Claims consultants or implementation partners who advised on the switch often have a candid outside view.
- **Use public signals.** The winning vendor's press releases and case studies often reveal what they emphasized.
- **Interview current customers who considered leaving but stayed.** They're easy to reach and highly informative. What kept them may tell you what the churned customers lacked.
- **Interview matched retained customers.** This gives you the control group from your earlier analysis. It also often reveals that retained customers share the same frustrations. If so, the difference lies elsewhere, perhaps in executive sponsorship or adoption depth.

One final point: the way you run these interviews is itself a customer experience. A former customer who has a respectful, non-defensive conversation with a senior person, and later hears that you acted on their input, is far more likely to speak well of you. Some will even come back someday.

## Turn 4

**User:** What if the analysis shows it really is both, roughly split between low-adoption early churners and mature customers leaving for better analytics? How do I keep the two VPs from treating that as permission to each run their own plan?

**Assistant:**

"Both" is the most politically dangerous result you can get. It lets each VP declare victory and go back to what they wanted to do before the analysis. You would end up with two plans competing for the same engineering capacity and the same customer attention, each measured by its own yardstick, with nobody accountable for the number that actually matters.

The way to prevent this is to make the finding change how the work is organized, not just how it's justified.

## 1. Make retention the single goal, and own it jointly

Both plans should be judged by one top-line metric: **gross revenue retention**, or lost ARR, reported by segment. Each VP can own supporting metrics. But neither plan counts as "working" unless retention in its segment improves.

Then define leading indicators for each segment, so you don't have to wait a year for renewals to show results.

- **Early-churn segment (Services):**
  - time to go-live;
  - share of the carrier's claims volume in your system at 6 and 12 months;
  - modules live against modules purchased;
  - escalation rate.
- **Mature segment (Product):**
  - adoption of the new analytics capabilities by at-risk mature accounts;
  - renewal intent from those accounts;
  - competitive win rate against the specific vendors customers are leaving for.

Agree up front on what "not working" looks like, and when you'll check. This is the same move as before the analysis: pre-committed criteria that turn later arguments into a reading of the evidence.

## 2. Don't split resources in proportion to the churn

A 50/50 churn split does not imply a 50/50 investment split. Weigh each segment on four dimensions:

| Factor | The question to answer |
|---|---|
| **Revenue at stake next** | Which segment has more ARR up for renewal in the next 12–24 months? |
| **Time to impact** | How quickly can each fix change outcomes? Onboarding fixes help new cohorts fast. Features take quarters to ship and more quarters to adopt. |
| **Compounding** | Is the problem growing? |
| **Cost and confidence** | How much does each fix cost, and how sure are you that it will work? |

On compounding, the two segments pull in different directions:
- Every customer onboarded under today's process is a candidate for a future early churner. The early-churn problem keeps refilling until you fix onboarding.
- The analytics gap may widen as competitors keep shipping.

Working through these factors usually produces a clear allocation, and it gives both VPs a principled reason to accept it.

## 3. Show them it's actually one problem

The strongest argument against two independent plans is that each depends on the other.

**Analytics only work on adopted, clean data.** Low-adoption customers can't use better analytics, because too little of their claims activity runs through your system. Broken onboarding caps the value of Product's work.

**New features have their own adoption problem.** If mature customers need a services project to turn on the new analytics, you've just recreated the implementation problem for your best accounts. Make "deployable with minimal services effort" a design requirement. Put Services in the room when features are specified.

**Fixing onboarding needs engineering time.** Real improvements often require product work:
- data migration tooling;
- configuration templates for regional carriers;
- in-product guidance;
- integration connectors.

This is where the two plans collide most directly: both want the same engineers. Decide explicitly how capacity is divided. Otherwise the fight happens quietly in sprint planning, and onboarding usually loses.

**There's likely a bridge investment.** A packaged analytics layer built on data customers already have could serve both segments. It gives mature accounts the capability they're leaving for. It also gives struggling accounts a visible early win.

Once these dependencies are visible, "two separate plans" is plainly unworkable. What you need is one plan with two workstreams and explicit handoffs.

## 4. Scope each workstream to the evidence

"Both" can easily become cover for each VP's entire wish list. Hold each side to what the analysis actually showed.

**Product.** If mature customers left for specific capabilities, build *those* capabilities. That might mean loss-ratio dashboards, reserve adequacy analytics, or fraud flags. It does not automatically justify an entire accelerated AI roadmap. The exit interviews and competitive losses should name the target.

**Services.** If early churn traces to particular failure points, fix those specific failures first. These might be:
- long data migrations;
- integration delays;
- loss of momentum after go-live;
- no path from go-live to the next module.

That is different from a broad services transformation.

A useful discipline is to have each VP write a short list of what they are *not* going to do this year.

## 5. Put governance above both of them

Two peers can't allocate a shared engineering team between themselves. Someone above both has to own the integrated plan and settle trade-offs. That is usually the CEO or COO.

In practice:
- **One document:** one integrated retention plan, with both workstreams, shared capacity, dependencies, and the metrics above.
- **One monthly review:** both VPs present together against the shared scorecard, not separately to their own audiences.
- **A small cross-functional team** for the overlap. It owns time to value for new features and the product work that onboarding depends on.
- **Aligned incentives.** If both VPs' goals include segment retention, collaboration becomes the rational choice.

## 6. Your role: the integrator

You're in the best position to hold this together. Customer success sees both segments, owns the renewal relationship, and has no stake in which plan gets more money. You ran the analysis, so you have credibility as the neutral party.

Propose to your CEO that retention be run as a single program with executive sponsorship. Offer to be the program owner or co-owner, with both VPs accountable for their workstreams. Pitch it this way:

> "We found two problems that share a root. Customers who can't get value from what we build will leave, whether the gap is in onboarding or in features. I'd like to run this as one retention program with shared metrics, so we're not funding two plans that compete for the same engineers and measure different things."

## How to present the finding

When you share the results, don't lead with "you're both right." That framing invites each VP to hear only half of it. Lead instead with:
- the revenue at stake in each segment;
- the dependencies between the two problems; and
- the proposal for one integrated plan.

The message is that neither of them was wrong, but neither plan alone would have fixed retention.

## Turn 5

**User:** What should we do?

**Assistant:**

Here is the plan, in order. It works whatever the analysis ends up showing, because the decisions are built in as checkpoints rather than assumed up front.

## This week: set it up

1. **Get CEO sponsorship.** Ask for three things:
   - retention run as one program with shared metrics;
   - you as program owner, with both VPs accountable for workstreams;
   - a hold on major roadmap or services reallocations until the diagnostic reports, about six weeks out.

   Frame it as protecting the company from betting on the wrong fix, not as delaying either VP.

2. **Run the "what would change your mind" meeting.** Get both VPs to write down, in advance, the evidence that would support or undercut their hypothesis. Use the prediction table from earlier: tenure at churn, adoption before churn, implementation duration, destination, and new-logo win/loss.

3. **Start the retention sprint.**
   - Score every renewal in the next 12 months for health.
   - Put the at-risk accounts into executive sponsorship and a value-recovery engagement.
   - Get them to full value on what they already own before pitching anything new.

   This protects revenue no matter what you learn.

## Weeks 1–6: diagnose

4. **Build the account profiles.**
   - **Which accounts:** those making up roughly 80% of lost ARR over 24 months, plus a matched retained group.
   - **What sources:** reconstruct from contracts, billing, tickets, and system data.
   - **How to record it:** use coarse categories, code blind where possible, and tag each data point by confidence level.

5. **Run the exit interviews.** Aim for 10–15 churned accounts:
   - invited by an executive, conducted by a neutral interviewer;
   - chronological questions, specific details, and counterfactual probes.

   Add current customers who nearly left and stayed.

6. **Pull new-logo win/loss.** Check whether you're losing new deals on the same capabilities churned customers mention. This is the cleanest test of whether the product gap is real or a stand-in for value failure.

7. **Start tracking implementations now.** For every new implementation, record:
   - signed date, planned and actual go-live, and scope changes;
   - modules live;
   - claim volume in your system at 6 and 12 months.

## Week 6: decide

8. **Present segmented lost ARR to the CEO and both VPs together.** Weight investment by:
   - revenue up for renewal next;
   - time to impact;
   - whether the problem is compounding;
   - cost.

   Then choose among three paths:

| What the analysis shows | What you do |
|---|---|
| **Mostly early, low-adoption churn** | Fix onboarding and the path from go-live to full value first. Scope the roadmap to features that help adoption. Delay broad AI acceleration. |
| **Mostly mature customers leaving for named capabilities** | Build those specific capabilities, designed to deploy without a services project. Keep onboarding fixes targeted. |
| **Both** | One integrated plan with two workstreams, explicit engineering capacity for onboarding tooling, and a bridge investment serving both segments. |

## Quarters 1–2: execute

9. **Run the program.**
   - **One plan document** covering both workstreams.
   - **Shared engineering capacity,** allocated explicitly.
   - **A small cross-functional team** owning time to value for new features and the tooling that onboarding depends on.
   - **A monthly joint review** against one scorecard: gross revenue retention by segment, plus the leading indicators.

10. **Check the leading indicators at 90 days.**
    - **Onboarding:** time to go-live, and claims volume in your system at six months.
    - **Mature accounts:** analytics adoption, renewal intent, and competitive win rate.

    Keep, adjust, or cut each workstream against the criteria you agreed at the start.

## Where I'd bet

My working guess is that the value-realization problem is larger than your VP of Product believes. Three observations point that way:
- Claims software is sticky.
- Churn doubled on a delay consistent with 3–5-year contracts.
- "The competitor has better AI" is exactly what customers who never reached full value tend to say.

But the analysis exists precisely so you don't have to rely on my guess or theirs.

## If you do only three things

1. **Protect the renewals coming up in the next 12 months,** starting now.
2. **Take six weeks to learn which customers are leaving for which reason,** using criteria both VPs agreed to in advance.
3. **Turn the answer into one retention program,** owned by you and sponsored by the CEO, not two competing plans.

## Outcome summary (sent to Jev)

The assistant recommends not choosing between the two VPs yet. Instead, run a roughly six-week diagnostic to learn which customers are leaving for which reason, then fold the answer into one retention program. The assistant would own that program as head of customer success, with CEO sponsorship and both VPs accountable for workstreams. Both VPs' stories are plausible, each directs budget to its author, and the two make different testable predictions. The assistant's prior is "both, interacting, in different segments," with value realization likely the bigger problem than the VP of Product believes. Three things point that way: claims software is sticky, churn doubled on a lag consistent with 3–5-year contracts, and "the competitor has better AI" is what customers who never reached full value tend to say.

Immediate steps:
- **Get CEO sponsorship**, including a hold on major reallocations until the diagnostic reports.
- **Hold a meeting where both VPs pre-commit** to what evidence would prove them wrong.
- **Start a retention sprint** on at-risk renewals in the next 12 months.

The diagnostic has four parts:
- **Compare churned and retained accounts.** Cover the accounts making up about 80% of lost ARR, against a matched retained group, on tenure at churn, adoption, implementation duration, destination, and support history. Reconstruct missing data from contracts, billing, tickets and system data, using coarse categories, blind coding and confidence tags.
- **Run 10–15 neutral exit interviews** with chronological, specific and counterfactual questions.
- **Pull new-logo win/loss** to test whether the product gap is real.
- **Begin tracking implementations** going forward.

At week six, the assistant would weight investment by revenue up for renewal, time to impact, compounding and cost, not in proportion to churn share. If both problems appear, that means one integrated plan with two workstreams, explicitly allocated engineering capacity, and a bridge analytics investment. Leading indicators would be reviewed at 90 days.

Caveats:
- Exit reasons are unreliable.
- Structural causes such as M&A, suite vendors and budget pressure must be ruled out.
- Hindsight and non-response bias can distort the analysis.
- A "both" result risks becoming permission for each VP to pursue their full wish list.
