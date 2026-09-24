# churn-cause/social/testB

Model: claude-opus-5-5 · 2026-09-24T15:32:56.387021+00:00

## Turn 1

**User:** You are a world-class sociologist who studies status and reputation.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

## Short answer

Nobody can tell you yet, including both VPs. Each has offered a hypothesis, and the hypotheses are testable. The more useful point from a sociological angle is that the two explanations are probably entangled, and the reasons customers *give* for leaving are the least reliable evidence you have.

## Why you should distrust the debate as framed

**1. Each diagnosis matches the diagnoser's jurisdiction.** Product sees a product problem; Services sees a services problem. This is one of the most reliable patterns in organizational sociology. Departments frame problems in terms their own function can solve, because that is what they can see and what secures them resources and standing. Neither VP is necessarily wrong. But their agreement with themselves is not evidence.

**2. Exit reasons are "accounts," not causes.** When customers leave, they offer socially acceptable explanations, what C. Wright Mills called "vocabularies of motive." "Your competitor has better AI" is a clean, impersonal, defensible reason. It is easy to say to a vendor, and easier still to say to one's own board. "Our implementation stalled, our champion left, and nobody internally could make the case for renewal" is messier and implicates the customer's own organization. So exit surveys will over-report product gaps.

**3. The two hypotheses feed each other.** A customer stuck in a long implementation never uses your analytics. They then experience your product as lacking analytics, and a competitor's demo looks like a leap forward. A "product gap" can be produced by a service failure.

**4. The timing is suspicious in a status-relevant way.** Your churn doubled over roughly the period when AI became a legitimacy signal across the industry. For regional carriers, whose boards, reinsurers, auditors and peers increasingly ask "what are you doing with AI?", switching to an AI-branded vendor can be about *appearing* modern as much as using the features. Institutional theorists call this mimetic isomorphism: organizations under uncertainty copy what high-status peers do. If this is the driver, the issue is real but it isn't a feature-count problem. It is a positioning problem.

**5. Regional insurance is a small, networked world.** Carriers talk at conferences, in mutual associations, and through shared brokers and consultants. A handful of painful implementations can become "their implementations are a nightmare" across the whole segment, which damages renewals and new sales at once. Reputation here travels as stories, not metrics.

## How to actually find out (a 3–4 week diagnostic)

Before looking at data, get both VPs to state in writing **what evidence would change their mind.** This single step converts a turf fight into an inquiry.

Then look at the evidence that discriminates between the hypotheses:

| Evidence | Points to Services | Points to Product | Points to Status/Positioning |
|---|---|---|---|
| **Churn by implementation length / time-to-value** | Churn concentrated in long, stalled implementations | Churn unrelated to implementation experience | Unrelated |
| **Churn by usage depth** | Churned accounts used few features | Heavy, satisfied users still left | Heavy users left for vendors whose AI they barely use |
| **Where churned customers went** | Simpler tools, in-house, or anyone who promised easier onboarding | Specific competitors winning on specific capabilities | AI-branded vendors, often with thinner products |
| **New-logo win rate** | Mostly stable (implementation pain shows up after the sale) | Falling, losing on feature comparisons | Falling, losing on narrative and "vision" |
| **What changed 18 months ago** | Implementation team turnover, new product version, scaled too fast | Competitor launches | Industry AI hype and board pressure |
| **Champion turnover at churned accounts** | High (no one internally could realize or defend value) | Low | Mixed |

The new-logo win rate is especially useful. Product gaps hurt you in both acquisition and retention. Implementation pain mostly hurts retention, at least until reputation catches up.

**Do real exit interviews.** Have a neutral third party run them, at least 10–15, and include people *below* the signer, such as claims managers and IT leads. Ask for the story of the relationship, not "why did you leave." Ask when they first thought about leaving. The answer is often "month 7 of implementation," and that tells you more than the stated reason. Also interview a few at-risk current customers and a few highly successful ones for contrast.

## What to do in the meantime

- **Triage the at-risk base now.** Don't wait for the diagnosis. Identify accounts with long implementations, low adoption, or recent champion departures, and put senior attention on them.
- **Don't let either VP make an irreversible bet yet.** Neither "accelerate the roadmap" nor "overhaul services" should get a major reallocation until the diagnostic reports, which is only a few weeks away.
- **Prepare for a mixed answer.** The most likely result is something like "implementation failure makes customers susceptible, and competitor AI narratives give them a legitimate exit." If that's what you find, the response has three parts:
  1. Fix time-to-value, the root vulnerability.
  2. Build a small number of visible, credible AI and analytics capabilities, chosen for use and for signaling rather than feature parity.
  3. Actively manage your reputation in the carrier community: reference customers who got to value quickly, a presence at industry forums, and a clear AI story that boards can repeat.

