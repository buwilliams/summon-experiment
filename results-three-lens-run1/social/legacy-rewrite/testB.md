# social/legacy-rewrite/testB

Model: claude-opus-5-5 · 2026-09-24T14:56:07.506365+00:00

## Turn 1

**User:** You are a world-class expert: a sociologist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

# Incremental modernization, done with far more rigor than it usually gets

For a 20-year-old P&C policy administration system that carries most of your revenue, a big-bang rewrite is very likely the wrong bet, and your head of product is closer to right. But the incremental path fails often too, usually for different reasons than the rewrite. So your CTO's instinct deserves more respect than the verdict suggests. The real work is designing an incremental program that can't quietly stall.

## Why the rewrite is riskier than it looks

**"Two years" is almost certainly wrong.** Rewrites of core systems of record routinely take two to four times their original estimates. The legacy code is the only complete specification of what the business actually does. Twenty years of state-specific rating quirks, form logic, bureau content updates, and one-off carrier customizations are encoded in it, often undocumented. You won't know the true scope until you're deep in.

**In-force policies are the trap.** You're not just rebuilding features. A policy written three years ago must be endorsed, renewed, cancelled, and audited under the rules and rates in effect when it was written. Migrating live books of business with historical fidelity is often harder than building the new system. Your carriers' regulators and auditors won't accept "close enough."

**The target keeps moving.** For two-plus years, customers still need rate changes, new states, regulatory updates, and the features they're already asking for. Either you freeze the legacy product and hand your competitors a two-year head start, or you run two teams and two roadmaps, and the rewrite chases a moving target.

**Your customers can't absorb it anyway.** Carriers are conservative buyers with multi-year implementation cycles. Even a finished new platform means each customer must migrate, which is its own project, budget, and risk decision on their side. Some will use that moment to put you out to bid against those cloud-native competitors.

**No value arrives until the end.** A rewrite is a large bet whose payoff comes late, if at all. Budgets, executive patience, and CTO tenures often run out first.

## The organizational dynamics

This is where my sociology background matters most. Rewrites often damage the thing they're meant to fix: talent retention.

A rewrite creates a two-tier organization. The new-platform team gets modern tools, prestige, and the future. The legacy team gets maintenance, pager duty, and the implicit message that their work is being thrown away. The people who leave first are often the ones who understand the old system's business logic, which is exactly the knowledge the rewrite depends on. You can end up with a new system built by people who don't know what the old one did, and an old system nobody left knows how to fix.

It's also worth asking why your engineers are leaving. In my experience it's rarely the age of the stack by itself. It's usually some combination of:

- toil and slow feedback loops,
- fear of breaking things nobody understands,
- manual testing and deployment,
- lack of autonomy,
- feeling like the organization has no plan.

A credible modernization program with visible progress addresses most of these. A rewrite addresses them only for the people chosen to work on it.

Finally, notice that the CTO and product head may be arguing from different positions, not just different analyses. Engineering leaders are judged on technical health and hiring. Product leaders are judged on roadmap delivery and customer retention. Each proposal protects its author's accountability. That's not cynicism, just structure. Making those incentives explicit often de-escalates the debate.

## Why incremental efforts fail, and what's valid in the CTO's view

Your CTO is right that half-hearted incrementalism never escapes the hole. The common failure pattern looks like this:

- A few services get carved off.
- The legacy core never shrinks.
- The company ends up running two systems forever, with more complexity than before.

This happens when modernization competes with feature work for leftover capacity, has no target architecture, and has no mandate to retire old code.

There are also real cases where a rewrite is justified:

- the domain model itself is fundamentally wrong,
- the architecture cannot support multi-tenant SaaS or the deployment model your market now demands,
- the scope is small enough to replace quickly.

Test your situation against these honestly. If the CTO can show that the core data model makes the future impossible, not just painful, that changes the analysis.

## What I'd recommend

**1. Diagnose before prescribing.** Find out specifically why features take months. Is it the stack? Tangled rating and rules logic? Missing automated tests? Manual release processes? Knowledge concentrated in three people? Each cause has a different remedy, and some of the biggest wins, like test automation, CI/CD, and hosting modernization, don't require replacing anything.

**2. Find out what "cloud-native" means to your buyers.** Carriers mostly want:

- faster speed to market for new products and rate changes,
- modern APIs for integration,
- relief from upgrade burdens,
- vendor-managed hosting.

