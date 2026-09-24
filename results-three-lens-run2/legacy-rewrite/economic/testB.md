# legacy-rewrite/economic/testB

Model: claude-opus-5-5 · 2026-09-24T15:26:00.978870+00:00

## Turn 1

**User:** You are a world-class economist who studies how firms make profits.

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

**Assistant:**

# Short answer: Your head of product is closer to right, but your CTO has correctly identified the problem.

The CTO is right that you're in a hole and that polishing won't get you out. The CTO is probably wrong that a from-scratch rewrite is the way out. The winning strategy is usually aggressive incremental modernization: funded, time-boxed, and measured like a real program rather than done as side work between features.

Here is the reasoning from the perspective of how your firm actually makes money.

## 1. Your profit engine is the installed base, and a rewrite puts it at risk

P&C policy administration is a high-switching-cost market. Insurers take years to select and implement a core system, and they almost never leave casually. That lock-in is your moat, and it funds everything else.

A rewrite hurts that moat in two ways:

- **It stalls feature delivery for two or more years.** Customers see a vendor that stopped listening. Their requested features stop arriving just as competitors are marketing agility.
- **It forces a migration event on every customer.** Moving an insurer onto a new platform is itself a re-platforming decision. That is exactly when a CIO asks, "If we have to migrate anyway, why not run an RFP?" You would be manufacturing the switching moment your competitors cannot create on their own.

The "cloud-native" competitors mainly threaten your new sales. A big-bang rewrite would make them a threat to your existing revenue too.

## 2. The economics of the two options are asymmetric

Think of each option as a stream of cash flows.

- **Rewrite:** Large costs up front, near-zero benefit until cutover, and a schedule-risk distribution with a fat right tail. "Two years" for replacing a 20-year-old system in a regulated domain commonly becomes four or more. The old system encodes two decades of state-specific rating rules, endorsements, filings, and edge cases that nobody fully remembers. Reaching feature parity is the hidden iceberg. Meanwhile you pay to run two platforms.
- **Incremental:** Benefits start arriving within months. Each carved-off capability can be stopped, redirected, or accelerated based on what you learn. That flexibility is real option value, and it is worth a lot when uncertainty is high, as it is here.

Both paths might cost a similar amount in total. But risk-adjusted, and discounted to today, incremental almost always wins unless the old architecture literally cannot support the business you need to be in.

## 3. When the CTO would be right

A rewrite, or more precisely a new product, is justified if one of these is true:

- **The data model or tenancy model blocks the business model.** For example, you need multi-tenant SaaS economics to be profitable, and the current system can't get there without rebuilding its core.
- **The installed base is going to erode anyway.** If you are already losing renewals because of the platform, the "protect the base" argument weakens.
- **You are targeting a different segment.** Examples include MGAs, insurtechs, small carriers, or new lines where requirements are simpler.

Even then, the better move is usually a greenfield product for the new segment, run alongside the incremental modernization of the core. That is the classic response to disruption: attack the new market with a new product without abandoning the customers who pay the bills today.

## 4. Why incremental efforts often fail, and how to avoid that

The CTO's skepticism is earned. Incremental modernization frequently turns into theater: a thin API layer, one microservice, and then the effort quietly dies, leaving you with two legacies. To prevent that:

1. **Diagnose where the months actually go.** Slow delivery is often caused by missing automated tests, manual deployment, environment bottlenecks, and knowledge concentrated in a few people, not by the language or stack. Fixing CI/CD and test coverage can halve cycle time without touching architecture.
2. **Put a facade in front of the old system.** A clean API and integration layer lets new capabilities attach at the seams (the "strangler fig" pattern).
3. **Sequence by value and coupling.** Carve off capabilities that customers care about and that are relatively separable. Likely candidates are rating, document generation, billing, customer and agent portals, and integrations. Leave the deepest policy core for last, if you replace it at all.
4. **Ring-fence capacity.** Dedicate a fixed share of engineering to modernization, say 30–40%, protected from roadmap pressure. This keeps it from becoming leftover work.
5. **Set milestones with kill criteria.** Track lead time for changes, the share of new features built on the modern stack, and legacy code retired. If these aren't improving within 12–18 months, revisit the strategy on evidence.

