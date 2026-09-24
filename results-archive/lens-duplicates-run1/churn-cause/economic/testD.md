# churn-cause/economic/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:59:57.947942+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

## Response

# Diagnosing Churn and Choosing Where to Invest

## Short answer

You can't yet know which VP is right. The data that would settle it is probably already in your systems, and a few weeks of analysis would be cheap compared with the money at stake.

My working hypothesis is that both are partly right, about different things:

- **Services is more likely right about why current customers leave.** Customers who never reach full value are the ones most open to a competitor's pitch.
- **Product is more likely right about future growth**: new-logo win rates, expansion revenue, and churn risk among your best-adopted customers.

The two problems also compound each other. AI and analytics depend on clean, well-configured data, which comes from good implementation. Features shipped into a product customers can't fully implement widen the value gap instead of closing it.

Exit interviews can mislead you here. Departing customers often cite "better analytics elsewhere" because it's a neutral, blameless reason. If a churned customer who cited missing analytics never used your existing reporting, the real problem was value realization, not a feature gap.

## Step 1: Settle the argument with data (4–6 weeks, low cost)

For every customer that churned or gave notice in the last 24 months, plus everyone renewing in the next 18 months, pull the following:

| Signal | Points to Services | Points to Product |
|---|---|---|
| Implementation status at churn | Never fully live; modules unimplemented | Fully live for years |
| Implementation duration vs. plan | Big overruns | On time |
| Adoption depth (% of claims processed in system, active users, modules used) | Low or declining | High |
| Use of your existing analytics | Rarely used | Heavily used, hitting limits |
| Support ticket volume and severity | High, unresolved | Normal |
| Competitor named in loss | Any competitor, or "went back to legacy" | Specific competitor, with AI/analytics named in the RFP |
| New-logo win/loss | — | Losing deals on analytics/AI |

Also separate out **non-addressable churn**: carrier M&A, insolvency, and core-system replacements. Regional carrier consolidation alone can explain a lot of churn. Neither VP's plan fixes it, so it shouldn't count toward either business case.

If you can, have a third party run 10–15 interviews with churned customers. Customers tell vendors what's polite and tell third parties what's true.

## Step 2: Follow the money, using an illustrative model

I don't have your numbers, so here is a hypothetical base you can replace with your own:

- **Base:** 120 customers at an average of $400K ARR, so $48M ARR, with 80% subscription gross margin.
- **Churn:** doubled from 6% to 12%, so you lose about $5.8M ARR a year instead of $2.9M. The **excess churn is about $2.9M ARR a year, and it compounds.**
- **Value of one point of churn:** about $480K ARR a year, or about $384K a year in gross profit, recurring for every subsequent year.
- **Hypothetical diagnostic result:**
  - 60% of excess churn is value realization (~3.6 points).
  - 25% is competitive feature gaps (~1.5 points).
  - 15% is non-addressable (~0.9 points).

### Proposal A: Accelerate the product roadmap (analytics and AI)

**Revenue it could protect**
- Only the feature-gap slice of churn. In this example that is about 1.5 points, or roughly $720K ARR a year.
- Only for customers whose renewal comes after the feature ships *and* after they've adopted it.

**Revenue it could generate** (this is the stronger part of the case)
- **Add-on revenue.** If 30% of customers buy an analytics/AI module at a 15% uplift, that is about $2.2M ARR, ramping over years 2–4.
- **Higher win rates** on new logos, if you're currently losing on analytics.

**Costs**
- Perhaps 15–20 additional engineers, data scientists, and ML staff at about $4M a year. This is recurring, and it won't go away.
- **AI inference and data costs sit in cost of goods sold.** They scale with usage. Unless they're priced in, they erode gross margin.
- Compliance and model governance. Many states have adopted the NAIC model bulletin on insurers' use of AI, so carriers will ask you for documentation, bias testing, and explainability.
- Watch the accounting. Capitalized development can make EBITDA look better while cash goes out the door.

