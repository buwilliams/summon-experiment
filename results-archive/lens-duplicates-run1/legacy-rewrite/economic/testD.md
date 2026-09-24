# legacy-rewrite/economic/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:47:54.978019+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

## Response

# Rewrite vs. Incremental Modernization: Following the Money

## The short answer

Neither proposal is right as stated, but the incremental approach is much closer. A two-year ground-up rewrite of a 20-year-old P&C policy administration system puts most of the capital at risk before any of it earns a return. It also relies on assumptions that rarely hold in this domain: that two years is enough, that customers will migrate on your schedule, and that the legacy system can coast in the meantime. The incremental approach earns returns sooner and caps your losses. Its own failure mode is spending indefinitely on a hybrid that never reduces cost.

The better option is a staged, revenue-targeted modernization funded in tranches, with explicit kill criteria. It may include a greenfield product aimed at *new* customers rather than migrating existing ones. The details follow. The numbers are illustrative, so substitute your own.

---

## 1. Start with where the money actually comes from and where it is leaking

Before comparing strategies, you need to know which of your problems actually cost money. Your business probably earns revenue in four ways:

| Revenue stream | What threatens it | How sticky it is |
|---|---|---|
| Recurring license / subscription / maintenance from existing insurers | Churn at contract renewal, pricing pressure | Very sticky. Replacing a PAS takes an insurer 2–4 years and many millions of dollars. |
| New customer wins | "Cloud-native" competitors, slow demos of modern capabilities | Most exposed |
| Implementation and professional services | Long timelines, customer frustration | Moderate |
| Upsell (new lines of business, states, modules) | Months-long feature delivery | Exposed |

The implication is that your installed base is probably not in immediate danger. Your growth is. Competitors marketing "cloud-native" mostly hurt your new-logo win rate and your pricing power at renewal. Churn will come too, but slowly. That matters because a rewrite spends heavily now to defend against a threat that mostly arrives later, while starving the feature work that protects near-term renewals.

**Data you need before committing capital:**
- **Win/loss analysis for the last 2–3 years.** How many deals were lost specifically on architecture or cloud, and how many on features, price, or implementation time?
- **Renewal pipeline for the next 36 months.** Which customers are at risk, and why?
- **Where the months go on a feature.** Break it down into design, coding, testing, customer-specific branches, and release and deployment to on-prem customers. In many legacy PAS vendors, the killer is not the old language. It is per-customer customizations, manual regression testing, and slow on-prem release cycles. None of those require a rewrite to fix.
- **The real cost of attrition.** Replacing a senior engineer who knows your rating logic costs roughly 1–2x salary in recruiting, ramp-up time, and defects. It also concentrates risk in fewer people.

If most lost deals trace to features and speed rather than architecture, the rewrite case weakens considerably.

---

## 2. The full rewrite: following the money

### Revenue generated or protected
- **Eventually:** a competitive new-logo product, lower hosting and support cost per customer, a SaaS pricing model, and possibly better margins.
- **But only after customers migrate.** Every insurer on the new platform requires a migration project: converting policy data, reproducing rating algorithms to the penny, re-validating state-filed rates and forms, and running both systems in parallel. Insurers move on their own schedules, usually timed to their contract renewals and regulatory calendars.

### Investment and operating costs
- **A dedicated rewrite team.** For example, 40–60 engineers at about $180K–$220K fully loaded, which is $8–13M per year.
- **The legacy system does not get cheaper.** You still maintain it, patch it, and handle regulatory changes (bureau circulars, state mandates) for every existing customer. That spending continues until the *last* customer migrates.
- **Double running.** Two platforms, two support organizations, and cloud hosting bills for the new system before it carries meaningful revenue.
- **Migration tooling and services.** Customers will often expect you to fund some or all of this, especially if you initiated the move.
- **Opportunity cost.** Every engineer on the rewrite is not building features customers are asking for today.

### When returns arrive
Industry experience with core-system replacements, including insurers' own PAS replacements, points to routine overruns of 1.5–3x. A realistic profile:

- **Years 1–2:** heavy spending, no new revenue, and slower legacy feature delivery.
- **Years 3–4:** first production customers, parity gaps discovered, dual running at peak cost.
- **Years 4–6:** meaningful migration volume. Legacy costs finally begin to fall.

### Risks that could wipe out the return
1. **The parity trap.** Twenty years of edge cases, state-specific rules, and customer-specific behavior are encoded in the old system, often undocumented. The rewrite keeps discovering them, and the finish line keeps moving.
2. **Legacy talent flight.** A rewrite creates a two-class organization: the "future" team and the "maintenance" team. The engineers who keep the revenue-generating system running are the ones most likely to leave, which endangers the system that funds everything.
3. **Customers decline to migrate** or demand free migration, discounts, or contractual penalties.
4. **Competitors keep shipping** while your feature roadmap stalls. Churn accelerates during the rewrite, the opposite of the goal.
5. **The CTO leaves mid-program.** Rewrites are often tied to one leader's vision, and sponsor departure is a common death point.

