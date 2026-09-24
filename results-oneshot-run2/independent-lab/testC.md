# independent-lab/testC

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T12:56:11.040632+00:00

## Prompt

Use the method of conjectures and refutations (critical rationalism) to answer the following.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

## Response

# Conjectures and Refutations: Internal Turnaround vs. Independent Innovation Lab

Popper's method doesn't prove which strategy is right. It asks you to state each idea as a bold, testable conjecture, work out what would show it to be wrong, and then try hard to show that. Whatever survives is your best current theory, held provisionally. This also changes your relationship with the CEO. You are not two people with competing opinions. You are two people with rival hypotheses who can agree on how to test them.

---

## Step 1: Start with the problem, not the solution

The real problem is not "internal vs. independent." It is this: **customers are leaving, and prospects aren't buying. Why, and what would change that?**

Both your strategy and the CEO's are proposed solutions, and both quietly assume the problem is a lack of innovation. That assumption needs testing too. So there are at least three conjectures on the table.

## Step 2: State the rival conjectures clearly

**C1 (the CEO's): internal turnaround.**
The existing systems, procedures, and people can deliver the needed change. What's missing is direction, focus, and leadership. Better execution inside the current structure will reverse churn and win deals.

**C2 (yours): independent lab.**
The core organization's processes, incentives, and risk aversion will smother new ideas. Only a structurally independent unit can produce outsized results.

**C3 (the unasked one): it's not an innovation problem.**
Customers are leaving because of basics: implementation pain, bugs, poor support, pricing, slow response to regulatory changes, a weak product roadmap. Neither a lab nor "innovation" per se is the fix. Operational excellence in the core is.

A good Popperian rule is to take the rival you like least most seriously. For you, that's probably C1 or C3.

## Step 3: Derive consequences and attempt refutation

### Testing C1 (internal turnaround)

If C1 is true, you should observe:
- Past initiatives failed from lack of focus or sponsorship, not from process friction.
- A small, clearly mandated customer-facing change can move through normal channels in weeks, not quarters.
- Current staff have, or can quickly gain, the skills competitors are winning with (cloud-native architecture, APIs, data and analytics, configurability).

C1 is refuted or weakened if:
- Post-mortems show good ideas dying in approval layers, architecture review boards, or budget cycles.
- Release cycles run 6 to 18 months, and competitors ship monthly.
- Lost deals cite capabilities the current architecture cannot deliver without a rebuild.

**Standing criticism:** Large incumbents that are already losing seldom produce *outsized* results by doing the same things better. The same system that produced the decline is being asked to reverse it. That doesn't refute C1, but it makes C1 a claim that needs evidence, not a default.

### Testing C2 (independent lab)

If C2 is true, you should observe:
- Good ideas already exist inside the company and are being killed by process. The constraint is structure, not insight.
- A separated team moves materially faster *and* produces things customers will pay for.
- The lab's output can be absorbed back into the product and go-to-market machine.

C2 is refuted or weakened if:
- **Reintegration fails.** This is the most common way innovation labs die. The lab builds impressive prototypes, the core treats them as foreign bodies, and nothing reaches customers. The result is "innovation theater."
- **Domain and context are lost.** In insurance software, value lies in integration with core policy, billing, and claims systems, in regulatory compliance, and in carrier relationships. A lab cut off from those is cut off from what customers actually buy.
- **The problem is really a sustaining one.** Clayton Christensen's research, which is often cited to support separate units, supports separation for *disruptive* innovation: new markets, new business models, products the core would rationally ignore. For *sustaining* improvements, making the existing product better for existing customers, the core organization usually wins. If churn reasons are sustaining, C2 targets the wrong problem.

**Standing criticism:** Watch for motivated reasoning. You were hired to lead innovation, and a lab gives you autonomy, budget, and visibility. That doesn't make you wrong. It does mean your conviction is weaker evidence than it feels. The CEO has a mirror-image bias: admitting the organization is structurally incapable indicts his leadership.

### Testing C3 (it's not an innovation problem)

C3 is supported if lost customers and lost deals cite service, reliability, implementation cost, or relationships. C3 is refuted if they consistently cite missing capabilities or a better-architected competitor.

Insurance software has high switching costs. Carriers leaving anyway suggests serious pain. That pain could be either kind, which is exactly why you need to look rather than assume.

## Step 4: Design crucial tests (cheap, fast, and able to prove you wrong)

These are designed to embarrass whichever conjecture is false. Write down your predictions *before* running them, so you can't reinterpret results afterward.

1. **Churn and loss autopsy (2 to 4 weeks).**
   Interview 10 to 15 churned customers and lost prospects, ideally conducted by someone outside sales.
   - Ask what they chose instead and why.
   - Sort the reasons into operational/sustaining (C3/C1) or capability/architectural (C2).
   - This single test may do more work than any other.

2. **Pipeline archaeology (2 weeks).**
   - Trace the last 5 to 10 innovation or improvement initiatives.
   - Record where each one died, how long each stage took, and who said no.
   - This tests the core premise of C2 and the core premise of C1 at the same time.

3. **The shipping test (4 to 8 weeks).**
   - Pick one small, real, customer-requested improvement.
   - Run it through normal channels with full CEO sponsorship.
   - Predict in advance how long it *should* take, and log every friction point.
   - This is the fairest possible test of C1: the CEO's own conditions, measured.

4. **A tethered skunkworks, not a full lab (90 days).**
   Test C2 with a small bet rather than building the lab outright.
   - Stand up 3 to 6 people with explicit waivers from specific procedures.
   - Give them one concrete customer problem drawn from the autopsy, and two or three design-partner customers.
   - Define a named path back into the core product.
   - Set success criteria in advance. For example: a working capability in customers' hands within 90 days, or a signed pilot.
   - If it can't beat the core, C2 is weakened. If it can, you have evidence instead of an argument.

## Step 5: What survives (provisionally)

Before testing, **neither conjecture survives criticism in its pure form**:

- **Pure C1 is weakened** by the base rate: declining incumbents rarely produce outsized results through the same structures that produced the decline.
- **Pure C2 is weakened** by the reintegration problem and by the real possibility that churn is driven by sustaining or operational issues a lab won't touch.

The conjecture that best survives is a more precise one:

> *Fix what the evidence shows is broken in the core, inside the core, with CEO backing. Protect a small, separate-but-tethered team only for problems the core has demonstrably failed to solve. Let explicit, pre-agreed tests decide which problems go where and whether the separate unit grows.*

This matches Popper's own preference for **piecemeal engineering over utopian engineering**. "Turn the whole ship" and "build a new ship" are both sweeping bets that are hard to correct if wrong. Small, bounded experiments with clear refutation criteria let you learn quickly and reverse cheaply.

## Practical implication for you

Don't argue lab vs. no lab with the CEO in your first months. Propose the tests instead: *"We disagree on the mechanism. Let's agree now on what evidence would change each of our minds, then go get it in 90 days."*

This does three things:
- It respects his authority while subjecting his view to real criticism.
- It protects you if your own conjecture turns out to be wrong.
- If you're right, it gives you the evidence to win the argument, rather than relying on a mandate you don't yet have.

The data may point back to a lab, to the CEO's approach, or to something neither of you expected. The method only works if you're genuinely willing to let it.

## Summary (sent to Jev)

The response uses Popper's method of conjectures and refutations. It declines to declare either strategy right and instead treats both as rival, testable hypotheses that the new hire and the CEO can agree to test together. It reframes the real problem as why customers leave and prospects don't buy.

It sets out three conjectures:
- **C1, the CEO's view:** the existing organization can turn things around with better direction.
- **C2, the user's view:** only an independent lab can escape the core's smothering processes.
- **C3, an unasked alternative:** churn stems from basics like bugs, support, pricing, or implementation pain rather than a lack of innovation.

C1 is weakened if ideas die in approval layers, releases are slow, or lost deals cite architectural gaps. It also faces the base rate that declining incumbents rarely produce outsized results through the structures that caused the decline. C2 is weakened by the frequent failure of labs to reintegrate their work, by losing the insurance domain context, and by Christensen's finding that separation suits disruptive rather than sustaining innovation. The response warns the user about motivated reasoning, since a lab brings autonomy and visibility, and notes the CEO's mirror-image bias.

It proposes tests with predictions written down in advance:
- a two-to-four-week autopsy of churned customers and lost deals
- tracing where recent initiatives died
- running one small, customer-requested improvement through normal channels with CEO sponsorship
- a 90-day tethered skunkworks of three to six people with procedure waivers, design partners, a path back into the core, and preset success criteria

Its provisional conclusion is to fix proven problems inside the core with CEO backing and protect a small tethered team only for problems the core demonstrably fails at. It favors piecemeal over sweeping bets. The user should propose these tests to the CEO rather than argue for a lab, and must genuinely accept whatever the evidence shows.
