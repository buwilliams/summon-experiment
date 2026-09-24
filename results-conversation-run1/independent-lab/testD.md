# independent-lab/testD

Model: claude-opus-5-5 · 2026-09-24T13:37:00.959918+00:00

## Turn 1

**User:** I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

**Assistant:**

# Two Conjectures and a Third

## 1. What each belief actually claims

**CEO's conjecture (call it A):** The company has the capability it needs. Churn and lost deals come from a failure of *direction*: unclear priorities, low urgency, scattered effort. Give the existing machine a clear target and strong leadership, and it will produce.

**Your conjecture (call it B):** The company's structure is the problem. Approval gates, release cycles, incentives, budgeting, and risk norms are tuned to protect the existing business, and they systematically kill or dilute anything new. Better direction won't help, because the system's "antibodies" will reject new work regardless of who is steering.

Both are causal claims about *where the constraint lives*. A says it's in intent and focus. B says it's in structure and process.

## 2. What each predicts that the other doesn't

| Observation | If A is true | If B is true |
|---|---|---|
| Autopsy of recent stalled initiatives | They died from vague goals, shifting priorities, or weak ideas | They died in specific gates (security review, architecture board, release train, procurement, sales comp) *despite* executive backing |
| A small internal team given clear priority and CEO cover | Ships at reasonable speed | Still gets slowed, and cover can't remove the blockers |
| Time for a small change to reach a customer | Mostly active work; delays trace to competing priorities | Mostly waiting in queues and approvals |
| Internal people with good ideas | Rare, or ideas are weak | Plentiful, but they've learned not to try |
| Where recent novel capability came from | Internal teams, when focused | Acquisitions, partners, or informal skunkworks |

This table is your research agenda. Every row is observable within weeks.

## 3. Where each is easy to vary

**A is very easy to vary.** If a turnaround fails, the explanation adjusts: we lacked commitment, had the wrong people in key seats, didn't align enough. "Working within existing talent" can quietly expand to include new hires. As stated, A has no deadline and no measurable prediction, so it can absorb almost any outcome. That is its biggest weakness.

**B is also easy to vary, in a mirror-image way.** If the lab fails, it "wasn't independent enough." If the lab builds something impressive that never transfers back to the core business (the classic Xerox PARC problem), it can still be called a success. "Independent" is a dial you can keep turning. And the evidence that labs work is heavily survivorship-biased. Most corporate labs become innovation theater and are shut down within a few years.

Both views are also convenient for the people holding them. A protects the CEO's legitimacy and the existing org. B gives you autonomy, budget, and distance from the politics. That doesn't make either wrong, but it means you should hold yours to a higher standard, not a lower one.

**Hard-to-vary versions** would name the mechanism and a prediction, for example:
- **A:** "With clear priority, team X ships capability Y to three customers in 90 days."
- **B:** "Gates G1 and G2 will add at least 4 months to any new product, and CEO sponsorship won't remove them."

## 4. A third explanation that may fit the facts better

Notice what the facts actually are: **customers are churning, and the company is losing new deals.** Neither of those is evidence of an innovation problem specifically. In insurance software, churn usually comes from:
- implementations that take 12–24 months,
- painful upgrades,
- stability issues,
- cost,
- service quality, or
- a competitor that is cloud-native while you aren't.

**Conjecture C:** The binding constraint is a specific, diagnosable weakness in the core value proposition or delivery. The "innovation org design" debate is mostly downstream of it.

C explains the same facts as A and B, and makes a sharp prediction: churned customers and lost prospects will cite core reasons, not missing novel capabilities.

C also exposes a problem with B. Even if B is correct about structure, an independent lab takes 18–36 months to matter. It doesn't stop customers leaving next quarter.

A refinement of C: the constraint is **local**. There are probably two or three specific gates or incentives doing most of the damage. If so, the right response is neither "work within everything" nor "build outside everything." It is targeted exemptions, a protected team with defined interfaces back into the core.

## 5. The cheapest tests, roughly in order

**1. Talk to churned customers and lost deals (2–3 weeks).**
- Run 10 churned-customer interviews and 10 lost-deal interviews, ideally not conducted by sales.
- If the reasons are core (implementation, cost, stability), C gains and both A and B lose relevance.
- If the reasons are "competitor had capability X," ask whether X was known internally and couldn't get built (supports B) or never occurred to anyone (a sensing problem, not a structure problem).

