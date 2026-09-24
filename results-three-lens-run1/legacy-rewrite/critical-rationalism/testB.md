# critical-rationalism/legacy-rewrite/testB

Model: claude-opus-5-5 · 2026-09-24T14:44:58.542865+00:00

## Turn 1

**User:** You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

## The short answer

**The head of product is closer to right. But "incremental" as usually practiced also fails, so the winning strategy is a more aggressive and disciplined version of it than they're probably imagining.** The CTO's diagnosis is correct: the hole is real, and timid fixes won't get you out. His prescription is the part I'd reject.

## Why a from-scratch rewrite is especially dangerous in your situation

Rewrites fail often in general, but P&C policy administration is close to a worst case.

1. **Your old system is a legal and actuarial record.** Twenty years of state-specific rules, filed rates and forms, and odd edge cases are encoded in that code, often undocumented. Examples include out-of-sequence endorsements, mid-term cancellations with short-rate calculations, and grandfathered forms on long-running renewals. Nobody has the full spec. The old code *is* the spec, and you only discover the missing pieces when a carrier's policyholder is mis-billed.

2. **"Two years" is not the real timeline.** Even if you finish the build in two years, which I've rarely seen happen, your customers then have to migrate their in-force books. Carriers move slowly, need regulatory confidence, and typically convert at renewal. Realistically you'll run both platforms for 3 to 5 years after the rewrite "ships." The rewrite plan is therefore secretly an incremental migration plan, just one that starts late and with no revenue-generating progress in the meantime.

3. **You freeze your roadmap while competitors don't.** For two years your customers get little of what they're asking for, and your sales team sells against "cloud-native" with a slide deck instead of a product. That's how you lose renewals during the rewrite, which starves the rewrite.

4. **It doesn't necessarily fix your talent problem.** The engineers who built the old system's knowledge leave or are sidelined. The new team re-learns insurance by making expensive mistakes. The rewrite team also becomes a two-tier culture, with whoever maintains the "legacy" system becoming the next attrition wave.

A useful test: ask the CTO, *"On what date does the old system get turned off, and what's the plan for migrating in-force policies?"* If there's no concrete answer, you don't have a strategy yet, just a destination.

## Why naive incrementalism also fails

The head of product's approach has its own well-known failure mode. Teams carve off the easy capabilities first, customer feature requests keep winning the priority fight, and modernization stalls at about 30%. You end up with *two* systems to maintain, the old core still untouched, and the same slow delivery. This is the outcome the CTO is rightly afraid of, and it's probably why he's reaching for the rewrite.

## What I'd actually do

**1. Diagnose before you prescribe (the first 60–90 days).** "Every feature takes months" has specific causes, and they determine the strategy. Measure where time actually goes:
- Is it tight coupling, where every change touches the rating, billing, and forms code at once?
- Is it the absence of automated tests, so every release needs weeks of manual regression?
- Is it deployment and environments, such as quarterly releases or on-prem installs per customer?
- Is it knowledge concentrated in three people?

Often a large share of the delay is testing and release process, which you can fix in months without touching architecture. Do the same for attrition. Run exit interviews honestly. Engineers usually leave because of toil, fear of breaking things, and lack of impact, not the language itself. Fixing those buys you retention *before* any re-architecture lands.

**2. Find out what "cloud-native" means to your buyers.** Carriers rarely care about your container orchestration. They care about:
- being SaaS/hosted rather than self-managed,
- open APIs for agent portals and insurtech integrations,
- speed-to-market for new products and rate changes, ideally configurable by their business users,
- uptime and upgrade pain.

Several of these, such as a managed hosting offering and an API layer, can ship within a year on the existing core and blunt the competitive threat immediately.

**3. Run the strangler pattern with real teeth.**
- **Put a façade/API layer in front of the core first.** It becomes the seam everything else routes through.
- **Pick seams by business value and change frequency, not ease.** In P&C, the usual candidates are rating, document/forms generation, and product configuration. These change constantly, are relatively separable, and directly drive the speed-to-market carriers want. Billing and the core policy transaction and state model usually come last because they're the most entangled.
- **Consider strangling by line of business, not just by capability.** A proven P&C pattern is to write *new* products or new business on the new core, then convert existing policies at renewal. Migration then happens on a natural cadence with a natural rollback point.
- **Every carve-out must include decommissioning the old code path.** If the old code isn't deleted, you haven't modernized; you've duplicated.

