# churn-cause/economic/testA

Model: claude-opus-5-5 · 2026-09-24T15:30:40.687696+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

Neither belief can be confirmed from where you sit. Both are plausible, both VPs are arguing from their own vantage point, and the two explanations aren't mutually exclusive. The good news is that your data can distinguish between them, and as head of CS you're well positioned to run that analysis as a neutral party.

## First, the two hypotheses predict different patterns

| If the Product VP is right... | If the Services VP is right... |
|---|---|
| Churned customers were fully implemented and actively using the product | Churned customers never fully went live or used only a fraction of the product |
| Churn is spread across tenure, including mature, happy-looking accounts | Churn clusters at first or second renewal |
| Churned customers go to competitors known for analytics/AI | Churned customers go to whoever promises an easier deployment, or back to legacy/in-house tools |
| Customers heavily used your existing analytics and hit its ceiling | Customers barely touched your existing analytics |
| Implementation length doesn't predict churn | Longer implementations and worse support metrics predict churn |
| Loss conversations mention specific missing capabilities | Loss conversations mention frustration, slow time to value, and unresponsive support |

## The analysis to run (4–6 weeks, not months)

**1. Build a churn dataset.** For every account lost in the last 18–24 months, plus a comparison set of retained accounts, pull:
- Contract start, go-live date, implementation duration vs. plan
- Modules purchased vs. modules actually live
- Usage depth before churn (active users, claims processed, analytics/reporting usage)
- Support ticket volume, severity, time to resolution, CSAT
- ARR, carrier size, lines of business
- Churn destination, if known
- Executive sponsor or champion changes

**2. Do a cohort analysis.** Churn doubled over 18 months, so something changed. Check:
- Did implementation times lengthen for cohorts starting 2–3 years ago?
- Was there services turnover, a reorg, or a shift to partner-led implementations?
- Did a competitor launch something notable?
- Did pricing, packaging, or the sales motion change (e.g., selling to smaller carriers who lack the IT capacity to implement)?

The timing of the inflection will often point to the cause.

**3. Hold structured exit interviews and treat stated reasons skeptically.** "Your competitor has better AI" is the easiest, least awkward reason a customer can give. It's rarely the whole story. Interview both the economic buyer and actual users (adjusters, claims managers). Ask what they expected at purchase, when they realized it wasn't happening, and what the replacement does that you don't. Have someone outside both the Product and Services orgs conduct them.

**4. Look at the ~20 largest losses individually.** Revenue churn is often driven by a handful of accounts, and reading those stories closely is often more revealing than the aggregate.

## Check for a third explanation

Neither VP has mentioned some causes common in your market:
- **Carrier consolidation.** Regional carriers merge or get acquired, and the acquirer standardizes on its own system.
- **Suite bundling.** Core system vendors (policy, billing, claims) sell claims as part of a platform, and carriers replace point solutions during core modernization.
- **Champion turnover.** The person who bought you left.
- **Price and budget pressure**, especially in bad loss years.

If a large share of churn falls here, both roadmaps are partially beside the point, and the fix looks more like platform integrations, partnerships, or multi-threaded relationships.

## The likely answer, and why it matters

In many cases, the two explanations are linked:
- Customers who never reach full value become receptive to competitor pitches. A half-implemented system compared against a polished AI demo looks like a product gap even when the root cause was adoption. Building more features won't help customers who aren't using the ones they have.
- Painful implementations are often partly a product problem: weak configurability, difficult integrations with core systems, poor data migration tooling. That's not purely a services issue.

So the real question is which problem is primary for which segment. You may find, for example, that small carriers churn because of implementation while large carriers churn over analytics.

## What to do now

**Immediately (no-regret moves):**
- Identify at-risk accounts renewing in the next 6–12 months and run save plans: exec outreach, adoption reviews, targeted services help.
- Triage stalled implementations. Get anyone stuck in go-live limbo to first value fast.
- Define a shared time-to-value metric (e.g., days to first claim processed, days to full module adoption).

**After the diagnostic:**
- Allocate investment in proportion to the evidence, not to who argues more persuasively.
- Agree up front with both VPs what evidence would change their minds. This keeps the analysis from becoming a debate over interpretation.
- Give Product and Services a joint goal, such as gross revenue retention, so they fix the handoff between them rather than competing for budget.

