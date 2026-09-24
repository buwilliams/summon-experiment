# economic/independent-lab/testB

Model: claude-opus-5-5 · 2026-09-24T14:49:02.012959+00:00

## Turn 1

**User:** You are a world-class expert: an economist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

**Short answer: Neither of you is fully right, and treating this as a binary is the first trap.** The right structure depends on *why* you're losing, and you probably don't know that yet. Here's how I'd think about it.

## 1. Churn in insurance software is a distress signal about the core

Policy admin, billing, and claims systems have some of the highest switching costs in enterprise software. Migrations take years, cost millions, and carry regulatory risk. When carriers leave anyway, something has usually been broken for a long time: slow or failed implementations, a painful cloud/SaaS transition, poor configurability, weak support, or a roadmap customers stopped believing in.

Churn is a lagging indicator. The damage was done three to five years ago.

That matters because **an innovation lab won't fix churn.** A lab produces new things on a two-to-four-year horizon. Your customers are leaving over the product they have today. If you pour your energy into a lab while the installed base keeps eroding, you'll have a promising prototype and a shrinking company.

## 2. But the CEO's framing has a contradiction in it

"Outsized results" from "existing systems, procedures, and talent" is internally inconsistent. Those systems and procedures produced the current outcomes. Organizations get exactly the results their incentives, budgeting processes, and decision rights are designed to produce. If you change nothing structural, you'll get incremental results at best.

So the CEO is right that the core must be fixed from within. He's wrong if he believes it can be fixed without changing how the core operates.

## 3. The independent lab has well-documented failure modes

Fully separate corporate labs fail far more often than they succeed. The usual reasons:

- **The organization rejects the transplant.** The core sees the lab as a threat or an insult ("the cool kids who get to ignore the rules") and quietly declines to adopt anything it produces.
- **No path to market.** The lab builds demos. Scaling requires sales, implementation, support, and compliance, all of which sit in the core.
- **Funding gets cut.** Labs funded out of the core P&L get cut in the first bad quarter. You're in a company that's already having bad quarters.
- **It discards your only real advantages.** Against a well-funded insurtech startup, your edge is the installed base, carrier relationships, data, regulatory expertise, and domain talent. A fully independent lab gives all of that up and competes as a startup without startup incentives.

## 4. What the evidence supports: ambidexterity, not independence

The research (O'Reilly and Tushman on ambidextrous organizations, Govindarajan and Trimble's *The Other Side of Innovation*) points to a hybrid:

- **A dedicated team** with its own leadership, metrics, pace, and hiring profile, protected from core processes that would smother it.
- **Deliberate linkage to the core** for distribution, customer access, domain experts, and infrastructure.
- **Integration at the top.** A senior sponsor, ideally the CEO, resolves conflicts between the two. This is the piece that makes it work or not.

Separate where the work is genuinely different. Connect where the core's assets create advantage.

## 5. What I'd do in your first 90 days

1. **Diagnose before you design.** Personally talk to churned customers, at-risk customers, and lost deals. Run a rigorous win/loss analysis. Find out whether you're losing on product gaps, implementation failure, pricing and total cost, architecture, or trust. This determines everything else.
2. **Split the problem into horizons.**
   - *Core repair* (churn): usually sustaining innovation such as faster implementations, modernized architecture, better configurability, and embedded AI in underwriting and claims. Do this inside the organization, but negotiate specific exceptions to procedure: a fast-track team, different release gates, direct customer access.
   - *Adjacent and new* (win rate and future growth): new segments such as MGAs, mid-market, or embedded insurance, or new business models. This is where a separate unit earns its keep.
3. **Get an early win in the core.** You're new, and your credibility is zero until you deliver something. Fixing a visible churn driver buys you the political capital to build anything more radical.
4. **Negotiate the terms before you launch anything separate:** multi-year protected funding, a direct reporting line to the CEO, different success metrics (learning milestones and customer validation, not quarterly revenue), and a pre-agreed handoff path into the core.

## 6. How to handle the CEO

Don't open with "your approach won't work; we need a separate lab." That puts you in opposition to the person who hired you, in your first months, on his stated belief. You'll lose that fight even if you're right.

Instead, frame it as **"fix the core fast, and build what's next alongside it."** Agree with him on the core, where he's largely right. Then introduce the separate unit as a complement, backed by what customers told you, and specifically scoped to the opportunities the core structurally can't pursue.

