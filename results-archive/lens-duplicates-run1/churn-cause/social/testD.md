# churn-cause/social/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:56:11.084424+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to know which approach wins approval and improves standing. Consider how each proposal would play inside and outside the company. Who gains status or credit, and who risks losing face or taking the blame? If each proposal went ahead, what would it signal to the board, employees, customers, and the public? Where might looking decisive or reassuring an audience matter more than operational results? What alliances and reputations would each proposal strengthen or threaten? And is there a third approach that wins greater support while letting the important players save face?

## Response

# Short answer

You can't know which VP is right from the arguments alone. But you can find out in a few weeks, and that finding, not either proposal, is your strongest political move. My prior leans toward Services as the *root* cause and Product as the *stated* cause, for reasons below. Treat that as a hypothesis to test, not a conclusion.

## Part 1: Finding out who's right

**Why the two beliefs are hard to separate:** Customers who never fully implemented also never used your existing analytics. When they leave, they'll honestly say "the competitor has better analytics." Exit interviews systematically overstate product gaps because "missing features" is an easy, blame-free reason to give a vendor.

**Diagnostics that separate them:**

1. **Churn by implementation outcome.** Split churned and retained accounts by whether implementation finished, how long it took, and whether they reached defined value milestones (e.g., % of claims processed in the system, active adjusters, analytics modules used). If churn concentrates in accounts that never got live or stayed shallow, it's primarily an adoption problem.
2. **Where they went.** Did churned customers move to a competitor with better AI and analytics, to a different mid-tier vendor, or back to in-house or legacy systems? Going to a feature leader supports Product. Going to anything simpler, or to nothing, supports Services.
3. **Fully adopted accounts.** Are deeply adopted customers also leaving? If healthy, well-implemented accounts churn for competitor features, Product's case gets much stronger.
4. **Timing.** Churn doubled over 18 months. Because contracts renew annually or longer, today's churn reflects decisions made 1–3 years ago. What changed then? A sales push that brought in less-ready customers, implementation headcount that didn't scale, a key competitor launch, a support reorg? The timeline often identifies the cause.
5. **Lost deals and at-risk renewals.** Ask Sales and your CSMs which competitor features actually come up in live evaluations, not what's assumed.

**Likely result:** For regional carriers, with constrained IT, legacy core systems, and heavy regulatory and data-mapping work, implementation pain is a very plausible driver. You'll probably find both are true in different segments: some accounts left because they never got to value, and a smaller set of mature accounts left for real capability gaps. That split matters, because it determines sequencing.

## Part 2: How each proposal plays politically

### Product-led ("accelerate the AI and analytics roadmap")

- **Board:** Plays well. It's a growth story, AI is what boards want to hear, and it looks decisive and forward-looking. It's easy to fund with a narrative.
- **Customers and market:** New AI announcements help at renewal and in analyst conversations. They reassure prospects and some current customers.
- **Employees:** Engineering and Product feel prioritized. Services and support staff may read it as leadership ignoring what they see daily.
- **Who gains:** The VP of Product gets budget, headcount, and the spotlight. Sales benefits, since "we lost on features" is a comfortable explanation.
- **Who risks blame:** If churn doesn't drop in 2–4 quarters, Product owns a costly miss. There's a worse hidden risk: if adoption is the real problem, more features increase implementation complexity and could make churn worse.
- **Where optics beat results:** This is the proposal where looking decisive can matter most. It's great for a board meeting and weak if the diagnosis is wrong.

### Services-led ("fix onboarding and support first")

- **Board:** Harder sell. It implicitly admits an operational failure and sounds defensive ("we'll fix our execution") rather than offensive. It is, however, typically cheaper and faster to show results.
- **Customers:** Existing customers feel it directly, and it's the most credible message to at-risk accounts. It does little for the public or the market narrative.
- **Employees:** Frontline staff feel heard. Engineering may feel deprioritized.
- **Who gains:** If it works, the VP of Services is vindicated.
- **Who risks blame:** Also the VP of Services, since the proposal concedes that their function has been underperforming. That's a real face-saving problem for them. It also brushes against you: if implementations have been failing, the question "why didn't CS escalate this sooner?" is coming.
- **Where results beat optics:** This proposal probably moves churn faster, but it's less rewarded in the short term.

