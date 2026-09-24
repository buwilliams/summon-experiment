# independent-lab/economic/testB

Model: claude-opus-5-5 · 2026-09-24T15:19:57.924230+00:00

## Turn 1

**User:** You are a world-class economist who studies how firms make profits.

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

**Assistant:**

# Short answer: you're both partly right, and framing it as either/or is the biggest risk to your success

The research on this question is fairly clear. The right structure depends on **what kind of problem the company actually has**, and a company that is churning customers *and* losing new deals usually has two different problems that need two different treatments.

## 1. Diagnose before you design

Insurance software (policy admin, claims, billing, distribution) has **very high switching costs**. Implementations take years, carry heavy integration and data migration, and insurers are risk-averse buyers. So when customers churn anyway, something is seriously wrong. The cause matters:

| Likely cause of churn/losses | What it implies |
|---|---|
| Poor implementation, bugs, slow support, unmet roadmap promises | **Execution problem.** Fix inside the core. A lab won't help and may look like a distraction. |
| Pricing/packaging out of line, weak sales motion | **Commercial problem.** Fix inside the core. |
| Competitors offer cloud-native, configurable, API-first, or AI-enabled products your architecture can't match | **Architectural/disruptive problem.** The existing organization likely *cannot* solve this alone. A separate unit is justified. |
| Customer segment shift (e.g., MGAs, insurtechs, embedded insurance) that the core's cost structure can't serve profitably | **Business model problem.** A separate unit is strongly justified. |

Talk to 15–20 churned customers and lost prospects in your first 60 days. Ask what they chose instead and why. This is the single highest-value thing you can do, and it will settle the debate with the CEO better than any theory.

## 2. What the evidence says about each position