The goal isn't to win the argument about structure. It's to match the structure to the problem, and right now you need data on what the problem actually is.

If you can share what you've learned so far about why customers are leaving and why deals are being lost, I can help you get more specific about where the line between "inside" and "separate" should fall.

## Turn 2

**User:** How do I get churned customers to actually talk to me honestly, especially if the account teams are nervous about me reaching out to them?

**Assistant:**

You're dealing with two separate problems. One is internal: account teams who fear what you'll find. The other is external: customers with little reason to spend time on a vendor they've already left. Solve the internal one first, because it determines how you're perceived in the building for the next two years.

## Part 1: Getting the account teams on side

**Understand why they're nervous.** It's rarely about protecting the customer relationship. They're worried about:
- **Blame.** Churn post-mortems in most companies turn into "who lost the account?"
- **Exposure.** Customers may say things about the account team that were never reported upward.
- **Compensation and pipeline.** Some churned customers are still mid-migration and paying, or there's a slim hope of a partial win-back. They don't want you disrupting that.
- **Disputes.** Some exits involve billing disputes, SLA claims, or lawyers.

**Address each directly:**

1. **Declare amnesty, and have the CEO or CRO say it too.** State plainly that this is about systemic causes (product, implementation, pricing, architecture), not individual performance, and that findings will be reported in aggregate, never attributed to an account team. Then keep that promise without exception. The first time a finding gets used against a rep, your access is gone.
2. **Interview the account teams first.** Ask them why they think each customer left. This gives you their hypothesis to test, signals respect, and often surfaces candid internal views like "we oversold the implementation timeline" that they'll never put in a CRM note.
3. **Give them a choice in how contact happens.** They can make the introduction themselves, or you can use a neutral third party. What they can't do is opt out. Most will choose to introduce, because it lets them keep control.
4. **Screen for landmines with legal and finance.** Exclude or delay accounts in active litigation, formal disputes, or sensitive contract wind-downs. This is prudent, and it shows the account teams you're not reckless.
5. **Share the synthesis with them before leadership sees it.** No surprises. Better still, invite a couple of respected account leads to help interpret the findings. People support what they help create.

**Use sponsorship, but don't lead with it.** You want the CEO's backing visible ("this is a company priority"). If you use it as a club to go around people, you'll get compliance and quiet sabotage.

## Part 2: Getting churned customers to talk

**Who reaches out matters most.** Your options, roughly from most to least candid:

- **A third-party win/loss firm.** Specialists such as Clozd or Primary Intelligence, or an independent consultant, get the most honest answers because the customer isn't sparing anyone's feelings. It's also the most politically safe option with account teams. The downside is cost and losing some texture.
- **You, as a new executive with no history.** This is an underrated asset. You didn't make the promises that were broken. "I'm new, I've been asked to figure out what we got wrong, and I'd value your unvarnished view" works well precisely because you're not defending the past.
- **The account team or anyone tied to the relationship.** This is the least candid option. Customers soften feedback to people they know.

I'd use a mix: a third party for breadth and your own interviews for depth, especially with senior contacts. Hearing it firsthand changes how you'll argue for it internally.

**Make the ask easy to accept:**
- Keep it short: 30 to 45 minutes.
- Promise explicitly: no selling, no win-back pitch, and their comments won't be attributed to them internally. Then honor it.
- Pitch it as influence rather than a favor. Many churned customers still run other vendors' products, sit on industry forums, and care about how the market evolves. Some are frustrated they had to go through a painful migration and genuinely want to be heard.
- Reach beyond the main buyer. In insurance software, the real story often sits with the implementation lead, the head of claims or underwriting operations, IT architecture, or the CFO who saw the cost overruns. The decision-maker gives you the official reason; the people underneath give you the real one.
- Check gift and compliance policies before offering incentives. Many carriers restrict gifts from vendors. A charitable donation in their name is usually the safe option, and often unnecessary anyway.

## Part 3: Running the conversation for honesty

**Reconstruct the timeline instead of asking for opinions.** "Why did you leave?" gets you a tidy, rationalized answer. Instead:
- "Take me back to when you first started thinking about replacing us. What was going on?"
- "What was the moment it became a real project rather than grumbling?"
- "Who pushed for it internally, and who resisted?"
- "What did the alternatives show you that we didn't?"
- "At what point, if any, could we have changed your decision? What would it have taken?"
- "What did we do well that you'll miss?" This one is surprisingly useful. It tells you what not to break.