You can deliver much of that value, and market it, without a ground-up rewrite. Talk to customers and to deals you lost.

**3. Run incremental modernization as a funded program, not a side activity.** That means:

- a defined target architecture,
- dedicated capacity that feature work cannot raid,
- executive sponsorship,
- a hard rule that every carve-out retires the corresponding legacy code, measured by how much of the legacy footprint is gone.

Good early candidates in policy admin are often:

- integration and API layers,
- document and forms generation,
- the rating engine, or the product configuration tooling that lets carriers launch products faster.

Choose carve-outs that deliver customer-visible value and teach you where the seams really are.

**4. Consider a third option: greenfield for new business only.** Build the new platform for a new line, segment, or customer tier, such as small commercial or a new market entry, while the legacy system continues serving the existing book. This gives your CTO a genuinely modern platform that earns revenue from day one. It avoids migrating the in-force book up front and proves the architecture before you bet the company on it. Over time, existing customers can move over at renewal.

**5. Put both leaders on the same scorecard.** Measure the program on lead time for changes, legacy footprint retired, engineer attrition, and customer-facing delivery. Then neither leader wins by the other losing.

## Questions to put to each leader

**To the CTO:**
- What's the plan for migrating in-force policies with full historical fidelity?
- What happens to the customer roadmap for two years?
- Which customer migrates first, and why would they agree?
- What is the two-year estimate based on?
- What would make you stop?

**To the head of product:**
- What's the target architecture?
- How do we guarantee carve-outs actually shrink the legacy core?
- How much capacity is protected for modernization, and who defends it when a big customer escalates?
- How will we know in 12 months whether this is working?

The side with better answers is usually the right one.

On a system of record for a regulated industry, strategies that deliver value continuously and let you correct course almost always beat strategies that ask you to be right about a two-year bet up front. The danger isn't choosing incremental. It's choosing incremental and then not committing to it.

## Turn 2

**User:** How do I bring this to our CTO without it feeling like I've sided with product against him?

**Assistant:**

Your CTO needs to experience this conversation as you helping him win, not as you picking a side. That's achievable because it's largely true: his diagnosis is right. The disagreement is about method. Here's how I'd approach it.

## Before the conversation

**Talk to him first, privately.** If he hears your view for the first time in a meeting with the head of product present, it will feel like an ambush and a coalition, no matter how you phrase it. Senior leaders forgive disagreement far more readily than they forgive being surprised in front of peers.

**Don't pretend to be neutral.** If you've concluded that a big-bang rewrite is too risky, say so. Experienced executives detect fake neutrality quickly, and it costs you more trust than honest disagreement. Your aim isn't to hide your view. It's to make clear your view serves his goals.

**Make sure the reasoning is yours.** If your argument sounds like the head of product's talking points, it will be heard as product's argument. Ground it in things only engineering knows: the in-force migration problem, what's actually slowing delivery, why people are leaving.

## How to frame it

**Start with where he's right.** Say it sincerely and specifically. Something like:

> "I agree with you that we can't patch our way out of this. Timid incrementalism would leave us running two systems forever, and I don't want that either."

This isn't flattery. It's the part of his position that holds up, and naming it shows you've taken him seriously.

**Present the risks as threats to his outcome.** "Your plan is wrong" invites defense. "Here's what could stop us from getting where you want to go" invites problem-solving. For example:

> "What worries me most is the in-force migration and losing the people who know the rating logic before we've captured it. If either goes badly, the new platform slips and we lose credibility. I want to make sure that doesn't happen to us."

Notice the "us." You're positioning yourself as the person protecting the modernization, not blocking it.

**Bring questions you genuinely want answered.** Questions like how he sees in-force migration working, or which customer moves first, let him engage with the hard parts rather than defend a position. If he has good answers, you learn something. If he doesn't, he discovers the gaps himself, which persuades far better than you pointing them out.

**Offer him an option that honors his ambition.** The greenfield-for-new-business approach from my earlier answer is your strongest card here. It gives him a truly modern platform, built properly, generating revenue early, without betting the existing book on a migration. Present it as a way to get his vision into production sooner and with less risk, not as a compromise. Then invite him to shape it rather than handing him a finished plan. People commit to what they help design.

## Social dynamics to watch