## The bottom line

Churn is partly a reputational phenomenon. Customers leave when staying becomes harder to justify, internally and to peers, than leaving. Your job is to find out whether that justification is being eroded by what customers *experience* (Services), what they *lack* (Product), or what they *can say* (status). Then fix the right thing first.

## Turn 2

**User:** How do I get both VPs to actually agree to a diagnostic without it feeling like I'm stalling or taking sides?

**Assistant:**

## First, recognize your own position

You aren't neutral either, and both VPs know it. Customer success owns the churn number, and CS usually sits closer to Services than to Product. The VP of Product may already suspect that "let's run a diagnostic" is a polite way of building the Services case. So your first job is to be visibly even-handed, not just actually even-handed.

## The core principle: protect everyone's face

The sociologist Erving Goffman observed that people in organizations defend their "face," the competent, credible self they present, as fiercely as they defend their interests. Your VPs have taken public positions. A diagnostic threatens to produce a loser, and that is the real source of resistance, more than any disagreement about method.

So design the process so that **nobody can lose badly and everyone can be partly right.** Churn really is multi-causal, so you can say this sincerely: "My bet is you're both seeing something real, and the question is sequencing and proportion, not who's right."

## Tactics

**1. Talk to each VP privately before any group meeting.** Consultants call this pre-wiring; Japanese firms call it *nemawashi*, preparing the roots before transplanting. Never let either VP hear the proposal for the first time in front of the other. In private:
- Ask what evidence they believe would prove their case. This signals respect and gives them a stake.
- Ask what would make them doubt it. People are much more willing to commit to disconfirming evidence privately than publicly.
- Ask what they'd need to see in the design to trust the result.

**2. Frame it as arming them, not judging them.** Each VP will eventually need to win budget from the CEO or board. A diagnostic gives them ammunition. You might say to Product: "If it's the roadmap, I want to walk into planning with data that makes your case undeniable." Say the equivalent to Services. The message is the same to both, and it's true.

**3. Let them co-design it, with symmetry.** Include the analyses each VP thinks will vindicate them. Product might want the competitor-loss and win-rate analysis; Services might want the time-to-value cohort analysis. Put them side by side. When each sees their own test in the plan, the process stops feeling rigged. Have the data pulled by someone neutral, such as finance, RevOps, or an analyst, rather than by either team or yours.

**4. Agree on the decision rule before seeing results.** Something like: "If churn concentrates in stalled implementations, Services gets priority. If well-implemented, high-usage customers are leaving for specific capabilities, the roadmap gets priority. If it's both, we split along these lines." Write it down. Pre-commitment is the single strongest protection against post-hoc rationalization, including yours.

**5. Use outside interviewers for exit conversations.** A third party removes the suspicion that CS or Services is shaping what churned customers say. It also produces the most credible evidence.

**6. Time-box it and attach it to a real decision.** "Stalling" means open-ended. Tie the diagnostic to the next planning cycle or budget meeting: "Results in four weeks, in time for Q3 planning." Now it feeds a decision instead of delaying one.

**7. Don't freeze anything in the meantime.** Pair the diagnostic with moves no one could object to. The roadmap continues as planned, with no acceleration or cuts yet. Services starts triage on at-risk accounts. Nobody has to stop doing their job to wait for data. This is what defuses the stalling charge most directly.

**8. Get a sponsor above both of them.** Ideally the CEO or COO asks for the diagnostic. Then it's a leadership request, not your intervention in a peer dispute. Brief the executive privately so they can frame it as "I want us to make this call with evidence," not as a verdict on anyone.

## Sample language for the joint meeting

> "Churn has doubled, and we have two credible explanations from two people who know this business well. It's probably some of both, so the real question is where to put the next dollar first. I'd like to spend four weeks getting evidence we'll all trust, using tests each of you helped design and a decision rule we agree on now. Nothing stops in the meantime. The goal is to walk into planning with a case strong enough that the CEO can't second-guess it."

## Watch for one trap