**If the data supports it,** a strong middle path is to prioritize product work that reduces implementation friction and surfaces value faster, such as better integrations, migration tools, and out-of-the-box dashboards for claims leaders. That addresses both hypotheses at once.

If you share what data you have access to (usage telemetry, support system, CRM loss reasons), I can help you design the specific analyses or an exit-interview guide.

## Turn 2

**User:** Our CRM loss reasons are mostly vague picklist entries like "went with competitor" or "budget." How do I get useful answers from customers who've already left?

**Assistant:**

Those picklist entries record the last step of the decision, not the cause. "Budget" usually means "not worth the money to us," and "went with competitor" doesn't say why. Former customers are often more candid than current ones, since they have nothing left to negotiate, if you approach them the right way.

## Who to contact

**Prioritize by learning value, not just size:**
- Your largest revenue losses
- Accounts that looked healthy and churned anyway (the most surprising cases)
- A mix of tenures, including first-renewal losses and long-time customers
- A few from each segment (carrier size, region, implementation type)

Aim for **12–20 conversations**. That's usually enough to see patterns; after that, new interviews mostly confirm what you've heard.

**Talk to more than one person per account where possible:**
- **Economic buyer** (VP Claims, COO, CIO): why the decision was made
- **Day-to-day users** (claims managers, adjusters, IT admins): what the experience was actually like
- **Your former champion**, if they've moved to another carrier. They're often the most open, and they may be a future buyer.

These people often give different stories, and the gap between them is informative.

## Who should conduct the interviews

Not the account's former CSM or sales rep, and not anyone from Product or Services, given the internal debate. Options, roughly from most to least candid:
1. **A third-party firm** that specializes in win/loss interviews. It costs more but yields the most honest answers, especially about your team's performance.
2. **Someone internal with no stake**: a CS leader who didn't own the account, or someone from strategy or finance.
3. **You**, which works if you're clearly positioned as wanting to learn, not win them back.

Anonymized reporting ("a mid-size carrier said...") increases honesty, especially about specific people on your team.

## How to ask

**The outreach message:**
- Short, personal, from a senior person
- Explicitly *not* a sales call: "We're not trying to win you back. We're trying to understand where we fell short."
- 20–30 minutes, their schedule
- Offer a thank-you: a donation to a charity of their choice or a modest gift card (check their compliance rules; insurance companies can be strict about gifts)

Expect a 20–40% acceptance rate. People are more willing than you'd guess, especially if the relationship ended without acrimony.

**Interview structure:** Walk through the timeline rather than asking "why did you leave?" Direct "why" questions get the tidy, socially easy answer. Timelines get the real story.

1. **The original purchase:** "Take me back to when you chose us. What were you hoping to accomplish?"
2. **Implementation:** "How did the rollout go compared to what you expected? When did you feel it was really working, if ever?"
3. **The turning point:** "When did you first start thinking this might not be the right fit? What was happening then?"
4. **The search:** "Who else did you look at? What made the one you chose stand out?"
5. **The decision:** "Who was involved in deciding? What was the argument for staying, and why didn't it win?"
6. **Counterfactual:** "If we could have changed one thing, what would have kept you?"

The **turning point** and **counterfactual** questions are usually the most revealing. Follow-ups matter more than the script: "Can you give me an example?" "What happened next?" "How did that affect your team?"

**Decoding vague answers:**
- **"Budget"** → "When you looked at what you were paying versus what you were getting, how did that compare?" and "Was there a specific budget cut, or was it a value question?"
- **"Better features"** → "Which ones specifically? Were those things you'd tried to do with our product?" This separates real gaps from perceived gaps caused by low adoption.
- **"Went with competitor"** → "What did they show you that we didn't?" and "Was the competitor already in use elsewhere in your organization?" (This surfaces the suite bundling and consolidation cases.)

**Avoid:** defending your product, explaining what they missed, leading questions ("Was it the implementation?"), and pitching. If they bring up a fixable problem, write it down and follow up later.

## Supplement with internal sources