## 5. The talent problem supports the incremental path

Engineers leave because they're stuck maintaining something with no future. A credible modernization program where people ship modern code into production within months retains talent. A two-year rewrite team that ships nothing to customers tends to burn out too, and the engineers left maintaining the old system feel like second-class citizens.

## 6. What customers are actually buying

Insurers don't buy "cloud-native." They buy faster time to market for products and rate changes, regulatory compliance, easy integrations, reliability, and lower total cost. "Cloud-native" is marketing shorthand for those outcomes. Deliver the outcomes incrementally, and move hosting to the cloud as part of the program, and you neutralize the competitors' message without betting the company.

## Bottom line

Take the CTO's urgency and the head of product's method. Modernize incrementally, but fund it seriously, sequence it deliberately, and measure it hard. Reserve greenfield building for a new segment or product rather than a wholesale replacement of the system that pays your salaries.

## Turn 2

**User:** How can I tell whether our data model or single-tenant setup actually blocks us from getting to SaaS economics, or whether the CTO is just assuming it does?

**Assistant:**

# Turning the CTO's belief into a testable claim

The useful move is to stop debating architecture and start measuring unit economics. "Single-tenant blocks SaaS economics" is an empirical claim about costs. You can check it.

## 1. Define what "SaaS economics" means for you

Get agreement on target numbers first, or the argument will never end:

- **Gross margin** on recurring revenue. Many vertical SaaS firms aim for 70–80%. Core insurance systems often run lower because of services and hosting intensity.
- **Cost to serve per customer per year**: hosting, operations, support, upgrades.
- **Time and cost to onboard** a new customer.
- **Time and cost to upgrade** a customer to the latest release.
- **Target segment ACV** (annual contract value). This matters more than people expect; see step 4.

## 2. Break down today's cost to serve by root cause

For each customer, or a representative sample, estimate where the money goes. Then attribute each cost to its cause:

| Cost driver | Caused by single-tenancy itself? | Fixable without a rewrite? |
|---|---|---|
| Duplicated infrastructure (separate DBs, servers per customer) | Yes | Partly: containers and right-sizing reduce the floor |
| Manual provisioning, deploys, patching | No, caused by lack of automation | Yes, with infrastructure-as-code and CI/CD |
| Different customers on different versions | No, caused by release discipline | Usually |
| Per-customer code branches and custom code | No, caused by customization practices | Hard, but it's a product and data model issue, not tenancy |
| Long, risky upgrades | Mostly schema and customization | Depends on data model |
| Support load | Mostly product quality | Yes |

In most legacy vendors, the bulk of cost to serve lands in the "not caused by tenancy" rows. If that's true for you, the CTO has the diagnosis wrong: the problem is operations and customization, not architecture.

## 3. Model the counterfactual: an automated single-tenant platform

Estimate what your margins would look like if you kept isolated per-customer environments but fully automated them, with one codebase, one version for everyone, automated provisioning, and fleet-wide upgrades.

- If that gets you near your margin target, **multi-tenancy isn't necessary**. Many successful vendors in regulated industries run isolated per-customer environments, and insurers often prefer isolation for data security, residency, and regulatory reasons.
- If automated single-tenant still misses the target by a wide margin, the CTO has a real point.

## 4. Check the tenancy cost floor against your target segment's ACV

This is where single-tenancy actually bites. Every isolated environment carries a minimum cost for compute, databases, monitoring, and operations overhead.

- If your target customers are mid-to-large carriers paying substantial annual fees, a per-tenant floor is a rounding error.
- If your growth strategy depends on small MGAs or insurtechs with small contracts, the floor can consume the margin.

Run the arithmetic: minimum annual cost per tenant divided by the target segment's ACV. If that ratio is small, tenancy isn't your constraint. If it's large, it might be, but only for that segment. That points toward a separate product for small customers, not a rewrite of the core.

## 5. Test the data model directly

These questions reveal whether the architecture is genuinely hostile to operating at scale:

