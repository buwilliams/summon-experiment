# legacy-rewrite/critical-rationalism/testA

Model: claude-opus-5-5 · 2026-09-24T15:23:48.108147+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

**Incremental modernization is almost certainly the right strategy, but only if it's done as a funded, architecturally directed program, not as "incremental fixes."** Your CTO is right that patching won't get you out of the hole. Your head of product is right about the method. The best path takes the CTO's ambition and executes it the way the head of product describes.

## Why a full rewrite is especially risky for you

**1. A 20-year-old policy admin system is mostly business logic, not technology.** The code encodes rating rules, state-specific forms and filings, endorsement handling, cancellation and reinstatement rules, and edge cases added because a regulator or a large carrier demanded them in 2011. Much of it is undocumented, and the people who knew why are gone. A rewrite team has to rediscover all of it, usually by shipping bugs to carriers.

**2. The two-year estimate is not credible.** Policy admin replacements are among the most notorious failure categories in insurance software. Carriers themselves regularly blow through budgets and timelines replacing these systems, and you'd be doing it while also serving customers. Plan for two years and you'll likely face three to five, with the old system still carrying the revenue.

**3. You deliver zero value until the end.** During a rewrite you either freeze features on the old system, handing ground to competitors and frustrating customers, or you build everything twice. And "done" isn't when the new system works. It's when carriers migrate their in-force books of business, which they are slow and reluctant to do. You could run both systems for years.

**4. A rewrite doesn't fix the reasons features take months.** If the causes are missing automated tests, manual deployments, poor domain knowledge, or unclear ownership, a new stack built by the same organization will drift toward the same state. The stack is rarely the root problem.

## When your CTO would be right

A rewrite becomes defensible if several of these are true:

- The platform depends on technology that is truly end-of-life (unsupported runtime, database, or hardware) with no migration path.
- The core data model is fundamentally wrong for where the market is going, not just ugly, so nothing can be carved off without rebuilding the center anyway.
- The domain is narrower and better understood than it appears, and you have people who deeply know the rules.
- You can fund a separate rewrite team while fully staffing the existing product, and key customers are committed to migrating.

If your CTO can make that case with evidence, take it seriously. It's rare for a system that "still works and runs most of the revenue."

## What incremental has to mean to succeed

The legitimate fear behind the CTO's position is that incremental efforts stall and become a permanent half-migrated mess. That happens when modernization is squeezed in around feature work. To prevent it:

- **Define a target architecture up front.** Know what the end state looks like (domains, data ownership, APIs, hosting model) so each carve-out moves toward it.
- **Dedicate real capacity.** A stable, protected share of engineering (often 30–50% early on) goes to modernization, not "whatever's left after the roadmap."
- **Pick seams by pain and value.** Common candidates in P&C policy admin are the rating engine, document and forms generation, integrations and APIs, billing, and agent or policyholder portals. The core policy lifecycle usually goes last.
- **Put an API layer in front of the legacy system** so new capabilities are built on the modern side from day one and customers see progress immediately.
- **Pin down legacy behavior before replacing it.** Characterization tests that capture what the old system actually does let you replace pieces safely. They're also the knowledge a rewrite would have needed anyway.
- **Address "cloud-native" as a go-to-market problem too.** A hosted or SaaS offering of the current system, with modern APIs on top, can blunt competitors' messaging within months rather than years.
- **Use the work to fix retention.** Engineers often leave because they spend all their time in the old codebase. Rotating people onto modern components is one of your strongest retention tools.

## How to settle the disagreement

Don't decide by debate. Run a 90-day test:

1. **Diagnose where the months go.** Trace a few recent features and measure time spent in understanding code, testing, deployment, coordination, and rework. This tells you whether the stack is the real bottleneck.
2. **Carve out one meaningful capability** behind the existing system, with the CTO's architectural standards applied to it.
3. **Review what you learned.** If the core proves genuinely impossible to strangle, you've lost little and gained the domain knowledge and tests a rewrite would need. If it works, you have a repeatable pattern and a roadmap.

