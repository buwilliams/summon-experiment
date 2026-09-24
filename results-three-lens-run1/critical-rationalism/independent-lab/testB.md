# critical-rationalism/independent-lab/testB

Model: claude-opus-5-5 · 2026-09-24T14:44:58.537797+00:00

## Turn 1

**User:** You are a world-class expert: a scientist by training who later spent two decades as a senior strategy advisor to executives at large enterprise software companies.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

# Probably neither, at least not yet

The honest answer is that you're both partly right, and the bigger risk is picking a structure before you've diagnosed the problem. Let me explain why, then offer a path.

## First, separate the two problems

You've described two problems, and they may need different solutions:

1. **Churning customers.** This is almost always a *core* problem. In insurance software, churn usually comes from painful upgrades, slow configuration, implementation overruns, weak APIs and integrations, a stalled cloud migration, or poor support. An innovation lab will not fix these. If anything, it pulls attention and talent away from them.
2. **Losing new business.** This *might* be a core problem, if you're losing on price, references, or delivery risk. Or it might be a positioning problem, if competitors like Guidewire, Duck Creek, Sapiens, or newer cloud-native entrants are offering something structurally different that your architecture or business model can't match.

If churn is your bleeding wound, the CEO's instinct to work within the existing organization is largely correct for that problem. Customers leaving today need the core to get better, not a lab demo in 18 months.

## Why each pure strategy tends to fail

**"Work entirely within existing systems"** fails when the innovation conflicts with the core's incentives, metrics, or business model. The core organization isn't stupid. It is optimized, and it will rationally kill or starve anything that threatens this quarter's numbers, cannibalizes existing licenses, or doesn't fit the release train. Christensen's work and decades of case evidence support this.

**"Independent lab"** fails more often than people admit. Common failure modes:
- **Innovation theater:** hackathons, prototypes, and a nice space, but nothing ships to customers.
- **Organizational antibodies:** the core resents the lab's freedom and budget and quietly refuses to adopt its output.
- **The handoff gap:** Xerox PARC is the classic case. Brilliant work, captured by others, because nothing connected it to the company's go-to-market.
- **Distribution blindness:** labs forget that the incumbent's real advantages are its customer relationships, regulatory knowledge, data, and sales channels. A fully independent lab gives those up and becomes a poorly funded startup.

## What the evidence supports: separate but linked

