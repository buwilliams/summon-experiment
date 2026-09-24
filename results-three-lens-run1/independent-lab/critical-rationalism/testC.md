# critical-rationalism/independent-lab/testC

Model: claude-opus-5-5 · 2026-09-24T14:44:58.539968+00:00

## Turn 1

**User:** Use the method of conjectures and refutations (critical rationalism) to answer the following.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

# Innovation Lab or Existing Systems? A Critical-Rationalist Analysis

## 1. Start with the problem, not the solutions

Popper held that inquiry begins with a problem, and that a poorly stated problem produces untestable answers. "Which strategy is right?" is a question about means. The underlying problem is:

> **Why are customers leaving and prospects choosing someone else, and what change would reverse that fastest?**

Both your view and the CEO's view are conjectures about *organizational structure*. Neither is yet a conjecture about *why customers are leaving*. That gap turns out to matter.

---

## 2. Conjecture A (the CEO's): "We can turn around within existing systems, procedures, and talent."

**Stated boldly:** The organization's capabilities are adequate. The problem is focus, execution, or prioritization, and better leadership inside the current structure will fix it.

**What it predicts (and therefore what could refute it):**
- Churned customers left for reasons the current organization *could* fix: bugs, service quality, missing features on the roadmap, pricing.
- There are good ideas already inside the company that are being slowed, not missing.
- Past improvement initiatives failed for identifiable, correctable reasons rather than being absorbed and neutralized.