For accounts that won't talk, you can still reconstruct a lot:
- **Implementation records:** planned vs. actual timeline, escalations, scope changes, what never went live
- **Support history:** ticket themes in the last 6–12 months, severity trends, sentiment in the ticket text
- **Usage data:** when engagement started declining relative to the churn date
- **Email and meeting history:** QBR notes and executive escalations often capture the problem in real time
- **Your own people:** debrief the CSMs, implementation leads, and support engineers who worked those accounts. Ask the same timeline questions.
- **Public information:** carrier mergers, leadership changes, core system replacement announcements, and press releases from the competitor who won

Where you have both an interview and internal records, compare them. If a customer says "missing AI features" but never logged into your analytics module, that's a meaningful finding.

## Analyze for patterns, not quotes

For each account, record:
- **Primary root cause** (one): implementation/time to value, support experience, product capability gap, price/value, organizational (M&A, champion loss, suite consolidation), other
- **Contributing factors** (several)
- **Turning point timing** relative to go-live
- **Destination** (which competitor or alternative)
- **Preventability:** was there a realistic window where you could have saved it?

Have two people code each account independently, then reconcile. This matters here because both VPs will read the results through their own lens, and a coding method agreed in advance makes the findings harder to dismiss.

## Fix the picklist going forward

Replace the single loss reason with:
- **Primary reason** from a sharper list (e.g., "never reached full adoption," "implementation exceeded plan," "specific capability gap," "acquired or merged," "consolidated onto core suite," "price relative to value," "champion departed")
- **Capability gap detail** (required if that reason is chosen): which capability
- **Competitor** (required if applicable)
- **Free text** summary, required
- **Exit interview completed?** Yes/no

Also trigger exit interviews automatically when a non-renewal notice arrives, not months later. Better still, run "risk interviews" with accounts showing churn signals while there's time to act.

If it helps, I can draft the outreach email, a one-page interview guide your interviewers can use, or a coding template for the analysis.

## Turn 3

**User:** How do I get both VPs to agree up front on what evidence would change their minds, without it turning into a political fight?

**Assistant:**

The key is to get commitments *before* anyone sees data, and to make agreeing feel safe rather than like conceding. Once results exist, people argue about interpretation; before results exist, they can usually agree on what a fair test looks like.

## Set the frame: a shared problem, not a trial

How you position this determines whether it feels like a verdict on someone.

- **Anchor on the business problem.** "Churn has doubled and we need to know where to put our next dollar" is neutral. "We need to figure out who's right" isn't.
- **Say out loud that both are probably partly right.** This is likely true, and it lowers the stakes. The question becomes *how much, for which customers*, not *who wins*.
- **Get your executive sponsor on board first.** Ideally the CEO or whoever owns the budget decision says: "I've asked [you] to run a churn diagnostic. I want both of you to shape it, and we'll use the results to allocate investment." This gives you authority as a neutral party and signals that sitting it out isn't an option.
- **Position yourself as the method owner, not a judge.** Your role is to make sure the analysis is fair and credible to both of them.

## Meet with each VP individually first

Don't start with a joint meeting. People posture in front of rivals and are more thoughtful one-on-one.

In each conversation:
1. **Let them make their full case.** Listen genuinely. You'll learn things, and they'll feel heard, which makes them more flexible later.
2. **Ask what they'd expect to see if they're right.** "If product gaps are the main driver, what would we see in the churn data?" Most people can answer this readily, and their answers become testable predictions.
3. **Then ask the harder question: what would they expect to see if they're wrong?** Frame it as rigor, not doubt: "What result would make you think implementation is the bigger factor?" Some will resist; ask it as "what would convince the skeptics on the leadership team?"
4. **Ask what analysis they'd consider unfair.** This surfaces their objections to the method now instead of after the results.
5. **Ask what outcome they could live with.** Often each VP mainly needs something specific: Product wants protection for a key roadmap item; Services wants headcount. Knowing this helps you design a decision rule both can accept.

Write down their predictions in their own words and send them back for confirmation. That written record matters later.

## Then run a joint session to agree on the method

Bring them together with a draft you've built from both conversations. Working from a draft is much easier than starting from a blank page.

