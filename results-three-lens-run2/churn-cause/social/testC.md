# churn-cause/social/testC

Model: claude-opus-5-5 · 2026-09-24T15:33:05.871619+00:00

## Turn 1

**User:** Use impression management to answer the following.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Churn Through the Lens of Impression Management

Impression management, in Erving Goffman's sense, is how people control the picture others form of them. There is a public "front stage" performance and a "backstage" reality. Applied here, it explains why you have two confident, conflicting diagnoses, and it points to how to find out which one is true.

## 1. Everyone Explaining Your Churn Is Managing an Impression

**Departing customers.** When a carrier leaves, the person explaining the decision is usually the executive or champion who bought your software. They have two stories available:

- *"Your competitor has better AI and analytics."* This is impersonal, forward-looking, and easy to defend to a CFO, board, or regulator. It makes the buyer look strategic.
- *"We spent 14 months implementing, our adjusters never adopted it, and we got little value."* This implicates their own team, their own project management, and their original purchase decision.

People reliably choose the first story. So **exit surveys and churn-call notes are biased toward "product gaps"** even when the real cause is a failed implementation. "Missing features" is the face-saving reason.

**Your two VPs.** Both are performing too, and not dishonestly. Notice that each locates the problem in their own domain and proposes a fix that requires investment in their own team.

- **Product** frames churn as a market-competition problem, which justifies a faster roadmap and more headcount.
- **Services** frames churn as an experience problem, which justifies onboarding redesign and more resources before new features ship.

Each diagnosis is plausible, and each is also a budget bid. That doesn't make either wrong. It means neither can be accepted on the strength of conviction or anecdote.

**You.** Customer success sits between the two. If churn is "a service problem," CS may be implicated. If you side with Product, you may look like you're deflecting. How you present your answer matters almost as much as the answer itself.

## 2. Look Backstage: Behavioral Data Beats Stated Reasons

The way through impression management is to rely on what customers *did*, not what they *said*. Run a 30–45 day churn diagnostic built around these questions:

| Question | If the answer is yes, it points to... |
|---|---|
| Is churn concentrated among customers whose implementations ran long or never fully completed? | **Services** |
| Do churned customers show low adoption (logins, claims processed in-system, workflows configured) well before renewal? | **Services** |
| Did customers who cited "better analytics/AI" actually use your existing analytics? If not, the stated reason is likely a cover story. | **Services** |
| Are fully implemented, highly adopted customers also leaving, specifically to competitors with AI features? | **Product** |
| Did the churn spike coincide with a competitor's AI/analytics launch rather than a change in your implementation times or staffing? | **Product** |
| Are you losing deals at the renewal-competition stage (a rival pitched them) rather than through quiet non-renewal? | **Product** |

Also:

- **Cohort by time-to-value.** Plot churn rate against months-to-go-live and against depth of adoption at month 6. This single chart often settles the debate.
- **Ask what changed 18 months ago.** Churn doubled, so something shifted. Look for new competitor launches, implementation backlog, CS or services turnover, a new customer segment, or a pricing change.
- **Interview below the buyer.** Talk to adjusters, claims managers, and IT leads at churned carriers. They have less face to protect and will tell you whether the tool was actually used. Consider using a neutral third party for these calls. Customers are more candid when they aren't performing for the vendor.

## 3. My Likely Read and What to Do

For claims software sold to *regional* carriers, I'd bet the Services story is more often the root cause and the Product story is more often the stated cause. Regional carriers have small IT teams, legacy policy-admin systems, and heavy integration and regulatory work. That combination makes long implementations and partial adoption very common. A customer who never reached full value is primed to be swayed by a competitor's AI demo, and then to cite that demo as the reason for leaving.

Most likely both VPs are partly right, in sequence: **poor time-to-value creates vulnerability, and product gaps provide the exit rationale.** Let the data confirm or overturn this before committing budget.

**Sequencing I'd propose (adjust after the diagnostic):**

1. **Stop the bleeding in the current base (Services-led, now).**
   - Identify at-risk accounts with low adoption or stalled implementations.
   - Launch "get-to-value" rescue plans for them.
   - Set a hard time-to-first-value target for new implementations.
2. **Make product investment targeted, not generalized (Product-led, in parallel).**
   - Build only the specific gaps that *healthy, well-adopted* customers leave over. Those are the real product losses.
   - Prioritize AI/analytics features that also shorten implementation or prove value quickly, such as out-of-the-box claims dashboards or automated triage. These satisfy both theories at once.
3. **Fix the measurement.** Tag every churn with both the stated reason and behavioral indicators, so this debate is settled by data going forward.

## 4. Manage the Impression of Your Recommendation

To get alignment rather than a winner and a loser:

- **Present it as "we found the sequence," not "one of you was right."** Both VPs keep face, and both get a role.
- **Propose a shared metric**, such as net revenue retention or percentage of customers reaching defined value by month 6, that both Product and Services are measured on. This ends the incentive to explain churn in your own team's favor.
- **Own CS's part openly.** If the data shows adoption problems, say what CS missed, such as health scoring or early warning. Taking accountability first makes it easier for the others to do the same, and it keeps you credible as the neutral broker.

**Bottom line:** Don't pick a belief. Pick a diagnostic that sees past the face-saving stories customers and executives tell. My expectation is that you'll find implementation and value realization is the root cause, with competitor features as the trigger. The answer is then to fix onboarding first while making product investment narrow and evidence-based.

