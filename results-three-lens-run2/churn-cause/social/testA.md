# churn-cause/social/testA

Model: claude-opus-5-5 · 2026-09-24T15:32:22.958624+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

Nobody can tell you which belief is right from the outside, and right now neither VP can either. Both are offering plausible stories that happen to point toward their own function. What you can do is turn this from a debate into a question with an answer, probably within a few weeks, using data you likely already have.

## Why this isn't either/or

The two hypotheses often interact in a way that makes them hard to separate:

- **Poor implementation creates perceived product gaps.** A customer who never got your existing analytics configured will honestly tell you "the competitor has better analytics." They're comparing a demo to a half-deployed system.
- **"Your competitor has better AI" is an easy exit reason.** It's impersonal and hard to argue with. "Your implementation dragged on and our team never adopted it" is more awkward to say and sometimes reflects on the customer's own execution.
- **Real product gaps can also make implementations long.** Heavy customization and workarounds for missing capability show up as a services problem.

So expect the answer to be a mix. The useful question is what the mix is and which lever moves churn fastest.

## Also rule out other explanations

Churn doubling over 18 months suggests something changed. Before accepting either story, check:

- **What changed ~18–24 months ago?** A competitor launch, a major release, services turnover or offshoring, a new sales segment or comp plan, a price increase?
- **Carrier consolidation.** Regional carriers get acquired, and the acquirer's system usually wins. That churn isn't about you.
- **Core-system bundling.** Are customers moving to claims modules inside their policy/core platform (Guidewire, Duck Creek, etc.)? That's a strategic threat neither VP is describing.
- **Champion turnover** at customer accounts.
- **Who's churning.** Were recent cohorts sold to smaller or more complex carriers that were a poor fit from the start?

## Tests that distinguish the hypotheses

Pull every account that churned or downgraded in the last 18–24 months and compare them to retained accounts.

| Evidence | Points to services | Points to product |
|---|---|---|
| **Tenure at churn** | Concentrated at first renewal | Mature, long-tenured customers leaving |
| **Implementation outcome** | Churners had late, over-budget, or partial go-lives | Churners implemented on time and fully |
| **Adoption before churn** | Low usage, key modules never turned on | Healthy usage, then left anyway |
| **Use of existing analytics** | Never adopted the analytics you already have | Used them heavily and hit their limits |
| **Support history** | High ticket volume, escalations, slow resolution | Support was fine; feature requests piled up |
| **Where they went** | Often a simpler tool, or a competitor with a strong services reputation | A competitor with specific capabilities you lack |
| **New-business win/loss** | Winning deals fine; problems start post-sale | Losing new deals on the same features |

Two of these are especially telling:

1. **Did churned customers use the analytics you already have?** If most never adopted them, "competitors have better analytics" is probably not the real story, and building more analytics they won't adopt won't help.
2. **Are you losing new deals on features?** Win/loss data is the cleanest read on product competitiveness because implementation experience isn't involved yet. If sales is winning on features but you're losing customers after the sale, that points to services. If you're losing both, the product gap is real.

**Exit interviews:** Have someone neutral conduct them, ideally a third party or at least not the account's CSM or the product team. Talk to both the executive who signed the non-renewal and the daily users. Ask when they started evaluating alternatives and what triggered it. The trigger (a failed go-live, a botched upgrade, a new CIO, a competitor demo) is often more revealing than the stated reason.

**Current customers:** Apply the same lens to your book. Which accounts look like past churners (stalled implementation, low adoption, rising tickets)? That tells you whether the pattern is continuing and gives you a rescue list.

## What to do

**1. Run the diagnosis quickly, and make it a joint exercise.** Four to six weeks is enough. Agree with both VPs up front what evidence would support each view, *before* seeing results. That keeps either side from reinterpreting the data afterward. You're a reasonable owner, but CS has its own stake in the outcome, so being transparent about the method matters.

**2. Meanwhile, take no-regret actions:**
- Build a risk list of accounts renewing in the next 6–12 months and start saving them now.
- Define a clear "time to first value" milestone and track it for every new implementation.
- Have product validate the specific competitive gaps customers name. "AI features" is vague; find out which workflows are affected (fraud flags, reserve recommendations, triage, document extraction) and how often they actually decide deals.

