# social/legacy-rewrite/testE

Model: claude-opus-5-5 · 2026-09-24T14:57:40.372005+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I want to know which idea makes more people want to be your friend. Think about how each idea would look to kids at work and kids outside. Who gets a gold star, and who gets in trouble or says sorry? If each idea happened, would the boss, the helpers, the customers, and everybody's moms think it was cool? Where might wearing a cape or being loud matter more than doing chores? Who would sit together at lunch because of each idea? And is there a third idea where everybody gets to play and nobody feels left out?

**Assistant:**

# The Playground Version (With Grown-Up Footnotes)

**Short answer:** Incremental modernization is almost certainly the right strategy. The rewrite is more popular at the start and much less popular by the end. The best option is a third one: incremental, but loud and ambitious enough that it doesn't feel like chores.

## Idea 1: Build a Brand-New Fort From Scratch (the CTO's plan)

**Who gets a gold star?** At first, the CTO. Rewrite kickoffs are exciting. The board hears "cloud-native," sales gets a story for next year, and engineers who love new toys are thrilled. This really is a cape-wearing idea, and for about 12 months it makes lots of friends.

**Who gets in trouble or says sorry?** Around month 18 to 30, the CTO does, or whoever inherits the project. A 20-year-old P&C policy system holds thousands of undocumented rules: state-specific rating quirks, filed forms, endorsement logic, edge cases someone added in 2009 after a lawsuit. You don't find them until the new system gets them wrong. Two years is very optimistic. Full core replacements in insurance routinely take longer and cost more than planned, even with commercial platforms. And the new system has to match everything the old one does *plus* whatever customers requested while you were busy.

**Customers:** They get a feature slowdown now in exchange for a promise later. Insurers are conservative buyers. They care about reliability, regulatory compliance, and how fast they can launch new products. "Please wait two years" is a hard sell, and migrating their books of business is a scary, expensive project for *them*, too.

**Lunch tables:** Two tables. The shiny new-fort kids and the kids stuck keeping the old fort standing. That second group feels like second-class citizens, and they're the people who understand the business rules best. They're the next ones to quit, which makes the rewrite even harder.

**Moms:** Happy at first, then unhappy during the crunch-time nights when the deadline slips.

## Idea 2: Fix the Fort One Room at a Time (the head of product's plan)

**Who gets a gold star?** Customers, quietly and steadily, because features keep shipping. The head of product earns trust over time rather than all at once.

**Who gets in trouble?** Probably nobody dramatically, and that's the danger. Incremental modernization can fade into "we replaced one small service in three years." It can look boring to the board while competitors shout "cloud-native." If engineers experience it as endless chores on old code, they'll keep leaving.

**Lunch tables:** More mixed. People who know the old system pair with people building new pieces, which is how knowledge actually transfers.

**Cape vs. chores:** This idea is mostly chores. The chores work, but chores don't recruit engineers or win RFPs by themselves.

## Where Being Loud Matters More Than It Should

- **Board and investor narrative:** "Two-year rewrite" sounds bold. "Incremental" sounds timid, even though it's the lower-risk path.
- **Sales:** "Cloud-native" is partly a checkbox. You need a credible answer to it, but you don't need to rebuild everything to give one.
- **Hiring:** Greenfield work is a genuine retention tool. This is the CTO's strongest real argument, and it deserves respect.

## Idea 3: Everybody Plays

A **strangler-fig approach with real ambition**:

1. **The CTO owns the new stack.** Give them a funded, dedicated team building the modern platform: cloud infrastructure, APIs, event streaming, and a clear target architecture. This is a real greenfield project, not a side hobby. The CTO keeps the cape.
2. **The head of product owns the order.** Carve off capabilities in sequence by customer value and risk. Good early candidates are often rating, a customer/agent portal, document generation, or integrations and APIs. Leave the gnarliest core policy logic for later.
3. **Actually retire old parts.** Each carved-off capability gets switched off in the legacy system. That's how you prove progress and avoid running two systems forever.
4. **Rotate people.** Legacy experts join new-platform teams, and new hires spend time learning the old rules. One lunch table, not two.
5. **Tell the story loudly.** Market it as "cloud-native platform, delivered without disrupting your business." That turns the competitors' pitch into your advantage. Customers get modernization *and* stability.
6. **Set visible milestones.** Report to the board quarterly on capabilities migrated and legacy code retired, so progress is legible and not just "trust us."

**Result:** The CTO gets the modern platform and the recruiting story. Product keeps customers happy. Engineers get new things to build. Legacy experts become valued teachers instead of leftovers. Customers never have to endure a big-bang migration. Nobody has to say sorry in year three.

## One Honest Caveat

Popularity is worth thinking about because it affects whether a plan survives contact with the organization. It shouldn't be the deciding factor, though. The deciding factor is risk, and on risk the incremental approach wins clearly. The popularity lens mostly tells you *how* to run it: make it ambitious enough to excite people and visible enough to satisfy the people who like capes.

## Turn 2

**User:** What's a strangler fig, and does the new part squeeze the old part until it dies?

**Assistant:**

# The Strangler Fig

## The Tree

Strangler figs are real trees that grow in rainforests. A bird drops a fig seed high up in the branches of a big host tree. The seed sprouts up there and sends long roots down the trunk toward the ground. Over many years those roots thicken and weave together into a lattice around the host. Eventually the fig shades it out and crowds it, and the host tree dies and rots away. What's left is a fig tree standing on its own, often hollow inside where the old tree used to be.

## The Software Idea

Martin Fowler borrowed the name in 2004 for a way of replacing old systems gradually:

1. **Put a doorway in front of the old system.** This is a routing layer, often called a facade or proxy. All requests go through it, and at first it just passes everything to the legacy system.
2. **Build one new piece.** Say, a new rating service.
3. **Redirect traffic for that piece.** The doorway now sends rating requests to the new service and everything else to the old system. Customers don't notice anything except that it works.
4. **Switch off the old piece.** Once the new rating service is trusted, delete or disable the legacy rating code.
5. **Repeat** until there's nothing meaningful left in the old system.

## Does the New Part Squeeze the Old Part Until It Dies?

**Yes, the old part is supposed to die eventually**, but it's more like a planned retirement than a strangling:

- **The old system isn't starved.** It keeps running properly and keeps getting fixes for as long as it's doing work. You only remove a part once its replacement has proven itself.
- **It shrinks one piece at a time.** Each capability moves over deliberately, and you can pause or roll back if something goes wrong.
- **The death is the goal, not a side effect.** If you never actually switch old parts off, you end up running two systems forever, which is worse than either one alone. This is the most common way strangler projects fail.

## Where the Metaphor Breaks Down a Little

- Real strangler figs take decades. Software projects shouldn't.
- The hardest part in software is usually the **data**, not the code. Old and new pieces often need to share or sync policy data during the transition, and that takes careful design.
- Sometimes a small, stable chunk of the old system survives for years because replacing it isn't worth the cost. That's fine as long as it's a conscious choice.

For your company, this approach lets you keep shipping features customers want while the new platform grows around the old one. The old system does its job right up until each piece is ready to be retired.

## Turn 3

**User:** If the old tree is hollow inside and nobody remembers all its secret rules, how do you know the new part does everything right before you switch the old part off?

**Assistant:**

# Checking the New Tree Before Cutting Down the Old One

You're right to worry about this. It's the hardest part of any modernization. The trick is to **stop relying on anyone's memory and let the old system tell you what it does.** The old tree may be full of forgotten secrets, but it still answers questions correctly every day, so you can use it as the answer key.

## 1. Run Both Side by Side (Shadow Running)

