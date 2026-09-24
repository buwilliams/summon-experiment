# legacy-rewrite/social/testE

Model: claude-opus-5-5 · 2026-09-24T15:28:43.455204+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I want to know which idea makes more people want to be your friend. Think about how each idea would look to kids at work and kids outside. Who gets a gold star, and who gets in trouble or says sorry? If each idea happened, would the boss, the helpers, the customers, and everybody's moms think it was cool? Where might wearing a cape or being loud matter more than doing chores? Who would sit together at lunch because of each idea? And is there a third idea where everybody gets to play and nobody feels left out?

**Assistant:**

## The short answer

**Incremental modernization is usually the right call for a system like yours.** But the CTO is right about something important: a timid, underfunded incremental plan fails too. The best path is a third option that combines the head of product's method with the CTO's ambition.

Why the full rewrite is so risky here: a 20-year-old P&C policy admin system holds thousands of undocumented business rules, including state-specific rating, forms, endorsements, cancellation rules, and regulatory quirks. Rewrites keep discovering these rules late. The new system can't replace the old one until it matches nearly all of that behavior, so you pay for two platforms, freeze features for customers, and often land years late. "Two years" for a from-scratch policy admin rewrite is very optimistic.

Now to your real question, the social one.

## Idea 1: Tear it down and build a new one (the rewrite)

**Who gets a gold star, and when:** Early, the CTO does. It looks bold and visionary. The board likes the story, marketing gets to say "cloud-native," and recruiting gets easier because engineers love greenfield work.

**Who gets in trouble later:** Around month 12–18, the new system usually isn't close to parity. Customers have been waiting for features, and sales can't point to a roadmap. The people keeping the old system alive feel like janitors for a building being demolished, and many of them leave. They are exactly the people who know the hidden rules. If it slips, the CTO is the one who says sorry, and sometimes leaves.

**Would everyone think it's cool?**
- *Boss/board:* Yes at first, nervous by year two.
- *Helpers (engineers):* New hires love it. Legacy experts feel demoted.
- *Customers:* Insurance carriers are risk-averse. A big migration plus a feature freeze scares them.
- *Moms (families, outsiders):* A late rewrite usually means crunch time and long nights.

**Who sits together at lunch:** The CTO, the shiny new-platform team, marketing, and the board. The legacy team sits alone. Customer success sits with the annoyed customers.

## Idea 2: Fix one room at a time (incremental)

**Who gets a gold star:** It comes slowly, and mostly to the head of product. Customers keep getting features, finance sees steady progress, and risk stays low.

**Who might get in trouble:** If progress is invisible, it looks like "more of the same." Engineers keep leaving because nothing feels new. Competitors' "cloud-native" pitch keeps landing, and the head of product gets blamed for "having no vision." Incremental plans also die quietly when urgent features keep stealing the modernization team.

**Would everyone think it's cool?**
- *Boss/board:* Safe, but maybe boring.
- *Helpers:* Legacy experts stay valued. Ambitious engineers may be bored.
- *Customers:* Mostly happy, since nothing breaks and features keep coming.
- *Moms:* Saner hours.

**Who sits together at lunch:** Product, sales, customer success, finance, and the legacy experts.

## Where wearing a cape matters more than doing chores

- **The cape matters** with the board, with recruiting, and in marketing against "cloud-native" competitors. The story really does affect hiring and some deals.
- **Chores matter more** with your actual buyers. Carriers care about reliability, compliance, and migration risk far more than architecture labels. Check your lost deals: are you actually losing because of "cloud-native," or because of slow features and integrations?
- **The lesson:** The incremental plan loses mainly because it has no cape. So give it one.

## The third idea: build the new playground next to the old one

This is a well-resourced "strangler" approach with a real identity:

