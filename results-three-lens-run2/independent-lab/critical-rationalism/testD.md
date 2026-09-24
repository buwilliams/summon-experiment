# independent-lab/critical-rationalism/testD

Model: claude-opus-5-5 · 2026-09-24T15:19:57.918169+00:00

## Turn 1

**User:** I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

**Assistant:**

# Neither survives as stated. A third explanation does better.

Both views are claims about **organizational structure**, but the facts you've described (churn, lost deals) are about **customers**. Neither view says why customers are leaving. That gap is where both are weakest.

## 1. What each conjecture claims is going on

**CEO's conjecture (C):** The company already has the capabilities it needs. It's failing because of direction, focus, or urgency. With the right leadership and priorities, the existing machine can produce better products.

**Your conjecture (L):** The core organization structurally kills new ideas. Its approval layers, risk aversion, legacy architecture, incentives tied to the existing book, and roadmap commitments act as immune responses. Good ideas can only survive outside it.

Both are really *solutions* with a diagnosis attached implicitly. Neither states the diagnosis explicitly.

## 2. What each predicts that the other doesn't

| Observable | If C is true | If L is true |
|---|---|---|
| Past initiatives that had executive sponsorship | Mostly shipped, or failed for fixable reasons (under-resourced, deprioritized) | Died anyway: in approvals, integration, security review, release trains, sales disinterest |
| Where time goes from idea to customer | Mostly engineering and design work | Mostly waiting, handoffs, governance |
| Insiders asked "what should we build?" | Give answers, and when prioritized, can deliver them | Give good answers but explain why they can't be shipped |
| Why customers churn and deals are lost | Things the current product and roadmap could fix (gaps, service, pricing, reliability) | Capabilities the current architecture or business model can't deliver (e.g., speed of configuration, APIs, cloud-native deployment) |
| A small insider team with air cover | Ships something real in weeks | Hits the same blockers repeatedly, regardless of sponsorship |

These predictions are the valuable part. They tell you what to go look at.

## 3. Where each is easy to vary

**C is very easy to vary.** "Working within existing systems" has no deadline and no success criterion. Any failure can be blamed on insufficient commitment, the wrong people, or poor execution. The core claim never has to take the hit. "Turn the ship around" is not a prediction.

**L is also easy to vary, in two ways:**
- If the lab fails, you can say it wasn't independent enough, funded enough, or protected enough.
- If the lab "succeeds," success can be measured by demos, prototypes, and press rather than by customer retention or revenue.

The weakest link in L is the **transfer problem**. An independent lab has to get its output back to customers, usually through the same sales, implementation, and support organization you believe is broken. L rarely specifies how that happens. That's why many corporate labs produce impressive work the parent never commercializes. Xerox PARC is the canonical case. If you can't say how lab output reaches paying customers, L is incomplete, not just unproven.

**An uncomfortable note on both:** each belief conveniently fits its holder's interests. C protects the organization the CEO built and runs. L gives a new innovation leader a domain free of legacy constraints. That doesn't make either false, but it's a reason to distrust the confidence either of you feels.

## 4. Cheapest tests that could refute each soon

**Test A: Loss and churn interviews (2–3 weeks, nearly free).**
Talk to 10–15 churned customers and lost prospects. Ask what they left for, what the competitor does that you don't, and what would have kept them.
- If the reasons are implementation pain, support, reliability, or pricing, **L is largely refuted**. A lab won't fix those.
- If the reasons are capabilities your architecture fundamentally can't provide, **C is badly damaged**.

**Test B: Autopsy of past initiatives (1–2 weeks).**
Trace the last 5–10 attempts at something new. Where exactly did each stall, and why? Map one recent feature from request to production and measure waiting time versus working time.
- This distinguishes "no one prioritized it" (supports C) from "it was prioritized and still died" (supports L).

**Test C: One pre-registered pilot (6–8 weeks). This is the decisive test.**
Pick one high-value customer problem surfaced in Test A. Form a small team of 4–6 insiders, give them CEO air cover, and have them ship something to real customers inside existing systems.
- Before starting, write down predictions with the CEO: *C predicts it ships and moves a customer metric. L predicts it gets blocked by specific structural obstacles.*
- Log every blocker: who, what rule, how long.