If the results favor one side, the other VP may attack the method after the fact. Your defenses are the pre-agreed rule, their own input into the design, and the neutral data source. When you present findings, lead with what each hypothesis got right before discussing proportions. Let the "winner" be magnanimous and the "loser" keep credibility. You'll need both of them to execute whatever comes next.

## Turn 3

**User:** What if the CEO doesn't want to sponsor it and just tells me to pick one and move on?

**Assistant:**

## First, take the CEO seriously

"Pick one and move on" may be a reasonable instruction, not an obstacle. Consider what the CEO might be signaling:

- **They value decisiveness.** In many leadership cultures, asking for a study reads as avoiding responsibility. Decisiveness is part of how leaders earn and keep status, and a proposal to "gather evidence first" can quietly cost you credibility.
- **They don't want to referee their VPs.** Sponsoring your diagnostic puts the CEO in the middle of a peer dispute. They may be delegating the call to you on purpose.
- **They see a cost to waiting.** Churn compounds. Every month of analysis is a month of renewals at risk.

So don't fight the instruction. Comply with it in a way that keeps the substance of what you wanted.

## Make the call, but make it with evidence you can get in days

You don't need a four-week diagnostic to make a defensible choice. You likely already have enough data for a rough answer:

- **Churn versus implementation duration or time-to-value.** Your team can probably pull this from CRM and project data in a day or two.
- **Usage depth of churned accounts** in the six months before they left.
- **Where churned customers went**, which account managers usually know informally.
- **New-logo win rate trend**, which sales ops can give you quickly.
- **Five or six phone calls** to recently churned customers, made by you personally.

Two things are enough to decide on. If churned accounts cluster in long, stalled implementations, that's your answer. If healthy, heavily used accounts left for competitors, that's the other answer.

## If the data is ambiguous, pick based on sequencing logic

When the evidence doesn't clearly point one way, there's a strong structural argument for **prioritizing time-to-value first**:

- **It's a precondition.** Customers who never reach full value won't benefit from new AI features either. Better onboarding makes every future feature land.
- **It's faster.** Onboarding fixes can show results within one or two renewal cycles. Roadmap acceleration usually takes quarters.
- **It's cheaper and more reversible.** If you're wrong, you've improved customer experience at modest cost. If you over-invest in the roadmap and you're wrong, you've spent heavily while churn continues.
- **It's closer to your control** as head of customer success, so you can be accountable for results.

Pair it with **one narrow, visible product commitment**, such as a specific analytics or AI capability. Choose it because customers are asking for it and because it gives carriers something to show their boards. This addresses the status dimension without betting the roadmap.

Be aware that recommending the Services-leaning option makes you look biased, since CS sits close to Services. The fastest data you can gather is your protection. Show the numbers, not just the logic.

## Build the learning into the decision

This is how you get most of the diagnostic's value without asking for one. Present the decision with:

- **Leading indicators** you'll track, such as implementation duration, time to first value, adoption depth, and at-risk account health.
- **A checkpoint at 60 to 90 days** where you'll report results.
- **A reversal condition** stated upfront: "If well-implemented accounts keep churning to competitors, we shift weight to the roadmap."

To the CEO, this looks like a decision. In practice, it's a structured experiment.

## Sample language for the CEO

> "Understood. My call is to prioritize time-to-value first, plus one targeted product commitment on [X]. Here's why: [two data points]. I'll report back in 90 days on [metrics]. If healthy accounts are still leaving for competitors at that point, I'll recommend shifting investment to the roadmap."

That takes under a minute, and it's decisive and accountable. It also quietly includes the evidence standard you wanted.

## Handle the VPs carefully

The CEO has given you authority, but the VPs still need to execute, and one of them will feel overruled.

- **Tell them privately and in person before any announcement.** Tell the VP whose view got less weight first.
- **Frame it as sequencing, not a verdict.** For example: "You're right about the competitive pressure. We're addressing it with [X] now, and the checkpoint gives us a clear trigger to go further."
- **Give them a role.** Ask the Product VP to own the targeted feature and help define the reversal metric. People support decisions they helped shape, even decisions they initially opposed.

## The honest caveat

If your quick data clearly points toward product gaps, pick the roadmap, even though it's outside your area. Your credibility with the CEO over the next two years depends on being seen as someone who follows the evidence, not someone who defends their own function. That reputation is worth more than winning this particular argument.

## Turn 4

