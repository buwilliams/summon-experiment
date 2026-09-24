# critical-rationalism/legacy-rewrite/testE

Model: claude-opus-5-5 · 2026-09-24T14:46:51.205939+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I don't need to be super sure; I just want a good idea we can try now and fix if it turns out wrong. Pretend each idea is a new toy: what does it do, and who gets to play with it? Which idea would make the people at work happy, and would anybody cry? Did everybody forget about something, like snacks or a place to play? Which part should we try first, and could we try it really fast, like before lunch? And is there a third idea everybody likes better, like a swing set for the whole office?

**Assistant:**

# Short answer: incremental, but aimed at the CTO's destination

Your head of product has the right **method** and your CTO has the right **ambition**. The strategy most likely to work combines them: agree on the modern target architecture now, then get there one capability at a time while you keep shipping. That's the swing set, covered below.

---

## Toy #1: The Big Rewrite

**What it does:** Builds a shiny new system in a separate room while the old one keeps running. In two years, everyone moves over.

**Who gets to play:** A select team of engineers building the new thing. Everyone else maintains the old toy, which nobody wants to touch anymore.

**Who's happy:** The CTO, the rewrite team, and recruiters (it's a great hiring pitch) for about 12 months.

**Who cries:**
- **Customers**, when feature requests slow to a crawl for two years while competitors keep shipping.
- **The legacy team**, who become second-class citizens. This is often who quits next.
- **Everyone, in month 20**, when the team discovers that 20 years of state-specific rating rules, endorsements, forms, regulatory filings, and odd edge cases for individual insurers were never written down anywhere except the old code.

**The track record:** Full rewrites of core systems in regulated industries frequently run far over schedule. The new system has to match the old one's behavior while the old one keeps changing, so the target keeps moving. "Two years" usually means "two years until we realize it's four."

## Toy #2: Carve It Off Piece by Piece (the "strangler fig" pattern)

**What it does:** Puts a modern layer in front of the old system, then moves one capability at a time behind it until the old core shrinks to nothing, or to something small enough not to matter.

**Who gets to play:** Everyone, eventually. Engineers get to work on modern code within months, not years, and customers keep getting features.

**Who's happy:** Customers, sales, finance, and the head of product.

**Who cries:**
- **The CTO**, if this turns into "incremental" with no destination: a decade of patching that never escapes the hole. That fear is legitimate.
- **Engineers**, if the carved-off pieces are all boring edge work while the scary core stays untouched forever.

**The real risk:** Losing momentum. Incremental plans fail by stalling, not by exploding.

---

## What everybody forgot (the snacks and the place to play)

1. **Your customers' data and their migration.** The expensive part of replacing a policy admin system isn't writing code. It's moving each insurer's in-force book, history, and integrations, and getting their IT and compliance teams to sign off. Insurers are conservative buyers. Whichever strategy you choose, migration is the long pole. Plan it first.

2. **Why features actually take months.** Before blaming the code, check how work flows. Is the delay coding, or manual testing, release windows, environment contention, approvals, and fear of breaking things? Some of this is fixable in weeks with CI, automated tests, and deployment automation, regardless of strategy.

3. **Why engineers are really leaving.** Old tech is often part of it. But "we never get to build anything new," "releases are miserable," and "I'm always on call for a system nobody understands" are more specific, and more fixable. Ask. Exit interviews and the people still there will tell you.

4. **What "cloud-native" means to buyers.** Find out why you lost deals. Often it's shorthand for: you host it, you upgrade it, it has good APIs, and configuration doesn't require a services engagement. You can deliver much of that (managed hosting, a modern API layer, self-service configuration) long before the core is rewritten.

5. **The knowledge in people's heads.** Your longest-tenured engineers and support staff are the only documentation for much of the business logic. If they leave mid-rewrite, the rewrite gets much harder. Their buy-in matters more than anyone's.

