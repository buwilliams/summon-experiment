# independent-lab/critical-rationalism/testB

Model: claude-opus-5-5 · 2026-09-24T15:19:57.912044+00:00

## Turn 1

**User:** You are a world-class philosopher of science.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

Neither strategy is right in the abstract. You and your CEO are each holding half of a well-documented truth, and the history of science and of firms shows how each half fails on its own.

## The philosophy-of-science lens

**Kuhn: normal science vs. revolutionary science.** Most scientific work is "normal science": puzzle-solving within an accepted paradigm. It is efficient, cumulative, and essential. But it is structurally bad at producing paradigm shifts, because its methods, incentives, and standards of success all presuppose the old paradigm. Anomalies get explained away. Revolutions tend to come from people at the margins: newcomers and those less invested in the old framework.

Your CEO is proposing normal science: improve within the existing paradigm. You are proposing that the paradigm itself is the problem. **Which of you is right depends on whether the company's troubles are puzzles or anomalies.**

**Lakatos: progressive vs. degenerating research programmes.** Lakatos offers a sharper test. A research programme is *progressive* when its adjustments lead to new successes. It is *degenerating* when it only patches failures after the fact. Ask honestly: over the last several years, have the company's fixes (new features, reorganizations, pricing changes) won new ground? Or have they mostly been defensive patches that explain away each lost deal? A degenerating programme rarely rescues itself from within.

**March: exploration vs. exploitation.** James March showed that organizations drift toward exploitation (refining what they know) because its returns are faster, more certain, and closer to home. Exploration pays off later, uncertainly, and often elsewhere. This contains a quiet logical problem in your mandate. **"Outsized results" and "existing systems, procedures, and talent" pull against each other.** Exploitation produces reliable, modest gains. Outsized results require variance, which the existing system is designed to suppress.

## The empirical record

The evidence points both ways:

- **Separation works for creation.** Lockheed's Skunk Works and IBM's PC team in Boca Raton succeeded partly because they were shielded from the parent's processes. Clayton Christensen's research on disruption found that incumbents rarely commercialize disruptive technologies from inside the mainstream organization, because the resource-allocation process starves them.
- **Separation often fails at transfer.** Xerox PARC invented the GUI, Ethernet, and laser printing, and Xerox captured little of it beyond printing. Independent labs frequently become "innovation theater": admired, isolated, and eventually defunded. The antibodies of the parent organization do not disappear. They wait for the reintegration moment.

The research that reconciles these is O'Reilly and Tushman's work on **organizational ambidexterity**. The units that succeeded were *structurally separate but strategically integrated*. They had their own processes, metrics, talent, and culture. They were also tightly linked at the senior leadership level, with shared access to the parent's real assets: customers, data, distribution, and domain expertise. In insurance software, those assets are huge advantages that a startup lacks.

## So what should you actually do?

**1. Diagnose before you prescribe.** Find out *why* customers are leaving and deals are being lost. Talk to churned customers and lost prospects yourself.

- If the causes are **sustaining problems** (bugs, slow implementation, poor service, missing features competitors have), the CEO is largely right. That is a execution problem, and a lab is a distraction from it.
- If the causes are **paradigmatic** (buyers want cloud-native, API-first, AI-driven, or embedded-insurance architectures that your core platform cannot become), you are largely right. Incremental work will not close the gap.
- Most likely it is both. That calls for a two-track answer.

**2. Frame the lab as ambidexterity, not escape.** "Independent of the large organization" will sound to your CEO like "I'm abandoning your people and your plan." Propose instead:

- **Separate:** its own team, processes, release cadence, and success metrics. Measure learning velocity and validated customer demand, not quarterly revenue.
- **Connected:** direct sponsorship from the CEO, privileged access to customers and data, and a few respected insiders recruited into it.
- **A transfer mechanism designed from day one:** who decides when something graduates, who funds scaling, and how the core organization is incentivized to adopt it rather than resist it.

**3. Earn the right to be revolutionary.** You are new, and the CEO hired you. Deliver one visible, fast win inside the existing organization in your first 90 days. That builds credibility, teaches you where the real constraints are, and turns the CEO into a sponsor rather than an opponent.

