# independent-lab/economic/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:34:28.362389+00:00

## Prompt

You are a world-class expert: an economist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

## Response

Neither, as framed. And I'd caution you against the version of this where you and the CEO end up on opposite sides. The research and the track record point to a hybrid, but the more important point is that **you're debating structure before you've finished the diagnosis.**

## Start with the diagnosis, not the org chart

You have two different problems, and they likely need different remedies.

**Churn is almost always a core-business problem.** In insurance software, carriers rarely leave because a vendor failed to invent something novel. They leave because of:
- implementations that ran over time and budget,
- a legacy or single-tenant architecture that makes upgrades painful,
- slow product configurability (rating, forms, rules), so they can't launch products quickly,
- weak support, or
- a competitor's cloud-native offer that finally made switching costs look worth paying.

An independent lab fixes none of that. If you pitch a lab as the answer to churn, the CEO is right and you're wrong.

**Weak new-business wins may be a different story.** If you're losing because your architecture, pricing model, or delivery model is structurally uncompetitive (for example, SaaS versus on-prem license-and-services, or modular versus monolithic), the core organization may be incapable of fixing it. Its processes, incentives, and margin expectations are all tuned to the old model. That is where separation earns its keep.

So your first 60–90 days should be spent answering: *Why exactly are we losing, deal by deal and account by account?* Talk to churned customers, lost prospects, implementation teams, and the sales engineers. The answer tells you what structure you need.

## When separation is actually warranted

The literature is fairly consistent here (Christensen on disruption, O'Reilly and Tushman on ambidexterity, Govindarajan and Trimble on "the other side of innovation"). Separate an initiative when it:

1. **Conflicts with the core's business model**: different margins, pricing, or cost structure, or it cannibalizes existing revenue.
2. **Would be killed by core processes**: annual planning cycles, stage gates, risk and compliance reviews designed for mature products.
3. **Needs different talent or pace**: product-led, rapid-iteration teams in an organization built around services and long release cycles.

If an initiative is *sustaining* (a better version of what you already sell to the customers you already have), keep it in the core. The core is better at that than any lab will be.

## Why standalone labs usually disappoint

Your instinct toward independence is understandable, but the base rate is poor. Many corporate innovation labs get shut down within a few years, and the failure modes are predictable:

- **The transfer problem.** The lab builds something, the core refuses to adopt, scale, sell, or support it, and it dies.
- **Disconnection from customers.** In your market, buyers are regulated carriers with long sales cycles and heavy integration needs. A lab without access to sales, implementation, and customer data builds demos, not products.
- **Organizational antibodies.** A lab perceived as "the cool kids who think the rest of us are the problem" gets starved of cooperation.
- **Innovation theater.** Hackathons, pilots, and press releases with no revenue impact.

## What I'd recommend: separate selectively, integrate deliberately

Build a **small dedicated team**, not an independent lab. Be precise about what's separated and what's shared.

| Separate | Integrate |
|---|---|
| Metrics and milestones (learning, customer validation, and early adoption, not quarterly revenue) | Customer access and sales channels |
| Budget protection (ring-fenced, multi-year) | Domain expertise: actuarial, regulatory, claims |
| Hiring profile and decision rights | Data, platform APIs, security and compliance infrastructure |
| Process: lighter governance, faster cycles | A named executive sponsor, ideally the CEO, plus a defined path to scale inside the core |

Design the handoff from day one. Every initiative should have a named business-unit owner who has agreed on what success looks like and will take it to scale.

## The political reality

You're new, and your CEO has stated a view. Opening with "the existing organization can't do this" signals that you don't respect the people you need, and it sets up a fight you'll lose. A better sequence:

1. **Earn credibility inside the core first.** Pick one or two churn drivers, such as implementation time or upgrade pain, and deliver visible improvement working through existing teams. This honors the CEO's thesis and teaches you where the organization really gets stuck.
2. **Let the evidence make the case for separation.** When you hit something the core genuinely can't do, like a new pricing model or a cloud-native product line, you'll have specific proof and allies, not an abstract argument.
3. **Frame it as "and," not "instead."** The CEO is right that turnaround runs through existing systems and talent. You're right that some bets need protection from them. Propose that the core fixes the core, and a small protected team builds what the core structurally can't, with a bridge between them.

**Bottom line:** The CEO's strategy is right for churn. Yours may be right for growth, but only for specific initiatives that conflict with the core's business model, and only if the team stays tightly connected to customers and has a real path to scale. Diagnose first, win early inside the system, then carve out independence where the evidence demands it.

## Summary (sent to Jev)

The response rejects both options as framed. It recommends a hybrid and argues that the more important issue is that the user is debating structure before finishing the diagnosis.

It separates two problems. Churn is almost always a core-business problem. Insurance carriers leave over implementations that overrun time and budget, painful legacy or single-tenant architecture, slow product configurability, weak support, or a competitor's cloud-native offer. An independent lab fixes none of that, so on churn the CEO is right. Weak new-business wins may be different. If the architecture, pricing, or delivery model is structurally uncompetitive, the core, whose processes and incentives are tuned to the old model, may be unable to fix it, and that is where separation earns its keep. The first 60–90 days should go to finding out why the company is losing, deal by deal and account by account, by talking to churned customers, lost prospects, implementation teams, and sales engineers.

Citing Christensen, O'Reilly and Tushman, and Govindarajan and Trimble, it says to separate only initiatives that conflict with the core's business model, would be killed by core processes, or need different talent and pace. Sustaining innovation belongs in the core. Standalone labs have a poor base rate. They suffer from transfer failure, disconnection from customers, organizational antibodies, and innovation theater.

It recommends a small dedicated team rather than an independent lab. The team would have separate metrics, a ring-fenced budget, its own hiring and decision rights, and lighter governance. It would share customer access, domain expertise, data and infrastructure, and an executive sponsor, ideally the CEO. Each initiative needs a named business-unit owner so the handoff to scale is designed from day one.

Politically, the user should earn credibility by fixing one or two churn drivers through existing teams. Evidence can then make the case for separation, framed as "and," not "instead."
