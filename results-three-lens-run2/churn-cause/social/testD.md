# churn-cause/social/testD

Model: claude-opus-5-5 · 2026-09-24T15:33:19.396543+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to know which approach wins approval and improves standing. Consider how each proposal would play inside and outside the company. Who gains status or credit, and who risks losing face or taking the blame? If each proposal went ahead, what would it signal to the board, employees, customers, and the public? Where might looking decisive or reassuring an audience matter more than operational results? What alliances and reputations would each proposal strengthen or threaten? And is there a third approach that wins greater support while letting the important players save face?

**Assistant:**

# Which Belief Is Right

**Neither VP can know yet, and you probably can't either.** Both explanations are plausible, both VPs have an incentive to believe theirs, and the evidence each cites is biased in their favor:

- **Exit interviews overstate product gaps.** "Your competitor has better AI" is an easy, face-saving reason for a customer to give. "We never got your system working properly" implicates their own team too.
- **Services hears implementation pain** because that's where customers complain to them. It doesn't prove that pain caused the departures.

The two explanations also interact. Customers who never reached full value are the ones most vulnerable when a competitor shows a shiny analytics demo. A fully adopted, deeply embedded claims system is hard to rip out. A half-implemented one isn't.

### A 4–6 week diagnostic

You can settle most of this quickly with data you likely already have:

| Question | If the answer is yes, it points to... |
|---|---|
| Did churned customers have longer implementations or lower adoption than retained ones? | Services / time-to-value |
| Did churned customers ever reach full go-live or use core modules? | Services |
| Did well-adopted, healthy accounts also leave, and for whom? | Product gaps |
| Are losses concentrated to one or two competitors with a specific feature? | Product gaps |
| Did churn accelerate after a specific event (competitor launch, reorg, support staff turnover, price change)? | Whatever that event was |
| Were churned carriers acquired or merged? | Neither. This is market consolidation, a structural driver in regional insurance that neither VP is talking about |

Also look at cohorts. If customers implemented in the last two years churn faster than older ones, something changed in delivery. If old, stable customers are suddenly leaving, the market moved.

Also consider an independent view: have someone outside both teams (you, or a third party) call 10–15 churned customers and ask what the decision process actually looked like, not just the stated reason.

My prior, for what it's worth: in enterprise vertical software, failed time-to-value is usually the root cause, and competitor features are the trigger. But the data should decide.

# The Political Landscape

### The Product proposal (accelerate the roadmap)

- **Who gains:** The VP of Product. AI and analytics are the story boards and investors want to hear, and the proposal positions them as the growth engine.
- **Who's exposed:** Product, later. Roadmap acceleration takes 12–24 months to affect churn. If churn keeps climbing meanwhile, they own a big bet that didn't pay off. It also implicitly says delivery is fine, which Services will resent.
- **Signals:**
  - *Board:* ambition and market awareness. Easy to approve.
  - *Employees:* excitement in engineering, frustration in services if they feel unheard.
  - *Customers:* promises, not relief. Customers struggling with implementation hear "we're building new things instead of fixing yours."
  - *Public/market:* a good press cycle.

### The Services proposal (fix onboarding and support first)

- **Who gains:** The VP of Services, if it works. It produces faster, measurable results (implementation time, adoption, support resolution) within 2–3 quarters.
- **Who's exposed:** Services and you. Saying "our delivery is the problem" is partly self-incriminating, and support usually sits near customer success. It also implicitly blames product complexity, since hard-to-implement software is partly a product problem.
- **Signals:**
  - *Board:* introspection and operational discipline, but it can read as defensive or "we're falling behind on AI."
  - *Employees:* validation for frontline staff.
  - *Customers:* the most credible message to existing accounts, because it addresses their actual experience.
  - *Public/market:* invisible, since nobody announces better onboarding.

### Your position

Churn is often treated as customer success's number. Both framings partly deflect from you, which is useful, but the Services framing touches support, so you're not fully neutral. Your strongest move is to be the one who brings the answer. You own the customer data and relationships, so you're the natural leader of the diagnosis, and that raises your standing more than siding with either VP.

### Where looking decisive matters more than results