**Attempted refutations:**
- **The system produced the problem.** The current processes, incentives, and talent mix are what generated the decline. Expecting the same system to produce different outputs requires explaining *what changes*. "Better leadership" is not yet a mechanism.
- **Base rates.** Incumbent enterprise software firms facing cloud-native or platform competitors (in insurance: Guidewire, Duck Creek, and newer API-first cores like Socotra or EIS) rarely recover through incremental improvement alone. Their processes are optimized for existing customers, and existing customers ask for incremental things (Christensen's core argument).
- **Your own hiring is evidence against it.** The CEO hired an outside innovation leader and asked for *outsized* results. That implicitly concedes the existing system isn't producing them.

**Verdict:** Seriously wounded, but not refuted. If churn is driven by fixable execution problems, A could be correct, and a lab would be an expensive distraction.

---

## 3. Conjecture B (yours): "Innovation requires an independent lab."

**Stated boldly:** The core organization's processes, risk tolerance, and culture will kill new ideas, so innovation must be structurally separated to survive.

**What it predicts:**
- The lab will produce things the core could not have.
- Those things will reach customers and affect churn and win rates.

**Attempted refutations:**
- **The graveyard of corporate labs.** Many independent innovation labs fail. They become "innovation theater": demos, hackathons, and prototypes that never ship. Xerox PARC is the canonical case: brilliant invention, near-zero capture by the parent. Independence protects ideas from the antibodies, but it also cuts them off from distribution, customers, data, and the core systems they must eventually integrate with.
- **The integration problem is acute in insurance software.** Your customers are regulated carriers with policy, billing, and claims systems, long procurement cycles, and heavy compliance requirements. An isolated lab building something new still faces those constraints the moment it touches a real customer. Separation doesn't remove them. It postpones them.
- **Time horizon mismatch.** Customers are leaving *now*. A lab building a new offering typically needs 18–36 months to affect revenue. If churn is the bleeding wound, a lab may be the right answer to a different question.
- **Political survival.** A lab set up against the CEO's stated belief has no sponsor when it hits its first setback, and it will hit one.

**Verdict:** Also wounded. B correctly identifies a real failure mode (the core rejecting novelty) but proposes a remedy with its own well-documented failure mode (the novelty never reaching the core's customers).

---

## 4. What the refutations reveal: a shared hidden assumption

Both conjectures assume **structure is the decisive variable**. But the criticism of each keeps pointing back to the same unknown: *what is actually causing churn and lost deals?*

| If the cause is... | Then the better conjecture is... |
|---|---|
| Execution: bugs, poor service, slow delivery | A (fix the core) |
| Product gap: customers want capabilities you're far from | B-like (build separately) |
| Architecture: your platform can't compete with modern cores | B, and possibly a much bigger bet |
| Price or business model | Neither; this is a commercial strategy problem |

You don't yet know which row you're in, and I suspect the CEO doesn't either. The disagreement between you may be unresolvable in its current form because neither of you has stated a theory of the customer problem that evidence could refute.

---

## 5. An improved conjecture (C)

Here is a bolder, more testable conjecture that survives the criticisms above better than either original:

> **Create a small, autonomous team with independent decision rights and processes, but aimed at the specific reasons customers are leaving, working directly with at-risk and recently lost customers, and with a pre-agreed path into the core product and sales channel.**

This keeps the part of B that survived criticism: protection from the core's processes and antibodies. It also keeps the part of A that survived: using existing customers, distribution, and domain talent. Organizational researchers call this "ambidexterity" (O'Reilly and Tushman), but the label matters less than the fact that it is falsifiable.

**Conjecture C is refuted if, within a defined window (say 6 months):**
- The team cannot get meaningful access to customers, data, or engineers without escalating to the CEO repeatedly, which would show the core's antibodies are stronger than autonomy can overcome and push you toward full separation (B).
- Customer research shows churn is driven by fixable execution issues, which would push you toward A, with your role becoming change agent for the core rather than lab leader.
- The team ships something customers value but the core cannot absorb or sell it, which would show integration is the binding constraint.
- At-risk customers show no change in retention intent after engaging with what you've built.

Notice that each refutation tells you which direction to move. That is the point: a good conjecture fails *informatively*.

---

## 6. Critical tests to run first (cheap, fast, designed to fail if you're wrong)

1. **Churn autopsy (weeks 1–6).** Interview 15–20 lost customers and lost prospects yourself, not through sales. Ask what they chose instead and why. This single test may refute A or B outright.
2. **Antibody test.** Pick one small, customer-requested change and try to ship it through normal channels. Time it, and document every blocker. This tests A directly.
3. **Pilot autonomy.** Ask for a team of 5–8 people with explicit exemptions from specific processes (procurement, release gates, reporting), aimed at one problem the autopsy surfaced. This tests C at low cost.
4. **Pre-register kill criteria with the CEO.** Agree *in advance* on what result would change each of your minds.

---

## 7. Tentative conclusion

Neither strategy, as stated, is "right." Both are conjectures with known failure modes, and both skip the prior question of *why customers are leaving*. Your intuition about the core's antibodies is well supported. Your proposed remedy, full independence, is the version most likely to produce impressive work that doesn't save the company.

The best current answer is Conjecture C: a small, protected team aimed at the churn problem and connected to the core's customers and channels. Hold it tentatively, and replace it the moment the evidence refutes it.

Critical rationalism also gives you a way through the disagreement with your CEO. Don't try to win the argument by authority or persuasion. Propose that you both state what evidence would prove each of you wrong, then go get it. A CEO who wants outsized results should accept that, and his reaction will tell you a lot about whether any strategy can succeed there.

## Turn 2

**User:** Suppose the churn interviews come back showing customers are leaving mainly because our core platform is outdated compared to Guidewire and the API-first players: how does that change your analysis?

**Assistant:**

# Revising the Analysis After the Churn Evidence

## 1. First, criticize the evidence itself

Popper insisted that observations are theory-laden and fallible, so before acting on "the platform is outdated," test the finding.

- **Lost customers give socially convenient reasons.** "Your platform is outdated" is easier to say than "your implementation burned us" or "your competitor offered a better price." Did the interviewees name specific capabilities, or use "outdated" as a summary verdict?
- **"Outdated" bundles several different problems, and they imply different remedies:**

| What "outdated" might mean | Likely remedy |
|---|---|
| On-premise delivery; customers want SaaS | Hosting and operations change; hard, but not a rewrite |
| Poor integration; no modern APIs | API layer over the legacy core |
| Slow to launch or change insurance products | Configurability in the core, usually requiring re-architecture |
| Dated user interface | New front end; the cheapest fix |
| Weak data and analytics | Data platform alongside the core |
| All of the above | Genuine platform replacement |

Before redesigning the company, go back to the interview notes and code each departure against this list. If the answer is mostly integration and user interface, you face a much smaller problem than if it is configurability and architecture. For the rest of this analysis I'll assume the finding survives this scrutiny: the core architecture itself is the problem.

---

## 2. What the evidence refutes

A good test should kill something. This one wounds all three earlier conjectures.

- **Conjecture A (the CEO's: fix within existing systems) is refuted in its strong form.** If the product itself is structurally behind, better execution of the existing roadmap won't close the gap. The CEO's premise was that the organization's capabilities are adequate, and the customers have said they aren't.
- **Conjecture C (a small autonomous team aimed at churn) is refuted as stated.** Six to eight people cannot re-platform an enterprise insurance system in six months. C was scaled for a product-gap problem, and this is an architecture problem.
- **Conjecture B (independent lab) is refuted as framed but strengthened in principle.** An "innovation lab" producing prototypes won't fix the core. However, the underlying logic of separation is now much better supported. Christensen's strongest case for a separate unit is exactly this one: the new thing requires a different architecture, will compete with the existing product, and threatens revenue the core organization depends on. The core will rationally starve a project designed to replace it.

---

## 3. The problem has changed

The new problem is no longer "how do we innovate?" It is:

> **Our core product is structurally behind well-funded competitors. Customers are leaving now. What do we do about the platform, and how do we survive the years it takes?**

This is a corporate strategy question, possibly an existential one. It belongs to the CEO and the board, not to an innovation mandate. That matters for your role, which I return to below.

---

## 4. Rival conjectures for the new problem

**D1: Build a new platform in a separate unit.**
A properly funded new business, not a lab, builds a modern core with its own team, processes, and eventually its own customers, then migrates the installed base.
- *Criticisms:* Guidewire and the API-first players have years of head start and heavy investment. A new build arrives late to a crowded market, and "second-system" rewrites are notorious for overrunning (Joel Spolsky's warning about rewrites from scratch applies). Migration of regulated carriers is slow and risky, so churn continues during the build.
- *Survives if:* the company can fund multiple years of investment and has some reason customers would choose a late entrant.

**D2: Incremental modernization (the "strangler fig" pattern).**
Wrap the legacy core in modern APIs, move to cloud hosting, then replace modules one at a time until the old core is gone.
- *Criticisms:* This can stall halfway, leaving you maintaining two systems. It may not fix configurability, the deepest architectural gap. Competitors keep moving while you catch up.
- *Advantages:* It delivers value to current customers early, which slows churn, and it works *with* the existing organization, preserving parts of the CEO's view.

**D3: Stop competing on the core; reposition.**
Concede the full-core fight and win somewhere narrower: a specialty line of business, a customer segment such as small mutual insurers, or a complementary layer (rating, distribution, claims analytics) that runs alongside Guidewire rather than against it.
- *Criticisms:* The company shrinks before it grows, and it requires admitting the current strategy is over.
- *Advantages:* This is the boldest conjecture and in some ways the most testable, because it depends on the company having a real advantage somewhere.

**D4: Structural options: partner, acquire, merge, or sell.**
Buy a modern core, license one, or recognize the company is worth more to an acquirer than as a standalone.
- *Criticisms:* This is outside your remit, and acquisitions carry their own integration failures.
- *Why include it:* Critical rationalism demands we not exclude conjectures because they are uncomfortable.

---

## 5. Which survives criticism best, pending tests

The most defensible current position is a **two-track conjecture**, with one track possibly replaced by D3:

1. **A retention bridge inside the core (D2-style):** APIs, cloud hosting, and user interface improvements that give current customers reasons to stay. This buys time and uses existing talent, which is where the CEO's instinct survives.
2. **A separately governed new-platform effort (D1) or a repositioning (D3).** Which of these depends on the answers to the tests below. Either way it needs real separation, meaning its own budget, leadership, and metrics, because it will threaten the core's revenue.

**Discriminating tests:**
- **Study the customers who stay.** Retained customers are the most informative group you haven't interviewed. If they stay because of deep functionality in a particular line or segment, that is evidence for D3. If they stay only because switching is painful, you are on borrowed time.
- **Quantify the gap.** Which specific capabilities would it take to win back, say, three of the recently lost accounts? Estimate the engineering cost and time. If the answer is "years and a full rewrite," D1 has to be weighed against D3 and D4.
- **Test capital reality.** Ask the CFO or board what multi-year investment is actually available. D1 is refuted immediately if the money isn't there.
- **Pilot the strangler.** Build one modern API or module on the legacy core and put it in front of an at-risk customer. Measure delivery time and whether it changes their renewal intent. This tests D2 cheaply.
- **Probe partners.** Exploratory conversations about licensing or complementing a modern core test D3 and D4 without committing to either.

---

## 6. What this means for you and the CEO

- **The CEO's conjecture has been refuted by his own customers, not by you.** Present it that way. You agreed in advance on what evidence would change minds, and this is it. That framing lets him update his view without losing face.
- **Your original conjecture was also refuted.** An innovation lab was an answer to the wrong problem. Saying so openly earns the credibility you'll need, and it models the kind of error correction the company now depends on.
- **Recognize the scope has changed.** A platform-architecture problem is bigger than an innovation mandate. Either your role expands to lead or shape the platform strategy, with the authority and budget that implies, or you risk being held responsible for "outsized results" on a problem you have neither the tools nor the authority to solve. Raise this explicitly.
- **Keep kill criteria on the new plan too.** For example: if the strangler pilot can't ship a customer-visible improvement within a quarter, or if retained customers show no distinctive advantage, move to the next conjecture rather than defending the current one.

## Tentative conclusion

The evidence moves you from "which organizational structure?" to "what is our platform strategy, and how do we survive while executing it?" Separation is now better justified than before, but as a serious new-platform business or a deliberate repositioning, not a lab. It should be paired with a retention bridge inside the core. Which long-term track to choose depends on three things you can find out quickly: why the remaining customers stay, how large the technical gap really is, and how much capital exists to close it.

## Turn 3

**User:** Say the CFO comes back and tells us there's only enough capital for about 18 months of serious investment. Using the same critical-rationalist approach, which of these conjectures still stand?

**Assistant:**

# Re-Testing the Conjectures Under an 18-Month Capital Limit

## 1. First, criticize the new evidence

The CFO's figure is now a test for every conjecture, so it deserves the same scrutiny the churn findings got.

- **What does "18 months of serious investment" mean?** It could mean 18 months before the company runs out of cash, or 18 months of discretionary budget on top of normal operations. These are very different situations. The first is a survival problem; the second is an investment-allocation problem.
- **The number is probably optimistic.** The CFO's model likely assumes current revenue continues. But customers are leaving because of the platform, and churn may accelerate once the market senses weakness. Ask for a downside case. If churn increases, 18 months may really be 12.
- **The number may be movable.** Runway can be extended by cutting legacy costs, redirecting existing R&D spend, getting customers to co-fund development, partnering, or raising outside capital. Each of these is a separate conjecture, but none should be ruled out simply because they weren't in the CFO's baseline.

For the analysis below, I'll treat 18 months as a hard limit, with the warning that the real constraint may be tighter.

---

## 2. Testing each conjecture against the constraint

**D1: Build a new platform in a separate unit. Refuted.**
Modern insurance core platforms take years to build and reach carrier-grade maturity. Even the API-first players needed several years, and implementing a new core at a carrier takes another 12 to 24 months. Within 18 months you might have an incomplete product and no revenue from it. D1 survives only if outside capital is raised, which is a different conjecture (part of D4), not D1 itself.

**D2: Incremental modernization (strangler fig). Refuted in its full form; a narrow version survives.**
Replacing the legacy core piece by piece is also a multi-year effort. A limited version still stands: APIs, cloud hosting, and a modern user interface that make the existing product easier to keep and easier to integrate. But criticism exposes a new weakness. **A bridge only makes sense if it leads somewhere.** Spending the runway modernizing a platform you can't finish modernizing just delays the decline. Narrow D2 survives only as support for another destination, not as a strategy by itself.

**D3: Reposition into a niche or complementary layer. Strengthened.**
This is the conjecture most compatible with limited capital. It concentrates spending, builds on what already exists, and can produce revenue within the window. A complementary product that works alongside Guidewire or the API-first cores could be faster still, because it turns competitors into distribution channels.
- *Remaining criticism:* The niche may be too small to support the current cost structure. D3 may therefore imply a smaller company, which the CEO and board must be prepared to accept.
- *Still depends on:* the retained-customer analysis showing that some segment stays for a real, defensible reason.

**D4: Partner, license, merge, or sell. Strengthened significantly.**
The capital limit changes this from an uncomfortable option into a leading one.
- **Partnering or licensing:** An API-first core provider may want your installed base, domain expertise, and implementation capacity. Licensing their core and migrating your customers onto it could fix the platform problem without building anything.
- **Sale or merger:** A company's value to an acquirer declines as its customers leave. If selling is the right answer, it is better to sell at month 3 than at month 15. **Timing matters most here.** Delay does not keep this option open; it reduces its value.
- **Acquiring a modern core:** Probably refuted, since there isn't capital for it.
- *Criticism:* Partnerships take time to negotiate and can fail late. Sale processes consume management attention and can alarm customers and staff if they leak.

**Two-track strategy (bridge plus new platform). Refuted as a balanced split.**
Splitting limited capital between a retention bridge and a major new build means doing both badly. The two-track idea survives only in an unequal form: a small bridge budget whose sole purpose is to protect whichever destination you choose.

**A (the CEO's original conjecture). Partly revived, unexpectedly.**
With limited capital, you can't hire a large new team or fund an independent unit for long. The existing people, customers, and domain knowledge are most of what you have. The CEO was wrong that the current system could fix the platform. But he may be right that the path forward must be built from existing assets. Acknowledging this will matter in your conversations with him.

---

## 3. Summary

| Conjecture | Status under 18-month limit |
|---|---|
| A: Fix within existing systems | Refuted as a platform fix; partly revived as "use existing assets" |
| B/D1: Separate unit builds new platform | Refuted, unless outside capital is raised |
| D2: Full strangler modernization | Refuted; narrow bridge survives only in support of another path |
| D3: Niche or complementary layer | Strengthened; depends on retained-customer evidence |
| D4: Partner, license, merge, or sell | Strengthened; the value of this option declines with time |
| Two-track (balanced) | Refuted; survives only as a small bridge plus one destination |

---

## 4. The surviving conjecture

> **Choose one destination, D3 or D4 (or a combination such as repositioning around a partner's core), within about three months. Fund a narrow bridge only to the extent it protects that destination. Put essentially everything else behind it.**

The key change in reasoning is that **keeping options open now has a cost.** Earlier, running several experiments in parallel was cheap insurance. Now every month spent undecided consumes runway and reduces the value of the sale and partnership options. Critical rationalism does not demand certainty before acting. It asks you to act on the best surviving conjecture while arranging to detect error quickly.

---

## 5. Tests compressed into weeks, not quarters

**Months 0–3: run these in parallel, at low cost**
1. **Retained-customer analysis (tests D3).** Why do the remaining customers stay? Is there a segment or line of business where you are genuinely strong? If none exists, D3 is refuted.
2. **Partner and acquirer conversations (tests D4).** Quiet, board-sanctioned discussions with two or three API-first players and potential acquirers. The market will answer quickly: either someone values your installed base and expertise, or no one does. Both answers are informative.
3. **Niche validation (tests D3).** Take a specific proposition to three to five target customers. Will they sign letters of intent or co-fund development?
4. **Bridge pilot (tests narrow D2).** Ship one API or user-interface improvement to an at-risk account and measure whether their renewal intent changes.

**Month 3: decision point.** Commit to one destination based on which conjectures survived.

**Month 9: checkpoint with pre-agreed kill criteria.** For example:
- If the niche hasn't produced signed revenue, move toward D4 while the company still has value.
- If partnership talks haven't produced term sheets, return to D3 or a sale.
- If churn outpaces the CFO's model, bring the decision forward.

---

## 6. Implications for you

- **The question is now a turnaround question, not an innovation one.** It involves the CEO, the board, and possibly the future of the company. Raise this directly. Your mandate, authority, and success measures need to reflect the actual problem.
- **Watch your own bias.** You were hired to lead innovation, and some surviving conjectures, such as a sale or a smaller niche company, may make that role smaller or eliminate it. Critical rationalism requires you to criticize most rigorously the ideas you have a personal stake in. Saying so openly will strengthen your credibility with the CEO and board.
- **Keep error correction fast.** Under an 18-month limit, the biggest risk is not choosing the wrong conjecture. It is holding on to a wrong one for too long because nobody agreed in advance on what would prove it wrong.

## Tentative conclusion

Building a new platform and full modernization are both refuted by the 18-month limit. The conjectures still standing are repositioning into a niche or complementary layer (D3) and partnering, licensing, or selling (D4), supported by a narrow retention bridge. Test D3 and D4 quickly and in parallel, decide within about three months, and treat time as the scarcest resource. Every month of delay reduces the value of the options that remain.

## Turn 4

**User:** What if the retained-customer analysis shows our loyal base is concentrated among small regional mutual insurers who stay for our workers' comp functionality? Using the same approach, how does that affect D3 versus D4?

**Assistant:**

# How the Workers' Comp Finding Changes D3 and D4

## 1. First, criticize the evidence

This finding looks like exactly what D3 needed, which is a reason to examine it harder, not less.

- **"Stay for" or "stuck with"?** Small regional mutuals may stay because your workers' comp (WC) functionality is genuinely better. They may also stay because switching is expensive for a small insurer with a lean IT staff, because larger vendors don't want their business, or because of long personal relationships. Only the first reason is a durable advantage. The others are a temporary reprieve.
- **Is WC the reason, or just where they happen to use you?** Many small mutuals write several lines, such as farm, homeowners, and commercial. Do they run everything on your platform and consider WC the part that works best, or do they use you only for WC? The answer determines whether your asset is a WC product or a small-mutual platform.
- **Is the depth real?** WC is a demanding line: state-by-state rules, rating-bureau requirements such as NCCI's, experience modifications, medical fee schedules, and mandatory electronic claims reporting to state agencies (IAIABC EDI standards). If your functionality handles this complexity well across many states, that is a genuine barrier to competitors. If it covers only a few states, the barrier is much smaller.
- **Is the segment large and stable enough?** Small mutuals have been consolidating for years through mergers and affiliations. A loyal base that shrinks by a few customers a year through mergers is still a shrinking base.

Assume, for the rest of this analysis, that the finding survives: the WC depth is real, and it is a meaningful reason these customers stay.

---

## 2. What the finding does to the rival conjectures

The main effect is surprising. **D3 and D4 are no longer competing strategies. They now share the same central asset.** Whether you build or sell, the WC capability and the loyal base are what create value. The real question becomes who captures that value and when.

### D3: Reposition. Strengthened, and it splits into three variants

**D3a: Become the core platform for small regional mutuals.**
- *For:* You already have the customers, the relationships, and domain credibility. Large vendors largely ignore this segment because the deals are small.
- *Against:* It doesn't fix the problem the churn interviews identified. These customers are running on the same outdated platform, and the forces that took your larger customers will eventually reach them. Serving a whole platform to many small customers also requires broad functionality, which your capital can't fund. **Weakened.**

**D3b: Make WC a standalone or add-on product that works with other core systems.**
- *For:* It concentrates limited capital on your strongest asset. It enlarges the market from "small mutuals using your platform" to "any insurer writing WC," including carriers running Guidewire or API-first cores. It turns competitors into potential distribution channels. It is also the only variant that doesn't require fixing the whole legacy platform.
- *Against:* It depends on whether the WC logic can be separated from the legacy system. If it is deeply entangled, extracting it may take longer than your runway. It also means selling into new customers where you have no track record. **Strengthened, but dependent on a technical test.**

**D3c: Use D3a as the anchor for D3b.**
Keep the small mutuals as a stable revenue base and as design partners while building the WC product for the broader market.
- *Against:* The risk is splitting limited capital again. This works only if serving the mutuals requires little new investment. **Survives only with a strict budget limit on the anchor.**

### D4: Partner, license, merge, or sell. Strengthened and clarified

Before this finding, D4 meant selling a declining generalist vendor. Now there is something specific and more valuable to sell or partner around.
- **Partnership:** API-first core providers generally want strength in specialized lines to win carriers. A WC product integrated into a partner's platform or marketplace could provide distribution that D3b otherwise lacks. **This is where D3b and D4 merge.**
- **Sale:** A focused business with a loyal base and difficult-to-replicate domain knowledge is more attractive to buyers than a declining generalist. Potential buyers include core vendors that are weak in WC, vendors serving small and mid-sized insurers, and private-equity investors assembling specialist insurance software companies.
- **Carve-out:** Sell or wind down everything except WC, and keep the WC business. This is D3 and D4 combined.
- *Criticism:* A buyer might value the WC knowledge but not your code, and pay accordingly. The timing problem from the last round still applies: the value of the base erodes as the platform ages.

---

## 3. Summary

| Conjecture | Status after the WC finding |
|---|---|
| D3a: Core platform for small mutuals | Weakened; doesn't solve the outdated platform |
| D3b: WC product that works with any core | Strengthened; depends on technical separability |
| D3c: Mutuals as anchor for WC product | Survives only with strict limits on anchor spending |
| D4: Partner around WC | Strengthened; supplies the distribution D3b lacks |
| D4: Sell whole company or the WC business | Strengthened; better asset to sell, still time-sensitive |
| Everything else (non-WC lines, general customers) | Candidates to maintain cheaply, sell, or wind down |

---

## 4. The surviving conjecture

> **Make workers' comp the whole strategy. Build it as a product that can work alongside other core systems (D3b), using the loyal mutuals as design partners and base revenue. Seek at least one core-platform partner for distribution (D4). Treat a sale of the WC business or the whole company as an active alternative, not a last resort. Decide between "build with partners" and "sell" based on the tests below.**

This conjecture is bold in a useful way. It predicts specific things that could easily be shown false: that WC can be separated from the legacy system, that other carriers will buy it, and that partners will distribute it.

---

## 5. Tests, sequenced for an 18-month runway

1. **Separability test (weeks).** Have your strongest engineers try to expose one WC capability, such as state electronic reporting or experience-mod calculation, as a standalone service. If WC is too entangled with the legacy system to extract within a few months, D3b is refuted and D4 (selling) becomes the leading option.
2. **"Stay for or stuck with" interviews (weeks).** Ask the loyal mutuals whether they would buy the WC product separately if they changed core systems, whether they would pay more for it, and whether they would recommend you to peers. Tolerance is not loyalty.
3. **Market test outside the base (1–2 months).** Take the WC proposition to carriers running Guidewire or API-first cores. Look for letters of intent, pilots, or co-funding, not just polite interest.
4. **Segment economics (weeks, with the CFO).** How much revenue and margin do the loyal mutuals represent? How many potential customers exist, and how fast is consolidation removing them? Could a WC-focused company cover a restructured cost base within the runway? If not, D3 alone is refuted and D4 must carry more weight.
5. **Partner and buyer conversations, now centered on WC (1–3 months).** The market will tell you what the WC asset is worth, and whether partners want to distribute it or would rather acquire it.

**Decision rule at about month 3:**
- Separable, with external demand and a willing partner: build (D3b plus a D4 partnership).
- Separable and in demand, but segment economics don't cover costs: carve out WC and sell or shrink the rest.
- Not separable, or no demand outside the base: sell while the loyal base still gives the company value.

---

## 6. Implications

- **For the CEO:** His belief in existing talent is partly vindicated again. Your WC experts, product managers, and implementation staff may now be the most valuable people in the company. Losing them during an uncertain period would undermine both D3 and D4, so retaining them should be an immediate priority.
- **For the rest of the business:** A WC-focused strategy implies hard decisions about everything else. Non-WC products and customers need an explicit plan: maintain at minimal cost, sell, or migrate. Leaving that undecided wastes the runway.
- **For you:** This is the first result where an innovation leader's skills fit the problem well, since building a focused product quickly with design partners is exactly that kind of work. That is also a reason for caution. Apply the hardest criticism to the conjecture that most flatters your role, and keep the sale option genuinely alive rather than treating it as a failure.

## Tentative conclusion

The finding doesn't simply favor D3 over D4. It shows they are built on the same asset. The strongest surviving conjecture is a focused WC product that works with other core systems, anchored by the loyal mutuals and distributed through partners, with a sale kept as a serious alternative. Three tests will decide between building and selling: whether WC can be technically separated, whether insurers outside your base will buy it, and whether the segment's economics can sustain the company.

## Turn 5

**User:** What should we do?

**Assistant:**

# What You Should Do

## The recommendation

**Reorganize the company around workers' comp.** Build WC into a product that works alongside other core systems, anchored by your loyal small mutuals and distributed through at least one core-platform partner. At the same time, run a serious, board-sanctioned partner and sale process for about 90 days. At day 90, commit to either building or selling, using a decision rule agreed with the board in advance.

My default expectation is that you build with a partner, because it keeps the most value and uses your real advantage. But one test decides it: **whether WC can be separated from the legacy platform quickly.** If it can't, sell.

This is a conjecture, not a certainty. It is the one that has survived every piece of evidence so far, and it is specific enough to be proven wrong quickly, which is what you need with 18 months of capital.

---

## Weeks 1–2: moves to make regardless of the final decision

These steps are worth taking whether you ultimately build or sell, so there's no reason to wait.

1. **Take the chain of evidence to the CEO, then the board.** Present how you got here: churn caused by the platform, a limited runway, and a loyal WC base. Propose the strategy and the day-90 decision rule. Ask the board to authorize confidential partner and buyer conversations, ideally with an adviser so management isn't distracted.
2. **Extend the runway.** Freeze new development outside WC, cut discretionary spending, and redirect the savings to WC. Ask the CFO for a downside model that assumes churn accelerates.
3. **Lock in your WC people.** Identify the 10–20 engineers, product managers, and implementation specialists who hold the WC knowledge, and offer retention agreements now. Every path, including a sale, depends on them.
4. **Protect the loyal base.** Assign senior executives to your top mutual accounts. Your message should be that you're investing in what they value. Limit any "bridge" spending to what these customers need to stay.

## Weeks 2–12: run the decisive tests in parallel

| Test | Refutes building if... |
|---|---|
| **Separability:** can a small team expose one WC capability as a standalone service? | It can't be done within a few months |
| **Loyalty check:** would the mutuals buy WC separately, pay more, or recommend you? | They are staying out of inertia, not preference |
| **Outside demand:** will carriers on Guidewire or API-first cores sign pilots or letters of intent? | No one outside your base commits |
| **Segment economics:** can a WC-focused company cover a restructured cost base? | The numbers don't work even after cuts |
| **Partner and buyer interest:** will a core provider distribute WC, or will a buyer pay a good price? | Establishes what selling is worth, and so what building must beat |

## Day 90: decide

- **Separable, with outside demand and a willing partner:** build.
- **Separable and in demand, but the economics don't support the whole company:** keep WC, and sell or shrink everything else.
- **Not separable, or no outside demand:** sell while the loyal base still gives the company value.

Also decide by day 90 what happens to the non-WC products and customers: maintain at minimal cost, sell, or migrate. Leaving that open quietly consumes the runway.

## If you build: months 3–18

- **Form a small, autonomous WC product team** with its own decision rights and exemptions from the processes that slow the core organization. This is your original innovation-lab idea, now aimed at the one problem where it can pay off.
- **Work with three to five loyal mutuals as design partners,** and integrate with at least one partner's core.
- **Checkpoint at month 9.** If you have no paying customer outside your base and no partner integration in production, move to a sale while the company still has value.

---

## What would change this recommendation

Change course if any of these turn out to be true:
- WC turns out to be deeply entangled with the legacy system.
- The mutuals are staying because switching is hard, not because your WC product is better.
- A buyer offers more than the realistic value of building.
- Churn in the loyal base itself begins to rise.

Agree with the CEO and board now that these would trigger a change of course, so no one has to win an argument later.

## For you personally

Ask to lead the WC product effort, with real authority over the team and budget. But be the person pushing hardest to test the sale option. That protects the company from your own bias, and it's the strongest demonstration to the CEO and board that you're serving the business rather than your role.

On your original question: neither you nor the CEO was right as first stated. You need an independent team, as you argued, but a focused one inside a company reorganized around its real strength. And the existing talent and customers the CEO wanted to rely on turn out to be what makes that strategy possible.

## Outcome summary (sent to Jev)

The assistant recommends reorganizing the company around its workers' comp functionality. The goal is to build it into a product that works alongside other core systems, anchored by the loyal small regional mutuals and distributed through at least one core-platform partner. In parallel, the company would run a confidential, board-sanctioned partner and sale process for about 90 days, then commit to building or selling under a decision rule agreed in advance.

The reasoning is that churn stems from an outdated platform, 18 months of capital rules out a new build or full modernization, and the workers' comp capability plus its loyal base is the company's one real asset, whether built on or sold. Building with a partner is the default expectation because it keeps the most value, but selling is a genuine alternative whose value declines with time.

Immediate steps:
- Present the evidence and plan to the CEO and board.
- Freeze non-workers'-comp development to extend the runway, and get a downside cash model.
- Lock in the 10–20 key workers'-comp staff with retention agreements.
- Assign senior executives to the top mutual accounts.

Tests to run in parallel over weeks 2–12:
- Can workers' comp be technically separated from the legacy platform?
- Are the mutuals loyal or merely stuck?
- Will carriers on other cores sign pilots?
- Do the segment's economics work?
- What would partners or buyers offer?

If the company builds, a small autonomous workers'-comp team would work with three to five mutuals as design partners. A month-9 checkpoint would trigger a sale if there is no outside paying customer and no partner integration in production.

Caveats: this is a conjecture, not a certainty. The team should change course if workers' comp proves entangled, loyalty proves to be inertia, a buyer outbids the value of building, or churn hits the loyal base. The fate of non-workers'-comp products must also be decided. The user should lead the effort while pushing hardest to test the sale option.