- **Can every customer run the same codebase and version?** If not, why not? Custom code forks are the real enemy of SaaS economics, far more than separate databases.
- **Are products, rates, rules, and forms defined as configuration or as code?** If adding a new product for a customer requires engineers to change code, you can't scale onboarding.
- **Where does business logic live?** Logic buried in stored procedures and per-customer schema variations makes upgrades and automation very hard.
- **Can you change the schema without breaking customers?** Look at how painful recent migrations were.
- **How long does an upgrade take per customer?** Days is healthy. Months signals deep structural problems.

## 6. Run cheap experiments before making expensive decisions

Short technical spikes, a few weeks each, give you evidence:

- **Provisioning test:** Stand up a new customer environment from scratch, time it, then automate it. If it drops from weeks to hours, tenancy was not the problem.
- **Fleet upgrade test:** Upgrade two or three customers to the same version using an automated process. Record what breaks. The failures tell you whether the obstacle is customization, schema, or operations.
- **Configuration test:** Ask the team to add a new product or line for a hypothetical customer using only configuration. Where they have to write code, you've found data model limits.

## 7. Check what customers actually demand

Talk to sales, and to prospects you lost. Did any deal fail because the system wasn't multi-tenant? Or because of implementation time, price, missing features, or perceived age? Buyers in insurance often actively ask for isolated environments. If no lost deal traces to tenancy, the market isn't asking for it.

## 8. Ask the CTO for a falsifiable claim

Frame it collaboratively: "What evidence would convince you single-tenancy isn't the blocker? And what would convince me it is?" Agree on the thresholds up front, such as a margin gap, a per-tenant cost floor, or upgrade times, then run the analysis together.

**The CTO is probably right if** automated single-tenant still misses margin targets, the target segment's ACV can't absorb the per-tenant floor, or customer-specific code and schema divergence can't be unwound.

**The CTO is probably assuming if** most cost to serve comes from manual operations, version sprawl, and customization practices. Those problems are real, but you fix them with automation, release discipline, and moving customization into configuration, not with a rewrite.

This analysis usually takes a small team six to ten weeks. That's cheap insurance before committing to a multi-year rebuild.

## Turn 3

**User:** If the analysis shows a lot of per-customer custom code, how do we realistically unwind it without upsetting the customers who paid for those customizations?

**Assistant:**

# Unwinding custom code without breaking customer trust

The key insight is that customers paid for **outcomes**, not code. A carrier that paid for a custom Texas homeowners rating tweak cares that its rates are correct, filed, and compliant. It does not care whether that behavior lives in a code branch or in configuration. If you preserve the outcome and make their life better in the process, most customers will accept, and often welcome, the change.

## 1. Inventory and classify every customization

Build a complete catalog. For each customization, record what it does, which customer or customers have it, when it was built, who paid, and whether it's still used.

Instrument the code to measure actual usage. In most legacy systems, a large share of customizations turn out to be dead: built for a product line the customer discontinued, a regulation that changed, or a person who left.

Then sort everything into categories:

| Category | What it looks like | What to do |
|---|---|---|
| **Dead** | No usage in 12+ months | Retire, with notice |
| **Duplicated** | Several customers have near-identical custom versions of the same thing | Build one standard, configurable feature and migrate everyone to it |
| **Generalizable** | One customer's need that others would plausibly want | Absorb into the core product |
| **Regulatory or market variants** | State-specific rules, filing requirements | Move into data-driven configuration (rules tables, rating tables) |
| **Truly unique** | Legitimately specific to one customer's business | Move to a supported extension point (APIs, plug-ins, rules engine) outside the core |
| **Unique and low value** | Rarely used, hard to support | Negotiate retirement or replacement |

You'll typically find that the duplicated and generalizable categories are larger than expected. Twenty customers with "custom" billing logic are often expressing four or five underlying patterns.

## 2. Build the landing zones before asking anyone to move

You can't ask customers to give up custom code until there is somewhere better for that behavior to live. That means investing in:

- **Configuration capabilities:** product definitions, rating tables, rules, forms, and workflows that can be changed without code.
- **Extension points:** stable APIs, event hooks, and a plug-in or rules layer where genuinely unique logic can live without forking the core.
- **Standard features** that replace the most common clusters of customization.