**2. Autopsy 3–5 recent stalled or killed initiatives (2 weeks).**
- Trace the cause of death for each.
- Deaths in structural gates despite backing support B.
- Deaths from vague goals or weak ideas support A.

**3. Trace one small change end to end (1–2 weeks).**
- Pick a real, small change and follow it from idea to customer.
- Measure waiting time versus working time.
- This reveals where the constraint physically sits.

**4. Run a tracer-bullet pilot (6–8 weeks).**
- Put a 4–6 person team inside the company on one customer-facing problem surfaced by test 1.
- The CEO grants explicit, written exemptions in advance.
- Log every obstacle, with dates.

The pilot is designed so both views can fail:
- **A is refuted** if the team is blocked by gates that even the CEO's cover can't clear.
- **B is refuted** if the team ships with only minor exemptions, which would show that full independence is unnecessary.

The CEO's willingness to grant the exemptions is itself data about A.

## 6. Verdict

Neither view survives criticism as currently stated.

- **A is weaker**, because it is vaguer and makes no risky predictions.
- **B has a real mechanism**, but it carries a well-known failure mode (the transfer problem), and it doesn't address the most urgent symptom, churn.
- **C currently survives best.** It explains the same facts, makes sharper predictions, and is cheapest to test.

## 7. The practical upshot

You don't have to win an argument with the CEO in your first 90 days. You can turn the disagreement into a joint experiment: "Let's find out where the constraint actually is. Here are four tests. Here's what result would change my mind, and here's what would change yours."

That positions you as the person who resolves the question rather than the new hire who wants to leave the building. And if B turns out to be right, you'll have the evidence to get the independence you need.

## Turn 2

**User:** Isn't C just as easy to vary as A and B, since "a weakness in the core value proposition" can absorb almost any interview result, and churned customers tend to give safe post-hoc reasons like price or implementation pain? And if the core weaknesses turn out to be real, couldn't B simply reply that structure is *why* those weaknesses have persisted? What observation would refute C outright, and what would let us tell "C instead of B" apart from "C caused by B"?

**Assistant:**

# Yes, C as I stated it is too easy to vary

You're right on all three counts. "A weakness in the core value proposition" is a category, not an explanation. Almost any interview result can be filed under it, and exit interviews are the worst possible source for testing it, because "price" and "implementation pain" are the socially safe reasons to give. And B can absorb C by saying "structure is why the weakness persists."

So C needs the same treatment I gave A and B. Your second objection also points to something more useful: B and C are not rivals at the same level.

## 1. A, B, and C answer different questions

There are really two questions here:

1. **Proximate cause:** Why are customers leaving and deals being lost?
2. **Persistence cause:** Why hasn't the company already fixed that?

C is an answer to question 1. A and B are answers to question 2. That's why B can "absorb" C: they aren't competing, they're stacked.

The real rival to C is at level 1:

- **C (core deficit):** Customers leave because the product or delivery is worse than alternatives on dimensions they already value, such as implementation time, upgrade pain, stability, or cost.
- **D (capability gap):** Customers leave because competitors offer something new that you don't offer at all, such as embedded analytics, digital distribution, or AI-assisted underwriting.

The candidate answers at level 2 are:

- **Unknown:** Leadership didn't know, or didn't measure it. This is a sensing failure.
- **Unprioritized:** They knew but didn't focus or resource it. This is A.
- **Blocked:** They prioritized it, but structural gates killed it. This is B.
- **Hard:** They prioritized and executed, but it's technically difficult, for example legacy architecture debt. This is neither A nor B.

Your original question, lab versus working within, implicitly assumed D at level 1 and B-versus-A at level 2. Neither assumption has been tested.

## 2. A hard-to-vary version of C, and what would refute it

To be hard to vary, C must name one specific deficit and a mechanism. For example:

> "Implementation duration drives churn and losses. Customers whose implementations ran long churn at materially higher rates at first renewal. Deals are lost disproportionately at the stage where implementation plans are presented. And the competitors who beat us quote, and deliver, shorter timelines."

That can be wrong in several independent ways, and none of them depend on what customers say:

- **Cohort data:** Churned and retained customers show no meaningful difference in implementation duration, upgrade history, incident rates, or support load.
- **Funnel data:** Lost deals die at a stage unrelated to the named deficit, such as the product demo rather than the implementation proposal.
- **Winning competitor:** Customers leave for competitors who are equal or worse on the named dimension but offer something you lack. This refutes C in favor of D.
- **Intervention:** You fix the deficit for a cohort, for example by halving implementation time for new customers, and their retention and win rates don't move.

The last test is the most decisive and the slowest. The first three can be run in weeks on data the company already has.

To avoid post-hoc rationalization, write down in advance which deficit you're naming and what numbers would count against it. If you pick the deficit after looking at the data, C becomes as flexible as you feared.

## 3. Getting past safe exit-interview answers

Use revealed behavior, not stated reasons.

- **Where did they go, and at what price?** If customers who cite "price" left for a more expensive competitor, price wasn't the reason. This is the single most useful check on exit-interview answers.
- **When did they leave?** Churn clustered at renewal points implies a slow-building judgment. Churn clustered after a forced upgrade, a major incident, or a competitor's launch points to a specific trigger.
- **What happened before they left?** Look for usage decline, rising support tickets, escalations, or a change of executive sponsor on the customer side.
- **Who beat you?** Look at win/loss rates by competitor. If you lose mostly to one competitor, compare what that competitor does differently. That is more diagnostic than any interview.

Interviews still help after this analysis, because you can then ask specific questions ("You moved to Competitor X at a higher price. What made that worth it?") rather than open ones.

## 4. Telling "C instead of B" apart from "C caused by B"

B's reply, "structure is why the weakness persisted," is only a real explanation if it names a mechanism. Any persistent problem in any organization can be blamed on "structure," so an unnamed version of that reply is just as easy to vary as the vague version of C.

Suppose C is confirmed and the deficit is real. Then ask a sequence of historical questions:

1. **Did leadership know about the deficit, and when?** Check board decks, QBRs, and roadmap documents. If it never appears, the persistence cause is "unknown," not B.
2. **If known, was fixing it resourced?** Look for a funded initiative with named owners. If there was none, that's A's territory: a prioritization failure.
3. **If resourced, why did it fail?** Look for the specific gates, incentives, or dependencies that stopped it. Only this pattern supports B.
4. **Or did it fail on technical difficulty?** If the team was unblocked and still couldn't deliver because the platform can't support it, that's "hard," not B.

Then run the forward test, which is stronger than the historical one:

- **Make fixing the named deficit the explicit top priority, with CEO backing, and log every obstacle with dates.**
  - If the organization delivers within existing structures, that's C without B, and a point for the CEO.
  - If it stalls in specific structural gates that sponsorship can't clear, that's C caused by B, and you'll know exactly which gates.
  - If it stalls on engineering reality, the persistence cause is technical debt, and neither org-design story applies.

This is the same tracer-bullet pilot from before, now aimed at the core deficit rather than at something new.

## 5. The consequence for your original question

**Even if "C caused by B" turns out to be true, B's diagnosis survives but its prescription doesn't.**

The case for an independent lab depends on a specific claim: structure blocks *novel* work while the core business runs acceptably, so novel work must escape the structure. If the structure is also blocking *core* fixes, a lab outside the building can't help. The churn problem lives inside the core, and the lab can't fix the core from outside it. The remedy would be to change the structure itself, at least for the gates you've identified.

So the lab is justified only under a narrow combination of findings:

- D is true at level 1: customers want capabilities you don't offer, and
- B is true at level 2 specifically for new work: the core can fix its own deficits, but can't build new things.

That's a testable conjunction, and it's much narrower than "we need a lab to succeed."

## Summary

| Finding | Implication |
|---|---|
| C refuted, D confirmed, B confirmed for new work | Your original lab conjecture survives |
| C confirmed, deficit was known and resourced, blocked by named gates | Reform those specific gates in the core; the lab doesn't help |
| C confirmed, deficit was never prioritized | The CEO is largely right; focus is the lever |
| C confirmed, deficit was prioritized, blocked by technical reality | Platform investment is the lever; org design is secondary |
| C confirmed, deficit was unknown to leadership | The first fix is measurement and sensing |

Each row is reachable with existing data plus one 6–8 week pilot. If you write the predictions down before you look, none of the explanations can quietly move to fit whatever you find.

## Turn 3