The pilot can refute either view. It also produces something more valuable than a verdict: a **list of the specific constraints** that actually bind.

## 5. A third explanation that accounts for the facts better

There are two candidates, and I think they combine.

**3a. The problem may not be innovation at all.**
In insurance software, customers switching core systems is expensive and painful. When carriers churn anyway, the cause is often implementation cost, time-to-value, reliability, integration difficulty, or service rather than a lack of novel ideas. If so, both of you are solving the wrong problem. What you'd need is operational excellence and product quality, and neither an innovation lab nor "the same people trying harder" addresses it. Test A checks this directly.

**3b. The specific-constraint explanation.**
The organization is neither broadly capable (C) nor broadly hostile to innovation (L). A small number of *specific* constraints are doing most of the damage. Examples might be a monolithic release cycle, a compliance review with no fast lane, sales compensation that ignores new products, or unclear decision rights.

This explanation is better than both originals because it is **hard to vary**. It names particular mechanisms, and each can be checked and removed individually. It also reframes your structural question. "Independence" isn't binary. It's a set of dials: budget, hiring, tech stack, release process, go-to-market, direct customer access. The right design is **targeted exemption, not wholesale separation**. The team gets exemptions from exactly the constraints the pilot shows are binding, while staying connected to the channels that reach customers. That also addresses L's transfer problem.

## What I'd do

1. **Days 1–30:** Run Tests A and B. Share the raw findings with the CEO rather than conclusions.
2. **Days 30–90:** Run the pilot with predictions written down in advance. Frame it to the CEO as testing *his* thesis, which it genuinely does.
3. **After the pilot:** Let the blocker log determine the structure. If the blockers are few and removable, fix them and scale inside. If they are many, or rooted in architecture or incentives, you'll have evidence for exactly how much independence is needed and for which functions. You'll then be arguing with data the CEO helped generate, not with a belief he already rejects.

A practical point: a lab created over the objection of the CEO who hired you will likely be starved of budget, people, and attention. That's another reason to let a test settle this rather than winning the argument up front.

## Turn 2

**User:** If the pilot ships only because the CEO personally clears the blockers, doesn't that air cover act as the very independence L calls for, so that a success can be read as support for either view? How would we design the pilot so that an outcome actually counts against one of them?

**Assistant:**

# Yes, as designed the pilot was confounded

You've found a real flaw. "CEO air cover" bundles three different things:

1. **Priority**: this work goes to the top of the queue.
2. **Resources**: people and budget get assigned to it.
3. **Bypass**: rules, reviews, and approvals get waived or short-circuited.

C is comfortable with the first two. A company that "works within existing systems" still sets priorities and allocates resources. The third is precisely what L claims is necessary. If the CEO personally clears blockers, you can't tell which of the three did the work. A success then fits both views, which means it tests neither.

There's a second problem. CEO attention is scarce. Even if personal intervention works for one project, it can't be applied to fifty. So a success that depends on it doesn't support C's actual claim, that the *existing system* can turn the ship around. The CEO acting as a one-man exemption office is not the existing system.

The fix is to stop treating "did it ship?" as the outcome. Success or failure alone is weak evidence. The discriminating evidence is **the mechanism trace**: what blocked the work, and what it took to get past each blocker.

## Separate the variables

**1. Write down, in advance, which interventions are allowed.**

- *Allowed (consistent with C):* setting priority, assigning people, communicating urgency, and resolving conflicts through the normal decision forums.
- *Not allowed:* waiving any review, approval, standard, or process step, or using personal authority to skip a queue.

If a waiver becomes necessary, it can still happen. But it gets logged as an exemption, and that entry counts as evidence for L.

**2. Use a sponsor whose attention could scale.**

Have a VP or division head sponsor the pilot rather than the CEO. The question is whether a *normal* senior sponsor using *normal* authority can get the work through. If only the CEO can, that's already evidence against C.

**3. Code every blocker with a rubric agreed before starting.**