**3. Allocate based on what you find.**
- **Mostly services:** Prioritize implementation methodology, staffing, and adoption programs. Point product capacity at reducing implementation complexity (configuration tooling, templates, integrations) rather than new headline features. That work is product investment, and it bridges the two camps.
- **Mostly product:** Accelerate the roadmap on the specific gaps confirmed by win/loss and exit data, not on generic "AI."
- **Mixed, the likely case:** Sequence it. Fix the implementation path first for the highest-value segment, because new features delivered into a broken onboarding process mostly add complexity and lengthen implementations. Close the one or two competitive gaps that demonstrably cost deals in parallel.

**4. Set up ongoing measurement.** Track churn by cohort, time-to-value, and adoption of key modules, plus win/loss reasons, and review them quarterly with both VPs. That way you won't be settling the next disagreement by argument.

If you can share what data you have access to (usage telemetry, implementation timelines, CRM churn reasons, win/loss notes), I can help you design the specific analysis or a draft exit-interview guide.

## Turn 2

**User:** How do I get honest answers in exit interviews when some of these customers left on bad terms and might not want to talk to us at all?

**Assistant:**

The customers who left angriest are often the most informative, and also the hardest to reach. A few principles make a big difference.

## Choose the right person to ask

**Use someone with no stake in the relationship.** Former customers won't be candid with the CSM who managed them or the account exec who sold them, and they'll suspect a win-back pitch. In rough order of how well they work:

- **A third-party research firm** that specializes in win/loss or churn interviews. They can offer anonymity ("we'll share themes, not attribute comments to you"), which is the single biggest unlock for candor. This is worth paying for on your most important or most hostile accounts.
- **A senior executive who wasn't involved,** such as your CEO or a peer executive. For customers who left on bad terms, a direct note from the top can land well: "I understand we let you down. I'm not trying to win you back; I want to understand what happened."
- **An internal researcher or someone from another team,** if budget is tight. They must be clearly separate from the account team.

## Make the ask easy to accept

- **Acknowledge the history plainly.** Something like "I know things didn't end well, and I understand if you'd rather not talk." Don't grovel or relitigate. Recognizing the frustration often defuses it.
- **Say explicitly that this is not a sales call,** and mean it. If anyone pivots to a win-back offer during an interview, word gets around and future requests fail.
- **Keep it short and specific.** "Twenty minutes" gets far more yeses than "an hour to share feedback."
- **Explain why it matters.** "We've seen churn increase and we're trying to fix the root cause. Your experience is the most useful input we could get." People who were frustrated often want to be heard, and some will welcome the chance to say "I told you so" to someone who's finally listening.
- **Consider a thank-you gesture carefully.** Many insurance carriers restrict gifts to employees. A charitable donation in their name is usually safe. Check their policies.

## Reach the right people

- **Talk to more than the signer.** The executive who ended the contract gives you the official reason. The claims managers and adjusters who used the system daily give you the real experience. Try to interview both at key accounts.
- **Look for people who've moved on.** Former champions who've since changed companies are often the most candid, because they no longer have to defend their old employer's decisions or relationships.
- **Use indirect sources.** Implementation consultants, integration partners, and industry peers often know why an account left.

## Run the interview for truth, not validation

- **Ask for the story, not the reason.** "Why did you leave?" gets a tidy, rehearsed answer. Instead try: "Take me back to when you first started thinking about alternatives. What was happening?" Then walk forward through the timeline.
- **Find the trigger.** Ask what event started the evaluation: a failed go-live, a bad upgrade, a new executive, a competitor demo, a renewal price.
- **Probe stated reasons neutrally.** If they say "better analytics," ask "Which reports or decisions were you trying to support? Were you using our analytics module at the time?" This separates genuine product gaps from value never realized.
- **Never defend or correct.** Even when they're factually wrong, the interviewer's job is to understand their perception. Push back and the interview is over, even if they stay on the call.
- **Ask what could have changed the outcome.** "Was there a point where something we did differently would have kept you?" This often surfaces the pivotal moment.
- **End with an open door.** "Is there anything I didn't ask that I should have?" often produces the most useful answer of the call.

## For customers who won't talk

- **Offer a lower-effort option.** A three-question email or short survey, answerable in two minutes, sometimes succeeds where a call request fails.
- **Accept the no gracefully.** A respectful response ("Understood, thanks for considering it") preserves the relationship. Some former customers come back years later.
- **Check for legal issues first.** If an account has an active dispute, billing conflict, or litigation, have legal review before anyone contacts them.

## Account for bias in what you hear

The customers who agree to talk aren't a random sample. They may skew toward those who are less angry, or unusually vocal. So:

- **Triangulate with behavioral data.** Implementation timelines, usage, and support tickets can't be spun, and they cover accounts that refuse to talk.
- **Compare interview themes across churn severity.** If the few hostile accounts who do respond tell a different story from the cordial ones, that difference is itself a finding.
- **Don't overweight a single dramatic interview.** Look for patterns across 10–15 conversations before drawing conclusions.