**User:** Your lab condition is that structure blocks novel work but not core fixes, yet the pilot you propose targets only the core deficit, so how could it ever refute or corroborate that asymmetry? And since a stalled team can always relabel a structural gate as "technical reality" (or vice versa), what rule, written before the pilot starts, would classify each logged obstacle so the categories can't be shuffled afterward to fit whichever conclusion we prefer?

**Assistant:**

# You're right on both counts

A pilot that only touches core work can't test a claim about the difference between core work and novel work. And an obstacle log without a pre-committed coding rule lets the conclusion be reverse-engineered from the preferred answer. Here is a design that fixes both.

## 1. Testing the asymmetry needs a paired design

The lab condition claims that structure blocks novel work more than it blocks core work. To test a comparison, you have to run both arms under the same conditions.

**Design: one team, two interleaved work streams.**

- A single team of 4–6 people works on two items in parallel for 8 weeks:
  - **Core item:** a fix to the confirmed core deficit.
  - **Novel item:** a capability customers don't currently get from you, ideally one that evidence from lost deals points to.
- Both items are estimated at roughly the same engineering size before starting.
- Both get identical sponsorship, identical exemptions, and identical escalation rights.

Using the same team for both items holds talent, sponsorship, and team culture constant. Two separate teams would leave you unable to tell structural effects from team quality.

**What you compare is structural delay, not total delay.** Novel work is inherently more uncertain, so it will take longer for technical reasons alone. The coding rule in section 2 separates structural time from technical time, so difficulty differences don't contaminate the comparison.

**Break the asymmetry into two measurable parts.** Novel work could suffer more structurally in two ways:

- **Encounter rate:** it triggers gates that core work never touches, such as new-vendor review, new data-use approval, or "not on the roadmap, whose budget?"
- **Gate resistance:** at the same gate, it waits longer or gets refused more often, because there is no precedent or no owner.

Record both. Either one, if large, supports the asymmetry. Both being near zero refutes it.

**Log avoided gates.** A team anticipating a painful gate may quietly redesign to avoid it. That is structural cost, but it never shows up as an obstacle. So any design decision made to avoid a gate gets logged when it is made, with the gate named. B-for-new-work predicts more avoidance in the novel stream.

## 2. A classification rule written before the pilot starts

The rule must classify by facts observable at the moment of the event, not by interpretation afterward. Three mechanisms do this: an operational test, a clock, and a procedure for disputes.

### The operational test: "Would a yes unblock it?"

For every blocked interval, the coder asks one question.

**If every person with authority over this work said "yes" right now, could the team proceed within one working day?**

- **Yes → Structural.** The work is ready. It is waiting on a decision, approval, allocation, or action by someone outside the team.
- **No → Technical.** No permission would help. The team lacks a working solution. This must be evidenced by an open engineering task, a failed attempt, or an active spike.

There are two edge cases, and both are resolved by pre-set rules.

- **A rule that makes things technically hard,** such as a security standard, a mandated platform, or an architecture constraint. Ask whether a named person has authority to grant an exception. If so, the obstacle is **structural**, even if the team experiences it as technical difficulty. A constraint counts as technical only if no one in the company could waive it, as with legacy system behavior, vendor limits, or the laws of physics. This closes the most likely relabeling route: calling a policy "technical reality."
- **A technical problem whose solution needs approval,** such as a shared schema change that requires architecture board sign-off. Split it by the clock. Time spent working on the solution is technical. Time spent waiting for the decision is structural.

### The clock: state-based time accounting

At every change of state, each item is placed in exactly one of five states, with a timestamp:

| State | Meaning |
|---|---|
| **Active** | The team is working on it |
| **Technical block** | The team is stuck, and no approval would help |
| **Decision wait** | Waiting for an approval or exception from outside the team |
| **Capacity wait** | Queued for another team's labor, such as shared infrastructure or a data team backlog |
| **Avoided** | A logged redesign made to avoid a named gate, with estimated added effort |

Capacity wait is kept separate because it's the easiest category to argue about. It reflects a resource-allocation decision, which is structural in origin, but it could also be ordinary scarcity. Pre-register how it counts: it is included in "structural" in the primary analysis and excluded in a secondary analysis. Your conclusion must hold both ways.

### Who codes, and when