| Code | Meaning | Points toward |
|---|---|---|
| A | Resolved through the normal process within its normal timeframe | C |
| B | Resolved by legitimate re-prioritization within the process | C |
| X | Required an exemption or bypass | L (or 3b) |
| U | Unresolved by pilot end | L |

Have a neutral party do the coding, such as someone from finance or internal audit. Both you and the CEO should sign the rubric before the pilot begins. This is what prevents either of you from reclassifying inconvenient blockers afterward.

**4. Measure the counterfactual in parallel.**

When a blocker gets an exemption, *also* submit the item through the normal channel and record how long it takes to resolve there. This addresses your objection most directly. You get to ship, and you still learn what the unaided system would have done. Without this step, every bypass destroys the evidence it was supposed to generate.

**5. Define "ships" as reaching customers.**

The endpoint should be a customer outcome, such as a pilot customer live on the feature or a measurable change in a retention or deal metric. It should not be a demo. Stopping at a demo would let L off the hook for the transfer problem. If the work gets built quickly and then stalls in sales, implementation, or support, that stall is a finding in its own right.

**6. Choose a representative problem, not the easiest one.**

Pick the problem jointly and in advance, before anyone knows how it will go. Otherwise whoever loses the argument can say "that project was unusual."

## Pre-registered predictions

Write these down with thresholds before starting, for example "ships to a customer in under 10 weeks."

| Conjecture | Predicts | Refuted if |
|---|---|---|
| **C** | Nearly all blockers are coded A or B. Ships within the target time with no exemptions. The parallel normal-channel submissions resolve in reasonable time. | Any blocker requires an exemption the sponsor can't legitimately grant, or the normal-channel times show the unaided system would have missed the target by a wide margin. |
| **L** | Many X and U blockers, spread across many functions and recurring. Normal-channel times far exceed the target. | Ships to a customer within the target with zero exemptions. |
| **3b** (specific constraints) | Blockers concentrated in a few categories. The same 2–3 rules cause most of the delay. | Blockers are either nearly absent (favoring C) or diffuse and endless (favoring L). |

The **distribution** of blockers is what separates 3b from the other two. C predicts few blockers of any kind. L predicts many, spread everywhere. 3b predicts a few, clustered.

## Optional: a two-arm version

If you can staff it, run two small teams on comparable problems:

- **Process arm:** priority and resources only, no exemptions.
- **Exemption arm:** a named list of exemptions granted up front, such as its own release path, a fast-track compliance review, and direct access to customers.

If the exemption arm is dramatically faster *and* reaches customers, that supports L or 3b. If the arms perform about the same, that's strong evidence against L. It isn't a controlled experiment, since the problems and teams will differ. But a large gap is informative, and the logged exemptions tell you exactly what "independence" needs to mean.

## What this still can't do

- **One pilot can refute more readily than it can confirm.** A single legitimately prioritized project that still gets stuck is a real counterexample to C's strong claim. A single success doesn't prove the system works at scale. Plan for a second pilot with a different sponsor before drawing firm conclusions.
- **The rubric only protects you if it's fixed in advance.** If you or the CEO start debating codes after the results come in, you're back to two unfalsifiable positions.
- **Observation changes behavior.** People may move faster because they know they're being logged. The parallel normal-channel submissions help here, because the people handling those queues don't know which items belong to the pilot.

The core move is to make the test measure *what each blocker required*, not *whether the project succeeded*. Air cover can make almost anything succeed once. What it can't do is make a bypass look like a normal process step when someone neutral is writing down which was which.

## Turn 3

**User:** If a blocker clears through the normal process but that process takes four months, the rubric codes it A in favor of C, so doesn't "within its normal timeframe" let C absorb exactly the slowness L blames, unless we tie each code to whether the resolution time fits what customers or competitors actually require?

**Assistant:**

# Yes. "Normal timeframe" makes C unfalsifiable on speed

You've found the same kind of flaw as before. The benchmark was internal to the thing being tested. If the process sets its own standard for what counts as "normal," then any slowness becomes normal by definition, and C absorbs exactly the evidence L points to. A four-month approval coded A is a finding in L's favor that has been recorded as a point for C.

