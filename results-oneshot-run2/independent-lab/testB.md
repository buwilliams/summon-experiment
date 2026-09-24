# independent-lab/testB

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T12:55:29.170262+00:00

## Prompt

You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

## Response

# Short answer: neither, as stated

Both positions have well-documented failure modes. The research and my experience point to a third option. Before structure, though, there's a more important question.

## First: is this actually an innovation problem?

Churn and lost deals in enterprise insurance software usually come from:

- **Core product gaps**: slow configurability, painful upgrades, weak APIs, aging UX
- **Delivery failures**: implementations that run 18 months over and blow budgets
- **Service and relationship decay**: customers feel ignored or nickel-and-dimed
- **Competitive repositioning**: Guidewire, Duck Creek, and cloud-native insurtechs have reset buyer expectations around SaaS, speed-to-market, and data/AI

If churn is driven mainly by the first three, an innovation lab won't fix it. You'd be building a speedboat while the ship takes on water, and the CEO would be right to resist. If it's driven by the fourth, the existing organization probably *can't* fix it alone, and you'd be right.

**So your first 30–60 days should be diagnostic, not structural.** Talk to churned customers, lost prospects, and sales engineers. Read loss reports. Sit in on implementations. Let the evidence tell you which problem you have. It will probably be a mix.

## Why "work within the existing system" often fails

When the innovation needed is genuinely different (new business model, new architecture, new buyer), the core organization tends to kill it. The reasons are structural, not personal:

- Resource allocation favors the current revenue base and your biggest, most conservative customers.
- Metrics like quarterly bookings and utilization punish exploratory work.
- Processes built for reliability (release gates, architecture review, compliance) are lethal to rapid experimentation.
- Your best people get pulled back into firefighting every time a key account escalates.

This is the core of Christensen's work, and it's real. The CEO's view works for **sustaining innovation**, which may be most of what's needed right now. It works poorly for anything that threatens the current model.

## Why "independent innovation lab" often fails

This is the part advocates underestimate. Most corporate innovation labs are quietly shut down within a few years. Common reasons:

- **No path to scale.** The lab builds something interesting, but it can't be sold, implemented, or supported by the core business. In insurance software this is acute. Carriers buy integration with policy admin, billing, claims, and regulatory reporting, not standalone novelty.
- **Organizational antibodies.** Core teams resent the "cool kids" with a budget and no quota. When the lab needs their help, they don't give it.
- **Pilot purgatory.** Endless proofs of concept, few production deployments, no revenue.
- **Sponsor dependence.** When the sponsoring executive's attention shifts or budgets tighten, the lab is the first cut.
- **Loss of customer contact.** Separated teams drift toward what's technically interesting rather than what carriers will pay for.

There's a specific risk for you too. Your first major move would contradict the CEO who hired you. You'd be staking your credibility on a structure that fails more often than it succeeds, against his stated belief, before you've earned trust.

## What the evidence supports: separate but tightly linked

O'Reilly and Tushman's research on "ambidextrous organizations" found that the structure that succeeds is neither fully integrated nor fully independent. The winning pattern:

- **Separate teams** for exploratory work, with their own processes, metrics, and culture
- **Tight integration at the senior level**: a single executive owns both, and leadership shares a strategic intent
- **Deliberate linkages** to borrow core assets such as customers, data, sales channels, domain experts, and platform

In their study, this model hit its innovation goals far more often than either fully integrated or fully spun-out approaches. Govindarajan and Trimble reach a similar conclusion in *The Other Side of Innovation*. You need a "dedicated team" *and* a formal partnership with the "performance engine," with the tension between them managed explicitly rather than wished away.

## What I'd actually recommend

**1. Split the work into two horizons, with different structures.**