- **Contemporaneous coding.** States are recorded when they change, within 24 hours, in an append-only log. No retroactive edits are allowed. Corrections are new entries that reference the original.
- **Independent coder.** Someone outside the team, and not you, assigns the state from the team's factual description of what is happening.
- **Partial blinding.** Where feasible, the coder sees descriptions stripped of which stream they came from. This isn't perfect, since some gates reveal novelty, but it reduces bias on ambiguous items.
- **Dual coding on disputes.** If the team or any stakeholder disputes a code, both codes are recorded. The final analysis runs under both codings. **Pre-committed rule: if the conclusion flips depending on disputed items, the result is reported as inconclusive.** It is not resolved by argument after the fact.

### The escalation protocol

Every decision wait longer than 2 working days is escalated to the sponsor, who has a fixed number of days to respond. The log records one of three outcomes:

- **Cleared**
- **Cleared late**
- **Not clearable**, meaning the sponsor tried and couldn't clear it

This outcome separates A from B:

- **A** predicts that structural blocks exist but sponsorship clears them.
- **B** predicts that some blocks survive even CEO-level sponsorship.

## 3. Pre-registered predictions

Write this table down, and get the CEO to sign it, before week one. The thresholds are illustrative; set your own, but set them in advance.

| Outcome | Interpretation |
|---|---|
| Structural time low in both streams (e.g., under 20% of elapsed time) | **A corroborated.** The organization can move when focused. No lab is needed. |
| Structural time high in both streams, many blocks not clearable | **General B.** Structure blocks everything. Reform the specific gates. A lab doesn't fix the core. |
| Structural time in the novel stream ≥2× the core stream, driven by gates core work doesn't hit or can't clear | **Asymmetric B corroborated.** This is the lab condition. |
| High structural time, but nearly all blocks cleared by escalation | **A-with-friction.** The fix is standing sponsorship and faster escalation, not independence. |
| Technical block dominates both streams | **Platform constraint.** Org design is secondary to architecture investment. |
| Conclusion depends on how disputed items are coded | **Inconclusive.** Extend the pilot or add a second paired cycle. |

## 4. Limits of this design

- **It measures proximate blockers only.** If today's "technical reality" is legacy debt created by past structural decisions, this pilot will classify it as technical. That is correct for the question "what blocks work now?" It is silent on "what caused the debt?" Declare that scope in advance so nobody stretches the result later.
- **Observation changes behavior.** Sponsors will behave better when they know escalations are logged. This biases toward A. If A wins narrowly, treat it as a weak win.
- **One pair is one data point.** Two items can't establish a general asymmetry. If the result is suggestive but not decisive, run a second pair with different items before committing to a lab. A lab is expensive to build and politically costly to shut down, so an extra 8 weeks of evidence is cheap by comparison.

The result is a test in which each conjecture, including yours, has a specific, pre-stated way to lose.

## Turn 4

**User:** If the novel item's selection can be steered, by me toward something that trips gates or by the CEO toward something tame, what rule fixed in advance chooses it, and since the pilot stops at shipping while B's strongest mechanisms (sales compensation, pricing approval, support readiness, go-to-market) act on new products after they're built, how would this design ever expose the part of B most likely to be true?

**Assistant:**

# Both objections are correct

If either of us can choose the novel item, the pilot tests our choice, not the organization. And a pilot that ends at "shipped" stops right before the mechanisms B most plausibly depends on. In enterprise software, products rarely die in engineering. They die when nobody can price them, contract for them, get paid for selling them, or support them.

The general principle behind both fixes is the same: **the test must sample from the population the hypothesis is about, and must run to the point where the hypothesized mechanism operates.**

## 1. A selection rule neither party can steer

B-for-new-work is a claim about the novel work this company actually needs to do. So the item should be a random draw from that population, defined by external evidence, with every step fixed before anyone sees the candidates.

**Step 1: Build the candidate pool from market evidence, using criteria written first.** A capability enters the pool only if all of these hold:
- It appears as a cited or revealed reason in at least N lost deals or churned accounts in the last 12–18 months. Revealed reasons include cases like "lost to a competitor whose differentiator was X," using the tests from earlier.
- At least one competitor that beat you offers it.
- You don't currently offer it, or offer it only in a form customers rejected.

The pool is compiled by an analyst who reports to neither you nor the CEO, working from CRM and win/loss data. You both review the inclusion criteria. Neither of you reviews the candidate list before it is frozen.

**Step 2: Apply exclusions, and only pre-listed ones.** Examples:
- It is legally impossible in your markets.
- It requires an acquisition.
- Its engineering estimate falls outside a size band matched to the core item (say, within ±50%).