**4. Treat your own strategy as a hypothesis.** In Popper's spirit, state in advance what evidence would show your approach is failing, and invite the CEO to do the same for his. That turns a clash of convictions into a shared experiment. That shift may matter as much as any org chart.

**Bottom line:** your instinct that transformative innovation needs protection from the core is well supported. Your CEO's instinct that innovation must ultimately run through the existing organization is also well supported. The companies that turned around did both: they explored at the edge and deliberately wired the edge back to the core.

## Turn 2

**User:** How do I figure out whether our churn problems are "puzzles" or "anomalies" without it looking like I'm just trying to prove my own point?

**Assistant:**

The answer from philosophy of science is simple to state and hard to practice: **decide what would count as evidence before you look at it, and involve people who hope for the opposite answer.** Here is how to turn that into a concrete process.

## 1. Pre-register the criteria with the CEO

Before collecting any data, sit down with the CEO and agree on what "puzzle" and "anomaly" would look like. Write it down. This is the organizational version of pre-registration in science, which exists because researchers who define success after seeing the data reliably find what they wanted.

A starting list you could propose and let him edit:

**Signals the problems are puzzles (fixable within the current paradigm):**
- Customers leave for competitors that look like us (similar architecture, similar business model).
- Churn reasons are specific and operational: implementation failures, bugs, support response times, missing features on a checklist.
- Churn concentrates in accounts with identifiable bad experiences, such as a botched rollout or a lost account manager.
- We lose deals on price or on features we could build within the current platform.
- Past fixes measurably reduced churn in the segments where they were applied.

**Signals the problems are anomalies (the paradigm itself is failing):**
- Customers leave for competitors with fundamentally different approaches, including ones we didn't consider competitors.
- Customers who report being satisfied still leave. "We like you, but..." is a classic anomaly signature.
- The buyer has changed. New personas (a chief digital officer or product team instead of IT operations) run evaluations with criteria we weren't designed for.
- Requirements we fail on would require re-architecting rather than adding features.
- Past fixes didn't move the numbers, or churn simply moved to a new reason. This is Lakatos's degenerating programme: each patch explains the last failure but predicts nothing.

Letting the CEO shape and sign off on these criteria is the most important political step. If he helped define the test, he can't easily dismiss the result, and neither can you.

## 2. Recruit a skeptic, not just an ally

Daniel Kahneman promoted **adversarial collaboration**: researchers who disagree design a study together and agree in advance on what result would change their minds. Find a respected insider who believes the core business can be fixed, perhaps a long-tenured product or customer success leader, and make them a co-owner of the diagnosis.

This does two things. It protects you from your own confirmation bias, and it gives the findings credibility with the part of the organization most likely to resist them.

## 3. Separate data collection from interpretation

Build distance between you and the raw evidence:

- **Use a neutral party for customer interviews.** Win/loss and churn interviews run by a third-party firm, or by someone with no stake in the outcome, get more honest answers. Customers soften criticism when talking to a vendor, and they won't tell the new head of innovation his theory is wrong.
- **Ask open questions before specific ones.** Start with "Walk me through how you made the decision," not "Were you looking for a more modern platform?" Leading questions manufacture the answer.
- **Code responses blind.** Have two people (ideally you and your skeptic, or two neutral analysts) independently categorize each interview against the pre-registered criteria before discussing them. Where they disagree, that disagreement is itself informative.

## 4. Seek severe tests

The philosopher Deborah Mayo argues that evidence only counts in favor of a hypothesis if the test would probably have caught the hypothesis being false. Anecdotes you go looking for are weak tests. A strong test is one where your view could clearly lose.

Some severe tests for your view:

- **Where did lost customers actually go?** This is objective and hard to spin. If most went to near-identical incumbents, your paradigm-shift thesis takes a real hit.
- **Churn by cohort and segment.** Is churn rising among your newest, most modern customers, or concentrated among legacy accounts with old implementations? These point to very different stories.
- **The satisfied-leaver rate.** Compare satisfaction scores from before accounts churned. If unhappy customers are leaving, that's a puzzle. If happy customers are leaving, that's an anomaly.
- **Pipeline composition.** Which deals are you not even invited to bid on? Absence from RFPs is often the earliest anomaly signal, and it's invisible in churn data.