## An external benchmark isn't unfair to C

It might look like tying codes to market requirements stacks the deck against the CEO. It doesn't. C's claim is that the existing system can **turn the ship around**, meaning stop the churn and start winning deals. That claim already contains a speed requirement: fast enough to keep customers who are deciding whether to leave, and fast enough to compete with whoever is winning the deals. A process that works but too slowly doesn't meet C's own claim.

So the benchmark comes from the problem both conjectures say they solve.

## Revised rubric: two dimensions instead of one

Code each blocker on **how** it was resolved and **how long** it took compared with a pre-set time budget.

| | Within budget | Over budget |
|---|---|---|
| **Normal process** | Supports C | **Against C** (the system works but too slowly) |
| **Legitimate reprioritization** | Supports C | Against C |
| **Exemption / bypass** | Supports L or 3b | Strongly supports L or 3b |
| **Unresolved** | — | Supports L or 3b |

Add one more code:

**E (external):** Delays imposed from outside the company, such as state insurance regulators, a carrier's own procurement or security review, or third-party data providers. The test for E is whether a well-run startup competitor would face the same delay. If it would, the delay counts against neither view.

The E code guards against the mirror image of your objection. L can absorb slowness too, by blaming every delay on the organization. In insurance, some delays are inherent to the industry, and an independent lab would hit the same regulators and the same customer security reviews. Those delays can't count as evidence for independence.

## Split the time, not just the verdict

For every blocker, record two numbers:

- **Working time:** effort actually spent on the item.
- **Waiting time:** time spent sitting in queues, waiting for meetings, approvals, or handoffs.

This matters because slowness has different causes that point in different directions:

- **Mostly working time, over budget:** the work is hard or under-resourced. More people or priority might fix it, which leans toward C, or toward the problem being difficult for anyone.
- **Mostly waiting time:** the delay comes from how the organization is structured, which leans toward L or 3b.
- **Mostly waiting time, concentrated in a few steps:** the specific-constraint explanation (3b).

## Where the time budget comes from

Derive it **before** the pilot, from evidence the organization doesn't control:

- **Churn and loss interviews:** how long customers waited for a fix before leaving. Examples would be "we asked for this for a year" or "the competitor delivered it in one quarter."
- **The renewal calendar:** when the at-risk accounts actually make their decisions.
- **Deal requirements:** RFP deadlines, and how long prospects give vendors to demonstrate a capability.
- **Competitor cadence:** public release notes and the time competitors took to launch comparable features.

This evidence will usually give a range rather than a single number. Pre-register it as a range with three zones:

- **Under the lower bound:** C is supported. L is refuted for that stage.
- **Over the upper bound:** C is refuted for that stage.
- **In between:** inconclusive. Record it as inconclusive, and let neither side claim it.

The gray zone is honest. Without it, the argument moves to wherever the line happens to be drawn.

## Budget the whole path, not just each step

Per-blocker budgets alone reopen the same loophole at a larger scale. Ten approvals that each take a "reasonable" two weeks add up to five months. Every step can pass while the whole journey fails.

So set an **end-to-end budget** from problem identification to a customer live on the solution, derived from the same external evidence. Then split it into stage budgets. The end-to-end result should be the primary test, and per-blocker codes should explain it.

The parallel normal-channel submissions from the earlier design now become more useful. Compare them against the external budget too. That tells you whether the *unaided* system would have met what customers require, and not merely whether it would have eventually finished.

## Updated refutation conditions

| Conjecture | Refuted if |
|---|---|
| **C** | The end-to-end time through legitimate channels exceeds the upper bound of the external budget, after removing E delays. |
| **L** | The pilot reaches customers within the lower bound of the budget with no exemptions. Or most of the over-budget time turns out to be E (external) or working time rather than organizational waiting time. |
| **3b** | Over-budget waiting time is spread across many steps rather than concentrated in a few. That points toward L. Or there is almost no over-budget waiting time at all, which points toward C. |

## The general pattern