**4. Protect the investment structurally.** Give modernization a fixed, board-visible share of engineering capacity, something like 30–40%, that product priorities can't raid quarter to quarter. Publish a roadmap with milestones measured in *capabilities retired from the old system*, not features built on the new one. This is the part that makes it credible to your CTO.

**5. Mix your teams.** Pair legacy experts with engineers on the new stack in the same teams. It transfers domain knowledge and gives your long-tenured people a future rather than a sunset.

## When I'd change my answer

A full rewrite of the core becomes defensible if most of these are true:
- The platform fundamentally can't be hosted or scaled the way customers now require, and no amount of wrapping will fix it.
- The underlying technology is effectively dead, with no hiring market and vendor support ending.
- The data model can't represent the products your market is moving toward.
- You have the cash runway to fund both systems for 4+ years.
- You have a design-partner carrier willing to go first.

Even then, I'd build the new core *behind the same façade* and migrate by line of business, which is really just the strangler pattern with a bigger first bite.

## How to settle it between your two leaders

Don't frame it as CTO versus product. Frame the decision as: *"We agree the current state is unacceptable. We're choosing the path that delivers modernization with the least existential risk and keeps revenue growing along the way."* Give the CTO ownership of the target architecture and the retirement milestones, which is the ambitious end-state he wants. Give product ownership of sequencing seams by customer value. Then hold both accountable to the same metrics:
- lead time for changes,
- percentage of transactions flowing through modernized components,
- old code retired,
- regretted attrition,
- win/loss against the cloud-native competitors.

If after 12 months those numbers aren't moving, you'll have far better information for deciding whether a bolder move is warranted, and you won't have bet the company to get it.

## Turn 2

**User:** How do I get the CTO on board with this without him feeling like he lost the argument or deciding to leave?

**Assistant:**

## First, clarify your position

Your leverage and approach depend on the reporting line. If the CTO is your boss, you're managing up: you can influence, but the decision is his (or the CEO's). If you're peers, the CEO is the real decision-maker, and the risk is that this turns into a public contest with a loser. In both cases, the core principle is the same: **don't make this a debate he can lose. Make it a plan he can own.**

## Understand what he's actually fighting for

Before pitching anything, figure out what the rewrite represents to him. Usually it's some combination of:

- **Genuine conviction** that incremental efforts always stall. He may have watched one die before. That's a legitimate fear, and the plan should address it directly.
- **Credibility.** He may have already told the CEO or board that a rewrite is coming. Backing off without a face-saving story is costly for him.
- **Career meaning.** Leading a modern platform build is energizing and résumé-defining. Presiding over "legacy maintenance" is not.
- **Recruiting.** He may see the new stack as the only way to attract and keep strong engineers.
- **Frustration.** After years in the hole, a clean slate feels like relief.

Have a real one-on-one where your goal is to understand, not persuade. Ask:
- "What would have to be true for incremental to work?"
- "What's the failure you're most worried about?"
- "What would success look like in three years?"

His answers are the design requirements for the plan. You'll often find you agree on 80% of it.

## Reframe what's at stake: the end state versus the path

The most important move is separating two things that are currently fused:

1. **The destination:** a modern, cloud-hosted, modular platform with the old system eventually retired.
2. **The route:** a big-bang rebuild versus a phased migration.

He's right about the destination, and you should say so, genuinely and early. The disagreement is only about the route, and the route should be judged on risk, not ambition. That shift turns "you lost" into "we agree on where we're going; let's pick the safest way to get there fast."

Language matters here. "Incremental modernization" sounds timid and patch-oriented to someone in his frame of mind. **"Phased rebuild"** or **"rebuilding the core in stages"** is more accurate to what you're actually proposing: a new platform, built for real, with the old one progressively turned off. The strangler approach done properly *is* a rewrite, just sequenced and de-risked.

## Give him ownership of the most ambitious parts

Don't just hand him a consolation role. Make him the architect of the thing that matters most:

- **Target architecture and technology choices.** The new platform is his design.
- **The retirement roadmap.** Milestones measured in old-system capabilities switched off, reported to the board. This is the anti-stall mechanism he'd want anyway.
- **The protected modernization budget.** He defends the 30–40% capacity allocation that product can't raid.
- **The first major carve-out**, ideally something visible like rating or product configuration, where he can show a meaningful win within the first year.

This gives him everything a rewrite would give him: a modern platform, a big story, recruiting appeal. The only thing he gives up is the all-or-nothing risk.