**Don't defend, explain, or correct.** Every time you say "well, actually, we fixed that in release X," they'll stop being candid. Take notes and say "tell me more." If there's something to clarify, do it at the very end, or not at all.

**Listen for the gap between the stated reason and the real one.** "Price" often means "the value didn't justify it" or "the implementation cost doubled." "Wanted cloud-native" often means "we lost faith in your roadmap." Probe the first answer at least twice.

**Record with permission** so you can quote verbatim, anonymized. Direct customer language in front of executives is far more persuasive than your summary of it.

## Part 4: Make it count

- **Include at-risk current customers and lost deals, not just churned accounts.** Churned customers tell you what already broke. At-risk customers tell you what's breaking now, which is where you can still act. Lost prospects tell you why you're not winning new business.
- **Triangulate with internal data**: support tickets, implementation durations against plan, escalations, product usage, discounting history. Interviews tell you why; data tells you how widespread it is.
- **Aim for patterns, not anecdotes.** Around 15 to 25 interviews across churned, at-risk, and lost deals usually shows clear themes. Code them systematically.
- **Close the loop with the customers.** A few months later, tell them what you changed because of what they said. It builds credibility, and in a market this relationship-driven, it occasionally reopens a door you thought was closed.

One last point: how you run this exercise becomes your reputation in the company. If people see it was fair, confidential, and used to fix systems rather than blame individuals, you'll have allies for everything that follows. If it looks like a witch hunt, you'll spend your tenure fighting the organization you're trying to change.

## Turn 3

**User:** What should I say to the CEO to get him to publicly back this, without it sounding like I'm already questioning his turnaround plan?

**Assistant:**

The key is to frame this as **ammunition for his turnaround, not an audit of it.** His plan is to fix the business from within. That plan needs a precise target, and customer evidence provides it. You're not questioning whether to fix the core; you're helping decide *what to fix first.*

## The framing principles

1. **Position it as sharpening, not validating.** Don't say "let's test whether the plan is right." Say "let's make sure we aim the plan at the highest-impact problems."
2. **Make him the owner.** It should feel like his initiative that you're running, not your side project he's being asked to bless.
3. **Ask for his hypotheses up front.** "What do you think is driving churn?" makes him invested in the answer instead of threatened by it, and it gives you his mental model.
4. **Promise him the first look.** Tell him he'll see the findings before anyone else. This is real value to a CEO: no surprises in front of his board or team, and time to shape the narrative. It also covers you if findings cut against his assumptions.
5. **Watch your vocabulary.** Avoid "root cause," "post-mortem," "audit," "what went wrong." Use "customer insight," "turnaround priorities," "where to focus," "voice of the customer."

## Before you meet with him

Brief the CRO or head of sales first, privately. If the CEO backs this and then hears objections from sales, he may waver. If sales is already on board, or at least not opposed, the CEO hears a united front. Show the CRO the amnesty principle and the plan for account team involvement. Ideally, ask them to co-sponsor.

## A sample script for the one-on-one

> "I've spent my first few weeks getting oriented, and I'm aligned with your view that the fastest path is fixing the core business. What I want to make sure of is that we aim our effort at the problems that move churn and win rates the most, because we can't fix everything at once.
>
> I'd like to run a focused customer listening effort over the next eight weeks: conversations with customers we've lost, customers who are at risk, and deals we didn't win. The goal is a clear, ranked list of what's driving these decisions, so we put resources where they'll have the biggest impact.
>
> Before I start, I'd like to hear your read. What do you think is driving churn? I want to make sure we test the things you think matter most.
>
> Two things would make this work. First, I'd like you to see the findings before anyone else, so there are no surprises. Second, I need a short message from you telling the organization this is a priority and that it's about finding systemic fixes, not blaming individuals. Without that, account teams will understandably be cautious, and we won't get the honest picture we need."

Then stop talking and let him respond.

## Anticipate his objections