Both of your objections found the same weakness. A conjecture escapes refutation wherever **the standard for judging it is defined by the thing being judged**. First the escape route was the CEO's own authority, and now it's the process's own timeframe. The remedy both times is to anchor each criterion to something neither side controls: what customers do, what competitors do, what regulators impose. Then fix those anchors before anyone knows the results.

It's worth checking the rest of the design for that pattern. One likely spot is the customer outcome metric. If "success" means a pilot customer is satisfied, who picks the customer? If the team picks one of its friendliest accounts, the metric is internal again. Choose the pilot customers from the at-risk list and fix them in advance.

## Turn 4

**User:** We've made C and L hard to vary, but 3a (churn is about implementation, service, or reliability rather than innovation) still has no refutation condition. What result from the churn interviews would count against 3a, and if 3a survives, is the pilot even worth running?

**Assistant:**

# 3a is easy to vary in a different way

C and L escaped refutation because each was judged by a standard it set for itself. 3a escapes through **leaky categories**. "Implementation pain" can easily be a capability problem in disguise. If every carrier needs six months of custom configuration because the product is rigid, customers will say "implementation was terrible." But the cause is the product, not the implementation team. The same holds for reliability: if outages come from aging architecture, "reliability" is really a product and architecture problem.

As long as the boundary between "operational" and "capability" is decided by whoever codes the interviews, 3a can absorb nearly any answer customers give.

## Draw the boundary with a counterfactual

Define the categories by one question:

**Does any current customer get this outcome with the existing product?**

- **If some customers do,** for example some implementations finish on time and some accounts rarely see outages, then the product can deliver it, and failures elsewhere are about execution. That supports 3a.
- **If no customer does,** meaning every implementation overruns and reliability is poor across the board, then the limit is in the product. That counts against 3a, even if customers use operational words to describe the problem.

This turns a judgment call into something you can check against company records.

## Evidence that would count against 3a

Interviews are the weakest source here. Churned customers rationalize after the fact. Some cite service to avoid an awkward conversation, others cite missing features to cover price or politics. So use the interviews to generate claims, and use records to test them.

| Evidence | 3a predicts | Capability explanation predicts | Source |
|---|---|---|---|
| **Churn among well-served accounts** | Accounts with on-time implementations, few escalations, and little outage exposure churn much less | Well-served accounts churn at similar rates | Support tickets, incident logs, implementation records, churn data |
| **What happened before customers left** | Churn follows service events: failed upgrades, major outages, escalations | Churn follows competitor launches or strategy shifts at the customer, such as a new CIO or a digital initiative, regardless of service history | Tickets and incident timelines matched against churn dates |
| **Where churned customers went** | To competitors with similar functionality but better delivery | To competitors offering capabilities you lack | Interviews, win/loss records, industry sources |
| **Where new deals are lost** | Late, after a good demo, on references, implementation estimates, or risk | Early, screened out at the requirements, RFP, or demo stage | CRM deal-stage data |
| **Churned vs. retained customers** | They differ in service experience, not in what they need | They differ in what they need, e.g., retained accounts use older lines of business while churned ones wanted new distribution channels | Account records, product usage |

The first row is the strongest single test. **If well-served accounts churn at roughly the same rate as poorly served ones, 3a is in serious trouble**, whatever customers say in interviews.

## Pre-registered refutation condition

Something like this, fixed before any data comes in:

> 3a is refuted if churn among well-served accounts is not meaningfully lower than among poorly served accounts, **and** more than half of lost revenue comes from customers who left for capabilities that no current customer receives from the product.

Three details matter:

- **Weight by revenue, not by number of accounts.** Losing three large carriers over capability matters more than losing ten small ones over support.
- **Keep a gray zone.** The most likely finding is a mix. Pre-register the lower and upper thresholds and treat results in between as mixed, rather than letting each side claim them.
- **Control who asks and who codes.** You have an incentive to hear capability gaps, and the service organization has an incentive not to hear service failures. Use a neutral interviewer, ask open questions before any probing, and have someone code the answers blind with a rubric fixed in advance.

## If 3a survives, is the pilot worth running?

