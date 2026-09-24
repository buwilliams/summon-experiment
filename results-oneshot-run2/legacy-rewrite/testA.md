# legacy-rewrite/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T12:58:55.856861+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

**Short answer: in most situations like yours, incremental modernization is the better bet.** But your CTO is right about something important, and the incremental approach fails just as often when it's done timidly. The real choice is between a well-run incremental migration and a poorly run one, more than between rewrite and refactor.

## Why a from-scratch rewrite is especially risky for a P&C policy admin system

1. **The old system is the spec.** Twenty years of policy admin code encodes state-specific rating rules, filed forms, endorsement logic, mid-term change edge cases, cancellation and reinstatement rules, and regulatory fixes nobody documented. A rewrite team discovers these one production incident at a time. This is the classic reason rewrites stall at "90% done" for years.

2. **Two years is almost certainly optimistic.** Core insurance system replacements routinely run two to three times over schedule, even with commercial platforms and large integrators. A from-scratch build by a team that is already losing its best people is harder, not easier.

3. **You pay twice during the rewrite.** The legacy system still runs your revenue, so it still needs regulatory updates, bug fixes, and customer commitments. Either you split the team, which slows both efforts, or you freeze the old product for two-plus years while competitors keep shipping.

4. **Value arrives late and all at once.** A rewrite delivers nothing to customers until cutover. Then comes the riskiest possible event: migrating live policies, in-force books, and billing history to an unproven system. Insurers are conservative buyers. A botched migration can cost you clients you'd otherwise keep.

5. **It's hard to course-correct.** If priorities, funding, or leadership change 14 months in, a half-finished rewrite is worth close to zero. A half-finished incremental migration still leaves you with working, modernized pieces.

## What the CTO is right about

Incremental modernization has its own well-known failure mode: **the strangler that never strangles.** Teams carve off a few easy edge services, the hard core stays untouched, and five years later you're running two systems plus an integration layer, which is worse than where you started. If your company has a history of "we'll clean it up later" and never doing it, your CTO's skepticism is earned.

A rewrite can also be the right call when:
- The platform is genuinely unmaintainable, with no tests, no one who understands it, and changes that routinely break unrelated things.
- The underlying technology is at real end-of-life, such as unsupported runtimes or security exposure you can't patch.
- The domain model itself is wrong for where the business is going, for example if you need to support product lines or distribution models the core data structures can't represent.
- You're willing to scope the new system narrowly, launching it for new business in one line or one state first. At that point it's really an incremental strategy anyway.

## How to make incremental modernization actually work

The head of product's approach succeeds only if it's treated as a real transformation program, not a side project:

- **Define the target architecture up front.** Set out domain boundaries (rating, quoting, policy issuance, billing, documents, claims integration), the event and API contracts between them, and the cloud platform. This is where the CTO's vision belongs.
- **Put a seam in front of the legacy system first.** An API or anti-corruption layer lets new capabilities be built outside the monolith and traffic be routed piece by piece.
- **Sequence by value and pain, not ease.** Target the capabilities where feature requests pile up or changes take months. Rating engines, product configuration, and document generation are common high-leverage candidates. Customer-facing pieces like portals and APIs also answer the "cloud-native" pitch quickly.
- **Commit real capacity.** Something like 30–50% of engineering, protected from being raided for feature work.
- **Decommission as you go.** Track how much legacy code and data has actually been retired. If that number isn't moving, you're building a second system, not replacing the first.
- **Migrate data by segment**, such as new business first or one line of business at a time, rather than as one big cutover.

## Separate the three problems you described

They have different fixes, and a rewrite doesn't automatically solve any of them.

- **Slow feature delivery:** Find out *why* first. Is it the code, missing tests, manual release processes, or approval bottlenecks? Adding automated tests, CI/CD, and environment automation around the legacy system often yields big gains within months, and you need that safety net for any migration.
- **Engineers leaving:** Ask them why. Often the cause is the lack of any credible path forward, more than old tech itself. A visible modernization program where people get to build new services can help retention faster than a two-year rewrite that most engineers expect to fail.
- **Competitors saying "cloud-native":** That's partly marketing. Buyers care about outcomes: speed to launch products, integration APIs, uptime, cost. You can compete on those well before your core is fully rebuilt, and hosting the existing system in the cloud can address some objections cheaply.

## How to settle the disagreement

Rather than debating in the abstract, run a time-boxed test of about 8–12 weeks. Pick one painful capability and deliver it outside the monolith using the target architecture. You'll learn how tangled the core really is, how fast the team can move on the new stack, and whether the seams exist. If carving anything off proves nearly impossible, that's genuine evidence for the CTO's position. If it works, you've started the migration and shipped something.

The strongest outcome usually combines both views: **the CTO's ambition and target architecture, delivered through the head of product's incremental method**, with firm commitments to retire the old system rather than live alongside it forever.

## Summary (sent to Jev)

The response recommends incremental modernization as the better bet in most situations like this one. It argues that the real choice is between a well-run and a poorly run incremental migration rather than between rewriting and refactoring.

It sees a from-scratch rewrite as especially risky for a P&C policy administration system for several reasons:

- The old system is effectively the spec, encoding undocumented rating, endorsement, and regulatory logic that a rewrite team would rediscover through production incidents.
- Two years is almost certainly optimistic.
- The company would pay twice by maintaining the legacy system alongside the new one.
- Value would arrive late, all at once, and through a risky cutover of live policies.
- A half-finished rewrite is worth close to zero if priorities change.

The response grants that the CTO is right to fear "the strangler that never strangles," where easy edges are carved off and the core is never retired. It says a rewrite can be justified when the platform is truly unmaintainable, the technology is at end-of-life, the domain model cannot support future business, or the new system is scoped narrowly enough that it becomes incremental anyway.

To make incremental work, it proposes:

- defining the target architecture up front, which is where the CTO's vision belongs
- putting an API or anti-corruption seam in front of the legacy system
- sequencing work by value and pain
- committing 30–50% of engineering capacity
- tracking decommissioning
- migrating data by segment

It advises treating slow delivery, attrition, and competitors' "cloud-native" claims as separate problems, each with its own diagnosis and fix.

To settle the dispute, it suggests an 8–12 week test that delivers one painful capability outside the monolith. It concludes by recommending the CTO's ambition delivered through the head of product's method, with firm commitments to retire the old system.