1. **The CTO names and owns the target platform.** It gets a real name, architecture, and brand. The CTO keeps the vision and the cape.
2. **Product owns the order of work.** Each slice is chosen for customer value, not only technical neatness.
3. **Pick a visible first win.** Examples include a modern API layer, a new rating or quoting service, or a new line of business built fully on the new stack for new customers. Marketing can then honestly say "cloud-native" for real modules.
4. **Pair legacy experts with the new team.** They become the rule-keepers instead of the janitors. This helps keep your best people and catches hidden rules early.
5. **Protect the team.** Give the modernization team dedicated people and budget that feature requests can't raid.
6. **Share the scoreboard.** Measure shipped customer value, the percentage of traffic or policies on new components, and engineer retention. Hold quarterly checkpoints with honest criteria for speeding up, changing direction, or stopping.

**Who sits together at lunch:** The CTO and head of product co-own it. New engineers and legacy experts work on the same team. Sales gets a story and a roadmap. The board gets a vision with lower risk.

One honest caveat: "nobody feels left out" is a good goal, but the CTO will need to give up the clean-slate dream, and product will need to give up some feature capacity. The third idea works because both of them give something and both get credit, not because nobody gives anything up.

## Turn 2

**User:** Does the new playground have a slide?

**Assistant:**

Yes, and it might be the most important piece of equipment there. A slide is fun, fast, and goes one direction without much effort. The new platform needs a few of those.

**A slide for the helpers (engineers):** Code should go from laptop to production in minutes, not weeks, with automated tests and deploys. This is the thing that makes good engineers want to stay. If the new platform feels as slow to ship on as the old one, nobody will want to play there.

**A slide for customers (the migration path):** Carriers should be able to glide from the old system to the new one: automated data conversion, side-by-side validation that the new rating matches the old, and a way to move one line or one state at a time. If moving is a scary climb, customers will stay on the old playground forever and you'll run both systems indefinitely.

**A slide for sales (the demo):** Build something quick and delightful to show, like instant quoting through an API or a self-serve sandbox a prospect can try the same day. That's your answer to the competitors' "cloud-native" pitch, and it's real rather than just a cape.

**Playground rule:** The slide only goes one way. Once a capability moves to the new platform, turn it off in the old one. Otherwise people keep climbing back up the ladder, and you end up maintaining two playgrounds instead of one.

## Turn 3

**User:** What happens to the old playground when everybody leaves? Is it sad?

**Assistant:**

A little sad, and that's okay. Here's what usually happens.

**It empties slowly, not all at once.** The last few kids are the hardest to move: odd policy types, one carrier with custom rules, a state with unusual filing requirements. Plan for this tail. It often takes as long as everything before it. Set a real closing date, or the old playground stays open "just for a few more months" for years.

**Some of it has to stay, quietly.** Insurance records have long memories. Claims can surface years after a policy ends, and regulators require you to keep policy history. So before you tear anything down, move the old records into a cheap, searchable archive. Think of it as a scrapbook of the playground, not the playground itself.

**Then you really do turn it off.** Servers get shut down, licenses cancelled, the old code frozen. That's when the savings actually show up. Until the lights are off, you're paying for two playgrounds.

**About the sad part:** The people who built and cared for that system kept your company alive for 20 years, and a lot of your hidden business rules exist only in their heads. Honor that out loud. Give them key roles on the new platform, credit them publicly, and hold an actual retirement party for the old system. Teams that feel respected carry their knowledge forward. Teams that feel like leftovers take it with them when they leave.

So it's a little sad, but mostly it's a sign the plan worked: the old playground did its job, and everyone got somewhere better.

## Turn 4

**User:** Do the grown-ups get cake at the retirement party?

**Assistant:**

Yes, and it should be a good cake, not grocery-store sheet cake.

**Make the cake about the right people.** Write the names of the folks who kept the old system alive on it, or at least read them out loud. The engineer who knew why a Texas endorsement rule worked the way it did deserves a bigger slice than the executive who approved the budget.

**Invite the people who left.** Former engineers who built pieces of the old system often love being invited back. It's good for your reputation as a place to work, and "boomerang" hires do happen.

**Have smaller cakes along the way.** Don't save everything for one big party at the end of a multi-year effort. Celebrate the first customer on the new platform, the first capability switched off in the old one, and the first state fully migrated. Regular cake keeps people going through the long, boring middle.

**Put cake in the budget.** Really. A few hundred dollars per milestone is tiny compared to the cost of losing one experienced engineer who felt their work went unnoticed.