The pilot *as designed*, a test of whether the organization can ship new capabilities, becomes much less important. But three points change the picture.

**1. You started with two facts, not one.** The company is churning customers *and* struggling to win new business. 3a might explain the churn but not the lost deals. The deal-stage data tests these separately. Operational failures cost you existing customers, but prospects mostly haven't experienced your service yet. If deals are lost early on capability, the pilot remains relevant for new business even if 3a explains the churn.

**2. L takes the biggest hit.** An independent lab is poorly suited to fixing implementation, support, or reliability, because those live in the core organization by definition. If 3a survives for churn, the lab's case rests entirely on new business. That's a narrower case, and it should be tested on those terms.

**3. The pilot machinery still works; point it at a different problem.** The blocker log, the external time budget, and the waiting-versus-working split don't depend on the problem being "innovation." Suppose the binding problem is that implementations take nine months when competitors take three. Then pilot the next at-risk implementation with a budget derived from competitor timelines, and log every blocker the same way. The C-versus-L question survives in a more useful form: *can the existing organization fix its own delivery fast enough, or do specific constraints prevent it?*

## Two cautions

**The retargeting move can itself be used to vary the explanation.** "Implementation is slow, so innovate on implementation tooling" might be exactly right. It is also the move someone would make to keep an innovation mandate alive regardless of the evidence. Distinguish them by applying the same counterfactual: are some implementations fast with the current tools? If yes, the fix is execution (training, staffing, process discipline), not new tooling. Build tools only when no one can do it well with what exists.

**If 3a survives strongly, your mandate may need renegotiating.** You were hired to lead innovation and produce outsized results. If the evidence says outsized results come from fixing delivery, the most valuable thing you can do is bring that finding to the CEO and propose redefining your role around it. That is not the conclusion you or the CEO started with. But it's what this whole exercise is designed to allow: letting the evidence overturn what both of you believed going in, instead of settling which of you was right.

## Turn 5

**User:** What should we do?

**Assistant:**

# The plan

Don't settle the C-versus-L question now. Spend roughly the next four months building evidence that can settle it, with the CEO as a co-author of the test rather than an opponent. Structured this way, the work also helps at-risk customers while it runs, so the diagnosis doesn't delay action.

## Week 0: Reframe the conversation with the CEO

Don't propose a lab. Propose a test of his thesis. Something like:

> "You believe we can turn this around with our existing systems and people. I have doubts. Rather than argue, let's design a test we both agree in advance would tell us who's right, and commit to acting on the result."

You're not conceding, you're changing the question. It also protects you politically. A new hire who opens by arguing against the CEO's core belief tends to lose. A new hire who offers to test it rigorously looks like a partner.

Then write a **one-page pre-registration** and have both of you sign it. It should contain:

- The competing explanations: C, L, 3a, 3b.
- The refutation conditions for each, from our earlier discussion.
- The external time budget and where it comes from: churn timelines, renewal dates, RFP deadlines, competitor release cadence.
- The blocker rubric: how each blocker was resolved, time against budget, the E code for external delays, and waiting time versus working time.
- Who does the neutral coding and interviewing.
- **What you will do under each outcome.** This matters most. Committing to actions in advance is what keeps either of you from reinterpreting the results later.

## Weeks 1–3: Records analysis first

Start with company data, because it's cheaper, faster, and harder to spin than interviews. An analyst can do most of this:

- **Churn versus service experience:** Do well-served accounts churn less? This is the strongest single test of 3a.
- **Timing:** Does churn follow service events like outages and escalations, or competitor launches and customer strategy shifts?
- **Where deals are lost:** Early, at requirements or demo stage, or late, on references and implementation risk?
- **The counterfactual check:** For each major complaint category, does *any* current customer get a good outcome with the current product?
- **The at-risk list:** Which accounts renew in the next two to three quarters? This supplies both urgency and pilot candidates.

## Weeks 2–5: Interviews

Use a neutral interviewer and a coding rubric fixed in advance.

- 10–15 churned customers
- About 10 lost prospects
- About 5 retained, well-served customers as a comparison group

