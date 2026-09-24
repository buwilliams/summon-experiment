# independent-lab/critical-rationalism/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:27:14.444439+00:00

## Prompt

You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

## Response

## The short answer

Neither strategy is right as stated, and framing it as "lab vs. no lab" will likely cost you the argument and possibly the job. The right answer depends on **what kind of problem you're actually solving**, and I'd bet that most of what's driving churn and lost deals isn't something an innovation lab can fix.

## Why each pure strategy tends to fail

**The CEO's approach (innovate within existing systems):** Established organizations are optimized to execute a known business model efficiently. Their budgeting, planning cycles, risk controls, incentives, and release processes will reliably smother anything uncertain, unproven, or threatening to current revenue. Christensen's work and decades of case evidence support this. If the company needs something genuinely new, like a new architecture, pricing model, or customer segment, the core will kill it slowly and politely.

**Your approach (an independent lab):** Separated labs have a poor track record in enterprise companies. The failure mode is predictable. The lab produces impressive demos, the core ignores them, nothing reaches customers at scale, a budget cycle arrives, and the lab gets shut down. Many high-profile corporate labs have followed this arc. Independence solves the *creation* problem but makes the *scaling* problem worse, and in enterprise software, scaling is the hard part. Insurance carriers buy on trust, compliance, integration with core systems, and reference customers. A lab has none of those. The core organization has all of them.

## First, diagnose before you design

You were hired to produce outsized results, but the burning platform is churn and lost deals. Before committing to any structure, spend 4–6 weeks finding out *why*. In insurance software, the causes are usually some mix of:

- **Implementation pain:** multi-year deployments, cost overruns, slow time-to-value
- **Upgrade burden:** customers stuck on old versions because upgrades are expensive projects
- **Architecture gap:** competitors (Guidewire, Duck Creek, cloud-native insurtechs) offering SaaS, open APIs, and configurability that carriers now expect
- **Product gaps:** weak data, analytics, AI in underwriting or claims, digital distribution
- **Service and relationship failures:** poor support, account management, or trust

Interview churned customers, lost prospects, your sales engineers, and implementation teams. Win/loss data will tell you more than any strategy framework.

Then sort what you find into two buckets:

1. **Execution and sustaining problems** (implementation, quality, support, incremental features). These belong **in the core**. A lab would be a distraction, and pulling them out would signal that you're avoiding the real fire.
2. **Genuinely new capabilities or models** (a cloud-native product, an AI-driven claims offering, a new SMB or MGA segment, usage-based pricing). These need **protected space**, because the core will not do them well.

My experience is that bucket 1 usually explains most of the churn, and bucket 2 determines whether the company still matters in five years. You need both, but they need different structures.

## The structure that works: separate, but not independent

The research on this (O'Reilly & Tushman on "ambidexterity," Govindarajan & Trimble's *The Other Side of Innovation*) converges on something between your two options:

**Separate where it matters:**
- A small dedicated team with its own leader, metrics, and processes
- Different success measures: learning milestones and customer validation, not quarterly revenue
- Freedom from the core's release cadence, architecture review boards, and planning cycle
- Protected, stage-gated funding, so the team isn't renegotiating its existence every quarter

**Linked where it matters:**
- A named executive sponsor, ideally the CEO, who arbitrates conflicts with the core
- Shared access to customers, sales, and domain experts from day one
- Deliberate use of core assets: customer relationships, data, compliance expertise, brand
- An explicit, pre-agreed path for how validated work transfers to or is scaled by the core, including who owns it, who funds it, and what the core gets credit for

Core leaders should see the innovation team as a source of their future growth, not as a critique of them or a competitor for budget. If the lab is framed as "the people who couldn't innovate vs. the people who can," the core will make sure it fails.

## How to handle the CEO

Don't position this as disagreeing with him. His instinct has real merit: the talent, customers, and domain knowledge inside the company are its biggest assets, and a lab that ignores them will fail. Build on that:

> "You're right that we win by using what we already have. Most of what's driving churn needs to be fixed inside the core, and I'll help drive that. But a few bets won't survive our standard processes. I want a small, protected team for those, tightly connected to the business, with clear milestones and a defined path back into the core."

That's a request he can say yes to. It's also a much smaller ask than "fund an independent lab," which makes it easier to expand once you've shown results.

## A practical first 90 days

- **Days 1–30:** Listen and diagnose. Hold churn and win/loss interviews, map the core's innovation blockers, and identify allies among core leaders.
- **Days 30–60:** Deliver one visible win *inside* the core, such as cutting implementation time on a key module or unblocking a feature customers are leaving over. This buys credibility you'll need later.
- **Days 60–90:** Propose 2–3 bucket-2 bets with a small dedicated team, clear kill/continue criteria, and named customer design partners (carriers willing to co-develop).

## Warning signs to watch for

- You're measured on revenue within 12 months for genuinely new bets
- Core leaders aren't involved in selecting or scaling the bets
- The team has no real customers, only internal demos
- There's no agreed answer to "what happens if this works?"
- You're quietly expected to fix the churn problem single-handedly through "innovation"

**Bottom line:** You're right that some work needs protection from the core. The CEO is right that the core is where the assets and the scale are. The winning strategy is to diagnose first, fix execution problems inside the core, and put a small, deliberately linked team on the few bets that are genuinely new. Earn the right to expand it with results rather than asking for independence upfront.

## Summary (sent to Jev)

The response argues that neither strategy is right as stated, and that framing the choice as "lab vs. no lab" could cost the new hire the argument and possibly the job. Working purely within existing systems tends to fail because established organizations smother anything uncertain or threatening to current revenue. Fully independent labs also have a poor enterprise track record: they produce demos the core ignores, never scale, and get cut. That is especially true in insurance software, where carriers buy on trust, compliance, integration, and reference customers, all of which the core holds.

It recommends diagnosing before designing. Spend four to six weeks interviewing churned customers, lost prospects, sales engineers, and implementation teams, and review win/loss data. Then sort the findings into two buckets. Execution problems such as implementation pain, upgrade burden, support, and incremental features belong in the core. Genuinely new capabilities, such as cloud-native products, AI claims offerings, new segments, or new pricing, need protected space. The author expects the first bucket explains most of the churn and the second determines relevance in five years.

The proposed structure is "separate, but not independent." It calls for a small dedicated team with its own leader, metrics, processes, and stage-gated funding. That team should be linked to the business through a named executive sponsor, shared access to customers and experts, use of core assets, and a pre-agreed path for transferring validated work to the core.

The response advises pitching this to the CEO as building on his instinct, not opposing it. Its 90-day plan is: diagnose first, deliver a visible win inside the core, then propose two or three bets with kill criteria and customer design partners. It warns against:

- Short-term revenue targets for new bets
- Uninvolved core leaders
- Internal-only demos
- No answer to "what happens if this works"
- Being expected to fix churn single-handedly