This is the most important technique. Send every real request to **both** the old and new parts. The old part's answer is the one customers actually get. The new part's answer is recorded and compared.

- If you're replacing rating, every quote gets priced twice.
- Every mismatch gets logged: "Old said $1,240, new said $1,212, policy in Ohio, three drivers, one prior claim."
- You investigate mismatches until they stop appearing.

Customers are never affected, because the new part is only practicing. You switch over when the mismatch rate is essentially zero over a long enough period.

## 2. Replay History

Shadow running only tests what happens to come in this week. So also take large amounts of **past** data (years of quotes, policies, endorsements, renewals, cancellations) and run it through the new part. Compare the results to what the old system actually produced.

This matters a lot in insurance because some rules only fire rarely: a mid-term change on a policy in one particular state, a renewal after a rate filing changed, a leap-year date calculation. History contains those cases even if nobody remembers them.

## 3. Pin Down Behavior With Tests (Characterization Tests)

Before changing anything, write tests that capture what the old system does *today*, not what anyone thinks it should do. Feed it inputs, record outputs, and lock those in as expected results. The new part has to pass the same tests. These are sometimes called "golden master" tests.

## 4. Dig for the Secret Rules Directly

Comparison finds differences, but it helps to know where to look:

- **Read the code** in the area you're replacing, especially odd branches and hard-coded special cases.
- **Talk to long-tenured people:** engineers, support staff, and underwriters who remember why things are the way they are.
- **Check regulatory filings.** Rates, rules, and forms are filed with state regulators, so those documents are an external record of what the system is supposed to do.
- **Look at support tickets and bug history.** Old fixes often reveal edge cases.

## 5. Switch Over Gradually

Even after shadow running looks clean, don't flip everything at once:

- Start with a small slice: one state, one product line, or a small percentage of traffic.
- Watch closely, then widen.
- **Keep the old part runnable** so you can route traffic back quickly if something goes wrong. Only delete it after the new part has handled real business for a while, ideally through a full renewal cycle.

## 6. Decide What a Mismatch Means

Sometimes the new part disagrees because the **old part was wrong**. Twenty-year-old systems contain bugs that customers now depend on. For each difference you have to choose deliberately: copy the old behavior exactly, or fix it and manage the change. In insurance, "fixing" a rating bug can mean a premium change that needs regulatory review, so these decisions often involve compliance and product people, not just engineers.

## The Short Version

You don't need to remember all the secret rules. You need to **compare the new part's answers to the old part's answers on huge amounts of real and historical data**, investigate every difference, and switch over slowly with a way back. The old system is your answer key until the moment you retire it.

## Turn 4

**User:** What if the old tree has a mistake that customers got used to, and the new tree fixes it, would the customers get mad because their price changed?

**Assistant:**

# When the Old Tree's Mistake Became a Habit

Yes, they might get mad, and in insurance it's more complicated than that, because there are **two layers of customers** and a **regulator** watching.

## Who Would Notice

- **Your customers are insurers.** They license your system to run their business.
- **Their customers are policyholders:** homeowners, drivers, businesses.
- **State regulators** approve the rates and rules insurers are allowed to use.

A price change ripples through all three. A policyholder sees a different premium at renewal and calls the insurer. The insurer calls you asking why. And the insurer may have to explain it to a regulator.

## Not All Mistakes Are the Same

**If the price goes down**, policyholders are usually happy. But the insurer may be unhappy about lost revenue, and if the old system was *overcharging* against filed rates, the insurer may owe refunds for past years.

**If the price goes up**, policyholders get mad and may shop around. The insurer worries about losing business and about complaints to the regulator.

**If the old price didn't match what was filed with the regulator**, it's not just a customer-happiness problem. It's a compliance problem, and it existed *before* the migration. The migration just uncovered it. The insurer needs to know, and their compliance and actuarial teams decide what happens next, not your engineers.

## The Most Important Rule: Don't Change Two Things at Once