A well-run set of even a dozen interviews, combined with the account data from the earlier analysis, should be enough to tell you whether you're mostly facing a services problem, a product problem, or something else entirely. I can draft an outreach email or a full interview guide if that would help.

## Turn 3

**User:** How do I get both VPs to agree on the evidence criteria up front when each of them is already pretty sure they're right?

**Assistant:**

You probably won't get either VP to doubt their view before the analysis. You don't need to. You need them to agree on what evidence would count, which is easier because each is confident the evidence will favor them. Confidence works in your favor here.

## Meet with each VP individually first

Don't open with a joint meeting where both feel they have to defend their position in front of the other. Talk to each one alone.

- **Start with their view, taken seriously.** "Walk me through why you think it's product (or services). What have you seen?" Listen fully. People are far more willing to commit to a test once they feel heard.
- **Ask what their hypothesis predicts.** "If you're right, what should we see in the churn data?" A confident person will happily answer. Their answers become your evidence criteria, in their own words.
- **Then ask the key question:** "What would you expect to see if you were wrong?" Frame it as rigor, not doubt: "I want this to hold up when we present it to [CEO], so I want to rule out the alternative."
- **Listen for what's really at stake.** Usually it's budget, headcount, and credibility. The Product VP may fear losing roadmap capacity; the Services VP may fear being blamed for churn. Knowing this helps you frame the process so it doesn't feel like a trial.

## Frame the goal as fixing churn, not picking a winner

In the joint session, set it up explicitly:

- "The question isn't which of you is right. It's what share of churn traces to each cause, so we put money where it moves the number."
- Say plainly that the answer is likely to be a mix. That makes it much easier for each VP to engage, because partial validation is the probable outcome, not total defeat.
- Point out that each of them has evidence the other lacks. Product sees win/loss and feature requests; Services sees implementation reality. The diagnosis is stronger with both.

## Write the criteria down before anyone sees data

This is the core step. Agree on a short document covering:

1. **Each hypothesis and its predictions**, in their words from the one-on-ones. For example, services predicts churn clusters at first renewal among accounts with delayed go-lives; product predicts fully implemented, active customers leaving for specific competitor capabilities.
2. **Other possible explanations** (consolidation, core-system bundling, pricing, champion turnover), so a result where neither was right is also allowed.
3. **Definitions.** What counts as churn, a delayed implementation, "adopted," and which time window you'll use. Most post-hoc arguments are really about definitions, so settle them now.
4. **Data sources and who does the analysis.** Both VPs should be able to check the work. Offer each the chance to add one test they think the other would overlook. That buys ownership.
5. **What happens next.** How findings will translate into decisions, and when you'll review them.

Have both VPs sign off, even informally by email. Share it with your executive sponsor.

## Get an executive sponsor

If you report to the same executive as the two VPs, or if the CEO or COO cares about churn (they should, at double the rate), get that person to endorse the process before the joint meeting. A simple "I want us to settle this with data; please work with [you] on the criteria" changes the dynamic. You're no longer a peer asking VPs to submit to your test; you're running a process the company requested.

Be candid with the sponsor about your own position: CS has a stake too, since churn lands on your team. Offering to have someone outside all three teams, or an outside firm, run parts of the analysis strengthens your credibility.

## Separate the diagnosis from the budget decision

Much of the resistance comes from the fear that the analysis will immediately cost someone budget. Reduce that by sequencing:

- **Phase 1:** Agree on what's causing churn.
- **Phase 2:** Decide how to respond.

In Phase 2, show that a services-heavy answer can still mean product investment. Reducing implementation complexity through better configuration tools, templates, and integrations is product work. A product-heavy answer still needs implementation capacity to deliver it. Neither VP needs to lose outright.

## Handle predictable pushback

- **"We already know the answer."** "Great, then this will confirm it quickly and give you airtight support with [CEO]. It's four weeks."
- **"Exit interviews are biased" or "The data's incomplete."** Agree, and ask what they'd add or how they'd weight it. Build their concern into the criteria rather than arguing.
- **Adding conditions after results come in.** Point back to the signed criteria. This is exactly why you wrote them down. If a genuinely new question comes up, treat it as a follow-up study, not a reason to discard the findings.
- **Refusing to engage.** Escalate to the sponsor, framed neutrally: "I need alignment on the criteria to finish this. Can you help?"

## Present the findings in a way that saves face

