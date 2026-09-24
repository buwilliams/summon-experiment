# legacy-rewrite/critical-rationalism/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:37:36.463789+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

**The incremental approach is almost certainly right for your situation, but only if it's done with the seriousness and investment your CTO is implicitly asking for.** Both of them are partly right, and the best outcome combines the CTO's ambition with the head of product's delivery method.

## Why a from-scratch rewrite is high-risk here

**1. The old system's value is in knowledge that isn't written down.** A 20-year-old P&C policy admin system encodes thousands of decisions: state-specific rating rules, form and filing requirements, mid-term endorsements, cancellations and reinstatements, audit and out-of-sequence transactions, and odd behaviors specific carriers now depend on. Much of it exists only in the code. A rewrite has to rediscover all of it before it's worth anything, and teams consistently underestimate this.

**2. You get no value until you reach parity.** A rewrite delivers nothing to customers until it can replace the old system for at least some of them. Meanwhile you either freeze the old product, which hands your competitors two years, or maintain two systems at once with a team that's already stretched.

**3. Two years is probably optimistic.** Core insurance system replacements are notorious for overruns even when carriers buy mature commercial platforms. The common failure mode is reaching month 18 with 60% of the functionality, the business losing patience, and ending up with two systems permanently.

**4. Customer migration is its own project.** Even with a finished new platform, moving each insurer's book of business, integrations, and regulatory setup is a major effort on their side. Your customers may not be willing to do it on your schedule.

**5. A rewrite doesn't fix the root causes.** If features take months because of missing tests, manual deployments, unclear domain ownership, or heavy approval processes, a new codebase will slowly develop the same problems.

## Where the CTO is right

Timid incrementalism fails too, and it's probably what your company has been doing. "Refactor a bit when we touch things" while the roadmap stays 100% features doesn't escape a hole this deep. Incremental modernization often dies as a half-finished migration that leaves you with the old system *plus* a partial new one. The CTO's instinct that you need a real break is correct. The method is what's risky.

## What serious incremental modernization looks like

This is usually called the **strangler fig pattern**: new capabilities grow around the old system and gradually replace parts of it until the core is small or gone.

- **Define a target architecture up front.** Know what "done" looks like, such as a cloud-hosted, API-first platform with separated domains for rating, policy lifecycle, billing, documents, and so on. This is where the CTO should lead.
- **Build a seam first.** Put an API and integration layer in front of the legacy system so new components and customers talk to it through defined interfaces rather than its internals.
- **Pick the first slice carefully.** Choose something with high change demand, clear boundaries, and visible customer value. Rating engines, document generation, agent or insured portals, and integration APIs are common candidates. Avoid starting with the gnarliest core transaction logic.
- **Invest in the foundations that speed up everything:** characterization tests around legacy behavior, CI/CD, and observability. These often deliver the fastest improvement in feature velocity.
- **Fund it explicitly.** Commit a real, protected share of capacity (often 30–50% for a period) with its own milestones, reported to leadership the way features are. Without this, it gets starved.
- **Don't create a two-tier team.** Rotating engineers between legacy and modern work spreads knowledge and helps retention. "The new team gets the fun work, the old team gets the pager" accelerates attrition.

## On the "cloud-native" competitive pressure

Find out what buyers actually mean by it. Usually it's some mix of hosted or SaaS delivery, faster release cycles, modern APIs, configurability without custom code, and a better UI. Several of these can be delivered well before the core is modernized. Moving to managed cloud hosting, shipping a modern API layer, and releasing a new portal can change your market story in months rather than years.

## When a rewrite could be justified

Reconsider if any of these hold:
- The underlying platform is genuinely dying (unsupported language, runtime, or database vendor) with no migration path.
- The core data model fundamentally cannot support what the business needs, such as true multi-tenancy or new lines of business, and can't be evolved.
- The system is much smaller than it seems.

A legitimate middle path is to **build a new product for a new segment** (for example, a greenfield offering for smaller carriers or a new line of business) without forcing existing customers to migrate. That gives the new platform real users and revenue early instead of betting everything on parity.

## Questions that will settle it for your case

1. Where does time actually go when a feature takes months: coding, testing, deployment, requirements, or fear of breaking things?
2. Can the system be decomposed behind APIs, or is it tightly coupled through a shared database with no seams?
3. Is the data model salvageable?
4. Are customers on-prem, hosted by you, or mixed? What would migration cost them?
5. Can the company fund two years of reduced feature output, and what happens to revenue and retention if the rewrite slips to three or four?

If the answers look typical for systems like yours, the recommendation is **incremental modernization with a bold target architecture, protected funding, and measurable milestones.** The CTO sets the destination and the head of product's approach gets you there without betting the company on a single delivery date.

## Summary (sent to Jev)

The response recommends incremental modernization, provided it is pursued with the seriousness and investment the CTO is implicitly demanding. It frames the answer as combining the CTO's ambition with the head of product's delivery method.

It argues a from-scratch rewrite is high-risk for five reasons:
- The old system holds undocumented knowledge, such as state-specific rating rules, endorsements, and carrier-dependent behaviors, that must be rediscovered.
- A rewrite delivers no value until it reaches parity.
- Two years is likely optimistic, and a common failure is ending up with two permanent systems.
- Customer migration is a separate major effort.
- A new codebase won't fix root causes like missing tests or manual deployments.

The CTO is right, however, that timid incrementalism fails and often leaves a half-finished migration.

It proposes the strangler fig pattern:
- Define a target architecture up front, led by the CTO.
- Build an API seam in front of the legacy system.
- Start with a bounded, high-demand slice like rating or portals rather than core transaction logic.
- Invest in characterization tests, CI/CD, and observability.
- Protect 30–50% of capacity with milestones reported to leadership.
- Rotate engineers so the team doesn't split into two tiers.

On competitive pressure, the response advises learning what buyers mean by "cloud-native." Hosting, APIs, and a new portal could change the market story within months.

A rewrite could be justified if the platform is dying, the data model can't evolve, or the system is smaller than it seems. A middle path is a greenfield product for a new segment.

It closes with diagnostic questions:
- Where does feature time actually go?
- Can the system be decomposed behind APIs?
- Is the data model salvageable?
- Where are customers hosted, and what would migration cost them?
- Can the company survive a slipped rewrite?