| | Fix the core (CEO's instinct) | Build the future (your instinct) |
|---|---|---|
| Goal | Stop churn, win competitive deals | Create differentiated new offerings |
| Examples | Faster implementation, better APIs, upgrade path, UX, embedded AI in existing workflows | New data/AI products, SaaS-native modules, new buyer segments, ecosystem plays |
| Structure | Embedded teams in existing orgs, with executive air cover and removed blockers | Small dedicated team, own processes and metrics, protected budget |
| Metrics | Retention, win rate, time-to-value | Validated learning, design-partner commitments, then revenue |

**2. Make the dedicated team small and tethered.**

- Aim for 8–20 people, not a 100-person lab with a fancy office.
- Staff it with some respected insiders who know the domain and have internal credibility, not only outside hires.
- Require co-development with 2–4 real carrier design partners from day one.
- Build on the core platform's data and integration layer wherever possible. Scale is the hardest part, so design for it at the start.
- Define up front how successful projects transfer to or get absorbed by the core, including who funds them in year two.

**3. Get early wins on the core problem.** Churn is the burning platform. If you visibly help reduce it in your first two or three quarters, you earn the credibility and budget to protect the exploratory work. If you ignore it to build a lab, you'll be seen as disconnected from what matters.

**4. Put governance above both horizons.** The dedicated team should report to you, and you should report to the CEO. Review exploratory work with different criteria than the core, such as kill/continue decisions based on evidence, not quarterly revenue.

## How to frame it with the CEO

Don't position this as "you're wrong, we need independence." Position it as **"you're right, and here's how we protect what the core system can't do on its own."**

Something like:

> "Most of our turnaround has to come from the existing organization. That's where the customers, revenue, and expertise are, and I'm going to spend most of my energy helping it move faster on churn and competitive wins. But a few bets will need different rules to survive: different speed, metrics, and risk tolerance. I'd like a small, tightly connected team for those, explicitly designed to feed back into the core. We'll judge it on evidence and kill what doesn't work."

That's hard to argue with, it respects his position, and it gets you the structural protection you need.

## The scientist's view

Treat your structural belief as a hypothesis, not a conclusion. You've been there a short time. Gather data on why customers leave and deals are lost, run a small, well-designed experiment with the dedicated-team model, and let results earn the right to scale. If the lab is the right answer, the evidence will make that case for you, far more persuasively than an argument in your first quarter.

## Summary (sent to Jev)

The response argues that neither the CEO's approach nor the independent lab is right as stated, and it recommends a third option. It first asks whether the problem is really about innovation. Churn in enterprise insurance software often comes from core product gaps, delivery failures, or service decay, which a lab won't fix. It can also come from competitive repositioning by Guidewire, Duck Creek, and cloud-native insurtechs, which the existing organization probably can't fix alone. The first 30–60 days should therefore be diagnostic: talk to churned customers, lost prospects, and sales engineers, read loss reports, and sit in on implementations.

Working within the existing system tends to kill genuinely different innovation, because resources, metrics, processes, and firefighting all favor the current business. It does suit sustaining innovation. Independent labs also usually fail. The causes include having no path to scale (acute in insurance, where carriers buy integration), organizational resentment, pilot purgatory, dependence on a sponsor, and lost customer contact. Opening by contradicting the CEO also risks the new hire's credibility.

Drawing on O'Reilly and Tushman's ambidextrous organizations and on Govindarajan and Trimble, the response recommends separate but tightly linked structures under one executive:

- **Two horizons.** Embedded teams fix the core, measured on retention and win rate. A dedicated team builds the future, measured on validated learning and then revenue.
- **Small, tethered team.** Keep it at 8–20 people, include respected insiders, work with 2–4 carrier design partners, build on the core platform, and plan the handoff and year-two funding in advance.
- **Early wins on churn.** These earn credibility.
- **Separate governance.** Review exploratory work with evidence-based kill/continue criteria.

With the CEO, the proposal should be framed as supporting his view while protecting a few bets. The new hire's belief should be treated as a hypothesis to test with data and a small experiment.