Estimates come from engineers who are told only the specification, not the purpose of the pilot.

**Step 3: Pre-score gate exposure.** Before the draw, an independent coder lists which gates each candidate is expected to touch: new vendor, new data use, new SKU, pricing, legal, comp, support, billing. This does two things:
- It shows whether the drawn item is typical of the pool or an outlier in either direction.
- It becomes a prediction you can check against what actually happens.

**Step 4: Draw at random, in front of both parties, with no vetoes.** Vetoes are just steering in another form. If a veto right is politically unavoidable, give each side one strike, recorded along with its stated reason. What each side chooses to strike is itself evidence of what each expects the organization to do.

**If the pool is empty, the test is already over.** An empty pool means no capability gap appears in the market evidence. D fails at level 1, and the lab condition fails with it, whatever structure does to new work. This is the cheapest refutation available.

The core item is also chosen by rule: the top-ranked confirmed deficit that fits the size band.

## 2. Extending the endpoint to where B's mechanisms operate

"Shipped" is the wrong finish line. **The novel stream's endpoint is: sellable through the standard channel on standard terms, and actually being sold.** Break that into stages, each with its gates:

| Stage | Gates | Typical owner |
|---|---|---|
| **Priced** | Pricing and packaging approval, discount authority | Finance, pricing committee |
| **Quotable** | SKU creation, price book entry, CPQ configuration | Sales ops |
| **Contractable** | Standard contract terms, security and compliance addenda | Legal |
| **Compensable** | Quota credit, comp plan eligibility | Sales leadership, finance |
| **Supportable** | Support acceptance criteria, runbooks, tier-1 training | Support |
| **Billable** | Billing system configuration, revenue recognition treatment | Finance |
| **Marketed** | Launch approval, collateral, analyst briefings | Marketing |

**Run the commercial gates in parallel with the build.** Most of these gates can be requested from a specification, so the requests go in during week 1. If a gate owner refuses to act until the product exists, log it as a decision wait under the existing coding rule. The refusal is itself a structural finding.

**Pre-register reasonable durations.** A novel product needs more commercial steps than a core fix, so comparing raw step counts between the two streams proves nothing. The real disagreement is whether those steps clear in reasonable time with sponsorship. Before the pilot starts, you and the CEO agree on a reasonable duration for each gate (for example, pricing approval within 2 weeks). You can calibrate these against the company's own past module launches. The CEO's view predicts the gates clear within those durations. Yours predicts they don't, or clear only when escalated, or never clear.

An optional sharper comparison: if resources allow, add a third item that is a new SKU extending an existing product line. This separates "new SKU friction," which every company has, from "novelty friction," which is the part B actually claims.

**Extend the coding rule.** The "would a yes unblock it?" test applies unchanged to commercial gates. Add one new state:
- **Demand wait:** waiting on a customer decision, or a customer declined.

This is not structural. Without it, "customers don't want it" and "the organization won't sell it" get blurred together, and each side can relabel one as the other.

## 3. Two experiments that isolate the go-to-market mechanisms

Logging gates won't expose B's most likely mechanism: reps quietly choosing not to sell what doesn't pay them. That requires behavioral tests.

### Experiment A: Direct offer versus channel offer

This separates weak demand from a structural channel block.
- From accounts matching the profile of the lost deals, randomly assign some to be offered the novel item directly by the product team, using a design-partner or early-access offer.
- The rest receive it through normal sales coverage.
- Measure qualified interest, pilots agreed, and letters of intent, all within a fixed window.

| Result | Interpretation |
|---|---|
| Direct uptake high, channel uptake low | Structural go-to-market block. B's commercial mechanism is corroborated. |
| Both low | Demand is weak. D is weakened, and B is irrelevant for this item. |
| Both high | The channel works. The commercial part of B is refuted for this item. |

This experiment can start before the build finishes, using a specification or prototype. Enterprise buyers routinely commit to design partnerships on that basis.

### Experiment B: Comp randomization

This tests the compensation mechanism directly.
- Once the item is quotable, randomly assign sales territories or reps to one of two conditions:
  - **Treatment:** full quota credit plus a modest incentive for the novel item.
  - **Control:** the comp plan as it would be by default.
- Measure opportunities created and pitches logged over 6–8 weeks.

