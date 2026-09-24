# legacy-rewrite/economic/testD

Model: claude-opus-5-5 · 2026-09-24T15:26:22.957047+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

**Assistant:**

# Rewrite vs. Incremental Modernization: Following the Money

**Short answer:** The full rewrite is the riskiest way to spend this capital. The incremental approach is closer to right, but only if it targets the parts of the system that actually cost you money, and only if it has funding discipline and kill criteria. The best option is a third one: fix the delivery bottlenecks first, move the hosting and commercial model to answer the "cloud-native" objection, then extract the few capabilities that drive revenue. Optionally, build new-platform capability on *new* business rather than migrating existing carriers.

The numbers below are illustrative. Replace them with your own. The structure of the argument matters more than the figures.

---

## 1. Where your money actually comes from

A P&C policy admin vendor typically earns from:

- **Recurring revenue** from existing carriers: license maintenance, subscription, hosting. This is most of your margin and the thing most at risk.
- **New logos**, where you're now losing to "cloud-native" competitors.
- **Expansion**: new lines of business, states, modules, and integrations for existing carriers.
- **Services**: implementation, upgrades, custom work.

Your problems map onto these streams differently:

- **Slow feature delivery** threatens expansion and eventually renewals.
- **Engineer attrition** raises the cost of every feature and makes it slower still.
- **The "cloud-native" competition** threatens new logos, and possibly renewals when contracts come up.

Any strategy should be judged by how quickly and reliably it protects recurring revenue and restores new-logo win rates, per dollar spent.

---

## 2. The full rewrite

### Revenue it generates or protects
- **Protects:** Nothing during the build. Existing customers see no benefit until they migrate.
- **Generates:** Potentially strong new-logo wins and a SaaS pricing story, but only once the new platform reaches parity for the lines, states, and configurations prospects need. That point is typically years out.
- **Puts at risk:** Existing revenue. Engineering capacity moves to the rewrite, so the legacy roadmap slows or freezes. Carriers asking for features today get told "wait for the new platform." That is how renewals are lost.

### Investment and operating costs
- **Build team.** Say 50–70 engineers at ~$180–220K loaded, or roughly $10–15M a year.
- **Dual maintenance.** The legacy system still needs regulatory updates, rate changes, form filings, and bug fixes throughout, so you run two platforms.
- **Migration.** This is the cost most rewrite plans underestimate. Every carrier has years of configuration, rating logic, state-specific rules, forms, integrations, and in-force policies. Each migration is effectively a re-implementation. Someone has to pay for it. Carriers rarely want to fund a migration they didn't ask for, so the cost often lands on you.
- **Cloud hosting.** If you move from customer-hosted to vendor-hosted, infrastructure cost moves onto your P&L. Gross margins compress until pricing catches up.

### When returns arrive
Late and all at once. The realistic shape is a deep J-curve:

| Years | What happens |
|---|---|
| 1–2 | Pure spend, legacy roadmap degraded |
| 2–4 | Parity chase. Twenty years of edge cases turn out to be requirements. |
| 3–6 | First migrations and new logos |

A "two-year" estimate for replacing a 20-year-old system that runs most of your revenue should be treated as optimistic until proven otherwise. The value is close to binary: little of it exists until the new platform can carry real customers.

### Risks that could wipe out returns
- Schedule slip, which extends dual running and burns cash.
- Churn during the feature freeze. Each point of churn on, say, $80M of platform revenue is ~$0.8M a year, compounding.
- Key legacy experts leave before their knowledge is captured in the new system.
- Competitors keep moving. The "modern stack" chosen in year one looks ordinary by year four.
- Migration failure at a flagship carrier, which becomes a reputational event in a small, conservative market.
- Leadership change or budget pressure cancels the program halfway. You then have spent the capital and gained nothing.

### Where spending grows without profit
- **Feature parity creep.** Rebuilding obscure functionality one or two customers use.
- **Infrastructure and platform-building** "for the future" before any customer runs on it.
- **Consultants and contractors** brought in to recover the schedule.
- **Migration tooling** and one-off conversion work per carrier.
- **Cloud bills** for environments that serve no revenue yet.

---

## 3. Incremental modernization (strangler pattern)

### Revenue it generates or protects
- **Protects:** Existing revenue, because you keep shipping what carriers ask for.
- **Generates:** Expansion revenue sooner, as extracted capabilities make certain features faster to build, for example a modern rating service, product configuration, or APIs for digital distribution.
- **Weakness:** It does less for the new-logo "cloud-native" story unless you deliberately package and market what you modernize.