- **"We already know why customers leave."** "You may be right, and if so, this confirms it quickly and gives us customer evidence to rally the organization and the board around. If there's anything we've missed, better to find it now than after we've committed the budget."
- **"This will upset the sales team."** "I've already talked with [CRO], and we've designed it around aggregate findings and no individual blame. Account teams will be involved from the start."
- **"We don't have time for a study."** "It's eight weeks, and it runs in parallel with everything else. It's designed to make the next twelve months of investment more effective, not delay them."
- **"I don't want to reopen wounds with customers."** "We'll exclude any account in a dispute, and the conversations are strictly listening, with no selling. In my experience, many former customers appreciate being asked, and it can leave the door open for the future."

## What to ask him for specifically

Make the public commitment small, concrete, and easy to say yes to:

1. **A short internal message** from him, drafted by you. Offer the draft so it's effortless.
2. **One sentence at his next leadership or all-hands meeting** reinforcing it.
3. **A date on his calendar** for the findings readout, which signals follow-through.

## A draft message you can hand him

> "As we work to strengthen our business, I've asked [your name] to lead a focused effort to hear directly from our customers, including those we've lost and deals we haven't won. The goal is simple: make sure we're focusing our turnaround on the issues that matter most to customers.
>
> This is about identifying systemic improvements across product, delivery, and service, not about individual accounts or teams. Findings will be shared in aggregate. I'm asking everyone, especially our account teams, to support this work. I'll be personally reviewing the results, and they'll directly shape our priorities for the coming year."

## One caution

Don't promise him the findings will support his plan. You don't know that, and if the data points elsewhere, you'll be trapped. The "first look" commitment is your protection. If the findings challenge his assumptions, you walk him through it privately, framed as "here's where the customer evidence says to focus." That gives him the chance to adopt the conclusion as his own. That's usually how strategy actually shifts in a company: not by winning an argument, but by giving the leader a credible reason to update his view.

## Turn 4

**User:** What if the findings come back and show the core problem is something the CEO personally championed, like a failed cloud migration he pushed for?

**Assistant:**

This is the moment the whole exercise was building toward, and how you handle it will define your relationship with him. The core rule: **don't soften the substance, but be very deliberate about the delivery.** Burying the finding would be a mistake both ethically and practically. Customers know, the account teams will know, and eventually the board will know. The only open question is whether the CEO hears it from you, framed constructively, or from someone else, framed as a failure.

## 1. Be rigorous about what the finding actually says

Before you say a word, make sure you know precisely what's wrong. "The cloud migration failed" is rarely the accurate conclusion. Separate these:

- **The strategic direction.** Was moving to cloud the right call? In insurance software, almost certainly yes. The market moved, and staying on-premises would likely have caused worse churn.
- **The execution.** Timelines, product maturity at launch, feature parity gaps, migration cost to customers, stability, support readiness.
- **The customer experience of the transition.** Were customers forced onto it before it was ready? Was pricing restructured painfully? Were promises broken?
- **Communication.** Did customers lose faith because of the roadmap, or because no one told them the truth about it?

In most cases, the honest finding is "right direction, flawed execution or sequencing." That's not spin; it's usually accurate, and it's a very different message. If the evidence says the strategic decision itself was wrong, don't blur that. But be sure before you say it.

Also make sure the evidence is solid. Triangulate the interviews with implementation data, support tickets, and revenue impact. Have a trusted colleague, or the third-party firm if you used one, pressure-test your conclusions. You need to be unassailable on the facts because this will be emotionally charged.

## 2. Understand the psychology you're dealing with

There's a well-documented pattern called escalation of commitment. Leaders who personally championed a decision tend to double down when evidence turns against it, because admitting the problem feels like admitting personal failure. The sunk cost pulls hard, and the decision becomes part of their identity.

Your job is to make it psychologically safe for him to change course. That means separating his judgment from the outcome, focusing on decisions going forward, and giving him a way to lead the fix rather than be blamed for the problem.

## 3. Structure the private meeting

This is the "first look" you promised him. Do it one-on-one, with no audience and no slides that could be forwarded.

**Open with context, not the verdict.** Remind him of the purpose: identify where to focus.

**Let customers deliver the hard message.** Lead with patterns and anonymized verbatim quotes, not your interpretation. It's much harder to dismiss twenty customers than one new executive, and it keeps you in the role of messenger rather than critic.

**Name the strategic merit explicitly and honestly.** If the direction was right, say so clearly. This isn't flattery; it's accurate and it gives him the footing to hear the rest.