**Timing of returns**
- Build takes 9–18 months, then general availability.
- Carriers then need 6–12 months to adopt, often including their own model-risk review.
- **Meaningful returns land in months 18–36.** Most of the at-risk renewals in your next 18 months will be decided before anything ships.

**Risks that could wipe out returns**
- Parity is a moving target. Competitors keep shipping.
- Customers can't adopt AI features because their data quality or configuration is poor, which is the services problem again.
- New features add implementation complexity and make onboarding worse.
- Inference costs outrun pricing.
- Regulation limits AI use in claims decisions.

**Where spending grows without profit**
- "One more feature to reach parity."
- Features built to win RFPs that existing customers never use.
- AI usage priced as free inclusions.
- Engineering headcount that stays after the push ends.

### Proposal B: Fix implementation and service first

**Revenue it could protect**
- The value-realization slice of churn. Recovering half of it (~1.8 points) is about $860K ARR a year.
- Part of this is fast: rescuing stuck customers who are renewing soon can show results within 2–4 quarters.

**Revenue and margin it could generate**
- **Services margin.** Long fixed-fee implementations with overruns are often margin-negative. Cutting a typical 14-month implementation to 9 could plausibly save $0.5–1M a year in unrecovered labor.
- **Earlier revenue.** Faster go-live pulls forward expansion revenue, and any go-live-triggered subscription ramps.
- **Better references.** Referenceable customers improve win rates. This effect is slow but real.

**Costs**
- About $1.5M one-time for implementation methodology, preconfigured carrier templates, data-migration tooling, and a remediation team.
- About $1M a year ongoing for customer success and support capacity.

**Timing of returns**
- Remediation shows results in 6–12 months.
- Process improvements show up in new cohorts 12–24 months out.

**Risks that could wipe out returns**
- If churn really is competitive, a smoother onboarding into a product customers see as inferior just delays the loss.
- Delays caused by the customer's own IT, data, or staffing may not respond to anything you do.

**Where spending grows without profit**
- Solving the problem with headcount instead of fixing root causes such as poor configurability or manual data migration. Cost then scales linearly with customers.
- Unbilled white-glove work.
- Customer success managers quietly doing implementation work.
- A permanent heroics culture in which the same accounts get rescued every year.

### Side-by-side (illustrative)

| | A: Product acceleration | B: Services fix |
|---|---|---|
| Incremental spend, Year 1 | ~$4M+ (recurring) | ~$2.5M ($1.5M one-time) |
| ARR protected (steady state) | ~$0.7M | ~$0.9M |
| New/expansion ARR | ~$2.2M+ (uncertain) | Modest |
| Margin effect | Risk of gross-margin dilution | Services margin improves |
| Returns begin | Months 18–36 | Months 6–12 |
| Main failure mode | Builds the wrong thing, or the right thing customers can't adopt | Treats symptoms with headcount |

In this model, B pays back faster and more reliably on retention. A's case rests mostly on monetization and new logos, not on churn. That doesn't make A wrong. It means A should be judged as a growth investment, with growth metrics, rather than justified as a churn fix.

## Step 3: Who controls budget, owns results, and decides to stop

This is probably your biggest structural problem. Each VP controls their own spend, but the result, renewals, lands in *your* number. Neither of them currently bears the cost of being wrong.

I'd set up governance this way:

- **One owner of net revenue retention (NRR) and gross retention**, most likely the CEO or CRO, with the CFO as scorekeeper. Both VPs' budgets are justified against metrics that person owns.
- **Stage-gated tranches instead of annual budgets.** Each tranche gets pre-agreed leading indicators and kill criteria, written down before the money is spent.
  - Product examples: design-partner adoption, attach rate, win-rate change in deals where AI/analytics was a criterion, gross margin per AI feature.
  - Services examples: time-to-go-live, % of customers on the full module set within 12 months, health-score movement for at-risk accounts, services margin.