The research on "ambidextrous organizations" (O'Reilly and Tushman) and Govindarajan and Trimble's *The Other Side of Innovation* points to the same answer. You need a dedicated team with distinct processes and metrics, tightly linked to the core through senior leadership and deliberate interfaces.

Key design choices:

| Dimension | Recommendation |
|---|---|
| **Reporting** | Directly to the CEO, not buried under the CTO or a product line. Protection must come from the top. |
| **Metrics** | Learning milestones and customer validation early. Don't judge a new venture on core P&L metrics in year one. |
| **Shared assets** | Deliberately borrow the core's strengths: customer access, domain experts, sales channels, data. |
| **Talent** | Mix outside hires with respected insiders. An all-outsider lab gets rejected. |
| **Graduation path** | Decide upfront how a successful project transfers or scales, and who owns it. |
| **Kill criteria** | Define in advance what failure looks like, so you stop things quickly and keep credibility. |

## How I'd approach your first 90 days

**1. Diagnose before designing (weeks 1–6).** Talk to 10–15 churned customers and 10–15 lost deals directly, not through sales' interpretation. Talk to implementation partners, who know where the bodies are buried. You're looking for the real reasons. Is it product, delivery, price, architecture, or trust?

**2. Sort the findings into two buckets.**
- *Sustaining problems* that the core can fix with better focus, such as upgrade pain, configurability, or support. Push these into the existing organization with your backing and CEO sponsorship. This is where the CEO's view is right.
- *Structural problems* the core can't fix because they conflict with how it makes money or builds software. Examples might be a usage-based SaaS offering for smaller carriers, an embedded or insurtech-partner platform, or AI-native claims triage. These justify a protected team.

**3. Earn autonomy rather than demand it.** Don't open with "we need an independent lab." You're new, and the CEO has told you his thesis. Contradicting him on structure before you've delivered anything spends political capital you don't have yet. Instead:
- Deliver one or two visible wins in the core, ideally something that measurably reduces churn risk with a key account.
- Use your diagnosis to show *specifically* where the existing system blocks a needed opportunity.
- Propose a small, time-boxed, protected team aimed at one validated opportunity, with clear kill criteria.

The CEO doesn't have to concede he was wrong. You're both right about different parts of the problem.

## The bottom line

"Independent lab vs. work within the system" is the wrong framing. The better question is: **which problems require a different operating model, and which just need focus and leadership?** Fix the core where the core can be fixed, because that's likely where your churn lives. Build a separate but linked team only for the opportunities the core structurally cannot pursue, and connect it to the company's customers and distribution from day one.

If you share more about why customers are leaving and who you're losing deals to, I can help you pressure-test which bucket your biggest problems fall into.

## Turn 2

**User:** How do I get churned customers to actually agree to talk to me, and what should I ask them?

**Assistant:**

# Getting Churned Customers to Talk, and Asking Questions That Get the Truth

Churned customers are usually more willing to talk than people expect. Many left frustrated and never felt heard. The key is making it clear you want to learn, not win them back.

## Part 1: Getting the Meeting

### Before you reach out
- **Check with legal and finance.** Some churned accounts may be in active disputes, contract wind-downs, or data-migration negotiations. You don't want to walk into a legal minefield or accidentally make commitments.
- **Tell the account teams, but don't let them gatekeep.** Sales and account managers sometimes resist these calls because they fear what will surface. Inform them. Don't ask permission, and don't let them join the call.
- **Pull the history.** Know the contract size, tenure, implementation story, support tickets, and who signed. Showing up informed signals respect.

### Who should reach out
**You, directly, as a senior executive.** A survey or a customer success rep gets ignored. A personal note from a new senior leader with a clear mandate gets answered. Your newness is an asset here: you didn't cause their pain, so you can credibly say you're trying to understand it.

**Warm paths work even better:**
- The original sales rep or implementation lead, if the relationship ended well
- Implementation partners and system integrators, who often still work with the customer
- Your CEO or board members with industry relationships
- Former employees now working at carriers

### How to frame the ask
- **Be explicit that it's not a sales call.** Say it plainly, and then honor it.
- **Keep it short.** Ask for 30 minutes. You'll often get 60 once they start talking.
- **Explain why their view matters.** "You know things about our weaknesses that we can't see from inside."
- **Offer something back.** Offer to share what you learn in aggregate. Senior people value peer-level insight.

### Sample outreach

> Subject: A request, not a pitch
>
> Hi [Name],
>
> I recently joined [Company] to lead innovation, and I've been asked to take an honest look at where we've fallen short for customers. [Carrier] moved off our platform last year, and I suspect you have a clearer view of our weaknesses than anyone inside the building.
>
> Would you give me 30 minutes to hear your unvarnished perspective? This is not a win-back conversation. I won't pitch anything, and I won't bring sales. I'm trying to understand what really happened so we fix the right things.
>
> Happy to share what I learn across these conversations if that's useful to you.
>
> [Your name]

**Expect a 30–50% response rate with personal outreach from a senior leader.** Follow up once, a week later, and consider a warm introduction for anyone who doesn't reply.

### Who to talk to at each customer
The person who signed the termination is often not the person who knows why. Try for two or three perspectives per account:
- **Economic buyer** (CIO, COO, or line-of-business head): strategic reasons, cost, vendor confidence
- **Day-to-day owner** (claims, underwriting, or policy admin leader): usability, workflow pain, business impact
- **IT or architecture lead:** integration, upgrades, cloud, technical debt
- **Your original champion,** if they're still there: what changed, and when they stopped defending you

## Part 2: What to Ask

### The core principle: ask for the story, not the reason
If you ask "Why did you leave?", you'll get a tidy, socially acceptable answer: "price," "strategic direction," "consolidation." These are usually the last step in a long chain, not the root cause.

Instead, reconstruct the **timeline of the decision**. This approach comes from Jobs-to-be-Done "switch interviews" (Bob Moesta and Clayton Christensen's work). People remember events far more accurately than they recall their own reasoning.

### Interview structure (45–60 minutes)

**1. Opening (5 min)**
- Restate: no pitch, you want candor, nothing they say will be held against them.
- Ask to record, and to share quotes anonymously internally.

**2. The early relationship (5–10 min)**
- "Take me back to when you first selected us. What were you hoping we'd do for you?"
- "What did we get right early on?"

This builds rapport and shows you the original promise, which tells you where the gap opened.

**3. The first crack (10 min). This is where the gold usually is.**
- "When did you first start thinking this might not work long-term? What was happening at the time?"
- "Was there a specific moment or incident?"
- "Who inside your organization first raised it?"

**4. Building momentum toward leaving (10 min)**
- "What happened between that first doubt and the decision to look elsewhere?"
- "Did you raise concerns with us? What happened when you did?"
- "Was there a point where you stopped trying to make it work?"

**5. The search and the alternative (10 min)**
- "Which alternatives did you consider, including staying or building in-house?"
- "What did [new vendor] show you that we couldn't?"
- "What worried you about switching? What almost made you stay?"

That last question matters a lot. It shows you what you still had going for you and what might have tipped the decision.

**6. The counterfactual (5–10 min)**
- "If we'd done one thing differently, would you have stayed? What would it have been?"
- "At what point would that have had to happen?"
- "What would we have to be true for you to consider us again someday?"

**7. Close (5 min)**
- "What should I have asked that I didn't?"
- "Who else should I talk to, inside your organization or elsewhere?"
- Thank them, and confirm you'll share aggregate findings.

### Interviewing technique
- **Bring a note-taker.** You need to stay fully present.
- **Never defend or explain.** Even when they're factually wrong, their perception is the data. "That's helpful, tell me more" is your default response.
- **Chase specifics.** When they say "the upgrade was painful," ask "Painful how? How long did it take? What did it cost you? Who got blamed internally?"
- **Get comfortable with silence.** The most honest answer often comes after an uncomfortable pause.
- **Treat "price" as a symptom.** When price comes up, ask: "Price compared to what value? What would have made the price feel justified?" Price is rarely the whole story. It usually means value didn't keep pace with cost.
- **Listen for emotion.** Frustration, embarrassment, and betrayal point to what really mattered, especially career risk. A CIO whose upgrade project blew up in front of their board will remember that.

## Part 3: Turning Conversations Into Insight

**Sample size:** Aim for 12–20 churned accounts, or more if you serve distinct segments like large carriers vs. MGAs or P&C vs. life. Patterns usually emerge by conversation 8–10. Keep going until you stop hearing new things.

**Synthesis:**
- After each call, write down the **trigger event**, the **root cause**, the **stated reason**, and **what might have saved them**.
- Separate *what they said* from *what you think actually happened*.
- Look for clusters: product gaps, delivery failures, relationship breakdowns, architecture limits, business model mismatch.
- Map each cluster to the sustaining vs. structural buckets we discussed earlier.

**Close the loop:**
- Share a short, anonymized summary with the people you interviewed. This builds enormous goodwill, and occasionally reopens doors.
- Present findings internally with **direct quotes and recordings**. Executives can dismiss your interpretation. They struggle to dismiss a former customer's voice describing a bad upgrade weekend.

## One Strategic Note

This exercise does more than generate insight. It also builds your credibility with the CEO. You'll arrive at the structure conversation, lab or no lab, with evidence nobody else in the building has. That's how a new leader earns the standing to challenge a CEO's thesis.

Consider running a parallel set of **5–10 lost-deal interviews** with prospects who chose a competitor. Churn tells you why you're losing the customers you have. Lost deals tell you why you can't win new ones. Together they give you the full picture.

## Turn 3

**User:** What should I do if the account managers or sales leaders push back hard and try to stop me from contacting their churned customers?

**Assistant:**

# When Sales Pushes Back

This is one of the most predictable obstacles you'll face, and how you handle it will shape your reputation in the organization. The goal is not to win the fight. It's to get the conversations while turning sales leaders into allies, or at least neutral parties, rather than enemies.

## First, understand why they're resisting

Pushback almost always has a reason. Some reasons are legitimate and some are defensive, and you need to tell them apart.

**Legitimate concerns (take these seriously):**
- **Active win-back efforts.** They may be working on getting the customer back and fear you'll disrupt it.
- **Other live business.** The churned business unit may belong to a parent company that still buys other products from you.
- **Legal or contractual sensitivity.** There may be disputes, credits, or migration terms under negotiation.
- **Relationship risk.** They worry an executive from headquarters will reopen old wounds or make promises they'll have to deal with.

**Defensive concerns (usually unspoken):**
- **Fear of blame.** The interview might reveal overselling, missed commitments, or neglected accounts.
- **Compensation.** Churn may already have hurt their quota or bonus, and they don't want it revisited.
- **Turf.** Customer relationships are a salesperson's currency. You're entering their territory.
- **Distrust of the new executive.** They don't know you yet, and they've probably seen "innovation" initiatives come and go.

Most resistance is a mix. Your job is to fully address the legitimate concerns, which often takes the air out of the defensive ones.

## Step 1: Get your mandate before you need it

Ideally, do this before you contact a single customer. Ask the CEO to explicitly endorse the churn study and communicate it to the CRO or head of sales. Something as simple as this works:

> "I've asked [you] to lead a study of why we've lost customers. I'd like everyone's support. This is about fixing the company, not assigning blame."

This changes the conversation from "Can I do this?" to "How do we do this well together?" If you've already started without it, get it now, before resistance hardens.

## Step 2: Start with the sales leader, one-on-one

Meet the CRO or VP of Sales privately before you go near individual account managers. Their stance determines everyone else's.

**What to do in that meeting:**
- **Lead with the shared problem.** Churn hurts their numbers more than anyone's. You're trying to fix the product, delivery, and support failures that make their job harder.
- **Explicitly say it's not about blame.** "I'm looking for systemic causes: product, implementation, support, pricing. I'm not evaluating individual reps, and I won't attribute findings to anyone."
- **Ask for their input.** "Which accounts do you think would be most useful to talk to? What do you think the real reasons were?" Their hypotheses are valuable, and asking signals respect.
- **Offer them early access to the findings.** Promise to share results with them before anyone else sees them. That removes the fear of being ambushed in an executive meeting.

A sales leader who feels like a co-owner of the study will often clear the path for you.

## Step 3: Offer clear guardrails

Most legitimate concerns disappear once you commit to specific rules. Offer them proactively:

1. **No selling, no promises.** You won't pitch, discount, or commit to anything.
2. **Advance notice.** You'll tell the account owner before contacting any customer.
3. **Carve-outs.** You'll exclude accounts with active legal issues or win-back efforts, for a defined period such as 60–90 days, not indefinitely.
4. **Shared notes.** You'll share relevant insights from their accounts, especially anything that helps a win-back.
5. **Anonymized findings.** Internal reports will aggregate themes and won't name individual reps.
6. **An optional warm intro.** They can make the introduction if they want to, which lets them look proactive to the customer.

Put these in a short written document. It signals seriousness and gives them something to show their own teams.

## Step 4: Handle individual resistance

Even with the sales leader on board, some account managers will resist. A few approaches work well.

**For "I'm working on a win-back":**
> "Great. What's your timeline? I'll hold off on that account until [date]. If it doesn't come back by then, can we revisit? And if you'd like, I can share what I learn from other accounts. It might help your pitch."

**For "They're still angry, you'll make it worse":**
> "That's exactly why I want to talk to them. Angry customers often just want to be heard. I'll go in purely to listen, and I'll tell you how it went afterward. Would you prefer to make the introduction?"

**For "I already know why they left":**
> "That's really helpful. Tell me. I'd like to test your view against what I hear from the customer, and I'll show you both side by side."

This last one is important. Often the account manager's explanation and the customer's explanation differ, and that gap is itself a major insight.

## Step 5: Build momentum where resistance is low

You don't need every account. Start where there's no friction:
- Accounts whose original rep has left the company
- Account managers who are curious or supportive, since there are almost always a few
- Churned customers reachable through implementation partners, board members, or your own network

Once the first few interviews produce useful, non-threatening insights, share them with sales. Resistance usually softens when people see the study helps them rather than hurts them. Early wins turn skeptics into volunteers.

## Step 6: If resistance persists, escalate carefully

Sometimes a sales leader will keep blocking after you've addressed every legitimate concern. At that point:

- **Escalate once, clearly, and without drama.** Go to the CEO with specifics: "I've offered these guardrails, excluded these accounts, and offered to share findings first. [Name] is still blocking contact with [X] accounts. I need your help."
- **Frame it around the business, not personalities.** "We can't fix churn if we can't learn from churned customers."
- **Avoid making it a public win.** If the CEO overrules them, be gracious. You'll need these people later.

## What NOT to do

- **Don't go around sales secretly.** Contacting their customers behind their backs will destroy trust, and they will find out. Customers often mention it to their former rep.
- **Don't publicly attribute churn to specific reps,** even when the interviews point that way. Take individual performance issues privately to the right leader, if at all.
- **Don't let carve-outs become indefinite.** "Win-back in progress" can turn into a permanent excuse. Put dates on exclusions.
- **Don't treat all resistance as bad faith.** Some of it protects real relationships and real revenue.

## One more thing: resistance is data

Pay attention to *where* the pushback is fiercest. Extreme resistance around specific accounts often signals something worth understanding: overpromised capabilities, a botched implementation, a missed commitment, or an account that was neglected. You don't need to confront this directly. But if one region, team, or product line fights especially hard, that's a hypothesis to test gently later.

Handled well, this process builds your standing in the organization. Handled poorly, it creates enemies in the function that most directly controls revenue. Move patiently, address real concerns generously, and let early results do the persuading.

## Turn 4

**User:** How do I get the CEO to actually act on the findings if they point to problems he doesn't want to hear, like the core product or leadership being the issue?

**Assistant:**

# Getting the CEO to Act on Findings He Doesn't Want to Hear

This is the moment that decides whether your churn study changes the company or becomes a slide deck nobody opens again. Most people get the analysis right and then lose the room in the delivery. How you prepare the CEO matters as much as what you found.

One reframe before the tactics: your goal is not to be proven right. It's to help the CEO reach the right decision in a way he can own. People rarely act on conclusions forced on them. They act on conclusions they feel they arrived at themselves.

## Before the findings: set it up so the truth has somewhere to land

The best time to handle resistance is before the results exist.

### 1. Agree on decision criteria in advance
Early in the study, ask the CEO something like:

> "If we find that most churn traces back to the core product, what would we be prepared to do? And if it's mostly implementation or support?"

Pre-commitment is powerful. Once someone has said "if X, then we'd do Y" before knowing the answer, it's much harder to dismiss X when it appears. It also reveals early how open he really is.

### 2. Get him into the room with customers
This is the most effective tactic available to you. Invite the CEO to join two or three interviews, ideally with articulate, candid customers. He can simply listen.

A CEO can argue with your interpretation. It is very hard to argue with a former customer describing, in their own words, the weekend an upgrade took their claims system down. If he hears it firsthand, you're no longer the messenger. You're the person helping him act on what he already knows.

If he won't join live, share recordings or short clips with his permission.

### 3. Pressure-test your own conclusions
Be honest with yourself here. You came in believing the organization needed an independent lab. Findings that "the core is broken" conveniently support that view. Before you present, have a skeptical colleague try to poke holes in your conclusions:
- Did you talk to a representative set of accounts, or the angriest ones?
- Do support tickets, win/loss data, NPS, and implementation records back up what customers said?
- Are you mistaking symptoms for causes?

If your findings survive honest scrutiny, you'll present with more confidence. If they don't, you've avoided a credibility-destroying mistake.

## Presenting the findings

### 4. No surprises: preview privately first
Never let the CEO hear difficult findings for the first time in front of his executive team or the board. People defend themselves hardest in public. Walk him through it one-on-one first, give him time to absorb it, and let him shape how it's shared more broadly.

> "I want you to see this before anyone else. Some of it is hard. I'd rather we work through it together before deciding how to share it."

### 5. Lead with customers and money, not opinions
Structure the evidence so it's hard to wave away:
- **Quantify.** "Of the $X million in ARR we lost over two years, roughly 60% traces back to upgrade and configurability issues." Money gets attention in a way themes don't.
- **Use the customers' words.** Two or three powerful quotes beat twenty bullet points.
- **Show the pattern, not the anecdote.** "11 of 16 customers independently described this same problem."
- **Triangulate.** Show that internal data points the same direction.

Separate clearly what customers said from what you infer. It makes you more credible and gives him room to engage with the facts before debating the interpretation.

### 6. Frame everything in terms of his goals
He wants to turn the ship around. So frame the findings as the map for doing exactly that, not as an indictment of the past.

> "This tells us precisely where the ship is taking on water. That's good news, because now we know where to focus."

If the core product is the problem, you may even be aligned with his original thesis: fixing the core *is* working within the existing organization. Let him see that the findings extend his strategy rather than overturn it.

### 7. Bring options, not verdicts
Never present a hard problem without paths forward. Offer two or three options with tradeoffs, including at least one modest, reversible first step:

> "Here are three ways we could respond. The first is a 90-day focused effort on upgrade reliability with our five most at-risk accounts. We'd learn fast and it's low risk. The other two are bigger bets we could decide on once we see results."

Small first steps lower the psychological cost of acting. A CEO who won't commit to a product overhaul may readily approve a 90-day pilot, and results from the pilot will carry the bigger decision.

## When the problem is leadership

This is the most delicate situation, and it needs a different approach.

### If it's a specific executive
- **Describe decisions and consequences, not people.** "The decision to cut implementation staff in 2022 correlates with the spike in failed go-lives" lands very differently from "the COO broke delivery."
- **Take it to the CEO privately, and only the CEO.** Never put it in a group deck.
- **Stick to what customers experienced.** You're reporting evidence. Judging people's performance is his job.
- **Consider whether it needs to be said at all.** If fixing the systemic problem will fix the outcome, you may not need to name anyone.

### If it's the CEO himself
If customers point to decisions the CEO made, such as underinvesting in the product, a failed strategy, or broken promises from the top, handle it with great care:
- **Ask permission.** "Some findings touch on strategic decisions made before I arrived, including some of yours. Do you want me to be completely direct?" Almost every CEO says yes, and having said yes, he's more receptive.
- **Depersonalize through timing and context.** "Given what the market looked like in 2020, that decision made sense. Customer needs have shifted since." This lets him change course without admitting he was wrong.
- **Give him the forward narrative.** The best CEOs are remembered for how they responded, not for never making mistakes. "The story here is a leadership team that listened and changed course" is a story he'll want to be part of.

## If he still won't act

Sometimes, even with perfect preparation, a CEO digs in. You have several options, in rough order:

1. **Give it time.** Initial defensiveness often softens over days or weeks. Don't push for a decision in the first meeting. Revisit it after he's had time to think.
2. **Act within your own remit.** Launch small pilots you can authorize yourself. Results change minds more reliably than arguments.
3. **Build allies.** Find other executives, such as the CFO, CRO, or head of product, who see the same problems. A CEO who dismisses one voice may listen to three.
4. **Let reality keep speaking.** Keep tracking churn and lost deals against your findings. If your diagnosis is right, the evidence will keep accumulating, and you'll have documented it early.
5. **Be very careful with the board.** Going around the CEO to the board is a nuclear option. It's generally only appropriate for ethical, legal, or fiduciary issues, not strategic disagreements. For strategy, you can advise, but he decides.

## Know your own line

Finally, decide in advance what you will and won't do. You can soften *how* you deliver hard truths, but don't soften *what* they are. If you find yourself watering down findings to protect your position, you've stopped doing the job you were hired to do.

If, over a reasonable period, it becomes clear the CEO fundamentally won't confront the company's real problems, that's important information for your own career. You were hired to produce outsized results. That isn't possible in an organization that won't act on the truth, and it's better to recognize that early than to spend years as the innovation leader who never got to innovate.

Most CEOs, though, will act when the evidence is solid, the delivery is respectful, and there's a credible path forward they can own. Your job is to make acting on the truth the easiest thing for him to do.

## Turn 5

**User:** What should we do?

**Assistant:**

# What I'd Do in Your Position

I don't know yet what your customers will tell you, so I can't prescribe a fix for your specific problems. Anyone who does without that evidence is guessing. But I can tell you what I'd do, in what order, and how I'd decide once the evidence comes in.

## The short version

1. **Don't build the lab yet.** Earn the right to build it, and aim it at a specific opportunity the core can't pursue.
2. **Diagnose first.** Churn interviews, lost-deal interviews, and internal data, over 6–8 weeks.
3. **Stop the bleeding in the core.** Churn is almost certainly the most urgent problem, and it's probably fixable inside the existing organization, as the CEO believes.
4. **Deliver a visible win within 90 days.** Credibility is your scarcest resource right now.
5. **Then propose a small, protected venture team** aimed at whatever structural opportunity the evidence reveals, with CEO sponsorship and clear kill criteria.

## The sequence

### Days 1–30: Align and listen
- **Agree the mandate with the CEO.** Get his explicit endorsement of the churn and lost-deal study, plus pre-commitment on decision criteria ("If we find X, we'd do Y").
- **Meet the sales leader one-on-one.** Offer guardrails and early access to findings.
- **Start interviews.** Begin with low-friction accounts and invite the CEO to two or three.
- **Pull internal data.** Look at churn by segment, support tickets, implementation history, upgrade timelines, and win/loss records.
- **Map the organization.** Who has credibility? Who sees the problems clearly? Who will block?

### Days 30–60: Synthesize and preview
- **Finish 15–20 churn interviews and 5–10 lost-deal interviews.**
- **Quantify lost ARR by root cause.**
- **Pressure-test your conclusions** with a skeptical colleague, especially anything that conveniently supports your lab thesis.
- **Preview privately with the CEO** before anyone else sees the results.

### Days 60–90: Act on the core
- **Pick the one or two biggest churn drivers** the core can fix.
- **Launch a focused, time-boxed fix** with your most at-risk accounts, for example a 90-day upgrade reliability program with five key customers.
- **Report results transparently,** including what isn't working.

### Days 90–180: Earn and build the venture team
- **Identify the structural opportunities,** meaning the things the core can't do because of its architecture, business model, or incentives.
- **Propose a small, protected team** for one validated opportunity, reporting to the CEO, with its own metrics, links to the core's customers and channels, and defined kill criteria.

## How to decide once the evidence is in

In insurance software, churn and lost deals tend to trace back to a handful of patterns. Here's how I'd respond to each:

| If the evidence shows... | Then the right move is... | Lab? |
|---|---|---|
| **Painful upgrades, slow configuration, technical debt** | A core product investment program with CEO-level priority | No. Fix the core. |
| **Failed or overrun implementations** | Rebuild delivery methodology, partner strategy, and staffing | No. This is operations. |
| **Poor support or neglected accounts** | Restructure customer success and set executive sponsorship for key accounts | No. |
| **Overselling and broken promises** | Tighten sales-to-delivery handoffs and align incentives with retention | No. This is leadership and incentives. |
| **Losing to cloud-native competitors on architecture** | A separate team building the next-generation platform, with a migration path for existing customers | **Yes.** This is the classic case. |
| **An unserved segment, such as smaller carriers, MGAs, or embedded insurance** | A separate venture with a different pricing and delivery model | **Yes.** |
| **A new capability the market expects, such as AI in claims or underwriting** | Depends. A protected team if it conflicts with the core's roadmap, otherwise core investment | **Maybe.** |

My honest expectation: most of your churn will fall in the top four rows, meaning core problems the CEO's approach can address. Your lost new business may point to the bottom rows. If so, you'll likely end up with a two-track strategy: fix the core to keep customers, and build a protected team to win the future. You and the CEO would both be right, about different problems.

## What I'd avoid

- **Launching the lab before the diagnosis.** It would look like you came in with an answer and ignored the evidence.
- **Spreading effort across ten initiatives.** Pick the two or three that matter most.
- **Letting the study drag on.** Six to eight weeks is enough. Speed signals seriousness.
- **Trying to win arguments.** Win with evidence and results.

## Where I can help next

The most useful thing now is specifics. If you can share any of the following, I can give you much sharper advice:
- What your products are (policy admin, claims, billing, a full suite?) and which customer segments you serve
- Who you're losing deals to
- What you already suspect is driving churn
- What your CEO and sales leadership are like to work with

And once you've run the interviews, bring me the patterns. That's where we can figure out exactly what to fix, and whether and where a protected venture team belongs.

## Outcome summary (sent to Jev)

The recommendation is to neither build an independent innovation lab now nor rely purely on the existing organization. The right structure should follow a diagnosis of why customers are leaving and why deals are lost. Churn is most likely a core problem, such as painful upgrades, slow configuration, failed implementations, weak support, or overselling. The CEO's approach of fixing things inside the existing organization is largely right for those problems.

A separate but linked team is justified only for structural opportunities the core cannot pursue because of its architecture, business model, or incentives. Examples include losing to cloud-native competitors, serving unserved segments like smaller carriers or MGAs, or possibly AI capabilities that conflict with the core roadmap. The likely outcome is a two-track strategy: fix the core to keep customers, and build a protected team to win the future. Pure internal efforts get starved by the core's incentives. Fully independent labs tend to produce innovation theater, trigger organizational antibodies, and lose the incumbent's customers and distribution.

The proposed sequence:

- **Days 1–30:** Secure the CEO's endorsement and advance commitment to decision criteria. Meet the sales leader one-on-one with guardrails. Start interviews and pull internal data.
- **Days 30–60:** Complete 15–20 churn interviews and 5–10 lost-deal interviews. Quantify lost revenue by root cause and pressure-test conclusions. Preview the findings privately with the CEO.
- **Days 60–90:** Launch a focused, time-boxed fix on the top churn drivers, such as a 90-day upgrade reliability program with five at-risk accounts.
- **Days 90–180:** Propose a small team reporting to the CEO, with its own metrics, links to core channels, and kill criteria.

Key caveats: the advice cannot be specific without evidence. Findings that conveniently support the lab thesis deserve particular scrutiny. Autonomy should be earned through visible wins rather than demanded. The study should not drag on or sprawl across too many initiatives.