- **The next board meeting.** The board needs to see that leadership understands the problem and has a plan with leading indicators. A credible diagnosis plus a dated plan reads as decisive. Two VPs arguing reads as a leadership problem.
- **At-risk customers right now.** Reassurance matters immediately: executive outreach, named escalation contacts, visible fixes. This is the fastest churn lever you have, and it doesn't depend on who wins the debate.
- **The market narrative.** Some AI story may be necessary just to stay on shortlists in new deals, even if it isn't the churn cause.

The caution is that churn is a lagging, very visible number. A plan chosen for optics that doesn't move retention gets exposed within two or three quarters, and the people associated with it take the hit. Here, the politically safe path and the operationally right path mostly coincide. Don't let them diverge.

# The Third Approach: A Time-to-Value Retention Program

Frame the problem as **"customers aren't reaching value fast enough, and competitors are exploiting that."** This is true under either hypothesis and lets both VPs be partly right.

**Phase 1 (weeks 1–6): Joint diagnostic, led by you.**
Run the data work above. Include both VPs in defining the questions up front so neither can dismiss the results later. Announce it to the board as a structured retention review with a decision date, which reads as rigor rather than delay.

**Parallel track, immediately: Save the at-risk renewals.**
Put executive sponsors on the top at-risk accounts and create fast-track fixes for their specific blockers. This buys time and shows results early.

**Phase 2: A combined plan weighted by what the data shows.**
The bridge between the two VPs is to **treat product investments that shorten implementation as the priority product work**:
- Out-of-box analytics dashboards that deliver value in week one, not after full configuration
- Configuration and data-migration tooling
- AI features that reduce implementation or adjuster workload, not just demo well

This gives Product the analytics and AI story they want, pointed at the problem Services has identified. Services gets implementation redesign, and possibly a sprint on support quality and staffing if the data supports it.

**Shared metrics, jointly owned:**
- Time to go-live
- Time to first value (define it concretely, e.g., first claims processed end-to-end)
- Adoption depth at 90 and 180 days
- Gross revenue retention by cohort

Joint ownership stops each side from declaring victory on its own metric while churn stays flat.

### How this lets everyone save face

- **VP of Product:** gets a visible AI and analytics roadmap and a strong board narrative. Their instinct about competitive pressure is validated.
- **VP of Services:** gets resources and recognition that delivery matters. Their critique is validated without being cast as the problem.
- **You:** become the person who turned a turf fight into a data-driven plan and owns the retention story. That's the best standing outcome available to you.
- **The CEO and board:** get a leadership team that looks aligned, with a clear plan and early indicators.

The one condition is that the diagnostic has to be genuine. If the data clearly favors one side, say so, and let the combined plan tilt accordingly. A third way that splits the difference regardless of evidence will look like politics to everyone, and the churn numbers will eventually confirm it.

## Turn 2

**User:** If churn is already seen as my number and support sits close to my team, won't the VPs and the board read my leading the diagnostic as grading my own homework, and should the CEO or CFO sponsor it so the findings carry weight with everyone?

**Assistant:**

Yes, that's a real risk, and I underweighted it. If churn is seen as your number and support sits near you, any finding that points away from your function will be discounted, and the VP it points toward will have an easy rebuttal: "Of course CS concluded it was Product." The diagnosis only has value if both VPs and the board accept it, so its credibility matters more than who gets credit for running it.

## Separate sponsorship, analysis, and input

**Sponsor: the CEO or CFO.** They own the question and the decision date, and they arbitrate disputes over method.

**Analysis: someone with no stake in the answer.** Good options:
- **FP&A or finance analysts.** They already own revenue and retention numbers, and the board trusts them.
- **RevOps or BizOps**, if it doesn't report into you, Product, or Services.
- **An outside firm for churned-customer interviews.** This is worth it even if the data work stays internal. Former customers are more candid with a third party than with the vendor that lost them.

**Input: you and both VPs.** Each supplies data and hypotheses. None of you controls the conclusions.

## CEO or CFO?

**The CFO is usually the better fit:**
- Retention and net revenue retention are financial metrics the CFO already reports to the board, so findings arrive in the board's language through a trusted channel.
- The CFO is seen as neutral between Product and Services.
- Watch-out: the CFO may frame the work around cost, e.g., "services is expensive, cut it" or "the roadmap is expensive, trim it." Set the charter explicitly around retention and revenue.

