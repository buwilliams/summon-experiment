# legacy-rewrite/social/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:42:00.853374+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

**Short answer:** Your head of product is closer to right. But your CTO has correctly diagnosed the problem, and incremental modernization only works if you take that diagnosis seriously. The winning strategy is usually aggressive, funded, architecturally directed incremental replacement, not patching and not a big-bang rewrite.

## Why a from-scratch rewrite is especially risky for you

- **Twenty years of business rules live in that code.** State-specific rating, forms, endorsements, cancellation rules, and regulatory edge cases were added one customer escalation at a time, and much of it is undocumented. Rewrites routinely discover that "the spec" is the old system's behavior.
- **In-force policies are the real problem.** You can't just launch a new system. Existing policies must be serviced, endorsed, and renewed under the rules they were written under, and migrating live books of business between platforms is where insurance rewrites go to die.
- **Two years is the optimistic estimate.** Large rewrites commonly take 2–3x longer. During that time the old system still needs features and compliance changes, so you either freeze it (and lose customers to those cloud-native competitors) or chase a moving target with a split team.
- **Revenue is concentrated.** The rewrite delivers no customer value until it's nearly done, and failure is existential rather than recoverable.
- **Your customers migrate slowly anyway.** Carriers take years to switch platforms. A "finished" new system still means years of running both.

## Why the CTO isn't wrong

"Incremental" often degrades into cosmetic fixes while the core rots further. If incremental means "keep shipping features on the old architecture and refactor when there's time," the CTO is right that you'll never get out. There's never time.

So the real choice isn't rewrite vs. incremental. It's **big-bang replacement vs. strangler-style replacement with a defined target architecture**. Both end with a new platform. One gets there in slices that each ship value and each can be course-corrected.

## What good incremental modernization looks like here

1. **Define the target architecture up front.** Decide what the end state is (domain services, cloud hosting, API-first, modern data layer) so every slice moves toward it. This is where the CTO should lead.
2. **Put a facade in front of the legacy system.** An API/integration layer lets new components and customer integrations talk to a stable interface while you replace what's behind it.
3. **Carve off seams with high value and clean boundaries.** Common candidates in P&C policy admin are the rating engine, document/forms generation, customer and agent portals, integrations, and sometimes billing. Pick the first one for both customer value and technical leverage.
4. **Use the renewal cycle as your migration mechanism.** Policies renew annually, so a common pattern is to write new business, or new lines or states, on the new components and move existing policies over at renewal rather than in a single cutover.
5. **Fund it as a dedicated program**, not a percentage of sprint capacity that gets raided. Give it a stable team, a budget, and quarterly milestones with measurable outcomes (e.g., "rating for commercial auto runs on the new engine for X customers").
6. **Fix the delivery pipeline early.** Find out where the "months per feature" actually go. It's frequently regression-testing fear, manual deployment, and environment pain, which automated tests and CI/CD can improve within quarters, before any major re-architecture.

This also addresses attrition. Engineers leave because the work is miserable and career-stagnant. Putting them on building the new platform, shipping to production regularly, fixes that without betting the company.

## When a rewrite would actually be the right call

Reconsider if one or more of these is true:
- The codebase has no workable seams (e.g., everything shares one tangled database schema with logic in stored procedures and UI code, and a facade genuinely can't isolate pieces).
- The underlying technology is at end of life and you can't hire for it or run it safely.
- You're targeting a meaningfully different market (e.g., a new segment or a much simpler product) where a greenfield product for *new* customers makes sense, with no migration of existing ones.

Even then, the better form is usually "build a new product for new business" rather than "rewrite and migrate everyone."

## How to settle the debate internally

- **Measure the pain.** Break down where time goes on the last several features. That tells you whether the bottleneck is architecture, testing, deployment, or domain knowledge.
- **Ask customers what "cloud-native" means to them.** Often it's SaaS hosting, uptime, APIs, and faster configuration, some of which you can deliver well before a full re-architecture.
- **Run a 90-day proof slice.** Stand up the facade and replace one bounded capability. If it works, you have your template. If the system truly can't be decomposed, you've gathered the evidence that justifies the CTO's approach, cheaply.

Framed that way, the CTO owns the destination and the head of product owns sequencing it so the business keeps winning along the way. That's usually a more productive split than picking a winner.

## Summary (sent to Jev)

The response concludes that the head of product is closer to right but that the CTO has correctly diagnosed the problem. It recommends aggressive, funded, architecturally directed incremental replacement rather than either patching or a big-bang rewrite.

It considers a from-scratch rewrite especially risky for this business for several reasons:

- Twenty years of undocumented business rules effectively make the old system's behavior the spec.
- In-force policies must be serviced under their original rules, and migrating live books is where insurance rewrites fail.
- Two years is optimistic, since rewrites often take two to three times longer while the old system still needs changes.
- Revenue is concentrated, so failure would be existential.
- Carriers switch platforms slowly anyway, so both systems would run for years.

It grants the CTO's point that incremental work often degrades into cosmetic fixes. It reframes the real choice as big-bang versus strangler-style replacement with a defined target architecture.

The proposed approach has six parts:

- Define the target architecture up front, led by the CTO.
- Put an API facade in front of the legacy system.
- Carve off high-value, cleanly bounded capabilities such as rating, forms, portals, integrations, or billing.
- Migrate policies at renewal rather than in one cutover.
- Fund the effort as a dedicated program with quarterly measurable milestones.
- Fix the delivery pipeline early with automated testing and CI/CD.

It says this approach also reduces attrition by giving engineers meaningful work.

A rewrite becomes appropriate if the code has no workable seams, the technology is end-of-life, or the company is targeting a different market. Even then, the response prefers building a new product for new business over migrating everyone.

To settle the debate, it suggests measuring where feature time goes, asking customers what "cloud-native" means, and running a 90-day proof slice. Under this split, the CTO owns the destination and the head of product owns the sequencing.