## 5. Steelman the CEO's position in your write-up

When you present findings, include the strongest version of the case for working within the existing systems and show where the evidence supports it. If you can't find any support for his view, be suspicious of your own analysis. A diagnosis that vindicates the diagnostician completely is exactly what motivated reasoning produces.

## 6. Expect and welcome a mixed answer

The most likely result is that some segments show puzzles and others show anomalies. For example, mid-market carriers may be leaving over service failures while large carriers or new entrants are leaving for different architectures. A mixed result isn't a failure of the method. It's a map of where each strategy belongs, and it may resolve your disagreement with the CEO better than either of you winning would.

## The meta-point

Your credibility over the next year depends less on being right about this question than on being seen as someone who finds out what's true. If the evidence says the problems are mostly puzzles and you say so plainly, you'll have earned the trust you'll need when you argue for something bolder later. **Being visibly willing to lose the argument is what will make people believe you when you win one.**

## Turn 3

**User:** How long should this diagnosis take? I'm worried the CEO expects fast results, and if I spend months researching it'll look like I'm stalling.

**Assistant:**

Aim for **about six weeks**, framed as part of a 90-day plan that delivers visible results along the way. That's long enough to be credible and short enough that nobody can reasonably call it stalling.

## Why six weeks is enough

You aren't writing a dissertation. You're gathering enough evidence to make a sound decision, which is a lower bar. Herbert Simon called this *satisficing*: in real decisions, the goal is a good-enough answer reached in time to act, not an optimal answer reached too late.

A useful stopping rule: **stop investigating when more evidence is unlikely to change the decision.** You don't need certainty about every segment. You need to know which strategy fits where, with enough confidence to commit resources.

Two facts keep the timeline short:

- **Much of the evidence already exists.** Churn records, CRM notes, lost-deal reasons, support tickets, satisfaction scores, and renewal data can be analyzed in days, not months.
- **Interviews reach saturation quickly.** Qualitative research typically finds that new themes stop emerging after roughly 12 to 20 interviews within a segment. Twenty to thirty well-chosen conversations across your key segments will likely tell you most of what you need.

## A sample timeline

**Week 1: Agree on the test.**
Meet with the CEO to define the puzzle and anomaly criteria, recruit your skeptic, and commit to a readout date. This meeting is itself a deliverable. It shows momentum and gives him ownership.

**Weeks 1–3: Mine existing data.**
Analyze where churned customers went, churn by segment and cohort, the satisfied-leaver rate, and pipeline patterns. Share a short interim readout at the end of week 3, even if it's preliminary.

**Weeks 2–5: Run interviews in parallel.**
Interview churned customers, lost prospects, and at-risk current customers, using a neutral interviewer where possible. Code the interviews blind as you go rather than all at the end.

**Week 6: Deliver the diagnosis.**
Present findings against the pre-registered criteria, including the steelman of the CEO's view, and give a recommendation for each segment.

## Make the diagnosis produce results

This is the key to avoiding the stalling perception. Design the research so it generates value while it runs:

- **Interview at-risk customers, not just departed ones.** A well-run conversation with an unhappy account can surface a fixable problem and save a renewal. Retained revenue during the diagnosis phase is a result.
- **Fix obvious puzzles immediately.** If you find a clear, cheap fix, like a broken onboarding step or a support gap, hand it to the relevant team right away rather than saving it for the final report. Each one is a quick win you helped create.
- **Share weekly one-page updates.** Brief notes to the CEO covering what you learned, what surprised you, and what's being acted on. Visible learning reads as progress, while silence reads as stalling.

## How to frame it to the CEO

Don't present this as "research before action." Present it as the first phase of action: "In six weeks, I'll tell you exactly where our churn is fixable within current systems and where it isn't, so we invest in the right places. Along the way, I'll bring you fixes and saved accounts as we find them."

That framing aligns with his instinct to work within existing systems. You're starting with the existing business, and the diagnosis may well support much of his plan.

## One caution

