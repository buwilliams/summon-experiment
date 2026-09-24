# critical-rationalism/churn-cause/testD

Model: claude-opus-5-5 · 2026-09-24T14:48:15.486307+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I don't need certainty; I want the most reasonable explanation we can act on now and correct as we learn. Treat each belief as a conjecture: what does each one claim is going on, and why? Whose values and goals is each one built around, and are they the ones that matter most here? What might both be leaving out that could change the outcome? Which assumption is most worth checking first, and what is a quick way to check it? And is there a better explanation that fits the same facts than either one?

**Assistant:**

# Diagnosing a Doubled Churn Rate: Two Conjectures and a Better Test

## Short answer

Neither belief should be adopted yet. They aren't wrong, but they are **untested and partly unfalsifiable as currently stated**. Each VP can explain any churned account after the fact. The good news is that you can probably discriminate between them in two to three weeks with data you already have, because they make different predictions about *which* customers leave and *where they go*.

My provisional bet: the most reasonable working explanation is a **time-to-value problem concentrated in a specific cohort**, with an external market factor possibly layered on top. Details below. First, each conjecture on its own terms.

---

## 1. What each conjecture claims

**Product-gap conjecture (VP Product)**
- *Mechanism:* The market's bar rose. Competitors shipped analytics/AI, buyers compared, and at renewal we lost on capability.
- *Implicit assumption:* Customers were getting value from what we have. They just want more, and someone else offers it.
- *What it predicts:*
  - Churn among **well-implemented, actively used** accounts.
  - Losses to **named competitors** whose feature differences show up in the decision.
  - Churn spread across tenure, including long-time happy customers.
  - Feature requests for analytics/AI rising in QBRs *before* churn.

**Service-experience conjecture (VP Services)**
- *Mechanism:* Customers never reach full value because implementations drag, adoption stalls, and support frustrates. At renewal they're paying for something they never got.
- *Implicit assumption:* The product is good enough *if* customers get it working.
- *What it predicts:*
  - Churn concentrated in accounts with **overrun implementations, low adoption, and unresolved escalations**.
  - Disproportionate churn at **first renewal**.
  - Losses to *anyone*, including a competitor with a simpler pitch, a return to the legacy system, or in-house tools.
  - Healthy, fully-adopted accounts renewing at roughly historical rates.

These are distinguishable. That's the most important thing about them.

## 2. Whose values each is built around

Each belief is centered on its author's function, and each conveniently concludes that its author's organization needs more investment. That doesn't make either wrong. It does mean neither should be accepted on the strength of conviction alone.

- **Product view** centers the *evaluator*: the executive who sees demos, reads analyst reports, and feels AI pressure from their board. It also fits the company's growth narrative and new-logo sales.
- **Services view** centers the *operator*: the claims ops team, IT, and adjusters who live through the implementation and use the system daily.

**Whose values matter most here** is the person who makes the renewal decision and what they're measured on. At a regional carrier, that's typically a claims executive or COO judged on loss-adjustment expense, cycle time, adjuster productivity, leakage, and regulatory compliance, with a CFO watching cost. Neither VP's framing starts from "what outcome did this buyer need, and did they get it?" That's the lens to use.

Your own function has a stake too. Churn often lands on CS's scorecard. It's worth having someone outside all three groups run the analysis, or at least review it.

## 3. What both leave out

Both conjectures assume churn is **internally caused and a single phenomenon**. Several things could break that assumption:

1. **Market structure.** Regional carriers consolidate. An acquired carrier often migrates to the acquirer's systems regardless of how happy it was. Carriers replacing core systems increasingly buy suites (Guidewire, Duck Creek, etc.) where claims comes bundled. Neither better AI nor better onboarding saves those accounts. The relevant gap there is *integration or platform fit*, not features.
2. **Cohort and fit shift.** A doubling that shows up over 18 months often traces back to something that changed two to three years ago:
   - Sales moving into smaller carriers with thin IT teams.
   - A pricing or packaging change.
   - A comp plan that rewarded closing marginal deals.
   - A batch of 3-year contracts all reaching renewal now.
