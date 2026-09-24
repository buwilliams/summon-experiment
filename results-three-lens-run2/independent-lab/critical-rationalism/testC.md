# independent-lab/critical-rationalism/testC

Model: claude-opus-5-5 · 2026-09-24T15:19:57.919832+00:00

## Turn 1

**User:** Use the method of conjectures and refutations (critical rationalism) to answer the following.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

# Lab vs. Existing System: A Conjectures-and-Refutations Analysis

## 1. Start with the problem, not the solutions

Popper insisted that inquiry begins with a problem. Both you and the CEO have jumped to solutions. The actual problem is:

> **Customers are leaving, and new customers aren't choosing us. Why, and what would change that?**

Both strategies are conjectures about how to solve a problem whose cause hasn't yet been established:

- **Conjecture A (CEO):** The company can recover through its existing systems, procedures, and people.
- **Conjecture B (you):** Meaningful innovation requires a lab independent of the parent organization.

Neither can be proven right. The method is to state each as boldly and testably as possible, attack it hard, and see what survives. Be hardest on your own conjecture. You were hired to "lead innovation," so you have an incentive to want a lab, and that is exactly when confirmation bias is most dangerous.

## 2. Attempting to refute Conjecture B (the independent lab)

**Refutation 1: The transfer problem.** History has many independent labs that invented well and delivered little to the parent company. Xerox PARC produced the GUI, Ethernet, and laser printing, and Xerox captured little of that value. Many corporate innovation labs of the 2010s were closed within a few years, often dismissed as "innovation theater." Independence protects ideas from the core's "antibodies," but it also cuts them off from the core's customers, sales channels, and integration paths. The more independent the lab, the harder the handoff.

**Refutation 2: Your domain makes independence costly.** Insurance software customers are regulated, risk-averse carriers with long sales cycles and deep dependence on core systems (policy administration, billing, claims). A new product that can't integrate with those systems, or pass a carrier's security and compliance review, is hard to sell. A lab isolated from the people who understand those constraints may build elegant things nobody can buy.

**Refutation 3: Timing.** Customers are leaving now. Labs typically need 18–36 months to produce commercially meaningful results. If churn comes from problems in the current product, a lab does nothing for the customers walking out the door this year. The company may not survive long enough for the lab to matter.

**Refutation 4: Sponsorship and politics.** A lab without strong CEO sponsorship tends to be cut at the first budget squeeze. Your CEO currently disagrees with you. A new executive whose first move signals "the existing organization can't do it" alienates the people whose cooperation you will eventually need.

**Status:** As a *universal* claim ("innovation requires an independent lab"), Conjecture B is refuted. Many successful transformations happened without one. It survives only in a narrower, conditional form.

## 3. Attempting to refute Conjecture A (work within existing systems)

**Refutation 1: The system produced the outcome.** The existing systems, procedures, and talent generated the current churn and weak win rate. This isn't decisive, since leadership, focus, or strategy could be the real failure. But if the cause is structural, the same structure will tend to reproduce the same results.

**Refutation 2: The resource-allocation trap.** Clayton Christensen's research on disruption offers a well-corroborated explanation: established organizations allocate resources toward their largest current customers and highest-margin products. Budget cycles, sales compensation, roadmap prioritization, and risk processes are all tuned for sustaining the existing business. New ideas that start small, with low margins or unproven customers, lose every internal prioritization contest. If what's killing you is a shift in the market, such as cloud-native or API-first platforms, embedded insurance, or AI-driven underwriting and claims, the core's processes will tend to starve the response.

**Refutation 3: Internal inconsistency.** The CEO wants "outsized results" but also wants them through the existing procedures. Normal processes tend to produce normal results. This doesn't make the conjecture false, but the CEO's position contains a tension he may not have examined.

**Counter-evidence (the conjecture partly survives):** Transformations have succeeded with largely the existing organization. Microsoft under Nadella changed course mostly with the same people by changing culture and priorities. Adobe moved to subscription cloud software within its core business. So "within" is not refuted in general either.

**Status:** As a universal claim, Conjecture A is also refuted. It survives in a conditional form.

## 4. The false dichotomy

Both universal versions fail, which suggests the question "Which strategy is right?" is badly posed. A better conjecture replaces both:

> **Conjecture C:** The right structure depends on *why* customers are leaving.
> - If churn comes from **execution failures** in the current product (bugs, slow implementations, poor service, pricing, missing features competitors have), the fix must happen **inside the core**. A lab is a distraction.
> - If churn comes from a **shift in what the market wants** (new architectures, business models, or capabilities your processes structurally can't produce), you need a **protected unit**. It should be protected from the core's resource allocation and processes, but **tethered** to its customers and distribution.
> - Most likely both are true to some degree. Then you need both: fix the core *and* protect the new. Organizational researchers O'Reilly and Tushman call this "ambidexterity."

Conjecture C is better in Popper's sense. It explains the successes and failures of both A and B, and it makes testable predictions about *your* company.

## 5. Critical tests

Popper's key discipline is to **write down in advance what result would refute your view**, then go look. Here are tests you can run in your first 60–90 days:

| Test | Result favoring "within" (A) | Result favoring a protected unit (B) |
|---|---|---|
| **Churn interviews** (talk to 10–20 lost customers) | They left over service, quality, and price, and went to similar competitors | They left for fundamentally different products or architectures |
| **Win/loss analysis** on recent deals | Lost on execution, references, or price | Lost because buyers wanted something you don't make and your roadmap can't reach |
| **The "small experiment" probe:** try to get one modest new idea to a customer pilot through normal channels | It moves in weeks with reasonable effort | It dies in prioritization, security review, or roadmap politics, or takes 9+ months |
| **History:** have past internal innovation efforts been tried? | Past failures were due to bad ideas or weak leadership | Good ideas were starved or killed by process |
| **Talent audit** | Few people inside have ideas | Many capable people have ideas and are blocked (the constraint is process, not talent) |
| **CEO sponsorship test** | — | Will he grant a protected budget, separate metrics, and decision rights? If not, a lab will likely fail regardless of merit |

The small-experiment probe is especially valuable. It is a real test of the CEO's conjecture, run on his terms. If the existing system handles it, you've learned something. If it fails, you have evidence rather than opinion, and the CEO has watched it happen.

## 6. Piecemeal rather than utopian change

Popper argued for *piecemeal* engineering, meaning small, reversible interventions with fast feedback, over wholesale redesigns whose errors surface too late to fix. That argues against both extremes: a big independent lab launched on faith, and an unexamined "keep doing what we do, harder." Choose the structure that **reveals your errors fastest and most cheaply**.

## 7. The recommendation that survives criticism

1. **Don't frame this as your view vs. the CEO's.** Frame it as a shared problem with competing hypotheses that you'll test together. This converts a political fight into an inquiry and protects your credibility as a newcomer.
2. **Spend the first 60–90 days on diagnosis:** churn interviews, win/loss analysis, the small-experiment probe. Write down your predictions beforehand.
3. **If you find a structural market shift, propose a small, protected team, not a large independent lab.** For example:
   - 5–8 people, time-boxed with explicit kill criteria.
   - Working on a problem taken directly from the churn data.
   - Protected from normal roadmap prioritization.
   - With a named core executive responsible for adopting what it produces.
4. **Scale autonomy in proportion to evidence.** If the team is strangled by the core, that is evidence for more independence. If it succeeds while tethered, that is evidence the CEO was partly right.

## Bottom line

Neither strategy, stated as a general rule, survives criticism. Your conjecture fails on transfer, timing, and sponsorship. The CEO's fails on resource allocation and on the tension between normal processes and outsized results. What survives is conditional: the right structure depends on the cause of churn, which you don't yet know.

Your first move isn't to build a lab or to work within the system. It is to find out why customers are leaving, and to design tests that could prove *you* wrong. Tests you run openly also give you the evidence, and the credibility, to win the argument with the CEO if you turn out to be right.

## Turn 2

**User:** If the CEO refuses to give a protected team its own budget or decision rights, what does that do to Conjecture C? Could you keep working through it the same way?

**Assistant:**

# What the CEO's Refusal Does to Conjecture C

**Short answer:** The refusal doesn't refute Conjecture C, but it does create a new problem. And yes, you can keep working through it the same way. The method doesn't depend on getting your way. It depends on treating each new obstacle as a problem to be explained and tested.

Popper described inquiry as a cycle: **P1 → TT → EE → P2**. You start with a problem (P1), propose a tentative theory (TT), eliminate errors through criticism and testing (EE), and arrive at a new, usually better-defined problem (P2). The CEO's refusal is a P2.

## 1. What the refusal refutes, and what it doesn't

Conjecture C makes a claim about the world: *if churn comes from a structural market shift, work done through the core's normal processes will fail to produce the needed response.*

The CEO's refusal is not evidence about the market or about why customers leave. It is a **decision**, and it constrains what you can do. Popper stressed the distinction between facts and decisions: a decision cannot refute a factual claim.

What the refusal does undermine is an **auxiliary assumption** you were relying on: *that a protected unit can be created here.* That assumption is now refuted, at least for the moment.

How much this matters depends on the diagnosis:

- **If the diagnosis points to execution problems**, the refusal barely matters. C already said to fix the core from within, and the CEO's approach and C agree.
- **If the diagnosis points to a structural shift**, the refusal matters a lot. C now predicts that the CEO's approach will fail at the capabilities you most need. That is a risky, testable prediction, and a valuable one.

The refusal is also weak evidence about the organization. If the resource-allocation trap operates even at the CEO level, that fits C's broader picture. But it is weak evidence, because he may have good reasons.

## 2. Treat the refusal as criticism, not just resistance

The CEO's "no" is itself a counter-argument against your proposal. In the spirit of the method, you should find out what it is and take it seriously. It may be correct. Different reasons point to different next moves:

| His likely reason | What it implies | Your response |
|---|---|---|
| **"We can't afford it."** Cash is tight during a turnaround. | The constraint is money, not philosophy | Look for protection that costs little: customer-funded pilots, reallocating your own budget, partnerships |
| **"We tried a lab before and it failed."** | He has evidence you lack, possibly about the transfer problem | Study that failure closely. It may refute part of your proposal. |
| **"It creates a two-tier culture."** | His concern is morale and cohesion | Design protection that doesn't look like an elite enclave, such as rotating core staff through the team |
| **"You're new; prove yourself first."** | The constraint is trust, not strategy | Earn credibility through a small win inside the system first |
| **"I believe the core can do it."** | A genuine disagreement about the facts | Agree together on a test (section 4) |

Only the last reason is a real clash of theories. The others are constraints you may be able to work around without changing his mind.

## 3. Refine the conjecture: which part of "protection" actually matters?

The refusal pushes you to sharpen C, which is exactly what criticism should do. "A protected team with its own budget and decision rights" bundles several things together. Take it apart:

- **Separate budget:** freedom from the annual allocation contest
- **Decision rights:** the ability to choose what to build without roadmap committee approval
- **Separate metrics:** not being judged by core-business KPIs such as revenue this quarter
- **Process exemptions:** a faster path through security review, procurement, and release processes
- **Dedicated people:** team members not pulled back to firefight in the core
- **Executive air cover:** the CEO visibly backing the work

Christensen's argument is mainly about the **resource-allocation and prioritization processes** that starve new ideas. A separate budget is one way to escape them, but not the only way. That suggests a sharper conjecture:

> **Conjecture C′:** What new-market work needs is protection from the *specific processes* that kill it (prioritization, metrics, certain reviews). A separate budget is one way to get that protection, but not necessarily the essential one.

C′ is more precise and more testable than C. It also opens options the CEO might accept, for example:

- A small team within your existing organization, with dedicated people and one or two process exemptions
- A design-partner customer who co-funds the pilot, so the money doesn't come out of the internal contest
- A partnership with an insurtech firm, where the new capability lives outside your processes by construction
- Personal CEO sponsorship of a single named initiative, without a formal lab

If some of these work and others don't, you learn which elements of protection are essential. That is knowledge nobody in the company has yet.

## 4. If you must work entirely within the system, turn it into a test

Suppose the CEO grants nothing. You can still use the method: make his approach the experiment.

**Write down in advance what would count as failure, and ideally agree on it with the CEO.** For example:

> "We'll pursue [the capability the churn data says customers want] through normal processes. If, within six months, it hasn't reached a customer pilot, or it has been deprioritized more than twice, or it has been blocked in review for more than 90 days, we'll both treat that as evidence the normal process can't deliver this kind of work, and revisit the structure."

This does three things:

1. **It gives the CEO's conjecture a fair test.** It might succeed, in which case C is refuted for your company and you've learned something important.
2. **It converts your disagreement into a shared experiment** rather than a power struggle you would lose.
3. **It prevents after-the-fact excuses on both sides.**

That third point matters most. Popper warned against **immunizing stratagems**: explaining away every failed prediction so a theory can never be refuted. Watch for both versions:

- **The CEO's version:** "It failed because the team executed poorly," or "We just needed more time." Neither is ruled out, which is exactly why you need criteria agreed in advance.
- **Your version:** "It only failed because it wasn't protected enough," or, if it succeeds, "That was an easy case; the real innovation would still need a lab." If you catch yourself reaching for these without having predicted them beforehand, you are rescuing your theory rather than testing it.

Also track *where* the effort gets stuck. C′ predicts specific failure points: prioritization meetings, KPI pressure, review queues, people being pulled away. If the effort stalls somewhere C′ didn't predict, that is informative too.

## 5. Where this could lead: the deeper problem

Follow the logic to its end. Suppose:

- The diagnosis shows a structural market shift,
- The CEO refuses all forms of protection,
- The within-system attempt fails in exactly the ways predicted in advance,
- And the CEO still won't update.

At that point the problem is no longer about labs. Popper's deepest concern was whether **institutions can correct their own errors.** He judged societies less by who rules than by whether bad policies can be recognized and changed without catastrophe. An organization whose leader won't let agreed-upon evidence change decisions has lost its main error-correction mechanism, and no innovation structure will fix that.

That becomes a new problem, P3, and it is about you: *Can I produce results here, and should I stay?* It deserves the same treatment. What would you need to see in the next six to twelve months to conclude the organization can learn? Write that down now, while you're still objective.

You are far from that point. The CEO hasn't refused anything yet, you don't yet know why customers are leaving, and his objections may improve your proposal.

## Bottom line

A refusal doesn't refute Conjecture C, because it tells you nothing about why customers leave. It does refute the assumption that a protected unit is available, and it forces a sharper question: *which element of protection actually matters?* That produces C′, which is more testable and more politically workable. If you get no protection at all, make the CEO's approach the experiment, with failure criteria agreed in advance and no excuses allowed on either side.

The method continues past every obstacle. Each "no" is a new problem, and working through it is how both you and the organization learn.

## Turn 3

**User:** Suppose the churn interviews come back mixed, with some customers leaving over service problems and others over missing capabilities. How would you keep working through that with the same method?

**Assistant:**

# Working Through Mixed Churn Results

Mixed results aren't inconclusive. They are a new problem, and a more interesting one. The question shifts from "Which cause is it?" to **"What explains the pattern of the mix, and which part of it matters most for the future?"**

## 1. First, criticize Conjecture C itself

Mixed results appear to confirm Conjecture C, which said "most likely both are true to some degree." That should make you suspicious, not pleased.

Popper warned that **confirmations are cheap when a theory would have been confirmed by almost any result.** Look at what C predicted:

- Service problems only: C says to work within.
- Missing capabilities only: C says to use a protected unit.
- A mix: C says to do both.

C was compatible with every outcome. As a guide to structure it was useful, but as a scientific claim it was nearly unfalsifiable. The mixed result therefore teaches you almost nothing *about C*. It only tells you that you need a **riskier theory**, one that explains *why* the mix looks the way it does and could be proven wrong by the details.

## 2. Rival conjectures that explain a mix

Several different worlds could produce the same mixed interviews, and they imply very different actions:

**H1: Two separate problems in two segments.** Different kinds of customers leave for different reasons, for example small carriers over service and large carriers over missing capabilities. The causes are independent.

**H2: Service problems are the root, and capability complaints are rationalizations.** Unhappy customers cite missing features because that is an easier, more defensible reason to give their boss or you. Fix service and the capability complaints fade.

**H3: The capability gap is the root, and it causes the service problems.** Customers needing capabilities you lack get custom workarounds, integrations, and configurations. Those make implementations slow, upgrades painful, and support expensive. The service failures are symptoms.

**H4: A common cause behind both.** Aging architecture or accumulated technical debt makes the product slow to support *and* slow to extend. Service and capability complaints are two faces of the same underlying problem.

**H5: A shift over time.** Service was the dominant reason for customers lost a few years ago, and capabilities are becoming the dominant reason for recent ones (or the reverse). The mix is a snapshot of a transition.

**H6: The interviews are misleading.** Stated reasons don't reflect real reasons. Exit interviews are notoriously polite, the real driver might be price or a relationship, and the people you interviewed may not be the people who made the decision.

These are not mutually exclusive, but they compete. Each forbids certain patterns in the data, which makes them testable.

## 3. Critical tests

Write down what each hypothesis predicts **before** you dig into the data, so you can't fit the story afterward.

| Test | What would support or refute which hypothesis |
|---|---|
| **Segment the churn by customer size, line of business, region, product module, and platform version** | Clean separation by segment supports H1. No pattern weakens it. |
| **Weight by revenue, not headcount** | Ten small customers leaving over service may matter less than two large ones leaving over capabilities. This doesn't test a hypothesis, but it changes what matters. |
| **Compare service problems against customization levels** | If service complaints concentrate in heavily customized accounts, that supports H3. If they are spread evenly, that weakens it. |
| **Map both complaint types to the same system components** | If both cluster on the same legacy modules, that supports H4. |
| **Sort churn by when customers left** | A rising share of capability-driven exits in recent cohorts supports H5. |
| **Check where they went** | Customers leaving for similar incumbents with better service suggests service is real. Customers leaving for modern platforms or insurtechs suggests capability is real. Destinations are behavior, and harder to fake than stated reasons (tests H6). |
| **Check support tickets and usage data before exit** | Did "service" churners actually file escalations? Did "capability" churners ever request those features? A mismatch with stated reasons supports H6. |
| **Test for H2 directly** | If capability complaints are rationalizations, customers citing missing features should *also* show poor service histories. If they had good service and still left, H2 is refuted for them. |

**The most powerful test is new-business losses.** Prospects who chose a competitor never experienced your service. If you are losing new deals mainly over capabilities, the capability gap is real and not a rationalization of service anger. That largely refutes H2 and confirms that the market wants something you don't make. If you are losing new deals over price, references, or reputation, service may be the bigger story, because reputation travels. Win/loss data acts as a control group your churn data lacks.

## 4. From diagnosis to action

Different surviving hypotheses imply different strategies, and in no case does "mixed" mean "split effort evenly."

- **If H1 survives (separate problems):** Run two distinct efforts. Fix service within the core, and pursue capabilities through protected work. Allocate effort by revenue at risk, not by the count of complaints.
- **If H2 survives (service is the root):** The CEO is largely right. Put your energy into service within existing systems. A protected unit would be a costly distraction, and you should say so openly.
- **If H3 survives (capabilities cause service pain):** Fixing service directly treats symptoms and will disappoint. The capability work is the real service fix, which strengthens the case for protected new work considerably.
- **If H4 survives (common cause):** Neither a service program nor a lab addresses the root. The real question becomes platform modernization, which is a core-business decision the CEO has to own. It may also be the most important finding you could bring him.
- **If H5 survives (a shift over time):** Weight the future, not the average. Service fixes protect current revenue, but the recent trend shows where the business is heading.
- **If H6 survives (misleading interviews):** Your diagnosis isn't done. Improve the evidence before committing resources.

## 5. Sequencing: a conjecture of its own

Even with two real problems, order matters. A reasonable conjecture is: **fix service first, because it is faster, retains revenue now, buys time for slower capability work, and earns you credibility with the CEO.**

Criticize that too. It fails if H3 or H4 is true, because then service fixes won't hold without the deeper work. It also fails if capability-driven churn is accelerating fast enough that delay is fatal. So the sequencing decision depends on the tests above. It is not a default.

## 6. The political dimension

Mixed results give you and the CEO a natural compromise: "you're right about service, I'm right about capabilities." That is useful, and you should openly concede whatever the data gives him, because it builds the trust you'll need.

But **a politically convenient conclusion is not a tested one.** Splitting the difference feels balanced, which is exactly why it attracts people who want to avoid conflict. If the evidence says H2 (you were mostly wrong) or H4 (you were both missing the point), the compromise would be an evasion. Let the tests decide the balance, not the need for peace.

## 7. The cycle continues

- **P1:** Why are customers leaving?
- **TT:** Conjecture C, which proved too accommodating.
- **EE:** Mixed interviews, which exposed C's weakness.
- **P2:** What structure explains the mix, and which part drives the future?
- **TT₂:** H1 through H6, each riskier and more specific.
- **EE₂:** Segmentation, destinations, behavioral data, win/loss.
- **P3:** Whatever survives, likely a sharper question you can't yet see, such as "Is this really a platform problem?"

## Bottom line

Mixed results mean your earlier theory was too easy to confirm, so replace it with rivals that make risky, specific predictions. Test them against segments, timing, customer destinations, behavioral data, and above all new-business losses, which isolate capability from service. Then let the surviving explanation set the balance between fixing the core and building the new, rather than defaulting to a compromise because it's comfortable.

## Turn 4

**User:** Suppose the data points to H4, aging architecture behind both complaint types, and the CEO says a platform modernization is too risky to take on mid-turnaround. How would you keep working through that the same way?

**Assistant:**

# When the Root Cause Is the Architecture and the CEO Says "Too Risky"

This is the hardest version of the problem so far, because the CEO's objection is probably partly right. The method helps precisely here: it separates the part of his objection that is well-founded from the part that isn't.

## 1. Take the CEO's objection seriously: it's a strong conjecture

"Platform modernization is too risky mid-turnaround" is not mere resistance. It is a conjecture backed by substantial evidence:

- **Large rewrites fail often.** Big-bang replacements of core software run late, over budget, or get abandoned at high rates. The standard cautionary tale is Netscape's decision to rewrite its browser from scratch, which is widely blamed for its collapse.
- **Your own customers prove it.** Insurers' core-system replacements are notorious for multi-year overruns. Your company probably earns money from that pain. The CEO has watched it happen.
- **Turnarounds are fragile.** A modernization consumes your best engineers, slows feature delivery, and adds risk to the existing product just when customers are already unhappy. If it fails mid-turnaround, the company may not survive.

In Popper's terms, this objection has survived many real tests. Dismissing it would be dogmatic.

## 2. Then find the hidden comparison

"Too risky" is a comparative claim, and the comparison is usually left unstated. **Too risky compared to what?**

If H4 is true, not modernizing is not a safe baseline. H4 predicts that as long as the architecture stays the same, both service problems and capability gaps will persist, and churn will continue. So the CEO's real conjecture is:

> **Risk of modernizing > Risk of continuing on the current architecture**

That comparison can be estimated:

| Question | Why it matters |
|---|---|
| **What is the churn trajectory if nothing structural changes?** | Project revenue retention over two to three years under H4 |
| **How much cash runway does the company have?** | If runway is shorter than any plausible modernization, the CEO is right: you can't finish, and a half-done modernization is worse than none |
| **How fast is the market moving?** | If competitors with modern platforms are winning an increasing share of deals, waiting makes the eventual modernization harder and the customer base smaller |
| **What is the cost of service firefighting?** | If the legacy system consumes a large share of engineering capacity just to stay upright, "stability" is already expensive |

Doing this analysis with the CEO, not against him, turns an argument about attitudes to risk into an argument about numbers. Either result is useful. If runway is too short, he is right, and you've learned it rigorously.

## 3. The key refinement: which kind of modernization?

"Platform modernization" is ambiguous in the same way "protected team" was. It bundles very different approaches, and Popper himself drew the relevant distinction.

**Utopian engineering** is the big-bang rewrite: design the ideal new platform, build it in parallel for years, then migrate everyone. Popper argued against wholesale redesigns because they are hard to evaluate until it's too late, errors compound invisibly, and failure is catastrophic.

**Piecemeal engineering** is incremental modernization. Software engineers call a version of it the **"strangler fig" pattern**: replace the legacy system one component at a time, routing traffic to new components as they prove themselves, until the old system has been gradually replaced. Each step is small, testable, and reversible.

This suggests a sharper conjecture:

> **Conjecture M:** The CEO is right about big-bang modernization and wrong about piecemeal modernization. Replacing the specific components most responsible for churn, one at a time, is less risky than both the big rewrite and the status quo.

Conjecture M is falsifiable. It predicts that:

- The worst problems are **concentrated** in a limited number of components, not spread evenly through the system
- Individual components can be **separated** from the rest with reasonable effort
- Each step can deliver **customer-visible improvement** within a quarter or two, rather than years of invisible work
- Each step can be **rolled back** if it goes wrong

If the problems turn out to be spread evenly, or the system is so entangled that no component can be separated, M is refuted. Then the choice really is between a big rewrite and living with the architecture, and the CEO's caution looks much stronger.

## 4. Before betting on H4, test it once more

H4 is now carrying a lot of weight, so criticize it again. "The architecture is the root of everything" is an attractive story for engineers and new innovation leaders. It is a convenient explanation that points toward a big, interesting project. That is exactly when to be suspicious.

Tests that could still refute or narrow H4:

- **Do problems concentrate in legacy components?** If service failures are just as common in newer parts of the system, the cause may be process, staffing, or management, not architecture.
- **Do competitors on modern platforms actually deliver better service?** If they have similar complaints, architecture may not be the differentiator.
- **What do your engineers say, and what do the data say?** Compare their assessments of which components are hardest to change against records of change failures, incident rates, and delivery times.

These tests have a second benefit. The same data that tests H4 also shows **where a piecemeal modernization should start**: the components with the most incidents, slowest delivery, and highest revenue at risk.

## 5. Other options that avoid touching the core

Don't let the choice collapse to "modernize or don't." Other conjectures deserve testing:

- **Wrap the legacy system.** Build a modern API layer around the core so new capabilities can be delivered outside it. This addresses capability complaints quickly but may not fix service problems.
- **Partner.** Integrate modern third-party components for specific capabilities rather than building them.
- **Acquire.** Buy a small company with a modern platform in a key area and migrate customers gradually. This trades technical risk for integration risk.
- **Stabilize and prepare for sale or merger.** If runway is short and the architecture is fatal, the most responsible turnaround strategy may be making the company attractive to a buyer. This is an uncomfortable conjecture, but a serious one.

Each has different risks and different refutation conditions. Some may fit the CEO's risk tolerance better than any modernization.

## 6. How this reconnects the earlier threads

Conjecture M may resolve the earlier disagreement about a protected team. A small team modernizing one high-impact component is:

- **Protected** in the ways that matter (C′): a dedicated team, clear goals, freedom from normal feature prioritization
- **Tethered to the core by construction**, since it is replacing part of the core, which solves the transfer problem that sinks many labs
- **The foundation for new capabilities**, because new features can be built on the modernized component

So the innovation work and the modernization work may be the same work. That is a more coherent proposal than either "build a lab" or "modernize the platform," and one the CEO may find easier to accept.

## 7. Turn the disagreement into a test

As before, ask the CEO: **"What would you need to see to consider this acceptably risky?"** Also ask yourself: **"What would convince me he's right?"**

Then propose a limited first step with criteria agreed in advance:

> "We'll modernize one component, the one behind the largest share of revenue at risk. We'll limit it to a small team and one to two quarters. It succeeds if incidents in that area fall by a defined amount, delivery speed improves measurably, and no major customer disruption occurs. If it fails those tests, we stop, roll back, and treat that as strong evidence that modernization is too risky for us right now."

This gives the CEO's conjecture a fair chance to be confirmed. If even a small, reversible step fails, he was right, and you have both learned it cheaply.

## 8. Watch for immunizing on both sides

- **The CEO's risk:** "Too risky mid-turnaround" can become permanent. There is always another quarter of pressure and never a calm moment. Ask what conditions would make it not too risky. If no answer is possible, the objection has become unfalsifiable.
- **Your risk:** "Architecture" can become an explanation for every failure. If a modernized component doesn't improve service, you'll be tempted to say "the rest of the system is holding it back." Unless you predicted that in advance, it is an excuse, not an explanation.

## 9. The cycle continues

- **P1:** Why are customers leaving?
- **TT:** H1 through H6.
- **EE:** Segmentation and behavioral data point to H4.
- **P2:** The root cause is architectural, but modernization is judged too risky.
- **TT₂:** The CEO's risk conjecture, Conjecture M (piecemeal modernization), and the non-core options.
- **EE₂:** Runway and churn projections, concentration analysis, one limited modernization step with agreed criteria.
- **P3:** Perhaps "How fast can we safely replace components?" or, if M fails, "Is this company viable on its current architecture?"

## Bottom line

The CEO is probably right that a big-bang modernization mid-turnaround is dangerous, and that part of his conjecture has strong evidence behind it. But "too risky" hides a comparison with a status quo that H4 says is also risky, and it treats modernization as a single all-or-nothing choice. Popper's distinction between utopian and piecemeal change suggests the better conjecture: replace the worst components one at a time, with small, reversible steps and success criteria agreed in advance. That approach tests the CEO's view fairly, costs little if you're wrong, and may turn your innovation mandate and the architectural fix into the same project.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

Critical rationalism never proves a plan right. But Popper was clear that we still have to act, and that we should act on the **best-tested theory available** while staying ready to change course. Here is the plan that has survived the criticism so far.

One caveat first: the scenarios we worked through were hypothetical. If you haven't yet run the diagnosis, that comes first. Everything after it depends on what you find.

## Step 1 (first two weeks): Align with the CEO on the question, not the answer

- **Don't propose a lab.** That would start a fight over a solution before either of you knows the cause.
- **Frame a shared problem:** "Customers are leaving and we're losing deals. Let's find out exactly why before we commit resources."
- **Agree in advance how you'll decide.** For example: "If the evidence points to service, we fix the core. If it points to capability or architecture, we consider protected work or piecemeal modernization. Either way, we'll let the data settle it." This commitment matters more than anything else you do early.

## Step 2 (days 1–60): Diagnose, and write down predictions first

Before looking at the data, write a one-page memo stating what you expect and what would prove you wrong. Then run:

- **Churn interviews** with 10–20 lost customers, reaching the actual decision-makers
- **Win/loss analysis** on recent new-business deals, your cleanest test of capability vs. service
- **Segmentation** by customer size, product module, platform version, and exit date
- **Where churned customers went**, and what their support and usage data showed before they left
- **Component-level data:** incidents, delivery times, and change failures by part of the system
- **A runway and churn projection:** how long you have if nothing structural changes

In parallel, run the **small-experiment probe**. Push one modest idea through normal channels and record where it stalls.

## Step 3 (now, not later): Protect the revenue you still have

Everything above takes weeks, and some customers are leaving right now. Start an **at-risk account program** immediately:

- Identify the top accounts showing signs of churn
- Put senior attention on them
- Fix their specific service problems

This is the CEO's approach, and it's correct for this purpose. Owning it visibly also earns you credibility.

## Step 4 (around day 60–90): Decide together, based on what survived

- **Mostly service problems:** Lead a core service improvement program. Drop the lab idea and say openly that the data changed your mind.
- **Mostly capability gaps:** Propose a small protected team, 5–8 people, tethered to the core, with a named executive responsible for adopting its work.
- **Architecture behind both (H4):** Propose **one** piecemeal modernization step. Choose the component tied to the most revenue at risk. Limit it to a small team and one to two quarters, and agree success and kill criteria in advance.
- **Runway too short for any of this:** The CEO's caution is right. Focus on stabilizing, and consider partnerships, acquisition, or preparing the company for sale.

## Step 5 (quarters 2–3): Run the test honestly

- Report results against the criteria agreed in advance, including failures.
- Don't explain away a miss unless you predicted that explanation beforehand. Hold the CEO to the same standard.
- If the first step succeeds, expand to the next component or capability. If it fails, stop and consider the alternatives: wrapping the legacy system with APIs, partnering, or acquiring.

## Step 6 (around month 12): A private checkpoint for yourself

Write down now what you'd need to see by then to conclude the organization can learn from evidence. For example: did agreed criteria actually change decisions? If they did, you have a company that can correct its errors, which is the precondition for any turnaround. If they didn't, that tells you something important about your own next move.

## Why this plan

It survived the criticisms of every earlier conjecture:

- **It avoids your original error:** a lab launched before knowing the cause.
- **It avoids the CEO's possible error:** assuming the current system can deliver whatever is needed.
- **It keeps each commitment small and reversible**, so mistakes cost little and surface quickly.
- **It works with the CEO rather than against him**, and his support is what any structure needs to survive.

So the short answer is: diagnose first, protect current revenue now, and then take the smallest reversible step the evidence supports, with success criteria you and the CEO agreed on in advance.

## Outcome summary (sent to Jev)

Neither strategy, stated as a general rule, is right. Launching an independent lab risks the transfer, timing, and sponsorship failures that sink many labs. Working purely within existing processes risks the resource-allocation trap, in which the core starves new work, and normal processes rarely yield outsized results. The right structure depends on why customers are leaving, and that is not yet known.

The plan is to act on the best-tested theory while staying ready to change course:

- **First two weeks:** Frame the problem jointly with the CEO rather than proposing a lab. Agree in advance how evidence will decide the path.
- **Days 1–60:** Write down predictions and refutation conditions before looking at data. Then run:
  - churn interviews with actual decision-makers
  - win/loss analysis, the cleanest test of capability versus service
  - segmentation by size, module, platform version, and exit date
  - where churned customers went, plus their prior support and usage data
  - component-level incident and delivery data
  - a runway projection
  - a small-experiment probe through normal channels
- **Immediately:** Start an at-risk account program to protect current revenue.
- **Around days 60–90:** Choose based on what survived:
  - **Service problems:** Fix the core and openly drop the lab idea.
  - **Capability gaps:** Form a small protected team of 5–8 people, tethered to the core, with a named executive responsible for adopting its work.
  - **Aging architecture behind both:** Modernize one high-impact component piecemeal, with agreed success and kill criteria.
  - **Runway too short:** Stabilize and consider partnerships, acquisition, or sale.

**Caveats:**

- The earlier scenarios were hypothetical, so diagnosis must come first.
- Big-bang rewrites are genuinely dangerous mid-turnaround.
- Neither side should explain away failures it didn't predict.
- By month 12, privately judge whether agreed evidence actually changes decisions, since an organization that can't correct its errors can't turn around.