**Pivot quickly to forward decisions.** Don't dwell on what went wrong. Spend most of the meeting on what to do now.

A sample script:

> "I want to walk you through what we heard before anyone else sees it. The clearest theme, by a wide margin, is the cloud transition. I want to be precise about this: customers overwhelmingly don't question the move to cloud. Several said it was the right direction. What they're reacting to is how the transition played out: [specifics, e.g., feature gaps at launch, migration costs, stability issues, timelines slipping].
>
> Here's what they said in their own words. [Two or three quotes.]
>
> The good news is these are fixable problems, and fixing them is probably the single biggest lever we have on churn and win rates. I've got a few options for how we could approach it that I'd like your thoughts on."

## 4. Bring options, not just the problem

Arriving with only bad news invites defensiveness. Arriving with credible paths forward invites leadership. For example:

- **Stabilize and close the gaps:** a focused program on the specific parity and reliability issues customers cited, with visible milestones.
- **Fix the migration economics:** revised migration pricing, funded services, or incentives for at-risk customers.
- **Re-earn trust:** direct CEO outreach to key at-risk accounts, a credible and realistic roadmap, and a commitment to report progress.
- **Win-back:** a targeted effort toward recently churned customers once the fixes are real.

Let him shape and choose among these. The more the plan becomes his, the more committed he'll be to it.

## 5. Give him a way to lead the correction

The most powerful thing you can do is show him that owning this makes him stronger, not weaker. Leaders who say "we made the right strategic bet, we underestimated what customers needed during the transition, and here's how we're fixing it" usually gain credibility with boards, employees, and customers. Leaders who deny a problem everyone can see lose it.

You might say:

> "Honestly, I think this is a strong story if you get out in front of it. The strategy was right, we've listened hard to customers, and now we're fixing the execution. Customers and the board will respect that, and it gives the whole company something clear to rally around."

## 6. Protect yourself without being political

- Write up your findings accurately and keep the underlying evidence. Don't make the written version more critical than what you say in the room, and don't make it softer than the evidence supports.
- Report in terms of causes and customer impact, not blame. Don't say or write "the CEO's decision failed."
- Don't preview the findings to anyone else before he sees them. Breaking the "first look" promise is the fastest way to turn him against you.

## 7. If he rejects the findings

Give it a little time. First reactions to hard news are often defensive, and many leaders come around after a few days of reflection. Follow up with additional data, a smaller first step he can say yes to, or a proposal to pilot the fix with a handful of at-risk accounts.

If he persistently refuses to engage, you face a harder question. You were hired to produce outsized results, and you can't do that if the biggest driver of churn is off-limits. You'll have to decide whether you can be effective in this role. Don't go around him to the board or leak the findings. That would be a breach of the trust you established and would almost certainly end your tenure without fixing anything. The rare exception would be if something rose to the level of misrepresentation to the board or investors, and even then, that's a conversation for legal counsel, not a unilateral move.

In most cases, though, it doesn't come to that. CEOs usually know when a pet initiative is struggling. What they often lack is a credible, non-threatening path to acknowledge it and change course. If you give him that path, you're not questioning his leadership; you're making it possible for him to exercise it.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the integrated plan. The specifics will depend on what customers tell you, but the sequence and principles hold regardless.

## The strategy in one sentence

**Fix the core first to stop the bleeding, earn credibility doing it, and then build a connected (not independent) unit for the growth bets the core can't pursue.**

The CEO is right about where to start. You're right that the existing way of working won't produce outsized results. The plan sequences both.

## Phase 1: Listen and diagnose (weeks 1–10)

**Goal: a ranked, evidence-based list of what's driving churn and lost deals.**

- Align the CRO privately, then get the CEO's public backing using the framing we discussed: sharpening the turnaround, not auditing it.
- Interview account teams first, under explicit amnesty.
- Run 15–25 conversations across churned customers, at-risk customers, and lost deals. Use a third-party firm for breadth and do the senior conversations yourself.
- Triangulate with internal data: support tickets, implementation timelines against plan, discounting, usage, and revenue by segment.
- Give the CEO the first look, privately, with options attached.

**Deliverable:** the top three to five drivers, each sized by revenue impact, with recommended actions.

## Phase 2: Stop the bleeding (months 3–9)

**Goal: visibly reduce churn risk in the installed base.**