**User:** How do I actually get those five or six churned customers to pick up the phone and be honest with me, since I'm the vendor they just left?

**Assistant:**

## Why it's harder than it looks, and why it's easier

Churned customers have little reason to help you. The conversation is mildly awkward, and they worry it's a win-back pitch. But several forces work in your favor:

- **Being asked for advice is flattering.** Asking someone to share expertise raises their status. Asking for "feedback" feels like a chore; asking for "advice" feels like recognition.
- **Regional insurance is a small world.** People move between carriers, and your paths will cross again. Many will want to leave on good terms.
- **Many people want to be heard.** If their implementation was painful, some have a story they've been waiting to tell someone who'll listen.

## Who to call

- **Don't default to the executive who signed the termination.** They'll give you the official account, the one they gave their board.
- **Look for former champions and day-to-day users.** Claims managers, implementation leads, and IT contacts who worked with your team know what actually happened, and they often liked individuals on your side even if the relationship failed.
- **Reach out to 15 to 20 people to get five or six conversations.** Expect a response rate of about a third.
- **Mix recent and older churns.** People who left within the last one to six months remember details. People who left longer ago are often more candid because the decision is settled.
- **Include at least one or two who left for a competitor on features.** You need evidence that can disconfirm your own leanings.

## How to ask

Send a short personal email from you, not a survey tool or marketing system. Something like:

> "Hi [name], I lead customer success at [company]. I know you moved on last [month], and I'm not reaching out to change that. We're trying to understand honestly where we fell short, and your perspective would genuinely help. Would you give me 20 minutes? No sales pitch, and I'll keep anything you say confidential to my team. Happy to work around your schedule."

What makes this work:

- **Name the thing they fear and rule it out.** "Not reaching out to change that" removes the win-back worry directly.
- **Keep the request small and specific.** Twenty minutes is easy to say yes to.
- **Promise confidentiality and keep that promise.** Don't attribute specific comments to named people in internal meetings.
- **Keep the account manager who lost them out of it.** Their involvement makes the call feel like an attempt to reopen the deal and makes criticism of that person awkward.

If someone doesn't reply, one gentle follow-up after a week is fine. After that, let it go.

## How to get honesty, not politeness

People open with the socially comfortable account. Your job is to get past it.

**Ask for the story, not the reason.** "Why did you leave?" gets you the official answer. Instead ask: "Take me back to when you first started working with us. How did it go?" Stories reveal sequence, and sequence reveals cause.

**Find the turning point.** "When did you first start thinking this might not work?" This question is often the most valuable one. An answer like "month seven of implementation" tells you far more than "the competitor had better AI."

**Give explicit permission to criticize.** "Please don't soften anything. The harsh version is the useful version."

**Use third-person questions.** People criticize more freely when they're describing others' views: "What were people on your team saying about us?" or "What would your claims staff say if I asked them?"

**Ask them to advise you.** "If you were in my job, what's the first thing you'd fix?" This puts them in the expert role and often produces the most direct answer of the call.

**Probe the competitor gently.** "What does [competitor] do that made the decision easier?" and "Now that you've switched, what's been better and what's been harder?" The second question often surfaces whether the switch was about features or about hope for a fresh start.

## How to listen

- **Don't explain, defend, or correct.** The first time you say "well, the reason that happened was...", the conversation turns polite again.
- **Leave silences.** After an answer, wait a few seconds. People often add the most honest part after the pause.
- **Take notes in their words.** Exact phrases are more persuasive to your VPs and CEO than your summaries.
- **Don't pitch, even softly.** If they ask about your roadmap, answer briefly and return to listening. Breaking your no-pitch promise ends the call's usefulness and damages your reputation in a small market.

## After the call

- **Send a short thank-you the same day.**
- **Close the loop later if you act on what they said.** A note a few months on, such as "Your comment about onboarding shaped a change we just made," builds real goodwill. Occasionally it leads a customer back, precisely because you didn't try to win them back.
- **Look for patterns across calls rather than weighting any single one heavily.** One vivid story can mislead. Three stories that share the same turning point are evidence.

## A note on gifts

A small thank-you, such as a charitable donation in their name, can be a nice gesture. But check your customers' gift policies first. Insurance carriers often have strict compliance rules, and an unwelcome gift makes the gesture backfire.

## Turn 5

**User:** What should we do?

**Assistant:**

## The plan