6. **A safety net.** You can't safely replace behavior you can't test. "Characterization tests," which capture what the old system does today for real policies, are the foundation for either strategy and almost nobody budgets for them.

---

## What to try first, and what you can do before lunch

**You can't modernize before lunch, but you can start learning before lunch:**

- **Pull your last 10 features and map where the calendar time went.** Coding, testing, waiting for a release, rework? This takes an hour or two and will tell you more than any architecture debate.
- **Ask sales for the last five deals lost to "cloud-native" competitors** and what the buyer actually said.
- **Ask three current engineers:** "What's the single most painful part of your week?" and "What would make you stay?"
- **Put the CTO and head of product in a room and ask them to agree on one thing:** what the system should look like in five years. They probably agree more than they think. Their disagreement is about the path.

**In the first month:**

- **Build the front door:** a modern API layer in front of the old system. Everything new goes through it. This is the foundation of carving off pieces, and it gives customers something tangible.
- **Pick a first slice at the edge, not the heart.** Good candidates are document and forms generation, agent or insured portals, notifications, reporting and data export, and third-party integrations. Don't start with rating or the policy lifecycle. Those come later, once you've built the muscle and the test harness.
- **Fix the release pipeline.** Automated builds, tests, and deploys for the existing system. This speeds up features right away and helps retention faster than almost anything else.

---

## The third idea: the swing set for the whole office

**Incremental with a funded destination, plus a new-customer lane.**

