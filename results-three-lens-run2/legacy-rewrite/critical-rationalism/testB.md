# legacy-rewrite/critical-rationalism/testB

Model: claude-opus-5-5 · 2026-09-24T15:23:51.973943+00:00

## Turn 1

**User:** You are a world-class philosopher of science.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

# Short answer

Your head of product is closer to right, but your CTO is right about something important. The best strategy uses the CTO's destination (a genuinely modern platform, not endless patching) and the product head's route (incremental replacement while shipping). What you should avoid is a two-year, big-bang rewrite of the system that carries most of your revenue.

# Why the big-bang rewrite is the riskier bet

**1. The old code is the real specification.**
A 20-year-old P&C policy system encodes thousands of decisions nobody wrote down: state-specific filing rules, rating quirks, endorsement edge cases, workarounds for one carrier's data from 2011. Michael Polanyi called this *tacit knowledge*: we know more than we can tell. A rewrite assumes you can extract and restate that knowledge. You can't fully, especially while your most experienced engineers are leaving and taking it with them. Many "bugs" in the new system will turn out to be rules the old one handled silently. Chesterton's fence applies at scale.

**2. A rewrite gives you almost no evidence until the end.**
Philosophers of science judge a research program by whether it keeps producing confirmed predictions (Lakatos's "progressive" program) or keeps explaining away delays (a "degenerating" one). A two-year rewrite is built to degenerate. For 18 months the only evidence of progress is internal demos. The moment of truth, migrating real carriers with real policies, comes last, when sunk costs are highest and admitting failure is hardest. Incremental replacement puts risky claims in contact with reality every quarter. Popper's advice holds: prefer the strategy that can be proven wrong early and cheaply.

**3. The base rates are bad.**
Big rewrites of core systems are notorious for overruns: Netscape is the famous case, and insurance core-system replacements are a well-known genre of multi-year slippage. Brooks's "second-system effect" predicts the new design will overreach, trying to fix everything the old one got wrong. Meanwhile you freeze or slow features for two years while the competitors you're worried about keep shipping, and you run two systems at once.

**4. You're rebuilding the ship at sea.**
Otto Neurath compared knowledge to a ship that must be rebuilt plank by plank without ever reaching dry dock. Your business has no dry dock either. Customers, renewals, and regulatory changes don't pause.

# Check your diagnosis first

"Features take months" and "engineers leave" have several possible causes, and a rewrite fixes only some of them. Before committing, find out how much of the slowness comes from:
- the code itself (tangled domain logic, no seams),
- missing automated tests, so every change needs heavy manual regression,
- manual, infrequent, scary releases,
- team structure and handoffs (Conway's law: a new stack built by the same organization tends to reproduce the old architecture),
- an obsolete platform you can't hire for.

If much of the pain is tests, deployment, and organization, a rewrite spends two years relearning the same lessons on a new stack.

Similarly, ask whether "cloud-native" is actually costing you deals, and which capabilities buyers want: APIs, configurability, speed to launch products, hosted operations. Marketing labels aren't requirements.

# When the CTO would be right

A rewrite becomes defensible if several of these hold:
- The platform is truly dead: unsupported runtime, security exposure, no hiring pool.
- The core domain model can't represent what the market now demands (new lines, new product structures), so every change fights the foundation.
- The system is small or modular enough that "rewrite" really means replacing a few bounded pieces.
- You've tried to create seams and found none, even at the data and integration layers. This is rarer than people think.

Even then, a rewrite should be delivered in slices with real customers on it early, which starts to look like the incremental path.

# What I'd do

1. **Adopt the target architecture now.** Let the CTO define the destination, then pursue it through a "strangler fig" approach: new capabilities are built outside the old system and gradually take over its responsibilities.
2. **Spend the first 90 days on safety and seams.** Write characterization tests around critical behavior (rating, issuance, renewals), add instrumentation, automate deployment, and put an API or event layer in front of the legacy core.
3. **Choose a first slice that proves something.** Good candidates are rating, document generation, integrations/APIs, or ideally a new product or line of business built entirely on the new stack. It should reach a real customer within six to nine months.
4. **Protect the investment.** The common failure of incremental modernization is the strangler that never strangles: it stalls and leaves you with two systems forever. Prevent this by dedicating fixed capacity (roughly 30–40%) with named ownership, and by setting decommissioning targets. Success means pieces of the old system are switched off, not just new pieces added.
5. **Use it to retain talent.** Engineers leave over toil and stagnation. Incremental work gets them building on the modern stack within months, not after a two-year slog.

# How to settle the disagreement

Turn the debate into testable predictions. Ask the CTO what evidence within 12 months would show incremental modernization is working or failing. Ask the head of product the same about the rewrite. Agree on measures:
- lead time for changes,
- release frequency,
- share of transactions handled by new components,
- legacy modules decommissioned,
- engineer attrition,
- win/loss reasons in sales.

Then commit to the incremental path with explicit checkpoints. If after a year the seams truly can't be cut, the CTO will have earned the evidence for a more aggressive replacement, and you'll be far better prepared to do it.

## Turn 2

**User:** How do I tell whether our slowness is really the code itself versus tests, deployment, or team structure?

**Assistant:**

# Diagnosing where the time actually goes

The core idea: **don't ask people why things are slow; trace where the time went.** Opinions about slowness usually reflect whoever holds them. The CTO will tend to see the code, product will tend to see process. The work itself leaves evidence. Four to six weeks of disciplined investigation should be enough.

## 1. Know what each cause looks like

Each cause leaves a different fingerprint.

| Cause | What you'd observe |
|---|---|
| **The code itself** | Active development time is large and estimates blow up during coding. Small changes ripple across many files and modules. The same hotspots recur. Changes break unrelated features. Only two or three people can safely touch key areas. New engineers take many months to become productive. |
| **Tests** | Long, fixed-length manual regression cycles. Bugs are found late, in QA or production, rather than during development. Engineers are afraid to change things they understand, because they can't verify the change. Work is batched because testing is expensive. |
| **Deployment** | Finished work sits waiting for a release window. Releases are infrequent, manual, and stressful. Environments are scarce or drift from production. Rollbacks are painful, so releases get even rarer. |
| **Team structure** | Work waits in queues between teams: handoffs, approvals, dependencies. Knowledge bottlenecks around specific people. Priorities shift, so work is started, paused, and restarted. |
| **Upstream requirements** (often overlooked) | Rework caused by unclear or changing specs. Long waits for regulatory or actuarial analysis. Features that are "done" but get reopened. |

## 2. Reconstruct the timelines of recent work

This is the most valuable step. Pick 15–25 features or significant changes delivered in the past year, a mix of large and small. For each, rebuild the timeline from "someone decided we'd do this" to "running in production for customers":

- Break it into stages: requirements, design, development, code review, testing, release, and any waits in between.
- For each stage, separate **active work time** from **waiting time**.
- Use tickets, commits, pull requests, and deploy logs, then check them against short interviews. Tickets often misrepresent reality: they get opened late, closed early, or left in the wrong state.

Then compute **flow efficiency**: active time divided by total elapsed time. In struggling organizations it's commonly 10–20%.

This matters for your decision. **If most elapsed time is waiting, a rewrite won't fix it,** because the new system will wait in the same queues. If most time is active development that keeps expanding, the code is a real culprit.

## 3. Run a trivial-change probe

Choose a change that is genuinely tiny in code terms: a label, a validation message, a rate-table value, a new field on a form. Push it through your normal process and time every step.

- If a one-line change takes three to six weeks, **the bottleneck is not code complexity.** It's testing, release, and process overhead.
- If trivial changes flow quickly but real features stall, look harder at the code's structure.

It's a controlled experiment: you hold code complexity near zero and see what remains.

## 4. Analyze the code's history, not just the code

Your version control history is a record of where the pain lives. Tools such as CodeScene, or Adam Tornhill's techniques in *Your Code as a Crime Scene*, can identify:

- **Hotspots**: files that are both complex and frequently changed. Pain usually concentrates in a small fraction of the codebase, often 5–10%.
- **Change coupling**: files that always change together despite being in "separate" modules. This reveals hidden entanglement.
- **Blast radius**: how many files and modules a typical feature touches.
- **Knowledge concentration**: code that only one person, or a departed person, has ever modified.

This also informs your modernization plan. Concentrated pain means targeted fixes, and your first strangler slices, can go where they help most. If the entanglement is truly everywhere, the CTO's case gets stronger.

## 5. Measure your delivery baseline

Collect the four standard DORA metrics:
- deployment frequency,
- lead time for changes (commit to production),
- change failure rate,
- time to restore service.

These separate the delivery pipeline from the code. Quarterly releases with a high failure rate point to testing and deployment first. These metrics also become the scoreboard for whichever strategy you pursue.

## 6. Ask engineers about specific incidents

"Why are we slow?" invites narratives. Instead, ask about specific recent events:
- "Think of the last time you were blocked for more than a day. What were you waiting for?"
- "What's the last change you were afraid to make? What made it scary?"
- "Where did the time go on the last feature you shipped?"

Also re-read exit interviews from departed engineers. Did they leave over the stack, the toil, the fear, the bureaucracy, or the lack of growth? These call for different remedies.

## 7. Look for natural experiments

Compare across your own organization. Do some modules or teams deliver noticeably faster? If a team working in equally old code ships twice as fast, the difference is practices or structure, not the code's age. If every team is slow in the same modules, it's the code.

## Two cautions

**The causes interact, so don't expect a single culprit.** Philosophers call this the Duhem–Quine problem: you can rarely test one hypothesis in isolation, because each observation depends on other assumptions. Here, missing tests make engineers afraid to refactor, so the code decays. Tangled code makes tests hard to write. Team boundaries mirror the code's structure (Conway's law). You're not looking for the one true cause. You're looking for the **binding constraint**: the bottleneck that, if relieved, would speed things up most right now. Fixing anything else barely helps until that one moves.

**Guard against confirmation bias.** Your CTO and head of product each hold a hypothesis this investigation could support or undermine. Before collecting data, have both agree on what findings would favor each view. For example: "If more than half of lead time is waiting rather than active work, that argues against a rewrite being the main fix." Consider having someone without a stake in the outcome lead the investigation.

## What you should end up with

A one-page breakdown along these lines: *"Average lead time is 14 weeks. About 3 are active development, 4 are waiting on manual regression testing, 3 are waiting for a release window, and 4 are waiting on requirements and cross-team dependencies. Development time is concentrated in rating and endorsements, which account for 8% of files but 60% of change effort."*

A result like that tells you what to fix first, where to make your first modernization cut, and whether the code itself deserves most of the blame.

## Turn 3

**User:** How do I pitch this four-to-six-week investigation to the CTO without it looking like I'm stalling or trying to prove him wrong?

**Assistant:**

# Pitching the investigation to your CTO

The most important thing is to make the pitch true, not just clever. If you privately hope the data sinks his plan, he'll sense it, and the investigation will be tainted whatever it finds. So first make sure you'd accept either outcome. Then the pitch mostly consists of saying why the work serves him.

## 1. Frame it as groundwork for any strategy

Don't present this as "let's find out whether you're right." Present it as work that has to happen whichever strategy you choose, because it does:

- **A rewrite needs this map.** Hotspots, hidden coupling, and undocumented business rules are exactly what a rewrite team must know to avoid rebuilding the old system's problems or missing its edge cases.
- **A rewrite needs a baseline.** In two years, someone (the CEO, the board, the CFO) will ask whether the investment paid off. Without today's lead times, release frequency, and failure rates, he can't show the improvement.
- **It strengthens his budget case.** "We traced 20 features, and here's where the time goes" is far more persuasive to leadership than "the system is old."
- **It finds quick wins.** If manual regression testing or release windows are eating weeks, fixing them helps now and makes the eventual migration safer.

The honest summary: the investigation isn't an argument against his plan. It's due diligence his plan will need.

## 2. Make it clear nothing waits on it

"Four to six weeks of investigation" sounds like delay. Remove that concern directly:

- Rewrite architecture, stack evaluation, and hiring can all continue in parallel.
- It needs a small team for a fixed period, not a halt in delivery.
- It has a firm end date and a defined deliverable: the one-page breakdown, plus hotspot analysis and baseline metrics.

Put a date on it: "Findings by [specific date], in time to inform the Q3 plan."

## 3. Offer him co-ownership, and mean it

People resist investigations done to them and support ones they shape. Invite him to:

- **Name his hypotheses.** Ask what he expects the data to show. If he's right that the code is the binding constraint, this will demonstrate it.
- **Set the decision criteria in advance.** Agree together which findings would favor a rewrite, which would favor incremental work, and which would favor fixing testing and deployment first. Scientists call this pre-registration: deciding what counts as evidence before seeing the results, so nobody can reinterpret afterward.
- **Choose some of the features** to trace, so he can't later say the sample was cherry-picked.
- **Name a lead** he trusts, or co-sponsor it with you.

Include criteria that would genuinely support his view, for example: "If most lead time is active development that keeps expanding, concentrated in modules with no clean seams, that strongly supports a more aggressive replacement." If you can't write such criteria sincerely, you're not running an investigation.

## 4. Start by acknowledging what he's right about

Open with the points he's correct on, and say them sincerely:

- The status quo is not acceptable.
- Incremental work often turns into endless patching and never gets anywhere.
- The team needs a real destination, not just maintenance.
- Losing strong engineers is an urgent problem.

This shows you're not defending the old system, which is likely his biggest concern about anyone who questions the rewrite.

## 5. Choose the setting carefully

- **Talk to him privately first.** Don't raise it in a meeting where it looks like you and the head of product are ganging up on him.
- **Don't act as the head of product's messenger.** Present the idea as your own responsibility as the person accountable for engineering delivery.
- **Once he's shaped the plan, present it jointly** to the wider leadership as a shared initiative.

## 6. Prepare for predictable objections

**"We already know the problem. It's the code."**
"You may well be right, and this will show it quickly. But when we ask for a two-year budget, leadership will want evidence, and we'll want to know which parts of the code hurt most so we tackle them first."

**"This is analysis paralysis."**
"It's time-boxed to [date], with a single deliverable, and nothing else pauses. If we find nothing surprising, we've lost almost nothing and gained a baseline."

**"You're trying to kill the rewrite."**
"No. I'd rather we pick the strategy that works than win an argument. Let's agree now what evidence would justify the rewrite, and if we see it, I'll back it fully." Then keep that promise.

## A sample opening

> "I agree we can't keep going as we are, and I want your modernization plan to succeed. Before we ask leadership for a two-year commitment, I'd like to run a short, time-boxed diagnostic, finishing by [date], on where our delivery time actually goes. It gives us a baseline to prove the investment later, maps the parts of the system the new platform has to get right, and may turn up quick wins we can take now. Nothing else stops while we do it. I'd like you to help shape it: tell me what you expect to find and what results would change your mind, and I'll do the same."

## One last point

Ask him what would change his mind, and be ready to answer the same question yourself. That commitment is what makes this an investigation rather than a political maneuver. It's also what protects you if the evidence favors his plan: you'll have shown that you care about getting the decision right, and that's worth more than being proven correct.

## Turn 4

**User:** What if the CTO says yes but then disputes or dismisses the findings when they come back pointing away from a rewrite?

**Assistant:**

# When the findings meet resistance

Plan for this from the start, because it's a common outcome. Evidence rarely changes minds on its own. Kuhn observed that scientists committed to a paradigm often explain away contrary results rather than abandon their view. That usually isn't dishonesty. A two-year rewrite may be tied to the CTO's vision, his reputation, and commitments he's already made. Your job is to make the evidence hard to dismiss and easy to accept.

## 1. Make dismissal harder before the results arrive

Most of the work happens earlier:

- **Put the agreed criteria in writing.** A short document or email recording which findings would favor which strategy is much harder to reinterpret later than a remembered conversation.
- **Give him access to the raw data throughout.** Findings he's watched take shape are harder to reject than a finished report.
- **Share interim results.** Surprise creates defensiveness. If the data points away from a rewrite, he should see that trend in week two, privately, not in a leadership meeting in week six.
- **Include his chosen features and his nominated reviewer.** This undercuts later claims about a biased sample or method.

## 2. Tell legitimate critique from motivated dismissal

Not every objection is resistance. He may spot real weaknesses, such as a small sample, unreliable ticket data, or features that weren't representative. Take these seriously. Conceding valid points builds the credibility you'll need for the ones that stand.

A useful test is whether the objection is specific and testable, or vague and shifting:

- **Legitimate:** "Those 20 features were mostly small changes. Big features behave differently." You can check this by tracing some large features.
- **Motivated:** "The data doesn't capture the real problem." What real problem? How would we measure it? If the answer keeps changing or can't be stated, that's a warning sign.

Lakatos described this pattern: a theory under pressure gets protected by *ad hoc* adjustments, new assumptions invented only to explain away the awkward result. The sign is that each new objection appears after the previous one was answered, and none of them predict anything checkable.

## 3. Answer objections by asking what would resolve them

When he disputes a finding, don't argue. Ask:

> "What additional data would settle this for you?"

If he names something reasonable, collect it, within a fixed time limit. This turns disagreement back into investigation. If he can't name anything that would change his mind, you've learned something important, and it will become clear to others too. Stay calm and curious rather than pointing it out.

## 4. Don't overstate your findings

Diagnostics are rarely clear-cut. If the data shows that testing and release delays are the largest share of lead time, that doesn't prove a rewrite is wrong. It shows that a rewrite alone won't fix the biggest bottleneck. Claim exactly what the evidence supports:

- **Overclaiming:** "This proves the rewrite is a mistake."
- **Accurate:** "Most of our lead time is in manual testing and release waits. Any strategy has to fix those, and fixing them first gets results within months."

Precise claims are harder to attack and give him room to agree without surrendering.

## 5. Give him a way to accept the findings without losing face

This matters more than anything else. People rarely accept evidence that requires public defeat. Present the findings as refining his plan, not refuting it:

- **His destination stands.** The target architecture, the modern stack, and the ambition all remain. The data affects sequence and route.
- **Credit his insight.** Something like: "You were right that the code is a serious problem in rating and endorsements. The data shows that's exactly where to start."
- **Give him ownership of the revised plan.** Let him lead the modernization program, including building the first new components on the new stack. He gets to build the future; it just happens in stages.

The best outcome is one where he says "the diagnostic sharpened our plan," not "I was wrong."

## 6. Look for the concern behind the position

Persistent resistance often signals that the rewrite is serving another purpose. Ask him directly and privately what matters most to him. Possible answers:

- **Talent:** he believes only a greenfield project will attract and keep strong engineers. Incremental modernization can offer modern-stack work quickly, but you need to show how.
- **Credibility:** he's already promised the board or CEO a transformation. Help him present the staged plan as that transformation.
- **Frustration:** he's watched incremental efforts fail before. Address this with protected capacity, decommissioning targets, and clear milestones.
- **Vision:** he wants a clean architecture, not a compromise. Show how the staged plan reaches that architecture.

If you meet the underlying need, the dispute over the data often goes away.

## 7. If he still dismisses the evidence, escalate carefully

Sometimes none of this works. Then the question becomes who decides.

- **Understand decision rights.** If the CTO has authority over technical strategy, you can inform and advise, but he decides. If the decision belongs to the CEO or the executive team, it's legitimate for the evidence to reach them.
- **Don't go around him secretly.** Tell him first: "I think the CEO should see these findings alongside your recommendation, so the decision is made with both. I'd like us to present them together." That's transparent, not insubordinate.
- **Present both views fairly.** Include his critiques and the strongest case for the rewrite. Leaders trust people who represent opponents fairly.
- **Frame it as a business risk decision.** A two-year rewrite of the system that produces most of your revenue is a bet-the-company decision. The CEO deserves to make it knowingly.

## 8. Be prepared to lose gracefully, and check yourself

Two final points:

- **You may be wrong.** Apply the same scrutiny to your own interpretation that you'd apply to his. If you find yourself dismissing his objections as quickly as you suspect him of dismissing the data, take that seriously.
- **If leadership chooses the rewrite with the evidence in view, the decision has been made properly.** Your role then is to help it succeed: use the diagnostic to reduce its risks, push for early real-customer milestones, and keep measuring against the baseline. The baseline you created becomes the honest check on whether the rewrite is working, and gives the organization a chance to change course before it's too late.

You were never trying to win. You were trying to make sure a very large decision was made on evidence rather than conviction. If you manage that, you've done your job, whichever strategy the company chooses.

## Turn 5

**User:** What should we do?

**Assistant:**

# My recommendation

**Don't commit to a two-year rewrite now. Commit to modernization now,** with the destination fixed and the route decided by evidence. Concretely: run the diagnostic, fix the binding constraint it reveals, and start replacing the legacy system one real slice at a time, with protected capacity and decommissioning targets. Revisit a more aggressive replacement at a set checkpoint if the evidence calls for it.

I can't see your data, so this is a considered default, not a verdict. But given what you've described (revenue concentrated in one system, twenty years of tacit business rules, experienced engineers leaving), the downside of a failed rewrite is severe and the downside of a disciplined incremental start is small.

## The sequence

### This week
- **Talk to the CTO privately.** Agree that the status quo is unacceptable and that a modern platform is the goal. Propose the diagnostic as groundwork for any strategy, time-boxed with a fixed end date.
- **Write down the decision criteria together**: what findings would favor a rewrite, incremental modernization, or fixing testing and delivery first.

### Weeks 1–6: diagnose, and keep shipping
- Trace 15–25 recent features, splitting active time from waiting time.
- Run a trivial-change probe.
- Analyze version history for hotspots and hidden coupling.
- Capture the DORA baseline metrics.
- Interview engineers about specific recent blockers, and re-read exit interviews.
- Share interim results with the CTO as you go.
- Keep delivering customer features. Continue rewrite architecture and stack evaluation in parallel, since that work is useful either way.

### Week 6: decide, jointly
Present one page showing where the time goes and where the pain concentrates, measured against the criteria you agreed. Then:

- **If most lead time is waiting** (testing, releases, handoffs): fix those first. You'll see gains within months, and they're prerequisites for any safe migration.
- **If the pain is concentrated in a few modules**: make those your first replacement slices.
- **If entanglement is everywhere with no workable seams**: take the CTO's case seriously and plan a more aggressive replacement, still delivered in stages, with real customers on it early.

### Months 2–12: execute with teeth
- **Fix the binding constraint.** Most likely this means automated tests around critical behavior (rating, issuance, renewals) and automated deployment.
- **Build seams.** Put an API or event layer in front of the legacy core.
- **Ship a first slice on the new stack to a real customer within six to nine months.** A new product or line of business built entirely on the new platform is ideal.
- **Protect the work.** Dedicate roughly 30–40% of capacity, give it named ownership, and set targets for switching off legacy components. Success means old parts are retired, not just new parts added.
- **Put your strongest and most restless engineers on the new platform first.** This is also your retention plan.
- **Tie the "cloud-native" story to what buyers actually need**, such as APIs, configurability, faster product launches, and hosted operations, and ship those visibly.

### Month 12: checkpoint
Compare against the baseline: lead time, release frequency, failure rate, share of work running on new components, legacy modules retired, attrition, and win/loss reasons. If progress is real, keep going. If the seams truly can't be cut, you'll have the evidence, the team, and the knowledge to do a larger replacement much more safely than you could today.

## The principle behind it

Choose the path that teaches you the most, soonest, at the lowest risk to the business. A big-bang rewrite asks you to bet the company on predictions you can't check for two years. This plan puts every important assumption in front of real evidence within weeks or months, while customers keep getting value and your CTO's vision stays the destination.

Start with the conversation with your CTO this week.

## Outcome summary (sent to Jev)

The assistant recommends against committing now to a two-year, from-scratch rewrite. Instead it advises committing to modernization now, with the CTO's modern platform as the fixed destination and the route decided by evidence. That route is incremental "strangler fig" replacement while continuing to ship customer features. It calls this a considered default rather than a verdict, since it cannot see the company's data.

Its main reasons:
- The 20-year-old system encodes undocumented tacit business rules that departing engineers take with them.
- A big-bang rewrite produces little real evidence until the end, when sunk costs are highest.
- Base rates for core-system rewrites are poor, and the business has no "dry dock."
- The downside of a failed rewrite of the revenue-carrying system is severe, while a disciplined incremental start costs little.

The plan starts with a private conversation this week with the CTO. The two would agree the status quo is unacceptable and write down criteria for what findings would favor each strategy. Next comes a time-boxed diagnostic of about six weeks, run while delivery continues:
- tracing 15–25 recent features to separate active from waiting time
- a trivial-change probe
- hotspot and coupling analysis of version history
- DORA baseline metrics
- interviews about specific blockers

At week six, the response depends on what the diagnostic shows. If most lead time is waiting, fix testing and release first. If pain is concentrated in a few modules, those become the first slices. If entanglement is everywhere with no seams, a more aggressive, still-staged replacement deserves serious consideration.

Over the following months, the company would:
- add automated tests and deployment
- build an API or event layer in front of the legacy core
- ship a first new-stack slice to a real customer within six to nine months
- dedicate 30–40% of capacity with named ownership and decommissioning targets
- put restless top engineers on the new platform

A twelve-month checkpoint against the baseline decides whether to continue or escalate.