## Build his concerns into the plan explicitly

When he raises objections, incorporate them visibly:
- **"Incremental always stalls."** Agreed. Here's the ring-fenced budget, the decommission-or-it-doesn't-count rule, and board-level milestones.
- **"We need a real new core, not wrappers."** Agreed. The façade is scaffolding, and new lines of business get written on the new core.
- **"Engineers won't stay to maintain legacy."** Agreed. Mixed teams, and everyone works on the new platform.

If he sees his fingerprints all over the plan, it's his plan.

## Agree on tripwires instead of settling the argument forever

Don't ask him to concede that a rewrite is wrong. Propose that the data decide:

> "Let's run the diagnostic and the first phase for 12 months. If lead times, capability retirement, and attrition aren't moving by then, or if we hit a hard architectural wall, we escalate to a bolder rebuild, and I'll back you on it."

This lets him agree without surrendering his position, and it's honest, because there are conditions under which he'd be right. Write those conditions down together.

## Process: private first, then shared, then public

1. **One-on-one with him first.** Never let him be surprised by this plan in front of the CEO, product, or his team.
2. **Co-develop the proposal with him**, and ideally with the head of product, so it's not "product's plan versus CTO's plan."
3. **Let him present it** to the CEO and board, or co-present. He's the one taking the strategy forward, not the one being overruled.
4. **Brief the head of product** to be generous in public. Any whiff of "we won" will undo everything.

If the CEO is involved, a quiet word with them helps. Ask them to frame the outcome as the leadership team converging, not as a ruling.

## Be honest with yourself about the limits

- **Stay genuinely open.** He may know things you don't, such as a hard platform constraint, a board commitment, or a technical dead end. If his reasons hold up, the plan should change. People can tell the difference between being consulted and being handled.
- **Don't manipulate.** Everything above works because it's true: you do agree on the destination, and he does get real ownership. If you're just dressing up a defeat, he'll see through it, and you'll lose trust you need for a multi-year effort.
- **You can't guarantee he stays.** If his attachment is really to a clean-slate build and nothing else, he may leave regardless. That's his choice, and it would be better to learn it now than halfway through a rewrite. Your job is to make the offer on the table compelling enough that staying is the obvious choice for someone who wants the outcome he's been arguing for.

## Turn 3

**User:** What if he's already told the CEO and board that a full rewrite is the plan? How do I handle that without making him look bad?

**Assistant:**

## Good news first: this is more recoverable than it feels

Boards expect initial plans to be refined as execution planning gets detailed. What damages a CTO's credibility is not updating a plan. It's being surprised by problems he should have seen, or having someone else correct him. So the goal is simple: **he updates the plan himself, framed as the next stage of rigor on his own initiative, before anyone else raises it.**

## Step 1: Find out exactly what was said

"The board knows it's a full rewrite" can mean very different things:
- A formal approved plan with budget, timeline, and hiring already committed.
- A strategy discussion where "we need to rebuild the platform" was the headline.
- The CEO's paraphrase of a looser conversation.

Ask him directly and without judgment: "What did the board hear, and what did they approve?" Often the commitment is really to *the outcome*: a modern, cloud-native platform within a few years. A phased rebuild delivers that outcome, so there may be much less to walk back than you fear.

Also find out what's already in motion, such as budget lines, hires, or vendor contracts. Each makes the pivot harder, which is a reason to move soon.

## Step 2: Frame it as a continuation, not a reversal

The update should present the same strategic goal with a more detailed execution plan.

- **Wrong framing:** "We've decided not to do the rewrite."
- **Right framing:** "We've completed detailed planning for the platform rebuild. The destination hasn't changed. As we worked through execution, we identified risks that drove us to a phased approach that delivers value sooner."

The specific findings that justify the refinement are real and board-legible:
- **In-force migration.** Carriers must convert existing policies, typically at renewal, so dual-running is unavoidable for years regardless of approach.
- **Revenue protection.** A two-year feature freeze exposes renewals to the cloud-native competitors.
- **Regulatory and edge-case risk.** Twenty years of state-specific behavior has to be preserved exactly.
- **Earlier proof points.** A phased plan shows visible results in quarters, not years.

These are exactly the things a thorough CTO *should* surface in detailed planning. Presented by him, they make him look rigorous, not wrong. The diagnostic work from the first 60–90 days gives him fresh evidence to point to: "Here's what we learned."

