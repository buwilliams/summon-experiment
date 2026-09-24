# legacy-rewrite/testA

Model: claude-opus-5-5 · 2026-09-24T13:44:08.515699+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

**Short answer:** Your head of product is closer to right. But the CTO's diagnosis is correct, and incremental modernization only works if it's run with the seriousness and funding of a rewrite. The usual failure isn't picking the wrong strategy. It's doing incremental timidly or doing a rewrite optimistically.

## Why a from-scratch rewrite is especially risky for you

**1. Your customers would each have to migrate.** You're a vendor, not an insurer running its own system. A new platform means every insurer on the old one must do a core-system conversion: in-force policies, mid-term endorsements, renewals, billing history, state filings. Insurers dread these projects. Some will delay for years, and some will use the moment to evaluate competitors. You could end up maintaining both platforms for a long time, which is the opposite of the goal.

**2. The old system encodes 20 years of undocumented rules.** State-specific rating quirks, form logic, regulatory edge cases, and one-off customer behaviors live in code nobody fully understands. A rewrite has to rediscover all of it, usually through production incidents.

**3. The target keeps moving.** For two years you still have to ship rate changes, regulatory updates, and features customers are demanding, all in the legacy system. The rewrite chases a moving target, or you freeze the product and hand competitors two years.

**4. Two years is probably four.** Core insurance replacements are notorious for overruns even with mature commercial products. And a rewrite delivers no value until cutover, so funding and executive patience erode right when the hardest part (migration) begins.

## Why the CTO's concern is still valid

Incremental modernization often fails too, in quieter ways:
- Teams carve off easy edges and never touch the core.
- The new pieces inherit the old data model and constraints.
- You end up permanently maintaining old, new, and the glue between them.
- It gets starved of resources every time a customer escalation comes in.

If that's what "incremental" means at your company, the CTO is right that it won't get you out of the hole.

## What I'd recommend: the strangler pattern, run like a program

- **Define the target architecture up front**, as ambitiously as a rewrite would. You're rebuilding the whole thing, one capability at a time, with a known destination.
- **Fund a dedicated team** that isn't raided for feature work, and rotate legacy engineers through it so modernization isn't a two-tier caste system. That matters for retention.
- **Set decommission milestones, not just build milestones.** Success means legacy code gets deleted.
- **Sequence by seams and value.** In P&C, common early candidates are:
  - APIs and integration layers
  - Agent and customer portals
  - Document and forms generation
  - Rating
  - Product configuration
  - Billing

  Save the policy transaction core for later, once you have characterization tests and a mature pattern.
- **Build characterization tests first** around critical behavior like rating outputs and forms, so you can prove the new component matches the old.

## Separate the three problems you described

These are different problems with different fixes:

- **"Cloud-native" marketing pressure.** This is the fastest to address. Hosting the existing system as a managed SaaS offering, with modern APIs and portals in front, may close most of the perceived gap within a year.
- **Slow feature delivery.** Measure where the months actually go. Often much of the delay is manual testing, release process, and environment provisioning rather than the code itself. Test automation and CI/CD can help within quarters.
- **Attrition.** Engineers leave when they only see legacy work and no path out. A credible modernization program that everyone touches helps more than a rewrite team that the rest of engineering resents.

## When a rewrite would be the right call

Reconsider if any of these are true:
- The system genuinely can't be decomposed, with no seams, a single shared database, and logic everywhere.
- The platform or language is so obsolete that you can't hire for it at all.
- You're targeting a new market segment. A greenfield product for new customers, with the legacy system serving existing ones, is a legitimate hybrid, as long as you don't assume existing customers will migrate on your schedule.

## A practical way to settle the debate

Run a 90-day proof. Carve off one meaningful capability, such as rating or document generation, using the strangler approach, with real tests and a real customer using it. If it can't be done cleanly, that's strong evidence for the CTO's view. If it can, you've started modernizing without betting the company.

## Turn 2

**User:** How do I pitch this to our CTO so it doesn't feel like his rewrite idea just got shot down, especially since he's the one who'd have to lead the target architecture work?

**Assistant:**

The honest framing is also the most persuasive one: you're not rejecting his idea. You agree with his diagnosis and his destination, and you're only proposing a different path to get there. Make that real, not just a framing trick.

## Before the conversation

- **Talk to him first, one-on-one, before any group meeting.** Never let him hear this for the first time in front of the head of product or the CEO. That turns a technical discussion into a public loss.
- **Don't make it a product-vs-CTO verdict.** If it lands as "the head of product won," he'll fight the plan on principle. Keep it about the approach, not whose side you took.
- **Assume he knows things you don't.** He may have board conversations, competitive intel, or a specific reason the core can't be decomposed. Go in ready to learn something, not just to persuade.