3. **Renewal economics.** Price increases at renewal, changes in contract terms, or budget cuts at carriers after bad loss years (cat events, auto severity inflation) can drive churn that customers *describe* as product or service dissatisfaction.
4. **Champion loss.** Turnover of the sponsor who bought you is one of the strongest churn predictors in B2B, and it fits neither story.
5. **The false product/services divide.** Long implementations are frequently a *product* problem: weak configuration tooling, poor data migration, missing APIs, brittle integrations with policy and billing systems. "Fix services" may really mean "fix the parts of the product that make implementation hard." That's neither VP's roadmap.
6. **Stated vs. revealed reasons.** Exit interviews are notoriously unreliable. "Your competitor has better AI" is a polite, face-saving reason. "We never got it working" or "our new parent company decided" are the less comfortable truths. Weigh what customers *did* (usage, escalations, destination) over what they *said*.

## 4. The assumption most worth checking first

**Check whether churn is one thing, and where churned customers went.**

This single check splits the hypotheses fastest. If churned accounts mostly went to feature-rich competitors after successful implementations, the product view gains a lot. If they mostly had stalled implementations, the services view gains. If they went to suites or acquirers, both are largely beside the point.

**Quick way to check (roughly 1–2 weeks):** Churned logos at regional carriers over 18 months are probably a manageable number. Build a one-row-per-account table for every churned account, plus a comparison set of renewed accounts from the same period.

| Field | Why it matters |
|---|---|
| Deal signed date, segment, size, sales rep | Cohort/fit shift |
| Implementation planned vs. actual duration; did they fully go live? | Services hypothesis |
| Adoption at churn (active users, modules in use, % of claims in system) | Did they ever reach value? |
| Open escalations / CSAT trend in final 12 months | Service experience |
| Tenure at churn (first renewal or later?) | Early vs. mature churn |
| **Destination**: named competitor, core suite, acquirer's system, legacy/in-house, unknown | Discriminates most sharply |
| M&A, core-system replacement, or champion departure in final year? | External causes |
| Price change at renewal | Renewal economics |
| Feature requests logged pre-churn | Product hypothesis |

Then run **8–10 short conversations with former economic buyers**, ideally conducted by someone neutral rather than their old CSM or sales rep. Ask about the decision process and alternatives considered, not about satisfaction.

**Set decision rules before you look**, so the data can't be read to fit anyone's prior:
- **Churn concentrated in unfinished or low-adoption implementations, healthy accounts renewing fine:** time-to-value is primary. Prioritize implementation, including the product work that shortens it.
- **Well-adopted accounts leaving for competitors that win on analytics/AI:** product gap is real. Accelerate targeted roadmap items, specifically the ones buyers cited, not "AI" generically.
- **Large share lost to suites, acquirers, or budget cuts:** this is a strategy problem. Look at integration and partnerships with core platforms, segment focus, and contract structure.
- **Churn concentrated in a sales cohort or segment:** fix targeting and qualification. The other fixes won't reach the root.

## 5. A better explanation?

Here's a candidate that fits the same facts and explains why two smart VPs see different things:

> **A cohort of customers, likely those sold in a particular period or segment, never reached full value because implementations were harder than expected. Part of that difficulty is product: configuration, migration, integration. When those customers hit renewal, competitors' analytics/AI demos looked compelling next to a system they'd never fully used. Some additional churn comes from market consolidation that neither fix would prevent.**

Why it's more plausible than either VP's view:
- It explains why **Product hears "missing features"**: that's what departing buyers say, and it's what competitors demo.
- It explains why **Services sees stalled implementations**: those are the accounts that leave.
- It accounts for the **timing** of a doubling, which a slow-moving feature gap explains poorly unless a specific competitor launch lines up.
- It makes a sharp, checkable prediction: **fully adopted customers should be renewing at close to historical rates.** If they aren't, this explanation is wrong and the product view gets much stronger.

Treat it as a conjecture too. The table above tests it as well as the other two.

## 6. What to do now, before the evidence is in

- **Protect current revenue regardless of cause.** Take every account renewing in the next 6–12 months and flag the ones with low adoption, overrun implementations, open escalations, champion changes, or M&A activity. Run save plays now; they pay off under every hypothesis.
- **Hold large irreversible bets for two to three weeks.** That means major roadmap reprioritization or a services reorganization. The cost of waiting is small compared with the cost of spending a year building the wrong thing.
- **Instrument for the future.** Make time-to-first-value, go-live completion, adoption depth, and churn destination standard fields, so this question is answerable continuously rather than through a one-off investigation.
- **Revisit quarterly.** Whichever explanation wins, name the evidence that would overturn it, and look for that evidence on purpose.