That framing gives the CTO ownership of the target architecture and the ambition, gives product continued delivery, and replaces a two-year bet with evidence you can act on within a quarter.

## Turn 2

**User:** How do I pitch this to the CTO without it sounding like I'm siding with product and shooting down his plan?

**Assistant:**

The key is that you're not choosing product's plan over his. You're proposing the safest route to *his* goal. If you believe that, and the previous answer suggests you should, the pitch is mostly about sequence and ownership.

## Before the conversation

- **Talk to him privately first.** Don't let him hear your position in a meeting with the head of product in the room. That turns it into a vote.
- **Do the diagnosis homework.** Trace two or three recent features and roughly quantify where the time went. Data about bottlenecks is neutral ground. Opinions about strategy aren't.
- **Examine your own framing.** If you walk in thinking "product is right," it will leak. Walk in thinking "the CTO has correctly identified an existential problem, and I want his fix to actually land."

## In the conversation

**1. Lead with where he's right, and mean it.**
He's correct that the platform is a strategic liability, that patching won't solve it, and that "cloud-native" competitors are a real threat. Say so explicitly, before any "but."

> "I agree with you that incremental fixes won't get us out of this. We need to end up on a fundamentally different platform. I want to talk about how we make sure we actually get there."

**2. Separate the destination from the route.**
Most of the disagreement is about route. Make that distinction out loud so he doesn't hear the proposal as rejecting the destination.

> "I'm fully bought into the target: a modern, cloud-native platform. Where I'm nervous is the path, specifically running two years with value only at the end and the old system still carrying the revenue."

**3. Frame it as risk to his vision, not flaws in his thinking.**
Name the ways rewrites die: undocumented business rules, timeline slip, feature freeze, carriers slow to migrate in-force books. Present them as threats to protect against, not arguments he missed.

> "What worries me is the board or a big customer losing patience in year two, before anything has shipped, and the whole effort getting cut. I don't want the platform you're describing to die that way."

**4. Ask questions instead of delivering conclusions.**
Let him engage with the risks rather than defend against them.

- "How would we handle the state-specific rules nobody has documented?"
- "What do we tell customers who need features in the next 18 months?"
- "What's our plan if carriers won't migrate their in-force policies on our timeline?"

If he has good answers, you learn something. If he doesn't, he'll often arrive at an incremental path himself, which is far better than being told.

**5. Give him ownership of the architecture.**
This is the most important move. The incremental approach only works with a strong target architecture and enforced standards, and that's his job.

> "I think the way to do this is that you define the target architecture, and every piece we carve off is built to it. Each quarter we're moving onto your platform, just in slices, and we can show progress the whole way."

**6. Propose the 90-day test as a joint experiment.**
It lowers the stakes. He isn't abandoning the rewrite, just agreeing to gather evidence first.

> "Can we pick one meaningful capability, like rating or documents, build it to your standards behind the existing system, and review in 90 days? If the core turns out to be impossible to carve up, we'll have learned that cheaply, and the tests and domain knowledge feed straight into a rewrite."

## Things to avoid

- **Don't mention that product proposed this.** If it comes up, acknowledge it honestly, but ground your position in your own analysis and data.
- **Don't say "strangler fig" in the first five minutes.** It can sound like a textbook rebuttal. Describe the approach concretely.
- **Don't cite industry failure statistics as a trump card.** One sentence of context is fine. Leaning on it implies he hasn't thought about it.
- **Don't force agreement in one meeting.** Leave room: "Would you think about it and we can pick it up later this week?" People often come around after reflecting, especially when they didn't feel cornered.

## If he still disagrees

Ask what evidence would change his mind, and what would change yours. That turns a standoff into a shared set of criteria. If you're still at an impasse, bring it to the CEO together as a decision with clearly laid-out tradeoffs, not as a fight you want someone to referee.

## Turn 3