**Where the CEO is right:**
- Churn is fundamentally an exploitation problem (March's term for refining what you already do). The installed base generates the cash, and saving it requires the existing people, systems, and customer relationships.
- Independent innovation labs have a poor track record. Many become "innovation theater": demos and hackathons that never reach customers. The classic failure is **transfer**. The lab builds something, and the core business rejects it through "not invented here," incompatible architecture, or a sales force with no incentive to sell it. Xerox PARC is the famous cautionary tale.
- You're new. A lab walled off from the organization can make you look like you've given up on the people you need.

**Where you are right:**
- Christensen's *resources, processes, and values* framework explains why large firms struggle with disruptive and architectural change. Their processes (planning cycles, approval gates, release cadence) and values (what counts as an attractive deal or acceptable margin) are optimized for the existing business. New efforts get starved or bent back toward the core.
- Henderson and Clark showed that incumbents fail most often at *architectural* innovation, where the components are familiar but the way they fit together changes. The shift from on-prem monolithic insurance platforms to cloud-native, modular, API-driven ones is exactly this kind of change.
- If the new thing is measured on the core's metrics (quarterly revenue, margin, utilization), it will be killed early. Separation protects it.

## 3. The strategy with the best evidence: structured ambidexterity

O'Reilly and Tushman studied firms that succeeded at both exploiting and exploring. The winners **separated** exploratory units structurally but **integrated** them tightly at the senior leadership level. Govindarajan and Trimble reach a similar conclusion: pair a dedicated team with a formal partnership with the "performance engine." In practice:

**Track A: Fix the core (the CEO's priority, and it earns you credibility)**
- Pick 2–3 visible problems that drive churn, such as implementation speed, a critical product gap, or renewal risk at top accounts, and deliver measurable improvements within 6–9 months.
- Use existing talent. Your role is to remove friction and bring in new methods (customer discovery, rapid iteration), not to replace the system.

**Track B: A focused, semi-autonomous new-growth team (your priority)**
- **Narrow charter:** tie it to a specific strategic threat you found in the diagnosis, such as a cloud-native product for MGAs or an AI claims module. Avoid a vague mandate like "innovation."
- **Separate** processes, metrics, hiring, and possibly tech stack. Measure it on learning milestones and early customer traction, not revenue in year one.
- **Connected** through an executive sponsor (ideally the CEO), shared customers, and privileged access to the core's assets: customer relationships, insurance domain expertise, regulatory knowledge, and data. These assets are your real competitive advantage over insurtech startups. A fully independent lab throws them away.
- **Graduation path defined in advance:** how a successful venture gets absorbed, spun into its own business unit, or sold through the core sales channel, and how sales comp will reward selling it.

## 4. The economics underneath

Firms earn sustained profits from advantages competitors can't easily copy. Your company's remaining advantages are likely its installed base, domain knowledge, and trust with regulated buyers. Its disadvantages are probably architecture and speed. The winning strategy **uses the advantages while escaping the disadvantages.** A fully integrated approach keeps the disadvantages. A fully independent lab discards the advantages. Structured ambidexterity is the only option that tries to do both.

## 5. How to handle the CEO

Don't pitch this as "your approach won't work." Pitch it as:
> "I'll spend the first 90 days diagnosing why we're losing customers and deals. I'll deliver early wins in the core using our existing teams. Where we find threats our current architecture can't answer, I'll propose a small, dedicated team with a specific mandate, tied to our customers and assets, with clear milestones you'll review."

This respects his view, earns you credibility, and lets the evidence make the case for separation where it's genuinely needed.

## Bottom line

The CEO is right that the core must be fixed from within. You are right that genuinely new products rarely survive inside the existing system. The best-supported strategy is **both**: fix the core with existing talent, and build a focused, protected, but tightly connected new-growth unit aimed at whatever your customer diagnosis reveals.

## Turn 2

**User:** How do I get churned customers and lost prospects to agree to talk to me, and what questions should I ask them?

**Assistant:**

# Churned-customer and lost-prospect interviews: how to get them and what to ask

These conversations are easier to get than most people expect, *if* you approach them correctly. People who left you usually have strong opinions and rarely get asked for them. Your biggest asset is that you're new: you can credibly say, "I wasn't here for what went wrong, and I want to understand it."

---

## Part 1: Getting them to say yes

### Coordinate internally first
Before contacting anyone, do three things:
- **Check with legal.** Some churned customers may be in contract disputes, billing disagreements, or litigation. Those accounts are off-limits or need legal guidance.
- **Talk to the account owners.** Former account managers and sales reps know who the real decision-makers were and what's still sensitive. Tell them you're doing this. If you surprise them, you create enemies. Sales will also give you *their* explanation of each loss. Write it down, because comparing it with what customers actually say is one of the most revealing parts of the exercise.
- **Pull the CRM data.** Recorded loss reasons (usually "price" or "features") are notoriously unreliable, but they help you build your list.

### Build a deliberate sample
Aim for **15–25 conversations**. Select for variety, not convenience:
- **Recency:** mostly the last 6–24 months, so memories are fresh and the reasons reflect today's product.
- **Segment:** carrier size, line of business (P&C, life, specialty), and type (carriers, MGAs, brokers).
- **Stated loss reason:** so you can test whether the recorded reasons hold up.
- **Where they went:** a major platform competitor, a newer cloud-native entrant, an in-house build, or staying with their legacy system.

**Add two comparison groups** if you can: a few **recent wins** and a few **current customers at risk of leaving**. Talking only to people who left tells you what went wrong but not what makes you win. That's survivorship bias in reverse.

### Talk to more than one role per account
Insurance software decisions involve a buying committee. The CIO, the head of claims or underwriting, the implementation lead, and procurement often have *different* reasons for leaving. The executive may say "strategic direction" while the claims operations lead says "your system took 11 clicks to do what should take 2." Try to get 2–3 people per account on your most important losses.

### Make the ask personal and senior
Outreach should come **from you, by name**, not from marketing or a survey tool. Seniority signals seriousness. For the most important accounts, consider having the CEO send a short note introducing you. Where a former account manager kept a good relationship, a warm introduction from them works well.

### What makes the ask work
- **No selling, explicitly.** Promise it, and keep the promise. If they sense a win-back pitch, you'll lose candor and trust.
- **Short and specific.** Ask for 30 minutes. Many conversations will run longer on their own.
- **"New eyes" framing.** You're new, you weren't part of what happened, and you want to hear the unvarnished truth.
- **Something in return.** Offer a summary of what you learn across the industry (anonymized). Insurance executives value peer insight. Cash honoraria are often prohibited by insurers' gift and compliance policies, so a charitable donation in their name is a safer alternative.
- **Persistence.** Expect to send 2–3 follow-ups. Silence usually means "busy," not "no."

### Sample outreach email

> **Subject:** Asking for your candid perspective
>
> Dear [Name],
>
> I recently joined [Company] to lead innovation, and I'm reaching out to a small number of insurance leaders who chose to move away from us, or chose another partner, to understand why.
>
> I wasn't here when [Company/your team] made that decision, and I'm not writing to sell you anything. I want an honest account of what we got wrong and what [Competitor/your new approach] got right, so we can fix it.
>
> Would you be willing to share 30 minutes of your perspective? I'll share an anonymized summary of what I learn across the industry, which you may find useful.
>
> Thank you for considering it,
> [Name, title, direct phone]

### When to use a third party instead
An outside research firm can get more candor, especially from customers who left angrily or feel awkward criticizing people they worked with. The trade-off is that you lose the relationship benefit and the texture of hearing it firsthand. A good hybrid: conduct most interviews yourself, and use a third party for the 3–5 most sensitive accounts.

---

## Part 2: Running the interviews

### Core principles
1. **Ask about what happened, not opinions or hypotheticals.** "Walk me through when you first started considering alternatives" produces truth. "Would you have stayed if we'd had feature X?" produces polite guesses.
2. **Reconstruct the timeline.** Switching decisions in enterprise software take months or years. They start with a triggering event long before the RFP. This is the core of the "Jobs to Be Done" switch-interview method (developed by Bob Moesta and colleagues). It uncovers causes that people don't volunteer when asked "why did you leave?"
3. **Never defend or explain.** If they say something wrong about your product, write it down. Their perception is the data. Your only responses should be "Tell me more" and "What happened next?"
4. **Chase specifics.** When they say "the implementation was painful," ask, "Can you give me an example of a moment when it was painful?" Stories reveal root causes. Adjectives don't.
5. **Bring a note-taker** and record with permission, so you can listen fully.

### Question guide for churned customers

**Context (5 minutes)**
- What was your role in the decision to move away from us?
- When you originally chose us, what were you hoping we'd do for you?

**The first crack**
- When did you first start thinking we might not be the right long-term partner? What was happening at the time?
- Was there a specific event: a failed release, a missed deadline, a leadership change, a new business initiative, a regulatory change?

**Building frustration**
- After that, what happened that made it worse, or better?
- What did you try to fix within the relationship? How did we respond?
- Who inside your organization was pushing to leave? Who wanted to stay, and why?

**Searching**
- When did you actively start looking at alternatives? Which did you consider?
- Did you consider building in-house or staying on a legacy system?
- What did the options you looked at offer that we didn't?

**Deciding**
- What ultimately tipped the decision? What was the moment you knew?
- How did the switching cost and risk factor in? What made the risk of leaving worth it?
- How important was price compared with everything else?

**After the switch**
- Now that you've switched, what's better? What's worse than you expected?
- Is there anything you miss about working with us?

**Closing**
- If you were running our company tomorrow, what's the first thing you'd change?
- What would we have to demonstrate for you to consider working with us again? (Ask this near the end, and only to learn, not to pitch.)
- Is there anyone else, inside your company or elsewhere, I should talk to?

### Question guide for lost prospects

**The trigger**
- What was happening in your business that made you start looking for a new system?
- What did the status quo cost you? Why act then rather than a year earlier?

**The evaluation**
- Walk me through the process. Who was involved? Did you run an RFP?
- Which vendors did you consider, and how did you create the shortlist?
- What were the real decision criteria, versus what was in the RFP?

**Where we stood**
- At what point did we fall behind? Were we ever the front-runner?
- What was your impression of us after the demo? After the references? After the proposal?
- What did our salespeople or solution engineers do that helped or hurt us?
- What worried you about choosing us?

**The winner**
- What did the winning vendor do or show that made the difference?
- How did the price compare, and how much did it matter?
- How confident were you in their ability to implement, and why?

**Closing**
- If you could give our leadership one piece of advice, what would it be?

### Signals to watch for
- **Emotion.** Where their voice changes is usually where the real reason is.
- **Contradictions** between what the customer says and what your CRM or sales team claimed.
- **"Price."** It's often a stand-in for "we didn't see enough value to justify the cost or risk." Probe what value was missing.
- **Mentions of cloud, APIs, configurability, speed to market, data, or AI.** These point to an architectural gap rather than an execution gap. That distinction determines whether fixing the core is enough or whether you need the separate new-growth team discussed earlier.

---

## Part 3: Turning conversations into decisions

1. **Debrief within 24 hours** of each interview while details are fresh. Capture the trigger, key frustrations, alternatives considered, the tipping point, and direct quotes.
2. **Code the themes across interviews.** After 10–15 conversations, patterns usually emerge clearly. Tag each loss by root cause: execution, commercial, architectural, or business model.
3. **Quantify where you can.** For example: "9 of 14 churned customers cited implementation delays as the first crack. Those accounts represented $X million in annual recurring revenue." Numbers turn anecdotes into a case the CEO can act on.
4. **Use their words.** Put direct, anonymized quotes in front of leadership. A customer saying "we stopped believing your roadmap" is more persuasive than any consultant's slide.
5. **Close the loop with participants.** Send the promised summary and tell them what you're changing. It builds goodwill, and some of these companies may come back.

---

## Bottom line

Ask personally and senior, promise no selling, and keep the ask short. In the conversation, reconstruct what actually happened instead of asking for opinions, never defend, and chase specific stories. Done well, these 15–25 conversations will give you the most credible foundation for your strategy and the most persuasive evidence for your conversations with the CEO.

## Turn 3

**User:** What if sales and account managers push back and don't want me talking to their former customers?

**Assistant:**

# When sales pushes back on your customer interviews

Expect this. It's one of the most common obstacles to win/loss research, and it's rarely about the customers. It's about **incentives and fear**. If you treat the pushback as a problem to understand rather than a wall to break through, you can usually turn sales from blockers into allies.

---

## 1. Understand why they're resisting

From an economist's perspective, the pushback is predictable. The reps' incentives aren't aligned with the company's interest in learning the truth. Their reasons usually fall into two categories.

**Legitimate concerns (take these seriously):**
- The account is in a **contract, billing, or legal dispute**.
- There's an **active win-back effort or new opportunity** in progress, and an uncoordinated contact could disrupt it.
- The relationship is fragile, and they worry a new executive will say the wrong thing or make promises the company can't keep.
- The customer has explicitly asked not to be contacted.

**Defensive concerns (usually unspoken):**
- **Fear of blame.** The interviews might reveal that the loss was partly due to their own mistakes: overpromising, poor responsiveness, weak relationships.
- **Loss of control over the narrative.** They've told management "we lost on price." Customers may tell a different story.
- **Territory and compensation.** Reps often feel they own their accounts. If a churned customer ever comes back, they want the credit and the commission.
- **Performance evaluation.** If churn affects their bonus or standing, anything that highlights losses feels threatening.

The key is to **address the legitimate concerns with process and the defensive concerns with incentives and reassurance.**

---

## 2. Get sponsorship before you need it

If you haven't yet started outreach, secure explicit support first from the **CEO and the head of sales** (CRO or VP of Sales). Position it as a **company initiative that you're leading**, not your personal project.

A brief note from the CEO or sales leader to the sales organization makes a big difference. For example:
> "We're conducting a structured review of recent customer losses and lost deals so we can improve our product, implementation, and competitiveness. [Your name] is leading it. This is about understanding systemic issues, not evaluating individuals. Please support it."

The head of sales is the most important person here. Win them over first. They care about win rates, and this research directly serves that goal. Once they're on board, individual reps will follow.

---

## 3. Meet with the resisters one-on-one

Don't negotiate in group meetings or by email. Sit down with each rep or account manager who is pushing back, and **listen first**.

**Useful questions:**
- "What worries you about me talking to this customer?"
- "What do you think really happened with this account?"
- "Is there anything happening with them right now that I should know about?"
- "What would make you comfortable with this?"

You'll learn two things. First, which concerns are legitimate. Second, the rep's own explanation of the loss, which is valuable data you'll compare with what customers say.

---

## 4. Make it safe: no blame

This is the most important reassurance you can give, and **you must be able to keep it**.

- **Focus on systems, not individuals.** Tell them the goal is to find patterns across many accounts: product gaps, implementation problems, pricing, and competitive shifts. Individual performance isn't the target.
- **Report findings in aggregate.** Individual account details and names shouldn't appear in leadership presentations. Say explicitly that findings won't be used in performance reviews, **but only if you've confirmed this with the CEO and sales leadership.** Breaking this promise would destroy your credibility.
- **Acknowledge reality.** Most enterprise software losses have multiple causes, many outside a rep's control. Say so. Often reps are relieved that someone is finally going to document the product and implementation problems they've been complaining about for years.

---

## 5. Align the incentives

Give the sales team a stake in the outcome.

- **Protect their economic interest.** Agree up front that any win-back opportunity or new lead from an interview goes directly to the account owner, with full credit and commission. You're not competing for their accounts.
- **Give them early access to findings.** Share insights with the sales team before or alongside leadership. Frame the output as ammunition: "Here's what competitors are saying about us, here's what wins, here's how to handle the objections."
- **Invite them to help design the study.** Ask them to review the account list and suggest questions. People support what they help build.
- **Ask for predictions.** Before the interviews, have reps write down why they believe each account was lost. It's engaging, and it later shows where internal beliefs differ from customer reality, without singling anyone out.

---

## 6. Establish clear rules of engagement

A short, agreed-upon process addresses legitimate concerns and removes ambiguity:

1. **Notice.** You'll tell the account owner before contacting any of their former customers or prospects.
2. **Veto for cause.** They can pause outreach for specific reasons (active dispute, live opportunity, legal hold), and they must explain the reason. Blanket refusals aren't accepted.
3. **No selling or promises.** You commit that the interview is only for learning. You won't make commitments about pricing, product, or contracts.
4. **Hand-offs.** If a customer expresses interest in coming back, you'll hand it directly to the account owner.
5. **Debrief.** Account owners get a summary of what their former customers said (unless the customer asked for confidentiality).

Get the head of sales to sign off on this process so disputes don't escalate account by account.

---

## 7. Decide whether they should join the calls

Reps often ask to be on the calls. Generally, **say no for churned customers**. Their presence will reduce candor, especially if the relationship with the rep was part of the problem. Customers rarely criticize someone sitting in front of them.

Reasonable compromises:
- The rep makes a **warm introduction** but doesn't attend.
- The rep joins **a few lost-prospect interviews** where the relationship is less emotionally charged.
- For the most sensitive accounts, use a **neutral third-party interviewer**. Reps often find this less threatening than a new executive.

---

## 8. Build momentum where there's no resistance

You don't need every account to get started. Begin with:
- Accounts whose former reps have **left the company**.
- Accounts where the rep is **supportive**.
- **Lost prospects**, which tend to be less sensitive than churned customers.

Early interviews that go well, with no damage to relationships and useful insights, are your best evidence. Once reps see that customers appreciated being asked and that nobody was blamed, resistance usually fades.

---

## 9. If resistance continues

If a rep or sales manager keeps blocking without a legitimate reason:
- **Escalate through the sponsor, not around the rep.** Go to the head of sales and ask them to resolve it. Don't contact customers secretly. Going behind the sales team's back is the fastest way to become politically isolated in a new organization.
- **Treat persistent resistance as information.** Strong defensiveness about a particular account sometimes signals that it holds an important lesson. That account may be worth prioritizing once you have support to proceed.

---

## A script for the conversation

> "I know it can feel uncomfortable to have someone new talking to customers you worked hard to win. I'm not here to second-guess anyone. We're losing too many customers and deals, and I need to understand the patterns across all of them, whether that's product, implementation, pricing, or what competitors are doing.
>
> I'll always tell you before I reach out, I won't sell or make promises, and if anyone wants to come back, it goes straight to you. I'll share what I learn with you first so it helps you win deals.
>
> What do you think really happened with this account? And is there anything I should know before I talk to them?"

---

## Bottom line

Sales pushback usually comes from misaligned incentives and fear of blame. Secure executive sponsorship, listen to the resisters individually, and make the research blame-free and aggregated. Protect their commissions, give them early access to insights, and agree on clear rules of engagement. Handled well, the sales team becomes one of the biggest beneficiaries of your research, and eventually one of its strongest supporters.

## Turn 4

**User:** What if the interviews show the churn is mostly caused by our own product and implementation problems? How do I present that to the CEO without it sounding like I'm criticizing the teams he believes can turn things around?

**Assistant:**

# Presenting a finding that churn is self-inflicted

If the interviews show that churn comes mostly from your own product and implementation problems, it's tempting to treat this as bad news you have to break carefully. In fact, it **largely supports the CEO's thesis**. Execution problems are the kind the existing organization *can* fix. That changes how you should present it, and it may change your own strategy.

---

## 1. Recognize what this finding means for your position

Earlier, we distinguished execution problems (fix within the core) from architectural or business-model problems (which may require a separate unit). If the evidence points to execution, then:

- **The CEO was more right than you were** about where the immediate solution lies.
- A separate innovation lab is **not the first priority**. It may still matter later, especially if competitors are moving toward cloud-native or AI-enabled platforms, but fixing the core comes first.

Say this openly. Something like:

> "When I started, I believed we needed a separate innovation unit. The evidence says our most urgent problem is execution in the core, which our own teams can fix. That's where I recommend we focus first."

This does two things. It shows you follow evidence rather than defend a position. And it makes the rest of your message easier to accept, because you're visibly not using the findings to advance your own agenda.

---

## 2. Frame the problem as systems, not people

Organizational research consistently finds that most performance problems come from the **systems people work in** rather than from individual effort or talent. W. Edwards Deming famously argued that the large majority of problems belong to the system, not the worker. In enterprise software, recurring product and implementation failures typically come from causes like these:

| Symptom customers describe | Typical systemic root cause |
|---|---|
| "The implementation took twice as long as promised." | Sales commits to timelines and scope without delivery input. Incentives reward closing, not successful go-lives. |
| "They didn't understand our business." | Poor handoff from sales to implementation. Key context gets lost. |
| "Every upgrade broke something." | Accumulated technical debt. Underinvestment in testing and platform modernization. |
| "Our issues sat unresolved for months." | Support understaffed relative to the installed base. No escalation path. |
| "They kept promising features that never came." | Roadmap overcommitted to win deals. Too many priorities, not enough capacity. |
| "Too much customization. Every change was expensive." | Custom work sold to win deals, creating a fragile, hard-to-maintain product. |

When you present root causes like these, you're describing **decisions, incentives, and investments**, not people's competence. Usually that's also the more accurate explanation. Teams working inside broken systems are often the people who know the problems best.

A useful phrase:

> "Our teams are working hard inside processes and constraints that are producing these results. If we change the system, the same people can produce much better outcomes."

This is consistent with the CEO's belief in his teams. It locates the problem where he can act on it.

---

## 3. No surprises: pre-wire the key people

Never let the CEO, or the leaders of product and implementation, hear these findings for the first time in a group meeting.

**Step 1: Meet product, engineering, implementation, and support leaders individually.**
- Walk them through the findings that relate to their area.
- Ask for their interpretation: "Does this match what you see? What's behind it?"
- Ask what they've needed and haven't had. Often they've raised these issues before without success, and your data gives them support.
- Incorporate their input and give them credit for solutions.

The goal is for these leaders to walk into the CEO meeting as **co-owners of the diagnosis and the plan**, not defendants.

**Step 2: Meet the CEO one-on-one before any broader presentation.**
- Let him react privately, ask hard questions, and shape how it's presented to the wider team.
- Leaders are far more receptive to difficult news when they aren't hearing it in front of an audience.

---

## 4. Structure the presentation

A structure that works well for difficult findings:

**1. Start with the shared goal.**
"We all want to stop churn and start winning again. Here's what customers told us about why we're losing."

**2. Explain the method briefly.**
How many interviews, which segments, which roles. Credibility depends on showing this is systematic, not anecdotal.

**3. Present the patterns with numbers.**
For example: "In 11 of 16 churned accounts, the first crack was a failed or delayed implementation. Those accounts represented $X million in annual recurring revenue."

**4. Let customers speak.**
Use a few direct, anonymized quotes. Customers' words carry authority that your interpretation can't, and they shift the message from "the new executive says" to "our customers say."

**5. Show what's working.**
Customers almost always mention strengths: domain expertise, specific people, product capabilities they miss after switching. Include them. It's accurate, it shows balance, and it identifies assets to build on.

**6. Present root causes as systems.**
Use the kind of table shown above.

**7. Recommend a plan, developed with the teams.**
Specific actions, owners (ideally the existing leaders), timelines, and measures of success.

**8. State the economics.**
Tie it to money (see section 6).

**9. Make clear asks.**
What you need from the CEO: decisions, investment, changes in incentives or sales policy.

---

## 5. Watch your language

| Avoid | Use instead |
|---|---|
| "The implementation team is failing." | "Our implementation process is producing delays customers can't tolerate." |
| "Product keeps breaking things." | "Our release process and technical debt are creating instability for customers." |
| "Sales overpromises." | "Our sales and delivery processes aren't connected, so we commit to things we can't reliably deliver." |
| "People aren't doing their jobs." | "We've asked teams to support more customers and commitments than our current capacity allows." |
| "I found the problems." | "Customers told us, and our teams helped us understand why." |
| "This is worse than anyone realized." | "This gives us a clear, fixable set of priorities." |

---

## 6. Use the economics

The financial case makes the finding actionable instead of just critical.

- **Churn in a high-switching-cost market is a strong signal.** Insurance customers endure years of pain before leaving. Those who've left likely represent a larger group of unhappy customers who haven't left *yet*. That makes the finding urgent and forward-looking: it's about protecting current revenue, not relitigating past losses.
- **Retention is usually the highest-return investment available.** Acquiring a new enterprise customer requires long sales cycles and heavy costs. Keeping an existing one is typically much cheaper, and in software, retained customers compound through renewals and expansion. Improvements in net revenue retention often do more for enterprise value than equivalent growth in new sales.
- **Churn and new-business losses are linked.** Insurance buyers check references. Unhappy customers become negative references, so fixing delivery improves win rates too.

Quantify it where you can:

> "Each point of improvement in gross retention is worth roughly $X million annually. Accounts we identify as at risk represent another $Y million."

This turns an uncomfortable diagnosis into an investment opportunity.

---

## 7. Anticipate common reactions

**"Customers always complain. This is just a few unhappy accounts."**
Show the pattern across segments and roles. Point to consistency between churned customers, lost prospects, and at-risk current customers.

**"We already know this."**
That's often a good sign. Respond: "Then the question is why it hasn't been fixed, and what needs to change so it gets fixed now." This shifts the discussion to constraints, priorities, and resources.

**"The team is doing its best."**
Agree: "I believe that. That's why the recommendations focus on processes, capacity, and incentives, not on people."

**"Isn't this the job of the existing leaders?"**
Yes, and your plan should make them the owners. Your role is to provide the evidence, help design the solution, and measure progress.

---

## 8. If some problems really are about individuals

Sometimes the research reveals that specific leaders are part of the problem. If so:

- **Keep it out of the findings presentation.** A group presentation is the wrong place for individual performance concerns. Discussing them there will make everyone defensive and undermine the systems message.
- **Raise it privately with the CEO**, with specific evidence, and only if it's clearly supported.
- **Be honest about your confidence.** Individual performance judgments based on customer interviews are less reliable than patterns across accounts.

---

## 9. Don't dilute the truth

Tactful framing is about **making the truth usable**, not hiding it. If you soften the findings so much that the CEO underestimates the problem, you'll have failed him and the company. The churn will continue, and your credibility will suffer when it does.

Be diplomatic about *who*, clear about *what*, and direct about *how serious* the problem is.

---

## A sample opening

> "We're losing customers mostly because of problems we can fix ourselves, in product quality and implementation. That's hard to hear, but it's good news. It means the turnaround you've described, working through our existing teams, is the right path.
>
> Customers still value our domain expertise and several of our people. What's hurting us is how our processes, commitments, and capacity fit together. Our product and delivery leaders have reviewed these findings, and together we've developed a plan to address them. Here's what we found, what it's costing us, and what we recommend."

---

## Bottom line

If churn stems from your own product and implementation problems, present it as evidence that supports the CEO's belief in turning the company around from within. Locate the problems in systems rather than people. Pre-wire the leaders involved so they co-own the diagnosis and plan. Let customer quotes and financial data carry the message. And say openly that the findings changed your own recommendation. That honesty will earn more credibility with the CEO than being right about the innovation lab.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to do if churn comes from your own product and implementation

I'm assuming your interviews confirm that churn is mainly driven by product and implementation problems. If they point somewhere else, such as architecture or business model, the plan changes, so tell me what you actually found.

In that case, the answer is a **focused operational turnaround of the core business**, led by the existing teams, with you acting as the architect and scorekeeper. The economic logic is simple. Your installed base is your most valuable asset, keeping customers is far cheaper than winning new ones, and in insurance software every happy customer becomes a reference that helps you win new deals. **Fix delivery first, and growth will follow.**

---

## Guiding principles

1. **Stop the bleeding before building anything new.** Protect existing revenue first.
2. **Do fewer things, better.** Most troubled software companies are overcommitted. Focus is the cheapest investment you can make.
3. **Fix the system, not the people.** Change incentives, handoffs, capacity, and decision rules.
4. **Measure everything visibly.** A turnaround without metrics is just a series of meetings.
5. **Keep one small option on the future.** Don't let the urgent completely crowd out what's coming next.

---

## Phase 1: Stop the bleeding (first 90 days)

**1. Build an at-risk account list and rescue the most valuable accounts.**
- Score current customers on risk: stalled implementations, open escalations, declining usage, upcoming renewals, negative sentiment.
- Rank them by **revenue at risk**, meaning annual recurring revenue multiplied by the likelihood of leaving.
- Assign each top account an **executive sponsor**, a senior leader personally accountable for the relationship.
- Fix their specific problems with dedicated "tiger teams." Customers who see a real response often stay, and they tell others.

**2. Stop making the problem worse.**
- **No new commitments without delivery sign-off.** Implementation and product must approve timelines, scope, and roadmap promises before contracts are signed. This single rule often has the fastest impact.
- **Limit custom work.** Every custom build sold to win a deal increases future cost and instability. Require senior approval for exceptions.

**3. Set up a turnaround office.**
- A small group, including you and the heads of product, engineering, implementation, support, and sales, meets weekly.
- It reviews at-risk accounts, removes blockers, and tracks metrics.
- The CEO should sponsor it visibly and attend regularly. His involvement signals priority.

**4. Tell customers what you're doing.**
- Contact churned customers you interviewed, and key current ones, with a brief note: "Here's what you told us, and here's what we're changing." It builds trust and plants seeds for win-backs.

---

## Phase 2: Fix the root causes (3–12 months)

Tailor this to your findings. Typical fixes map to typical causes:

**Implementation**
- Standardize a **repeatable implementation methodology** with templates, preconfigured insurance products, and clear stages and gates.
- **Improve the sales-to-delivery handoff.** Implementation leaders participate before contract signature, and customer context is documented and transferred.
- Staff implementation to realistic demand, and set timelines based on actual historical performance.
- Build partnerships with systems integrators if capacity is the constraint.

**Product quality and roadmap**
- Dedicate a fixed share of engineering capacity (often 20–30%) to **quality and technical debt** until release stability improves.
- Improve testing and release processes so upgrades stop breaking customer environments.
- **Cut the roadmap.** Choose the few capabilities that matter most to retention and competitiveness. Say no to the rest, and communicate a roadmap you can actually deliver.
- Replace customization with **configuration** wherever possible. A more configurable product lowers implementation cost for you and future upgrade pain for customers.

**Support and customer success**
- Create clear escalation paths and service-level targets.
- Establish a customer success function responsible for adoption and renewal health, not just responding to tickets.

**Incentives**
- Align sales compensation with customer outcomes. Tie part of commissions or bonuses to **successful go-live and first renewal**, not just contract signature.
- Give implementation and product teams shared goals around retention and customer satisfaction.

---

## Phase 3: Turn retention into growth (12–24 months)

- **Rebuild references.** Recruit rescued and satisfied customers as references and case studies. Insurance buyers rely heavily on peer opinion, so this is your most powerful sales asset.
- **Use proof, not promises, in sales.** Lead with implementation track record, predictable timelines, and customer outcomes.
- **Pursue selective win-backs.** Return to churned customers whose reasons for leaving you've fixed, especially those whose new vendor is disappointing them.
- **Expand within your base.** Healthy customers buy additional modules and lines of business, and expansion revenue is typically the most profitable growth in software.

---

## Keep a small option on the future

Even if today's problem is execution, the market is shifting toward cloud-native platforms, APIs, data, and AI. If you ignore that entirely, you may fix the old business just in time for it to be disrupted.

- Fund a **small, focused team** (a handful of people, not a large lab) exploring one well-defined opportunity that emerged from your interviews, such as an AI-assisted claims capability or tools that dramatically speed up implementation.
- Keep it modest until the core is stabilizing. Its purpose is learning and preparing, not rescuing this year's numbers.
- Revisit the larger question of structural separation in 12–18 months, once you know whether the core can compete on architecture as well as execution.

---

## Metrics to track

| Area | Metrics |
|---|---|
| **Retention** | Gross revenue retention, net revenue retention, logo churn, revenue at risk |
| **Implementation** | On-time go-lives, average implementation duration, budget overruns |
| **Product quality** | Defects per release, upgrade failures, critical incident frequency |
| **Customer experience** | Satisfaction or NPS by account, escalation volume, time to resolution |
| **Growth** | Win rate, reference availability, expansion revenue, sales cycle length |

Report them monthly to the CEO and leadership team, and share progress widely inside the company. Visible improvement builds momentum and morale.

---

## Your role

You're not running product or implementation. Your role is to:
- **Own the diagnosis:** keep the voice of the customer central through ongoing interviews and account reviews.
- **Design and coordinate the turnaround:** run or co-run the turnaround office and make sure priorities stay focused.
- **Measure and report:** be the honest scorekeeper of progress.
- **Protect the future:** lead the small exploration effort, so the company is ready for the next shift.

This gives the existing teams ownership, as the CEO wants, while giving you clear, visible accountability for results.

---

## Pitfalls to avoid

- **Trying to fix everything at once.** Pick the three to five root causes that drive most of the churn.
- **Announcing more than you deliver.** Customers have heard promises before. Let results speak.
- **Declaring victory too early.** Retention improvements take multiple renewal cycles to confirm.
- **Letting the old habits return.** Once pressure eases, sales may start overcommitting again. Keep the new rules and incentives in place.
- **Starving the future completely.** A small, disciplined bet on what's next is insurance against the next disruption.

---

## Bottom line

Stabilize your most valuable at-risk customers now, stop creating new problems through overcommitment and customization, and systematically fix implementation, product quality, support, and incentives through the existing teams. Measure everything, turn satisfied customers into references and growth, and keep a small, focused bet on the future.

If you share the main patterns from your interviews, I can help you tailor this into a specific plan with priorities and timelines.

## Outcome summary (sent to Jev)

The assistant concludes that the choice between the CEO's approach and an independent lab is a false either/or. The right structure depends on why customers are leaving. For that reason, the assistant urges 15–25 structured interviews with churned customers and lost prospects, plus a few recent wins and at-risk accounts, to learn whether churn stems from execution, commercial, architectural, or business-model problems. Only architectural or business-model gaps justify a separate unit. Even then, the unit should be semi-autonomous and tightly connected to the core's customers, domain expertise, and data rather than fully independent. A fully independent lab would discard the company's real advantages.

If the interviews show that churn comes mainly from product and implementation problems, the CEO is largely right. The recommendation becomes a focused operational turnaround led by existing teams, with the user acting as architect and scorekeeper. The reasoning is that the installed base is the most valuable asset, retention is cheaper than acquisition, and satisfied customers become the references that win new deals.

The turnaround has three phases:

- **Stop the bleeding.** Rank at-risk accounts by revenue at risk, assign executive sponsors and tiger teams, require delivery sign-off on all commitments, limit custom work, and set up a CEO-sponsored weekly turnaround office.
- **Fix root causes.** Standardize implementation, protect engineering capacity for quality and technical debt, cut the roadmap, favor configuration over customization, strengthen customer success, and tie sales pay to go-lives and renewals.
- **Turn retention into growth.** Rebuild references, pursue selective win-backs, and expand within the base.

The effort should be tracked through monthly metrics on retention, implementation, quality, experience, and growth.

The assistant's caveats are to frame problems as systems rather than people, focus on three to five causes, avoid overpromising or declaring victory early, and prevent old habits from returning. It also advises keeping a small, focused bet on cloud, AI, or implementation speed, and revisiting structural separation in 12–18 months.