### Where spending grows without profit improving
- Parity chasing: building features in the new system that customers already have, which produces zero new revenue.
- Dual running that extends because the "last 20%" of customers never move.
- Cloud infrastructure scaled for a future that has not arrived.
- **Capitalized development.** Under software capitalization rules (ASC 350-40 in the US), much of the rewrite cost can be capitalized, making EBITDA look healthier than cash flow. That is legitimate accounting, but it can hide a program that is burning cash without progress. Your board should see a cash view, not only a P&L view.

---

## 3. Incremental modernization: following the money

### Revenue generated or protected
- **Continuous feature delivery protects renewals and upsell** starting in year one.
- **Each carved-off capability can earn money on its own** if you choose well. Good candidates are capabilities that are both commercially visible and technically separable:
  - A modern rating engine or product configurator, which shortens time to launch new products and states and is a common sales differentiator
  - Digital distribution APIs and portals for agents, MGAs, and embedded partners, which can be sold as a new module
  - Document generation and communications
  - Billing, if it is a known pain point
- **Earlier improvement in retention and hiring** as engineers work on modern components.

### Investment and operating costs
- A smaller modernization team, perhaps 15–25 engineers ($3–5M per year), working alongside feature teams.
- **An integration tax:** anti-corruption layers, data synchronization between old and new components, and more complex testing. This is real and often underestimated.
- Some period of running hybrid infrastructure.

### When returns arrive
- **6–12 months:** the first capability in production and the first measurable gains in delivery speed.
- **12–24 months:** sales can demonstrate modern capabilities, and faster product launches become possible.
- **Ongoing:** gradual cost reduction as legacy modules are actually retired.

### Risks that could wipe out the return
1. **Never finishing.** You end up with a permanent hybrid that costs more to run than either system alone. This is the incremental approach's signature failure.
2. **Carving the wrong things.** Modernizing technically interesting components with no revenue impact.
3. **Feature pressure cannibalizes modernization.** Every quarter, sales escalations pull people back, and modernization stalls at 10%.
4. **Insufficient answer to the "cloud-native" pitch** if nothing customer-visible changes for 18 months.

### Where spending grows without profit improving
- Integration layers that multiply rather than shrink.
- New components built but legacy modules never switched off. **Cost only falls when old code is deleted**, not when new code ships.
- "Modernization" becoming a permanent budget line with no end state.

---

## 4. Illustrative comparison

This assumes a company with $100M in revenue, a 25% EBITDA margin, and an existing R&D budget of $25M. The figures show *incremental* spending and benefits versus the status quo, in $M. They show the shape of the returns, not a forecast. Build your own version using the data from section 1.

| Year | Rewrite: extra spend | Rewrite: benefit | Incremental: extra spend | Incremental: benefit |
|---|---|---|---|---|
| 1 | –12 | –2 (slower features, lost deals) | –5 | +1 |
| 2 | –13 | –3 | –5 | +4 |
| 3 | –12 (overrun) | +1 (early migrations) | –5 | +7 |
| 4 | –10 (dual running) | +5 | –4 | +9 |
| 5 | –6 | +12 | –3 | +10 |
| **Cumulative** | **≈ –40** | | **≈ +9** | |

The rewrite may eventually have a higher ceiling, with lower cost per customer and a cleaner SaaS model. But it requires roughly $40–60M at risk before breakeven, a trough that lasts 4+ years, and a large chance of never reaching that ceiling at all. At a 25% margin on $100M, that trough represents 1.5–2.5 years of your entire profit. Few mid-sized companies can absorb that if it overruns.

---

## 5. Who should control the budget, own the results, and decide when to stop

This matters as much as the choice of strategy. In the current framing, each advocate would effectively grade their own homework. My recommendations:

- **Budget control:** treat modernization as a distinct investment portfolio approved by the CEO and CFO, and by the board if it exceeds roughly 10% of revenue. Release funding in **tranches of 6–9 months**, not a two-year commitment. Each tranche is released only when the previous one has hit pre-agreed milestones.
- **Ownership of financial results:** a single accountable executive owns the business outcomes, not just the technical delivery. That means win rate, retention, cost to serve, and time to market. This is usually a product or business-unit leader. The CTO owns technical execution. Separating these keeps the program honest.
- **Stop authority:** the CEO and CFO, advised by someone other than the program's sponsor. **Kill criteria must be written down before spending starts**, for example:
  - Milestone slip beyond 50% on any tranche
  - No legacy module retired within 18 months
  - Delivery lead time not improved by X% within 12 months
  - Legacy engineer attrition above Y%
- **Metrics reviewed quarterly, in cash terms:**
  - Cumulative spend against plan
  - Share of transactions or policies flowing through new components
  - Legacy lines of code or modules retired
  - Feature lead time
  - Win rate on deals where architecture came up
  - Legacy team attrition
  - Hosting cost per policy

---

## 6. A third approach: staged, revenue-targeted modernization with a greenfield wedge