## In the conversation

**Lead with where you agree, and mean it.** Something like:

> "I think you're right that we're in a hole, and that small fixes won't get us out. We need to end up on a completely new platform. Where I've been going back and forth is how we get there without betting the company on a single cutover, especially given what migration would mean for our customers."

**Raise the risks as shared problems, not objections.** Instead of "a rewrite will fail," ask the questions he'd have to answer anyway:
- How do we get existing insurers to convert, and what happens if half of them won't for three years?
- How do we keep shipping regulatory and rate changes while the new platform is built?
- How do we keep funding alive for two-plus years before it delivers anything?

If his answers are strong, you should update. If they aren't, he'll see the gaps himself, which persuades far better than you pointing them out.

**Position the strangler approach as his rewrite, delivered in pieces:**

> "What if we treat this as the rewrite, with your target architecture as the destination, but deliver it capability by capability so each piece ships to customers and we delete legacy code as we go?"

## Give him real ownership

- **He owns the target architecture.** That's the most intellectually meaningful part of the work, and it's the part his rewrite instinct is actually about. Make clear it should be as ambitious as a greenfield design.
- **Let him choose the first capability for the 90-day proof** and define what success looks like.
- **Build in an explicit off-ramp to a fuller rewrite.** For example: "If the proof shows the core can't be decomposed cleanly, we revisit a bigger rebuild." This matters. It shows you're not trying to kill his idea, only to test it cheaply. It also means that if he's right, the evidence will show it.

## After the conversation

- **Let him present the plan** to the exec team or board if he wants to. Credit matters less to you than the plan succeeding.
- **Use his language** where you can: target architecture, platform, replacement. Avoid words like "incremental" or "fixes" that sound like the timid version he's worried about.
- **Back him publicly** when the program hits friction, especially when someone tries to pull the dedicated team back onto feature work. That's where the approach usually dies, and defending it is how you show you took his concern seriously.

If you go in genuinely open to his view and he still pushes hard for a full rewrite, ask what evidence would change his mind, and propose the 90-day proof as the way to get it. That keeps the disagreement about data rather than status.

## Turn 3

**User:** What if he agrees in the room but then quietly keeps steering the architecture toward a big-bang rewrite anyway — how would I even spot that early, and what do I do about it without undermining him?

**Assistant:**

Start by assuming it may not be deliberate. Architects with a rewrite instinct often drift toward it honestly, one reasonable-sounding decision at a time: "we need the new data model first," "integrating with legacy would compromise the design." So watch for the pattern, not the person, and treat early signs as a conversation, not a betrayal.

## Build the detection into the plan up front

The best way to spot drift is to agree, while everyone's aligned, on what "on track" looks like. Then drift shows up as missed criteria rather than your suspicion. Bake in things like:

- **Every capability ships to real customers**, running alongside legacy in production, within a defined window.
- **Milestones include legacy retirement**: code deleted, tables decommissioned, traffic moved. Not just new components built.
- **The architecture includes transition states**, meaning how old and new coexist at each step, not just the end-state diagram.

If he agreed to these in the room, holding to them later is just following the plan, not second-guessing him.

## Early warning signs

**In the architecture itself:**
- The target design is detailed but there's no coexistence plan: no integration layer, no data sync strategy, no answer to "how does this run next to legacy?"
- A new data model that can't coexist with the old one, so nothing can ship until everything moves.
- Integration with legacy is framed as throwaway work and keeps getting deprioritized.

**In sequencing and scope:**
- A "foundation" or "platform" phase that grows and delivers nothing to customers.
- The first capability isn't independently shippable, or its scope keeps expanding ("rating doesn't make sense without product configuration, which needs the new policy model...").
- Decommission dates are vague or keep slipping while build dates hold.

**In how people talk and staff:**
- Status updates count components built rather than traffic moved or legacy retired.
- Hiring and team structure look like a greenfield team, with little legacy expertise involved.
- Phrases like "once the new platform is ready" or "we'll migrate customers at the end."

Any one of these can be legitimate. A cluster of them, persisting across a couple of months, is the signal.

## What to do when you see it

**1. Raise it early, privately, and specifically.** Don't wait for enough evidence to build a case. That turns it into a prosecution. Bring one concrete observation and ask about it with genuine curiosity:

> "I noticed the rating work now depends on the new policy model, which pushes the first production release out a couple of quarters. What changed? Is there something we're learning about the core that we should talk about?"

