# legacy-rewrite/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T12:59:30.524173+00:00

## Prompt

You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

# Short answer: modernize incrementally, but more aggressively than your head of product probably means

For a 20-year-old core system that carries most of your revenue, a from-scratch rewrite is the higher-risk bet by a wide margin. Your CTO's diagnosis is largely correct, though. Timid incrementalism fails too. The winning strategy is incremental in method and ambitious in scope.

## Why the full rewrite is the riskier bet

**1. The two-year estimate is almost certainly wrong.** A P&C policy admin system has two decades of business logic in it: state-specific rules, rating quirks, forms, endorsements, cancellation and reinstatement edge cases, regulatory fixes, and customer-specific workarounds. Much of it is documented nowhere except the code. In a rewrite, the old system *is* the spec, and you find its requirements by missing them. Large core-system replacements in insurance routinely run 2–3x over schedule. That comes from the domain, not from your team.

**2. You pay twice while you build.** Either you freeze features for two-plus years while competitors ship and customers get impatient, or you maintain both systems and split your team. Split teams usually produce a second-class "legacy" group. Those engineers leave, and the knowledge you need for the rewrite leaves with them.

**3. You end up incremental anyway.** Finishing the new platform doesn't finish the job. Each carrier has a book of in-force policies, integrations, and custom configurations to convert, and carriers migrate slowly and cautiously. Customer migration will be gradual whether you like it or not. The real choice is whether you take on that risk continuously from the start or all at once at the end.

**4. "Cloud-native" is a marketing frame, not a buyer requirement.** Carriers buy outcomes: launching a product or rate change quickly, clean APIs, reliable SaaS operations, lower IT burden. You can deliver many of these (managed hosting, an API layer, faster configuration) well before any core is replaced.

## Why your CTO still has a point

Incremental modernization has its own common failure: the strangler that stalls. Teams carve off the easy edges (a portal, some reporting, a notification service), declare progress, and never touch the tangled core. Three years later you have the old monolith plus a ring of new services, and more complexity than when you started. If "incremental" means modernization squeezed into leftover capacity between feature requests, the CTO is right that it will never get you out.

## What a strategy that works looks like

**Diagnose before you prescribe.** Find out why features take months. Common causes include no automated tests (so every change requires fear-driven manual QA), slow manual releases, tight coupling in a few modules, or knowledge held by three people. Some of these are cheap to fix and pay off within months, regardless of the long-term strategy.

**Define a target architecture first.** The CTO should own a clear picture of the end state: domain boundaries, data ownership, integration patterns. Incremental work without a destination is just drift.

**Sequence by value and pain, and go for the core early.** In P&C, product definition and rating is often the highest-leverage domain to extract first, because speed-to-market for products and rates is what carriers feel most. Billing, document generation, and integrations are also common candidates. Pick at least one early slice that proves you can extract something hard, not just something peripheral.

**Fund it as a program, not a side project.** Commit a fixed share of capacity, typically 30–40%, protected from feature pressure. Use product-aligned teams that own both old and new code in their domain, so no one is stuck on the legacy side.

**Decommission as you go.** Count a slice as done only when the old code path is turned off. Track the percentage of transactions running through new components, and track lead time for changes. These are your real progress metrics.

**Set decision gates.** Review at 6 and 12 months. If extraction shows that a particular core module truly can't be untangled, a targeted rebuild of *that module* becomes reasonable, and you'll be making the call with evidence instead of conviction.

## When I'd change my answer

A rewrite, or a parallel new product, becomes more defensible if:

- the codebase is smaller or simpler than "20-year core system" suggests,
- the underlying technology is unsupported, or you literally cannot hire people to work on it,
- the market has shifted so much that the old domain model is wrong, not just old, or
- you target a new segment (say, small carriers or a new line) with a greenfield product and keep existing customers on the modernizing platform. That is a legitimate hybrid, not a replacement.

## Resolving the disagreement

Your CTO and head of product agree on the most important thing: the status quo is fatal. They disagree on method. Give the CTO ownership of the target architecture and the technical ambition, and give product ownership of sequencing by customer value. Then hold the whole program to one measurable outcome, such as cutting lead time for a typical feature from months to weeks within 18 months. That turns a debate about beliefs into a plan you can track.

## Summary (sent to Jev)

The response recommends modernizing incrementally, but more aggressively than the head of product likely intends: incremental in method, ambitious in scope. It considers a from-scratch rewrite the far riskier bet. Twenty years of undocumented P&C business logic makes the two-year estimate almost certainly wrong, and such replacements routinely run two to three times over schedule. The company would also pay twice during the build, either freezing features or splitting teams into a legacy group whose engineers, and their knowledge, leave. Migrating carriers would be gradual anyway. And "cloud-native" is a marketing frame, since carriers buy outcomes such as speed-to-market, clean APIs, and reliable SaaS, many of which can be delivered before the core is replaced.

The response grants the CTO a point: incrementalism often stalls when teams carve off easy edges and never touch the core, especially if modernization gets only leftover capacity. To avoid this, it proposes several steps:

- Diagnose why features take months, since causes like missing tests or slow releases may be cheap to fix.
- Have the CTO define a target architecture.
- Extract a hard, high-value domain early, such as product definition and rating.
- Protect 30–40% of capacity with product-aligned teams owning old and new code.
- Count a slice done only when old code is turned off, tracking transaction share and lead time.
- Hold decision gates at 6 and 12 months, allowing targeted module rebuilds if evidence warrants.

A rewrite becomes more defensible if the codebase is simpler than assumed, the technology is unsupported or unstaffable, the domain model is wrong, or a greenfield product targets a new segment. Finally, the CTO should own architecture and product should own sequencing, with a shared goal like cutting feature lead time to weeks within 18 months.
