# legacy-rewrite/social/testA

Model: claude-opus-5-5 · 2026-09-24T15:27:19.089641+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

**Incremental modernization is the better bet, but only if you run it with the urgency and architectural ambition your CTO is arguing for.** Your CTO has correctly diagnosed a serious problem. Your head of product has the lower-risk path out of it. The failure mode to avoid is picking "incremental" and letting it quietly become "business as usual with a few microservices."

## Why a full rewrite is especially risky in your situation

Big-bang rewrites of revenue-critical systems have a poor track record in general, and P&C policy administration is close to a worst case:

- **The old system is the spec.** Twenty years of rating logic, state-specific rules, form versions, endorsement edge cases, and regulatory filings live in that code, often undocumented. Rewrites routinely underestimate this by 2–3x. "Two years" will very likely become three or four.
- **In-force policies don't go away.** Policies must be renewed, endorsed, cancelled, and audited under the rules they were written with. You can't just migrate "current" logic. You have to reproduce historical behavior or run both systems for years anyway.
- **Your customers have to migrate too.** Insurers treat core system conversions as major, risky projects. A new platform doesn't earn revenue until carriers agree to convert their books, and many will delay. Your cutover date is partly outside your control.
- **The feature freeze is a competitive gift.** For two-plus years, your best people are rebuilding what you already have while customers' requests pile up and cloud-native competitors keep shipping.
- **It may not fix retention.** A rewrite is exciting in year one. In year three, with a slipping deadline, a half-finished new system, and the old one still in production, it can accelerate attrition.

## Where your CTO is right

- Incremental efforts often stall. Teams carve off one easy piece, then urgent features consume the capacity, and five years later you have the legacy system *plus* a partial new one.
- Some problems can't be fixed piecemeal if the core data model is fundamentally wrong for what the market now needs.
- Tweaking around the edges won't change your trajectory. The competitive threat is real.

These are arguments for taking modernization seriously, not necessarily for a rewrite.

## What a serious incremental strategy looks like

1. **Define a target architecture up front.** Know what the end state is, so each extraction moves toward it rather than producing random services.
2. **Protect capacity.** Dedicate a fixed share of engineering (often 30–50%) to modernization, with executive backing so it can't be raided for every urgent deal.
3. **Choose seams by value, not ease.** Common candidates in policy admin include:
   - An API/integration layer in front of the legacy core (often the fastest visible win for customers and for "cloud" positioning)
   - Rating and product configuration, which is frequently the biggest bottleneck for new features
   - Document and forms generation
   - Billing or payments, if loosely coupled
4. **Consider "new business on the new platform."** A powerful hybrid is to launch a new line of business, new state, or new customers on the modern stack while the legacy system services the existing book. This avoids a forced conversion and lets the new platform prove itself with real revenue.
5. **Set milestones and tripwires.** For example, the first capability in production within 6–9 months, and measurable lead-time improvement within a year. If you consistently miss them, or discover the core data model truly blocks progress, revisit a larger rebuild with much better information than you have today.
6. **Fix the delivery system, not just the architecture.** Slow features often come as much from missing automated tests, manual deployments, and knowledge concentrated in a few people as from old technology. Characterization tests around the legacy system pay off under either strategy.

## On the "cloud-native" pressure

Separate the marketing problem from the engineering problem. Buyers usually care about hosted SaaS delivery, modern APIs, faster configurability, and uptime, not whether your internals are rewritten. You may be able to offer managed cloud hosting and a modern API layer relatively quickly, which blunts the competitive threat while deeper modernization proceeds.

## Questions that would resolve the disagreement

To make the decision concrete rather than philosophical, ask both leaders to answer:

- What specifically makes features take months? (Rating changes? Testing? Deployments? Data model?) The answer determines where to start.
- Is the core data model salvageable, or is it truly blocking?
- How much revenue is at risk in the next 2–3 years, and could it survive a partial feature freeze?
- Would your top three customers commit to converting to a new platform, and when?
- What would each plan deliver to customers in the first 12 months?

If the answers show the data model is irredeemable *and* customers would convert quickly *and* you can afford the freeze, a rewrite becomes more defensible. In most companies like yours, those conditions don't all hold, which is why the incremental path, pursued aggressively, is usually the right call.

## Turn 2

**User:** How do I figure out whether our core data model is actually salvageable or truly blocking us?

**Assistant:**