## Turn 2

**User:** Still using impression management, how should I run the interviews with adjusters and claims managers at churned carriers so I actually get candid answers?

**Assistant:**

# Running Candid Churn Interviews: An Impression Management Playbook

Your goal is to get adjusters and claims managers to talk about how the work actually happened, what Goffman calls the backstage, rather than the tidy front-stage story their company told you when it left. That means understanding which performances are at play and designing the interview so they aren't needed.

## 1. The Performances You're Up Against

Before designing anything, recognize what each interviewee is likely protecting:

| Performance | What it sounds like | Why they do it |
|---|---|---|
| **Team loyalty** | "Leadership made a smart call switching." | Goffman's "teams" cooperate to sustain a shared impression. An adjuster won't easily contradict the story their executives told you. |
| **Self-competence** | "The system was just clunky." | Blaming the tool is safer than admitting they never learned it or reverted to spreadsheets. |
| **Politeness** | "It was fine, honestly, just not the right fit." | Protecting *your* face. People soften criticism to a vendor's face. |
| **Fear of leakage** | Vague, guarded answers | Worry that comments will reach their boss or affect their reputation in a small regional-carrier world. |
| **Performing expertise** | Detailed opinions on AI roadmaps | Being interviewed feels like being consulted as an expert, so people drift toward strategy talk instead of daily reality. |

Every design choice below aims to remove the need for one of these performances.

## 2. Recruiting: Get the Right People Without Triggering Defenses

- **Interview below and beside the buyer.** Target adjusters, claims supervisors, claims ops managers, and the IT or integration lead who ran the implementation. These are the people who used the system, not the people who justified the switch.
- **Be transparent with the former account.** Tell your former executive contact you're doing learning interviews and ask for introductions, or at least let them know. Going around them risks backlash and makes interviewees nervous that they're doing something disloyal. Frame it as "helping us serve carriers like yours better," not "finding out what went wrong."
- **Go through outside channels too.** People who have since left the carrier are often the most candid, because they no longer belong to that team. LinkedIn outreach to former claims staff can surface these voices.
- **Handle incentives carefully.** Insurance has gift and compliance rules. A modest payment, a charity donation in their name, or a summary of cross-carrier findings (anonymized) often works better and signals that this is research, not sales.
- **Mix recent and older churners.** Recent churners remember details. Older ones have less at stake and may speak more freely.

## 3. Choose the Right Interviewer

This may be the single biggest lever.

- **Don't use the account's former CSM, implementation lead, or salesperson.** Criticizing the implementation to the person who ran it is a face-threat most people will avoid.
- **Ideally, use a neutral third party**, such as a research firm or independent consultant. Interviewees don't have to manage their relationship with your company, and "the vendor won't know it was you" becomes credible.
- **If it has to be internal**, pick someone with no history on the account, and have them present as a researcher. Someone from a research, strategy, or ops role works better than someone from sales or product.
- **Avoid pairing a VP with the interviewer.** A senior presence raises the stakes and pulls people back onto the front stage.

## 4. Set the Stage: Framing That Lowers the Stakes

The first two minutes define the "situation," Goffman's term for the shared understanding of what kind of interaction this is. You want it to read as **a confidential conversation about how work gets done**. You don't want it to read as a customer satisfaction call, a win-back attempt, or an evaluation of them.

**Do:**
- **Hold one-on-one conversations only.** Group interviews create a team performance, where no one wants to contradict colleagues.
- **Use video with the camera optional, or phone,** at a time outside their busy claims hours.
- **Make confidentiality concrete.** Explain exactly what happens to their words: quotes anonymized, carrier name removed, nothing shared with their employer. If you record, ask permission and explain who hears it.
- **State explicitly that this is not a sales call.** Then keep that promise. Any pivot to win-back destroys candor in this interview and in your reputation for future ones.

**Sample opening:**

> "Thanks for making time. I want to be clear up front: I'm not in sales, and I'm not trying to win back your business. We're trying to understand what day-to-day work was like for people who used our system, because we think we got some things wrong, especially around implementation. Nothing you say will be attributed to you or shared with anyone at [carrier]. Honestly, the most useful thing you could do is tell us what was frustrating or what didn't get used. You won't hurt anyone's feelings."

The line "we think we got some things wrong" matters. When you admit fault first, their criticism becomes agreement rather than attack, and the politeness performance loses its purpose.

## 5. Questions That Reach the Backstage

**Principle 1: Ask about behavior, not opinions.** Opinions invite performance, while specific past events are harder to dress up.

- ❌ "What did you think of our analytics?"
- ✅ "Think back to a typical week when you were using our system. Walk me through how a new claim came in and what you did with it."

**Principle 2: Hunt for workarounds.** Workarounds are the clearest signs of non-adoption, and people describe them without feeling they're confessing.

- "Were there things you kept doing in spreadsheets, email, or the old system?"
- "Was there anything the team just stopped using or never turned on?"
- "When you needed a report, where did it actually come from?"

**Principle 3: Ask about others, not self.** Projective questions let people describe backstage reality without implicating themselves.

- "How did the other adjusters on your team feel about it?"
- "What did new hires struggle with?"
- "What did people complain about in the break room?"

**Principle 4: Reconstruct the timeline.** Long implementations and partial adoption show up in chronology, not in summaries.

- "When did you first start using it for real claims?"
- "Was there a point where it felt like it was finally working, or did that never happen?"
- "When did you first hear the company was looking at other vendors? What was going on at the time?"