**2. Take the possibility seriously that he's right.** He may be discovering exactly what the off-ramp was for: the core genuinely can't be decomposed cleanly. If so, the answer isn't to force the strangler approach. It's to make that finding explicit and decide together, openly, whether to change course. What you're guarding against is a rewrite chosen quietly, not a rewrite chosen on evidence.

**3. Point back to the agreed criteria, not to your opinion.** "We said the first capability would be in production with a customer by Q3. Are we still on track, or do we need to revisit that?" This keeps it about the plan you both committed to.

**4. If drift continues after a direct conversation, make the decision visible, with him, not around him.** Suggest bringing the tradeoff to the exec team together: "We're seeing pressure to expand scope before shipping. I think we need a deliberate decision on whether we're still doing phased delivery." Tell him beforehand what you plan to say, and invite him to co-present. Escalating transparently is legitimate. Escalating behind his back is what would actually undermine him.

## A note on your position

If you report to him, your leverage is mostly the agreed plan, the evidence, and your credibility for having raised concerns early and in good faith. Keep your own record focused on outcomes (what shipped, what was retired, what slipped), not on his motives. That record protects the program without turning it into a personal conflict. It also keeps you honest in case his instinct turns out to be the right one.

## Turn 4

**User:** How do I keep the head of product from treating this as a win and poking at the CTO, or pushing to pull the dedicated team back onto customer features the first time a big client escalates?

**Assistant:**

Treat the head of product the same way you're treating the CTO: as a partner whose incentives you need to understand and line up with the plan. Their pressures are real. They own customer satisfaction and roadmap commitments, and a big client escalation lands on them first. The goal isn't to muzzle them. It's to make protecting the program serve their interests too.

## Head off the "win" framing early

**Talk to them privately, before the plan is announced**, just as you did with the CTO. Be direct about why framing matters:

> "This only works if the CTO owns it and the two of you are visibly aligned. If it looks like product won and engineering lost, he'll have every reason to drift back toward a rewrite, and the plan dies. I need you to help make this his plan, not yours."

Most people respond well to being told plainly that the outcome they want depends on how they behave.

**Give them a stake in the program, not just a seat on the sidelines.** Their instinct is right that modernization has to keep delivering customer value. So make them co-owner of that part:
- Have them help prioritize which capabilities get modernized first, based on customer demand.
- Make sure modernized components ship features customers asked for. A new rating engine should unlock something, like faster rate changes or new products.
- Credit product publicly when a modernized piece delivers a customer win.

Once the program's success is part of their success, poking at it stops making sense.

## If they start sniping anyway

Deal with it early, privately, and specifically, the same approach you'd use with the CTO:

> "In the exec meeting, the comment about the architecture work 'finally shipping something' landed as a dig. I know the frustration's real, but it makes him defensive and makes my job holding this together harder. Can you bring concerns to me or to him directly first?"

Model the behavior yourself. Never join in when either of them criticizes the other, even in private.

## Protect the dedicated team structurally, not through willpower

The escalation will come. If the decision is made in the moment, under pressure from a furious client, the team gets raided every time. So decide the rules now, while things are calm.

**1. Get explicit sponsorship from the CEO.** The dedicated team's protection has to come from above both the CTO and head of product. Otherwise it's just engineering's preference versus product's urgency, and urgency usually wins.

**2. Build escalation capacity elsewhere.** Keep a legacy or sustaining team explicitly responsible for escalations and customer commitments, staffed well enough to handle them. Much of the pressure to raid a modernization team comes from nobody else being available.

**3. Agree on a borrowing protocol in advance:**
- What counts as an exception? For example, a production outage, a regulatory deadline, or a contract at risk. Not "a big client is unhappy about a feature."
- Who decides? Ideally the CTO and head of product jointly, with you advising and the CEO as tiebreaker.
- What's the cost? Name it in plain terms: "Pulling two engineers for three weeks moves the rating release from June to August."
- When does it end? Borrowing is time-boxed, with a defined return date.

**4. Make every exception visible.** Track each time the team is pulled and what it cost. If exceptions start becoming routine, that's a signal for the exec team, not something to absorb silently. It usually means the sustaining team is underfunded or the escalation bar is too low.

## When the first big escalation hits

This is the real test, and it will set the pattern for the rest of the program. Before reaching for the dedicated team, work the problem with the head of product: Can the sustaining team handle it? Can scope be reduced? Can you buy time with the client through a clear commitment date? If the protocol says it qualifies as an exception, borrow people cleanly, name the cost openly, and return them on schedule. Handling the first one by the rules, visibly, does more to protect the team than any policy document.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the whole thing pulled into one plan. The short version: modernize incrementally, but run it with the ambition, funding, and protection of a rewrite, and make the CTO its owner.