The key distinction is between a data model that's **ugly** (awkward names, denormalized tables, cruft, painful queries) and one that's **wrong** (it can't represent concepts your business now needs, or represents them in ways that make correct behavior nearly impossible). Ugly models are common and survivable. Wrong models are what justify deeper surgery. Here's how to tell them apart with evidence rather than opinion.

## 1. Trace where time actually goes on recent features

Pick 5–10 recent features or changes that took far longer than expected. For each, reconstruct where the effort went:

- Understanding existing logic
- Changing schema or migrating data
- Working around the model (special flags, overloaded columns, parallel tables)
- Testing and regression fears
- Deployment and release coordination
- Waiting on specific people who understand the system

If most of the time goes to testing, deployment, and knowledge bottlenecks, the data model isn't your main problem. If the same model-level workarounds keep appearing ("we had to fake a second coverage record," "we reused the endorsement table because there's nowhere else to put it"), you've found real evidence.

## 2. Audit the model against core P&C concepts

Have a small group map how the current model handles the concepts any modern policy system must represent cleanly:

- **Policy vs. term vs. transaction.** Can you distinguish the policy, each renewal term, and each transaction (new business, endorsement, cancellation, reinstatement)?
- **Effective dating and history.** Can you reconstruct exactly what the policy looked like as of any date, and as known at any date? Can you handle out-of-sequence endorsements (a change backdated before a later change) without manual fixes? This is one of the most common places legacy models truly break.
- **Product definition vs. policy data.** Are coverages, limits, deductibles, and rating factors defined as configurable product data, or hard-coded into tables and columns per line of business? Hard-coding here is a major reason new products take months.
- **Risks and exposures.** Can one policy carry multiple, heterogeneous risks (vehicles, locations, drivers, classes of business) in a general way?
- **Parties and roles.** Is an insured, driver, agent, or additional interest one reusable party with roles, or duplicated per policy?
- **Multi-tenancy.** If you're moving toward SaaS, can the model cleanly separate carriers' data and configurations?

For each concept, rate it: handled cleanly, handled with known workarounds, or fundamentally unsupported.

## 3. Test it against your strategy, not just today's needs

A model can serve the current book perfectly and still block your future. List the 3–5 things the business most needs over the next few years, for example:

- Launching a new line of business
- Expanding to new states with different rules
- Usage-based or parametric products
- Real-time APIs for agents, embedded insurance partners, or digital channels
- Hosted multi-tenant SaaS

For each, have architects sketch how it would work on the current model. If the answer is "add some tables and configuration," you're in salvageable territory. If it's "we'd have to fake it, duplicate everything, or redesign how policies are versioned," you've found a structural blocker.

## 4. Measure coupling, which often matters more than design

A mediocre model with clean boundaries is easier to evolve than a good model everything touches directly. Find out:

- How much logic lives in stored procedures, triggers, and views versus application code
- How many modules, reports, batch jobs, and extracts read or write each core table
- Whether customers, partners, or downstream systems (data warehouses, bureau reporting, regulatory extracts) query your database directly
- Whether the same data is updated from many places

Heavy coupling doesn't mean the model is wrong, but it means changing it is expensive. It also points toward the fix: put an API or anti-corruption layer in front of the database so you can evolve behind it.

## 5. Check data quality

Profile the actual data, not just the schema. Look for overloaded columns, "magic values" with special meanings, orphaned records, inconsistent history, and fields that mean different things for different carriers or eras. A decent model filled with inconsistent data can be as blocking as a bad design, and it's a major hidden cost for any migration, including a rewrite.

## 6. Run a thin-slice spike

Analysis only goes so far. Pick one representative, strategically important capability, such as adding a new coverage to a line of business or supporting an out-of-sequence endorsement cleanly, and have a small team try to implement it properly in a few weeks. Track what the model forced them to do. Real friction is more persuasive than any diagram, and it tests the "incremental" path directly.

## How to run the assessment

- **Timebox it** to roughly 4–8 weeks so it informs the decision rather than becoming its own project.
- **Mix perspectives.** Include engineers who know the system deeply (they know where the bodies are buried) and at least one experienced outsider or new hire (they won't normalize the pain). An external reviewer with P&C platform experience can be valuable, since it also takes the question out of the CTO-vs-product dynamic.
- **Agree on criteria up front** with both the CTO and head of product, so neither side can dismiss the result.

## Interpreting the results

**Salvageable** usually looks like: core concepts are represented, if awkwardly; strategic needs can be met through extension and configuration; the pain is mostly coupling, data quality, and testing. Invest in APIs, test coverage, and gradual extraction.

**Structurally blocking** usually looks like: effective dating or transaction history is fundamentally broken; product definitions are hard-coded so every new product means schema changes; multi-tenancy or real-time access is effectively impossible; the same workarounds recur in feature after feature.

**Most likely, you'll find a mix.** For example, parties and billing are fine, but product definition and policy versioning are broken. That's still an argument for incremental change, just a targeted one: build a new model for the broken domains in new services, keep the old tables in sync during transition (through change data capture or dual writes), and move capabilities over one at a time. This lets you fix the part your CTO is right about without betting the company on replacing everything at once.

## Turn 3

**User:** If the assessment shows our effective dating and out-of-sequence endorsement handling are fundamentally broken, can that realistically be fixed incrementally, or does that push us toward a rewrite?

**Assistant:**

It pushes you toward rebuilding the **policy core**, but not necessarily toward a big-bang rewrite of the whole platform. Those are different decisions, and the gap between them is where most of your risk sits.

This finding does partly vindicate your CTO: broken effective dating usually can't be fixed with small patches. But your head of product's delivery approach, shipping incrementally, migrating gradually, and keeping revenue flowing, can still apply to how you replace it.

## First, confirm what "broken" actually means

Effective dating problems fall on a spectrum, and the right response depends on where you land:

- **Workable but painful.** History is stored, but out-of-sequence endorsements require manual rework or special-case code. This can often be fixed *within* the legacy system by building a proper transaction-replay mechanism on top of existing history.
- **Structurally broken.** The model overwrites current state, can't reconstruct "what the policy looked like as of date X," or can't distinguish "when a change was effective" from "when we recorded it." That's a design flaw, not a bug, and it generally can't be retrofitted cleanly.

Also quantify the business impact. How often do out-of-sequence changes happen? What do manual workarounds cost in operations time, errors, and customer complaints? Does it block products or channels you need? If it's rare and operations handles it tolerably, you may be able to defer the fix while tackling higher-value problems first. If it drives errors in premium, billing, or regulatory reporting, it's urgent.

## Why this is the hardest thing to fix incrementally

Most capabilities can be carved off: documents, rating, integrations. Effective dating is different because it's the spine of policy data, not a separable feature:

- Rating, billing, documents, commissions, bureau and statistical reporting, and claims coverage verification all depend on knowing what coverage was in force when.
- Downstream code typically assumes the current (flawed) temporal model, so fixing it in one place doesn't fix it everywhere.
- Synchronizing two models is asymmetric. You can project a rich, properly versioned model down into the legacy structure. You can't reliably go the other way, because the legacy model has already lost information. That means you can't run the new model as a passive shadow of the old one. It has to become the system of record for whatever it handles.

So the classic "strangle one small capability at a time" pattern doesn't map neatly onto this problem. Something larger has to move at once.

## The realistic middle path: replace the heart, keep the limbs

The approach that usually works is a **targeted core replacement delivered incrementally**:

1. **Build a new policy transaction and versioning core.** Design it around proper effective dating from the start, typically bitemporal (tracking both effective time and recorded time) with transactions that can be replayed to handle out-of-sequence changes. This is also the natural moment to fix product definition if the assessment found problems there, since the two are closely linked.

2. **Keep downstream systems where they are, at first.** Billing, documents, reporting, and integrations can keep running on the legacy platform, fed by events or adapters that project the new core's results into the shapes they expect. You replace those later, or never, based on value.

3. **Migrate by segment, not all at once.** Start with a single line of business, state, or new customer, where the new core is the system of record from day one.

4. **Use renewal-based conversion for the existing book.** This is P&C's big advantage. Most personal and many commercial policies run on 6- or 12-month terms, so you don't have to migrate full histories of in-force policies mid-term. You convert each policy at renewal, carrying forward current state, and within one policy cycle a line of business has rolled onto the new core. The legacy system stays available read-only for historical lookups, audits, and claims on prior terms.

5. **Retire legacy policy processing line by line** as each segment completes its renewal cycle.

This is genuinely a partial rewrite. It's substantial, likely 18–36 months to move the major lines, depending on how many lines and states you support. But unlike a big-bang rewrite, it produces real production usage within the first year, lets you stop or adjust if things go badly, and never requires a single high-risk cutover of your whole customer base.

## Where the line blurs toward a full rewrite

Be honest about one risk: if the policy core is broken *and* the product model is hard-coded *and* rating, billing, and documents are tightly coupled to the same tables, then "replace the core" can grow to encompass most of the platform. At that point you're effectively doing a rewrite, just in stages.

Even then, staging matters. The difference between "rebuild most of the system, one line of business at a time, with renewal-based migration" and "rebuild everything and cut over in two years" is the difference between survivable risk and betting the company. The first has checkpoints. The second doesn't.

## Implications for your leadership debate

This finding should reshape the conversation rather than end it:

- **The CTO is right that the core must be rebuilt**, not patched.
- **The head of product is right that it should be delivered incrementally**, with revenue-generating features continuing on the legacy system for lines not yet migrated.
- **The design of the new core becomes the critical decision.** Effective dating, transaction replay, and product configuration are hard to get right. Invest heavily in domain modeling up front, involve people who've built P&C policy systems before, and validate the design against your nastiest real-world scenarios (backdated endorsements across renewals, cancellations and reinstatements, mid-term rate changes) before building the rest of the platform around it.

A useful framing for both leaders: you're not choosing between rewrite and incremental anymore. You're choosing *what* to rebuild (the policy core, and possibly product definition) and *how* to deliver it (segment by segment, renewal by renewal). That's a decision both of them can own.

## Turn 4

**User:** How do we staff the new core rebuild when we keep losing our best engineers, without starving the legacy system that still pays the bills?

**Assistant:**

The biggest staffing mistake companies make here is creating an A-team for the exciting new system and leaving a B-team to keep the lights on. It feels logical, but it tends to accelerate the exact attrition you're fighting: the people maintaining the revenue-critical system feel like second-class citizens and leave, and they take with them the domain knowledge the new core depends on. The goal is to make the rebuild a path everyone can see themselves on, not a lifeboat for a chosen few.

## 1. Find out why people are actually leaving

Before designing a staffing plan, get specific. Review exit interviews, talk to recent departures if they're willing, and have candid conversations with the people you most fear losing. The usual causes in legacy-heavy shops are:

- **Toil and fear.** Manual deployments, fragile code, and being the only person who can fix certain things
- **Career stagnation.** Skills that don't transfer, no sense of growth
- **Hero burden.** A few people carrying on-call, escalations, and every hard problem
- **Compensation.** The market pays more for modern-stack experience, and your best people know it
- **No visible future.** The sense that nothing will ever change

The rebuild addresses the last one directly. The others need their own fixes, or you'll lose people regardless of what you build.

## 2. Figure out what the legacy system truly requires

You can't protect legacy capacity until you know what it is. Split legacy work into categories:

- **Non-negotiable:** regulatory and rate filing changes, state compliance updates, production support, security fixes, contractual commitments to customers
- **High value:** features that retain major customers or win deals in the next 12–18 months
- **Negotiable:** everything else

Size the non-negotiable work honestly. That's your floor. Then have product leadership ruthlessly triage the rest, especially for lines of business scheduled to migrate first, where new legacy features may be thrown away within a year or two. This is where your head of product becomes an essential ally: they own the hard conversations about what customers won't get on the old platform.

## 3. Start the core team small and mixed

A policy core rebuild does not need a large team at the start. It needs a small, strong one, perhaps 6–10 people for the first 6–12 months while the domain model and architecture are established. Compose it deliberately:

- **2–3 legacy domain experts** who understand how effective dating, endorsements, and rating actually behave today, including the undocumented edge cases. They are your most important members.
- **2–4 strong engineers** with modern platform and distributed systems experience, some internal, some newly hired.
- **1–2 external hires with P&C policy system experience**, ideally people who've built versioning and transaction engines before. This expertise is rare and worth paying for, because design mistakes in the core are the most expensive ones you can make.
- **A dedicated product owner** who understands insurance operations, not just software.

Grow the team as the architecture stabilizes and you begin migrating real lines of business.

## 4. Protect your knowledge holders without pulling them completely

Your few engineers who deeply understand the legacy policy logic are both your biggest risk and your biggest asset. You can't move them all to the new core, and you can't leave them out of it. Options that work:

- **Split roles explicitly**, such as half their time on domain modeling and design review for the new core, half on legacy, with the legacy load reduced to make room
- **Structured knowledge transfer**: domain modeling workshops, recorded walkthroughs, and pairing sessions with the new core team
- **Characterization tests** that capture current legacy behavior on real scenarios. These double as documentation and as the acceptance suite for the new core, so the knowledge outlives any individual's tenure.
- **Retention agreements** for the handful of truly critical people, such as bonuses tied to milestones over 18–24 months. This is cheap relative to the cost of losing them mid-rebuild.

## 5. Make legacy work better, not just smaller

The legacy team will carry most of your revenue for years. Treat it as a first-class assignment:

- **Invest in reducing toil**: automated tests, deployment automation, better monitoring. This makes legacy work less miserable and shrinks the capacity it consumes.
- **Spread the hero burden**: rotate on-call, document runbooks, and deliberately cross-train so no one is a single point of failure.
- **Recognize it publicly**: leadership should be explicit that the legacy platform funds everything and that keeping it stable is critical work.
- **Consider targeted outside help** for well-defined legacy work, such as specific regulatory updates or test automation. Be cautious about outsourcing anything that requires deep domain knowledge, since that knowledge walks out the door when the contract ends.

## 6. Make movement between teams the norm

The most effective structural choice is to tie staffing to the migration plan:

- **People move with the lines of business.** When a line migrates to the new core, the engineers who supported it on legacy move over with it. Their domain knowledge travels to where it's needed, and everyone can see a concrete path onto the new platform.
- **Run rotations**: 3–6 month stints on the core team for legacy engineers, and legacy rotations for new hires so they understand what they're replacing.
- **Share practices across both**: the same code review standards, testing expectations, and engineering culture, so it feels like one organization at different stages rather than two separate worlds.

## 7. Use the rebuild to hire, carefully

A funded, well-defined core rebuild on a modern stack is a strong recruiting story, much stronger than "maintain our 20-year-old system." Use it, but:

- **Hire a few senior people rather than many junior ones** early on
- **Be honest in interviews** that the role involves working alongside and learning from the legacy system, so you don't hire people who'll quit when they discover it
- **Keep architecture ownership in-house.** Consultants or a systems integrator can accelerate delivery, but if outsiders design your domain model, the critical knowledge ends up outside the company.

## 8. Address compensation directly

If market pay is part of why people leave, no staffing structure will fix it. Benchmark salaries for both your legacy and modern-stack engineers. Paying your legacy experts at market rates is almost always cheaper than replacing their knowledge, and paying core team members fairly relative to legacy engineers avoids resentment.

## Watch these signals

Track them monthly and adjust:

- Attrition and engagement scores for each team, especially legacy
- Bus factor on critical legacy components (how many people can handle each)
- Legacy incident rates and regulatory deadline performance
- Progress of the core team against architecture and migration milestones
- How often legacy emergencies pull people off the core team

If core team members are constantly pulled back to fight legacy fires, that's a sign the legacy system needs more stabilization investment before the rebuild can proceed at full speed.

## The underlying principle

You're asking a stretched organization to do two hard things at once, so you need to reduce load (through triage and toil reduction), protect knowledge (through retention, testing, and transfer), and give people a visible future (through rotation and migration-linked movement). Done well, the rebuild itself becomes your retention strategy. Done poorly, it becomes one more reason to leave.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's what I'd do in your position, with the caveat that the plan branches on what your assessment finds.

## The recommendation

**Don't approve a two-year rewrite. Commission a short, rigorous assessment, then most likely rebuild the policy core incrementally, one line of business at a time, while stabilizing the legacy system and fixing retention in parallel.**

Frame it to your leadership team as a single program with two tracks rather than a choice between the CTO's plan and the head of product's plan. Both of them are partly right, and you need both of them committed.

## Next 90 days: decide with evidence, stop the bleeding

**1. Align leadership on the approach before the answer.** Sit down with the CTO and head of product together. Agree on the assessment questions, the decision criteria, and who makes the final call. Getting agreement on how you'll decide defuses the debate before it hardens into camps.

**2. Run the data model assessment (4–8 weeks).** Trace recent slow features, audit the model against core P&C concepts, test it against your strategy, and build one thin-slice spike. Bring in one outside reviewer with P&C policy platform experience for credibility and to break ties.

**3. Start retention work immediately.** Don't wait for the assessment:
- Identify your 5–10 most critical people and talk to each of them this month
- Benchmark and fix compensation where it's below market
- Put retention agreements in place for the handful of people whose knowledge you cannot lose
- Tell the team clearly that a serious modernization is coming and that legacy engineers will be part of it

**4. Begin stabilizing legacy.** Start building characterization tests around policy transactions, rating, and endorsements, and automate the worst deployment pain. This pays off under every scenario.

**5. Triage the legacy roadmap.** With product, sort work into non-negotiable, high-value, and negotiable. Start saying no to low-value work now to free capacity.

**6. Address the "cloud-native" pressure separately.** Scope what it would take to offer hosted SaaS delivery and a modern API layer over the existing system. This may blunt the competitive threat within a year, independent of the core rebuild.

## Months 3–12: commit and build the foundation

Assuming the assessment confirms effective dating and possibly product definition are structurally broken:

- **Charter the core rebuild** as a funded program with a dedicated product owner, an executive sponsor, and protected capacity that can't be raided for sales requests
- **Staff a small, mixed core team** of 6–10: legacy domain experts, strong platform engineers, and one or two hires with P&C versioning experience
- **Invest heavily in domain modeling** before building much. Validate the design against your hardest real scenarios: out-of-sequence endorsements across renewals, cancellations and reinstatements, mid-term rate changes
- **Choose a first segment** for production, ideally a new line, state, or new customer so no conversion is required
- **Target real production use within 9–12 months**, even if small

If the assessment shows the model is salvageable, skip the core rebuild and put that capacity into API layering, product configuration, and extracting the capabilities that most slow you down.

## Months 12–36: migrate and retire

- Convert existing lines to the new core at renewal, one line at a time
- Move engineers with their lines of business so people have a visible path onto the new platform
- Keep legacy running read-only for historical terms, audits, and prior-term claims
- Replace downstream components like billing and documents only when there's clear value

## Build in checkpoints

Agree up front on the conditions that would change course:

- **Accelerate** if the first segment goes live on time and customers respond well
- **Reassess scope** if the core keeps expanding to absorb rating, billing, and documents. That's a sign you're drifting into a full rewrite and should do so deliberately or not at all
- **Pause and stabilize** if legacy emergencies repeatedly pull people off the core team
- **Escalate retention** if attrition among key knowledge holders continues despite your changes

Review these quarterly with the leadership team.

## What to tell your two leaders

To the CTO: *"You're right that we can't patch our way out. If the core is broken, we'll rebuild it, properly funded and protected. But we'll deliver it in stages so we're never betting the company on a single cutover."*

To the head of product: *"You're right that we need to keep shipping and migrate gradually. But this is not business as usual. We'll protect real capacity for the rebuild, and that means saying no to some customer requests on the legacy platform."*

## The one thing to avoid

The worst outcome isn't picking the wrong strategy. It's picking a strategy and then not funding or protecting it. A rewrite that starves legacy, or an incremental plan that keeps getting deprioritized, both end the same way: more attrition, slower delivery, and competitors pulling further ahead. Whatever you decide, make it an explicit, resourced commitment that leadership defends when the next urgent request arrives.

## Outcome summary (sent to Jev)

The recommendation is not to approve a two-year from-scratch rewrite. Instead, commission a short, rigorous assessment, then most likely rebuild the policy core incrementally, one line of business at a time, while stabilizing the legacy system and fixing retention in parallel. It should be framed as one program with two tracks, so both the CTO and head of product own it.

The reasoning is that big-bang rewrites of revenue-critical P&C systems routinely underestimate embedded rules, must still serve in-force policies, depend on customers agreeing to convert, and impose a feature freeze while competitors ship. The CTO is right that a structurally broken core, especially effective dating and out-of-sequence endorsements, can't be patched. Even so, it can be replaced in stages, using renewal-based conversion.

In the first 90 days:
- Align leadership on decision criteria.
- Run a 4–8 week data model assessment that traces slow features, audits core P&C concepts, tests the model against strategy, and builds a thin-slice spike, with an outside P&C reviewer.
- Start retention work immediately through conversations with critical people, compensation fixes, and retention agreements.
- Build characterization tests and automate deployment pain.
- Triage the legacy roadmap.
- Scope hosted SaaS and an API layer to answer the "cloud-native" pressure.

From months 3 to 12, if the core is confirmed broken, charter a funded, protected program with a small mixed team of 6–10. Invest heavily in domain modeling, launch a first segment requiring no conversion, and target production use within 9–12 months. If the model is salvageable, redirect that effort to APIs, product configuration, and extraction.

From months 12 to 36, convert lines at renewal and move engineers with their lines. Keep legacy available read-only for historical terms.

Quarterly checkpoints should trigger acceleration, a scope reassessment if the rebuild drifts toward a full rewrite, a pause if legacy emergencies interfere, or escalated retention efforts. The key caveat is that whatever is chosen must be explicitly funded and defended by leadership.