**Principle 5: Normalize the answers you need to hear.** Give people permission.

- "A lot of carriers tell us the implementation dragged and some features never got set up. Was that true for you, or was your experience different?"
- "It's really common for teams to keep using their old tools alongside a new system. How much did that happen for you?"

**Principle 6: Test the official story gently.** If the company cited competitor AI or analytics, ask about it neutrally and with specifics.

- "Did you use our reporting or analytics features? Which ones?"
- "What does the new system let you do that you couldn't do before?"
- If they praise the competitor's AI: "How often do you use that in a typical week?"

If someone says the new system's analytics were the reason for switching but never touched yours, that is a key finding.

**Principle 7: Close with a shift in footing.** Change their role from "former customer" to "advisor to peers." People are often most candid when helping someone like themselves.

- "If a claims manager at another regional carrier were about to buy our system, what would you warn them about?"
- "If you could go back to the start of the implementation, what would you change, on our side or yours?"

## 6. During the Interview: Protect the Backstage Once You Reach It

- **Never defend the product.** "Actually, that feature exists…" signals that criticism will be contested, and they'll go back to polite front-stage answers. Just note it. The fact that they didn't know it existed is itself data.
- **Reward candor with interest, not judgment.** Try "That's really helpful, can you tell me more?" or "What happened next?"
- **Listen for backstage slips.** Phrases like "honestly," "between us," "off the record," or a laugh before an answer often signal that the real story is coming. Slow down and follow up.
- **Allow silence.** People often fill a pause with the more honest version of what they just said.
- **Watch for rehearsed language.** If an adjuster uses executive phrasing like "strategic alignment" or "AI-forward platform," they're likely repeating the official story. Redirect to specifics: "What did that look like in your day-to-day?"
- **Don't bring up usage data confrontationally.** Know the account's adoption data beforehand so you can ask better questions, but don't say "our logs show you never logged in." That forces a defensive performance.

## 7. After the Interviews: Guard Against Your Own Organization's Impression Management

Candid data can still get distorted once it's inside your company.

- **Code stated reasons and behavioral evidence separately.** For each interview, record what they said the reason was and what the behavioral evidence shows (workarounds, timelines, unused features). The gap between the two is your core finding.
- **Share raw material, not only summaries.** Give both VPs access to anonymized transcripts or clips. Summaries let each side hear the parts that confirm their theory.
- **Have the synthesis done by someone neutral**, not by Product or Services, and ideally agree on the coding approach with both VPs *before* the interviews start. That way no one can dismiss inconvenient results as biased.
- **Watch your own interviewers.** Internal interviewers may soften findings that reflect badly on colleagues or leadership. That's another reason a third party helps.
- **Close the loop with interviewees.** Send a short note on what you learned and what you're changing. It builds trust and keeps the door open for follow-ups and future win-backs.

## Quick Checklist

- ☐ Neutral interviewer, no history with the account
- ☐ Former executive contact informed, not bypassed
- ☐ One-on-one, confidential, explicitly not sales
- ☐ Admit likely fault in the opening
- ☐ Behavioral, timeline, and workaround questions
- ☐ Projective questions about the team
- ☐ Official story tested gently with specifics
- ☐ Closing "advice to a peer" question
- ☐ No defending, no correcting
- ☐ Stated reasons and behavioral evidence coded separately
- ☐ Raw data shared with both VPs

**Bottom line:** Candor happens when the interview no longer requires anyone to protect their company's decision, their own competence, or your feelings. Remove those needs, and adjusters will usually tell you plainly whether they switched because of your competitor's AI, or because your system never really became part of their workday.

## Turn 3

**User:** Keeping with impression management, how do I handle the conversation with our current at-risk accounts so they'll admit adoption problems before they decide to leave?

**Assistant:**

# Surfacing Adoption Problems Before Accounts Leave: An Impression Management Playbook

With churned customers, the challenge was getting past the story they told on the way out. With current at-risk accounts, the challenge is harder. The relationship is live, the renewal is ahead, and **both sides are performing that things are fine**. You have to end that performance before they quietly decide to leave.

## 1. Why At-Risk Accounts Hide Adoption Problems

Goffman describes a "working consensus," an unspoken agreement between parties to sustain a pleasant definition of the situation. In many customer relationships, it looks like this:

- **Your CSM** wants a green health score and a smooth QBR.
- **The customer's champion** wants to look like they made a good purchase and ran a competent implementation.
- **Both sides** avoid the awkward truth, so meetings stay polite and forward-looking while adoption quietly stalls.

On top of that, each party has its own performances:

| Performance | What it sounds like | What's underneath |
|---|---|---|
| **Champion protecting the purchase** | "We're making good progress." | Admitting low adoption means admitting their project is failing and their judgment was wrong. |
| **Team competence** | "We just need a bit more time." | The claims team reverted to spreadsheets, but saying so makes their department look bad. |
| **Negotiation posture** | "Things are okay, but we're watching the market." | Admitting problems feels like it weakens their hand, or like it might trigger an upsell pitch. |
| **The quiet exit** | Polite, shorter, less frequent meetings | They've already started evaluating competitors and see no reason to show you the backstage. |
| **Politeness** | "Your team has been great." | Protecting the CSM's feelings, especially if they like them personally. |

The quiet exit is the most dangerous. By the time a customer stops performing enthusiasm and starts performing polite distance, the decision may be half-made. Your window is **before** that shift.