**Agree on:**
- **The questions**, framed neutrally, such as "What share of churned revenue is primarily driven by implementation and adoption failure vs. capability gaps vs. other causes, and how does this vary by segment?"
- **The evidence sources**: exit interviews, usage data, implementation records, support history
- **The coding method**: root-cause categories, definitions, and who does the coding (two independent coders is a good answer to "who decides?")
- **The predictions**: each VP's written predictions, side by side
- **The decision rule**: how results translate into action (more on this below)

**Techniques that keep it from becoming a fight:**
- **Put both hypotheses on equal footing visually.** A two-column table, same level of detail. Any asymmetry will be noticed.
- **Invite each to strengthen the other's test.** "Is there anything that would make the product-gap test more convincing to you?" This is surprisingly defusing; it's hard to argue that a test is rigged when you helped design it.
- **Include the third category explicitly**: consolidation, suite bundling, champion loss, price. It prevents a zero-sum framing, and if it turns out to be large, neither VP "loses."
- **Keep the conversation on the method.** When someone starts arguing the conclusion ("but we all know the AI gap is killing us"), redirect: "Great. What would we see in the data if that's true? Let's make sure the analysis can detect it."

## Make the decision rule concrete

This is where commitment becomes real. Vague agreements ("we'll follow the data") dissolve under pressure. Specific ones hold.

Examples:
- "If more than half of churned ARR is primarily attributed to implementation or adoption failure, we'll fund the onboarding initiative before accelerating analytics work."
- "If capability gaps are the primary cause for more than half of churned ARR among fully implemented customers, we'll accelerate the analytics roadmap."
- "If results differ by segment, we'll match investments to segments."
- "If neither dominates, we'll prioritize work that addresses both, like integration tooling or out-of-the-box dashboards."

The exact thresholds matter less than agreeing on them in advance. Frame the rule as proportional investment rather than winner-take-all. That's both more likely to be correct and much easier for each VP to accept.

## Build in face-saving and ongoing involvement

- **Show interim results to both at once.** Never let one VP see findings first. Unequal access is the fastest way to lose trust in your neutrality.
- **Share raw material, not just conclusions.** Let them read anonymized interview notes. People accept findings more readily when they've seen the evidence themselves.
- **Report findings as "we learned," not "X was right."** Credit good predictions from both sides; there will almost certainly be some.
- **Give each a role in the solution.** Whatever the result, both VPs will be needed to fix it, especially since implementation friction is often partly a product problem.

## If it starts to go sideways

- **One VP won't commit to predictions:** "Help me understand what you'd need to see to be confident. If there's no possible result that would change the plan, we don't need the study." Said calmly, this usually prompts engagement.
- **One VP attacks the method after the fact:** Return to the written agreement. "This was the method we agreed on. If there's a genuine flaw, let's look at it, but let's apply the fix to both hypotheses equally."
- **It escalates into a personal conflict:** Bring the executive sponsor in early rather than trying to manage it alone. It's their decision, and they may need to reinforce that both leaders are expected to engage in good faith.

## A suggested sequence

1. **Week 1:** Brief your sponsor; get their explicit backing and framing.
2. **Week 1–2:** One-on-ones with each VP; document predictions and concerns.
3. **Week 2:** Joint session to agree on method and decision rule; circulate a one-page written summary for sign-off.
4. **Weeks 3–7:** Run the diagnostic, with a brief check-in midway (method only, no findings).
5. **Week 8:** Present findings to both VPs together, then jointly to the sponsor.

If useful, I can draft the one-page "diagnostic charter" for the VPs to sign off on, or a set of questions for the one-on-ones.

## Turn 4

**User:** What if the findings come back and a lot of the churn traces to things my own CS team should have caught, like at-risk accounts or champion changes?

**Assistant:**

Then you report it, clearly and early. This is the moment that determines whether the diagnostic, and your neutrality, has any credibility. You've asked two VPs to commit to changing their minds based on evidence. If the evidence points at your team and you soften it, both of them will notice, and neither will accept findings that touch their own areas.

The good news is that owning it well usually builds your standing rather than damaging it.

## Add your own hypothesis now, before results exist

Don't wait to see if this happens. Put it in the charter today:

- Add a root-cause category like **"detectable risk not acted on"**: champion departure, declining usage, escalating tickets, or a stalled implementation that CS could have seen but didn't escalate or address in time.
- Tell both VPs and your sponsor you've added it, and why: "If we're testing Product and Services, we should test CS too."

