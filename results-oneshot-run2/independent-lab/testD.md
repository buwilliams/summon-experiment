# independent-lab/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T12:57:09.624947+00:00

## Prompt

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

## Response

# Neither conjecture survives as stated

Both are claims about **organizational structure**, but neither is a claim about **why customers are leaving**. That gap is where both are weakest, and where a better explanation likely sits.

---

## 1. What each conjecture actually claims

**Conjecture A (CEO): "Work within existing systems, procedures, and talent."**
- **Claimed mechanism:** The organization has the capability to win. What's missing is direction, priority, and leadership. The machine is sound but pointed the wrong way.
- **Implied causal story:** Churn and lost deals result from bad choices about what to build and sell, not from the organization's inability to build or sell differently.

**Conjecture B (you): "An independent innovation lab."**
- **Claimed mechanism:** The organization actively rejects novel work. Approval layers, risk aversion, incentives, legacy architecture, and resource contention kill new ideas before they reach customers. The machine is optimized for its current output and treats deviation as a threat.
- **Implied causal story:** Good ideas either exist or could exist, but the core's processes prevent them from shipping. Remove those processes and output changes.

---

## 2. What each predicts that the other doesn't

This is where the conjectures can actually be told apart.

| Observation | If A is true | If B is true |
|---|---|---|
| **History of past initiatives** | They failed from lack of focus, poor ideas, or weak sponsorship | They died in approval queues, resource fights, architecture reviews, or at integration |
| **Cycle time for a small, customer-requested change** | Reasonably fast once prioritized; mostly working time | Slow regardless of priority; mostly *waiting* time (reviews, release trains, handoffs) |
| **What happens when you give an internal team air cover** | They ship something meaningfully different, with manageable friction | They hit specific, repeatable, structural blockers that air cover can't remove |
| **High performers** | Frustrated by unclear direction; energized by clarity | Frustrated by process; have tried and been blocked; some have left |
| **Why customers churn and deals are lost** | Fixable gaps within the current product and architecture | Competitors offer capabilities that the current system structurally can't produce at a competitive speed |
| **Skunkworks history** | Rare or unremarkable | Informal workarounds have succeeded where formal programs failed |

---

## 3. Where each is easy to vary

A good explanation is hard to vary: change the details and it stops working. Both of these have escape hatches.

**Conjecture A's escape hatches:**
- "It didn't work because we didn't execute hard enough." This absorbs any failure.
- "Existing talent" can be quietly redefined. Replace people and it still counts as "working within."
- It never specifies which systems and procedures are adequate, so any failure can be blamed on the wrong ones.
- **Its deepest problem:** The current system is producing the current results, which are churn and lost deals. A must explain why the same system will produce different outputs. The only coherent answer is "the inputs were wrong (priorities, leadership), not the machinery." That is a specific, testable claim, and A rarely states it.

**Conjecture B's escape hatches:**
- If the lab fails, "it wasn't independent enough."
- If the core rejects the lab's output, "that proves the immune system."
- If the lab succeeds at building prototypes that never reach customers, "the core wouldn't adopt it," which again gets counted as confirmation.
- **Its deepest problem:** B explains why ideas die inside the core but says nothing about how the lab's output reaches customers. In insurance software, value lives in the core platform: policy, billing, and claims systems, integrations, compliance, data migration, implementation services, and support. A lab product must usually pass through all of these. Independence doesn't remove the bottleneck. It moves the bottleneck to the handoff. The base rate matters too: many insurers and financial firms opened innovation labs in the 2010s and quietly closed them, often because of this transfer problem.

**Summary:** A can't explain why the same machine will produce different results. B can't explain how independent output gets through the machine to customers.

---

## 4. A third explanation that may fit the facts better

Start from the actual facts: **customers are leaving, and new customers aren't choosing you.** In enterprise insurance software, switching costs are enormous. Carriers endure years of pain before migrating. Churn despite those costs signals severe dissatisfaction with something specific.

**Conjecture C: There is a small number of binding constraints causing churn and lost deals. The right structure follows from what they are.**

Plausible candidates, each implying a different strategy:
- **Implementation and time-to-value.** Deployments take too long and cost too much. The fix is delivery methods, configurability, and migration tooling. This is core work, and a lab can't fix it.
- **Architecture.** Competitors (cloud-native platforms) iterate faster and integrate more easily. The fix is a platform modernization strategy. This is neither "work within" nor "lab."
- **Reliability and service.** The product breaks and support is slow. The fix is operational, not innovation at all.
- **Genuine capability gaps.** Competitors offer things you don't have, such as embedded analytics, AI underwriting or claims, or digital distribution. This is the only case where something like a protected new team clearly helps.
- **Go-to-market.** Pricing, packaging, or sales motion. This isn't an engineering problem.

C is harder to vary than A or B because each candidate predicts specific things churned customers will say and specific places where cycle time goes. It also explains why you and the CEO disagree: you're each assuming a different answer to a question nobody has investigated.