### Investment and operating costs
- A modernization allocation within existing R&D, say 20–35% of capacity, instead of a separate large team.
- An **integration tax**: API layers, data synchronization between old and new components, and more complex testing. Expect individual features to cost somewhat more during the transition.
- Lower migration cost, because customers move capability by capability, often invisibly.

### When returns arrive
Early and gradually. Each slice can be justified on its own terms, such as faster rate changes or quicker onboarding of a new state. Returns start within quarters, not years.

### Risks that could wipe out returns
- **Modernizing the easy periphery instead of the costly core.** You carve off notifications and document generation while rating, policy lifecycle, and billing stay untouched.
- **Starvation.** Product priorities crowd out modernization every quarter, and the allocation quietly goes to zero.
- **Permanent hybrid.** You carry both the legacy system and the integration layer forever, paying for two architectures.
- **No marketable story.** Competitors keep winning deals on the cloud-native pitch.

### Where spending grows without profit
- Integration and synchronization infrastructure that becomes its own maintenance burden.
- Modernizing components chosen for engineering interest rather than economic impact.
- An open-ended program with no definition of done.

---

## 4. Side-by-side

| | Full rewrite | Incremental |
|---|---|---|
| Existing revenue during program | At risk | Protected |
| New-logo impact | Large but late | Modest unless packaged |
| Capital at risk before first return | High (tens of millions) | Low per slice |
| Shape of returns | Binary, back-loaded | Incremental, early |
| Main failure mode | Late, over budget, or cancelled | Drift, starvation, permanent hybrid |
| Ability to stop without loss | Poor | Good |

The rewrite concentrates risk. The incremental approach diffuses it, sometimes so much that nothing important ever changes.

---

## 5. A third approach: economically sequenced modernization

Fund work in the order that most directly protects and grows revenue, in tranches, with stop points.

### Step 1: Diagnose where the time and money actually go (1–3 months, low cost)
Before choosing an architecture, find out why features take months:
- **Value-stream analysis.** Break lead time down into design, coding, testing, environment setup, release, and customer upgrade. In many legacy shops, most of the delay is manual testing, release process, and per-customer customization, not the programming language.
- **Lost-deal analysis.** In deals lost to cloud-native competitors, what did buyers actually object to: hosting model, upgrade burden, APIs, UI, configurability, or price?
- **Exit interviews with departed engineers.** Did they leave because of the stack, or because of toil, on-call burden, and lack of career path?

This step decides whether you have an architecture problem or a delivery-process problem. It is the cheapest money you'll spend.

### Step 2: Fix the delivery system (6–12 months)
- Automated regression testing, especially of rating and forms.
- CI/CD and reproducible environments.
- Reducing per-customer code forks by moving customization into configuration.

This lowers the cost of every feature, legacy or modern, and makes any later modernization cheaper and safer. It also directly addresses engineer frustration.

### Step 3: Answer the market objection commercially (in parallel)
Much of what carriers mean by "cloud-native" is:
- a vendor-hosted, managed SaaS offering
- continuous upgrades instead of painful version migrations
- APIs for distribution and insurtech integrations

You can offer managed hosting, a subscription model, and an API layer on the existing core long before rewriting it. This protects renewals and new-logo win rates within a year. Price it to cover the hosting cost you're taking on.

### Step 4: Extract the highest-value capabilities (ongoing, funded per slice)
Rank candidates by revenue impact and cost-to-change. In P&C, typical winners are:
- **Rating and product configuration.** Faster new products, states, and rate changes drive expansion revenue.
- **Integration and API layer.** Enables distribution deals.
- **Billing or document generation**, if those are frequent sources of customer pain.

Each slice gets a business case, a budget, a success metric, and a stop condition.

### Step 5 (optional): Build the new platform on new revenue, not migration
If the diagnosis shows the core really can't compete, build the new platform for a **new segment**, such as a line of business or customer tier you don't currently serve well. That way:
- New customers fund and validate the platform.
- The legacy system is run for cash and stability rather than forcibly migrated.
- Migration of existing carriers happens later, voluntarily, and only if the new platform has proven itself.

You could also evaluate **buying or partnering** for specific components, such as a licensed rating engine, rather than building everything.

### Why this gives better returns for the capital at risk
- **Earliest returns:** Delivery fixes and the hosting/API offering pay back within 6–18 months.
- **Revenue protection:** Existing carriers keep getting features throughout.
- **Staged capital:** Each tranche is justified by the previous tranche's results.
- **Preserved option:** You retain the option of a larger rebuild, now informed by data rather than conviction.

---

## 6. Governance: who controls the money and who decides to stop

This is where modernization programs usually fail, regardless of strategy.

**The core conflict.** If the CTO designs, runs, funds, and judges the rewrite, nobody is positioned to call it failing. If product controls the roadmap under the incremental plan, modernization gets deferred every quarter. Both proposals, as described, give budget control to the person most invested in the outcome.