This does three things. It makes the study visibly fair, it shows the VPs you're holding yourself to the standard you're asking of them, and it means a finding against your team is something you anticipated rather than something that was uncovered.

## Distinguish "should have caught" from "could have caught"

When the findings come in, dig into why risk was missed. The answer determines the fix:

- **Did CS have the signal?** If usage data, support trends, or contact changes weren't visible to CSMs, that's a tooling or data problem.
- **Did CS have the capacity?** If each CSM carries 40 accounts, proactive risk detection is aspirational. That's a coverage and resourcing problem.
- **Was it anyone's job?** If no one owned monitoring champion changes or tracking multi-threading, that's a process and role-design problem.
- **Did CS see it and escalate, but nothing happened?** This is common and important. Check whether flags went to Services, Product, or Sales and stalled. If so, the failure is in the handoff, not detection.
- **Was it individual performance?** Sometimes, yes. But if the pattern spans many accounts and CSMs, it's systemic.

Most of the time, the answer is a mix of the first four, which is fixable and not a personal indictment of your team.

## Keep it in proportion

Two things can be true at once:

- **CS missed signals it could have caught.** That's real, and you should fix it.
- **Catching risk doesn't remove the cause.** If a customer is drifting because the implementation stalled or the product lacks something they need, earlier detection buys time to intervene, but someone still has to fix the underlying problem.

Code "detectable risk not acted on" as a **contributing factor alongside the primary root cause**, not as a replacement for it. Otherwise CS becomes a convenient catch-all that lets everyone else off the hook, which is neither accurate nor useful. You're not trying to minimize your team's share, just to make sure the study still answers the original question.

## Present it before anyone else can

- **Tell your sponsor first, privately and early**, as soon as the pattern is clear. Executives hate being surprised by bad news about someone's own team in a group meeting.
- **Present it yourself, in the main findings, not buried in an appendix.** State it plainly: "About X% of churned ARR had detectable risk signals CS didn't act on in time. Here's what we found about why."
- **Bring a plan with it.** For example: a health score combining usage, support, and implementation status; champion and executive-sponsor tracking with multi-threading targets; a defined escalation path with response commitments from Services and Product; a review of CSM coverage ratios.
- **Be specific about what you need from others.** If escalations stalled, say so factually, without blame. This naturally connects CS's fix to the other teams' work.

## Protect your team while holding them accountable

- **Run it as a blameless review.** Focus on systems, signals, and decisions, not on individuals. If one or two people genuinely underperformed, handle that separately and privately.
- **Tell your team before leadership hears it.** Explain what the data showed, that you've taken ownership of it upward, and what's changing. They'll hear about it anyway; hearing it from you first preserves trust.
- **Involve them in the fix.** Your CSMs likely know exactly which signals they couldn't see or which escalations went nowhere. Their input will make the new process better and help them feel like part of the solution.

## Why this helps you

A leader who runs a fair process, finds a problem in their own area, and shows up with a clear fix earns something valuable: credibility the next time they need to tell a peer something uncomfortable. It also makes it much harder for either VP to reject findings about their own areas. You'll have already shown what accepting difficult evidence looks like.

If you'd like, I can help you draft the "detectable risk" category definitions for the charter, or outline a customer health score based on the signals you have available.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the whole thing as one plan. The short version: **don't pick a side yet, but don't wait to act either.** Run a fast, fair diagnostic, and in parallel take the steps that make sense no matter which VP is right.

## My honest prior

If I had to bet before seeing your data: in enterprise software with long implementations sold to organizations with thin IT teams, like regional carriers, **slow time to value is more often the primary churn driver than missing features**, and "competitor has better AI" is frequently the story customers tell once they've already stopped getting value. But capability gaps become decisive at renewal once a customer is shopping. And carrier consolidation and suite bundling could be a bigger factor than either VP expects.

That's a starting hypothesis, not a conclusion. Your data should decide it.

## The plan

### This week
- **Brief your sponsor** (CEO or budget owner). Get explicit backing to run an 8-week churn diagnostic with a commitment to allocate investment based on it.
- **Pull a list of renewals in the next 6–12 months** and flag the at-risk ones: stalled implementations, declining usage, rising tickets, champion changes.