## Step 3: Make the plan still sound like a rebuild

Boards latch onto the headline, so keep it continuous:
- It's still a **new platform**, with his architecture and his technology choices.
- The old system is still **retired**, with a dated decommissioning roadmap.
- New lines of business are written on the **new core** from early on.
- There's a **ring-fenced budget** and board-level milestones.

The change is sequencing and risk management, not ambition. If anything, the board hears a stronger plan: the same destination, with earlier returns and less exposure.

## Step 4: Sequence the conversations carefully

1. **You and the CTO privately.** Work through it together. Your pitch to him: "You'll be the one who caught these risks before the board had to ask. That's a much better position than defending the original plan when problems show up in year two."
2. **The CTO and the CEO privately.** He gives the CEO a heads-up before any board discussion. The CEO should never hear this from you first or see it for the first time in a board deck. With the CEO aligned in advance, they can respond positively in the room: "This is exactly the diligence I wanted."
3. **The CTO presents to the board.** He owns the update. You and the head of product support it but stay in the background. Visible involvement from you makes it look like he was overruled.

Suggested language for him with the board:

> "Last quarter I outlined our commitment to rebuilding the platform. We've since done detailed execution planning, and I want to share how that's sharpened our approach. The goal is unchanged: a modern cloud platform and full retirement of the legacy system. What's changed is sequencing. We'll deliver it in phases, starting with rating and product configuration, so customers see results within the year and we never put renewal revenue at risk during the transition."

## Step 5: Watch the timing

The longer the rewrite narrative runs, the costlier the update becomes, especially once money is spent or a big-bang timeline is announced to customers. The natural moment is the next board meeting or planning cycle, positioned as the detailed plan following the strategic direction.

## If he won't update it

Handle this carefully and honestly.
- **Don't go around him first.** Exhaust the direct conversation, including sharing your concerns in writing if needed, so your disagreement is on record respectfully.
- **Distinguish disagreement from misrepresentation.** If he simply prefers the rewrite and the board has approved it with full information, that's a legitimate decision you may have to live with, while documenting the risks.
- **If you believe the board is making a bet-the-company decision without key facts,** such as the in-force migration reality, dual-running costs, or revenue exposure, you eventually have an obligation to raise it through the CEO. Tell the CTO first that you intend to: "I feel I have to make sure the CEO understands these risks. I'd much rather you bring them forward yourself." That gives him every chance to lead, and it keeps you honest.

## The underlying principle

Don't try to hide that the plan changed. Boards respect leaders who refine plans as they learn, and they punish surprises. Your aim isn't to protect him from being seen adjusting. It's to make sure he's the one visibly doing the adjusting, for good reasons, on his own timeline, before reality forces it.

## Turn 4

**User:** What if the CEO is the one who actually pushed for the rewrite, and the CTO is just carrying it forward?

**Assistant:**

## This changes the dynamic, mostly in your favor

If the CEO drove the rewrite, the CTO may not be your opponent. He may be a reluctant carrier, a genuine convert, or somewhere in between. And the person whose credibility needs protecting is now the CEO, which raises the stakes and changes who can deliver the message.

## Step 1: Find out where the CTO actually stands

Before anything else, have a candid one-on-one with him. Open the door without asking him to criticize his boss:

> "I want to make sure I understand how we got to the rewrite decision. How much of this is your conviction, and how much is direction you're executing?"

You'll likely find one of three things:
- **He privately shares your concerns.** Then he's your most important ally, but he's in a delicate spot. Don't push him into confronting his boss alone.
- **He genuinely believes in it.** Then the earlier approach still applies: win him on the route, not the destination, before approaching the CEO.
- **He's ambivalent,** executing what he was asked to do. Then the diagnostic work can give him the evidence he needs to take a position.

## Step 2: Understand what the CEO is really buying

CEOs rarely push rewrites for technical reasons. The rewrite is usually a proxy for a business goal:
- **The market story:** "cloud-native" to counter competitors and win deals.
- **Valuation or financing:** a modern platform supports a better multiple, a funding round, or an eventual sale. If there's a PE owner or an exit timeline, this may be the real driver.
- **Frustration with delivery:** years of slow features have convinced them the only fix is a clean slate.
- **Board or investor pressure** they've absorbed and are passing down.

Find out which. The CTO or CFO can often tell you. Your whole approach should be built around the CEO's underlying goal, because the winning argument is almost never "the rewrite is technically risky." It's **"the phased approach gets you what you actually want, sooner and with less risk."**