**A better structure:**
- **Capital allocation:** An investment committee (CEO, CFO, CTO, head of product) funds modernization in tranches, like a venture investor, typically every 6 months.
- **Financial ownership:** One executive owns the business case and reports against financial outcomes, not engineering milestones.
- **Delivery ownership:** Engineering owns execution and technical quality.
- **Protected capacity:** A fixed percentage of R&D is ring-fenced for modernization so product can't quietly reclaim it. Its use is justified by results.
- **Pre-committed kill criteria:** Agreed before funding. For example: "If extracted rating service isn't live with two carriers by month 12, or lead time for rate changes hasn't fallen by 40%, we stop or re-scope."
- **Independent review:** An outside technical assessment at each major gate, especially before any decision to escalate toward a larger rebuild.

**Metrics tied to money, reviewed quarterly:**
- Lead time from feature request to production at customers
- Engineering cost per delivered feature
- Gross retention and renewal rates
- Win rate against cloud-native competitors
- Expansion revenue per carrier
- Gross margin, especially as hosting shifts onto your books
- Regretted engineering attrition

---

## 7. How to settle the disagreement

Don't decide between the CTO and the head of product on conviction. Run the Step 1 diagnosis and let these questions decide:

1. **Of lead time, how much is architecture vs. testing, release, and customization?** If most is process, a rewrite won't fix it.
2. **Why are you losing deals?** If it's hosting and upgrades, managed SaaS on the existing core may recover most of it.
3. **Can the core be changed safely at all?** If critical components are truly unmodifiable and undocumented, extraction becomes more urgent. That points to accelerating Steps 4–5, still not a big-bang rewrite.
4. **What would it cost to migrate your top 10 carriers?** If nobody can estimate this credibly, the rewrite plan isn't ready for funding.
5. **How much churn can the business absorb during a slowdown?** This sets your real risk tolerance.

The CTO is right that the status quo is a slow decline and that timid, peripheral fixes won't get you out. The head of product is right that the revenue you have today is what funds any future. The approach that respects both makes early, measurable progress on the problems that cost you money, and escalates investment only as the evidence justifies it.

## Turn 2

**User:** You say managed hosting on the existing core pays back within a year, but moving on-prem carriers onto our infrastructure is its own migration. What would that cost per carrier, how much of a price uplift will carriers actually accept, and what happens to gross margin if they won't pay more?

**Assistant:**

You're right, and I overstated it. "Pays back within a year" is plausible for new carriers who start hosted. It is not a safe assumption for moving your installed base, where each move is a project with real cost and the price uplift may not cover it. The figures below are illustrative. Replace them with your own data.

## 1. What a hosting migration costs per carrier

A hosting move is much cheaper than a rewrite migration. The code, configuration, rating logic, and data model stay the same; only where it runs changes. But several things can make it expensive.

**Cost drivers, roughly in order of impact:**

1. **Version gap.** If a carrier is several releases behind or runs a customized fork, you'll almost certainly need to upgrade them before hosting them. Otherwise you're operating many different versions. In many cases the upgrade, not the move, is most of the cost.
2. **Integrations.** Claims, general ledger, billing, agency portals, data warehouses, print vendors, reporting tools, and nightly batch jobs that assume the system sits inside the carrier's network. Each has to be re-pointed and tested over private connectivity or APIs.
3. **Security and vendor-risk review.** Carrier security reviews, audit rights, data-residency questions, and regulatory cybersecurity requirements. Slow, and heavy on staff time.
4. **Data migration and validation.** Moving the database, confirming in-force policies, and re-running rating comparisons.
5. **Testing and cutover.** Carrier acceptance testing, possibly a parallel run, a cutover weekend, and several weeks of hypercare.

**Illustrative ranges (replace with your own estimates):**

| Carrier profile | Likely one-time cost |
|---|---|
| Small, current version, few integrations | $150K–$400K |
| Mid-size, one or two versions behind, moderate customization | $500K–$1.5M |
| Large, old version, custom code, many integrations | $2M–$5M+ |

**Platform costs you incur once, before any carrier moves:**
- Hosting environments and automation
- Security certification (e.g., SOC 2 Type II)
- Disaster recovery
- A 24x7 operations team

This might be $2–5M to set up and $2–4M a year to run. The run cost is largely fixed, so hosting only pays if enough carriers use it.

**To estimate your real numbers,** look at your last three major customer upgrades and any hosted implementations you've done. Those are your best predictors. Then inventory each carrier's version and integrations.

## 2. What price uplift carriers will accept