**The CEO makes sense if:**
- The dispute is already heated enough that only the CEO can make both VPs accept the result.
- The board is already alarmed and expects the CEO to own the response.
- Watch-out: check whether the CEO has already signaled a view. If they've been telling the board an AI story, their sponsorship won't look neutral, and people will expect the findings to confirm it.

A common structure: the CEO names it a priority and commits to acting on the findings, and the CFO's team runs it.

## Put your own function under test

This is what makes the process credible, and it's what protects your standing. Include CS-specific hypotheses in the charter:
- Were early warning signs visible in health scores, usage, or tickets, and did CS act on them?
- Was CSM coverage adequate for at-risk accounts?
- Were renewals engaged early enough?
- Did support quality or response times decline over the 18 months?

If the findings implicate CS, it's far better that they emerge from a process you proposed than that the board discovers them later. And if they clear CS, the result carries weight because you didn't control it.

## Where your standing comes from now

Not from owning the answer, but from:
1. **Proposing the independent structure yourself**, before anyone raises the conflict of interest. Raising it first reads as confidence. Having it raised against you reads as defensiveness.
2. **Opening your data fully**: raw account histories, health scores, ticket data, renewal notes. No curated summaries.
3. **Owning the retention actions afterward.** Save plays for at-risk accounts, adoption programs, and health monitoring are naturally yours once the diagnosis lands.

## Set it up with a short charter

Before starting, get the sponsor and both VPs to agree on a one-page charter:
- Sponsor and analysis owner
- The questions and hypotheses being tested, including each VP's and yours
- Data sources and cohort definitions
- What evidence would support each hypothesis, agreed up front
- A decision date, and a commitment that findings will shape the plan

Agreeing in advance on what would count as evidence is the most important part. It makes it much harder for anyone, you included, to dismiss results they don't like.

## Turn 3

**User:** If I take this proposal straight to the CEO or CFO, won't both VPs see it as me escalating their disagreement over their heads and exposing them as the problem, and should I get their buy-in first so it reads as our joint idea?

**Assistant:**

Mostly yes. Going to them first is usually right, both for the relationships and because a diagnostic the VPs helped design is much harder for them to dismiss later. But do it quickly, and don't give either VP a veto.

## Why talking to them first works

- **It removes the escalation read.** "We three agreed we need a neutral referee" lands very differently from "CS went over our heads."
- **It improves the design.** Each VP knows where the evidence for their view lives, and each will spot weaknesses in how the other's hypothesis gets tested.
- **It gets you commitment early.** Anyone who co-authored the charter can't easily reject the findings.
- **It protects them.** Neither VP wants to own the churn problem alone. An independent diagnostic with a shared plan protects both from being blamed for a failed bet.

## How to approach them

**Talk to each separately first, then together.** Separate conversations let each raise concerns without performing for the other. Frame it around what they gain:

- **To the VP of Product:** "Your competitive-gap case is strong, but right now it's your word against Services. An independent analysis with win/loss data would give the roadmap investment real backing with the board."
- **To the VP of Services:** "You're arguing delivery is the problem, which can look like you're asking for budget to fix your own area. Neutral data showing time-to-value drives churn makes the case for you."

Then say plainly what you're doing yourself: "Churn is seen as my number, and support is near my team, so I shouldn't run this. I'm putting CS under the same scrutiny. I'd like the three of us to take it to the CFO together."

**Then meet all three together** to agree on the charter, the hypotheses, and who presents it. Ideally all three of you bring it to the sponsor, or the two VPs present it with you supporting. That's the strongest signal of alignment, and it lets them share the credit.

## Risks to manage

**Speed.** Don't let pre-alignment stretch into weeks. Aim for a week or two, especially if a board meeting is coming. Churn keeps happening, and a slow process can look like leaders protecting themselves.

**Someone getting there first.** Once you raise the idea, a VP may go to the CEO alone and frame it their way, for example "CS wants a study to delay the roadmap." Keeping the conversations close together and moving quickly to the joint meeting reduces this.

**Watered-down conditions.** Buy-in shouldn't mean dropping the hypotheses that make someone uncomfortable, or letting either VP's team do the analysis. The non-negotiables are a neutral analyst, all hypotheses tested (including yours), agreed evidence standards, and a decision date.

