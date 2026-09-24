# legacy-rewrite/social/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:42:37.355642+00:00

## Prompt

You are a world-class expert: a sociologist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

**Neither strategy is right as your executives have framed it. But if forced to choose, bet on incremental modernization, run with the ambition and funding of a rewrite.** The CTO's diagnosis is largely correct and his prescription is dangerous. The head of product's prescription is safer, but as usually practiced it fails quietly. Here is why, and what I'd do.

## Why a from-scratch rewrite is so risky here

**1. The old system encodes 20 years of knowledge nobody wrote down.** A policy admin system holds state-specific rating rules, filed forms, endorsement edge cases, out-of-sequence change handling, audit requirements, and fixes for disputes long forgotten. Much of it lives only in the code. Rewrite teams consistently underestimate this. The last 20% of parity takes most of the time.

**2. "Two years" is a forecast almost nobody hits.** Large rewrites commonly take two to three times their estimate. Meanwhile you face a bad choice. You can freeze the legacy product and watch customers and competitors move on. Or you can keep shipping on it, which means the rewrite chases a moving target. Either way you fund two platforms with one revenue stream.

**3. Migrating in-force policies is the hardest part.** Your customers are conservative insurers with regulators, auditors, and years of policy history. Moving that data and those contracts is a risk they will resist. A new platform nobody migrates to is a very expensive demo.

**4. The sociological problem: a rewrite splits your organization into two classes.** A "new platform" team gets the modern stack, the attention, and the future. A "legacy" team keeps the revenue alive and knows it is being phased out. The legacy group, who hold the tacit knowledge the rewrite depends on, leave fastest. You would accelerate the attrition you are trying to stop, among exactly the wrong people.

## Why "incremental" often fails too

The head of product's plan has its own common failure pattern:

- Modernization gets whatever capacity is left after the roadmap, which means almost none.
- Services get carved off without a target architecture, so you end up with the old monolith *plus* a layer of new complexity.
- The "strangler" never finishes, and you run a permanent hybrid.

When the CTO says incremental fixes will never get you out of the hole, he is probably describing this pattern accurately. He has likely watched it happen already.

## What I would recommend: incremental execution, rewrite-level commitment

**1. Define the destination.** Agree on a target architecture: domain boundaries, data ownership, integration patterns, hosting model. The CTO should own this. It gives his conviction a constructive outlet.

**2. Fund it as a protected program.** Reserve a fixed share of engineering capacity for modernization, typically 30–40%. Don't let the quarterly roadmap renegotiate it. Report progress to the CEO and board as a strategic initiative, not as tech debt.

**3. Use the renewal cycle as your migration engine.** This is P&C's structural gift to you. Most policies renew every year. That allows two moves:
- **New business first.** Write new products, lines, or states on the new platform.
- **Migrate at renewal.** Move existing policies when they renew, not in a big-bang conversion.
- **Let legacy run off.** The old system gradually handles a shrinking book.

This makes migration far more palatable for your customers and their regulators.

**4. Pick the first slice using data, not opinion.** Look for capabilities that meet three tests:
- They change often.
- Customers visibly care about them.
- They have reasonably clean boundaries.

Common candidates are rating and rules configuration, document and forms generation, product configuration, APIs for distribution partners, and billing integration. Mine your version control for "hotspots," code that changes frequently and is highly complex. That is where modernization pays back fastest.

**5. Prove it in production within about six months.** One real capability, serving real customers, on the new architecture. Nothing settles the internal argument faster than evidence, and nothing retains engineers better than visible progress.

**6. Staff it as one organization.** Rotate people between new and legacy work. Put legacy experts on the modernization teams as domain authorities, not as caretakers. The message should be "we are all migrating the platform," never "some of you are the past."

## Reframe the two symptoms driving the urgency

**Attrition.** Exit interviews rarely say "the language was old." They say:
- "I couldn't ship anything."
- "I had no say."
- "I saw no future here."

A credible modernization path with real ownership addresses all three. So does fixing build, test, and deploy pipelines on the legacy system, which is often the cheapest retention investment you can make.

**"Cloud-native" competitors.** Treat this partly as a sales narrative problem. Insurers buying on that message usually want:
- faster product launches
- configurability without vendor involvement
- modern APIs
- painless upgrades
- someone else running the infrastructure

Several of these can be delivered through managed hosting, an API layer, and better configuration tools well before your core is rebuilt. Before letting competitor marketing set your architecture, analyze your lost deals. What did buyers actually choose them for?

## When a rewrite *would* be the right call

I'd change my recommendation if one or more of these is true:

- **The platform is dying.** The runtime, database, or language is reaching end of support, or you genuinely cannot hire people to work on it.
- **The domain model is wrong for where the market is going.** For example, it cannot support multi-line products, usage-based insurance, or embedded distribution, and cannot be refactored to.
- **The system is smaller than it feels.**
- **The "rewrite" targets a different market.** If the new platform serves new customers or segments who never need to migrate, you are building a new product, not rewriting the old one. That is a different and often reasonable bet.

If none of these apply, the rewrite case rests mostly on frustration. The frustration is legitimate, but it is not a strategy.

## A note on the disagreement itself

Look closely at the structure of the conflict. Each executive's plan expands their own domain. The CTO's plan centers engineering, and the head of product's plan centers the roadmap. That doesn't make either of them wrong. It does mean this shouldn't be settled as a debate won by the more persuasive person.

Get them to agree on decision criteria and shared metrics first:
- lead time per change, by module
- percentage of revenue running on the new architecture
- regretted attrition
- win/loss rate against the cloud-native competitors

Then evaluate both plans against those criteria. In my experience, the plan that comes out of that process looks a lot like what I've described above, and both of them can own it.

## Summary (sent to Jev)

The response concludes that neither strategy is right as framed. If forced to choose, it favors incremental modernization run with the ambition and funding of a rewrite. It judges the CTO's diagnosis largely correct but his prescription dangerous, and the head of product's plan safer but prone to failing quietly.

A from-scratch rewrite is risky for four reasons. Twenty years of undocumented rules and edge cases live only in the code. Rewrites commonly run two to three times their estimate, forcing the company to fund two platforms from one revenue stream. Migrating in-force policies for conservative, regulated insurers is the hardest part. And a rewrite splits the organization, driving away the legacy experts whose knowledge it depends on. Incremental efforts, meanwhile, often starve for capacity, lack a target architecture, and never finish.

The response recommends six steps:
- Have the CTO own a target architecture.
- Protect 30–40% of engineering capacity as a board-reported strategic program.
- Use the P&C renewal cycle for migration: new business goes on the new platform first, existing policies move at renewal, and the legacy book runs off.
- Choose the first slice by data, favoring frequently changing, customer-visible, cleanly bounded capabilities and version-control hotspots.
- Prove one capability in production within about six months.
- Staff new and legacy work as one rotating organization.

It reframes attrition as a problem of shipping, ownership, and future prospects rather than an old language, and it treats "cloud-native" partly as a sales narrative worth checking through lost-deal analysis.

A rewrite becomes justified if the platform is reaching end of support, the domain model can't be refactored for where the market is going, the system is smaller than it feels, or the new platform targets a different market. Finally, the response advises having both executives agree on shared criteria and metrics before evaluating the plans.