The underlying reframe for leadership: the question isn't "product or services?" but **"which customers are leaving, did they ever get value, and where did they go?"** Answer that and the resource debate largely resolves itself.

## Turn 2

**User:** If churn turns out to be mostly a time-to-value problem, could the competitors' AI features still be costing us new deals, and should we check win rates before sidelining the product view?

**Assistant:**

Yes to both. A time-to-value finding would tell you why customers *leave*. It says nothing about why prospects *don't buy*. Those are different populations making different decisions on different evidence, so the product view deserves its own test before it's sidelined.

## Why the churn result doesn't settle the new-deal question

- **Different information.** A customer at renewal judges you on lived experience. A prospect judges you on demos, RFP checklists, analyst reports, and references. Features that barely matter once someone is using the system can matter a lot when they're comparing slide decks.
- **Different decision-makers.** New deals often involve executives and boards feeling "we need an AI strategy" pressure. Renewals are more influenced by operators who know whether the system works.
- **AI can be a filter even if it isn't the deciding factor.** If analytics/AI has become a required line in RFPs, you may be eliminated before anyone sees your implementation track record.

So it's entirely possible that fixing onboarding is right for retention *and* the feature gap is quietly shrinking your pipeline.

## The two problems also interact

- **A service problem can look like a product problem in sales.** Churned and frustrated customers make poor references, and long implementations are a known objection. Some deals your team loses "to AI" may really be lost on references or implementation risk.
- **A product fix can help both.** If implementation pain comes partly from the product (configuration, migration, integrations), that work shortens time-to-value for customers and becomes a selling point for prospects.

## How to check win rates without fooling yourself

CRM loss reasons are weak evidence on their own. Reps tend to attribute losses to product or price rather than their own execution. Look at patterns:

| Signal | Points toward an AI/feature gap | Points elsewhere |
|---|---|---|
| Win rate trend | Declines around specific competitor AI launches | Declines tied to sales team, pricing, or segment changes |
| Who beats you | Concentrated among AI-strong competitors | Spread across competitors, or "no decision" |
| Stage lost | Early: RFP shortlist, technical evaluation, demo | Late: price, references, contract terms |
| RFP content | AI/analytics requirements increasingly appear and are weighted | Present but treated as checkbox items |
| Deals won | Winners rarely cared about AI | Winners had similar AI requirements and chose you anyway |

To go beyond the pattern data:
- **Pull 12–18 months of closed deals** against an earlier baseline, split by competitor, segment, and stage.
- **Run 8–10 win/loss interviews** with prospects, including some you won, ideally through someone outside sales. Ask what eliminated or favored each vendor, not whether they liked your product.
- **Review recent RFPs** for how analytics/AI requirements are worded and weighted.

One nuance: in insurance, "AI" covers everything from fraud scoring to document intake to reserving support. Carriers are also increasingly cautious about AI governance under state insurance regulation. Find out *which* capabilities buyers ask for and what they need to trust them. "Accelerate AI" is too vague to act on.

## How to decide once you have both answers

Frame the choice around revenue at risk, not which VP was right:

- **Retention:** annual revenue lost to churn attributable to time-to-value.
- **Acquisition:** annual revenue in deals lost where feature gaps were plausibly decisive, especially early-stage eliminations.

If both are material, fund both, but sequence carefully. Onboarding fixes usually pay back faster because they protect revenue you already have, and they improve references for sales. Product investment should target the specific capabilities that are knocking you out of deals, plus any product work that shortens implementation.

The one outcome to avoid is letting a clean churn diagnosis become a verdict on the whole business. It answers the retention question. The win-rate analysis answers the growth question.

## Turn 3

**User:** Could some AI capabilities, like automated document intake or data-migration mapping, actually shorten implementation and time-to-value, making the two VPs' roadmaps less of an either-or than we're treating them?

**Assistant:**

Yes, and that's probably the most productive reframe available to you. But the overlap is real only where AI targets the actual bottlenecks in your implementations, so it's worth verifying before it becomes a slogan that lets both VPs claim victory.

## Where AI plausibly serves both roadmaps

**Shortening implementation (mostly used by your services team):**
- **Data-migration mapping.** Suggesting field mappings from legacy claims systems, flagging anomalies, normalizing messy historical data. Migration is often one of the longest, most error-prone phases.
- **Configuration assistance.** Translating a carrier's existing workflows, authority limits, and rules documentation into draft configuration.
- **Integration mapping.** Proposing mappings to policy, billing, and payment systems from their schemas or sample files.
- **Test generation.** Creating realistic test claims for user acceptance testing (UAT), which often drags.