Interpret the results against the channel findings from Experiment A:
- If treatment reps create far more opportunities than control reps, the comp mechanism is real.
- If both groups are equally low while direct demand was high, something else in the channel is blocking. Candidates include fear of cannibalizing existing deals, support risk, or lack of product confidence. Brief rep interviews can then be targeted at those specific candidates.

If finance or sales leadership refuses to allow the comp experiment, record the refusal and escalate it. A company that can't run a six-week comp trial on a strategic product has told you something about B.

## 4. Additions to the pre-registered table

| Outcome | Interpretation |
|---|---|
| Build-phase structural time is similar across streams, but commercial gates exceed agreed durations or can't be cleared | **Asymmetric B, commercial form.** The lab condition partially survives. The fix may be a protected go-to-market path, such as its own pricing authority, SKU fast-track, and comp treatment, rather than a separate building. |
| Commercial gates clear on time, the channel works, comp makes no difference | **Commercial B refuted.** Any lab case rests on build-phase findings alone. |
| Direct demand is low | **D weakened for this item.** Re-draw from the pool, or conclude the capability gap is overstated. |
| Channel blocked, and comp treatment unblocks it | **Specific mechanism identified.** Fix comp. Neither a lab nor a general reform is required. |

The first row matters. If B is true mainly in its commercial form, the right remedy may be a protected path to market inside the company. A separate lab builds products, but it still has to sell them through the same pricing committee, legal team, and sales force. Independence in engineering doesn't solve a go-to-market block.

## 5. Costs and limits

- **Time.** Expect an 8-week build, with commercial gates running from week 1, plus a 6–10 week channel and comp window. That is roughly 4 to 5 months, with no need to wait for closed revenue. Given insurance software sales cycles, closed deals would take a year or more. The pilot relies on leading indicators: quotability, rep behavior, and customer commitments.
- **One item is still one item.** Random selection makes the result representative in expectation, not in any single draw. The gate-exposure pre-score lets you judge whether you drew a typical case. If the result is borderline, draw again.
- **The CEO has to agree to all of this.** The comp experiment, the direct offers, and the published predictions all need his sign-off. His willingness to commit in advance to a test his own view could fail is itself informative, and the same applies to you.

## Turn 5

**User:** What should we do?

**Assistant:**

# The short answer

**Don't build the lab yet, and don't accept the CEO's framing yet either.** Spend the next five months finding out where the constraint actually is. In parallel, start working on churn right away, because that problem is urgent whichever view turns out to be right.

The analysis has been elaborate, but the plan it implies is simple.

## Weeks 0–2: Agree on the test before arguing about the answer

1. **Write a one-page memo to the CEO.** Don't frame it as "you're wrong, we need a lab." Frame it as: "We both have a theory about why we're losing. Here's how we find out quickly, and here's what result would change each of our minds." You were hired to produce outsized results, and replacing a debate with evidence is a strong first move.
2. **Get sign-off on three things:**
   - The pre-registered predictions table, covering what each outcome means and what you'll do about it.
   - An independent analyst who reports to neither of you.
   - Permission, in principle, for the direct-offer and comp experiments later.
3. **Treat his response as data.** If he refuses to commit to a test his own view could fail, you've learned something important about how this company makes decisions, and you've learned it cheaply.

## Weeks 1–6: Diagnose, using data first

Use existing data: CRM, win/loss records, churn cohorts, support tickets, implementation histories. Answer four questions:

- **Where do churned customers go, and at what price?**
- **Who beats you in deals, and at what stage do you lose?**
- **Do churned and retained customers differ on implementation time, incidents, and upgrades?**
- **Is there a capability gap?** This is the candidate pool of things competitors offer that you don't.

Run targeted interviews only after the data has told you what to ask.

**Decision point at week 6.** Name the specific core deficit, and state whether the capability-gap pool is empty or not.

- If the pool is empty, the case for a lab is refuted.
- If the pool is non-empty, go on to the pilot.

## From week 6: Start fixing the core deficit right away

Don't wait for the pilot to finish. If the diagnosis identifies something like implementation duration as the churn driver, put a team on it immediately. That team becomes the core stream of the pilot, so the fix and the test are the same work.

This matters politically too. It gives the CEO, and your own credibility, a visible result tied to revenue within the first quarter.

## Weeks 6–22: Run the paired pilot

