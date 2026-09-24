# legacy-rewrite/economic/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:45:57.030371+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

**Short answer:** In most cases like yours, the head of product's strategy is the right one, but only if it's executed with the urgency and ambition the CTO is asking for. The CTO has the diagnosis right: you're in a hole, and small fixes won't get you out. The prescription, a two-year from-scratch rewrite, is the part most likely to sink you.

## Why a full rewrite is especially dangerous for a P&C policy admin system

**1. The old system encodes 20 years of knowledge nobody has written down.** Rating algorithms, state-specific forms and rules, endorsement edge cases, mid-term cancellation math, regulatory filing quirks, workarounds for specific carriers. Much of this lives only in the code. A rewrite team must rediscover all of it, and they usually find the gaps in production, on a customer's book of business.

**2. Two years is almost certainly wrong.** Rewrites of core insurance platforms routinely run 2–3x over schedule. Meanwhile the target keeps moving, because you're still maintaining and patching the old system for regulatory changes. You end up running two systems with a split team for years.

**3. Migration is the hardest part, and it's often underestimated.** Even with a finished new platform, you have to move carriers' live policies, history, and in-force business onto it. Carriers are conservative and contractually protected. Some will refuse or delay for years, leaving you supporting both platforms indefinitely.

**4. You go dark to the market.** A rewrite usually means a feature slowdown or freeze on the product that pays the bills, exactly when competitors are pressing. Customers asking for features today don't care about your 2027 architecture.

**5. It doesn't automatically fix the talent problem.** It fixes it for the rewrite team. Everyone left maintaining the legacy system now feels like a second-class citizen, and attrition there can get worse right when you need their knowledge most.

## Why incremental modernization often fails too

Your CTO's skepticism isn't baseless. Incremental efforts commonly die because they are:

- **Timid:** a few services get extracted, the hard core never gets touched, and in five years you have the old monolith *plus* a sprawl of microservices.
- **Underfunded:** modernization gets whatever capacity is left after the feature roadmap, which is to say none.
- **Directionless:** there's no target architecture, so each "carve-off" is a local decision that doesn't add up to anything.

If that's what the head of product is proposing, the CTO is right to reject it.

## What tends to work: aggressive, strangler-style modernization

1. **Define the target architecture up front,** as the CTO would for a rewrite. Know what the end state looks like.
2. **Put an API/integration layer in front of the legacy system** so new capabilities can be built outside it and old ones replaced behind a stable interface.
3. **Carve along real seams, in order of value and risk.** In P&C these are typically:
   - integrations and APIs (often the fastest customer-visible win)
   - document generation and correspondence
   - rating engine (high value, well-bounded, testable against the old system's outputs)
   - billing
   - policy core last
4. **Consider putting new business on the new platform first.** New lines of business, new states, or new customers can start on modern components, which avoids migrating legacy books until the platform is proven.
5. **Ring-fence the capacity.** A dedicated, protected modernization team (often 30–50% of engineering) with explicit milestones, not leftover time.
6. **Run old and new in parallel and compare outputs,** especially for rating. This is how you capture the hidden knowledge safely.
7. **Keep shipping customer features,** ideally building them on the new components where possible, so modernization and roadmap reinforce each other.

This approach gets you real "cloud-native" pieces to show the market within 6–12 months instead of in two years, and it retires risk continuously instead of all at once at cutover.

## When a rewrite might actually be the right call

A rewrite becomes defensible if several of these are true:

- The system truly can't be decomposed. There are no seams, and any change touches everything.
- The underlying technology is at a dead end: unsupported platform, no one hireable who knows it, vendor end-of-life.
- Your customer base is small or concentrated enough that migration is tractable.
- You can fund both platforms fully for 3+ years without starving the existing product.
- You have leaders who have successfully delivered a rewrite of this scale before.

If most of those aren't true, the rewrite is a bet-the-company move with poor odds.

## Before you decide, diagnose why features take months

"Every feature takes months" can have very different causes, and they point to different fixes:

- **No automated tests, so everything needs manual regression:** Build a test harness. This is prerequisite to *either* strategy.
- **Slow, manual release process:** CI/CD and deployment work, independent of architecture.
- **Tangled code where every change ripples:** This is a real architectural problem and favors decomposition.
- **Knowledge concentrated in a few people:** Documentation, pairing, and retention, which a rewrite would make worse in the short term.
- **Product/process bottlenecks:** Not an engineering problem at all.

It's common to find that a significant chunk of the delay is testing and deployment, which can be improved in months regardless of which path you choose.

## Bottom line

Frame the decision not as "rewrite vs. incremental" but as "how do we get to a modern platform while never stopping revenue or customer delivery?" That usually means adopting the CTO's ambition and target end state with the head of product's delivery method. If you can get both of them to co-own a funded, staged plan with a clear architecture and visible milestones, you'll also resolve the leadership tension, which is itself a risk to whichever strategy you pick.

## Summary (sent to Jev)

The response concludes that the head of product's incremental strategy is usually right, but only if pursued with the urgency and ambition the CTO wants. It says the CTO's diagnosis is correct and his prescription, a two-year from-scratch rewrite, is the part most likely to sink the company.

A rewrite is especially dangerous for a P&C policy admin system for several reasons. The old code holds 20 years of undocumented knowledge, such as rating algorithms, state rules, and cancellation math, that a rewrite team would rediscover in production. Such rewrites routinely run two to three times over schedule. Migrating carriers' in-force business is hard, and conservative carriers may resist it. Feature delivery stalls while competitors press. Attrition could worsen among engineers left on the legacy system.

The response grants that incremental efforts often fail when they are timid, underfunded, or directionless. If the head of product proposes that version, the CTO is right to reject it.

Instead it recommends aggressive strangler-style modernization:
- Define a target architecture up front.
- Place an API layer in front of the legacy system.
- Carve along seams in order of value and risk: integrations, documents, rating, billing, and the policy core last.
- Consider starting new business on the new platform.
- Ring-fence 30–50% of engineering capacity with milestones.
- Run old and new systems in parallel and compare outputs.
- Keep shipping features.

This approach promises cloud-native pieces within 6–12 months.

A rewrite may be defensible if the system can't be decomposed, its technology is at a dead end, migration is tractable, both platforms can be funded for 3+ years, and experienced leaders exist. The response also urges first diagnosing why features are slow, since testing and deployment problems are often fixable within months under either path. Finally, it advises having both leaders co-own a funded, staged plan.
