# legacy-rewrite/social/testC

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:43:23.730536+00:00

## Prompt

Use impression management to answer the following.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

## Response

# Using Impression Management to Decide Between Rewrite and Incremental Modernization

Impression management is the work of shaping how key audiences perceive you. It's a useful lens here because much of what's driving this debate is perception: competitors *look* more modern, engineers *feel* stuck, and leadership wants to *be seen* taking bold action. The right strategy is the one that changes those perceptions fastest and most credibly while keeping the revenue engine running.

**Short answer:** Modernize incrementally, but frame and resource it with the ambition your CTO is asking for. A from-scratch rewrite creates the worst possible impression trajectory. Incremental modernization wins if you manage how it is seen.

## 1. Map the audiences and what each needs to believe

| Audience | What they need to believe | What they currently believe |
|---|---|---|
| **Insurer customers and prospects** | "This vendor is stable, compliant, and getting more modern." | "Reliable but dated; competitors look newer." |
| **Your engineers** | "I'll build modern things here and grow my career." | "I'll maintain legacy code forever." |
| **Board and executives** | "Engineering has a credible plan with visible milestones." | "Features are slow and we're losing ground." |
| **The market** | "They're cloud-capable too." | "The other two are cloud-native; you aren't." |

## 2. Why the rewrite loses on impressions

- **Two years of invisibility.** During a rewrite, customers see little new, and the board sees spending with nothing shipped. By month 12 you look stalled to everyone.
- **Schedule slippage is near-certain.** A 20-year-old P&C policy system encodes decades of state-specific rating rules, forms, endorsements, and regulatory edge cases, much of it undocumented. Rewrites of such systems routinely run 2–3x over plan. "Two years" will become three or four, and each slip damages leadership credibility.
- **Customers are risk-averse.** Insurers fear migrations. Announcing a "new platform" invites them to ask whether they'll be forced to migrate, and to evaluate competitors while they wait.
- **Engineer optics decay.** The rewrite excites engineers at first. Later it becomes a death march while a shrinking team keeps the old system alive, which is exactly the attrition you're trying to stop.

## 3. Why incremental can also lose, and how to prevent it

The CTO's instinct is legitimate. Incremental modernization often *looks* timid and can degrade into endless patching. Manage that risk deliberately:

- **Give it a name and a destination.** Present it as a funded platform program with a published target architecture, not "tech debt work." Let the CTO own that architecture.
- **Ship a visible first carve-out within 6–9 months.** Pick a capability that customers and sales can see, such as a modern API layer, the rating engine, document generation, a billing service, or an agent/insured portal. Build it on the new stack, in front of the old system, using a strangler-fig pattern with an anti-corruption layer.
- **Move to cloud hosting early**, with managed infrastructure, CI/CD, and observability. That lets you honestly claim cloud-delivered SaaS long before every line is rewritten.
- **Keep shipping customer features**, ideally built on the new services where possible, so modernization and roadmap progress reinforce each other.

## 4. Keep the impressions truthful

Don't market "cloud-native" before it's true. Insurers run vendor due diligence, and being caught overclaiming does far more damage than looking dated. Instead, tell a verifiable progress story: "X% of transactions now run through modern services," "new API platform live," "SOC 2 on cloud infrastructure." Specific evidence beats competitors' slogans.

## 5. Manage your own position between the CTO and head of product

Avoid appearing to pick a winner. Frame your recommendation as a synthesis: **"rewrite by replacement, one capability at a time."** This approach:

- Adopts the CTO's end state and architectural standards.
- Adopts the head of product's sequencing and continued delivery.
- Adds an explicit checkpoint. If, after 12–18 months, carve-outs prove the core truly can't be decoupled, you revisit a more aggressive replacement of the remaining core, now with better knowledge of the domain logic you've extracted.

That positions you as the person who resolved the conflict rather than the person who sided against someone.

## 6. Address retention directly

Give your strongest engineers ownership of the new services, visible technical leadership roles, and permission to speak and write publicly about the modernization. This changes their story from "maintaining legacy" to "leading a platform transformation," which is a far better résumé line and a better reason to stay.

## Bottom line

The rewrite promises the best eventual impression but delivers two-plus years of bad ones and a high chance of failure. Incremental modernization, run as a named, ambitious, visibly progressing program, improves every audience's perception within the first year and keeps your revenue safe. Choose incremental, and sell it with the CTO's ambition.

## Summary (sent to Jev)

The response frames the decision through impression management, arguing that much of the debate is about perception: competitors look more modern, engineers feel stuck, and leadership wants to be seen acting boldly. It recommends incremental modernization, framed and resourced with the ambition the CTO wants.

It maps four audiences (customers, engineers, the board, and the market) and what each currently believes versus what they need to believe. It argues the rewrite loses on impressions for several reasons. It brings roughly two years of invisible progress. Schedule slippage is near-certain because a 20-year-old P&C system encodes undocumented rating rules and regulatory edge cases, so rewrites often run two to three times over plan. Risk-averse insurers may fear forced migrations and look at competitors. And engineer enthusiasm tends to decay into a death march.

It grants that incremental work can look timid or become endless patching, and proposes safeguards:

- Name it as a funded platform program with a target architecture owned by the CTO.
- Ship a visible first carve-out within six to nine months using a strangler-fig pattern with an anti-corruption layer. Candidates include an API layer, rating engine, document generation, billing, or a portal.
- Move to cloud hosting with CI/CD and observability early.
- Keep shipping customer features on the new services.

It cautions against claiming "cloud-native" before it is true, since insurers run due diligence. It recommends verifiable progress metrics instead.

It suggests presenting the plan as a synthesis, "rewrite by replacement, one capability at a time," with a checkpoint at 12 to 18 months to reconsider a more aggressive core replacement if decoupling proves impossible. For retention, it advises giving strong engineers ownership of new services, leadership roles, and permission to speak publicly about the work.