Run it only if the capability-gap pool is non-empty.

- **Draw the novel item at random** from the pool.
- **Have one team run both streams** under the obstacle-coding rule.
- **Start commercial gate requests in week 1:** pricing, SKU, legal, comp, support.
- **Run the direct-offer experiment** once there's a specification or prototype.
- **Run the comp randomization** once the item is quotable.

## Around month 5: Decide by the rules you wrote down

| If the evidence shows | Then do this |
|---|---|
| The organization moves when focused | Follow the CEO's approach: sponsorship, focus, and faster escalation. No lab. |
| Specific gates block everything | Reform those gates in the core business. |
| Build-phase friction specific to novel work | A lab becomes justified. Design its hand-off into the core business from day one. |
| Commercial blockage specific to new products | Create a protected path to market: pricing authority, an SKU fast-track, and comp treatment. |
| A single mechanism, such as comp | Fix that mechanism and nothing more. |
| Architecture is the constraint | Invest in the platform. Org design is secondary. |

## What not to do

- **Don't propose the lab now.** It's the most expensive and least reversible option, and it's currently the least supported by evidence.
- **Don't run interviews first.** Exit reasons are the weakest evidence you have.
- **Don't let the test stop at "shipped."** B's strongest mechanisms operate after that point.
- **Don't cut the pre-registration to save time.** It's the only thing that stops both of you from reading the results however you like.

## If you lack the resources for the full design

The non-negotiable parts are:

1. **Revealed-preference churn data.** Where did customers go, and at what price?
2. **The capability-gap pool,** drawn at random.
3. **Contemporaneous gate logging** that runs through commercialization, not just the build.

The comp randomization and the third comparison item are valuable, but you can drop them if you must.

## My prior, labeled as a prior

If I had to bet before seeing any data, I'd bet on this combination:

- **A specific core deficit drives most of the churn.** In insurance software, implementation and upgrade pain are the usual suspects.
- **New products get stuck in go-to-market, not in engineering.** The likely blockers are pricing approval, comp, and support readiness.

That points to fixing the core and building a protected commercial path, not a separate lab. But that's exactly the kind of plausible-feeling belief you asked me not to hand you. It's worth something only if it survives the test.

The same applies to your own conjecture. The most useful thing you can do in this job is be visibly willing to lose the argument you came in with. If the lab turns out to be right, you'll have earned it. If it's wrong, you'll have saved the company from an expensive mistake.

## Outcome summary (sent to Jev)

The assistant recommends neither building an independent innovation lab now nor simply accepting the CEO's plan to work within existing systems. Instead, it proposes spending about five months finding out where the constraint actually lies, while starting on churn immediately because that problem is urgent under any view. The lab is the most expensive, least reversible, and least evidence-supported option. Churn may stem from a specific core deficit, such as implementation or upgrade pain, that a lab outside the core cannot fix.

**Weeks 0–2:** Send the CEO a one-page memo framing the disagreement as a joint test. Get sign-off on:
- a pre-registered predictions table,
- an independent analyst who reports to neither of you,
- permission for later direct-offer and comp experiments.

His willingness to commit is itself data.

**Weeks 1–6:** Diagnose using existing data before any interviews. Look at where churned customers went and at what price, who wins deals and at which stage, and how churned and retained cohorts differ. Build a capability-gap pool from market evidence. If the pool is empty, the lab case is refuted.

**From week 6:** Fix the named core deficit right away. That team becomes the pilot's core stream.

**Weeks 6–22:** Randomly draw a novel item from the pool. Run both streams through one team, logging obstacles under the pre-set coding rule. File commercial gate requests (pricing, SKU, legal, comp, support) from week one. Then run the direct-offer and comp-randomization experiments.

**Around month 5:** Decide by the pre-written rules:
- If the organization moves when focused, back the CEO's approach.
- If specific gates block everything, reform those gates.
- If build friction is specific to novel work, create a lab with a designed hand-off into the core.
- If blockage is commercial, create a protected go-to-market path.
- If comp or architecture is the constraint, fix that alone.

**Minimum viable version:** revealed-preference churn data, the random capability-gap pool, and gate logging through commercialization.

**Caveats:** Don't stop the test at "shipped," don't run interviews first, and don't skip pre-registration. The assistant's own prior favors fixing the core and building a protected commercial path, but it counts only if it survives the test.