## 2. Before the Conversation: Prepare Backstage

**Know the real picture first.** Review adoption data before you talk to them:

- logins by role
- claims processed in-system versus total claims volume
- which modules were configured versus purchased
- integration status
- support ticket patterns
- implementation milestones missed

You won't use this data to confront them. You'll use it to ask good questions and recognize when you're getting a front-stage answer.

**Watch for signs the performance is shifting toward exit:**
- engagement drops, meetings get rescheduled, or the champion goes quiet
- new stakeholders appear, especially procurement or IT asking about data export or contract terms
- the executive sponsor stops attending
- questions about contract flexibility, term length, or termination clauses
- a sudden spike in questions about features competitors are known for

**Choose the right messenger.** If the account's CSM has been part of the "everything's fine" consensus, it can be hard for them to break it. Their own face is tied to the account's health. Consider bringing in:
- your own senior leader, which signals the conversation matters and resets the frame, or
- a "value realization" specialist who is new to the relationship.

Present this as added investment, not as replacing the CSM.

**Time it away from renewal.** Close to renewal, every admission feels like negotiation leverage or a risk. Aim for **6–12 months before renewal**, when it can be framed as a working session rather than a commercial conversation.

**Segregate your audiences.** Goffman's "audience segregation" means people perform differently for different audiences. Don't ask a champion to admit adoption problems in front of their boss. Plan separate conversations:
1. **Champion one-on-one first.** This is where the truth is most likely to come out.
2. **Users and claims managers separately.** These are the people who know about the workarounds.
3. **Executive sponsor last,** after you and the champion have agreed on a rescue plan they can present as their initiative.

## 3. Frame the Meeting So Honesty Is Safe

What you call the meeting shapes the performance.

- ❌ "Health check," "QBR," "account review." These invite a scorecard performance.
- ❌ "Renewal planning." This invites negotiation posture.
- ✅ **"Value realization review"** or **"Implementation reset session."** These signal you're there to fix something together.

**Say explicitly what the meeting is not:**
- not a sales or upsell conversation
- not a renewal negotiation
- not an evaluation of their team

Then keep those promises. Pitching new features in this meeting is especially damaging. It implies the fix is buying more, and it confirms their suspicion that honesty leads to a sales pitch.

## 4. Make Admission Face-Saving

This is the heart of it. People admit problems when admitting them doesn't cost them face. Give the champion a story that protects them.

**Take the blame first.** When you open with your company's shortcomings, their admission becomes agreement, not confession.

> "I want to start by saying I think we let you down on parts of the implementation. Looking at the timeline, we ran long, and I don't think we did enough to get your adjusters comfortable. I'd rather hear that directly from you than find out later."

**Normalize it with benchmarks.** Place their situation in a common pattern so it's about the process, not their competence.

> "Honestly, a lot of regional carriers we work with hit the same wall around month six. The integration with the policy system takes longer than planned, and adjusters end up running parallel spreadsheets. Is that anything like what you're seeing?"

**Make the problem the system's fault, not a person's.** Frame issues as structural: "our onboarding process," "the integration approach," "how the training was designed." Don't frame them as "your team didn't adopt it."

**Offer the champion a hero role.** Their biggest fear is looking like they backed a failing project. Reframe them as the person who spotted the problem and turned it around.

> "What I'd like to do is put together a plan you can take to [executive] that shows exactly how we get you to full value in the next 90 days. You'd be the one who caught this early and got it fixed."

**Give them a story they can tell upward.** Explicitly help them craft the narrative for their boss: "We identified gaps in the vendor's implementation, pushed them to invest in a reset, and now we're on track." That story protects their standing and makes honesty worth it.

## 5. Questions That Get Past "It's Going Fine"

Many of the same principles from the churn interviews apply: behavior over opinion, workarounds, projective questions.

**Behavioral and specific:**
- "Walk me through how a new claim moves through your team today. Where does our system come in, and where doesn't it?"
- "When your claims director wants a report, where does it actually come from?"

**Workaround hunting:**
- "Are there things your team still does outside the system, in spreadsheets, email, or the old tool?"
- "Which parts did you decide not to turn on, or turned on and stopped using?"

**Projective, about the team:**
- "How do your adjusters talk about the system when you're not around?"
- "What do new hires find hardest?"

**Future-back questions, which surface risk without direct confrontation:**
- "If you had to justify the renewal to your CFO tomorrow, what would be the hardest question to answer?"
- "If renewal were today, what would make it an easy yes, and what would make you hesitate?"

**Direct but safe:**
- "Is anyone at [carrier] starting to ask whether this is the right system? If so, I'd much rather know now while we can do something about it."

The last question matters. Asking directly, after you've made honesty safe, signals that you can handle the answer and won't punish them for it.

## 6. When They Open Up: Protect the Backstage

- **Don't defend or correct.** "Actually, that feature is available…" re-establishes the front stage instantly. Note it. Their not knowing is the finding.
- **Thank them for candor explicitly.** "This is exactly what I needed to hear. Thank you for being straight with me."
- **Don't escalate what they told you in confidence.** If the champion admits their team hasn't adopted it, don't then tell their executive "your team isn't using the system." That's a betrayal of the audience segregation you promised, and they'll never be candid again.
- **Respond with commitment, not analysis.** Admission needs to lead quickly to visible help. That shows honesty pays.

## 7. Turn Admission Into a Credible Rescue

An admission only helps if it leads somewhere. Make the payoff concrete:

- **A 90-day value realization plan** with specific milestones: integrations completed, workflows configured, a percentage of claims processed in-system, adjuster training completed.
- **Visible investment from your side:** dedicated implementation resources, onsite training, configuration help, possibly at no cost. This signals commitment and makes the champion look good for securing it.
- **Quick wins in the first 30 days**, such as one dashboard their claims director actually uses, or one workflow that saves adjusters time. Early wins give the champion evidence for the upward story.
- **A joint executive presentation**, where the champion presents the plan as their initiative, with your leader present to show your company's commitment.

## 8. Don't Forget Your Own Team's Impression Management

At-risk accounts often stay hidden because of performances inside your company.

- **CSMs manage impressions upward.** If a red health score reflects badly on the CSM, they'll find reasons to keep it yellow. Reward early flagging of risk, and make "I found a problem" a positive signal, not a performance failure.
- **Health scores become theater.** If they're based on CSM judgment or meeting sentiment, they measure the performance, not reality. Weight them toward behavioral data like usage, claims volume in-system, and module adoption.
- **Leadership reviews can create a green-dashboard culture.** If executives react badly to red accounts, CSMs will stop surfacing them. Model the behavior you want from customers: thank people for bad news.

## Sample Opening for a Champion One-on-One

> "Thanks for making time. I want to be upfront about why I asked for this. It's not about renewal, and I'm not here to sell you anything. Looking at how the implementation went, I think we underdelivered in some places. The timeline ran long, and I'm not sure your adjusters got the support they needed to really make the system part of their day.
>
> A lot of regional carriers hit the same wall we're probably seeing here, and the ones that get past it usually do because someone on their side flags it early. So I'd really value your honest read: where is the system working, and where are your people working around it?
>
> Whatever you tell me, my goal is to put together a plan you can take to [executive] that shows how we get you to full value. I want this to be a win you can point to."

## Quick Checklist

- ☐ Adoption data reviewed beforehand, not used confrontationally
- ☐ Right messenger, possibly someone outside the existing "all fine" consensus
- ☐ Timed 6–12 months before renewal
- ☐ Champion first, one-on-one, separate from their executive
- ☐ Framed as a value realization session, not a QBR, renewal, or sales call
- ☐ Your company takes blame first
- ☐ Situation normalized with benchmarks
- ☐ Champion given a hero narrative and an upward story
- ☐ Behavioral, workaround, and future-back questions
- ☐ No defending, correcting, or pitching
- ☐ Confidences protected
- ☐ Concrete 90-day rescue plan with visible investment
- ☐ Internal incentives reward early risk flagging

**Bottom line:** At-risk customers hide adoption problems because admitting them costs the champion face, weakens their negotiating position, or seems pointless if they're already leaving. Your job is to reverse that math. Take the blame, normalize the struggle, protect the champion in front of their boss, and turn honesty into a visible rescue that makes them look good. When admitting the problem is the champion's best move, they'll make it, and they'll make it while you can still keep the account.

## Turn 4

**User:** Still using impression management, how do I present what we learn from all this to the VP of Product and VP of Services without either of them digging in?

**Assistant:**

# Presenting the Findings Without Either VP Digging In: An Impression Management Playbook

The customers were managing impressions, and so are your VPs. Each has publicly committed to a diagnosis in front of peers, the CEO, and their own teams. People rarely abandon a public position because of evidence alone. They dig in when changing their mind would cost them face. Your job is to present findings so that **updating their view looks like leadership, not defeat**.

## 1. Why Each VP Might Dig In

Both VPs have face at stake, including the one whose theory the data supports.

**VP of Product.** If the findings show implementation is the root cause:
- Their public diagnosis looks wrong.
- Their roadmap acceleration, and the resources attached to it, is at risk.
- They may worry about looking like they were chasing shiny features while customers struggled with basics.

**VP of Services.** If the findings support their view, you might expect them to be pleased. But look closer:
- "Implementation is the problem" also means "**your team's work is driving churn**."
- Being right about the diagnosis means being responsible for the failure.
- They may get defensive about specifics, such as staffing, scoping, or customer readiness, as soon as the data gets granular.

**Both of them.**
- Neither wants to "lose" in front of the CEO or the exec team.
- Both are tied to budget and headcount outcomes.
- Both will scrutinize the method if the conclusion threatens them.

**You.** You're the messenger, and your credibility depends on looking neutral. If CS's own misses appear in the findings, as they probably will, you have face at stake too.

The most important insight: **there are no pure winners here**. That's useful, because it means you can frame this as a shared problem rather than a verdict.

## 2. Before the Meeting: Pre-Wire Privately

Goffman observed that people handle threatening information much better backstage than in front of an audience. **Never let either VP see the findings for the first time in a group setting**, especially with the CEO present.

**Hold one-on-ones with each VP first.**
- Share the findings privately, including the parts that challenge their position.
- Give them time to react, push back, and absorb it without an audience.
- Ask for their interpretation: "What do you make of this? Is there anything I'm missing?"
- Invite them to shape how the findings are presented, and incorporate reasonable input.

**Consider the order.** Generally, meet first with the VP whose position is most challenged. They need the most time and the most face protection. Meeting them first also signals respect rather than ambush.

**Surface objections early.** If a VP has a legitimate critique of the method or the sample, you want it now, not in the group meeting. If they raise an objection you can't answer, adjust the analysis or acknowledge the limitation openly in the presentation.