1. **Agree on the CTO's target architecture** so the incremental work is heading somewhere real, not just patching.
2. **Get there by carving off capabilities** (the head of product's method), with a dedicated modernization team and quarterly milestones, such as "by Q3, all document generation runs on the new platform." That makes progress visible and hard to quietly stall.
3. **Optionally, open a new-customer lane:** launch the new core for a narrow, fresh use case, like a new line of business, a new state, or a small new insurer, instead of migrating an existing book. The new stack gets real users and real feedback early, the big migrations wait until it's proven, and sales gets its "cloud-native" story honestly.
4. **Rotate engineers** between legacy and new work so nobody is permanently stuck on the old toy, and the legacy knowledge flows into the new system.

**Who's happy:**
- **CTO:** gets a real destination and a modern stack.
- **Head of product:** keeps shipping.
- **Engineers:** get modern work now.
- **Customers:** see steady improvement without a risky cutover.
- **Finance:** revenue keeps flowing the whole time.

**Would anybody cry?** A little. You'll run two systems for a while, which costs money and patience. That's the price, and it's much cheaper than a failed rewrite.

**How you'll know if it's wrong, so you can fix it:** Track feature lead time, engineer attrition, and the share of traffic or capabilities running on the new platform. If after two or three quarters the new share isn't growing, or you find the old core is too tangled to carve at all, that's real evidence for a more aggressive rewrite of specific pieces, and you'll have the tests, API layer, and team to do it safely.

## Turn 2

**User:** When there are two systems running at the same time, how does the front door know whether to send someone to the old one or the new one?

**Assistant:**

# How the front door decides

The front door (usually an API gateway or a thin routing service) checks each request against a set of rules. Those rules answer: **"Which system owns this thing right now?"** A few kinds of rules, often combined, do most of the work.

## 1. By capability ("what are you asking for?")

The simplest rule is based on the type of request.

- "Generate a declarations page" goes to the **new** document service.
- "Endorse a policy" still goes to the **old** system.

This is how you carve off the edge capabilities first. The rule lives in the gateway's routing table: this URL or operation goes here, that one goes there. When you finish moving a capability, you change one line.

## 2. By customer ("who are you?")

Route based on which insurer (tenant) the request belongs to.

- Insurer A has moved to the new billing service, so their requests go new.
- Insurers B through Z stay on the old one.

This lets you move one friendly customer first, learn, and expand. It's also how the new-customer lane works: every request from the new customer goes to the new core.

## 3. By the record itself ("which policy is this?")

This is the most important rule for insurance, and the one people forget.

Once you start moving core capabilities, a single policy must live in **exactly one system at a time**. Otherwise you get two versions of the truth, which is dangerous with money and regulators involved. So you keep a small **ownership table**:

| Policy number | Lives in |
|---|---|
| HO-10023 | new |
| HO-10024 | old |

The front door looks up the policy and routes accordingly. Anything that touches that policy (endorsements, cancellations, billing, claims lookups) follows it.

**P&C gives you a natural migration point: renewal.** Instead of moving a live policy mid-term, write the renewal in the new system. The old term finishes in the old system, and the new term starts clean in the new one. Over 12 months, a book of annual policies drains from old to new without a big-bang cutover.

## 4. By switch or dial ("feature flags")

Put a switch in front of any rule so you can change routing without redeploying.

- **On/off:** Send document generation to the new service. If something breaks, flip it back in seconds.
- **Percentage:** Send 5% of requests to the new service, then 25%, then 100%.

This is your "try it and fix it if it's wrong" safety valve. Rollback becomes flipping a switch, not an emergency project.

---

## Two helpers that make this safe

**Shadow mode (a practice run).** Before trusting the new system, send each request to **both** systems. Customers only see the old system's answer, but you compare the two behind the scenes. If the new rating engine quotes $1,204 and the old one says $1,210, you've found a rule nobody wrote down, before any customer or regulator did. This is how you surface those 20 years of hidden edge cases.

**Keeping the two systems in sync.** Even when a policy lives in one place, other systems need to know about it. Reporting needs everything, and the old system may still handle claims for a policy the new system just wrote. So the systems publish changes ("policy HO-10023 was endorsed"), usually as events on a message queue, and a **translator** (often called an anti-corruption layer) converts between the old data format and the new one. The translator keeps the old system's quirks from leaking into your clean new design.

---

## A day in the life of one request

An agent asks to add a driver to auto policy PA-55812:

1. The request hits the front door.
2. The gateway checks the capability: endorsements are split between old and new.
3. It checks the flag: new endorsements are on for Insurer A.
4. It checks the ownership table: PA-55812 renewed last month, so it lives in the **new** system.
5. The request goes to the new system, which processes it and publishes an "endorsed" event.
6. The translator updates the old system's reporting feed so month-end reports still balance.

If step 5 had gone wrong, you'd flip the flag and route Insurer A back to the old path while you fixed it.

## One warning

The ownership table and the routing rules become **critical infrastructure**. If they're wrong, requests go to the wrong place. Keep the rules simple, version them like code, log every routing decision, and make "where does this policy live, and why?" easy for support staff to answer.

## Turn 3

**User:** What happens if the front door itself breaks? Does everybody get stuck outside?

**Assistant:**

# Yes, if you build it carelessly

The front door is a **single point of failure** by design, because everything goes through it. Before it existed, the old system could only be taken down by its own problems. Now there's one more thing that can break. So you design the door to be the most boring, reliable part of the whole setup.

## 1. Have more than one door

Run several identical copies of the gateway behind a load balancer, spread across data centers or cloud availability zones. If one copy crashes, traffic shifts to the others and nobody notices. This is standard practice and the cheapest protection you'll buy.

## 2. Keep the door dumb

The door should only **look up and forward**. It shouldn't calculate premiums, transform data, or run business logic. Every clever thing you add is another way for it to break. If someone proposes "let's just have the gateway also handle X," the answer is usually no. Put X in a service behind the door.

## 3. Don't let the door depend on something fragile

The ownership table ("which system owns this policy?") is the door's biggest dependency. If the door has to ask a database for every request and that database goes down, the door goes down with it.

- **Keep a local copy.** Each gateway instance caches the ownership table in memory and refreshes it often. If the source is unavailable, the door keeps working with slightly stale data.
- **Design for staleness.** A policy's owner changes rarely, mostly at renewal, so data that's a few minutes old is almost always correct.

## 4. Decide in advance what "safe" means when unsure

When the door can't make a confident decision, it needs a predetermined fallback. For most requests, the safe choice early on is **send it to the old system**, since that's what has worked for 20 years.

The exception is policies that already live in the new system. Sending those to the old one would create two versions of the truth. For those, it's better to **fail clearly** ("try again in a moment") than to write to the wrong place. A short, obvious outage is far better than silently corrupted policy data you discover at month-end or during an audit.

## 5. Be most careful with rule changes

In practice, gateways rarely fail because the software crashes. They fail because **someone pushes a bad routing rule**, like a typo that sends all traffic to a service that isn't ready. Protect against that:

- Treat routing rules like code: reviewed, versioned, and tested before they go live.
- Roll out rule changes gradually, starting with one gateway instance or a small percentage of traffic.
- Make rollback one command that restores the last known good configuration.

## 6. Keep an emergency side entrance

For a true emergency, have a documented, tested way to **bypass the door** and point traffic straight at the old system, the way things worked before the door existed. You hope never to use it, but you should practice it, because an untested backup plan usually fails when you need it.

## 7. Watch it closely

The door sees every request, which makes it your best early-warning system. Alert on error rates, response times, and sudden shifts in where traffic goes. If new-system traffic jumps from 10% to 90% in a minute, something is wrong even if nothing has crashed yet.

---

## Also worth knowing

- **Not everything has to go through the door.** Nightly batch jobs, bulk renewals, and data feeds often talk to the systems directly on their own schedule. That limits how much a door outage can affect.
- **Start small.** At first, route only the carved-off capabilities through the door and let everything else reach the old system as it does today. The door's importance grows as your confidence in it grows.
- **Rehearse failure.** Deliberately shut off one gateway instance in a test environment, then in production during a quiet period, and confirm traffic keeps flowing. Finding out it doesn't on a calm Tuesday afternoon is much better than finding out during a customer's renewal cycle.

**Bottom line:** A well-built front door almost never locks everybody out. The risk is real, but it's one of the best-understood problems in software, and the fixes are standard practice: multiple copies, simple logic, local caching, safe fallbacks, careful rule changes, and a tested emergency bypass.

## Turn 4

**User:** Who gets to change the routing rules, and how do they know nobody else is changing them at the same time?

**Assistant:**

# Who changes the rules, and how to avoid collisions

Treat routing rules like money: a small number of people can move them, every change is recorded, and the system itself blocks two people from moving the same thing at once.

## Who gets to change what

Not all rules are the same kind of change, so they shouldn't all have the same owner.

| Kind of rule | Example | Who changes it | How |
|---|---|---|---|
| **Capability routing** | "Document generation goes to the new service" | Platform/modernization team | Code change with review |
| **Customer rollout** | "Turn on new billing for Insurer A" | Product or customer success, with engineering approval | Feature-flag tool |
| **Policy ownership** | "PA-55812 now lives in the new system" | **No human.** The migration or renewal process updates it automatically | Automated, transactional |
| **Emergency rollback** | "Send everything back to the old system now" | On-call engineer | Pre-approved fast path |

Two principles sit behind this table:

- **Every rule has a named owner.** When someone asks "why does Insurer A's billing go to the new system?", one team can answer.
- **Humans shouldn't hand-edit the ownership table.** It changes thousands of times as policies renew, and manual edits there are how you end up with a policy in two places.

## How people avoid stepping on each other

### Keep rules in version control, not in someone's head or a console

Store capability routing rules as files in a Git repository. Changes go through pull requests, and an automated pipeline applies them to the gateways. This practice is often called GitOps. It gives you:

- **A single source of truth.** What's in the repository is what's running. Nobody can quietly change a gateway by hand.
- **Built-in collision detection.** If two people edit the same rule, Git flags a merge conflict and someone has to resolve it deliberately. Neither change silently overwrites the other.
- **One change at a time.** The pipeline applies merged changes in order, so two deploys can't race each other.
- **Review.** A second person approves every change. Most bad rules get caught here.

### Use a feature-flag tool for rollout switches

Tools built for feature flags (commercial or open source) handle much of this for you:

- **Permissions:** Customer success can flip flags for their own customers but can't touch capability routing.
- **Approvals:** You can require a second sign-off for changes to production.
- **Audit log:** Who changed what, when, and from what value to what.
- **Version checks:** If two people open the same flag and both hit save, the second is told "this changed since you opened it" rather than silently winning.

### Make ownership updates atomic

When the renewal process moves a policy to the new system, the ownership update and the policy creation should succeed or fail **together**, in a single transaction. The update should also be conditional: "set owner to *new* only if it's currently *old*." If two processes try to move the same policy, only one succeeds and the other is rejected. That rules out half-migrated policies and double moves.

## The human layer: code doesn't cover everything

Tooling prevents two people from editing the same rule. It doesn't stop two people from making separate changes that interact badly, like one team moving Insurer A to new billing while another moves Insurer A's documents on the same afternoon. For that you need some lightweight habits:

- **Announce changes** in a shared channel before and after, including what's changing, for whom, and how to roll it back.
- **Keep a change calendar** so big moves don't overlap.
- **Respect insurance freeze windows.** Don't change routing during month-end close, heavy renewal periods (January 1 is huge in P&C), or a customer's major renewal cycle. Agree on these windows with customers ahead of time.
- **Move one thing at a time per customer.** If something breaks, you want to know exactly which change caused it.

## The emergency exception

When production is on fire, nobody should wait for a pull request review. Give on-call engineers a pre-approved rollback: a single command or switch that restores the last known good configuration. Two rules keep this from becoming a loophole:

1. It can only **go back** to a previously approved state, never introduce something new.
2. Every use is logged and reviewed afterward, and the fix gets committed back into version control so the repository and reality match again.

## Why this matters more in insurance

Regulators and insurer auditors may ask how a specific policy was processed and why. If you can answer "on March 3, this policy's renewal was routed to the new system under rule change #412, approved by these two people," that's a strong answer. An audit trail for routing isn't just good engineering practice. It becomes part of your compliance story.

**Bottom line:**
- **Clear ownership** decides who changes what.
- **Version control and flag tools** stop simultaneous edits from colliding.
- **Atomic updates** protect the ownership table.
- **A change calendar and freeze windows** keep separate changes from surprising each other.

## Turn 5

**User:** What should we do?

**Assistant:**

# What I'd do

**Decision:** Modernize incrementally toward a clearly defined modern platform. Don't approve a from-scratch rewrite. Don't approve open-ended patching either. Fund it as a real program with a destination, a dedicated team, and quarterly milestones, and revisit the decision with evidence after two or three quarters.

The case in one sentence: the old system carries your revenue and 20 years of undocumented insurance rules, so the safest way to replace it is gradually, with the ability to test and roll back every step.

---

## This week: learn before committing

1. **Map where feature time goes.** Take the last 10 features and trace the calendar: coding, testing, waiting for releases, rework. This tells you whether the bottleneck is the code, the process, or both.
2. **Ask why you're losing deals.** Get specifics from sales on the last five losses to "cloud-native" competitors. Was it hosting, upgrades, APIs, configurability, or price?
3. **Ask why engineers leave.** Talk to three or four current engineers and review recent exit interviews. What would make them stay?
4. **Align the CTO and head of product on the destination.** Ask them to agree on what the platform should look like in five years. Then frame the plan as the CTO's destination reached by the head of product's path. Both of them win something real, which matters because you need both committed.

## First 90 days: build the foundation and ship one real slice

- **Fix the release pipeline for the existing system:** automated builds, tests, and deploys. This speeds features up and improves morale fastest.
- **Start characterization tests** that capture how the old system behaves today for real policies, starting with the areas you'll carve off first.
- **Stand up the front door:** a thin, redundant API gateway with routing rules in version control, a feature-flag tool, and a tested emergency bypass.
- **Carve off one edge capability.** Document generation, portals, notifications, or reporting are good candidates. Run it in shadow mode, roll it out with flags, and put it into production for at least one customer.
- **Form a dedicated modernization team** and rotate engineers through it so legacy knowledge flows into the new platform and nobody is stuck on old work forever.

**The 90-day test:** one capability running in production on the new platform, releases measurably faster, and a working rollback you've actually practiced.

## First year: work toward the core

- Carve off two or three more capabilities, moving from the edges toward the core.
- **Offer modern hosting and APIs** to address what buyers mean by "cloud-native" before the core is finished.
- **Consider a new-customer lane:** launch a narrow new use case, like a new line of business, a new state, or a small new insurer, directly on the new core.
- **Plan core migration around renewals** so policies move to the new system naturally at term end, with an ownership table and atomic updates.
- Agree with customers on freeze windows around month-end and major renewal periods.

---

## How you'll know it's working

Track four numbers every quarter:

| Metric | Direction you want |
|---|---|
| Feature lead time (idea to production) | Falling |
| Engineer attrition | Falling |
| Share of capabilities or traffic on the new platform | Rising steadily |
| Win rate against cloud-native competitors | Rising |

## When to change course

- **New-platform share stalls for two quarters:** the program is losing momentum. Add people or narrow the scope, but don't let it quietly die.
- **The old core proves too tangled to carve:** rewrite that specific piece more aggressively. By then you'll have the tests, front door, and team to do it safely.
- **Lead time falls sharply from pipeline fixes alone:** the code was less of the problem than it looked. Keep modernizing, but with less urgency and budget.

## The biggest risks to manage

- **Losing momentum.** Incremental programs usually fail by stalling, not by exploding. Visible milestones and executive attention prevent it.
- **Running two systems gets expensive.** Accept it as the price of safety, but keep pushing the old system's share down.
- **Losing your veteran engineers.** They're the only documentation for much of the business logic. Invest in keeping them and involve them in the new work.

**Bottom line:** Start this week by learning where the time actually goes, fix the release pipeline and build the front door within 90 days, ship one real capability on the new platform, and let the results tell you how fast to push from there.

## Outcome summary (sent to Jev)

The recommendation is to modernize incrementally toward a clearly defined modern platform, rejecting both a from-scratch rewrite and open-ended patching. It should be funded as a real program with a destination, a dedicated team, and quarterly milestones, and the decision should be revisited with evidence after two or three quarters. The reasoning is that the old system carries the revenue and 20 years of undocumented insurance rules, so it is safest to replace it gradually, testing and rolling back each step. Rewrites of regulated core systems tend to overrun as the target keeps moving, while incremental efforts fail mainly by stalling.

This week the company should:
- map where calendar time went on the last ten features
- ask sales why the last five deals were lost to "cloud-native" competitors
- ask engineers why they leave and what would keep them
- have the CTO and head of product agree on a five-year destination, framed as the CTO's destination reached by the head of product's path

Within 90 days it should:
- fix the release pipeline
- start characterization tests
- stand up a thin, redundant API gateway with version-controlled routing rules, feature flags, and a tested emergency bypass
- form a rotating modernization team
- carve off one edge capability (documents, portals, notifications, or reporting), run it in shadow mode, and put it into production for at least one customer

Over the first year it should:
- carve off more capabilities, moving toward the core
- offer modern hosting and APIs
- consider a new-customer lane on the new core
- migrate policies at renewal, using an atomic ownership table and customer-agreed freeze windows

Progress should be tracked through lead time, attrition, new-platform share, and win rate. If share stalls, the program needs more people or a narrower scope. If part of the core is too tangled to carve, that piece should be rewritten aggressively. If pipeline fixes alone cut lead time sharply, the company should keep modernizing with less urgency. The main risks are lost momentum, the cost of running two systems, and losing veteran engineers.