**User:** What if the diagnosis shows the stack really is the bottleneck? Does that mean he's right about the rewrite?

**Assistant:**

Not automatically. If the stack really is the bottleneck, that proves the stack has to go. It doesn't yet prove it has to go all at once. The strangler approach *is* a way of replacing the stack, just in slices. So the real question becomes: **what kind of stack problem is it?**

## Be honest about what the finding changes

If the diagnosis points at the technology rather than process or knowledge, the CTO's instinct was more right than the head of product's framing. Say so to him directly. It builds the credibility you'll need for the harder conversation about *how*, and it's the fair thing to do. It also means "keep shipping features and modernize on the side" is off the table. Modernization moves from a parallel track to the main program.

## Distinguish the types of stack bottleneck

**1. Localized pain.** A few modules (say rating or document generation) are slow to change because of old frameworks or tangled code, while other areas are tolerable.
→ Strongly favors incremental. Replace the worst areas first and you get most of the benefit early.

**2. Pervasive tooling and runtime pain.** Everything is slow because of the language, build system, deployment model, or infrastructure: hour-long builds, no automated deploys, an unsupported runtime, difficulty hiring.
→ Consider **re-platforming** before rewriting: move the existing logic to a supported runtime, containerize, add CI/CD, run it in the cloud. Sometimes that's automated or semi-automated code migration. It's unglamorous, but it can remove much of the friction in months and makes later carving easier.

**3. Architectural pain in the core.** The data model and core policy lifecycle are so entangled that every change touches everything, and there's no clean seam to cut along.
→ This is where the CTO's case is strongest. Even here, a big-bang rewrite isn't the only option (see below).

**4. End-of-life risk.** The platform depends on something that will stop being supportable (hardware, database, language runtime) on a timeline you don't control.
→ This creates a deadline, which changes the calculus. It still usually argues for re-platforming first to buy time, not for betting the company on a rewrite racing the deadline.

## If it's truly type 3, rewrite smart

A core rewrite can still be staged to avoid the worst risks:

- **Rewrite by line of business or product, not all at once.** Build the new core for one line (for example, personal auto in a handful of states), put new business on it, and expand from there. Existing policies stay on the old system until they renew or migrate.
- **Run in shadow mode.** Feed real transactions through old and new systems in parallel and compare outputs (premiums, forms, and so on) before cutting over. This is how you catch the undocumented rules.
- **Carve the edges first anyway.** Even if the core needs a rewrite, pulling out rating, documents, integrations, and portals first shrinks what the core rewrite has to cover and delivers value while it's underway.
- **Buy what isn't differentiating.** Rating engines, document composition, and billing components exist as products. Rewriting commodity pieces burns time you need for the parts that make you competitive.
- **Keep a thin feature stream alive.** Protect a small team for regulatory changes and must-have customer requests so you don't lose accounts during the build.

## What the finding settles and what it doesn't

A stack-level diagnosis settles **what** has to happen: the platform must be substantially replaced, and that becomes the company's top engineering priority.

It doesn't settle **how**. The risks of a big-bang rewrite (undocumented rules, timeline slip, no value until the end, slow carrier migration) don't go away because the stack is bad. They exist *because* of the business logic and the customers, not because of the technology.

So the likely outcome is a synthesis that gives the CTO more than he'd have gotten otherwise: a committed, platform-replacement program under his architectural leadership, executed in stages that deliver value and reduce risk along the way. That's a much easier thing for both of you to take to the CEO than either original position.

## Turn 4

**User:** How do I actually run that diagnosis without it taking months or looking like I'm building a case against his plan?

**Assistant:**

Two moves solve both problems: **keep it small and time-boxed**, and **make it a joint effort with the CTO from the start**. A diagnosis you design together is shared evidence. One you run alone and present to him is a case file, whatever the results.

## Set it up together

**Invite him to co-own it.** Pitch it as groundwork for his plan, which it genuinely is:

> "Whatever path we take, we'll need a clear picture of where our delivery time actually goes. It shapes the target architecture, the sequencing, and what we tell the board. Can we spend three or four weeks getting real data on it together?"

**Agree on the questions before you see any data.** For example:

- Where does time go between "feature requested" and "feature in customers' hands"?
- How much of that is caused by the code and stack versus process, testing, deployment, or knowledge gaps?
- Is the pain concentrated in a few areas or spread everywhere?
- Why are engineers leaving?

**Agree on what the answers would mean.** Write down in advance something like: "If most delay traces to core coupling everywhere, that points toward replacing the core. If it's concentrated or mostly process, that points toward targeted work." Pre-committing protects both of you from interpreting results to fit a conclusion. It's the single best thing you can do for the diagnosis's credibility.

**Let him pick some of the features to study,** or pick them jointly. Nobody can say the sample was cherry-picked.

## What to actually do (about 3–4 weeks)

**1. Trace 5–8 recent features end to end.** This is the core of the work.
Pick a mix of sizes and product areas. For each, reconstruct the timeline from tickets, pull requests, commits, test cycles, and release records, then fill gaps with a short conversation with the engineers who built it. Categorize the time:

- Understanding existing code and business rules
- Actually writing the change
- Waiting (reviews, environments, other teams, decisions)
- Testing, especially manual regression
- Deployment and release
- Rework from bugs or misunderstood requirements

You'll often find the "months" are mostly waiting and testing rather than coding, or the reverse. Either answer is valuable.

**2. Pull basic delivery metrics from existing tools.**
No new instrumentation, just what you can extract in a day or two: deployment frequency, lead time for changes, change failure rate, and time to recover (the four DORA metrics). Add build times and test suite duration and coverage. These show whether the pipeline itself is a bottleneck.

**3. Run a code hotspot analysis.**
Combine version-control history (which files change most often) with a complexity measure. Files that are both complex and constantly changing are your real pain points. Tools exist for this, or an engineer can script a rough version in a few days. This answers "concentrated or pervasive" with data instead of opinion.

**4. Interview 8–12 engineers,** ideally a mix of tenures and teams, 30 minutes each, same questions every time:

- What slows you down most?
- Walk me through the last change that took longer than it should have.
- What would you fix first if you could?
- What makes people think about leaving?

Include one or two recent leavers if they're willing, plus any exit interview notes. Consider having someone neutral, like a respected staff engineer, conduct these so people speak freely.

**5. Check hard constraints.**
List end-of-life dependencies, unsupported versions, and security or compliance exposure. This is quick but can change the timeline conversation entirely.

## Keep it neutral in practice

- **Share raw findings weekly** with the CTO, not a polished verdict at the end. No surprises.
- **Include a staff engineer he trusts** on the working group.
- **Report data and your interpretation separately.** Let findings stand on their own before anyone says what they mean.
- **Leave room for evidence that supports a rewrite.** If the data points there, say so plainly. The process is only credible if it could have gone either way.
- **Don't let it sprawl.** Four weeks, fixed scope. A diagnosis that drags on looks like stalling, and your competitors aren't waiting.

## What you end up with

A short document, five pages or fewer, containing the feature timelines, delivery metrics, the hotspot map, interview themes, and hard constraints. Close with an interpretation the two of you work out together against the criteria you agreed on at the start.

That document becomes the foundation for the conversation with the CEO. Whatever it shows, you'll be presenting it side by side with the CTO instead of from opposite corners.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the whole thing condensed into a plan. I don't know what your diagnosis will show, so the later steps branch on the results.

## The short answer

**Commit to replacing the platform, and do it in stages.** Treat modernization as the company's top engineering priority, with the CTO owning the target architecture, but deliver it in slices that ship value and reduce risk along the way instead of one two-year bet.

## The next 90 days

**Weeks 1–2: Align privately**
- Meet the CTO one-on-one. Agree with him on the problem and the destination, raise concerns about the route, and propose a joint diagnosis.
- Brief the head of product separately. Explain that the goal is a real platform replacement, not a slower version of today, so they need to expect feature capacity to shrink.