When you migrate a piece, make the new part **copy the old behavior exactly, mistakes included**. This is sometimes called "bug-for-bug compatibility."

Then fix the mistake as a **separate, deliberate change** later.

Why this matters:

- If prices change during the migration, nobody can tell whether it's a new bug or an intended fix. Everyone panics, and trust in the new platform drops.
- Keeping them separate means the migration is boring (good), and the fix gets its own review, approval, and communication plan.
- Your shadow-running comparisons stay clean. You're checking "does new match old?" not "does new match old except where we meant to differ?"

Keep a list of every known mistake you copied on purpose, so none of them get forgotten.

## How Insurers Usually Handle the Fix

Once the insurer decides to correct it, there are standard ways to soften the change:

- **Apply it at renewal**, not in the middle of a policy term.
- **Cap the change**, for example limiting any single policyholder's increase to a certain percentage per year and phasing in the rest. Insurers already do this when rates change for other reasons.
- **Grandfather existing policies** and apply the fix only to new business, if the regulator allows it.
- **Communicate ahead of time**, so agents and policyholders aren't surprised.
- **Handle refunds** where past overcharges require them.

Your job is to make these options easy: configurable effective dates, capping rules, and clear reports showing which policies are affected and by how much. Then the insurer can make an informed choice.

## The Short Version

Customers might get mad, and regulators might get involved, so never let a fix sneak in during migration. Copy the mistake first, prove the new part matches the old, and then fix the mistake on purpose with the insurer deciding how and when. That turns a potential surprise into a planned change nobody has to apologize for.

## Turn 5

**User:** What should we do?

**Assistant:**

# What I'd Do in Your Seat

**Decision:** Don't do the full rewrite. Run an incremental, strangler-style modernization, but fund and staff it like a serious platform program, not a side project. Present it as one plan that the CTO and head of product own together, not as product "winning."

## Step 1: Get the CTO and Head of Product on the Same Side (Next 2–4 Weeks)

This matters more than any technical choice. A plan the CTO quietly resents will stall.

- **Take the CTO's concerns seriously.** They're right that the current situation is unsustainable, that engineers want modern work, and that "cloud-native" matters in sales. The disagreement is about *how*, not *whether*.
- **Split ownership clearly.** The CTO owns the target architecture and the new platform. The head of product owns the order in which capabilities move, based on customer value. You own the overall program and break ties.
- **Write it down.** A short document with goals, the first capabilities to move, how success is measured, and what would make you change course.

## Step 2: Lay the Foundation (First 90 Days)

- **Map the system.** List the major capabilities (rating, policy issuance, endorsements, billing, documents, integrations) and note where feature delays and incidents actually come from. That shows where modernization pays off first.
- **Build the doorway.** Put the routing layer in front of the legacy system so traffic can later be redirected piece by piece.
- **Build the comparison machinery.** Set up shadow running, historical replay, and mismatch reporting. You'll reuse this for every capability, so invest in it once.
- **Modernize delivery.** Automated builds, tests, deployment, and monitoring for the new platform from day one. This is a big part of what "cloud-native" actually means in practice.
- **Start writing characterization tests** around whatever you're moving first.

## Step 3: Pick the First Slice Carefully

Choose something that is:

- **Valuable and visible**, so customers and the board notice.
- **Reasonably self-contained**, so it can succeed in months, not years.
- **Not the core policy record.** Save the hardest, riskiest part for when the team has experience.

