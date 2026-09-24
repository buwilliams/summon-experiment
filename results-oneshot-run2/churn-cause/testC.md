# churn-cause/testC

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T13:04:46.573321+00:00

## Prompt

Use the method of conjectures and refutations (critical rationalism) to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

# Churn Diagnosis Through Conjectures and Refutations

**Short answer:** Neither belief can be declared right yet, and asking "which one is right?" is itself a trap. In critical rationalism you don't choose the most persuasive theory. You treat each as a bold conjecture, work out what it *forbids*, and try hard to refute it. The one that survives serious attempts at refutation earns tentative acceptance. Both VPs' views can be tested against data you probably already have, within a few weeks.

---

## Step 1: State the conjectures sharply

Vague theories can't be refuted, so the first job is to make each claim precise enough to be wrong.

- **H1 (Product gap):** Customers leave because competitors offer analytics and AI capabilities we lack, and customers value those capabilities enough to switch.
- **H2 (Implementation and service):** Customers leave because they never reach full value from what we already sell, due to long implementations and poor support.

Both must also explain a fact that is easy to overlook: **churn doubled over 18 months.** A theory that only explains why churn exists, not why it *rose*, is incomplete.

- **H1 has a natural account of the change.** Competitors plausibly shipped AI/analytics features in the 2023–2024 generative-AI wave.
- **H2 must name something that got worse.** Candidates include implementation staff attrition, a shift to larger or more complex customers, outsourcing to a partner, or a product release that made setup harder. If implementations were always this long and churn used to be half as high, H2 is in trouble unless it can point to such a change.

**Ask each VP to write down, in advance, what evidence would make them abandon their view.** If either can't name any, their belief is currently unfalsifiable, which is a warning sign in itself. Pre-committing also stops both sides from reinterpreting whatever the data shows as support.

---

## Step 2: Derive risky, discriminating predictions

The valuable predictions are those where the two conjectures **disagree**. Evidence both theories expect, such as "churned customers complained," tests nothing.

| Test | H1 (Product) predicts | H2 (Service) predicts |
|---|---|---|
| **Churn vs. adoption/implementation quality** | Churn is roughly as high among well-implemented, high-adoption customers as among struggling ones | Churn is concentrated in low-adoption, long-implementation accounts; healthy accounts rarely leave despite lacking AI |
| **Where churned customers went** | To competitors with stronger analytics/AI | Often to simpler tools, the incumbent core-system vendor, or even a competitor with *fewer* features but a better rollout |
| **Timing in the lifecycle** | Churn hits tenured, mature customers too | Churn clusters at first renewal, before customers ever reach steady state |
| **Timing in the calendar** | The churn rise follows competitor feature launches | The churn rise follows an internal change: staffing, process, customer mix, a release |
| **The "missing" features** | Customers cite features we genuinely don't have | Customers cite features we *already have* but they never deployed or learned |
| **New-business win/loss** | Lost deals also cite analytics/AI, and win rates fell in parallel | Win rates are stable; the problem appears only post-sale |
| **Leading indicators** | Feature requests and competitor mentions rise before churn | Ticket escalations, falling CSAT, and stalled go-lives appear before churn |

The **first test, the 2×2 of adoption health against churn, is the most decisive.** If healthy, fully implemented customers are leaving at high rates, H2 as the main explanation is badly damaged. If they almost never leave, H1 is badly damaged, because those customers lack the AI features too.

The **"missing features" test is especially sharp.** "Your product lacks X" is a common, socially easy exit reason, and it's often wrong. If a meaningful share of cited gaps are capabilities you already ship, that is strong evidence for H2 masquerading as H1.

### A caution about evidence quality
Exit interviews and churn-reason fields are weak evidence. They're collected after the decision, often by the salesperson, and they favor face-saving answers. Prefer behavioral data: usage logs, implementation timelines, ticket histories, and where customers actually went. Use interviews to generate hypotheses, not to confirm them.

---

## Step 3: Don't limit yourself to two conjectures

A debate framed as A versus B often hides C. Credible rivals in regional insurance claims software include:

- **H3 (Carrier consolidation):** Your customers are being acquired, and acquirers standardize on their own systems. *Test:* what share of churned logos underwent M&A?
- **H4 (Core-suite bundling):** Policy/billing/claims suite vendors (Guidewire, Duck Creek, etc.) are bundling claims modules. *Test:* how many churned customers moved to their core-system vendor?
- **H5 (Budget pressure):** Poor underwriting results from catastrophe losses and claims inflation led carriers to cut vendor spend. *Test:* did churned customers downgrade or consolidate rather than switch to a richer product?
- **H6 (Cohort effect):** A sales push roughly three years ago brought in poor-fit customers whose multi-year contracts are now renewing. *Test:* is churn concentrated in a specific signing cohort or sales segment?
- **H7 (Champion loss):** Your internal sponsor left and the replacement had no attachment. *Test:* was there contact turnover in the 6–12 months before churn?
- **H8 (Reliability):** Performance or outage problems. *Test:* incident history of churned vs. retained accounts.