I can't give you a reliable industry-wide uplift percentage, and you should be skeptical of anyone who does. What I can tell you is how carriers will evaluate it.

**Carriers compare your new fee to their total cost of running the system today**, not to their current maintenance fee. That total includes:
- servers, storage, and data-center or cloud costs
- database, system, and security administrators
- disaster recovery
- periodic hardware refresh
- the internal cost and pain of doing upgrades

For a mid-size carrier, that might be $500K–$1.5M a year. Your uplift is effectively a share of those savings. A price that captures 30–60% of them is a defensible starting hypothesis. Test it in real proposals rather than assuming it.

**Acceptance will vary by situation:**

- **Higher willingness to pay:**
  - smaller carriers with thin IT teams
  - carriers facing a hardware refresh or data-center exit
  - carriers that just lost a key administrator
  - carriers with an overdue upgrade
- **Lower willingness to pay:**
  - large carriers with established infrastructure teams, where the move threatens internal jobs and budgets
  - carriers that just refreshed hardware (sunk cost)
  - carriers with long contracts and no renewal pressure

**A risk that's easy to miss:** if you earn services revenue from upgrades, a hosted model with included upgrades cannibalizes it. Count that as lost revenue in the model.

## 3. What happens to gross margin

Today, on-prem maintenance revenue has very high gross margin because carriers pay for the infrastructure. Hosting moves that cost onto your books.

**Illustrative mid-size carrier:** $1M a year in maintenance, $150K of existing support cost, and new hosting cost of $300K a year ($150K infrastructure plus $150K share of the ops team).

| Scenario | Revenue | Cost | Gross profit | Gross margin |
|---|---|---|---|---|
| Today, on-prem | $1.00M | $0.15M | $0.85M | 85% |
| Hosted, no uplift | $1.00M | $0.45M | $0.55M | 55% |
| Hosted, +$300K uplift | $1.30M | $0.45M | $0.85M | 65% |
| Hosted, +$500K uplift | $1.50M | $0.45M | $1.05M | 70% |

What this shows:

- **Without an uplift, you lose about $300K of gross profit per carrier per year,** permanently, plus the migration cost.
- **Even at a healthy uplift, gross margin percentage falls.** Only gross profit dollars can improve. Decide in advance which one your board and investors will judge you on, and prepare them for it.
- **Payback on migrating stable carriers can be poor.** At a $500K uplift you net about $200K more gross profit a year. Against a $1M migration you pay for, that's a five-year payback. At a $300K uplift you never pay it back.

**Offsets that can improve the picture:**
- Supporting fewer versions, running on infrastructure you control, reduces support and engineering cost.
- Faster releases and fewer environment-specific bugs.
- Consolidating carriers onto shared infrastructure. A 20-year-old system is probably single-tenant, so hosting cost scales nearly one-for-one with carrier count. Sharing databases, compute, and operations tooling is where hosting margins improve. That may require some engineering work, and it belongs in the business case.

## 4. Revised recommendation: segment the base, don't migrate all of it

Hosting pays for itself mainly through three things:
- **new carriers**, who have no migration cost
- **retention** of carriers who might leave
- **version consolidation**

Uplift on happy, stable carriers is the weakest source of return. So sequence it:

1. **New carriers: hosted by default.** This is the cleanest economics and directly answers the "cloud-native" objection in sales.
2. **Carriers at a natural trigger point:** hardware refresh, an overdue upgrade, contract renewal, or IT staff loss. Combine the move with an upgrade they'd pay for anyway, and price it as one package.
3. **At-risk accounts** being pitched by cloud-native competitors. Treat the migration as a retention investment and compare its cost to the value of the account over its expected lifetime.
4. **Stable, satisfied on-prem carriers: leave them alone** until they reach a trigger.

**Contract terms that protect you:**
- Require a multi-year commitment (e.g., five years) in exchange for any migration subsidy.
- Charge a migration fee, even if only partial.
- Use a price ramp so the uplift phases in.
- Set minimum fees and pass-through pricing for unusual infrastructure usage.
- Include upgrades in the price, and account for the services revenue you give up.

## 5. Prove it before scaling

Pilot with two or three carriers from segments 2 and 3. Track four numbers:

1. Actual migration cost vs. your estimate
2. Actual hosting cost per carrier
3. Price actually accepted
4. Change in support effort for those carriers

Set go/no-go thresholds before you start. For example: scale only if migration cost comes in within 25% of estimate and gross profit per migrated carrier is at least flat within two years. Carriers that start hosted give you the cleanest read on hosting economics. The pilots tell you whether migrating the base is worth it at all, or whether you should let it happen only at trigger points.

## Turn 3