**Let each VP see what the other will see.** Don't tailor the substance of the findings to each audience. That undermines trust when they compare notes. Tailor the framing and emphasis, not the facts.

**Ideally, you secured their agreement earlier.** If you had both VPs agree on the diagnostic method and the questions *before* data collection, remind them of it gently: "This is the analysis we agreed on together back in [month]." It's much harder to dismiss a method you helped design.

## 3. Frame the Story So Both Positions Were Rational

This is your most powerful move. The research likely showed a gap between **stated reasons** (competitor AI and analytics) and **underlying behavior** (stalled implementations, workarounds, partial adoption). That gap is the key to saving face for both VPs.

**The frame:**

> "Both of you were seeing real signals. Customers genuinely told us they were leaving for better analytics and AI, and that's what Product heard. At the same time, most churned customers never reached full adoption, and that's what Services saw. What the research shows is how these connect: poor time-to-value made customers vulnerable, and competitor features gave them a reason to leave that was easy to justify internally."

This does several things:
- **The Product VP wasn't wrong.** They were accurately reporting what customers said. The customers were managing impressions. That's a finding about customers, not a failure of the VP's judgment.
- **The Services VP is validated without being handed a win.** The diagnosis also highlights the gaps their team needs to fix.
- **It turns the debate into a sequence.** Instead of Product versus Services, it becomes cause, then trigger. There's a role for both.

The underlying message: **the disagreement existed because the problem was hard to see**, not because either leader was careless.

## 4. Structure the Presentation to Lower Defenses

**Start with the customer's voice, not the conclusion.**
- Open with anonymized quotes and short stories from interviews, especially vivid ones about workarounds, long implementations, and competitor demos.
- Customer stories are harder to argue with than analysis, and they shift the focus from "who's right" to "what customers are going through."

**Own your team's misses first.** Before discussing Product or Services, lay out what the research showed about Customer Success:
- health scores that masked risk
- early warning signs missed
- champions not engaged early enough

This models the behavior you want. When you go first, it becomes much easier for the others to acknowledge their parts without losing face.

**Show data before conclusions.** Walk through the evidence step by step:
1. churn rates by implementation length and adoption depth
2. the gap between stated reasons and behavioral evidence
3. how healthy, well-adopted customers churned, and why
4. timeline correlation with competitor launches versus implementation delays

Let them reach the conclusion alongside you. People defend conclusions they're handed, and they accept conclusions they reach themselves.

**Present findings as "what we learned," not "who was right."**
- ❌ "The data shows Services was right."
- ✅ "The data shows implementation and time-to-value are the biggest driver, with product gaps acting as the trigger in many cases."

**Include the parts that support each side.** There will almost certainly be product findings, even if implementation is the bigger issue. Examples:
- well-adopted customers who left for specific missing capabilities
- product complexity that made implementations harder
- analytics features customers couldn't find or configure

Give these genuine weight. It keeps the Product VP engaged, and it's also true.

**End with the joint plan, not the diagnosis.** Spend most of the meeting on what happens next. The diagnosis should feel like a stepping stone, not the headline.

## 5. Language That Keeps People Engaged

| Instead of… | Say… |
|---|---|
| "You were wrong about…" | "What customers told us on the way out didn't always match what their usage showed." |
| "Implementation is failing." | "Our implementation approach isn't consistently getting regional carriers to value." |
| "Services is driving churn." | "Time-to-value is the biggest predictor of churn, and it's something all our teams touch." |
| "Product was chasing the wrong thing." | "The product gaps are real, but they matter most once customers are fully adopted." |
| "The data proves…" | "The data strongly suggests…" (leave room to refine) |
| "Here's what we need to do." | "Here's a proposal. I'd like both of your input to make it work." |

Two principles run through this language:
1. **Make problems structural, not personal.** Talk about processes, not teams or people.
2. **Leave room for revision.** Conclusions framed as final invite a fight. Conclusions framed as strong but refinable invite collaboration.

## 6. Give Each VP a Role and a Win

People dig in when they see only loss. Make sure each VP walks out with something they can present to their team and the CEO as progress.

**For the VP of Services:**
- Ownership of the implementation reset and time-to-value goals.
- Investment to fix onboarding, possibly including headcount, tooling, and training resources.
- The narrative: "We identified the root cause and are leading the fix."

**For the VP of Product:**
- Ownership of **features that accelerate time-to-value**, such as out-of-the-box dashboards, easier configuration, simpler integrations, and faster setup of AI features.
- A clear mandate to address the specific product gaps that healthy customers leave over.
- The narrative: "We're building the capabilities that help customers adopt faster and stay competitive."

This matters because Product's work is now part of the solution to the churn problem, not the losing side of the debate. Framing AI and analytics features as time-to-value accelerators lets the Product VP keep much of their roadmap ambition while aligning it with the diagnosis.

**A shared metric.** Propose a joint goal that both VPs own, such as:
- percentage of new customers reaching defined value within six months
- gross or net revenue retention
- adoption depth at month six

A shared metric changes the relationship from competing explanations to a common target. It also removes the incentive for either VP to explain future churn in their team's favor.

## 7. Handling Pushback in the Meeting

Even with pre-wiring, you may get resistance. How you respond determines whether people dig in further.

**Don't argue.** Arguing in front of an audience forces the other person to defend their position to save face. Respond with curiosity and data.

**Acknowledge and redirect to evidence:**
> "That's a fair point. Here's what the data showed on that specifically…"