**Weeks 2–6: Diagnose together**
- Run the time-boxed diagnosis: feature timelines, delivery metrics, hotspot analysis, engineer interviews, end-of-life check.
- Agree on the questions and what results would mean *before* looking at the data.
- Share findings weekly.

**Weeks 6–8: Decide the approach from the evidence**
- **Pain is concentrated, or mostly process and pipeline:** fix the pipeline (CI/CD, test automation) and start carving off the worst areas behind an API layer.
- **Pain is pervasive tooling or runtime:** re-platform the existing system first, then carve.
- **Pain is in the core architecture:** plan a staged core rewrite by line of business, with shadow-mode validation, while carving off the edges first.
- **End-of-life deadline:** re-platform to buy time, then proceed with whichever of the above fits.

**Weeks 8–12: Present jointly and start**
- Take one recommendation to the CEO with the CTO, grounded in the data, with honest tradeoffs, costs, and a roadmap.
- Start the first slice immediately, built to the CTO's target architecture. Early visible progress is what keeps the program funded.

## Commitments that apply whatever the diagnosis shows

- **Protected capacity.** A fixed, substantial share of engineering goes to modernization and isn't raided for the roadmap.
- **A thin feature stream.** A small team handles regulatory changes and must-have customer requests so you don't lose accounts.
- **Characterization tests before replacement.** Capture what the old system actually does before changing it.
- **Buy commodity components** where it saves time: rating, documents, billing.
- **Address "cloud-native" in go-to-market now.** A hosted offering with modern APIs can counter competitors long before the replacement is done.
- **Rotate engineers onto the new platform.** It's your best retention lever.
- **Quarterly reviews against the plan,** so the program can adjust rather than drift.

## What success looks like in a year

- The CTO and head of product are aligned behind one program.
- Several capabilities run on the new architecture and customers can see them.
- Lead time for changes is measurably shorter.
- Attrition is flattening.
- You have a credible, evidence-based roadmap for the core that the board trusts.

The single most important step is the first one: that private conversation with the CTO, going in as someone trying to make his goal succeed.

## Outcome summary (sent to Jev)

The recommendation is to commit to replacing the platform, but in stages rather than through a two-year big-bang rewrite. Modernization becomes the company's top engineering priority, with the CTO owning the target architecture, and it is delivered in slices that ship value and reduce risk along the way. The CTO is right that patching won't get the company out of the hole. The staged method is safer because a 20-year-old policy administration system is mostly undocumented business logic. Two-year rewrite estimates in this category are not credible, a rewrite delivers nothing until carriers migrate their in-force books, and a new stack doesn't fix process causes of slow delivery.

The first step is a private conversation with the CTO, agreeing on the problem and destination while raising concerns about the route. After that comes a joint, three-to-four-week diagnosis, with the questions and their implications agreed before seeing data. It would include:
- traces of five to eight recent features
- DORA metrics
- a code hotspot analysis
- engineer interviews
- an end-of-life dependency check

The approach then branches on the results:
- **Concentrated or process-driven pain:** fix the pipeline and carve off the worst areas behind an API layer.
- **Pervasive tooling pain:** re-platform first.
- **Core architectural pain:** a staged rewrite by line of business with shadow-mode validation, carving edges first.
- **End-of-life deadline:** re-platform to buy time.

The CTO and the engineering lead then present one recommendation to the CEO together and start the first slice immediately.

Whatever the diagnosis shows, the plan keeps several commitments:
- protected modernization capacity
- a thin feature stream for regulatory and must-have requests
- characterization tests before replacement
- buying commodity components
- a hosted offering with modern APIs to counter "cloud-native" competitors now
- rotating engineers onto new work for retention
- quarterly reviews

The key caveat is that even if the stack proves to be the bottleneck, that settles what must happen, not how. The risks of a big-bang rewrite remain regardless.