**Accelerating time-to-value (customer-facing):**
- **Document intake.** Extracting data from FNOL submissions, police reports, medical bills, and correspondence. This can deliver a visible, measurable win (less manual keying, faster cycle time) early, which is exactly what stalled accounts lack.
- **In-product guidance for adjusters.** Speeds adoption and reduces "we went live but nobody uses it."
- **Support deflection.** An assistant grounded in your documentation and the customer's configuration.

These also help sales, but only if you can show the result. "AI-assisted implementation, live in X weeks instead of Y, with reference customers to prove it" answers the implementation-risk objection and the AI-checkbox question at once.

## Where the overlap breaks down

- **It only helps if AI hits the real constraint.** If most implementation delay comes from the customer side (slow decisions, scarce IT staff, internal politics, UAT scheduling), faster mapping moves the bottleneck without shortening the timeline.
- **Accuracy matters more than speed here.** Migration errors in reserves, payments, or claim history create financial and compliance problems. AI mapping needs human validation, so realistic gains may be 30% on a phase, not 90%.
- **Implementation AI and deal-winning AI may differ.** The capabilities that knock you out of RFPs might be fraud scoring, predictive severity, or reserving analytics, which don't shorten implementation at all. The win-rate analysis tells you how much overlap actually exists.
- **Customer-facing AI carries governance weight.** Intake and extraction are relatively low-risk. Anything influencing claim decisions draws more scrutiny under state AI regulations and carrier governance. Implementation tooling your own team uses is the lowest-risk place to start.

## How to check before committing

1. **Find out where implementation time actually goes.** Take your last 10–15 implementations and break down the weeks by phase: migration, integrations, configuration, training, UAT, and waiting on the customer. Your services team and project records can likely reconstruct this in a week or two. This tells you the maximum possible gain from AI tooling.
2. **Match AI to the biggest vendor-side phases.** If migration and configuration consume half the timeline and are mostly your team's effort, the case is strong. If waiting on the customer dominates, process and contract changes (clear customer commitments, decision deadlines) will beat AI.
3. **Pilot on one or two live implementations.** Try the most promising tool, such as migration mapping, and measure phase duration and error rates against comparable past projects before building it into the product.
4. **Cross-reference with win/loss findings.** Capabilities that shorten implementation *and* appear in lost-deal RFPs go to the top of the list.

## The organizational payoff

The bigger benefit may be structural. If both VPs share one metric, such as **time-to-first-value for new customers** alongside **competitive win rate**, the debate shifts from whose budget grows to which investments move both numbers. Items that serve both get priority. Items that serve only one compete on the revenue-at-risk math from before.

So the answer to "which VP is right" may turn out to be that each has half the problem, and some of the best investments sit where their halves overlap. The implementation breakdown is the fastest way to find out how large that overlap really is.

## Turn 4

**User:** If the breakdown shows most implementation time is spent waiting on the customer, would tougher contract commitments scare off the smaller, thinly staffed carriers we've been selling to, and are they even the customers we should be keeping?

**Assistant:**

Possibly, but tougher contracts are likely the wrong tool for this segment anyway. And whether to keep these customers is a question you can answer with numbers rather than instinct.

## Why stricter commitments may not fix the problem

For a thinly staffed carrier, "waiting on the customer" usually reflects **capacity, not unwillingness**. Their claims VP is also running daily operations, and their IT team may be three people handling everything. A contract clause requiring a dedicated project lead can't create a person who doesn't exist. The likely results:

- Some prospects walk away, which is fine if they would have churned but costly if they would have succeeded with a different approach.
- Others sign anyway, miss the commitments, and you end up with the same stalled implementation plus an awkward penalty conversation that damages the relationship.

Before redesigning contracts, confirm the diagnosis. In the implementation breakdown, check whether customer-side waiting **correlates with carrier size and staffing**. Larger carriers often wait too, but for different reasons: governance committees, procurement, competing IT priorities. Those call for different fixes.

## Alternatives that match the constraint

If small carriers lack capacity, adjust what you ask of them and what you provide:

- **Standardized packages.** Preconfigured workflows based on common regional-carrier practice, so the customer makes a dozen decisions instead of hundreds. Fewer decisions means less waiting.
- **Vendor-supplied capacity.** Your team does more of the work: data extraction, configuration, test execution. Price it explicitly as a managed implementation rather than absorbing it as overrun.
- **Phased go-lives.** Start with one line of business or one high-value capability, such as document intake, to get an early win before tackling the full migration.
- **Mutual commitments instead of penalties.** Named decision-makers and response windows on their side, matched by commitments on yours. It feels like a partnership rather than a trap.
- **Readiness assessment before signing.** A short, structured check of staffing, data condition, and decision authority. Use it to choose the right package and set realistic timelines, and occasionally to advise a prospect that they aren't ready yet.

These can also reduce the scare-off risk, because they lower the effort required of the customer rather than just raising the stakes.

## Should you keep serving this segment?

Answer this by building a **segment-level P&L**, not by debate. For small carriers versus the rest, compare:

- Customer acquisition cost and sales cycle length
- Implementation cost, including overruns and unbilled services hours
- Annual contract value and gross margin after support and services costs
- Churn rate, especially at first renewal
- Expansion revenue and reference value
- Support burden per account

This gives three broad possibilities:

1. **The segment is profitable if implementations succeed.** Keep it, and invest in the standardized, managed model above. This segment may even be defensible, since the large suite vendors often find small carriers uneconomic to serve.
2. **The segment is profitable only at higher prices or with a lighter product.** Redesign the offering: a packaged tier with limited customization, priced to cover the real cost of serving these carriers.
3. **The segment loses money even when things go well.** Stop actively selling there, and qualify harder going forward.

Also check **how much of your addressable market** these carriers represent. The regional carrier market is finite. If small carriers make up a large share of the remaining prospects, walking away shrinks your growth ceiling, and that tradeoff belongs in the decision.

## Separate existing customers from future sales

Whatever the answer, treat the two groups differently:

- **Current small-carrier customers** signed in good faith, often on a promise of easier implementation than they got. Honor those commitments, run save plays, and consider moving stalled accounts onto a more standardized or managed path. How you treat them also affects your reputation in a market where carriers talk to each other.
- **Future deals** are where you apply qualification, readiness checks, and redesigned packages.

## Check the incentives that created the problem

If the cohort analysis shows a rush of small-carrier deals in a particular period, look at what drove it: sales compensation, quotas, or a push into new territory. Unless compensation accounts for implementation success or first-renewal retention, the same pattern will recur whatever contract terms you set.

## A low-risk way to test

Rather than changing policy across the board, trial a readiness assessment plus a standardized package on the next several small-carrier deals. Track three things against recent comparable deals:

- **Win rate:** does it actually scare prospects off?
- **Time-to-first-value:** does it shorten implementations?
- **Early health signals:** adoption, escalations, and sponsor engagement at 6 and 12 months.

A deal lost before signing costs far less than a customer who churns after an expensive, stalled implementation. The goal isn't to avoid small carriers. It's to sell them only what you can actually deliver, in a way that works for them.

## Turn 5

**User:** What should we do?

**Assistant:**

## Bottom line

Don't pick a VP's side. Run a short, structured diagnosis, protect the revenue already at risk while it runs, and commit in advance to how the results will drive decisions. My provisional bet is still that time-to-value in a specific cohort is the main driver of churn, but you can confirm or overturn that within about six weeks without delaying anything that matters.

## Weeks 0–2: Protect revenue and launch the diagnosis

**1. Triage upcoming renewals now.** List every account renewing in the next 6–12 months and flag low adoption, overrun or incomplete implementations, open escalations, champion turnover, and M&A or core-system replacement activity. Assign save plays to the highest-risk accounts. This pays off whatever the diagnosis turns out to be.

**2. Start four analyses in parallel,** owned by someone neutral (finance, strategy, or an ops analyst), with both VPs reviewing the method but not running it:
- **Churn account table:** every churned account from the last 18 months, compared against renewed accounts, including destination, adoption, implementation history, tenure, cohort, and pricing changes.
- **Win/loss review:** 12–18 months of deals by competitor, segment, and stage lost, plus 8–10 interviews with prospects, including some you won, and a review of recent RFP requirements.
- **Implementation time breakdown:** your last 10–15 implementations, split into migration, integration, configuration, training, UAT, and waiting on the customer, cut by carrier size.
- **Segment P&L:** small carriers versus the rest, including acquisition cost, unbilled implementation hours, margin, churn, and expansion.