**User:** If we only win two or three new carriers a year and move a few more at trigger points, how many hosted carriers does it take to cover the $2–4M a year of fixed platform and 24x7 ops cost, and how many years of losses are we funding before we reach that number?

**Assistant:**

At two to six hosted carriers a year, the hosting line on its own loses money for roughly two to four years in a reasonable case, and may never break even in a bad one. What decides it is how much each hosted carrier contributes, how much of the fixed cost you really need on day one, and whether hosting wins or saves accounts you'd otherwise lose.

## 1. Setting up the math

In my earlier example, the $300K hosting cost per carrier included a $150K share of the ops team. That share is part of the $2–4M fixed cost, so it can't also be counted per carrier. Splitting the two:

- **Variable cost per carrier:** about $150K a year of infrastructure (compute, storage, backups, DR, connectivity).
- **Fixed platform cost (F):** $2–4M a year for the 24x7 ops team, security, and tooling. Separately, there's a one-time setup cost of $2–5M.
- **Contribution per hosted carrier (c):** hosting price uplift minus variable cost. That's about $350K at a $500K uplift, $250K at $400K, and $150K at $300K.

The core formulas:

- **Carriers needed to break even:** N = F ÷ c
- **Years to get there:** roughly N ÷ (carriers added per year), plus about half a year because carriers onboard throughout the year
- **Cumulative operating losses before break-even:** roughly F × years ÷ 2, since the annual loss shrinks steadily toward zero. Setup cost comes on top.

## 2. Carriers needed to break even

| Fixed cost | c = $350K | c = $250K | c = $150K |
|---|---|---|---|
| $2M | 6 | 8 | 14 |
| $3M | 9 | 12 | 20 |
| $4M | 12 | 16 | 27 |

At four to six carriers a year, the right-hand column is five years or more of accumulation. The left column is one to two.

## 3. Three scenarios, year by year

These assume carriers onboard evenly through the year, so each contributes half a year in the year it's added.

**Base case:** 5 carriers a year, c = $250K, F = $3M, setup $3.5M

| Year | Carriers at year end | Operating result | Cumulative, incl. setup |
|---|---|---|---|
| 1 | 5 | −$2.4M | −$5.9M |
| 2 | 10 | −$1.1M | −$7.0M |
| 3 | 15 | +$0.1M | −$6.9M |
| 4 | 20 | +$1.4M | −$5.5M |
| 5 | 25 | +$2.6M | −$2.9M |
| 6 | 30 | +$3.9M | +$1.0M |

That's two years of operating losses, a funding trough of about $7M, and cumulative payback in year 6. Any migration subsidies you pay push those dates later.

**Pessimistic:** 3 a year, c = $150K, F = $4M, setup $3.5M
- Needs 27 carriers, which takes about 9–10 years to reach.
- Operating losses accumulate to roughly $17–19M before break-even, plus setup.
- In practice, this never pays back on the hosting line alone.

**Optimistic:** 6 a year, c = $350K, F = $2M, setup $2M
- Operating break-even in year 2.
- Trough of about $3M, payback in about year 3.

**A caveat on fixed cost:** it rises in steps as you add carriers, because more carriers eventually need more ops staff, on-call coverage, and security work. So even the base case is somewhat optimistic past about 20 carriers.

## 4. Two things change the answer more than the carrier count

### Fixed cost is partly a choice
A full in-house 24x7 team from day one is the most expensive way to start. Alternatives convert fixed cost into per-carrier cost:
- Use your cloud provider's managed database, backup, and monitoring services instead of building your own.
- Contract overnight and weekend coverage to a managed service provider that charges per environment.
- Cover business hours with existing support staff, and hire dedicated ops staff only as carrier count grows.

If this cuts year-one fixed cost from $3M to around $1–1.5M, the base case breaks even at about 4–6 carriers, and the trough falls to roughly $3–4M. That's the single biggest lever you have.

### The hosting line isn't the full return
The tables credit hosting only with its uplift. They ignore three benefits.

- **Deals won because you offer hosting.** If hosting is why you win a carrier you'd otherwise lose, that carrier's full account profit counts: maintenance, services, and expansion, perhaps $850K or more a year in gross profit, not just the $250K hosting contribution. Two such wins a year would cover a $3M fixed cost within about two years.
- **Churn prevented.** Keeping one at-risk mid-size carrier protects around $850K a year in gross profit. That is worth several stable migrations.
- **Version consolidation.** Fewer versions and customer environments to support reduce engineering and support cost. Measure this in the pilots rather than assuming it.

So the key question isn't how many hosted carriers you need. It's how many deals you are losing, or are about to lose, because you don't offer hosting. That's what the lost-deal analysis from the first step should tell you:
- **If the answer is two or more a year:** hosting pays back quickly even at low volume.
- **If the answer is close to zero:** at your win rate, hosting is a multi-year, $7M+ bet on uplift alone. Keep it small and variable-cost until demand shows up.