### Weeks 1–2: Set up the diagnostic
- **One-on-ones with each VP.** Capture their predictions, what would change their minds, and what they need to be able to live with the outcome.
- **Joint session to sign off on a one-page charter:** the questions, data sources, root-cause categories (including consolidation/suite, price, and "detectable risk CS didn't act on"), coding method, and a proportional decision rule.
- **Start outreach** for 12–20 exit interviews, conducted by someone neutral (ideally a third party).
- **Fix the CRM loss-reason picklist** so future data is usable.

### Weeks 1–8: No-regret moves, in parallel
These make sense regardless of what the diagnostic finds:
- **Save plans for at-risk renewals.** Executive outreach, adoption reviews, targeted services help.
- **Triage stalled implementations.** Get every customer stuck short of go-live to first value quickly.
- **Start tracking time to value** for every new customer.
- **Build a basic health score and champion tracking** so CS catches risk earlier.

### Weeks 3–7: Run the diagnostic
- Build the churn dataset (implementation, usage, support, ARR, destination) for churned and retained accounts.
- Run cohort analysis to find what changed 18 months ago.
- Complete exit interviews; debrief internal staff for accounts that won't talk.
- Two independent coders assign primary and contributing causes per account.
- Mid-point check-in with both VPs on method only, no findings.

### Week 8: Decide
- Present findings to both VPs together, then to your sponsor, including anything about your own team.
- Apply the decision rule you agreed on. Expect a **proportional split, likely varying by segment**, not a winner-take-all verdict.
- Give both VPs a role in the fix, and set a shared goal: **gross revenue retention**, with time to value as a leading indicator.

## If the findings are mixed, where to invest first

Prioritize work that addresses both hypotheses at once:
- **Integration and data migration tooling** that shortens implementations
- **Out-of-the-box dashboards and analytics** for claims leaders, so customers see value early and your analytics story competes with rivals
- **Better integration with the core systems** your carriers use (policy and billing), which helps against suite bundling too

Then fund the larger bets, whether that's an onboarding overhaul or an accelerated AI roadmap, in proportion to what the data shows.

## What success looks like in 6–12 months

- Time to value is falling for new cohorts
- Fewer implementations stall past plan
- At-risk accounts are flagged months before renewal, not weeks
- Gross revenue retention is trending back toward where it was before churn doubled
- Loss reasons in your CRM actually explain losses

If you want to start tomorrow, the most useful single artifact is the one-page diagnostic charter. I can draft it for you.

## Outcome summary (sent to Jev)

The recommendation is not to pick either VP's side yet, but also not to wait before acting. Run a fast, fair eight-week churn diagnostic, and in parallel take no-regret steps that make sense whichever explanation proves right.

The two explanations predict different patterns in the data and are probably linked. Customers who never reach full value become receptive to competitor AI demos, and painful implementations are often partly a product problem. The working prior is that slow time to value is more often the primary driver for regional carriers with thin IT teams, and that "competitor has better AI" is frequently the story told after value stopped. Capability gaps can still be decisive at renewal, and carrier consolidation, suite bundling, champion turnover, and price may matter more than either VP expects.

**Setup**
- Secure sponsor backing and a commitment to allocate investment based on the results.
- Hold one-on-ones with each VP to capture their predictions and what would change their minds.
- Get joint sign-off on a charter covering root-cause categories, including "detectable risk CS didn't act on," independent double coding, and a proportional decision rule.

**Diagnostic work**
- Run 12–20 neutral exit interviews built around timelines rather than "why."
- Build a churn dataset and a cohort analysis to find what changed.
- Fix the CRM picklist.

**No-regret moves, in parallel**
- Save plans for at-risk renewals.
- Triage stalled implementations.
- Time-to-value tracking.
- A health score and champion tracking.

At week eight, present findings to both VPs together, including any CS failings. Expect a proportional, segment-varying split rather than a single winner. Set gross revenue retention as the shared goal. If findings are mixed, invest first in work that addresses both explanations: integration and migration tooling, out-of-the-box dashboards, and core-system integrations. Fund larger bets in proportion to the evidence.