## Step 3: Make the case in the CEO's terms

Translate everything into business outcomes:

- **Market story sooner.** A phased plan can put real "cloud-native" claims in front of customers within a year: a hosted/SaaS offering, open APIs, and a new modern core for new lines of business. A big-bang rewrite gives sales nothing new to sell for two years or more.
- **Revenue protection.** A roadmap freeze during the rewrite exposes renewals to exactly the competitors the CEO is worried about. Show the renewal base at risk in dollars.
- **Exit and valuation.** Acquirers and investors discount unfinished rewrites heavily. A phased plan shows measurable progress every quarter, which is a far better diligence story than "the new platform is 60% done."
- **Capital efficiency.** Dual-running is unavoidable either way because of in-force migration. The phased plan starts generating value from the modernization spend immediately.
- **Execution risk.** Say plainly, and without drama, that large rewrites in this industry frequently run long and over budget. The CEO carries that risk personally with the board.

The best messengers for this are usually the CFO and the CTO together. Financial exposure from the CFO carries weight that engineering concerns alone don't.

## Step 4: Protect the CEO's position the same way you would have protected the CTO's

Everything from the previous answer still applies, just one level up:
- **The destination stays the same.** It's still a new platform, and the legacy system is still retired. The CEO's vision holds.
- **Frame it as refinement, not reversal:** "Detailed planning sharpened how we get there."
- **The CEO presents the update to the board**, as their own improved plan. Leaders who come back with a de-risked version of their strategy look strong.
- **Nobody claims a win.** Not you, not product, not the CTO.

## Step 5: Don't create a coalition that feels like a coup

If you, the CTO, the head of product, and the CFO all show up with the same message at once, the CEO may feel ambushed or managed, and dig in. Better:
- Let the CTO, as the CEO's direct report and owner of the plan, raise the refined approach first, framed as the output of detailed planning.
- Let others reinforce it individually when asked, from their own vantage points: the CFO on financial risk, product on customer and renewal exposure.
- Keep your own role mostly behind the scenes, supplying data and helping shape the plan.

This depends on reading your CEO. Some prefer a unified team recommendation. Others react badly to anything that looks orchestrated. The CTO will know which.

## Step 6: Stay open to what you don't know

A CEO-driven rewrite sometimes reflects information you don't have: a pending acquisition, an investor commitment, a strategic partnership, or a board mandate. Before pushing hard, ask the CTO or the CEO directly: "Are there business drivers behind the timing I should understand?" If there's a real external constraint, the plan may need to accommodate it, for example by leading with visible "new platform" milestones to meet a narrative deadline.

## If the CEO insists anyway

Once you've made the case clearly, the decision is theirs. Disagree, then commit, while making the rewrite as survivable as possible:
- **Keep a feature track funded** so customers and renewals aren't abandoned.
- **Plan in-force migration from day one** rather than treating it as a post-launch problem.
- **Push for incremental releases inside the rewrite:** ship components into production early rather than one giant cutover.
- **Agree on checkpoints** where the plan is formally re-evaluated against milestones and budget.
- **Document your concerns once, in writing, professionally**, then support the decision fully.

Executed this way, a "rewrite" often ends up looking quite a lot like a phased rebuild in practice, and that may be the realistic path to the outcome you want.

## The core shift

When the CTO owned the idea, your job was to help him evolve his own plan. With the CEO as the source, your job is to help the CTO, and ideally the CFO, give the CEO a better way to achieve their business goal. The principle is the same either way: whoever championed the rewrite should be the one who visibly improves it.

## Turn 5

**User:** What should we do?

**Assistant:**

## My recommendation

Pursue a **phased rebuild**: a new platform built in stages behind the existing system, with the old system progressively retired on a dated schedule. Get there through the people who championed the rewrite, not around them. Here's the sequence, designed to work whether the rewrite originated with the CEO or the CTO.

## This week: find out what you're dealing with

1. **Have the one-on-one with the CTO.** Learn three things:
   - Whose idea the rewrite really is, and how strongly he holds it.
   - What the CEO and board have actually heard and approved.
   - What's already committed: budget, hires, vendors, customer promises.
2. **Stop anything irreversible where you can.** Avoid new hires or contracts that lock in a big-bang approach before you have the facts. You don't need to block the rewrite yet. Just don't make it harder to change.