If H3, H4, or H5 explains a large share of churn, **both VPs' prescriptions could be expensive and largely beside the point.**

---

## Step 4: Anticipate that the answer may be an interaction

A plausible synthesis, offered as a further conjecture to test rather than a conclusion:

> **H1×H2:** Poor implementation leaves customers under-served and uncommitted, which makes them *vulnerable*. Competitor AI marketing then gives them a *reason* and a *story* to leave.

This conjecture makes its own risky prediction: **competitor AI pitches should win disproportionately against low-adoption accounts and fail against healthy ones.** If that pattern holds, fixing onboarding would reduce churn even without new features, while shipping features to customers who never adopt the existing ones would change little.

It may also turn out that different segments churn for different reasons, for example product gaps among larger carriers and service pain among smaller ones. That would make "which VP is right" the wrong question entirely.

---

## Step 5: What to do

### Next 2–4 weeks: run the refutation tests
Pull every churned account from the last 18 months plus a matched set of retained accounts. For each, capture:

- implementation duration and go-live status
- module adoption and usage depth
- time to first renewal
- support ticket and escalation history
- stated churn reason, and whether the cited feature actually exists in your product
- destination vendor
- M&A events
- signing cohort and segment
- contact turnover

Then run the tests in the table above. Present results against the criteria each VP committed to in advance.

### Meanwhile: take actions that double as experiments
Critical rationalism favors acting on the best-surviving conjecture while designing the action so it can be refuted.

1. **Launch a rescue program for at-risk, low-adoption accounts** with dedicated re-implementation support. Where possible, hold out a comparable group, or at least compare against prior renewal rates. If rescued accounts renew at markedly higher rates, H2 gains strong support. If they churn anyway, H2 is weakened.
2. **Run a structured test of H1 with at-risk accounts.** Show prototypes or a committed AI/analytics roadmap and measure whether renewal intent changes, in signed commitments rather than polite enthusiasm. If it changes little, H1 is weakened.
3. **Avoid irreversible bets until the data is in.** Don't restructure the roadmap or the services organization wholesale. Both are costly errors if the dominant cause turns out to be consolidation or bundling.

### Afterward: keep the theory open to revision
Whatever survives becomes your working explanation, not a permanent truth. Build the discriminating metrics into your ongoing customer health scoring:

- adoption depth
- time to value
- destination on churn
- competitor mentions

That way, the next shift in the market shows up as a failed prediction rather than another round of dueling opinions.

---

## Bottom line

Each VP has offered a conjecture. That is a good start, but neither has earned acceptance. The decisive question is whether **healthy, well-implemented customers are also leaving:**

- **If they are,** the product-gap theory survives and the service theory is badly weakened.
- **If they aren't,** the reverse holds.
- **If most churn traces to acquisitions, bundling, or budget cuts,** both theories fail and you need a different strategy.

Run the test, commit to the criteria in advance, and let the evidence do the refuting.

## Summary (sent to Jev)

The response argues that neither VP's belief can yet be declared right, and that asking which is right is a trap. Following critical rationalism, it treats each view as a conjecture to be sharpened and tested against data the company likely already has, within a few weeks. The product-gap theory easily explains why churn doubled, because competitors shipped AI features. The service theory must identify something that got worse, such as staff attrition or a shift in customer mix. Each VP should state in advance what evidence would make them abandon their view.

The central test is whether healthy, well-implemented customers are also leaving. If they are, the product theory survives. If they aren't, the service theory does. Other discriminating tests include where churned customers went, whether churn clusters at first renewal, whether the rise follows competitor launches or internal changes, and whether cited "missing" features actually already exist. The response warns that exit interviews are weak evidence compared with behavioral data.

It also proposes rival explanations: carrier consolidation, core-suite bundling, budget pressure, a poor-fit sales cohort, champion loss, and reliability problems. If consolidation, bundling, or budget cuts dominate, both VPs' prescriptions may miss the point. It suggests an interaction, in which poor implementation makes customers vulnerable and competitor AI gives them a reason to leave, and allows that segments may differ.

The recommended actions are to analyze churned and matched retained accounts. Meanwhile, the company should run a rescue program for low-adoption accounts, ideally with a holdout group, and test whether AI roadmaps change signed renewal intent. It should avoid irreversible roadmap or services restructuring. Afterward, it should build these metrics into health scoring.