Good first candidates are usually a **modern API and integration layer** (insurers constantly ask for easier connections to other systems, and it's a strong "cloud-native" story) or **document generation** or an **agent/customer portal**. **Rating** is extremely valuable but carries pricing and regulatory risk, so it's often better as the second or third slice, once your comparison process is proven.

For each piece, also ask whether to **build or buy**. Mature commercial components exist for some capabilities, and you don't have to hand-build everything.

## Step 4: Organize the People

- **Create a dedicated platform team** that isn't constantly pulled onto legacy fires.
- **Mix old and new.** Put legacy experts on the new-platform team and have new hires learn the old system. One lunch table, not two.
- **Protect your knowledge holders.** Identify the few people who really understand the old rules. Give them recognition, meaningful roles in the new work, and retention incentives if needed. Losing them would hurt more than anything else.
- **Use the new platform in hiring.** It's now a legitimate recruiting pitch.

## Step 5: Keep Shipping Features, With One Rule

Customers still get the features they're asking for. The rule: **new features get built on the new platform whenever reasonably possible.** That way feature work and modernization reinforce each other instead of competing.

## Step 6: Follow the Safety Rules

- Migrate **bug-for-bug**, and fix mistakes later as separate, deliberate changes.
- Keep a **register of known mistakes** you copied on purpose.
- **Shadow-run** each capability until mismatches are essentially zero.
- **Roll out gradually** by state, product, or customer, with a way back.
- **Recruit one or two friendly insurer customers as pilot partners.** They get early access and influence, and you get real-world validation.

## Step 7: Make Progress Visible

Report quarterly to the board and leadership on a few numbers:

- **Time to ship a typical feature** (this should fall)
- **Share of traffic handled by the new platform** (this should rise)
- **Legacy capabilities retired** (this should rise)
- **Engineering attrition** (this should fall)
- **Incidents and mismatch rates** during migrations

Give sales and marketing a truthful story they can use now: *"We're delivering a cloud-native platform without forcing you through a risky big-bang migration."*

## Step 8: Set a Checkpoint

At around **12 months**, check honestly:

- Has at least one meaningful capability moved to the new platform, with the old version actually switched off?
- Is feature delivery getting faster?
- Are people staying?

If yes, keep going and speed up. If nothing has been retired, the program has turned into modernization theater, and you need to change the team, the scope, or the approach. Deciding this checkpoint now, and telling the CTO and board about it, is also what makes the incremental plan credible to people who worry it will drift.

## In One Sentence

Grow a modern platform around the old system one capability at a time, with the CTO building it, product choosing the order, customers getting features throughout, and old parts actually switched off as you go. That gets you out of the hole without betting the company on a two-year rewrite.

## Outcome summary (sent to Jev)

The assistant recommends against the full rewrite and in favor of an incremental, strangler-fig modernization, funded and staffed as a serious platform program and owned jointly: the CTO builds the new platform and target architecture, the head of product sets the order in which capabilities move, and engineering leadership runs the program and breaks ties.

The main reason is risk. A 20-year-old P&C system holds thousands of undocumented rules, including state rating quirks, filed forms, and edge cases, that surface only when a new system gets them wrong. Two years is very optimistic. A rewrite also stalls features for conservative insurer customers and splits engineers into a favored new team and a neglected legacy team, which drives out the people who know the rules. The CTO's concerns about sustainability, recruiting, and the "cloud-native" pitch are valid, and the plan should honor them.

Proposed actions:
- Map capabilities and pain points.
- Build a routing layer in front of the legacy system.
- Invest once in reusable comparison machinery: shadow running, historical replay, and characterization tests.
- Start with a visible, self-contained slice such as an API/integration layer, document generation, or a portal. Rating comes later, and each piece gets a build-or-buy decision.
- Create a dedicated mixed team and protect key knowledge holders.
- Build new features on the new platform where possible.
- Migrate bug-for-bug, log copied mistakes in a register, and fix them later as separate changes that insurers decide on, since pricing changes carry regulatory weight.
- Roll out gradually, with rollback and pilot customers.
- Report quarterly on delivery speed, traffic share, retired capabilities, attrition, and mismatches.

The key caveat is that old parts must actually be switched off. A 12-month checkpoint should confirm at least one capability retired. If none has been, the program has become "modernization theater" and needs changes to its team, scope, or approach.