- **A stop rule.** If a tranche misses its gate, spending pauses automatically unless the NRR owner re-approves it. This prevents sunk-cost continuation.
- **The CFO tracks inference costs and unbilled services hours monthly.** These are the two places where spend quietly grows.

## Step 4: A third approach with better returns for the capital at risk

The idea is to **fund time-to-value first, including product work that shortens implementation, and treat AI as a narrow, priced bet. Pay for it mostly through reallocation.**

1. **Run the churn diagnostic now.** Cost is minimal. It decides how much goes to each track.

2. **Rescue at-risk renewals immediately.** Health-score every account renewing in the next 18 months and put a small cross-functional team on the savable ones. Save 5 of those $400K accounts and you've protected $2M ARR, the cheapest revenue available to you.

3. **Point part of the product roadmap at implementation itself.** Build data-migration tooling, preconfigured templates by line of business (workers' comp, personal auto, property), and **out-of-the-box analytics dashboards that are live on go-live day.** This single investment answers both VPs: customers get analytics, and they get value sooner. It also reduces services labor permanently instead of adding headcount.

4. **Make one or two targeted AI bets, not a platform race.** Pick use cases with measurable claims ROI, such as document extraction and first-notice-of-loss (FNOL) intake, triage and severity scoring, or subrogation and fraud flags.
   - Consider partnering or white-labeling before building.
   - Price them as add-ons with a gross-margin floor.
   - Pilot with 3–5 design-partner customers, ideally at-risk ones that are well implemented. That turns the pilot into a retention tool as well.

5. **Change the commercial terms.**
   - Tie implementation fees to milestones.
   - Offer at-risk accounts early multi-year renewals, paired with a committed value plan and roadmap access.
   - Stop selling configurations you can't implement on time.

6. **Protect profitability.** Cap net-new spend. For example, hold Year 1 to roughly $2.5–3M, funded largely by moving engineering capacity off low-usage roadmap items. Add AI investment only after the pilots pass their gates.

In the illustrative model, this approach puts most early dollars where payback is 6–12 months: rescue work and time-to-value tooling. It builds analytics that customers will actually adopt, because it arrives with implementation. It limits AI risk to small, priced, reversible bets. The product side keeps a growth agenda and the services side gets root-cause fixes, and both are measured against one retention number owned by one person.

**Your immediate next move** is to propose the diagnostic to the CEO and CFO as the way to settle the debate between the two VPs, and to bring the list of 18-month renewals, ranked by risk. That list turns the conversation from opinions into dollars.

## Summary (sent to Jev)

The response says neither VP can yet be shown right. The deciding data likely already exists, and a few weeks of analysis is cheap relative to the stakes. Its working hypothesis is that Services is probably right about why current customers leave, since customers who never reach full value are most open to competitors, while Product is probably right about future growth. The two problems compound because AI and analytics depend on well-implemented data. It cautions that exit interviews citing "better analytics" can mask value-realization failures.

It proposes a four-to-six-week diagnostic across churned and upcoming-renewal accounts. The diagnostic would look at implementation status and overruns, adoption depth, use of existing analytics, support tickets, competitors named, and new-logo win/loss. It would separate out non-addressable churn such as M&A, and use third-party interviews with churned customers.

An illustrative financial model shows the services fix paying back faster and more reliably on retention. The product push is framed as a growth investment with recurring costs, gross-margin risk from inference costs, compliance burdens, and returns arriving only in months 18 to 36.

On governance, it recommends a single owner of net and gross retention, with the CFO as scorekeeper. Spending would be released in stage-gated tranches with pre-agreed kill criteria, and inference costs and unbilled services hours would be tracked monthly.

Its preferred third path has six parts:
- Run the diagnostic.
- Rescue at-risk renewals.
- Direct product work at implementation, including migration tooling, templates, and go-live analytics dashboards.
- Make one or two narrow, priced AI pilots with design partners.
- Change commercial terms.
- Cap net-new spend largely through reallocation.

The immediate next step is to bring the diagnostic proposal and a risk-ranked renewal list to the CEO and CFO.