When results come in, present them against the predictions each VP made, not as a verdict on the person. Highlight what each got right, because both likely got something right. Then move straight to what you'll do. The point is shared ownership of the fix, not a scoreboard.

If it would help, I can draft a one-page criteria template or talking points for the one-on-ones.

## Turn 4

**User:** What if our implementation dates and usage data are spotty or inconsistent across accounts? Can we still run this analysis?

**Assistant:**

Yes. Spotty data is normal, especially for implementations that happened years ago. You'll need to reconstruct what you can, use coarser measures, and be honest about how confident you are. The analysis doesn't need precision; it needs to be good enough to show which way the evidence leans.

## Start with a data audit

Before any analysis, build a simple spreadsheet of every account in scope (churned and retained) and record what you have for each: implementation start, go-live date, usage data, support history, contract dates. This tells you:

- How much of the population has usable data
- Whether gaps are random or concentrated in certain periods, segments, or teams
- Which proxies you'll need

## Reconstruct from indirect sources

Implementation and adoption usually leave traces even when nobody recorded them cleanly:

- **Contracts, SOWs, and change orders.** Signed dates, planned go-live dates, and scope changes. Repeated change orders often signal a troubled implementation.
- **Billing records.** Services invoices, milestone payments, and total services hours versus the original estimate. Overruns are a strong proxy for a hard implementation.
- **Project tools and email.** Old project plans, kickoff and go-live announcements, status reports.
- **System logs.** First login, first claim processed in production, when integrations went live, when key modules were first used. Even without full usage telemetry, first-use dates are often recoverable.
- **Support tickets.** Ticket volume, severity, and escalations over time. A spike that never subsides after go-live tells a story.
- **People.** Implementation leads, CSMs, and support engineers often remember which accounts struggled. Record their recollections, but treat them as the weakest source and confirm with documents where possible.

## Use coarse categories instead of precise numbers

You may not know that an implementation took 14.5 months, but you can probably classify it. For example:

- **Implementation:** on time / late / very late or never fully live
- **Adoption:** core modules in active use / partial / minimal
- **Analytics usage:** used regularly / used occasionally / never set up

Coarse categories are much easier to fill in consistently, and they're enough to test the hypotheses. You're looking for a big difference between churned and retained accounts, not a small statistical effect.

## Keep the reconstruction honest

When people fill gaps after the fact, bias creeps in. Guard against it:

- **Write the classification rules first.** For example, "late" means go-live more than 90 days after the SOW date. Apply the same rules to every account.
- **Classify without knowing the outcome, where possible.** Have someone who doesn't know which accounts churned do the classification, or at least classify retained and churned accounts together rather than in separate batches.
- **Record the source and confidence for each data point** (documented, inferred from proxy, or someone's recollection). This lets you check whether conclusions hold up using only the well-documented accounts.

## Treat missing data as a possible finding

Check whether missingness itself correlates with churn. If the accounts with no clear go-live date or no usage data are disproportionately the ones that churned, that's meaningful. It may indicate implementations that never reached a clean finish, or accounts nobody was actively managing.

## Adjust the analysis to fit the data

- **Analyze the well-documented subset first.** If 40 accounts have solid data, that's often enough to see a clear pattern. Then check whether the less complete accounts point the same way.
- **Run the analysis both ways.** Once including inferred data and once excluding it. If the conclusion holds either way, you can be confident. If it flips, say so.
- **Lean harder on evidence that doesn't depend on your records.** Win/loss data, exit interviews, and support tickets can carry more weight where implementation and usage data are weak.
- **Look for consistency across sources.** If billing overruns, ticket spikes, staff recollections, and exit interviews all point to the same accounts, that's strong evidence even if no single source is complete.

## Update the criteria with both VPs

Since you're agreeing on evidence criteria up front, bring the data limitations into that conversation. Agree on which proxies count, the classification rules, and how much confidence each source carries. That keeps the result from being dismissed later with "the data's bad," because both VPs accepted the method in advance. Neither side can then selectively trust data only when it supports them.

## Fix it going forward

Whatever the analysis shows, the gaps are a finding. If you can't reliably tell when customers went live or whether they're using the product, you can't manage churn proactively. As part of the outcome, define a small set of fields every account must have (contract date, planned and actual go-live, key module adoption, health score) and assign an owner for keeping them current. Then the next time this question comes up, the answer takes days rather than weeks.

If you tell me which data sources you have access to, I can help design the classification scheme or the audit spreadsheet.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the plan pulled together, in the order I'd do it.

## Where I'd bet, and why you still need to check

If I had to guess, I'd expect implementation and adoption to explain more churn than your Product VP believes. In enterprise software with long implementations, customers who never reach full value are a very common source of churn, and "the competitor has better features" is often the stated reason even when the real problem is that value was never realized. But there's probably a real, narrower product gap too, and something else could matter as well, such as carrier consolidation or core-platform bundling. Treat this as a hypothesis to test, not a conclusion.

## Weeks 1–2: Set up

- **Get an executive sponsor.** Ask the CEO or COO to endorse a data-driven diagnosis of churn, with you coordinating.
- **Meet each VP one-on-one.** Ask what their hypothesis predicts and what they'd expect to see if they were wrong.
- **Agree on written criteria.** Predictions, definitions, proxies for missing data, classification rules, and how findings will lead to decisions. Get both VPs to sign off.
- **Start the data audit.** List every account in scope and what data exists for each.
- **Start no-regret actions now** (see below). These shouldn't wait for the analysis.

## Weeks 2–6: Diagnose

- **Reconstruct and classify accounts** using contracts, billing, logs, and tickets, applying the agreed rules without knowing churn status where possible.
- **Run the comparison** between churned and retained accounts: tenure at churn, implementation outcome, adoption, analytics usage, and support history.
- **Pull win/loss data** on recent new deals to test product competitiveness independent of implementation.
- **Conduct 10–15 exit interviews,** ideally through a third party for the most important or hostile accounts, focusing on the timeline and the trigger that started their search.
- **Check the alternative explanations:** acquisitions, core-system bundling, pricing changes, and what changed 18–24 months ago.

## Week 6–7: Decide

Present the findings against each VP's predictions, then allocate:

- **Mostly services:** Fund implementation methodology, staffing, and adoption programs. Point product capacity at reducing implementation complexity through configuration tools, templates, and integrations.
- **Mostly product:** Accelerate the specific gaps confirmed by win/loss and exit data, not "AI" in general.
- **Mixed, the likely case:** Fix the implementation path for your most valuable segment first, and close the one or two competitive gaps that demonstrably cost deals in parallel. Avoid shipping major new features into a broken onboarding process; that usually makes implementations longer.

## Start these now, whatever the diagnosis

- **Rescue upcoming renewals.** Flag accounts renewing in the next 6–12 months that show stalled implementations, low adoption, or rising tickets, and put a save plan on each.
- **Track time to first value** for every new implementation, with a defined milestone and a named owner.
- **Clarify the competitive gap.** Have product identify which specific AI and analytics workflows customers mention and how often they appear in lost deals.
- **Fix data capture.** Require go-live dates, key module adoption, and a health score for every account going forward.

## Ongoing

Review churn by cohort, time to value, adoption, and win/loss reasons quarterly with both VPs. That turns this from a one-time argument into a shared operating rhythm and gives you early warning if the pattern shifts.

The most important move this week is getting the executive sponsor and the one-on-ones on the calendar. Everything else follows from that alignment. I can draft the sponsor pitch, the one-on-one talking points, or the criteria document if useful.

## Outcome summary (sent to Jev)

The assistant says neither VP's belief can be declared right without evidence, and recommends running a joint, data-driven churn diagnosis of about six weeks. Its tentative bet is that implementation and adoption explain more churn than the Product VP believes, because customers who never reach full value often cite competitor features as the reason for leaving. It also expects a real but narrower product gap, and says other causes such as carrier consolidation or core-platform bundling could matter. It treats all of this as a hypothesis to test, not a conclusion.

The setup comes first: secure a CEO or COO sponsor, meet each VP one-on-one to learn what their hypothesis predicts and what would show it wrong, and get both to sign written criteria covering definitions, proxies and classification rules. Then audit existing data. Where records are spotty, reconstruct accounts from contracts, billing, logs and tickets using coarse categories, classifying without knowing churn status where possible. Compare churned and retained accounts on tenure, implementation outcome, adoption, analytics usage and support history. Pull win/loss data, run 10–15 neutral exit interviews focused on what triggered each customer's search, and check the alternative explanations.

The decision depends on the results. If the cause is mostly services, fund implementation work and point product effort at reducing implementation complexity. If it is mostly product, close only the specific confirmed gaps. In the likely mixed case, fix onboarding for the most valuable segment first and close one or two deal-losing gaps in parallel, avoiding new features shipped into a broken onboarding process.

Some actions should start immediately: rescue at-risk renewals, track time to first value, clarify the specific competitive gaps, and fix data capture. After that, review the key metrics quarterly with both VPs.