A refinement of C that is also testable: if the diagnosis points to new capabilities, the need may be **independence of process, not independence of product.** That means a small team with named exemptions from specific procedures, such as a release train, an architecture board, or a procurement cycle, while staying embedded in the core product and customer base. This is not a mushy "hybrid." It makes a precise claim: a few identifiable procedures are the blockers, and everything else in the core is necessary.

---

## 5. The cheapest tests that could refute each, soon

These can run in parallel over about 30–60 days.

**Test 1: Churn and lost-deal autopsy (2–3 weeks, nearly free)**
Interview 10–15 churned customers and lost prospects, not your sales team's summary of them. Ask what made them leave and what the winner had.
- *Refutes B as the primary strategy* if reasons cluster around implementation, reliability, service, or cost. A lab can't fix those.
- *Refutes A* if reasons are "competitor ships monthly, you ship yearly" or "they have X and you can't build it."
- *Tests C directly* by showing whether the reasons cluster.

**Test 2: Innovation graveyard trace (1–2 weeks)**
Find the last 3–5 attempts at something new. For each, determine exactly where and why it died.
- Died in approvals, resourcing, or integration: supports B.
- Died because nobody wanted it: refutes both, and suggests the real gap is customer discovery, not structure.
- Died because leadership changed priorities: supports A.

**Test 3: Value-stream trace of one small change (1–2 weeks)**
Take one small, customer-requested change and map idea to production, separating working time from waiting time.
- If a trivial change takes months and most of it is waiting, A's claim that "existing procedures" are adequate is refuted for fast innovation. You'll also know which procedures are responsible.

**Test 4: Protected internal team, 6–8 weeks (the decisive test)**
Form a small team inside the organization. Give them one real customer problem from Test 1 and explicit CEO air cover. Log every blocker: what it was, who owned it, and how long it cost.
- *A survives* if they ship something meaningful and the friction is manageable.
- *B gains support* if they hit structural blockers that air cover couldn't remove. You also get the exact list of what "independence" would need to mean.
- This test is fair to both views. It gives the CEO's approach a real chance while generating evidence rather than argument.

**Test 5: The CEO's commitment (one conversation)**
Ask for one or two specific exceptions, such as bypassing a review cycle or pulling two named engineers off their current work for eight weeks.
- If refused, "work within the existing systems" means "change nothing," and you learn that cheaply.
- If granted, the CEO's position is more flexible than its framing, and some version of C becomes politically viable.

**Test 6: Absorption test for B (one week)**
Before proposing a lab, ask: if the lab built something customers loved, who in the core would own, integrate, support, and sell it? Get names.
- If nobody can commit, the lab will likely fail at transfer, whatever it builds.

---

## 6. Where this leaves you

- **Conjecture A** is unlikely as stated. It has to explain why an organization producing churn will produce growth without structural change. It survives only if the constraint turns out to be leadership and prioritization, which Tests 2–4 will reveal.
- **Conjecture B** is vulnerable in your specific industry. Value is delivered through the core, so a lab likely relocates the bottleneck to the handoff. It survives only if Test 1 shows the gap is new capabilities and Test 6 shows a credible path back into the product.
- **Conjecture C** currently explains the facts best, mostly because it takes the churn seriously as the thing to explain. It is also the most refutable: if the autopsy shows no clustering, C is in trouble.

**A practical note:** You're new, and the CEO holds the opposite view. Opening with "we need an independent lab" asks him to accept your conjecture on your authority. Opening with Tests 1 and 4 lets the evidence settle the question. If you're right about the immune system, the protected-team experiment will show it in eight weeks, with a documented list of the specific blockers, and that list becomes your case for exactly as much independence as the evidence supports.

## Summary (sent to Jev)

The response argues that neither the CEO's view nor the user's is right as stated. Both are claims about organizational structure, and neither explains why customers are leaving.

The CEO's position, working within existing systems, cannot explain why the same machine now producing churn will produce different results. It survives only if the real constraint is leadership and prioritization. The independent lab is especially vulnerable in insurance software. Value is delivered through core policy, billing, and claims systems, integrations, compliance, and implementation, so a lab mostly moves the bottleneck to the handoff. The response notes that many insurers' labs from the 2010s closed because of this transfer problem.

It proposes a third explanation: a few binding constraints are driving churn and lost deals, and the right structure depends on what they are. Candidates include slow implementation, outdated architecture, reliability and service, genuine capability gaps, and go-to-market. Only capability gaps clearly favor a protected new team. Even then, the need may be independence of process rather than of product: a small embedded team with named exemptions from specific procedures.

To test these views over 30–60 days, the response recommends six steps:
- Interview 10–15 churned customers and lost prospects.
- Trace where past initiatives died.
- Map one small change from idea to production, separating working time from waiting time.
- Run a protected internal team on a real customer problem for 6–8 weeks, logging every blocker.
- Ask the CEO for one or two specific exceptions.
- Identify by name who would own, integrate, support, and sell anything a lab built.

As a new hire facing a CEO with the opposite view, the user should lead with evidence rather than a demand for a lab. A documented blocker list would justify exactly as much independence as the evidence supports.