**3. Hold irreversible bets.** No major roadmap reprioritization or services reorganization until the results are in. Routine work continues.

**4. Write down the decision rules before seeing the data** and get both VPs to agree to them:

| If the data shows... | Then prioritize... |
|---|---|
| Churn concentrated in stalled or low-adoption implementations | Implementation: process, staffing, and product work that shortens it |
| Well-adopted accounts leaving for AI-strong competitors | Targeted product capabilities that buyers actually cited |
| Early-stage deal losses tied to analytics/AI requirements | Product investment for acquisition, sized by revenue at stake |
| Most implementation delay is customer-side, concentrated in small carriers | Standardized packages, managed implementation, readiness checks |
| Large share of churn from M&A or suite consolidation | Strategy: integrations and partnerships with core platforms, segment focus |
| Small-carrier segment unprofitable even when implementations succeed | Reprice, repackage, or stop actively selling there |

## Weeks 3–6: Decide and start pilots

**5. Allocate by revenue at risk.** Compare annual revenue lost to churn from time-to-value problems against revenue lost in deals where feature gaps were plausibly decisive. Fund in proportion to those numbers, with priority for investments that move both, such as AI-assisted migration mapping if migration turns out to be a major vendor-side phase.

**6. Launch two small pilots:**
- **Readiness assessment plus standardized package** on the next several small-carrier deals. Track win rate, time-to-first-value, and 6-month health against recent comparable deals.
- **AI-assisted implementation tooling** (whichever targets the largest vendor-side phase) on one or two live implementations. Measure phase duration and error rates against past projects.

## Months 2–6: Scale what works and fix the system

**7. Give both VPs shared metrics:** time-to-first-value for new customers and competitive win rate. This turns the debate from whose budget grows into which investments move both numbers.

**8. Fix incentives.** If a sales cohort drove the churn, tie part of sales compensation to implementation success or first-renewal retention.

**9. Take care of existing small-carrier customers.** Honor their contracts, move stalled accounts onto a standardized or managed path, and treat them as future references, not write-offs.

**10. Build permanent measurement.** Track time-to-value, go-live completion, adoption depth, churn destination, and loss reasons as standard fields so this question never again needs a one-off investigation. Review quarterly, and name the evidence that would overturn your current conclusion.

## Your first move

Bring this to your CEO or exec team as a joint plan, not as a verdict on either VP. Your position in customer success gives you credibility as the person closest to the customer, and your pitch is simple: *"We have two plausible explanations and possibly a third. Here's how we find out in six weeks, protect revenue meanwhile, and decide by rules we all agree on today."* That framing keeps both VPs invested, because each one's view gets a fair test, and it keeps the decision anchored to the customer.

## Outcome summary (sent to Jev)

The recommendation is not to side with either VP but to run a roughly six-week structured diagnosis, protect at-risk revenue meanwhile, and agree in advance on rules for how results will drive decisions. The provisional bet is that churn is mainly a time-to-value problem concentrated in a specific cohort, likely smaller, thinly staffed carriers. Part of that is product difficulty in configuration, migration, and integration, possibly with market consolidation layered on top. Both VPs' views are untested, and each conveniently favors its author's function. They also make distinguishable predictions about which customers leave and where they go.

Immediate actions:
- Triage renewals due in the next 6–12 months and run save plays on risky accounts.
- Have someone neutral run four analyses: a churned-versus-renewed account table including destination, win/loss review with interviews and RFP analysis, a phase-by-phase breakdown of recent implementations cut by carrier size, and a small-carrier segment P&L.
- Pause irreversible roadmap or services reorganizations.

Next, allocate investment by revenue at risk, favoring work that moves both retention and acquisition, such as AI-assisted migration mapping. Two pilots follow:
- Readiness assessments with standardized packages for small carriers.
- AI implementation tooling on live projects.

Longer-term steps:
- Give both VPs shared metrics: time-to-first-value and competitive win rate.
- Tie sales compensation to implementation success.
- Honor existing small-carrier contracts.
- Build permanent measurement.

Caveats: a clean churn diagnosis does not settle whether AI gaps cost new deals. AI helps implementation only if it hits vendor-side bottlenecks. Tougher contracts may not fit capacity-constrained carriers. Every conclusion should name the evidence that would overturn it.