This is also your modernization program. Each landing zone is a capability you carve off from the legacy core. The unwinding and the modernization are the same work.

## 3. Preserve behavior exactly and prove it

In insurance, customizations often touch rating, policy issuance, and filed forms, where regulators care about exact behavior. A migration that changes a premium by a few dollars can create a compliance problem.

- **Run old and new side by side.** Push historical and live transactions through both the custom code and the new configuration and compare outputs: premiums, forms, documents, billing schedules.
- **Treat any discrepancy as a defect** until it's explained. Either the old code had a bug the customer is relying on, or the new configuration is wrong. Both need a deliberate decision.
- **Share the comparison results with customers.** Showing a carrier that thousands of their policies produced identical results under the new configuration is the most persuasive argument you have.

## 4. Get the economics of the conversation right

The savings from unwinding custom code accrue mostly to you: lower maintenance cost, faster releases, cheaper upgrades. So you should bear most of the migration cost.

- **Do the migration at your expense.** Asking customers to pay to lose something they paid for is a nonstarter.
- **Share the gains.** Offer faster access to new releases, reduced maintenance fees, price stability at renewal, or credits.
- **Make the benefit concrete.** "You'll get new features every quarter instead of waiting 18 months for a custom upgrade" is compelling to a carrier that has been stuck on an old version.
- **Price what remains unique.** If a customer insists on keeping bespoke logic that can't fit an extension point, it's legitimate to charge a premium support fee that reflects the real cost of maintaining it. This turns a hidden subsidy into a visible choice, and many customers will choose the standard path.

## 5. Check the contracts early

Before talking to customers, have legal review:

- **Maintenance obligations.** Some contracts may commit you to supporting specific functionality.
- **IP ownership.** Some customers may own the custom code they paid for, which affects whether you can generalize it into the product.
- **Renewal dates.** Renewals are natural moments to renegotiate terms and schedule migrations.

This tells you where you have flexibility and where you need to negotiate.

## 6. Sequence the rollout deliberately

- **Start with dead code.** It's low risk, builds momentum, and immediately shrinks the codebase.
- **Pick friendly pilot customers next.** Choose customers with good relationships who are frustrated by slow upgrades. Their success stories and references will make later conversations easier.
- **Consolidate duplicated customizations** in batches, one standard feature at a time.
- **Tie remaining migrations to renewals and upgrades** so the change feels like part of a natural cycle, not a forced event.
- **Leave the most complex, highest-value customers for last,** when your tooling, landing zones, and track record are strongest.

## 7. Frame it as a partnership, not a takeaway

How you describe the change matters a lot:

- **Don't say:** "We're removing your customizations."
- **Do say:** "We're moving your specific requirements onto a supported part of the platform, so they'll survive every future upgrade and you'll get new releases as soon as they ship."

Consider a customer advisory group to help design the standard features that replace common customizations. Customers who shaped the replacement are far more likely to adopt it, and they often push other customers toward it too.

## 8. Stop creating new custom code

None of this works if sales keeps selling forks. Change the rules going forward:

- **New requirements go into configuration, extension points, or the core roadmap,** not customer-specific branches.
- **Custom work requires executive approval** and carries explicit pricing for long-term maintenance.
- **Align sales incentives** so reps aren't rewarded for deals that create permanent engineering liabilities.
- **Track the customization count** as a metric the leadership team reviews. It should fall every quarter.

## What realistic success looks like

You won't get to zero customization, and you shouldn't try. The goal is that every customer runs the same core codebase and version, differences live in configuration or in supported extensions, and upgrades roll out to the whole customer base in days rather than months.

Expect this to take two to three years for a system of your age, running in parallel with your broader modernization. It's slow, but each migrated customer immediately lowers your cost to serve and speeds up your releases. That makes it one of the highest-return investments in the whole program.

## Turn 4

**User:** What do we do if one of our largest customers flat-out refuses to migrate off their custom code, even with the migration and credits paid by us?

**Assistant:**