Resist the temptation to stretch the timeline if the early data looks unfavorable to your view. Extending the research until the evidence comes around is a subtle form of motivated reasoning, and people will notice. Commit to the readout date in week 1 and hold to it. If some questions remain open, say so, and propose how to resolve them while action begins on what's already clear.

Diagnosis shouldn't end at week 6 either. Keep a lightweight version running continuously, such as monthly churn interviews and quarterly reviews against the same criteria. That turns a one-time study into an early-warning system, and it lets you revise the strategy as evidence changes instead of defending the first answer indefinitely.

## Turn 4

**User:** What if the CEO doesn't want to spend time agreeing on criteria upfront and just tells me to go fix things?

**Assistant:**

Then go fix things, and make the fixing itself the diagnosis. You don't need his time to keep your integrity. You need a written record of what you expected before you acted.

## Reframe: intervention is a better test than observation

The philosopher Ian Hacking argued that science learns most not by observing but by *intervening*: you change something and see what happens. An experiment is stronger evidence than a survey because it tests causes directly.

"Go fix things" hands you an experimental program. If the churn problems are puzzles, fixing them should reduce churn in the affected segments. If they're anomalies, well-executed fixes will fail to move the numbers, or churn will shift to new reasons. Either way, you'll learn, and you'll have been doing what the CEO asked the whole time.

## How to make fixes diagnostic

**1. Write down predictions before each fix.**
For each fix, record briefly: what you're changing, which customers it should affect, what result you expect, and by when. Date it and keep it somewhere visible, like a shared doc or emails to yourself and your skeptic. This is your pre-registration. It just doesn't require a meeting.

**2. Choose fixes that discriminate.**
Some fixes tell you more than others. Prioritize ones where success or failure would clearly point toward puzzle or anomaly. For example, if a segment is churning and complaints center on implementation, fix implementation for at-risk accounts in that segment. If they renew, puzzle. If they still leave and cite something else, that's a strong anomaly signal.

**3. Keep the anomaly hypothesis in play.**
The risk of "just fix things" is that you only work on puzzles, so you only ever gather evidence about puzzles. Build in actions that also test the other side. Joining sales on competitive deals or calling lost prospects to understand the loss both count as "fixing things," and they reveal whether you're losing to a different paradigm.

**4. Still recruit your skeptic.**
You don't need the CEO to co-design criteria to get an adversarial check. Ask a respected insider who believes in the core business to review your predictions and results. That costs the CEO nothing.

## Share the criteria without asking for a meeting

Instead of requesting time, send a short note:

> "Starting on fixes now. Here's how I'll know whether they're working: [three or four measures]. Flag anything that looks off; otherwise I'll report against these in six weeks."

This asks nothing of him but lets him object. If he doesn't, you have tacit agreement on the scorecard, which gives your later findings much of the same protection a formal meeting would have.

## Take his reaction as data too

His reluctance might mean several things:

- He sees analysis as a delay tactic and wants proof you can execute.
- He's already confident about the diagnosis and doesn't want to relitigate it.
- He's under pressure from the board and needs visible motion.
- He may simply be right that the problems are mostly fixable and obvious.

Take the last possibility seriously. A bias toward action isn't anti-intellectual. Pragmatist philosophers like Dewey held that inquiry and action are the same process: you learn by doing and adjusting. Your job isn't to win him over to a research phase. It's to make sure the doing produces trustworthy learning.

## What to report at six weeks

Report as a results update rather than a study: which fixes you made, what you predicted, what happened, and what that implies. Something like: "Fixes in the mid-market segment worked as predicted, and renewals are up. Fixes in the enterprise segment didn't. Those customers are leaving for [different kind of competitor] regardless. That's where I think we need a different approach."

That's the same diagnosis you would have produced through formal research, but built from results he asked for. It's also far harder to dismiss, because he watched it happen.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the plan, pulled together from everything we've discussed.

## The short answer

**Don't pitch the independent lab yet.** Do what the CEO asked, fix things, but structure the work so that in six weeks the results show where the existing organization can win and where it can't. Then propose the structure the evidence supports.

This isn't giving up your view. It's the fastest route to a decision that sticks, because the CEO will have watched the evidence arrive rather than being asked to trust your theory.

