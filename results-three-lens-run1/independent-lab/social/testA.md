# social/independent-lab/testA

Model: claude-opus-5-5 · 2026-09-24T14:54:16.454866+00:00

## Turn 1

**User:** I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

Neither pure version is likely to work. The good news is that you and the CEO are probably closer than it seems, and the way you resolve this will matter as much as which structure you pick.

## The case against each extreme

**"Work within existing systems" alone** tends to fail because large organizations are built to optimize what they already do. Budgeting, sales incentives, release cycles, and risk controls all reward predictable improvements to the current product. New ideas get starved or reshaped until they look like the old thing. If the company's problem is that the market has shifted (cloud-native competitors, insurtechs, AI-driven underwriting and claims), incremental improvement won't close the gap.

**An independent lab alone** has a poor track record, especially in enterprise software. Common failure modes:
- It becomes "innovation theater": demos and prototypes that never ship.
- The core organization resents it or ignores it ("not invented here").
- It can't access what makes the company valuable: customer relationships, domain expertise, data, distribution.
- It gets cut in the first budget squeeze because it has no revenue and no internal allies.

## The part you may be missing

You're **churning existing customers**. That usually signals a problem with the current value proposition: product gaps, reliability, implementation pain, service, pricing. An innovation lab won't fix that, and it can distract from it. If customers are leaving because onboarding takes 18 months or the platform is hard to configure, the "outsized result" might be fixing the core, not inventing something new.

So before choosing a structure, find out:
- **Why are customers leaving?** Talk to churned customers directly, not just through sales.
- **Why are you losing deals?** Look at win/loss data. Who are you losing to, and on what?
- **Is this an execution problem or a market shift?** Execution problems are solved inside. Market shifts need something protected from the core.

## What usually works: separate but connected