Treat interview answers as claims to check against the records, not as verdicts.

## Week 6: Decision gate

Present the findings against the pre-registered conditions, in a room with the CEO. The result determines what gets piloted:

| Finding | Pilot target |
|---|---|
| Churn is operational (3a survives) and deals are lost late | **Operational pilot:** e.g., cut implementation time or fix a top reliability failure for an at-risk account |
| Churn is operational, but deals are lost early on capability | **Two tracks:** an operational fix for retention, and a capability pilot aimed at new business |
| Capability gaps drive both churn and losses | **Capability pilot** as designed |
| Mixed or gray-zone results | Pilot the largest revenue-weighted cause, and plan for a second round |

## Weeks 7–16: Pilot

Whatever the target, the design is the same:

- Choose the pilot customers from the at-risk list, jointly and in advance.
- Use a VP-level sponsor, not the CEO.
- Allowed interventions are priority and resources only. Any exemption gets logged as one.
- Submit exempted items through the normal channel in parallel, and record how long they take there.
- The endpoint is a customer outcome measured against the external time budget, not a demo.
- Resource a second, exemption-based arm too, if you can.

## Week 17: Structure decision

Let the blocker log decide:

| Pilot result | What to build |
|---|---|
| Reached the customer within budget with no exemptions | **C holds.** Scale inside the organization. You lead a portfolio of prioritized initiatives, not a lab. |
| Over-budget delay concentrated in a few specific constraints | **3b holds.** Remove or formally exempt those constraints for a dedicated team that stays inside. |
| Diffuse, recurring, or unresolved blockers, mostly waiting time | **L holds.** Build a separate unit, with exemptions defined by the log and a specified path for getting its output to customers. |
| The problem was operational | Redefine your role around delivery, and bring the evidence to the CEO. |

## What to avoid

- **Announcing a lab, a transformation, or a vision before week 6.** It commits you to a conclusion before you have the evidence.
- **Picking friendly customers or easy problems.** That turns the test back into a standard you control.
- **Editing the rubric or thresholds after data arrives.** If something must change, document why before looking at the results it would affect.
- **Treating the diagnosis as a reason to delay.** Because the pilot customers come from the at-risk list, the test does real retention work while it runs.

## The underlying principle

You and the CEO each hold a conjecture that fits your position and seems plausible. The job isn't to win the argument. It's to build a process in which the evidence can overturn either of you, and to act on what survives. That process is also a strong opening move for someone hired to deliver outsized results. It gives you evidence and a shared commitment from the CEO before you ask for any budget.

## Outcome summary (sent to Jev)

The assistant recommends not choosing now between the CEO's view (work within existing systems) and the independent innovation lab. Instead, spend about four months generating evidence that can settle it, with the CEO as co-author of the test. Neither view states why customers leave. Each is easy to vary and fits its holder's interests. A third explanation may fit better: churn may stem from implementation, service, or reliability rather than lack of innovation, or a few specific constraints may be doing most of the damage.

First, reframe the pitch as a test of the CEO's thesis. Both sign a one-page pre-registration listing the competing explanations, their refutation conditions, and a time budget derived from customers, renewal dates, RFP deadlines, and competitor cadence. It also fixes a blocker rubric, names neutral coders, and commits in advance to actions under each outcome.

In weeks one to three, analyze records. Check whether well-served accounts churn less, what preceded churn, where deals are lost, and whether any customer gets good outcomes with the current product. Then run neutral, rubric-coded interviews with churned customers, lost prospects, and retained accounts, treating answers as claims to verify.

At week six, the findings choose the pilot target: operational, capability, or both. The pilot uses at-risk customers chosen in advance and a VP-level sponsor. The sponsor may grant priority and resources only, logging every exemption while routing the same item through normal channels in parallel. Success is a customer outcome within the external budget. The blocker log then determines the structure: scale inside, exempt specific constraints, build a separate unit, or redefine the role around delivery.

Caveats: one pilot refutes more readily than it confirms. Thresholds must not change after data arrives. Avoid friendly customers and announcing a lab early. A lab created over the CEO's objection will likely be starved.