**One VP refusing.** Tell them openly that you're taking it forward anyway: "I understand. I still think the company needs this, so I'll raise it with the CFO and say you have concerns. I'd rather you were part of shaping it." Going ahead openly isn't going over their heads. Going ahead behind their backs is. A leader who refuses a neutral review usually weakens their own position more than yours.

## One exception

If the CEO or CFO has already asked you to explain the churn, or the board is pressing for answers, you can't wait for full consensus. Tell the executive what you're proposing and that you're aligning the VPs on it, then bring the VPs in immediately. Don't sit on a request from the top to protect peer relationships. Just tell your peers promptly.

## Turn 4

**User:** If I pitch each VP on the idea that the diagnostic will back their case, won't whichever one the data goes against feel I set them up, lose face in front of the CFO, and hold it against me, so how do I frame it now so the losing side can still come out looking good?

**Assistant:**

You're right, and that's a flaw in the pitches I suggested. Telling each VP "this will back your case" is a promise you can't keep to both, and whoever loses would reasonably feel misled. Frame it now as a fair test, not a vindication, and build face-saving into how the results are produced and presented.

## Pitch fairness, not victory

The honest selling point is that **neither VP currently has a way to win this argument, and the diagnostic gives them one.** Each gets a fair hearing, and each is protected from being blamed for a bet the company made without evidence.

Revised pitches:

- **To the VP of Product:** "Right now this is opinion against opinion, and the board can't fund a major roadmap push on that. This gives your competitive-gap case a fair, independent test. If it holds up, you'll have strong backing. If the picture is mixed, you'll help shape what the product response should be."
- **To the VP of Services:** "Same for you. Your time-to-value argument gets tested properly, by someone who isn't you or Product. Whatever it shows, you're not stuck asking for resources on your own say-so."
- **To both, and it's true:** "My honest guess is you're each partly right, and the question is how much and in what order. I'm putting CS under the same test."

This sets the expectation of a mixed result from the start, so a tilt one way reads as calibration, not defeat.

## Design the process so no one is exposed

**Test causes, not people.** Frame hypotheses around the customer's experience ("customers leave before reaching value," "healthy customers leave for competitor features"), not "Product is wrong" or "Services failed." Findings then describe where customers struggle, not whose judgment was wrong.

**Measure weight, not winners.** Ask the analysts to estimate how much of the churn each factor explains and in which segments, rather than naming a single cause. The answer will almost certainly be something like "time-to-value explains most of the losses among newer customers, and competitive gaps matter most for larger carriers." Both VPs then have validated ground to stand on.

**Agree the evidence standards up front, and write them down.** A VP who helped define what would count as evidence is much less likely to feel ambushed by the result.

**No surprises.** The VPs should see the findings privately, with the analysts, before anything goes to the CFO. That gives them time to absorb the result, challenge the method, and decide how to talk about it. Losing face mostly happens when people react in real time in front of the boss.

## Give the losing side a way to look good

**Credit the hypothesis.** A leader who put their theory up for a real test deserves credit even if the data leans away from it. Say that explicitly in the readout: "Both hypotheses were serious and both showed up in the data."

**Give everyone a role in the fix.** Agree before the results come in that each VP owns part of the response. If time-to-value dominates, Product can own the tooling that speeds implementation, such as configuration tools and out-of-box analytics. If product gaps dominate, Services can own migration, adoption, and win-back plays. No one ends up sidelined.

**Let them present their implications.** In the CFO readout, have each VP present what the findings mean for their own area. A leader who says "here's what this tells us and here's what I'm going to do" looks strong, whatever the data said about their original theory.

**Look forward, not back.** Keep the readout about what to do next, not about who called it right. If the CFO or anyone else starts keeping score, redirect: "The useful question is what we fund first."

## What you can't control

Even with all this, a VP whose view comes out weaker may be disappointed for a while. What you can ensure is that they can't reasonably say they were misled or set up. The protection against lasting resentment is that you were straight from the first conversation: you promised a fair test, you ran one, you tested your own function too, and you made sure they came out of it with a meaningful role.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the plan, pulling together everything we've discussed.

## This week

