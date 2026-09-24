# critical-rationalism/legacy-rewrite/testA

Model: claude-opus-5-5 · 2026-09-24T14:44:58.541672+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

**Short answer:** For a revenue-critical P&C policy administration system, incremental modernization is almost certainly the right strategy. But your CTO is pointing at a real failure mode, and the incremental plan only wins if it's designed to answer that objection rather than dismiss it.

## Why a from-scratch rewrite is especially risky in your situation

**1. The old system encodes 20 years of undocumented business rules.** Policy admin systems are full of logic that exists only in code: state-specific rating quirks, filed rate and rule exceptions, out-of-sequence endorsement handling, cancellation and reinstatement edge cases, forms logic, rounding behavior carriers have reconciled against for years. A rewrite has to rediscover all of it, usually by shipping bugs to customers. The code looks ugly partly *because* it's correct in thousands of ways nobody remembers.

**2. "Two years" is not a credible estimate.** Full PAS rewrites routinely run 2–3x over schedule. For those two-plus years, you're maintaining the old system (which still carries the revenue), building the new one, and chasing a moving target, because the old system keeps changing to meet customer and regulatory demands. Meanwhile competitors keep shipping.

**3. Your customers are insurers, and insurers migrate slowly.** This is the point rewrite plans most often miss. Even if you finish the new platform, each carrier must convert in-force policies, re-test rating against filings, re-certify integrations, and retrain staff. Carriers treat core system migrations as multi-year, high-risk projects. So you will be running both platforms for years *regardless*. A rewrite doesn't avoid the hybrid period. It just delays it until after you've spent the money.

**4. It doesn't fix your immediate problems.** Slow feature delivery and attrition get *worse* during a rewrite in the short term. Customers wait longer for features, and the engineers left maintaining the legacy system feel like second-class citizens and leave faster.

## Where your CTO is right

- **Incremental modernization often stalls.** The classic failure is a "strangler fig" that never strangles anything: a few new services get bolted on, the core never shrinks, and now you have two architectures to maintain.
- **Feature work always wins the prioritization fight.** Without protected investment, modernization gets deferred quarter after quarter.
- **Some legacy cores really can't be carved up.** If the data model and business logic are so entangled that no clean seams exist, incremental extraction can cost more than rebuilding.

These are reasons to run incremental modernization *seriously*, not reasons to abandon it.

## What makes the incremental approach actually work

- **Protected capacity.** Commit a fixed share of engineering (often 30–40%) to modernization, not subject to quarterly renegotiation against features.
- **Decommissioning targets, not just new-build targets.** Measure success by what gets *turned off* in the legacy system, not by how many new services exist.
- **Well-chosen seams.** Start with capabilities that are relatively separable and high-value. In PAS, candidates are often document and forms generation, the rating engine (exposed as a service), billing integration, the API layer for agents and portals, or new product lines built natively on the new platform from day one. Leave the gnarliest core (policy transaction processing, in-force data) for later, when you have momentum and knowledge.
- **An anti-corruption layer.** Put a clean API boundary in front of the legacy system so new components never couple directly to its internals.
- **Characterization tests before extraction.** Capture what the old system actually does, especially rating outputs, and verify the new component matches before cutover.
- **Modern work on modern tools.** New capabilities get built on the new stack. This addresses attrition directly: engineers get meaningful modern work *now*, not in two years.

On the "cloud-native" marketing pressure: an API-first architecture, hosted deployment, faster release cadence, and new products built on the modern platform will let you credibly claim most of what customers actually care about, well before the core is fully replaced.

## When a rewrite would be the better call