And save the last slice for whoever finally turns off the last server. That's the moment it's actually done.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's my recommendation.

## The decision

**Don't do the from-scratch rewrite. Do a funded, incremental modernization with an ambitious target platform: the "new playground next to the old one."** Frame it as one plan the CTO and head of product co-own, not a win for either side.

## First 90 days

**1. Get the facts that settle the argument (weeks 1–4)**
- **Lost deals:** Review the last 12–18 months of losses. Did you lose because of "cloud-native," or because of slow features, integrations, or price? This tells you how much the cape actually matters.
- **Attrition:** Talk to engineers who left or are close to leaving. Is it the old tech, slow shipping, or feeling stuck? A faster delivery pipeline may fix more than a new stack.
- **Where it hurts:** Map which parts of the system cause the most delay, incidents, and customer pain. These are your first candidates to carve off.

**2. Align the leaders (weeks 3–6)**
- Get the CTO and head of product to agree on a one-page plan: the target architecture, the order of work, and shared success metrics.
- Give the CTO clear ownership of the platform vision so this doesn't read as them losing.
- Take it to the CEO and board as a joint recommendation.

**3. Set up the team (weeks 4–8)**
- Create a dedicated modernization team with protected capacity, roughly 20–30% of engineering to start. Feature work can't borrow from it.
- Pair your deepest legacy experts with new-platform engineers.
- Build the fast deploy pipeline first. It helps both systems and gives engineers an early, visible improvement.

**4. Pick the first slice (weeks 6–12)**
- Choose one capability that customers value and that marketing can show, such as an API layer, a rating or quoting service, or a new line of business for new customers.
- Scope it to reach production within 6–9 months with real customers using it.

## How to know it's working

Review quarterly:
- Share of traffic or policies running on new components
- Lead time for new features
- Engineer retention, especially among legacy experts
- Customer satisfaction and win rates

Agree in advance on what would make you speed up, change course, or reconsider.

## When the CTO might be right

Revisit the rewrite if the old system is genuinely at risk of failing (unsupported hardware, security exposure, vendor end-of-life), or if the analysis shows the core design can't be carved up at all. Even then, rebuild one line of business at a time rather than everything at once.

## Your role

The biggest risk isn't picking the wrong strategy. It's the CTO and head of product continuing to pull in different directions. Your job is to get them into the same plan, protect the modernization team from feature pressure, and keep the story visible so the board, engineers, and customers can see progress.

And budget for cake.

## Outcome summary (sent to Jev)

The recommendation is to reject the from-scratch rewrite and pursue a funded, incremental "strangler" modernization toward an ambitious target platform, built next to the old system and co-owned by the CTO and head of product. The CTO names and owns the platform vision, product sets the order of work by customer value, and the plan goes to the CEO and board as a joint proposal.

The main reason is risk. A 20-year-old P&C policy system holds thousands of undocumented rules, such as state-specific rating, forms, endorsements and cancellation logic, that rewrites discover late. That forces the company to pay for two platforms and freeze features for risk-averse carriers, and two years is very optimistic. The CTO is still right that a timid, underfunded incremental plan fails, so the plan needs a visible identity.

Proposed actions:
- Review 12–18 months of lost deals to see whether "cloud-native" actually matters.
- Interview departing engineers.
- Map pain points to find the first capabilities to carve off.
- Dedicate a protected team of roughly 20–30% of engineering, pairing legacy experts with new-platform engineers.
- Build a fast deploy pipeline first.
- Ship a visible first slice, such as an API layer, a rating or quoting service, or a new line of business, to real customers within 6–9 months.
- Make migration one-way by turning capabilities off in the old system.
- Archive old records for claims and regulators, then set a firm shutdown date.
- Credit legacy staff publicly and celebrate milestones.

Progress would be tracked quarterly through:
- the share of traffic or policies on new components
- feature lead time
- retention
- customer satisfaction and win rates

Speed-up and stop criteria would be agreed in advance.

The caveats are that both leaders must give something up and that the migration tail may take as long as everything before it. A rewrite should be revisited only if the system faces failure risk or cannot be carved up, and even then it should proceed one line of business at a time.