Research on "organizational ambidexterity" (O'Reilly and Tushman) and practical experience point to a hybrid:

1. **A small, protected team** with its own processes, speed, and success metrics. It is insulated from quarterly revenue pressure and legacy release cycles.
2. **Tightly linked to the core**: it reports to the CEO (not buried under IT or product), has access to customers and domain experts, and has a clear path for handing off what works.
3. **Two portfolios.** One set of bets targets the churn problem in the core product (fast, visible wins). The other explores new models or products (longer-term).
4. **Borrow talent from inside.** Rotating strong internal people through the team builds allies and brings knowledge back to the core.
5. **Kill criteria and stage gates**, so the effort is disciplined rather than a sandbox.

## How to handle the CEO

Don't frame this as "you're wrong, we need independence." You're new, and that framing makes it a contest. Try something like:

> "I agree we have to win with our existing people and assets. That's our advantage. To move fast enough, I'd like a small team with some protection from normal processes, pointed first at our biggest churn drivers. If it works, we scale what we learn across the organization."

That respects his view, gives you the structure you need, and ties innovation to the problem he cares about most: stopping the bleeding.

## Practical first 90 days

- **Weeks 1–4:** Customer and churn interviews, win/loss analysis, and conversations with frontline staff, who usually know exactly what's broken.
- **Weeks 4–8:** Pick 1–2 high-visibility problems tied to retention or deal wins. Assemble a small cross-functional team.
- **Weeks 8–12:** Ship something real to customers, even if it's small. Credibility earned early buys you the autonomy for bigger bets later.

If you can share more, such as why customers say they're leaving, who's beating you, and how much budget and authority you have, I can help you decide where the balance should sit.

## Turn 2

**User:** How many people should be on that small protected team, and which roles should I start with?

**Assistant:**

## Size: start with 5–7 people

That's small enough to move fast and avoid coordination overhead, but big enough to ship real software to real customers. Resist pressure to go bigger early. A 15-person lab gets noticed, scrutinized, and budgeted like a department before it has results. You can add people once you've earned it.

## Core roles (full-time)

**1. Product lead (1)**
Owns the problem, talks to customers constantly, and makes prioritization calls. This may be you at first, but if you're also managing up to the CEO and building internal alliances, you'll want someone dedicated. Look for someone who is comfortable with ambiguity and good at killing ideas.

**2. Engineers (2–3)**
- At least one **senior engineer who knows the existing platform** deeply, ideally an internal hire. They know where the bodies are buried, what integrations are possible, and how to get things into production. Without this person, your prototypes will never connect to the core.
- One or two **strong full-stack builders** who can move fast. Hiring one from outside can bring fresh practices and tools.

**3. Designer / user researcher (1)**
In enterprise insurance software, usability and workflow pain are often the hidden churn drivers. This person runs customer interviews, maps workflows, and makes sure you solve the real problem. If you can only afford one, pick someone who can both research and design.

**4. Insurance domain expert (1)**
Someone who has worked as an underwriter, claims adjuster, or operations lead at a carrier, or who has spent years implementing your product. They keep the team from building things that look clever but don't fit how insurers actually work, and they give you credibility with customers.

## Part-time links to the core (not on your headcount)

These people keep you connected and prevent the "isolated lab" failure:

- **Customer success liaison**: brings churn signals and gets you access to at-risk accounts.
- **Sales engineer or solutions consultant**: knows why deals are being lost and can put early work in front of prospects.
- **Platform/infrastructure contact**: helps with deployment, security, and compliance approvals so you don't get stuck in review.
- **Executive sponsor**: ideally the CEO, meeting with you regularly to clear roadblocks.

Ask for a few hours a week from each, formally agreed with their managers.

## Add later, based on what you learn

- **Data/ML engineer**, if your bets involve AI in underwriting, claims, fraud, or pricing. Don't hire this role speculatively.
- **Additional engineers**, once you have a validated direction worth scaling.
- **Go-to-market or partnerships lead**, if you move toward a new product or business model.

## Hiring sequence

1. **Senior internal engineer and domain expert first.** They give you credibility and knowledge immediately, and they signal that this is built *with* the organization, not against it.
2. **Designer/researcher next**, so customer discovery starts within weeks.
3. **Remaining engineers** as your first problem comes into focus.

## Internal vs. external mix

Aim for roughly **60% internal, 40% external**. Internal people bring context, relationships, and buy-in. External people bring new methods and less attachment to "how we've always done it." When picking internal people, choose respected high performers, not those who are available. Managers will try to give you people they can spare. Push back, and use the CEO's backing if necessary. Who you get tells the organization how seriously this effort is being taken.

## Roles to avoid early

- Dedicated managers or a "head of" layer
- Strategy or innovation consultants who don't build
- Project managers (the product lead and team can self-organize at this size)

If you tell me your likely first problem area, such as onboarding pain, a specific product gap, or an AI opportunity, I can adjust the role mix to fit.

## Turn 3

**User:** How do I convince managers to give up their best people for this team when they'll probably want to keep them?

**Assistant:**

Managers resist for rational reasons: losing a top performer puts their own goals at risk, and they get little in return. Your job is to change that math, not just win the argument.

## Understand what they're afraid of

Before asking, figure out what each manager stands to lose:
- **Missed commitments**: "If my best engineer leaves, the Q3 release slips and I'm blamed."
- **Permanent loss**: "They'll never come back."
- **No credit**: "My team develops the talent, and someone else gets the glory."
- **Status**: giving up headcount can look like weakness.

Address these directly, and most resistance softens.

## Make it a good deal for them

**1. Offer a backfill.** This is the single most powerful lever. Negotiate budget with the CEO so every manager who gives up a person gets approval to hire a replacement or bring in a contractor. It turns "losing someone" into "gaining headcount."

**2. Time-box the assignment.** Frame it as a 6–12 month rotation with a guaranteed return path, not a permanent transfer. People who come back bring new skills and connections, which benefits the manager.

**3. Solve their problems.** Point the team at issues that matter to them. If the head of claims products is losing customers over a workflow pain point, pick that as an early target. Now lending you a person is an investment in their own success.

**4. Share credit visibly.** Commit to crediting their team in updates to the CEO and leadership. Make "developed talent for the innovation team" something that counts in their performance review. You'll need the CEO to back this.

**5. Start part-time if needed.** If a manager won't release someone fully, ask for 50% for two months. Once the person is engaged and the work is visible, converting to full-time is much easier.

## Talk to the people, too

Top performers often want these opportunities. They're drawn to new challenges, visibility, and escaping bureaucracy. Once you've spoken to the manager first (never go around them), talk to the candidate. A strong person who asks to join is hard for a manager to refuse.

Don't recruit behind a manager's back, though. It's the fastest way to make enemies in your first months.

## How to make the ask

Be specific and prepared. Ask for a named person, not "someone good." Something like:

> "I'm building a small team focused on [the churn problem]. The CEO has made it a priority, and I think [name] would be ideal because of [specific reason]. I know losing them hurts, so here's what I can offer: a backfill for their role, a 9-month rotation with a guaranteed return, and our first project will tackle [problem that affects your area]. What would make this workable for you?"

That last question matters. It invites them to negotiate rather than just refuse, and you'll learn what they actually need.

## Use the CEO carefully

You need the CEO's support, but it works best as a backstop, not your opening move.

- **Up front:** ask the CEO to announce the team publicly, explain why it matters, and state that leaders are expected to contribute strong people. This sets the norm without targeting anyone.
- **In negotiation:** lead with the deal, not the mandate.
- **As a last resort:** if a manager blocks a critical person with no good reason, escalate. Do this sparingly. Each forced transfer spends political capital and creates someone who may want you to fail.

## Watch for the "B-player handoff"

Some managers will agree readily and offer someone mediocre. Politely hold your ground: "I appreciate that. For this role I really need someone with [specific skill], which is why I asked about [name]." If you accept weaker people to avoid conflict, the team underdelivers and the whole effort loses credibility.

## Build momentum

Your first one or two recruits matter most. Once a respected manager contributes a strong person and gets visible credit, others follow. Early wins also help: when the team ships something that helps customers, being part of it becomes something managers want for their people.

If you tell me which managers or functions you expect the most resistance from, I can help you tailor the pitch for each.

## Turn 4

**User:** What if the CEO won't approve budget for backfills? How do I make the case without that?

**Assistant:**

Backfills are the easiest lever, but they aren't the only one. What managers really fear is failing their commitments with fewer people. If you can't add money, you can reduce the commitments, lower the cost of the ask, or increase what managers get back. First, though, it's worth one more serious attempt at the budget.

## Make a stronger case for backfill budget

The CEO may have heard "backfills" as extra overhead. Reframe it as a return on investment tied to the problem he already cares about:

- **Quantify churn.** "We lost $X in annual recurring revenue last year. If this team keeps even two mid-sized customers, it pays for five backfills several times over."
- **Keep the ask small.** Four or five backfills, possibly contractors, is a rounding error in a large company's budget. Make that comparison explicit.
- **Stage it.** Ask for backfills for the first two or three hires only, with the rest contingent on early results. A small, reversible bet is easier to approve.
- **Offer to self-fund.** If you have any budget of your own, use part of it for backfills. It shows you're sharing the risk.

If the answer is still no, ask why. Is it a hiring freeze, cost pressure from the board, or skepticism about the team itself? Each needs a different response, and the last one is a warning sign.

## If there's truly no money: trade commitments instead

This is the most important alternative. Ask the CEO to **formally reduce what's expected** of managers who contribute people:

> "If you can't fund backfills, I need you to explicitly tell [manager] that it's acceptable for [project] to slip a quarter, or to drop [lower-priority item], so they can release [name]."

This costs nothing, but it requires the CEO to make real priority trade-offs. It also protects managers from being blamed later, which is often what they care about most. Get it in writing, or at least stated in a leadership meeting.

## Lower the cost of each ask

- **Part-time first.** 30–50% of someone's time for a defined period is much easier to give.
- **Shorter rotations.** Three to six months instead of a year, with specific end dates.
- **Stagger requests.** Don't pull top people from the same team at once, and spread the load across departments.
- **Look for teams with slack.** Some groups are between major releases or have lighter roadmaps. Timing your asks to their cycles helps.
- **Target high performers who are ready to grow.** A strong senior person may be ready for a stretch assignment, and their manager may see it as a chance to promote someone junior into their role. That's a free backfill in effect.

## Increase what managers get back

Without money, the value you offer has to come from elsewhere:

- **Work on their problems.** Make the team's first project something that directly reduces churn or pain in their area. This is your strongest non-financial offer.
- **Give credit publicly and specifically.** Name the managers and teams who contributed in updates to the CEO and leadership.
- **Performance recognition.** Ask the CEO to make "developed talent for strategic priorities" count explicitly in leaders' reviews.
- **Return better people.** Promise that people come back with new skills, customer insight, and exposure to leadership, and make sure that happens.
- **Early access.** Contributing teams get first look at what the team builds and a say in its direction.

## Change your team composition

- **Use any budget you control for external hires**, so you need fewer internal transfers. Keep internal asks for roles where context truly matters, like the senior platform engineer and the domain expert.
- **Lean on part-time connections** such as customer success, sales engineering, and platform contacts, as described earlier.
- **Start with three or four people instead of six.** A smaller team that ships something real is better than a full team you can't staff.

## Read what "no" is telling you

If the CEO won't fund backfills *and* won't reduce anyone's commitments, that's important information. It may mean this effort is less of a priority than the mandate to "produce outsized results" suggested. Treat this as a moment to align expectations directly:

> "I can deliver results with the team I can staff, but without backfills or priority trade-offs, we'll start smaller and move more slowly. Here's what I think is realistic in six months."

That protects you from being judged against expectations the organization isn't resourcing, and it often prompts the CEO to find the money after all.

Would it help to draft the business case for the CEO? If you can share rough numbers on churn, deal losses, or average contract value, I can help you build it.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's my recommendation, based on what you've told me.

## The short answer

**Don't build a lab yet. Start by diagnosing churn, then launch a small, CEO-sponsored team aimed at your biggest retention problem, and let results earn you the independence you want.**

You're right that innovation needs protection from the core. The CEO is right that the company's assets are its people, customers, and domain knowledge. The way to reconcile the two is to prove the model on the problem the CEO cares about most: customers leaving.

## The plan

**Month 1: Find out why customers are leaving**
- Personally interview 10–15 churned or at-risk customers and 5–10 lost prospects.
- Talk to frontline staff in support, implementation, and sales engineering.
- Come back with a clear, evidence-based answer: is this an execution problem (fix the core) or a market shift (build something new)?

This protects you from building the wrong thing, and it gives you facts the CEO can't easily dismiss.

**Month 2: Secure the mandate and the team**
- Present findings to the CEO along with a proposal: a team of 4–6 people, reporting to him, aimed at the top one or two churn drivers.
- Ask for backfills, framed against the revenue lost to churn. If he says no, ask for explicit priority trade-offs instead.
- Recruit your senior internal engineer and domain expert first, using the "good deal for managers" approach.

**Months 3–6: Ship something real**
- Put a working improvement in front of at-risk customers within about 90 days of the team forming.
- Measure what matters: retention, customer satisfaction on the targeted workflow, and deals won or saved.
- Credit contributing managers publicly.

**Month 6: Decide what's next**
- If you've shown results, make the case for more autonomy, a larger team, and a second portfolio of longer-term bets (new products, AI, new business models).
- If the diagnosis showed the core product is the problem, your team may evolve into a model for how the whole product organization works, which could be a bigger win than a lab.

## Why this approach

- **It ties innovation to survival.** A lab working on future ideas while customers leave will lose its funding. A team that saves accounts won't.
- **It builds allies instead of rivals.** You're new, and your influence depends on relationships you haven't built yet.
- **It's low-risk for the CEO to approve.** A small, measurable bet is easy to say yes to.
- **It keeps your options open.** You can still build a more independent unit later, with evidence and support behind you.

## What would change my advice

- **If your diagnosis shows the market has fundamentally shifted**, for example competitors winning with a completely different architecture or business model, then the case for a more independent unit gets much stronger, and you should make it sooner.
- **If the CEO won't provide people, money, or priority trade-offs**, have a frank conversation about whether the mandate is real before investing too much of yourself.

## Your next step this week

Book the first five customer conversations. Everything else, from the team design to the budget case to the CEO pitch, gets easier once you know why customers are leaving.

If it would help, I can draft an interview guide for those conversations or an outline for your Month 2 proposal to the CEO.

## Outcome summary (sent to Jev)

The recommendation is to hold off on an independent innovation lab. First diagnose why customers are leaving. Then launch a small, CEO-sponsored team aimed at the biggest retention problem, and let results earn more independence. This reconciles two valid views: innovation needs protection from the core, but the company's real assets are its people, customers, and domain knowledge.

The plan runs in phases:

- **Month 1:** Personally interview 10–15 churned or at-risk customers and 5–10 lost prospects, and talk with frontline support, implementation, and sales engineering staff. The goal is to determine whether churn is an execution problem, which means fixing the core, or a market shift, which means building something new.
- **Month 2:** Present the findings with a proposal for a 4–6 person team reporting to the CEO and focused on the top one or two churn drivers. Request backfills justified by revenue lost to churn, or failing that, explicit priority trade-offs. Recruit a senior internal engineer and a domain expert first, making the deal attractive to their managers.
- **Months 3–6:** Ship a working improvement to at-risk customers within about 90 days. Measure retention, satisfaction with the targeted workflow, and deals won or saved, and credit contributing managers publicly.
- **Month 6:** With results in hand, seek more autonomy, a larger team, and a second portfolio of longer-term bets. Alternatively, the team could become a model for the whole product organization.

The rationale is that tying innovation to survival protects funding, builds allies rather than rivals for a newcomer, is a low-risk bet for the CEO to approve, and keeps options open.

Two caveats apply. If the diagnosis reveals a fundamental market shift, the case for a more independent unit strengthens and should be made sooner. If the CEO provides no people, money, or trade-offs, question whether the mandate is real. The immediate step is booking five customer conversations this week.