**Offer a test instead of a debate:**
> "I think that's worth testing. Could we look at [specific cohort or metric] together over the next two weeks?"

This gives the objecting VP a way to keep their view while still moving forward. It also means the next update comes from data they helped examine.

**Give people an exit line.** Goffman called this "tact": helping others save face when their performance falters. If a VP has backed themselves into a corner, give them a graceful way out:
> "Given what we knew at the time, that was a reasonable read. The interviews gave us information we just didn't have before."

"New information" is the most face-saving reason to change your mind. It suggests their earlier view was sound given the evidence then available.

**Take heated disagreements offline.** If a discussion becomes a public standoff:
> "I want to make sure we get this right. Can we dig into this together after the meeting?"

Then resolve it in a one-on-one, where neither side has an audience to perform for.

## 8. If the Findings Don't Match Your Earlier Bet

In the first conversation, I suggested implementation was likely the root cause. If the research shows something different, such as significant churn among well-adopted customers leaving for product capabilities, the same approach applies in reverse:

- Pre-wire the Services VP first, since their position is now most challenged.
- Use the same frame: both saw real signals, and the research shows how they connect.
- Give Services ownership of what does matter, such as implementation speed as a competitive advantage and faster time-to-value for new features.

Also, **be willing to update your own position visibly**. If you proposed an early hypothesis and the data disagrees, saying so openly builds your credibility as a neutral broker. It also makes it easier for the VPs to update theirs.

## 9. After the Meeting: Manage Attribution

How the story gets told afterward matters as much as the meeting itself.

- **Let each VP present their part of the plan to the CEO or exec team.** Ownership in front of senior leaders turns the plan into their initiative, not something imposed on them.
- **Credit both VPs publicly** for the insight: "This came out of Product and Services both pushing us to look harder at churn."
- **Share early wins in a way that credits both teams.** When time-to-value improves, highlight the Services process changes and the Product features that helped.
- **Follow up individually.** Check in with each VP a week later. Any lingering resistance usually comes out in private, and it's easier to resolve there.

## Sample Opening for the Joint Meeting

> "Thanks, both of you. I want to start by saying this research exists because the two of you pushed us to take churn seriously from different angles, and both angles turned out to matter.
>
> I'll also start with what we got wrong in Customer Success. Our health scores missed a lot of the risk, and we didn't catch stalled adoption early enough. That's on us, and we're fixing it.
>
> What I'd like to do is walk through what customers told us, what their usage actually showed, and how those two things connect. Then I'd like most of our time to go toward a joint plan. I think there's a clear role for both Product and Services, and I'd like your input to shape it."

## Quick Checklist

- ☐ One-on-ones with each VP before the group meeting
- ☐ Most-challenged VP briefed first
- ☐ Same facts shared with both; framing tailored, not substance
- ☐ Reference the method they agreed on earlier
- ☐ Frame: stated reasons versus underlying behavior, so both positions were rational
- ☐ Open with customer voices, not conclusions
- ☐ Own CS's misses first
- ☐ Data before conclusions; let them reach the conclusion with you
- ☐ Include genuine findings that support each side
- ☐ Structural, not personal, language
- ☐ A clear role and win for each VP
- ☐ A shared metric both VPs own
- ☐ Pushback met with curiosity, tests, and exit lines, not argument
- ☐ Heated disagreements taken offline
- ☐ Credit shared publicly afterward
- ☐ Individual follow-ups a week later

**Bottom line:** Your VPs will dig in if the presentation feels like a verdict delivered in front of an audience. They'll engage if it feels like shared discovery, where both of them were seeing real signals, the problem was genuinely hard to see, and each has a meaningful role in fixing it. Pre-wire privately, frame the findings so no one was foolish, own your own misses first, and give each leader a win they can take to their team. When changing their mind makes them look like the leader who solved churn rather than the one who lost an argument, they'll change it.

## Turn 5

**User:** What should we do?

**Assistant:**

# What You Should Do

**Stop treating this as a debate about which VP is right. Run a short, jointly owned diagnostic, start rescuing at-risk accounts now, and commit budget based on what the evidence shows.** My bet remains that poor time-to-value is the root cause and product gaps are the trigger customers cite. But you don't need to win that argument today, and you shouldn't try.

Here's the plan, sequenced.

## Weeks 0–2: Set Up So the Answer Will Be Accepted

The biggest risk isn't getting the diagnosis wrong. It's getting it right and having one VP reject it. Do this first:

1. **Propose the diagnostic to both VPs in one-on-ones**, framed as "let's settle this with evidence we both trust."
2. **Agree on the method and decision rules up front**, in writing. For example:
   - If churn is concentrated among long or stalled implementations and low adoption, the priority is time-to-value.
   - If well-adopted customers are leaving for specific capabilities, the priority is those product gaps.
   - If it's both, we sequence, and here's how.
3. **Agree on a shared metric** both VPs will own. A good choice is the percentage of customers reaching defined value by month six, alongside gross revenue retention.
4. **Get CEO sponsorship** for a 6–8 week diagnostic window. Say plainly that major roadmap reprioritization and big services investments wait for the results. Normal work continues.

## Weeks 1–8: Diagnose and Stop the Bleeding in Parallel