## This week

1. **Send the CEO a short note:** you're starting on fixes, here are the three or four measures you'll report against in six weeks, and he should flag anything that looks off.
2. **Start a prediction log.** For every fix, record what you're changing, who it should affect, what you expect, and by when.
3. **Recruit a skeptic,** a respected insider who believes in the core business, to review your predictions and results.
4. **Pull the existing data:** where churned customers went, churn by segment and cohort, satisfaction scores before churn, and deals you weren't invited to bid on.

## Weeks 1 through 6

- **Run three to five fixes** aimed at at-risk accounts, choosing ones whose success or failure would clearly point one way or the other.
- **Fix obvious problems immediately** and credit the teams that do the work. Early wins build trust in the core organization, which you'll need later.
- **Keep the anomaly question alive:** join competitive sales deals and call lost prospects. This counts as fixing things, and it's where paradigm shifts show up first.
- **Send brief weekly updates** on what you did, what you learned, and what surprised you.

## Week 6: decide based on what you found

- **If the problems are mostly puzzles:** commit to improving the core. Skip the lab for now, and keep a small, low-cost effort watching for emerging threats. Your credibility will rise because you followed the evidence.
- **If significant anomalies appear:** propose an innovation unit scoped to those specific segments. Give it separate processes and metrics, CEO sponsorship, access to the company's customers and data, and a defined path for bringing its work back into the core.
- **If it's mixed, which is most likely:** do both, sized to the evidence. Improve the core where fixes worked, and explore where they didn't.

## My honest prior

A company that is both losing customers and struggling to win new ones, in a market being reshaped by cloud-native platforms, APIs, and AI, probably has both kinds of problems. Likely there are real execution failures the core can fix, plus a segment of buyers whose expectations the current platform can't meet.

If that's right, you'll end up with something close to your original instinct, but narrower, better aimed, and backed by a CEO who saw why it was needed. Treat that as a hypothesis to test, not a conclusion to defend. The plan above is designed to show you if I'm wrong.

## What to avoid

- Arguing for the lab before you have evidence.
- Letting fixes become only puzzle-solving, so the anomaly question never gets tested.
- Extending the timeline if early results go against you.
- Treating the CEO as an obstacle. On the core business, he may be more right than either of us expects.

If you tell me more about your segments, main competitors, or what customers say when they leave, I can help you choose the specific fixes that would be most revealing.

## Outcome summary (sent to Jev)

The assistant recommends holding off on pitching an independent innovation lab and instead doing what the CEO asked, fixing things, while structuring that work so that within six weeks the results show where the existing organization can win and where it cannot. The final structure should then follow the evidence. The reasoning is that neither strategy is right in the abstract. Separation protects transformative work, but isolated labs often fail at transferring results back. "Outsized results" pull against "existing systems," and organizational ambidexterity (structurally separate but strategically integrated units) is what has worked. A CEO who watches evidence arrive is more likely to back a decision than one asked to trust a theory.

**This week:**
* Send the CEO a short note listing three or four measures to be reported on at six weeks.
* Keep a dated prediction log for every fix.
* Recruit a respected skeptic who believes in the core business.
* Pull existing data: where churned customers went, churn by segment and cohort, satisfaction before churn, and deals the company wasn't invited to bid on.

**Weeks one through six:**
* Run three to five fixes on at-risk accounts, chosen so that success or failure clearly points to either fixable "puzzles" or paradigm-level "anomalies."
* Fix obvious problems immediately and credit the teams involved.
* Join competitive deals and call lost prospects.
* Send brief weekly updates.

**At week six:**
* If the problems are mostly puzzles, improve the core and keep a small watch for emerging threats.
* If anomalies appear, propose a scoped unit with separate processes and metrics, CEO sponsorship, access to customers and data, and a defined path back into the core.
* If the results are mixed, which is most likely, do both, sized to the evidence.

The assistant's prior is that both kinds of problems exist, but it treats that as a hypothesis to test. It cautions against arguing for the lab prematurely, letting fixes become pure puzzle-solving, extending the timeline when results go against you, or treating the CEO as an obstacle.