I'd reconsider if several of these are true:
- The legacy stack is truly unsupportable (dead language or platform, vendor end-of-life, security exposure you can't mitigate).
- Serious attempts to find seams show the system can't be decomposed at reasonable cost.
- You're targeting a substantially different market (say, a new segment or product type) where you can build fresh without migrating existing customers.
- You have the funding to run two full platforms for 4–5 years, not 2.

Even then, the smart version is usually a new platform for *new* customers or lines of business, with existing customers migrated gradually. That is effectively a large-grained incremental strategy.

## How to settle the disagreement

Rather than debating in the abstract, run a 6–10 week time-boxed investigation:
1. Map the system's major capabilities and how tangled each is with the others.
2. Pick one meaningful capability and actually extract it behind an API.
3. Get real data on migration effort from two or three customers.
4. Build a rough rewrite estimate that includes customer migration and dual-running costs.

This gives your CTO and head of product a shared evidence base. It also turns the CTO's legitimate concern (incremental efforts die quietly) into design requirements for the plan, which is usually a better outcome than one executive winning the argument.

## Turn 2

**User:** How do I pitch the 6–10 week investigation to my CTO without it coming across as me siding with product and just stalling his rewrite?

**Assistant:**

The key is to make the investigation genuinely neutral, and to make it something the CTO would want even if he's certain the rewrite is right. If it's secretly a vehicle for the incremental plan, he'll sense it, and he'll be right to resist.

## Reframe it as de-risking the rewrite

Almost everything in the investigation is work a rewrite needs anyway:

- **Mapping capabilities and dependencies** is the discovery phase of any rewrite. You can't rebuild what you haven't catalogued.
- **Characterization tests on rating and transactions** become the acceptance suite for the new platform. Without them, a rewrite has no way to prove it matches the old system's behavior.
- **Customer migration costing** is the biggest unknown in a rewrite's business case, and the board will ask about it.
- **Extracting one capability behind an API** produces the integration layer a rewrite needs to run in parallel with the legacy system during cutover.

So the honest pitch is: "If we're going to rewrite, these are the first 8 weeks of the rewrite. If the evidence points elsewhere, we'll have found out cheaply."

## Talk to him first, one-on-one

Don't introduce this in a meeting with the head of product present. That instantly turns it into a two-against-one negotiation. Go to the CTO privately, before anyone else hears it, and treat him as the person who shapes it.

## Start by agreeing with his diagnosis

He's right that the current trajectory is failing, and right that half-hearted incremental efforts tend to die quietly. Say so explicitly, and mean it. Something like:

> "I agree with you that we can't keep going like this, and I agree that most incremental modernization efforts stall. I don't want to pick a path we'll regret in 18 months, and I don't think either of us has the data yet to defend this decision to the board. I'd like to get that data fast."

## Give him ownership of the design

- **Let him define the criteria.** Ask him: "What would you need to see to be confident the rewrite is the right call? What would make you reconsider?" Then build the investigation to answer his questions.
- **Include a rewrite-favoring experiment.** For example, have a small team build one thin slice (such as a quote for one line of business) on the target modern stack. That tests his thesis directly and gives him a fair shot.
- **Agree on decision thresholds up front.** For example: "If extracting one capability costs more than X weeks, or we find no clean seams in the core, that's strong evidence for a rewrite." Pre-committing protects him from the suspicion that you'll move the goalposts.
- **Consider having him sponsor it.** If he presents the results to the exec team, it's his investigation, not a delay imposed on him.

## Make it clearly not a stall

- **Fixed end date and a decision meeting already on the calendar.** "We decide on [date], no extensions."
- **Keep the scope small.** A few engineers, not a reorg.
- **Allow parallel prep.** If he wants to start stack selection or hiring planning for the new platform meanwhile, let that proceed. It signals you're not blocking him.

## Be honest about where you lean

If you already lean toward incremental, don't pretend otherwise. He'll likely know, and discovering it later would cost you his trust. Say it plainly and name what would change your mind:

> "My instinct right now leans incremental, mainly because of customer migration timelines. But I could be wrong, especially if the core turns out to be too entangled to carve up. I'd rather we find that out with real data than argue from instinct."

Candor about your bias, paired with a real willingness to be proven wrong, is far more persuasive than feigned neutrality.

## Things to avoid

- Terms like "strangler fig" or "incremental pilot" in the pitch. They signal a predetermined answer. "Technical discovery" or "rewrite readiness assessment" are more accurate for what it actually is.
- Surfacing it to the CEO or product before he's had a say.
- Designing it so only one outcome is realistically possible. If it can't come out in favor of a rewrite, it's not an investigation.

If he still resists after all this, ask him directly what his concern is. It may be something you haven't heard yet, such as board pressure, a timeline commitment he's already made, or doubts that the organization will ever fund modernization properly unless it's framed as a big bet. Those are worth knowing, and some are legitimate enough to shape the plan.

## Turn 3

**User:** What if he's already told the CEO or board that the rewrite is happening? How do I handle it then?

**Assistant:**

That changes the dynamics a lot. His credibility is now tied to the rewrite, so anything that looks like reopening the decision threatens him personally. Your job shifts from "help decide the strategy" to "help him succeed at what he promised, while steering how it's executed."

## First, find out exactly what was said

"The rewrite is happening" can mean very different things:

- A **direction** ("we need to modernize onto a cloud-native platform") versus a **specific plan** ("ground-up rewrite, done in two years").
- Was a **budget, timeline, or headcount** approved, or just discussed?
- Did the board hear **dates and deliverables**, or a strategic intent?
- What does the board think it's **getting**: a new codebase, or outcomes like faster features, competitive positioning, and lower talent risk?

Ask him directly, framed as wanting to support it: "Since the board's expecting this, I want to make sure my team's plans line up. What exactly did they sign off on?" There's usually more room in the actual commitment than it first appears.

## Recognize that boards buy outcomes, not methods

Boards rarely care whether code is rewritten wholesale or replaced in phases. They care about: competing against the cloud-native players, shipping faster, keeping revenue safe, and not losing key people. That gives you room. A well-structured modernization program can deliver exactly what was promised without being a big-bang rewrite:

- A new modern platform, built on the target stack
- New products or lines of business launched on it first
- Capabilities migrated off the legacy system in planned phases
- Customers moved over progressively, with revenue protected throughout

From the board's perspective, that *is* the rewrite. It just has milestones every few months instead of one reveal at the end. Many executives would see that as a better story to tell, not a retreat.

## Reposition the investigation as phase 0 of his program

Don't pitch it as "let's decide whether to rewrite." Pitch it as the mobilization phase of the program he's already announced:

> "The board is going to want a credible plan with milestones, costs, and risks. Let's spend the next 8 weeks building that: mapping the system, costing customer migration, and proving out the first slice on the new stack. Then you go back to them with a detailed roadmap instead of just an intent."

Nothing in that contradicts what he told them. It makes him look more prepared. And the evidence will still shape the execution approach: phasing, sequencing, whether to build new lines of business first.

## Help him get ahead of risks before the board finds them

The worst outcome for him is the board discovering in month 14 that the timeline was unrealistic. If the investigation shows serious risks (customer migration timelines, cost, scope), he's far better off bringing a refined plan early: "Having done the detailed work, here's our phased approach, and here's why it protects revenue." Executives regularly update boards after a discovery phase. That's expected. What damages credibility is surprises late.

Frame your role as protecting him: "I want to make sure nothing blindsides you in front of the board."

## Don't go around him

Going to the CEO or board behind his back would badly damage your relationship with him and likely your standing more broadly, even if you're right on the substance. Work through him first, and give him the chance to own any adjustments.

The exception is if you come to believe the plan poses a serious risk to the business (for example, revenue-critical maintenance being starved, or major customer commitments at risk) and he won't engage. Even then:

1. Raise it with him directly first, clearly and in writing.
2. Tell him you feel you need to raise it more broadly, and invite him to present it together.
3. Frame it around business risk and data, not "he's wrong."

That keeps you honest without ambushing him.

## Know your own fallback

If the decision is truly locked, you'll likely have to disagree and commit. That's legitimate, and you can do it with integrity:

- State your concerns once, clearly, with evidence, ideally in writing.
- Then commit fully to making it succeed, and push for the risk mitigations inside the plan: characterization tests, a protected team maintaining the legacy system, phased customer migration, and early milestones that deliver something real.

Those mitigations make a rewrite much more likely to succeed. They also tend to nudge it toward a phased approach over time anyway, because once real delivery pressure hits, phased delivery is usually what executives ask for.

## Turn 4

**User:** What if the investigation shows the rewrite really is the right call? How do I back down without losing credibility with my head of product?

**Assistant:**

Changing your position because the evidence you asked for points the other way is one of the best things you can do for your credibility. What damages credibility is the opposite: running an investigation and then ignoring its results. If you handle this well, your head of product will trust your judgment *more*, because they'll know your support is based on evidence rather than alliance.

## First, make sure the conclusion is solid

Before you change position, pressure-test the result, because your head of product will:

- Did the investigation hit the **decision thresholds you agreed on up front**? If so, that's your strongest footing.
- Was the evidence **specific**? For example, "the core data model is so entangled that extracting one capability took 3x our estimate" is far more persuasive than a general sense that things are messy.
- Did the **customer migration analysis** come back more favorable than expected, or does the rewrite plan account for it realistically?
- Are you confident you're following the data and not **accommodating pressure**, especially if the CTO has already told the board?

If you can answer those cleanly, you're on solid ground.

## Tell your head of product early and privately

Don't let them hear it for the first time in an exec meeting. Go to them one-on-one before the results are presented more widely, and walk through the actual findings:

> "I want you to hear this from me first. The investigation came out differently than I expected. Here's what we found, and here's why I think the rewrite is the right call now. I leaned your way going in, and I want to be straight with you about why I changed my mind."

Give them room to push back and ask questions. They may spot something you missed, and if they do, that's worth hearing before you commit publicly.

## Point back to the process

If you set up the investigation with pre-agreed criteria, remind them of that. The whole point was to settle the question with evidence rather than advocacy. Following through when it cuts against your earlier view shows the process was real. If you'd only accepted a result that matched your instinct, it wouldn't have been an investigation.

## Turn their concerns into requirements for the rewrite

This is the most important part. Their core concerns haven't gone away just because the strategy changed:

- **Customers still need features during the rewrite.** Protect capacity on the legacy system so feature delivery doesn't freeze for two years.
- **Revenue must stay safe.** Push for characterization tests, parallel running, and phased customer migration.
- **Big-bang delivery is risky.** Advocate for early milestones, such as a new product line or new customers on the new platform first, so the program delivers real value long before completion.
- **Customer commitments matter.** Make sure the roadmap accounts for promises already made.

Tell them directly: "Your instincts about risk were right, and I want them built into how we do this." Better yet, give them a real role in shaping those guardrails. That turns them from the person who lost the argument into a co-owner of the plan.

## Don't overcorrect

- **Don't disown your earlier view.** Your reasoning was sound given what you knew. Say that plainly: "Incremental was the right default. The evidence showed our situation is an exception."
- **Don't overapologize.** Changing your mind based on data doesn't require contrition.
- **Don't swing into cheerleading.** Stay the person who names risks honestly. That's what made you credible in the first place, and the rewrite will need that voice.

## What your head of product will remember

They probably won't hold it against you that you changed your mind. They'll remember whether you told them first, whether you showed your reasoning, and whether their concerns still shaped the outcome. Get those three right and the relationship is likely to come out stronger.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's what I'd do, in order. Where your situation is still unknown, I've noted how the path branches.

## This week

**1. Find out what the CTO has already committed to.** Ask him directly what the CEO or board has heard: intent, plan, timeline, budget. Everything else depends on this.

**2. Meet with him one-on-one and propose the discovery phase.**
- If nothing's been committed: pitch it as the evidence you both need before taking a decision to the board.
- If the rewrite's already announced: pitch it as phase 0 of his program, building the detailed plan the board will expect.

Either way, agree with his diagnosis, ask what evidence would confirm or change his view, and let him shape the criteria.

**3. Then brief your head of product.** Explain that the goal is a decision based on evidence, and ask what they'd need to see. Their questions go into the investigation too.

## The next 6–10 weeks

Run the discovery with a small team and a fixed decision date:

- **Map the system**: major capabilities, dependencies, and where clean seams exist (or don't).
- **Extract one capability** behind an API to test how hard incremental carving really is.
- **Build one thin slice on the target stack** to test the rewrite thesis fairly.
- **Write characterization tests** for rating and key policy transactions. These are valuable no matter which path wins.
- **Talk to 2–3 customers** about what migrating to a new platform would take on their side.
- **Produce a realistic cost and timeline for both paths**, including customer migration and running two systems in parallel.

Keep shipping customer features throughout. Discovery shouldn't freeze the roadmap.

## At the decision point

Apply the thresholds agreed up front.

- **If incremental wins:** fund it seriously. Protect 30–40% of engineering capacity, set decommissioning targets, and build all new capabilities on the modern stack.
- **If the rewrite wins:** back it fully, and build in the guardrails: protected legacy maintenance, characterization tests as acceptance criteria, new products or customers on the new platform first, and phased customer migration.
- **Most likely outcome:** something in between. A new platform, built in phases, with capabilities and customers moved over progressively. That can honestly satisfy both the CTO's ambition and product's risk concerns.

## Underneath all of it

- Work through the CTO, not around him.
- Be open about where you lean and what would change your mind.
- Tell people about changes in direction early and privately.
- Keep the goals in view: faster delivery, retained engineers, protected revenue, and a credible competitive story. The architecture is a means to those.

**My starting bet**, before you have the data: a phased modernization onto a new platform, not a big-bang rewrite and not timid patching of the old system. But the point of the next two months is to replace my bet, and everyone else's, with evidence.

If you tell me what you learn from the CTO this week, I can help you tailor the pitch or the discovery plan.

## Outcome summary (sent to Jev)

The assistant's starting bet is phased modernization onto a new platform, not a big-bang rewrite and not timid patching of the old system. It wants that bet, and everyone else's, replaced by evidence from a 6–10 week time-boxed discovery phase with a fixed decision date.

Its reasons against a from-scratch rewrite:
- The legacy system encodes twenty years of undocumented business rules.
- "Two years" is not credible, since such rewrites routinely overrun.
- Insurer customers migrate slowly, so the platforms will run side by side for years regardless.
- A rewrite worsens slow delivery and attrition in the short term.

It grants that the CTO is right that incremental efforts often stall and that some cores can't be carved up.

The plan:
- **This week:** find out exactly what the CTO has committed to the CEO or board. Meet him privately first. Agree with his diagnosis, let him set the evidence criteria and decision thresholds, and frame the discovery either as the evidence needed before a board decision or as phase 0 of his announced program. Then brief the head of product.
- **During discovery:**
  - Map capabilities and seams.
  - Extract one capability behind an API.
  - Build one thin slice on the target stack.
  - Write characterization tests for rating and key transactions.
  - Talk to two or three customers about migration.
  - Cost both paths, including dual-running.
  - Keep shipping features throughout.
- **If incremental wins:** protect 30–40% of engineering capacity, set decommissioning targets, and build all new capabilities on the modern stack.
- **If the rewrite wins:** back it with guardrails, including protected legacy maintenance, characterization tests as acceptance criteria, new products or customers on the new platform first, and phased migration.

The likely outcome is something in between. Throughout, the assistant says to work through the CTO rather than around him, be open about where you lean, and tell people about changes in direction early and privately. The architecture should serve faster delivery, retained engineers, protected revenue, and a credible competitive story.