# When a major customer won't migrate

A refusal from a large customer is not a dead end, but it changes the problem. You're no longer running a migration; you're in a negotiation with a party that has real leverage. The goal is to make sure one customer can't hold your entire platform strategy hostage, without damaging a relationship that matters to your revenue.

## 1. Find out what the refusal is actually about

"No" is information. Before deciding anything, understand the real reason. Common ones:

- **Risk aversion.** Their system works, and someone's career depends on it not breaking. A migration is all downside for the person who approves it.
- **Regulatory anxiety.** They worry about refiling rates or forms, or about auditors questioning any change.
- **Internal capacity.** They don't have the staff to test and validate, even if you do the work.
- **Distrust.** Past upgrades went badly, so they don't believe this one will go smoothly.
- **Leverage.** They know they're large and see refusal as a way to extract concessions.
- **A genuine gap.** Your standard platform really doesn't do what their custom code does.

Go above the working level. Meet with their CIO or COO, ideally with your CEO present. The person refusing is often a mid-level owner protecting stability, and the executive view may be very different.

Each cause has a different remedy. Risk aversion calls for parallel running and guarantees. Capacity calls for you doing their testing. Distrust calls for a small pilot first. A genuine gap calls for building the missing capability. Leverage calls for the negotiation described below.

## 2. Quantify what their exception costs you

You need an honest number before you negotiate. Include:

- Engineering time to maintain their branch and keep it compatible with each release.
- Slower release cycles for everyone, if their fork holds back the main codebase.
- Operational cost of running a nonstandard environment.
- Risk: security patches, regulatory changes, and key-person dependence on the few engineers who understand their code.
- Opportunity cost: what those engineers would otherwise build.

Compare that total to their revenue and margin. Often a large customer remains highly profitable even with the exception, which means the right answer is to contain the problem rather than force a fight. Sometimes the numbers show that the customer is much less profitable than everyone assumed, which changes your negotiating posture.

## 3. Contain the exception so it can't block the platform

This is the most important step. Whatever happens with this customer, your modernization must not depend on their cooperation.

- **Isolate their custom code** behind a stable interface: an extension layer, adapter, or dedicated service that talks to the modern core through the same APIs as everyone else.
- **Keep the main codebase moving.** Their customization should become something that adapts to the core, not something the core must accommodate.
- **Freeze scope.** Their custom code gets maintained, but no new custom features get added to it without a new commercial agreement.

Done well, containment turns their refusal from a strategic threat into a manageable line item.

## 4. Make the cost visible and priced

Right now, the cost of their fork is probably hidden inside your general engineering budget, effectively a subsidy to your largest customer. Bring it into the open:

- **Offer a clear choice at renewal.** They can take the standard platform, with migration paid by you, credits, and faster releases, or they can keep the custom environment under a premium support tier that reflects its real cost.
- **Present it as a menu, not an ultimatum.** "Here are two supported options; you choose" preserves their autonomy and dignity.
- **Build in a sunset path.** For example, the premium tier might include a commitment to revisit migration at the next renewal, or it might step up in price over time as the fork diverges further from the core.

Many customers who refuse a free migration change their minds once the alternative carries an explicit price. Those who don't are now paying for the burden they create, which is also a fine outcome.

## 5. Consider the bargaining position on both sides

It's worth being clear-eyed about leverage, because a large customer often has less of it than it appears.

**Their leverage:** Their revenue matters to you. Losing them would hurt, and they know it.

**Your leverage:** Switching core policy systems is enormously expensive and slow for a carrier. Their realistic alternative to staying with you is a multi-year replacement project, which is far more disruptive than your migration. Also, over time, a fork on an aging branch becomes riskier for them: slower patches, fewer engineers who understand it, and missing out on new capabilities.

You don't need to wield this bluntly. But knowing that their best alternative is worse than your offer should keep you from making concessions out of fear.

## 6. Protect against precedent

Other customers will notice what happens here. If your largest customer successfully refuses, others will ask why they can't do the same.

- Put any exception in writing, with explicit terms and pricing.
- Frame it as a paid, supported tier available to anyone, not as special treatment.
- Avoid side deals that other customers could later demand under most-favored-customer clauses. Have legal check existing contracts for such clauses.