## 5. What to take to the investment committee

1. **Fund a lean launch, not a full platform.** Set a year-one fixed cost target of $1–1.5M using managed services and a partner for overnight coverage. Commit to building in-house 24x7 capability only past an agreed threshold, such as 8–10 hosted carriers.
2. **Set a price floor.** Don't accept hosting deals with contribution below about $250K, unless it's an explicit retention or competitive-win decision with the full account value documented.
3. **Track attribution.** For every hosted deal, record whether hosting was decisive, and track retention of hosted vs. on-prem carriers. That's the evidence for expanding or stopping.
4. **Set a stop condition now.** For example: if fewer than 6 carriers are hosted by the end of year 2, or contribution per carrier is below $200K, freeze the fixed cost and offer hosting only through the partner.

With those controls, the capital at risk falls from $7M+ to roughly $3–4M. You'll also know within about two years whether hosting is winning business or just moving costs onto your books.

## Turn 4

**User:** You flip the case by crediting hosting with the full ~$850K of account profit on every "hosting-decisive" win or save, but lost-deal reasons usually come from sales reps, and some of those carriers would have signed or stayed anyway. How do we estimate the share of that value hosting actually causes, and at what level of attribution does the $3–4M bet stop paying back?

**Assistant:**

You're right to challenge that. Crediting hosting with the full account profit is only valid when hosting actually caused the win or the save. Sales-reported loss reasons tend to overstate product gaps, because "we lacked hosting" is easier to say than "we were outsold" or "we were too expensive." The case has to be rebuilt with an explicit attribution factor, and then you need to see how sensitive the answer is to it.

## 1. Restating what hosting is worth

**Value of hosting = hosting-line contribution + p × incremental account value of hosting-decisive deals**

- **p** is the share of rep-labeled "hosting-decisive" wins and saves that would not have happened without hosting.
- **Incremental account value** should be contribution, not gross profit. For a new carrier, subtract sales commission, implementation cost you absorb, and ramp time. For a save, count only the profit you'd actually have lost, not the whole account forever.

For illustration, I'll use two values per event: **$850K a year** (the earlier gross-profit figure) and **$600K a year** (a more realistic net contribution). Both are placeholders. Your finance team should calculate the real number from actual account data.

Two further conventions:
- Events happen mid-year, so each contributes half a year in the year it occurs.
- Hosting-decisive carriers are assumed to stay through a five-year horizon. Real churn lowers the value somewhat.

## 2. Two hosting-line cases

Both use a lean launch: $2M setup, fixed cost starting around $1.5M a year and stepping up to $3M as volume requires.

**Case A: moderate.** 5 carriers a year, $250K contribution each.

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Cumulative, incl. setup | −$2.9M | −$3.3M | −$3.1M | −$1.8M | +$0.9M |

This pays back in year 5 even with zero attribution. Attribution only determines how much sooner.

**Case B: harsh.** 4 carriers a year, $150K contribution each.

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Cumulative, incl. setup | −$3.2M | −$3.8M | −$5.3M | −$6.2M | −$6.5M |

This never pays back on the hosting line alone. Attributable wins and saves must cover about $6.5M within five years.

## 3. Break-even attribution

The attribution p needed to close the gap is:

**p = hosting-line shortfall ÷ (claimed events per year × value per event × accrual years)**

Accrual years are 4.5 through year 3 and 12.5 through year 5.

**Case A: p needed to pay back by year 3 instead of year 5** (shortfall about $3.1M)

| Claimed events per year | $850K per event | $600K per event |
|---|---|---|
| 3 | 27% | 39% |
| 2 | 41% | 58% |

**Case B: p needed to pay back at all within five years** (shortfall about $6.5M)

| Claimed events per year | $850K per event | $600K per event |
|---|---|---|
| 3 | 20% | 29% |
| 2 | 31% | 43% |

What this means:

- **If Case A holds,** attribution is upside. You don't need to prove much.
- **If Case B holds,** you need at least 20–45% of rep-claimed hosting-decisive deals to be genuinely caused by hosting. Below roughly 20%, the $3–4M bet doesn't pay back in any combination modeled here.
- **The claimed-event count comes from reps too.** Two or three claims a year is a small base. One misclassified deal moves p by 30–50 points.

## 4. Estimating p honestly

Rank evidence by how hard it is to fake, and weight it accordingly.

