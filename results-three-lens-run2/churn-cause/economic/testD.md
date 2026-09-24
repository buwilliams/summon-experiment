# churn-cause/economic/testD

Model: claude-opus-5-5 · 2026-09-24T15:31:09.232611+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

**Assistant:**

# Which VP Is Right, and What to Do About Churn

## The short answer

You can't know yet which VP is right, and neither can they. Both theories are plausible, both are self-serving (each VP is asking for budget their own team would control), and they are probably connected. Customers who never finish implementation never use the analytics you already have. When they leave, "the competitor has better analytics" is the easiest thing to tell you. So a product gap and a services failure can look identical in exit interviews.

The right move is a short, cheap diagnosis before committing capital to either theory. Then fund a combined time-to-value program in stages, with one owner of the churn number. The details follow.

---

## 1. First, work out which belief is right (4–6 weeks, under ~$100K)

Your data can largely settle this argument. Run these cuts on the last 24–36 months of churned and renewed accounts:

| Test | If it points to **Product** | If it points to **Services** |
|---|---|---|
| **Churn by adoption depth at renewal**: did churners go fully live and use core modules? | Healthy, fully adopted customers are leaving | Churners never fully went live or used a fraction of modules |
| **Churn by implementation cohort** | Churn is spread evenly across cohorts | Churn is concentrated in customers implemented in the last 2–3 years, especially long or over-budget projects |
| **Implementation duration vs. churn** | No correlation | Longer or overrun implementations churn at much higher rates |
| **Where churners went** | A named competitor, citing AI/analytics | In-house build, cheaper vendor, or "status quo." (Also check carrier M&A. Regional carriers consolidate, and acquired-carrier churn isn't fixable by either VP.) |
| **New-logo win/loss** | Win rates have dropped in competitive deals, with losses citing analytics/AI | Win rates are stable (the product still sells; it just doesn't stick) |
| **Support ticket trends** | Mostly feature requests | Mostly configuration, integration, and data issues |
| **Third-party churn interviews** (not your own team, whom customers are polite to) | "They do things we can't" | "We never got it working the way we were promised" |

Two cautions:
- **Separate logo churn from dollar churn**, and look at downgrades. Losing ten small carriers is a different problem from losing two large ones.
- **Account for contract lag.** Claims systems usually sell on multi-year terms, and carriers decide 12–18 months before renewal. Today's churn reflects experiences from 2–3 years ago. That matters for diagnosis (look at what those cohorts experienced) and for ROI timing (any fix shows up in churn late).

---

## 2. Following the money

I don't have your numbers, so here is an **illustrative model**. Substitute your own figures; the structure is what matters.

**Assumed baseline:** $50M ARR, 250 carriers at ~$200K average contract value, 80% subscription gross margin. Churn has doubled from 7% to 14%.

### What the churn increase costs

- **Excess ARR lost each year:** about $3.5M.
- **Compounding:** each lost cohort stays lost. By year 3, you are roughly $10M ARR below where you'd otherwise be. That is about **$16–17M in cumulative gross profit** over three years.
- **Replacement cost:** replacing $3.5M of ARR through new sales at a typical ~1.5× contract value in acquisition cost is roughly **$5M of sales and marketing spend per year**, just to stand still.
- **Customer lifetime:** at 7% churn a customer lasts about 14 years on average; at 14%, about 7. You have roughly halved the lifetime value of every customer. That also means the business can justify less acquisition spend, which slows growth.

This is the prize. Either proposal should be judged on how much of it it recovers, how fast, and at what cost.

### Proposal A: Accelerate the roadmap (VP of Product)

**Revenue it could generate or protect**
- **Retention:** recover churn that is actually caused by feature gaps. In this model that is some fraction of the $3.5M/yr excess, and unknown until you run the diagnosis.
- **Upsell:** an AI or analytics module priced at a 15–25% uplift on contract value, sold to adopters.
- **New logos:** better win rates in competitive deals.

**Costs**

| Item | Estimate | Notes |
|---|---|---|
| Engineering, data science, ML | ~20 people × ~$220K loaded ≈ $4.4M/yr | Ongoing |
| AI infrastructure and inference | Scales with usage | Recurring cost of goods sold; this lowers gross margin |
| Model governance and compliance | ~$0.3–0.7M/yr | Insurance regulators are actively scrutinizing AI in claims decisions (bias, explainability, state adoption of the NAIC AI bulletin). Carriers will demand documentation and audit support. |
| **Total** | **~$5M+/yr** | |

**When returns arrive**
- Build: 9–12 months.
- Customer adoption: another 6–12 months.
- Effect on churn: gated by renewal cycles.
- **Realistic payback: year 2–3 at best.** Upsell revenue can arrive earlier than retention benefits.

**Risks that could wipe out returns**
- **Customers can't adopt it.** If implementation is the real problem, new features land on customers who aren't live on the old ones. You'd spend $5M a year building features that stalled customers never reach.
- **The feature-parity treadmill.** Well-funded competitors keep moving, so "catching up" has no finish line.
- **Regulatory friction** slows how fast carriers are willing to deploy AI in claims decisions.
- **Diversion.** Engineering capacity is pulled away from fixing configurability and integration, the very things that make implementations long.

**Where spending can grow without profit**
- **Bundling AI "free"** to save accounts. Inference costs then scale with usage while revenue doesn't.
- **One-off features** built to rescue individual carriers.
- **Roadmap scope creep** with no adoption gate.

### Proposal B: Fix onboarding and service (VP of Services)

**Revenue it could generate or protect**
- **Saved renewals:** at-risk accounts renewing in the next 6–18 months that haven't reached value can be rescued. This is the fastest money available.
- **Earlier revenue:** shorter implementations pull revenue forward, especially if billing or revenue recognition starts at go-live.
- **Better services margin:** fewer fixed-fee overruns and write-offs.
- **Referenceability:** successful go-lives create references, which matter a lot in a small, word-of-mouth market like regional carriers.

**Costs**

| Item | Estimate | Notes |
|---|---|---|
| Implementation methodology, templates, configuration accelerators | ~$0.5–1M | One-time |
| Additional implementation and customer success staff | ~8 people × ~$150K ≈ $1.2M/yr | Ongoing |
| Integration connectors to core systems (Guidewire, Duck Creek, etc.) and data migration tooling | ~$1M/yr | Requires engineering, so it competes with Proposal A for the same people |
| Value-recovery program for stalled accounts | ~$0.3–0.5M | One-time or short-term |
| **Total** | **~$2.5–3M in year 1, ~$2M/yr after** | |

**When returns arrive**
- Rescues of the installed base: **6–12 months**.
- Shorter new implementations: visible within 2–3 quarters.
- Effect on churn among new cohorts: still lagged by contract terms.
- **Realistic payback: 12–18 months** if the diagnosis confirms that stalled adoption drives churn.

**Risks that could wipe out returns**
- **Treating the symptom.** If implementations are long because the product is hard to configure, adding services people is a permanent tax rather than a fix.
- **Headcount grows in step with customers,** which caps margin.
- **Genuine product gaps** mean well-onboarded customers still leave.

**Where spending can grow without profit**
- **Free "white glove" rescue work** that becomes the expected standard.
- **Unbilled customization** that creates technical debt.
- **Customer success headcount added reactively** to firefight rather than to prevent churn.

### Side-by-side (illustrative)

| | A: Roadmap | B: Services |
|---|---|---|
| Annual cost | ~$5M+ | ~$2.5–3M, falling to ~$2M |
| Time to first return | 18–24 months | 6–12 months |
| Revenue upside beyond retention | Yes (upsell, new logos) | Limited (services margin, faster revenue) |
| Effect on gross margin | Can erode it (inference costs) | Can erode it (services headcount) |
| Biggest failure mode | Features nobody can adopt | Headcount papering over product flaws |
| Capital at risk if the diagnosis is wrong | High | Moderate |

---

## 3. Governance: the structural problem

Right now the likely picture is:
- **Product** controls the roadmap budget but doesn't own renewals.
- **Services** controls delivery but doesn't own the product causes of long implementations.
- **Customer success (you)** owns the churn number but controls neither budget.

That is how churn doubles without anyone being accountable. Whatever you fund:

- **Give one person ownership of net revenue retention and gross churn,** with authority over the combined budget. That could be you, a Chief Customer Officer, or the GM.
- **Tie each proposal's budget to leading indicators its owner is measured on.**
  - Product: adoption of new features among live customers, attach rate, inference cost as a share of related revenue.
  - Services: median time to go-live, share of customers fully live within X months, overrun rate, health scores at renewal.
- **Set stop rules in advance, and have the CFO and CEO hold the kill switch rather than the spending VP.** Example: "If time to go-live hasn't dropped 25% in two quarters, we stop hiring implementation staff."

---

## 4. A third approach: a staged time-to-value program

This approach aims product engineering at the implementation problem instead of choosing between features and services. It uses less capital up front, and returns arrive sooner.

**Phase 0: Diagnose (weeks 0–6, ~$100K)**
Run the tests in section 1. This decides the split of spending in later phases.

**Phase 1: Protect the revenue at risk now (months 0–6, ~$0.5–1M)**
- Build a list of every account renewing in the next 18 months, scored by adoption depth.
- Run structured value-recovery sprints on the at-risk, high-revenue accounts.
- **This is the highest-return money in the whole plan.** Saving even $1.5M of ARR at 80% margin pays for the entire phase several times over.

**Phase 2: Engineer the implementation problem out of the product (months 3–15, ~$2–3M/yr, mostly reallocated rather than new)**
Point roadmap capacity at the things that make implementations slow:
- Configuration tooling so business users can set up rules without services work.
- Prebuilt integration connectors to the major core systems.
- Data migration tooling.
- In-product onboarding and usage telemetry.

This lowers services cost and improves retention at the same time, and it improves gross margin instead of eroding it.

**Phase 3: Close the analytics gap cheaply first (months 3–12)**
- **Embed or partner before building.** An embedded BI tool on the claims data you already hold, or a partnership with an established claims-AI vendor, can close the visible gap in months at lower fixed cost.
- **Price it as a paid module,** not a free giveaway.
- **Build proprietary AI only where win/loss data shows it decides deals,** and only once adoption proves customers use what exists.

**Phase 4: Scale whatever the data supports**
Release further budget in tranches, each against the pre-agreed metrics and stop rules above.

### Why this offers better returns for the capital at risk

- **Earliest returns:** the first money goes to saving revenue that is already at risk.
- **Lower capital at risk:** peak new spending is probably ~$3–4M rather than $5M+, and much of it is reallocated engineering capacity.
- **Margin improves on both sides:** less services labor per implementation, and no large bundled inference costs.
- **Reversible:** each tranche can stop if its metrics don't move.
- **Both VPs get something defensible,** tied to evidence rather than advocacy.

---

## Bottom line

My working hypothesis, to be tested rather than assumed: **stalled time-to-value is the primary driver, and it gets reported as a product gap.** If your diagnosis shows healthy, fully adopted customers leaving for competitors while your win rates fall, the VP of Product is right and you should shift capital toward the roadmap.

Either way:
1. Diagnose first.
2. Spend on the renewal pipeline immediately.
3. Point engineering at configurability and integration.
4. Partner before building AI.
5. Put one person in charge of churn, with stop rules the spenders don't control.

If you share actual ARR, churn by cohort, implementation durations, and contract terms, I can replace the illustrative numbers with a real model.

## Turn 2

**User:** You call Phase 2 "mostly reallocated rather than new" spend, but pulling $2–3M of engineering off the roadmap for a year isn't free: what revenue do we forgo or put at risk by delaying those features, and does the plan still beat Proposal A once that opportunity cost is counted?

**Assistant:**

You're right, and "mostly reallocated" was the wrong framing. Reallocated engineering isn't free. Its cost is the value of the work it displaces, so I should have priced that in. Here's the corrected comparison, using the same illustrative model ($50M ARR, 250 carriers at ~$200K, 80% subscription margin, churn up from 7% to 14%, so about $3.5M of excess ARR lost per year).

## What delaying the roadmap costs

Assume Phase 2 pulls ~10–12 engineers (~$2.5M) off the existing roadmap for about a year. The roadmap doesn't stop, but features slip roughly 6–9 months. That slip costs money in four ways:

| Opportunity cost | Mechanism | Is it permanent? |
|---|---|---|
| **Delayed native AI/analytics upsell** | The paid module ships later, so attach revenue starts later | Mostly a delay, but some upsell goes to competitors in the meantime |
| **New-logo losses** | Competitive deals lost while you visibly lag on AI | **Yes.** Lost carriers sign multi-year contracts elsewhere. |
| **Worse product-driven churn** | Customers already leaving over feature gaps leave faster as the gap widens | **Yes** |
| **Contractual or promised roadmap items** | Features committed in contracts, RFP responses, or renewal negotiations | Potentially severe. Audit this before anything slips. |

Phase 3 (embedding or partnering for analytics) offsets part of the first two costs, though at lower margin because of revenue share.

## Does the plan still beat Proposal A?

The answer depends on what's actually driving churn, so I modeled three diagnoses over three years. Both plans are measured against the same baseline: churn stays at 14% and the roadmap continues at its current pace.

### Key assumptions (replace with your own)

- **A's cost:** 20 new engineers, ramping from $4M in year 1 to $5M per year, so $14M total. AI inference costs reduce module margin to about 65%.
- **Plan C's cost:** $2.7M in year 1, then $1.7M per year, so $6.1M total. This covers the diagnosis, the account-rescue program, services and customer success staff, and partner fees.
- **C's effect on churn:**
  - Recovers 50% of adoption-driven churn in year 1 and 60% from year 2 onward.
  - Recovers 25% of product-driven churn from year 2, through the partner analytics module.
- **A's effect on churn:**
  - Recovers 60% of product-driven churn from year 2, at half strength in year 2 while adoption ramps.
  - Recovers only 10% of adoption-driven churn, because new features don't fix onboarding.
- **Timing of saved revenue:** a cohort of customers saved in a given year contributes half a year of revenue that year and full years afterward.

### Mixed diagnosis (50% adoption-driven, 50% product-driven): 3-year gross profit

| Line item | Proposal A | Plan C |
|---|---|---|
| Churn recovered | +$1.3M | +$4.1M |
| Upsell: native AI module | +$1.8M | −$0.8M (forgone/delayed) |
| Upsell: partner module (lower margin) | — | +$1.0M |
| New logos | +$1.0M | −$0.6M (slippage, half offset by partner) |
| Worse product churn from roadmap slip | — | −$0.3M |
| Services savings (fewer overruns) | — | +$1.0M |
| Incremental spend | −$14.0M | −$6.1M |
| **Net** | **−$9.9M** | **−$1.8M** |

C's opportunity cost is about **$1.7M** of gross profit in this scenario. That's real, but it's small next to the roughly $8M difference in spend.

### All three diagnoses

| Diagnosis | A net | C net (after opportunity cost) | C's advantage |
|---|---|---|---|
| Mostly adoption (75/25) | −$11.6M | +$0.3M | ~$12M |
| Mixed (50/50) | −$9.9M | −$1.8M | ~$8M |
| Mostly product (25/75) | −$9.5M | −$4.4M | ~$5M |

In the product-driven case, C's opportunity cost grows to about $2.5M. The partner module no longer covers the competitive losses, and the slip makes product churn worse.

**So C still wins, but its lead shrinks the more churn is product-driven.** It's also worth being clear about why both plans look negative. Contract lag means feature-driven retention mostly pays off after year 3. Proposal A is really a bet on a permanent capability whose output compounds over time, and a three-year window structurally favors faster-payback options like C. At the end of year 3 in the mixed case, A's annual incremental gross profit (~$4M) still doesn't cover its annual team cost (~$5M). A therefore only works if the team keeps producing revenue-bearing features beyond what I've modeled.

## When the answer flips to A

In the product-driven scenario, A needs about $5M more gross profit over three years to match C. That happens if any of the following is true:

1. **The AI upsell is much larger than assumed.** For example, native AI reaches roughly $5M+ ARR by year 3, around three times my estimate, because carriers treat it as must-have.
2. **The market is tipping.** Win/loss data shows AI deciding most competitive deals, so every lost logo is also a lost reference in a small market.
3. **C's rescue work underperforms.** If C saves half the adoption-driven churn I assumed, most of its lead disappears.
4. **Contractual commitments** would be breached by the slip.

The diagnosis phase can test the first three, which is one more reason to run it first.

## How to shrink the opportunity cost

The model treats the slip as uniform, but you get to choose what slips:

- **Tag every roadmap item with the revenue attached to it:** pipeline deals citing it, renewals depending on it, and contractual commitments. Protect those items and let the rest slip. In most roadmaps, a meaningful share of items has no attributable revenue, and delaying them costs close to nothing.
- **Count Phase 2 as product, not just cost.** Configuration tooling and prebuilt connectors to core systems are sellable. "Live in four months instead of twelve" is a competitive claim that can recover some of the new-logo slippage.
- **Consider a small targeted backfill.** Hiring 5–6 engineers (~$1.3M/yr) dedicated to the features that win/loss shows decide deals would remove most of C's new-logo and product-churn opportunity cost. That still costs well under half of Proposal A.
- **Set a tripwire.** If the share of competitive losses citing AI or analytics rises above a set threshold for two consecutive quarters, fund the backfill automatically instead of relitigating the plan.

## Bottom line

Counting the opportunity cost, Plan C still beats Proposal A under all three diagnoses in this model. Its lead ranges from about $12M if churn is adoption-driven to about $5M if it's product-driven. The opportunity cost is roughly $1.2–2.5M of gross profit, which is real but far smaller than the ~$8M difference in spend.

The comparison turns on four numbers you can measure within weeks:
- how much churn is adoption-driven versus product-driven,
- how often AI or analytics decides competitive deals,
- how large the native AI upsell could realistically be, and
- which roadmap items carry revenue or contractual commitments.

If you can share those, I'll rerun the model with your figures. The ranking could change.

## Turn 3

**User:** Your model credits Plan C with recovering half of adoption-driven churn in year one but delays A's retention gains by contract lag. If C's rescues only land on the 12–18-month renewal window like everything else, how much of its roughly $8M lead survives?

**Assistant:**

Most of the lead survives, roughly $6M of the $8M in the mixed case. But the correction changes what that lead is made of, and that matters more than the number.

## The inconsistency cut both ways

You're right that I exempted C from the decision lag. Carriers decide 12–18 months before renewal, so rescue work in year 1 mostly reaches accounts whose minds are already made up. But I was also generous to A. I gave it half-strength retention gains in year 2, even though it needs about 12 months to build, 6–12 months for customers to adopt, and then the same decision lag. Applied consistently, A's retention gains barely start before year 3.

## Revised assumptions

An intervention only affects renewals whose decision point comes after the customer feels its effect.

**Plan C**
- Adoption-driven churn recovered: 10% in year 1 (late deciders and accounts still negotiating), 40% in year 2, 60% in year 3.
- Product-driven churn recovered via the partner module: 0% until year 3, then 25%.
- The penalty I charged C for the roadmap slip worsening product churn also shrinks, since that effect is lagged too.

**Proposal A**
- Product-driven churn recovered: 0% in year 2, 30% in year 3 (half of its eventual 60%).
- Adoption-driven churn recovered: 5% in year 3.

**Unchanged**
- Upsell and new-logo effects. Add-on modules and new deals aren't tied to renewal dates.
- Services savings.
- Spend on both sides.

## Mixed diagnosis, recomputed (3-year gross profit)

| Line item | A (original) | A (lagged) | C (original) | C (lagged) |
|---|---|---|---|---|
| Churn recovered | +$1.3M | +$0.2M | +$4.1M | +$1.8M |
| Worse product churn from slip | — | — | −$0.3M | −$0.1M |
| All other lines | +$2.8M | +$2.8M | +$0.4M | +$0.4M |
| Spend | −$14.0M | −$14.0M | −$6.1M | −$6.1M |
| **Net** | **−$9.9M** | **−$11.0M** | **−$1.8M** | **−$3.9M** |

## All three diagnoses

| Diagnosis | Original lead | Lag applied to C only | Lag applied to both |
|---|---|---|---|
| Mostly adoption (75/25) | ~$12M | ~$9M | ~$10M |
| Mixed (50/50) | ~$8M | ~$6M | ~$7M |
| Mostly product (25/75) | ~$5M | ~$4M | ~$5M |

Applied only to C, the lag costs it $1.5–3M. Applied honestly to both, it costs C about $1M net.

## What the correction reveals

C's lead survives mainly because it never came from churn timing. It came from spending $7.9M less. After the correction, C's churn recovery over three years is only about $1–2.5M of gross profit. Both plans lose money over three years in every scenario.

Three implications follow.

1. **C is a cheaper, lower-risk option, not a quick win.** I overstated its speed. Its advantage is that less capital is exposed while you learn which diagnosis is true.

2. **The fair comparison is at equal budgets.** A lead of $4–7M driven mostly by cost means a smaller Proposal A, say 10–12 engineers instead of 20, could roughly match C in the product-driven case. So the real choice is not features versus services. It is what the first ~$2M a year should buy, and what evidence releases the next tranche.

3. **Year-1 spend should follow the lag.** If returns can't arrive before the year-2 renewal cohort, don't hire C's full services team in month one. Front-load the cheap parts: the diagnosis, account triage, and implementation fixes for new customers (services savings aren't renewal-gated). Time the rescue headcount to the decision windows of year-2 renewals.

## How to rescue some of the year-1 value

Triage by where each account is in its decision, not by its renewal date. Pull historical data on when churning carriers actually signaled:
- non-renewal notices (contract notice periods, often 90–180 days, set a hard floor),
- RFP issuance,
- executive sponsor changes,
- usage drop-offs.

Accounts that haven't yet started evaluating alternatives are rescuable even inside the window. Accounts already running an RFP mostly aren't. Two other levers can move revenue before the renewal date: preventing downgrades (dropped modules, reduced claim volumes) and closing mid-term expansions. If your data shows late-deciding accounts are common, C's year-1 recovery could land between my original 50% and this revised 10%. That single number is worth measuring before you finalize staffing.

## Bottom line

With the lag applied consistently, C keeps a $5–10M advantage over three years, depending on diagnosis. That advantage now rests almost entirely on committing less capital, not on faster returns. It's still the better choice. The stronger conclusion, though, is to fund both teams in tranches against evidence, since neither plan pays back within three years.

## Turn 4

**User:** If both plans lose money over three years against a do-nothing baseline, how does a stripped-down option compare: just the diagnosis, renewal triage, and implementation fixes for new customers, at a fraction of C's $6.1M? And in what year does each option break even?

**Assistant:**

The stripped-down option wins on payback. In the mixed case it breaks even in year 4, versus year 6 for Plan C and year 8 at best for Proposal A. But it recovers only a small share of the churn problem, so the decision is really about sequencing, not choosing a winner.

## Option D: what it includes and costs

| Component | Year 1 | Year 2 onward |
|---|---|---|
| Diagnosis (cohort analysis, win/loss review, third-party exit interviews) | $0.10M | — |
| Renewal triage (~3 dedicated customer success managers, ranking accounts by where they are in their renewal decision) | $0.45M | $0.45M/yr |
| New-customer implementation fixes (methodology and templates, plus one implementation lead) | $0.60M | $0.20M/yr |
| **Total** | **$1.15M** | **$0.65M/yr** |

Over three years that's about $2.5M, roughly 40% of C's $6.1M. D includes no roadmap diversion and no partner module, so it carries no opportunity cost.

## Assumptions

These use the mixed diagnosis ($1.75M/yr of adoption-driven excess churn and $1.75M/yr of product-driven excess churn) and apply the renewal-decision lag consistently to all three options.

- **Triage without engineering fixes is weaker than C's full rescue program.** Many stalled accounts are stalled because the product is hard to configure, which triage alone can't fix. D recovers 5% of adoption-driven churn in year 1, 25% in year 2, and plateaus at 35% from year 3 (C plateaus at 60%). It recovers no product-driven churn.
- **New-customer fixes pay off slowly.**
  - Services savings from fewer overruns arrive early but stay modest: $0.1M in year 1, then $0.3M/yr.
  - The churn benefit on new cohorts barely registers until years 4–6, because those customers' first renewals are 3–5 years out.
- **A and C** carry forward the year-by-year figures behind the last model:
  - C's spending continues at $1.7M/yr.
  - A continues at $5M/yr.
  - A's win-rate advantage persists indefinitely, which is generous to A.

## Cumulative net gross profit vs. doing nothing (mixed diagnosis)

| End of year | A | C | D |
|---|---|---|---|
| 1 | −$4.0M | −$2.4M | −$1.0M |
| 2 | −$8.2M | −$3.5M | −$1.1M |
| 3 | −$11.0M | −$3.9M | −$0.8M |
| 4 | −$11.9M | −$2.8M | **+$0.1M** |
| 5 | −$10.9M | −$0.4M | +$1.6M |
| 6 | −$8.3M | **+$3.4M** | +$3.7M |
| 7 | −$4.2M | +$8.3M | +$6.3M |
| 8 | **+$1.6M** | | |

## Break-even summary

| Option | Annual cash flow turns positive | Cumulative break-even | Largest cumulative loss |
|---|---|---|---|
| **D** | Year 3 | **Year 4** | ~$1.1M |
| **C** | Year 4 | **Year 6** | ~$3.9M |
| **A** | Year 5 | **Year 8** (year 7 if the team shrinks to ~$3M/yr after year 3; possibly never if competitors close the AI gap) | ~$11.9M |

**Sensitivity of D to the diagnosis:**
- Mostly adoption-driven churn: early year 4. There's more churn for triage to catch.
- Mostly product-driven churn: about year 6. D doesn't touch the actual problem. That is also the scenario where A's case is strongest.

## What the numbers mean

**1. D has the best return on capital, but it doesn't fix the problem.** At its plateau, D recovers about $0.6M of the $3.5M in excess ARR you lose each year. C recovers about $1.5M. A recovers about $1.2M, plus upsell and new logos. D is profitable because it's cheap, not because it's effective. By year 5 you'd still be losing most of the excess churn.

**2. C's additional spend over D has a poor stand-alone payback.** The extra ~$3.6M that C spends over three years doesn't break even against D until about year 6. That's too slow to fund on faith. It's worth funding only if the diagnosis shows D's triage is plateauing because of configurability and integration problems, which C's engineering work would fix.

**3. If the company's value is judged on ARR, break-even understates the bigger programs.** If you expect to raise capital or sell the company, retained ARR is valued at a revenue multiple. That makes the larger recoveries from C, or a targeted A, worth more than their gross-profit break-even suggests.

## Caveats that affect all three options

- **Saved customers are treated as saved permanently.** In reality they'd churn at your normal ~7% rate afterward. Correcting this pushes every break-even out slightly and trims C's late lead most, because C has the largest saved base.
- **D's saves are the most fragile.** Triage without root-cause fixes can postpone churn rather than prevent it. Rescued accounts may leave at their next renewal. If your data shows that pattern, D's plateau is lower than 35%.
- **Contract terms drive everything.** With shorter contracts, returns arrive sooner for all options. With longer ones, returns slip later, and D's head start becomes more valuable.

## Recommendation

Run D now as the first funding tranche, not as the final plan. It risks about $1M at peak, pays back around year 4, and produces the diagnosis that decides the next move. Then use explicit triggers:

- **Add C's engineering components (configuration tooling and integration connectors) if:**
  - triage saves stall because accounts can't reach value in the product as it stands, and
  - cohort data confirms that stalled adoption drives churn.
- **Add a targeted slice of A (5–6 engineers on deal-deciding features) if:**
  - fully adopted customers are leaving for competitors, and
  - win/loss data shows AI or analytics deciding competitive deals.
- **Stay with D only if** the diagnosis shows most excess churn is uncontrollable, for example carrier M&A. D's profitability is not a reason to stop there, because it leaves most of the churn problem in place.

## Turn 5

**User:** What should we do?

**Assistant:**

**Start with the stripped-down option now, and make the bigger investments conditional on evidence you'll have within 90 days.** Don't approve the VP of Product's full roadmap acceleration or the full services build-out yet. You don't know which problem you have, and the cheap option is also the one that tells you.

All the figures below come from my illustrative model, so they'll shift once your real data is in.

## Next 90 days: diagnose and protect revenue (~$0.6M this quarter, ~$1.15M in year one)

**1. Run the diagnosis.** Owner: you, with finance and a third-party interviewer. Budget: ~$100K.
- Churn by adoption depth and by implementation cohort.
- Implementation duration and overruns against churn.
- Where churned customers went: a competitor, an in-house build, or carrier M&A.
- New-logo win/loss for the last 24 months, especially whether AI or analytics decided deals.
- Independent interviews with 15–20 churned and at-risk carriers.

**2. Stand up renewal triage.** Owner: you. Staffing: ~3 customer success managers, reallocated if possible.
- Rank every account renewing in the next 24 months by where it is in the renewal decision: usage trend, sponsor changes, RFP activity, notice-period dates.
- Put rescue effort on accounts that haven't started evaluating alternatives. Accounts already running an RFP are mostly lost.

**3. Fix implementation for new customers.** Owner: VP of Services.
- Standard methodology and templates.
- Go-live milestones in every new deal.
- Tracking of time to go-live and overruns from day one.

**4. Audit the roadmap for revenue attachment.** Owner: VP of Product.
- Tag each item with the pipeline deals, renewals, or contractual commitments that depend on it.
- This costs nothing. It tells you what could safely slip later if you choose to reallocate engineers, and it tests the product thesis with evidence.

Leave the current roadmap untouched during this phase.

## Governance: settle this now

- **One owner of churn.** One executive owns gross churn and net revenue retention, with authority over the retention budget across product, services, and customer success. If that's you, get it formalized. If not, get it assigned. The current split, where each VP controls spending but nobody owns the outcome, is how churn doubled without anyone being accountable.
- **The CEO and CFO hold the decision** on releasing further funding, using criteria agreed in advance. The VPs who would spend the money don't decide.
- **Tracked metrics:**
  - Renewal-risk saves.
  - Median time to go-live.
  - Implementation overrun rate.
  - Share of competitive losses citing AI or analytics.
  - Adoption depth at renewal.

## Day-90 decision gate

| If the data shows... | Then... |
|---|---|
| Churners mostly never reached full adoption, and triage saves stall on configuration and integration problems | Fund Plan C's engineering work (configuration tooling, prebuilt integration connectors), letting untagged roadmap items slip |
| Fully adopted customers are leaving for competitors, and AI or analytics decides competitive deals | Fund a targeted slice of the product plan: 5–6 engineers on the deal-deciding features. Pilot an embedded or partner analytics module first |
| Both | Fund both, sized to each problem's share of churn |
| Mostly carrier M&A or other churn you can't control | Stay lean, and put the money into new-logo growth rather than retention |

Whatever you fund, set stop rules at the outset. For example: if median time to go-live hasn't fallen 25% within two quarters, stop adding implementation headcount.

## What to tell the two VPs

**Both of you may be right, and the data will size each problem.** Spell out what that means for each side:
- **VP of Product:** the product thesis gets tested through win/loss data and the roadmap audit, and a clear signal gets funded quickly.
- **VP of Services:** onboarding improvements start now, and deeper investment follows if the cohort data backs it.

Neither loses the argument. Both get funding tied to evidence.

## What would change this recommendation

- **A renewal cliff.** If several large carriers renew in the next 6–12 months and are visibly at risk, spend more on triage immediately rather than waiting for the diagnosis.
- **Fast competitive tipping.** If you're losing most competitive deals over AI right now, start the partner analytics pilot in parallel with the diagnosis rather than after it.
- **A near-term fundraise or sale.** Retained ARR is worth more than its gross-profit payback suggests, which strengthens the case for larger programs.

## This week

1. Ask finance for churn, renewal, and implementation data by account and cohort for the last 36 months.
2. Get retention ownership and the day-90 decision gate agreed with the CEO.
3. Pull the list of accounts renewing in the next 24 months and start ranking them.

Once the data is in, send me the actual figures and I'll rerun the model to size the day-90 decision.

## Outcome summary (sent to Jev)

The assistant recommends starting with a stripped-down option now and making larger investments conditional on evidence available within 90 days. Neither the VP of Product's full roadmap acceleration nor the full services build-out should be approved yet, because nobody knows which problem is driving churn. The cheap option is also the one that reveals it. In the illustrative model, this option costs about $1.15M in year one, risks roughly $1M at peak, and breaks even around year 4, versus year 6 for a fuller time-to-value program and year 8 at best for roadmap acceleration. Its weakness is that it recovers only a small share of the excess churn, so it is a first tranche, not the final plan.

The first 90 days involve four steps:

- **Diagnosis (about $100K):** churn by adoption depth and implementation cohort, overruns against churn, where churners went (including carrier M&A), win/loss on whether AI or analytics decided deals, and 15–20 independent interviews.
- **Renewal triage:** about three customer success managers rank accounts renewing in the next 24 months by where each is in its decision, focusing on accounts not yet evaluating alternatives.
- **New-customer implementation fixes:** standard methodology, go-live milestones, and tracking of time to go-live.
- **Revenue-attachment audit of the roadmap:** each item is tagged with the deals, renewals, or contracts that depend on it. The roadmap itself stays untouched.

Governance matters as much as spending. One executive should own churn and net revenue retention, with authority over the retention budget. The CEO and CFO, not the spending VPs, should release further funding against pre-agreed criteria and stop rules.

At day 90:

- If stalled adoption and configuration or integration problems dominate, fund engineering for configuration tooling and connectors.
- If adopted customers are leaving for competitors over AI, fund 5–6 engineers and pilot a partner analytics module.
- If both apply, fund both, sized to each problem's share of churn.
- If churn is mostly uncontrollable, stay lean and invest in new-logo growth.

The figures are illustrative. Three conditions would change the plan: an imminent renewal cliff calls for more triage now, rapid competitive tipping calls for starting the partner pilot in parallel, and a near-term fundraise or sale strengthens the case for larger programs.