## 7. Keep the door open and build proof

Refusal today doesn't mean refusal forever.

- **Migrate their peers first.** When similar carriers are running smoothly on the standard platform and receiving new features quickly, the case makes itself.
- **Offer a partial pilot.** Migrate one line of business or one state first. A small success reduces perceived risk.
- **Show them what they're missing.** Keep them informed about new capabilities available only on the standard platform, so staying behind carries a visible cost.
- **Revisit at natural decision points:** renewals, leadership changes, regulatory changes, or when their own IT strategy shifts.

## 8. Know your walk-away point, even if you never use it

In rare cases, the numbers show that a customer's custom environment costs more than they're worth, and they refuse both migration and premium pricing. At that point, the honest options are to accept a loss-making relationship for strategic reasons, such as reference value or market presence, or to let the relationship end gracefully at contract expiration with a generous transition period.

You'll almost never need to go there. But having done the math, you'll negotiate from clarity instead of anxiety.

## The practical sequence

1. Diagnose the real reason at the executive level.
2. Quantify the cost of their exception.
3. Isolate their code so the platform moves forward regardless.
4. Offer a clear choice between a free migration and a priced premium tier.
5. Document the terms to avoid setting a precedent.
6. Keep building evidence through peer migrations and pilots.

In most cases, this turns a standoff into either a delayed migration or a profitable, contained exception, and either one is acceptable.

## Turn 5

**User:** What should we do?

**Assistant:**

# My recommendation

**Don't approve the two-year rewrite. Approve a serious, funded modernization program, and spend the next quarter gathering the evidence that tells you how aggressive it needs to be.** You are currently choosing between two strategies based on beliefs. You can cheaply replace those beliefs with facts before committing millions.

Here's the plan I'd follow.

## First 90 days: diagnose while starting to fix

Run these in parallel with a small dedicated team, perhaps four to six strong engineers plus someone from finance and someone from product.

**1. Unit economics analysis.** Build the cost-to-serve model described earlier. Attribute costs to tenancy, manual operations, version sprawl, and customization. Model what an automated single-tenant platform would look like.

**2. Customization inventory.** Catalog every custom code path, instrument usage, and classify each one (dead, duplicated, generalizable, regulatory variant, unique). Have legal review contracts for maintenance obligations, IP ownership, and most-favored-customer clauses.

**3. Delivery bottleneck diagnosis.** Trace several recent features from request to production and find where the months actually went. I'd bet a large share was testing, deployment, environments, and waiting on the few people who understand the code, rather than the stack itself.

**4. Immediate quick wins.** Start on automated testing and deployment pipelines now. They pay off under every scenario, including a rewrite, so there's no reason to wait.

**5. Customer and market check.** Review lost deals and talk to key customers about what they actually need: speed, integrations, cost, isolation. Find out whether "cloud-native" is costing you revenue or just marketing share.

## The decision point at roughly day 90

The evidence will point toward one of three paths:

| If the analysis shows... | Then... |
|---|---|
| Costs are mostly operations, versions, and customization; automated single-tenant hits margin targets | **Incremental modernization of the core.** This is the most likely outcome. |
| The core is fixable, but you want to win small MGAs or insurtechs whose contract sizes can't absorb the per-tenant cost floor | **Incremental modernization plus a separate greenfield product** for that segment. |
| The data model makes consolidation onto one version impossible, and automated single-tenant still misses margins badly | **A staged rebuild of the core**, but still delivered capability by capability behind a facade, never as a big-bang cutover. |

Notice that even the third path isn't the CTO's original plan. A true big-bang rewrite with a single switchover is almost never the right answer for a system carrying your revenue, because it concentrates schedule risk, freezes features, and invites every customer to reconsider you at once.

## Months 3 to 24: execute the program

Assuming the likely outcome:

- **Protect the capacity.** Ring-fence 30 to 40 percent of engineering for modernization, not subject to roadmap raids.
- **Build the facade and the landing zones.** Create the API layer, configuration capabilities, and extension points that let you carve off capabilities and absorb customizations.
- **Carve off capabilities in value order.** Likely candidates are rating, documents, billing, and portals, whichever customers care most about and are most separable.
- **Unwind customizations in parallel.** Start with dead code, then friendly pilots, then consolidated duplicates, then migrations tied to renewals.
- **Stop the bleeding.** Change sales policy so no new custom forks get sold without executive approval and explicit maintenance pricing.
- **Handle holdouts through containment and pricing,** as discussed, so no single customer can stall the platform.
- **Keep shipping customer features** on the modernized parts of the platform, which is what keeps the installed base loyal.

## Metrics to review every quarter

- Lead time from feature request to production
- Share of new work built on the modern stack
- Number of active customizations and code branches
- Customers on the current version
- Time to onboard and time to upgrade a customer
- Gross margin and cost to serve per customer
- Engineering attrition

Set kill criteria now. If lead time and cost to serve aren't clearly improving by month 12 to 18, reopen the strategy based on the data.

## How to handle the CTO and head of product

This is as much an organizational decision as a technical one, and you're the person who can bridge it.

- **Give the CTO credit for the diagnosis.** They're right that the situation is urgent and that small fixes won't suffice. The program should feel ambitious, not like a rejection of their concern.
- **Make the 90-day analysis a joint effort** with agreed thresholds in advance: what numbers would justify a deeper rebuild, and what numbers would rule it out. That turns a turf battle into a shared experiment.
- **Give the CTO ownership of the target architecture.** The landing zones, extension model, and modern stack are where their vision belongs. Incremental delivery is the path to that architecture, not an alternative to it.
- **Hold the head of product accountable for the other half.** Customer features must keep shipping, and the customization unwind depends on product and sales changing how they sell.

## The one-paragraph version for your CEO

"We have a real platform problem, but the biggest risk to the business is disrupting the installed base that funds us. We'll spend 90 days measuring where our costs and delays actually come from, while starting on test and deployment automation that pays off regardless. Unless the data shows the architecture itself is the barrier, we'll modernize incrementally: replacing capabilities one at a time, consolidating custom code, and continuing to ship what customers ask for. We'll track clear metrics quarterly and change course if they don't move."

That's what I'd do. It honors the CTO's urgency, keeps the product lead's protection of revenue, and replaces a high-stakes bet with a decision you can make on evidence.

## Outcome summary (sent to Jev)

The assistant recommends rejecting the two-year from-scratch rewrite and instead approving a seriously funded incremental modernization program. The next 90 days should go to gathering evidence on how aggressive that program needs to be.

The core reasoning is that the installed base is the profit engine and the moat. A big-bang rewrite would stall feature delivery, concentrate schedule risk (two years could become four or more), and force a migration that invites every customer to run an RFP. Incremental work delivers benefits within months and keeps option value. It also retains engineers by letting them ship modern code, and it delivers the outcomes insurers actually buy rather than the "cloud-native" label.

In the first 90 days, a small dedicated team should:

- build a cost-to-serve model attributing costs to tenancy, manual operations, version sprawl, and customization
- inventory and classify custom code, with legal review of contracts
- trace recent features to find delivery bottlenecks
- start test and deployment automation immediately
- check lost deals and customer needs

At day 90, the evidence points to one of three paths:

- **Incremental core modernization**, the likeliest outcome.
- **Incremental modernization plus a greenfield product** for small MGAs or insurtechs whose contract sizes can't absorb per-tenant costs.
- **A staged rebuild**, still delivered capability by capability behind a facade rather than as a single cutover.

Execution would ring-fence 30–40% of engineering. It would build an API facade and configuration and extension "landing zones," carve off capabilities like rating, documents, billing, and portals in value order, and unwind customizations at the company's expense. Sales would stop selling new forks, and holdout customers would be handled through containment and premium pricing. Quarterly metrics would track progress, with kill criteria: if lead time and cost to serve aren't clearly improving by months 12–18, the strategy gets reopened. The CTO should own the target architecture and co-design the 90-day analysis thresholds, while the head of product stays accountable for continued feature delivery.