**Track A: Diagnostic (owned by you, with a neutral analyst or outside firm)**
- **Cohort analysis:** churn by implementation length, time-to-go-live, adoption depth at month six, modules configured versus purchased, and integration status.
- **Timeline check:** what changed 18 months ago? Look at competitor launches, implementation backlog, staffing or turnover, customer mix, and pricing.
- **Churn interviews:** 12–20 conversations with adjusters, claims managers, and IT leads at churned carriers, run by a neutral interviewer. Code stated reasons and behavioral evidence separately.

**Track B: At-risk account rescue (owned by CS, supported by Services)**
Don't wait for the diagnosis to act on accounts that are slipping.
- Rebuild your health score around **behavior**: claims processed in-system, usage by role, and configured modules. CSM sentiment shouldn't drive it.
- Identify the at-risk accounts, prioritizing those 6–12 months from renewal.
- Run **value realization sessions** with champions one-on-one. Take the blame first, normalize the struggle, and give the champion a rescue plan they can present upward as their win.
- Offer **visible investment**, such as implementation help, training, and configuration support, with 30-day quick wins.

Track B also feeds Track A. What at-risk accounts tell you is live diagnostic data.

**No-regret moves to start immediately:**
- Set a time-to-first-value target for every new implementation, and track it weekly.
- Reward CSMs for flagging risk early, not for green dashboards.
- Ask Product to scope two or three features that would **shorten implementation**, such as out-of-the-box claims dashboards, simpler integration with policy-admin systems, and guided configuration. These are valuable under either theory.

## Weeks 8–10: Present and Decide

- **Pre-wire each VP privately**, starting with whoever's position is most challenged.
- In the joint meeting, frame it as **stated reasons versus underlying behavior**. Both VPs were seeing real signals, and the research shows how they connect.
- **Own CS's misses first.**
- Spend most of the time on the **joint plan**, not the verdict.
- Apply the decision rules you agreed on in week one. This is where that earlier work pays off.

## Months 3–6: Execute

If the findings match my expectation, the plan looks like this:

| Workstream | Owner | What it covers |
|---|---|---|
| **Implementation reset** | VP Services | Shorter, phased implementations; a standard integration playbook for regional carriers; adjuster training; hard time-to-value milestones |
| **Time-to-value features** | VP Product | Faster setup, out-of-the-box analytics, easier integrations, AI features that deliver value in weeks rather than months |
| **Targeted product gaps** | VP Product | Only the specific capabilities that *well-adopted* customers leave over |
| **Early warning and rescue** | CS (you) | Behavioral health scores, proactive value reviews, at-risk playbook |
| **Shared scorecard** | All three | Month-six value attainment, gross revenue retention, adoption depth, reviewed monthly with the CEO |

**Leading indicators to watch:**
- median time-to-go-live
- percentage of claims processed in-system at month six
- number of at-risk accounts moved back to healthy
- whether renewals among rescued accounts actually close

**Lagging indicator:** annual churn returning toward its level from 18 months ago within 12–18 months. Contracts renew on annual cycles, so the churn number will move last.

## If the Findings Surprise You

If the diagnostic shows well-adopted customers leaving for competitor capabilities in large numbers, shift the weighting. Accelerate the specific product gaps and keep implementation improvements as a supporting workstream. Say openly that the data changed your view. That builds your credibility and makes it easier for everyone else to follow the evidence.

## The Short Version

1. **Don't pick a side.** Get both VPs to agree on how you'll decide before you gather evidence.
2. **Diagnose with behavior, not stated reasons.** Customers leaving will cite features because it's the face-saving explanation.
3. **Rescue at-risk accounts now**, making it safe for champions to admit adoption problems.
4. **Present findings so no one loses face**, and give each VP a role in the fix.
5. **Most likely outcome:** fix time-to-value first, and point Product at features that speed adoption plus the few gaps healthy customers actually leave over.

Handled this way, you'll end up with the right diagnosis, both VPs aligned behind it, and a better chance of keeping the at-risk accounts you're about to lose.

## Outcome summary (sent to Jev)

The assistant recommends not picking a side between the two VPs. Instead, run a short, jointly owned diagnostic, start rescuing at-risk accounts immediately, and commit major budget only after the evidence is in. Its bet is that poor time-to-value is the root cause and competitor product gaps are the trigger customers cite. Departing buyers favor "better AI and analytics" because it saves face, while admitting a failed implementation implicates them. Each VP's diagnosis is also partly a budget bid for their own team.

In the first two weeks, meet each VP one-on-one to agree in writing on the method and decision rules. Adopt a shared metric, such as the percentage of customers reaching defined value by month six plus gross revenue retention. Get CEO sponsorship for a 6–8 week window during which major reprioritization waits.

In parallel, run two tracks:
- **Diagnostic:** a neutral analyst runs cohort analysis of churn by implementation length and adoption depth, checks what changed 18 months ago, and conducts 12–20 neutral interviews with adjusters and claims staff, coding stated reasons separately from behavioral evidence.
- **Rescue:** rebuild health scores around behavior and hold face-saving value-realization sessions with at-risk champions, backed by visible investment.

Several steps are worth taking regardless of the diagnosis: set time-to-first-value targets, reward early risk flagging, and have Product scope features that shorten implementation.

When the findings are ready, pre-wire each VP privately and frame the results as stated reasons versus underlying behavior. CS should own its misses first. Then assign owners for an implementation reset, time-to-value features, targeted gaps that well-adopted customers leave over, and early warning.

The main caveats are that churn will move last, over 12–18 months, and that if well-adopted customers are leaving for competitor capabilities, the weighting should shift toward product and that change of view should be stated openly.