**1. Start saving at-risk renewals now.** This doesn't depend on the diagnosis. Identify the accounts renewing in the next two quarters with weak health signals, assign executive sponsors, and fix their specific blockers. It's the fastest way to reduce churn, and it's squarely your job.

**2. Talk to each VP separately.** Pitch a fair test, not vindication: "Neither of us can win this on opinion. Let's get an independent answer. My guess is you're both partly right, and I'm putting CS under the same scrutiny." Keep these conversations close together so neither hears about it secondhand.

**3. If an executive has already asked about churn,** tell them now that you're aligning the VPs on a proposal. Don't wait for consensus.

## Next week

**4. Meet with both VPs to draft a one-page charter:**
- Hypotheses, framed around customer experience: customers not reaching value, healthy customers leaving for competitor features, CS missing early warning signs, and market consolidation
- What evidence would support each, agreed in writing
- Neutral analysis, ideally the CFO's team, with an outside firm interviewing churned customers
- A readout date, with findings shared privately with the VPs before the sponsor
- An agreement that each VP owns part of the response whatever the results show

**5. Take it to the sponsor together.** The CFO is likely the best fit, since retention is a financial metric the board already trusts from them. Go with the CEO if the dispute needs top-level authority to settle, or if the board is pressing. Ideally the VPs present with you supporting.

## Weeks 3–8: the diagnostic

**6. The analysis compares churned and retained customers** on implementation time, adoption depth, competitor destination, cohort, and events like acquisitions or support turnover. The outside firm interviews 10–15 churned customers. You open all your data without curation.

**7. Keep the save plays running** and track their results. Early wins buy credibility with the board while the diagnostic runs.

**8. Tell the board it's underway,** framed as a structured retention review with a decision date. That reads as decisive, not delayed.

## After the readout

**9. Build a combined plan weighted by the evidence.** Most likely, it will prioritize time-to-value: product work that shortens implementation (configuration tools, migration tooling, out-of-box analytics), plus fixes to delivery and support, plus targeted feature work where competitive losses concentrate. If the data points clearly one way, tilt the plan accordingly. Don't split the difference for politics.

**10. Set shared metrics that all three of you own:** time to go-live, time to first value, adoption at 90 and 180 days, and retention by cohort. Review them monthly.

**11. Take ownership of the retention side:** health monitoring, early-warning processes, and adoption programs. That's where your standing grows.

## The principle behind all of it

Be straight with everyone from the start, test your own function alongside theirs, and let evidence decide the plan. That's also the best political strategy here. Churn is too visible a number for optics to hide a wrong call for long, and the person who led the company to the right answer, fairly, comes out of this better than either VP could by winning the argument.

## Outcome summary (sent to Jev)

The assistant holds that neither VP's belief can be confirmed yet. Exit interviews tend to overstate product gaps, and Services mostly hears about implementation pain, so each side's evidence is biased. Its prior is that failed time-to-value is usually the root cause in enterprise vertical software and competitor features the trigger, but the data should decide. Market consolidation is another possible driver.

It recommends starting save plays on at-risk renewals immediately, with executive sponsors fixing specific blockers, because this cuts churn regardless of the diagnosis. The user should approach each VP separately, pitching a fair test rather than vindication, then draft a one-page charter together. The charter should cover:
- hypotheses framed around customer experience, including one testing customer success itself
- evidence standards agreed in writing
- neutral analysis, ideally by the CFO's team, with an outside firm interviewing 10–15 churned customers
- a readout date, with findings shown privately to the VPs first
- a prior commitment that each VP owns part of the response

The group should bring this to a sponsor together, likely the CFO, or the CEO if the board is pressing or the dispute needs top-level authority. The analysis compares churned and retained customers on implementation time, adoption, competitor destination, cohort, and events such as acquisitions or support turnover. The board should be told this is a structured retention review with a decision date.

Afterward, the company builds a combined plan weighted by the evidence, probably prioritizing implementation-shortening product work plus delivery fixes. All three leaders share metrics: time to go-live, time to first value, adoption at 90 and 180 days, and retention by cohort. The user then owns the retention programs.

Caveats: if the data clearly favors one side, the plan should tilt that way rather than split the difference. Pre-alignment must move fast, and no VP gets a veto. Churn is too visible for optics to hide a wrong call.