- **Name a single owner for each top driver** with a budget and a deadline. If the biggest issue is the cloud transition, that means a focused stabilization and parity program, not a general "improvement initiative."
- **Stand up a small fast-track team inside the core** with a few negotiated exceptions: shorter release cycles, direct customer access, and authority to cut through approvals. This is how you work "within the system" while still changing how it operates.
- **Launch an at-risk account program:** identify your top 20–30 accounts by revenue and churn risk, assign executive sponsors, and involve the CEO directly with the most important ones.
- **Get one quick, visible win** within 90 days of the readout, something customers and employees can see. Your credibility for everything that follows depends on this.

**Metrics:** gross revenue retention, at-risk accounts stabilized, implementation time against plan, and escalation volume. Report monthly to the CEO and leadership team.

## Phase 3: Build the growth engine (months 6–18)

**Goal: fix the win-rate problem and create new growth the core can't.**

Only once Phase 2 is showing results do you propose the separate unit, and design it as ambidextrous rather than independent:

- **Scope it tightly** to two or three bets that the findings and lost-deal analysis point to. In insurance software these often involve an underserved segment like MGAs or mid-market carriers, AI-native capabilities in underwriting or claims, or a lighter-weight product with a different business model.
- **Separate what should be separate:** leadership, hiring profile, pace, and success metrics (customer validation and learning milestones, not quarterly revenue).
- **Connect what should be connected:** access to customers, domain experts, data, and the sales channel.
- **Report directly to the CEO**, with multi-year protected funding agreed up front, and a defined path for scaling successes back into the core.

**Metrics:** win rate on competitive deals, pipeline in new segments, and validated customer pilots.

## What to protect throughout

- **The amnesty promise.** Never let findings be used against individuals.
- **The CEO's first look.** No surprises, ever.
- **Focus.** Three priorities done well will beat ten launched. Most turnarounds fail from dilution, not lack of ideas.
- **Customer language.** Keep putting customers' own words in front of leadership. It's the most persuasive tool you have.

## Decision points to plan for

- **After Phase 1:** if the evidence points to something the CEO championed, use the private, options-based approach we discussed.
- **At month 6:** if churn isn't improving, reassess before launching Phase 3. A growth unit on top of a collapsing base is a distraction.
- **At month 12:** decide whether the growth bets merit scaling, reshaping, or shutting down, using the metrics agreed at launch.

## What would sharpen this

To make this more specific, it would help to know:
1. Roughly how many customers you've lost and what share of revenue that represents.
2. Whether there's already a known suspect, like the cloud migration, or whether the cause is unclear.
3. Your budget and whether you have any team of your own yet.
4. How much time the CEO and board are giving the turnaround before they expect results.

With those, I can help you turn this into a 90-day plan you could put in front of the CEO.

## Outcome summary (sent to Jev)

The assistant recommends a sequenced plan: fix the core business first to stop churn and earn credibility, then build a connected, not independent, unit for growth bets the core cannot pursue. Its reasoning is that an innovation lab works on a multi-year horizon and cannot fix churn caused by today's product. Fully separate labs tend to be rejected by the core, lack a path to market, lose funding in bad quarters, and give up the company's real advantages: installed base, carrier relationships, data, and regulatory expertise. The CEO's belief that unchanged systems can produce outsized results is also inconsistent, so the core must change how it operates.

The first step is diagnosis over roughly ten weeks:
- Align the CRO, then secure the CEO's public backing, framed as sharpening his turnaround rather than auditing it.
- Interview account teams under explicit amnesty.
- Run 15 to 25 conversations with churned customers, at-risk customers, and lost deals, using a third-party firm plus personal senior interviews.
- Triangulate with internal data.
- Give the CEO a private first look with options attached.

Next comes stopping the bleeding: single owners for each top driver, a fast-track team with negotiated process exceptions, an at-risk account program involving the CEO, and one visible win within 90 days. Only after churn improves should a tightly scoped ambidextrous unit be proposed. It would have its own leadership, pace, and metrics, stay linked to customers and sales, report to the CEO, and receive protected multi-year funding.

The key caveats are these:
- Never let findings be used against individuals.
- Never surprise the CEO.
- Stay focused on a few priorities.
- If findings implicate something he championed, deliver them privately, separating strategy from execution.
- Reassess at month six if churn isn't improving.