### Strongest evidence: documents and behavior
- **RFP requirements.** Was vendor hosting a mandatory requirement, a scored criterion (and at what weight), or absent? If a mandatory requirement disqualified you, hosting was close to fully causal.
- **Where the deal ended.** Losing at the first screening for lack of hosting is strong evidence. Losing at the final decision when hosting was never raised is weak evidence.
- **What the winner offered.** If the competitor won with an on-prem deal, hosting wasn't the reason.
- **Revealed preference.** Quote every new prospect both on-prem and hosted pricing. If most choose on-prem, or refuse to pay the hosted premium, hosting isn't decisive for them.

### For saves: require documented churn intent first
Count a save only if the risk was on record before hosting was offered: an RFP issued, a competitor demo, a non-renewal notice, or explicit executive escalation. Then compare the retention rate of at-risk carriers offered hosting against your historical retention of at-risk carriers.

### Medium evidence: independent win/loss interviews
Have someone outside sales interview the carrier's decision makers. That could be finance, product, or a third party. Ask them to rank decision factors and say what would have changed the outcome. This is still stated preference, so discount it, but it is far better than rep coding.

### Weakest evidence: rep-reported reasons
Use these only to flag deals for review, never as attribution.

### Starting weights until your own data exists
These are heuristics to calibrate over time, not established figures:
- Mandatory RFP requirement, or documented churn threat resolved by hosting: **80–100%**
- Scored criterion, and the winning competitor offered hosting: **30–60%**
- Mentioned in independent interview but not in RFP: **15–30%**
- Rep-reported only: **0–10%**

### Process rules to prevent inflation
- **Classify before the outcome.** Record hosting's role (mandatory, scored, or not mentioned) when the opportunity is qualified, not after it closes.
- **Have finance own the classification,** not sales.
- **Separate compensation from attribution.** If reps earn more on hosted deals, they will label more deals hosting-decisive.
- **Review every claimed event** at the quarterly investment review.

### Accept the limits of small numbers
At two or three events a year, no statistical test will settle p for several years. Estimate a range from the evidence above, and make funding decisions using the low end.

## 5. The decision rule

1. **Calculate your own break-even p** with the formula in section 3, using real contribution per carrier, real fixed cost, and a finance-calculated value per event.
2. **Compare it with your conservative evidence,** meaning documented RFP requirements, verified churn threats, and revealed preference. Rep claims don't count here.
   - **If the conservative estimate clears the break-even p comfortably:** fund the next tranche.
   - **If the case only works on rep-reported attribution:** stay lean. Keep fixed cost near $1.5M, run overnight coverage through a partner, and wait for documentary evidence.
3. **Re-estimate p every six months** as more deals close, and tie each funding step to it. For example, move to full in-house 24x7 operations only if verified attribution plus hosting-line results show payback within four years.

The practical result: if hosting-line economics look like Case A, you can proceed cautiously even while attribution is uncertain. If they look like Case B, attribution becomes the entire investment case. That makes it the one number in this plan that should be measured by someone with no stake in the answer.

## Turn 5

**User:** What should we do?

**Assistant:**

## Recommendation

**Don't approve the two-year rewrite. Don't approve open-ended incremental modernization either.** Approve a staged program funded in six-month tranches, with the first tranche aimed at finding out where the money is actually lost and fixing the cheapest, surest problems first.

The rewrite puts $10–15M a year at risk, with no returns for years and your existing revenue exposed while you build. The staged program puts roughly $3–4M of new cash at risk in year one, plus a reallocation of existing engineering capacity, and every step produces evidence for the next decision.

## First 90 days: diagnose and set up governance

**Diagnosis** (small cost, mostly internal time):
1. **Lead-time breakdown.** Measure where the months go on recent features: design, coding, testing, release, customer upgrade. This tells you whether you have an architecture problem or a delivery-process problem.
2. **Lost-deal and at-risk review.** Pull the last two to three years of losses and churn threats. Classify them using documents (RFP requirements, where each deal ended, what the winner offered), not rep-reported reasons.
3. **Installed-base inventory.** For each carrier: version, customizations, integrations, contract renewal date, and upcoming hardware refresh. This gives you the real migration cost and the trigger-point calendar.
4. **Attrition review.** Exit interviews for engineers who left in the past two years. Were they leaving the stack, the toil, or the pay and career path?

**Governance:**
- Form an investment committee of CEO, CFO, CTO, and head of product to fund work in tranches.
- Give finance ownership of the business case and hosting attribution.
- Ring-fence about 25% of R&D capacity for modernization so it can't be quietly reclaimed.
- Agree kill criteria before spending anything beyond the diagnosis.

**Start immediately, because it pays off under every scenario:** automated regression testing of rating and forms, and a working CI/CD pipeline.

## Months 3–12: fix delivery, pilot hosting, pick one extraction