### Your position

You own the churn number, so you absorb blame regardless of which diagnosis is adopted, unless you're the one who produces the diagnosis. Right now you're a referee between two VPs. The strongest move is to become the person with the answer.

## Part 3: A third approach that wins support and saves face

**Reframe the problem as "time-to-value," co-owned by both VPs.**

1. **You run a short, rigorous churn diagnostic (4–6 weeks)** using the analysis above. This positions you as neutral and data-driven, and it delays a costly bet without looking indecisive, because you're committing to a date for a decision.
2. **Present the findings as "both of you were right about different parts of the base."** This is likely true, and it lets both VPs save face. Services was right about why most accounts fail. Product was right about what mature accounts need.
3. **Recommend a sequenced joint plan:**
   - *Immediate:* A rescue program for at-risk accounts that are mid-implementation or shallowly adopted. This is Services-led, with you coordinating.
   - *Product investment aimed at adoption friction:* AI and automation that shortens implementation and time-to-value, such as automated data mapping, configuration templates, out-of-the-box analytics dashboards, and AI-assisted claims triage that works on day one. This gives Product its AI story, gives the board a growth narrative, and directly supports the Services fix instead of competing with it.
   - *Targeted feature work:* Build for specific capability gaps that show up in losses among well-adopted accounts.
4. **Shared metrics:** Time-to-first-value, implementation completion rate, and net revenue retention, jointly owned by Product, Services, and CS. Shared metrics turn a turf fight into an alliance.

**The board narrative:** "We found the root cause, we're fixing it fast, and we're investing in AI where it accelerates customer value." That sounds both decisive and grounded.

**Alliances:** Both VPs get credit and neither is publicly wrong. Sales gets a better story for prospects. You move from owner of a bad number to owner of the recovery plan.

## One caution

Optimize for the proposal that actually reduces churn, not just the one that wins the meeting. Churn reappears every quarter, so an optics win on a wrong diagnosis becomes a visible failure within a year, and the person who owns the number (you) inherits it. If the diagnostic shows one VP is clearly right, say so, using the face-saving framing, but don't blur the finding to keep the peace. Your lasting reputational gain comes from being the one who called it correctly.

## Summary (sent to Jev)

The response argues that neither VP can be proven right from argument alone, but the question can be answered within weeks, and producing that answer is the customer success leader's strongest move. Its prior leans toward Services as the root cause and Product as the stated cause, offered as a hypothesis to test. Customers who never fully implemented also never used the existing analytics, so exit interviews overstate product gaps, which are an easy, blame-free reason to give.

It proposes diagnostics:
- Split churn by implementation completion, duration, and value milestones.
- Check whether departing customers went to feature leaders or to simpler, legacy, or in-house options.
- Check whether fully adopted accounts are also leaving.
- Trace what changed one to three years ago, since annual renewals lag decisions.
- Ask Sales and CSMs which competitor features actually come up in live evaluations.

For regional carriers, implementation pain is plausible, and the likely finding is that both beliefs hold in different segments.

Politically, the Product plan plays well with boards but risks a costly miss and could worsen churn by adding complexity. The Services plan is a harder sell and concedes failure, including a question about why CS didn't escalate sooner, but it probably moves churn faster.

The recommended third approach reframes the problem as time-to-value, co-owned by both VPs. The CS leader runs a four-to-six-week diagnostic and presents the findings as both VPs being right about different parts of the base. The sequenced plan that follows has three parts:
- A Services-led rescue of at-risk accounts.
- AI investment that reduces adoption friction.
- Targeted features for gaps among well-adopted accounts.

These are backed by shared metrics. The caution is to optimize for actually reducing churn rather than winning the meeting, and not to blur a clear finding just to keep the peace.