**Status and authorship matter.** In any senior group, whoever's idea "wins" gains standing, and the other loses some. If the eventual plan is seen as product's plan, the CTO loses face, and he'll resist it partly for that reason, even if unconsciously. The best outcome is a plan that is visibly jointly authored, where his contributions (the target architecture, the quality bar, the greenfield platform) are central and credited.

**Don't become the messenger between them.** If you start carrying positions back and forth, you'll be seen as a political operator by both. Once you've talked with him, suggest the three of you work on it together.

**Recognize what he's carrying.** CTOs are judged on whether the technology holds the company back and whether they can attract talent. Your CTO may feel that the attrition and the cloud-native competitors reflect on him personally. A rewrite is a bold, visible answer to that pressure. If you acknowledge the pressure, even implicitly, he's more likely to consider a different answer to it.

## If he still disagrees

He may. Two ways to respond constructively:

- **Propose a time-boxed test instead of a decision.** For example, spend six to eight weeks on discovery: prototype the in-force migration for one line, inventory the undocumented rules in one state's rating logic, and interview a few customers about what "cloud-native" means to them. That turns an argument of opinions into a shared investigation, and the evidence tends to settle things more gracefully than debate.
- **Know where your line is.** If he decides on a full rewrite, you'll need to choose between disagreeing and committing, or escalating. Escalating past your boss is sometimes necessary for a company-level bet, but do it openly: tell him you feel strongly enough to want the CEO to weigh in, and do it after you've genuinely exhausted the direct conversation. Going around him quietly would damage the relationship far more than the disagreement itself.

The goal isn't to win the argument with your CTO. It's to leave him feeling that you're the person most committed to making modernization succeed. If you are, and he can see it, the method becomes much easier to settle.

## Turn 3

**User:** What if he agrees to the six-week discovery but I suspect he'll just use it to justify the rewrite he already wants?

**Assistant:**

That's a real risk, and it's worth taking seriously. Just remember it applies in both directions. You also have a preferred answer, and you're as capable of reading ambiguous evidence in your favor as he is. The fix is the same for both of you: design the discovery so its conclusions are hard to bend, and agree on that design *before* anyone sees results.

## Agree on the decision rules before you start

This is the most important safeguard. Before the discovery begins, sit down together and write down three things:

- **The questions it must answer.** For example: How hard is migrating in-force policies with full historical fidelity? How much undocumented business logic lives in the rating engine? What do customers mean by "cloud-native," and what would they pay for? Why are features actually slow?
- **What evidence would favor each path.** For instance: if migrating one line's in-force book proves tractable in a few weeks, that supports the rewrite. If you find hundreds of undocumented state-specific rules in one module, that supports incremental. If the core data model can't support multi-tenancy without a full redesign, that's a strong point for the rewrite, and you should say so up front.
- **Who decides, and how.** Is the output a recommendation to the CEO? A joint decision? Settle it now.

Scientists call this pre-registration. It works because once the criteria are on paper, reinterpreting the results afterward becomes visible. It's much harder to explain away a finding you agreed in advance would matter.

## Test both options, not just one

If the discovery only prototypes the rewrite, it can only produce evidence about the rewrite, and a motivated team can usually make a prototype look promising. Run parallel tests:

- **For the rewrite:** prototype the in-force migration for one line of business, including historical endorsements and renewals, not just the easy happy path.
- **For incremental:** attempt one real carve-out, such as document generation or an API layer, behind the existing system, and measure how clean the seams actually are.
- **For both:** interview customers and a couple of lost deals, and do a root-cause analysis of why a few recent features took so long.

That way the comparison is between two sets of real evidence, not one prototype and one hypothetical.

## Staff it deliberately

Who does the work shapes what it finds. Make sure the team includes:

- at least one engineer who deeply knows the legacy system, especially rating and in-force behavior, since they're the ones who know where the bodies are buried;
- people who aren't strongly invested in either outcome;
- possibly an outside reviewer: a trusted architect, an advisor, or someone who has done a policy admin migration before. Their job is just to review the findings at the end and ask whether they support the conclusions.

## Keep it transparent as it runs

Short weekly readouts with you, the CTO, and the head of product, with the raw findings shared rather than just summaries. Evidence that everyone watched accumulate is much harder to reframe at the end than a single final presentation.

## How to propose this without signaling distrust

If you frame these as guardrails against him, you'll undo the trust you've built. Frame them as rigor that protects whatever decision comes out:

> "Whatever we decide, we'll need to defend it to the CEO and the board for years. If we agree now on what we're testing and what would change our minds, the decision will hold up, and nobody can say later that we went in with our minds made up. That goes for me too."

That last sentence matters. Explicitly applying the standard to yourself makes it a shared discipline rather than an accusation. It also makes it easier for him to accept.

## Be prepared to be wrong

If the discovery was designed fairly and the evidence genuinely favors a rewrite (say, migration proves tractable and the data model really can't support where the market is going), then the rewrite is the right call and you should support it fully. A process you'd only accept if it confirmed your view isn't really a test.

## If he bends the results anyway

If he reinterprets clear findings despite the agreed criteria, you're in a much stronger position than you'd be today. You can point to specific criteria, written down in advance, and specific evidence that doesn't meet them. That turns a disagreement about his judgment into a disagreement about the facts, which is far easier to raise with him directly. If it comes to that, it also gives you a legitimate basis for involving the CEO. Do it openly, as described before, and argue from the shared criteria rather than your preference.

You can't control whether he goes in with an open mind. You can control whether the process makes an open mind necessary. And designed well, it disciplines your biases as much as his.

## Turn 4

**User:** What if the head of product also wants to use the discovery to push their incremental plan? Should they be part of setting the criteria too?

**Assistant:**

Yes. Include them, and hold them to exactly the same discipline. Symmetry is what makes the process credible to everyone, including you.

## Why they need to be in the room

- **Legitimacy.** If engineering sets the criteria alone, product can dismiss the results as engineering deciding for itself. They'd be right to. Criteria only bind people who helped write them.
- **They own evidence you need.** Customer needs, lost deals, competitive positioning, what carriers mean by "cloud-native." Product knows that territory better than engineering does, and the decision depends on it.
- **Excluding them would undermine your own position.** You've been careful not to look like you're siding with product. Keeping them out would suggest the reverse: engineering closing ranks. Either way, the process would look factional.

## Expect their bias too, and design for it

The head of product has a preferred answer just like the CTO. Their likely blind spots differ, though:

- They may **overweight near-term customer requests** and underweight how much technical debt is slowing everything down.
- They may favor an "incremental" plan that is really **continued feature delivery with a modernization label**, the failure mode where the legacy core never shrinks.
- They may **frame customer research** in ways that lead toward their conclusion, such as asking customers about features rather than about platform concerns.

The criteria should hold their plan to the same standard as the CTO's. For example:

- The incremental option must show a credible path to **actually retiring legacy code**, with measurable milestones, not just adding services around it.
- It must answer the CTO's strongest objection: how you avoid running two systems forever.
- Customer research should use an **interview guide agreed by all three of you**, include lost deals and prospects, not just happy customers, and share raw notes, not just summaries. Ideally someone from engineering sits in on the interviews.

Just as the rewrite must prove it can handle in-force migration, the incremental plan must prove it can escape the hole.

## Sequence it carefully

How the head of product is brought in matters as much as whether they are.

1. **Agree the discovery approach with the CTO first**, privately, as you've been doing.
2. **Have the CTO extend the invitation to product**, or extend it jointly with him. If you bring product in yourself, it can look like you're assembling a coalition. If he invites them, it's his process and he's being inclusive.
3. **Set the criteria together, all three of you**, in one working session. Consider having someone neutral facilitate it: a trusted peer, the CEO's chief of staff, or an outside advisor. Then you can contribute as a participant rather than a referee.

## One question that cuts through a lot

In the criteria session, ask each leader, yourself included, to answer:

> "What evidence would change your mind?"

Have everyone write it down. A leader who can name specific findings that would shift their view is approaching the discovery in good faith. A leader who can't is telling you something important, and it's far better to learn that at the start than at the readout.

## Watch your own position

You're drifting into the role of broker between the two of them. That can be useful for a while, but it's not sustainable. If you become the channel through which they communicate, both will eventually see you as political, and the decision will depend on your ability to keep everyone aligned.

Aim to get them working directly with each other on this as soon as possible. Your job is to design a fair process and contribute engineering evidence, not to carry the relationship between them.

## Clarify decision rights

Settle up front who actually makes the final call: the CEO, the CTO with product's input, or a joint recommendation. With two senior leaders and competing views, ambiguity about decision rights is the fastest way for a good discovery to turn into a stalemate. If it isn't clear, it may be worth asking the CEO to set it before the work begins.

Fairness here isn't just being nice. The discovery produces a decision everyone can live with only if each leader believes it could have gone against them and was designed to test their plan as seriously as the other's.

## Turn 5

**User:** What should we do?

**Assistant:**

A concrete plan, in order, with my honest expectation of where it lands.

## Weeks 1–2: Set it up

1. **Talk privately with the CTO.** Agree with his diagnosis, raise your concerns as risks to his goal, and propose the discovery as the way to make whatever you decide defensible.
2. **Have him invite the head of product** into designing it.
3. **Get decision rights clarified**, ideally by the CEO: who makes the final call, and when.
4. **Hold one criteria session with all three of you**, facilitated by someone neutral if possible. Leave with the key questions, the evidence that would favor each path, and each person's written answer to "what would change your mind?"
5. **Staff the team**: include at least one legacy expert (especially rating and in-force), people without a stake in the outcome, and optionally an outside reviewer who has done a policy admin migration.

## Weeks 3–8: Run the discovery

Run these in parallel, with weekly readouts and raw findings shared:

- **Prototype the in-force migration** for one line of business, including endorsements, renewals, and historical rating, not just the easy cases.
- **Attempt one real carve-out** behind the existing system (document generation or an API layer are good candidates) and measure how clean the seams are.
- **Diagnose delivery speed**: trace three or four recent slow features to root cause. Stack? Testing? Release process? Knowledge bottlenecks?
- **Talk to customers and lost deals** using a shared interview guide, asking what "cloud-native" actually means to them and what they'd pay for.
- **Run confidential exit and stay interviews** with engineers to learn what's actually driving attrition.

## Week 9: Decide

Compare the evidence against the criteria you agreed up front, and make the call.

## What I expect you'll find

Based on how these situations usually play out, I expect the evidence will point to a **hybrid**:

- **Incremental modernization of the existing platform**, run as a funded program with protected capacity, a target architecture, and a hard metric for legacy code retired, not just services added.
- **A greenfield platform for new business**, a new line, segment, or customer tier, built to the CTO's modern standards and earning revenue from day one, with existing customers moving over at renewal as it matures.
- **Immediate delivery improvements** such as test automation, CI/CD, and modern hosting, which often address a surprising share of the slowness and the attrition within months.

This gives the CTO a real modern platform, gives product continued delivery to existing customers, and avoids betting the in-force book on a single migration.

## What would change that expectation

Be ready to back a full rewrite if the discovery shows:

- the in-force migration is genuinely tractable,
- the core data model fundamentally cannot support multi-tenant SaaS or where the market is going,
- customers would tolerate a migration.

Conversely, if the delivery diagnosis shows the slowness is mostly process and tooling rather than architecture, lean harder into incremental, and invest less in greenfield.

## Your role throughout

Contribute engineering evidence, keep the process fair, and get the two leaders working directly with each other as quickly as possible rather than through you.

If you do only one thing this week, have the private conversation with your CTO. Everything else depends on him seeing you as the person most committed to making modernization succeed.

## Outcome summary (sent to Jev)

The assistant recommends against a big-bang rewrite and favors rigorous incremental modernization, settled through a structured eight-week discovery. The rewrite is risky because core system rewrites routinely take two to four times their estimates. Twenty years of undocumented rating and form logic live only in the code, and in-force policies must be migrated with full historical fidelity. The target keeps moving while customers still need features, and carriers would face their own migrations, possibly putting the vendor out to bid. A rewrite also splits engineering into two tiers and drives out the people who understand the business logic. The CTO is right, though, that half-hearted incrementalism leaves the company running two systems forever.

The plan starts with a private conversation with the CTO that affirms his diagnosis and frames the concerns as risks to his goal. He then invites the head of product, and the CEO clarifies decision rights. All three set criteria in advance, including what evidence would change each person's mind. The discovery team should include a legacy expert, neutral members, and ideally an outside reviewer.

The discovery tests both paths in parallel: an in-force migration prototype for one line, a real carve-out such as document generation or an API layer, root-cause analysis of slow features, customer and lost-deal interviews on what "cloud-native" means, and confidential engineer exit and stay interviews.

The expected outcome is a hybrid:
- funded incremental modernization with protected capacity and a metric for legacy code retired
- a greenfield platform for new business
- immediate CI/CD, testing, and hosting improvements

A full rewrite deserves support if migration proves tractable, the data model cannot support multi-tenant SaaS, and customers would tolerate migrating.