I'd recommend combining four moves, each funded separately so they can succeed or fail independently.

**Track A: fix the delivery engine first (months 0–9, low cost, fast payback).**
Automated regression testing around rating and forms, CI/CD, consolidating per-customer customizations into configuration, and faster release trains. This often cuts feature lead time dramatically without touching the architecture. It also protects the revenue base that funds everything else, and it tells you how much of the "months per feature" problem was ever architectural.

**Track B: neutralize the "cloud" objection quickly.**
Offer a vendor-managed hosted version of the current system on a major cloud provider, with a SaaS-style contract, SLAs, and managed upgrades. It isn't cloud-native, but many insurers mostly want to stop running infrastructure and stop dreading upgrades. This can produce new recurring hosting margin within 12 months and blunts the competitive pitch while real modernization proceeds.

**Track C: targeted strangler carve-outs chosen by revenue impact.**
One or two capabilities at a time, beginning with the one that most affects deals or retention, often rating or product configuration and distribution APIs. Each carve-out has a business case, and the legacy module is actually switched off.

**Track D (optional, the highest-upside bet): a greenfield product for a *new* segment.**
Instead of rewriting for your existing customers and forcing migrations, build a modern product for a segment you don't serve well today. MGAs, small commercial, specialty lines, or embedded insurance are common candidates. This captures most of the rewrite's upside while avoiding its worst risks:
- No migration, because new customers start fresh.
- No parity trap, because the product needs to be good for *that* segment, not match 20 years of features.
- Revenue from new customers helps fund the investment.
- The new components (the rating engine, APIs) can later be strangled back into the legacy platform, and existing customers can migrate when the product is proven.

This track should be tightly scoped, funded in tranches, and killed if it doesn't win design-partner customers within about 12–18 months.

**Why this beats both proposals on returns for the capital at risk:**
- Tracks A and B produce returns within a year, protect profitability, and show whether bigger bets are needed.
- Track C compounds steadily, with the discipline of actually retiring legacy code.
- Track D offers rewrite-scale upside at a fraction of the capital at risk, and it fails cheaply if it fails.
- It gives the CTO a real path to a modern platform, and it gives the head of product continuous delivery. That makes it politically durable, which matters for a multi-year program.

A rough envelope: $6–9M per year of incremental spending, peaking in years 1–2, compared with $12M+ per year for the rewrite. That spending is spread across bets that pay back at different times, instead of one bet that pays back late or never.

---

## 7. The next 90 days

1. **Gather the data from section 1:** win/loss, renewal risk, the lead-time breakdown, and attrition cost.
2. **Have finance build a cash-based model** of all three options using your real numbers. Include an overrun scenario for each: 1.5x for incremental, 2–3x for the rewrite.
3. **Run a 90-day Track A pilot** on one product line and measure the change in lead time. It is the cheapest way to learn how much of your problem is architecture and how much is process.
4. **Scope Track B** with two or three existing customers to test demand for hosting.
5. **Identify the first carve-out** by asking sales and customer success which capability most often loses or saves deals.
6. **Agree on the governance structure and kill criteria** before approving any large budget.

One final point. Your CTO is right that pure incrementalism can become an excuse never to fix the foundation. Your head of product is right that the current system funds everything and cannot be starved. The staged approach takes both concerns seriously. It commits to a modern platform as the destination, while insisting that the business stays profitable, and that each stage of the journey earns the right to fund the next.

## Summary (sent to Jev)

The response concludes that neither proposal is right as stated, though incremental modernization is much closer. A two-year ground-up rewrite puts most capital at risk before earning anything, and it assumes the timeline will hold, customers will migrate on schedule, and the legacy system can coast. Incremental work pays back sooner, but it risks becoming a permanent, costly hybrid.

Its reasoning starts from revenue. The installed base is sticky, so the real threat is to growth: new-logo wins and upsell. A rewrite spends heavily now against a threat that arrives later. The response estimates rewrite costs of $8–13M per year, overruns of 1.5–3x, dual running, migration costs, and a parity trap of undocumented edge cases. It also warns of talent flight from the legacy team and the risk of the sponsor leaving. In its illustrative five-year model, the rewrite ends near –$40M and the incremental path near +$9M. The response notes that capitalized development can mask cash burn.

It recommends a staged, revenue-targeted program funded in 6–9-month tranches, with written kill criteria and stop authority held by the CEO and CFO. A business leader, not the CTO, would own the outcomes. The program has four tracks:

- **A:** Fix delivery through test automation, CI/CD, and consolidating customizations.
- **B:** Offer a vendor-hosted version of the current system.
- **C:** Carve out capabilities chosen by revenue impact, and actually switch off the legacy modules.
- **D (optional):** Build a greenfield product for a new segment, to be killed if it wins no design partners within 12–18 months.

For the next 90 days, it proposes gathering win/loss, renewal, lead-time, and attrition data; building a cash model with overrun scenarios; piloting Track A; scoping hosting demand; picking the first carve-out; and agreeing on governance.