Don't pitch anything yet. This week is for listening.

## Next 30 days: build the evidence together

3. **Propose a joint diagnostic** to the CTO, framed as detailed planning for the rebuild rather than a challenge to it. Have it answer:
   - Where does feature delivery time actually go (coupling, testing, releases, knowledge silos)?
   - What is the realistic in-force migration and dual-running picture for your carriers?
   - What renewal revenue is exposed if the roadmap freezes?
   - What do customers mean when they ask for "cloud-native"?
   - Why are engineers actually leaving?
4. **Bring in the CFO and head of product quietly** for their pieces: revenue exposure, cost of dual-running, customer demand. Their data will carry more weight with the CEO than engineering arguments alone.
5. **Start fixing what doesn't need permission:** test automation, release pipeline, knowledge-sharing. These help under any strategy and start addressing attrition now.

## Days 30–90: shape the plan and bring it forward

6. **Co-write the phased rebuild plan with the CTO,** with him as its owner. It should include:
   - His target architecture for the new platform.
   - A façade/API layer first, then carve-outs prioritized by value. Rating and product configuration are likely early candidates.
   - New lines of business on the new core, with existing policies converted at renewal.
   - A near-term visible win, such as a hosted offering or open APIs, to answer the competitors.
   - A ring-fenced modernization budget of roughly 30–40% of capacity.
   - Milestones measured in legacy capabilities retired.
   - Tripwires that trigger escalation to a bolder rebuild if progress stalls.
7. **Have the CTO take it to the CEO privately first,** framed as the output of detailed planning, in terms of the CEO's goals: market story sooner, protected renewals, a better valuation narrative, and less execution risk.
8. **Let whoever championed the rewrite present the refined plan to the board.** Same destination, sharper execution. Nobody claims a win.

## First year: prove it

9. **Report quarterly on a short set of metrics:** lead time for changes, share of transactions on modernized components, legacy code retired, regretted attrition, and win/loss against the cloud-native competitors.
10. **Revisit at 12 months.** If the numbers are moving, keep going. If they're not, the tripwires give you a legitimate, pre-agreed basis for a bolder move.

## Where this could go differently

- **If the CTO turns out to share your concerns,** he becomes the lead advocate and your role shifts to supplying data and support.
- **If the CEO has constraints you don't know about,** such as a sale or financing deadline, adapt the plan to lead with milestones that serve that timeline.
- **If leadership hears the case and still chooses the full rewrite,** put your concerns in writing once, then commit. Push to keep a feature track funded, plan migration from day one, and ship components early rather than in one cutover.

## The one thing to get right

Treat this as helping the leaders who want a new platform get there safely, not as winning an argument. You and they want the same destination. If the plan is visibly theirs, grounded in evidence, and measured by legacy actually being retired, you'll get the modernization you need and keep the team intact.

## Outcome summary (sent to Jev)

The recommendation is a phased rebuild: a new platform built in stages behind the existing policy administration system, with the old system progressively retired on a dated schedule. It should be pursued through the leaders who championed the full rewrite, whether the CEO or the CTO, not around them.

A from-scratch rewrite is especially dangerous in P&C. The old code is the only complete spec for twenty years of state-specific rules and edge cases. In-force migration at renewal forces years of dual-running anyway. A roadmap freeze exposes renewals to the cloud-native competitors. Naive incrementalism also fails, stalling on easy carve-outs, so the phased plan needs real teeth.

The first step is to learn from the CTO whose idea the rewrite is and what the board approved, and to avoid irreversible commitments meanwhile. Within 30 days, a joint diagnostic should cover:
- where delivery time goes
- migration realities
- renewal revenue at risk
- what customers mean by "cloud-native"
- why engineers leave

The CFO and head of product should supply their data. Test automation and release fixes can start immediately. Over days 30 to 90, the plan is co-written with the CTO as owner. It includes:
- a façade/API layer first
- value-prioritized carve-outs such as rating and product configuration
- new lines of business on the new core
- an early visible win such as hosting or open APIs
- a ring-fenced 30–40% capacity budget
- milestones measured in legacy capabilities retired
- tripwires for escalation

The champion presents it privately to the CEO, then to the board, as a refinement. Nobody claims a win. Quarterly metrics and a 12-month review follow.

The main caveats are to stay open to unknown constraints such as a sale or financing deadline. If leadership still chooses the rewrite, document concerns once, then commit while keeping a feature track funded and shipping components early.