1. **Delivery system.** Finish test automation, move to reliable releases, and start converting per-carrier code forks into configuration. Target a measurable cut in lead time, for example 30–40% within 12 months.
2. **Lean hosting launch.**
   - Offer hosting to all new carriers by default.
   - Migrate two or three carriers that are at a trigger point or at risk.
   - Keep fixed cost near $1.5M using cloud managed services and a partner for overnight coverage.
   - Enforce a price floor of about $250K contribution per carrier, with exceptions only for documented retention or competitive cases.
   - Quote every prospect both on-prem and hosted pricing so you learn what they actually choose.
3. **API layer on the existing core.** It supports distribution deals and weakens the "cloud-native" pitch against you.
4. **One capability extraction, chosen by economics.** Most likely rating and product configuration, if the diagnosis confirms it drives the most revenue-relevant delay. Fund it as a single slice with its own success metric.

## Month-12 gate: decide with evidence

| Question | Evidence | If yes | If no |
|---|---|---|---|
| Is hosting paying its way? | Actual cost per carrier, price accepted, verified attribution vs. break-even | Fund in-house 24x7 past about 8–10 carriers | Stay partner-run and variable-cost |
| Did delivery fixes cut lead time? | Lead-time and cost-per-feature trend | Keep capacity allocation, extract next slice | Revisit whether the core itself is the constraint |
| Is the core truly unmodifiable? | Extraction slice outcome, diagnosis | Plan a new platform for a *new* segment, funded by new customers | Continue incremental extraction |
| Are you still losing deals on architecture? | Document-based loss analysis | Accelerate extraction and packaging | Hold spend steady |

Even in the worst case, where the core can't be modernized in place, the answer is a new platform proven on new business first. It is still not a big-bang migration of the carriers who pay your bills.

## Roles

- **CTO:** Own the delivery-system overhaul, the extraction architecture, and technical quality. This is a real mandate, and it's the fastest way to fix the engineering experience that's driving attrition. The CTO doesn't also get to judge whether their own program is succeeding.
- **Head of product:** Protect the customer roadmap and own the revenue metrics: retention, expansion, and win rate against cloud-native competitors.
- **CFO:** Own the business case, the attribution rules, and the tranche decisions.
- **CEO:** Chair the gates and enforce the kill criteria.

## What would change this recommendation

The diagnosis could show three things that would change the plan:
- Lead time is dominated by the architecture itself.
- The core can't be changed safely.
- You are losing a large and growing share of deals because of it.

If so, speed up extraction and bring forward the new-segment platform. Commit capital only as each stage proves out.

## The message to your team

"We're not choosing between the CTO and the head of product. We're funding the moves that protect today's revenue and pay back fastest. We'll measure them honestly, and we'll only put in more capital when the evidence says it will earn a return."

## Outcome summary (sent to Jev)

The assistant recommends approving neither the two-year rewrite nor open-ended incremental modernization. Instead, it proposes a staged program funded in six-month tranches, starting with finding out where money is actually lost and fixing the cheapest, surest problems first.

**Why not the rewrite.** It puts $10–15M a year at risk. Returns are back-loaded and nearly binary, while existing revenue is exposed to churn during the feature slowdown. The staged plan risks roughly $3–4M of new cash in year one, and each step produces evidence for the next decision.

**First 90 days**
- Break down feature lead time.
- Classify lost deals and churn threats from documents such as RFP requirements, not rep-reported reasons.
- Inventory each carrier's version, customizations, integrations and trigger dates.
- Review engineer exit interviews.
- Form an investment committee, give finance ownership of the business case and hosting attribution, ring-fence about 25% of R&D, and agree kill criteria before spending.
- Start regression test automation and CI/CD immediately.

**Months 3–12**
- Target a 30–40% lead-time cut.
- Launch lean hosting: new carriers hosted by default, two or three trigger-point or at-risk migrations, about $1.5M fixed cost using managed services and an overnight partner, and a price floor of about $250K contribution.
- Quote prospects both on-prem and hosted pricing.
- Add an API layer to the existing core.
- Fund one capability extraction chosen by economics, likely rating and product configuration.

**Month-12 gate.** Decide on in-house 24x7 operations only past 8–10 hosted carriers. Base further extraction on measured results.

**Roles.** The CTO owns delivery and architecture but does not judge their own program. Product owns revenue metrics. The CFO owns the business case and tranche decisions. The CEO enforces kill criteria.

**Caveats.** Figures are illustrative, and the hosting case may rest heavily on verified attribution. If the diagnosis shows architecture dominates lead time, the core cannot be changed safely, or deals are increasingly lost because of it, the plan should accelerate extraction and build a new platform proven on a new segment, not migrate existing carriers.