Here is the whole thing as one sequence, with my recommendation at the end.

### Week 1: Gather fast evidence

1. **Pull the numbers yourself.** Get churn by implementation duration and time-to-value, the usage depth of churned accounts in their final six months, where churned customers went, and the new-logo win-rate trend over 18 months. Have someone neutral, like RevOps or finance, pull or check the data so neither VP can dismiss it.
2. **Start the exit calls.** Email 15 to 20 former champions and day-to-day users, aiming for five or six conversations. Ask for the story and the turning point, not the reason.
3. **Talk to each VP privately.** Ask what evidence would support their view and what would change their mind. You're not asking permission, just making sure neither is surprised later.

### Week 2: Decide

Read the evidence against this rule:

- **Churn clusters in long or stalled implementations and low-usage accounts:** prioritize time-to-value.
- **Healthy, well-implemented, heavily used accounts are leaving for specific competitor capabilities, and new-logo win rates are falling:** prioritize the roadmap.
- **Ambiguous or mixed:** prioritize time-to-value, for the sequencing reasons below.

### My default recommendation

Unless the data clearly points to product gaps, **fix time-to-value first and make one narrow, visible product commitment.**

- **Time-to-value is the precondition.** Customers who never reach full value won't benefit from new features either.
- **It's faster, cheaper, and more reversible** than accelerating the roadmap, and it sits within your control.
- **The single product commitment addresses the status problem.** Regional carriers face board, peer, and reinsurer pressure to show progress on AI and analytics. Pick one capability customers actually ask for and that gives them something credible to point to. Let the Product VP own it.

If the data clearly shows product gaps, recommend the roadmap even though it's outside your area. Your long-term credibility depends on following the evidence rather than defending your function.

### Week 2 or 3: Bring it to the CEO

Keep it to one minute: the decision, two data points, the metrics you'll track, a 90-day checkpoint, and the condition under which you'd shift course. For example: "If well-implemented accounts keep leaving for competitors, we move investment to the roadmap."

Tell both VPs privately before any announcement, starting with the one whose view got less weight. Frame it as sequencing, not a verdict, and give each a role.

### Now, in parallel: Protect the at-risk base

Don't wait for any of the above. Identify current accounts with stalled implementations, low adoption, or a recently departed champion, and give them senior attention now. These are next year's churn numbers.

### Day 90: Report back

Show movement on implementation duration, time to first value, adoption depth, and at-risk account health, plus what the exit calls taught you. Then either stay the course or trigger the reversal you committed to.

## The bottom line

The question has shifted from "which VP is right" to "what do we fix first, and how will we know if we're wrong." Answer it with a week of fast evidence and a decision you can defend, and build the checkpoint into the decision itself. That makes you the person who resolved the argument rather than someone on one side of it, and it gives the company a real chance of bringing churn back down.

## Outcome summary (sent to Jev)

Neither VP can be declared right yet. The two explanations are likely entangled: a stalled implementation can make customers experience the product as lacking analytics, and the industry's AI hype gives them a socially acceptable reason to leave. Stated exit reasons are unreliable, and each VP's diagnosis conveniently matches their own function.

The recommendation is a fast, evidence-based decision rather than a long study. In week one, the head of customer success should have RevOps or finance pull or check several figures: churn by implementation duration and time-to-value, usage depth of churned accounts in their final six months, where those customers went, and the 18-month trend in new-logo win rates. In parallel, they should email 15 to 20 former champions and day-to-day users to get five or six candid conversations, asking for the story and the turning point rather than "why did you leave." They should also privately ask each VP what evidence would change their mind.

In week two, decide against a pre-set rule. If churn clusters in stalled implementations and low-usage accounts, prioritize time-to-value. If healthy, heavily used accounts are leaving for specific competitor capabilities while win rates fall, prioritize the roadmap. If the evidence is mixed, default to time-to-value, because it is the precondition for any feature landing and is faster, cheaper, more reversible, and within CS's control. Pair it with one narrow, visible AI or analytics commitment owned by the Product VP, which addresses carriers' board and peer pressure.

Present this briefly to the CEO with metrics, a 90-day checkpoint, and a reversal condition. Tell the VPs privately beforehand, framing it as sequencing rather than a verdict. Meanwhile, give at-risk accounts senior attention now.

One caveat matters most. If the data clearly points to product gaps, recommend the roadmap, because credibility depends on following the evidence rather than defending one's own function.