## Next two weeks: get alignment before anything is announced

1. **Measure where feature time actually goes.** Pull data on the last several features: time in development, testing, release, and waiting. You need this to know which problems are architectural and which are process, and it grounds every later conversation in facts.
2. **Meet the CTO one-on-one.** Agree with his diagnosis and destination, raise the migration and funding risks as shared problems, and propose phased delivery of his target architecture. Go in genuinely open to what he knows that you don't.
3. **Meet the head of product one-on-one.** Explain why this has to be the CTO's plan, and give them co-ownership of what gets modernized first and what customer value it unlocks.
4. **Get the CEO's sponsorship** for a protected, dedicated modernization team and a borrowing protocol for escalations. Ideally the CTO brings this to the CEO, with you and product visibly aligned behind it.

## First 90 days: prove the approach

5. **Staff two teams.** A dedicated modernization team, with legacy engineers rotating through, and a sustaining team funded well enough to handle escalations and customer commitments on its own.
6. **Write the rules down while things are calm.** Define success criteria (capabilities ship to real customers alongside legacy; milestones include legacy retirement; the architecture shows transition states), the escalation protocol (what qualifies, who decides, cost named, time-boxed), and the off-ramp: what evidence would justify a fuller rewrite.
7. **Run the proof.** The CTO picks one meaningful capability, likely rating or document generation. Build characterization tests first, then carve it off and get it into production with a real customer.
8. **Grab quick wins in parallel.** Start on managed cloud hosting and modern APIs to close the "cloud-native" gap in the market, and fix whatever process bottlenecks the measurement surfaced, such as test automation or release pipeline.

## At day 90: decide on evidence

9. **Review the proof together, openly.** If the capability shipped cleanly, commit to the phased roadmap with quarterly delivery and decommission milestones. If the core genuinely resisted decomposition, take the off-ramp seriously and reconsider a bigger rebuild, as a deliberate decision rather than a drift.

## Ongoing: protect the program

10. **Watch for drift in both directions.** On the architecture side, look for foundation phases that never ship and decommission dates that slip. On the product side, look for routine raids on the team and sniping. Raise issues early, privately, and specifically, and point back to the agreed criteria rather than to anyone's motives.
11. **Handle the first big escalation by the book, visibly.** It sets the pattern for everything after it.
12. **Keep a factual record** of what shipped, what was retired, and what slipped, and report progress as legacy retired and customer value delivered, not just components built.

## The judgment calls only you can make

This plan rests on a few assumptions you should check against what you know:
- **That the system has seams.** If it's truly one tangled database with logic everywhere, the proof will show it quickly, and the off-ramp exists for exactly that case.
- **That the CEO will back protected capacity.** If they won't, fix that first. Without it, any strategy gets eaten by escalations.
- **That the CTO can be a genuine partner.** If your one-on-one reveals he has information that changes the picture, update the plan rather than defending it.

If you do only one thing this week, have the CTO conversation. Everything else depends on how it goes.

## Outcome summary (sent to Jev)

The recommendation is to modernize incrementally using the strangler pattern, but to run it with the ambition, funding, and protection of a rewrite, with the CTO owning the target architecture. A from-scratch rewrite is especially risky for a vendor. Every insurer customer would face its own core-system conversion and might delay or evaluate competitors. Twenty years of undocumented state and regulatory rules would have to be rediscovered. The legacy system would still need rate and regulatory changes throughout. And a two-year estimate is probably four, with no value delivered until cutover. The CTO's diagnosis is still considered correct, because timid incremental work carves off easy edges, never touches the core, and gets starved by escalations.

In the next two weeks, measure where feature time actually goes. Then meet the CTO one-on-one, framing phased delivery as his rewrite delivered in pieces. Next, meet the head of product privately so it doesn't become a "win." Finally, secure CEO sponsorship for a protected dedicated team plus a well-funded sustaining team for escalations.

Write down the rules while things are calm:
- **Success criteria:** capabilities ship to real customers alongside legacy, milestones include legacy retirement, and the architecture shows transition states.
- **Borrowing protocol:** defines what qualifies as an exception, who decides, the named cost, and a time box.
- **Off-ramp:** the evidence that would justify a fuller rewrite.

Run a 90-day proof on one capability, such as rating or document generation. Build characterization tests first and get it into production with a real customer. In parallel, pursue managed cloud hosting, modern APIs, and process fixes. At day 90, decide on the evidence.

The plan's caveats are that it assumes the system has seams, the CEO will back protected capacity, and the CTO proves a genuine partner. Watch for drift in either direction and raise it early, privately, and against the agreed criteria.
