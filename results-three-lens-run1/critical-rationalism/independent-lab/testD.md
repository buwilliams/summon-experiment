# critical-rationalism/independent-lab/testD

Model: claude-opus-5-5 · 2026-09-24T14:44:58.540230+00:00

## Turn 1

**User:** I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

I don't need certainty; I want the most reasonable explanation we can act on now and correct as we learn. Treat each belief as a conjecture: what does each one claim is going on, and why? Whose values and goals is each one built around, and are they the ones that matter most here? What might both be leaving out that could change the outcome? Which assumption is most worth checking first, and what is a quick way to check it? And is there a better explanation that fits the same facts than either one?

**Assistant:**

# Two Conjectures About Turning the Ship Around

## 1. What each belief claims

**The CEO's conjecture: "Work within existing systems, procedures, and talent."**
- **Claim:** The organization has the raw capability. The problem is focus, direction, or execution. Point the existing machine at the right targets and it will deliver.
- **Why he might believe it:** He knows the people and their tacit knowledge. Insurance software is deeply integrated, regulated, and relationship-driven, so the institutional knowledge in the core is a real asset. Reorganizing is expensive and distracting. And the revenue, customers, and implementation capacity all live in the core.
- **Hidden premise:** The current system *can* produce different outputs if given different inputs. The obstacles are strategic, not structural.

**Your conjecture: "Build an independent innovation lab."**
- **Claim:** The core has an immune system (approval layers, release cycles, risk aversion, quarterly incentives, legacy architecture) that will slow or kill anything new. Only separation lets new ideas survive long enough to prove themselves.
- **Why you might believe it:** There's solid precedent: Christensen's disruption work, Lockheed's Skunk Works, many corporate venture arms. You've probably seen good ideas die in committee.
- **Hidden premise:** The main problem is a *lack of new things*, and new things built outside can later be absorbed back in.

## 2. Whose values and goals each is built around

| | CEO's view | Your view |
|---|---|---|
| **Centers** | Existing employees, stability, the board's appetite for risk, his own track record (he built or inherited this org) | Speed, autonomy, the innovator's freedom, and your own mandate to deliver "outsized results" |
| **Protects against** | Disruption, cost, a two-class culture | Bureaucratic drag, dilution, slow death by process |
| **Underweights** | Whether the current system is itself the cause | Whether the core can absorb what the lab builds |

**Who matters most here is largely absent from both: the customers.** That means the insurers who are leaving or not buying, and behind them their policyholders, agents, and underwriters. Both conjectures are arguments about *internal structure*. Neither starts from *why customers are walking away*. Both are also partly shaped by self-interest. The CEO's view protects the org he's responsible for. Yours gives you the most control over the outcome you'll be judged on. That doesn't make either wrong, but it's worth noticing.

## 3. What both might be leaving out

1. **The actual cause of churn and lost deals.** If customers leave because of painful implementations, slow configuration changes, outages, poor support, a missing cloud or SaaS option, or pricing, then an innovation lab building novel products won't fix it. Neither will "doing the same things harder." You need to know the failure mode before choosing the structure.
2. **The time horizon.** Labs typically need 18 to 36 months to produce something that moves revenue. Churn is happening now. What's the financial runway, and what does the board expect in 12 months?
3. **The transfer problem.** The most common failure of corporate innovation labs is not that they fail to invent. It's that the core can't adopt, sell, implement, or support what they invent. The lab becomes "innovation theater": demos, awards, no revenue. In insurance software, where everything must integrate with policy, billing, and claims systems and pass carrier security and compliance reviews, this risk is especially high.
4. **Your political position.** You're new, and you'd be opening with a proposal that contradicts the CEO's stated belief. Labs perceived as elite and separate also tend to get defunded in the first budget crunch. Structure is partly a question of who will defend it when things get hard.
5. **What the CEO actually means.** "Work within existing systems" might mean "don't spend a lot," "don't insult my people," or "I've seen labs fail before." Each implies something different about what he'd accept.
6. **Whether competitors win on innovation at all.** Your rivals may be winning on cloud-native architecture, faster time to value, or better partner ecosystems. Those are delivery-model advantages, not necessarily "innovations" a lab would produce.

## 4. The assumption most worth checking first

**Assumption:** Customers are leaving, and prospects aren't buying, because the company isn't producing new capabilities fast enough.

Both strategies quietly depend on this. If it's false, the whole structure debate is premature.

**A quick check you can do in two to three weeks:**
- Pull the last 10 to 20 churned accounts and 10 to 20 lost deals. Look at whatever win/loss or CRM notes exist.
- Interview 5 to 8 people: a few churned customers or lost prospects if you can reach them, plus 2 or 3 sales reps and 2 or 3 customer success or implementation leads.
- Tag each loss by primary reason:
  - capability gap
  - legacy tech / no cloud
  - implementation cost and time
  - service and reliability
  - price
  - relationship
- **Interpretation:**
  - Mostly **capability or architecture gaps**: new building is needed, which favors a protected team.
  - Mostly **implementation, service, or reliability**: the problem is the core's operating system, which favors fixing the core, though maybe with lab-style methods.
  - **A mix**: likely the answer below.

**A second, cheap check: does the immune system actually kill things?**
- Find 2 or 3 past initiatives that died and ask what killed them. Was it budget, architecture review, release cadence, sales compensation, or security approval?
- Or run a live probe: pick one real customer problem, form a small team inside the org with explicit CEO air cover, and log every blocker for six weeks.

The blockers tell you *exactly* what needs to be separated, which is almost never "everything."

## 5. A better explanation that fits the same facts

**The company is losing because its core offering fails customers on specific, identifiable dimensions, and its delivery system (processes, permissions, incentives, architecture), not its talent, is too slow to respond. Both of you are half right.**

- The CEO is right that the fix must reach the core. That's where the revenue, customers, and churn are. You cannot lab your way out of a retention problem in the installed base.
- You're right that the existing processes will throttle new work if it's forced through them unchanged.

**The implication: separate the *rules*, not the *organization*.** This follows O'Reilly and Tushman's "ambidextrous organization" research. Exploratory units work best when they're operationally distinct but strategically integrated, with a senior leader connecting them to the core.

In practice:
- **Small, protected teams working on problems drawn from the churn and loss data.** Each team would be tied to a real customer and to a core executive who owns adoption.
- **Targeted exemptions only.** For example, the team gets its own release path, lightweight approvals, and dedicated engineers, while security, compliance, and integration standards stay intact.
- **Scaling paths designed from day one.** Decide upfront who will sell, implement, and support it if it works.
- **Measured by retention and wins, not demos or patents.**
- **Staffed partly with respected insiders.** This spreads the methods and neutralizes the "elite lab" resentment. It's also true to the CEO's belief in existing talent, which makes it far easier to get his support.

This framing also lets you *agree* with the CEO rather than oppose him: "You're right that our people and our core are the path. I want to change how a few teams work so they can move at the speed customers need."

## 6. What would change your mind

- **If the churn analysis shows a fundamental architecture gap** (for example, customers demanding cloud-native SaaS the core can't become), a truly separate unit building a new platform becomes much more defensible. That's the classic disruption case.
- **If the six-week probe shows blockers are few and fixable,** lean further toward the CEO's view.
- **If the CEO won't grant even targeted exemptions,** that's crucial information about whether "outsized results" is achievable in this role at all.

## A 90-day sketch

- **Weeks 1–3:** Churn and loss analysis. Clarify privately with the CEO what "outsized results" means to him and what he fears about labs.
- **Weeks 3–4:** Present findings with the CEO before anyone else, framed as customer truth rather than a structural argument.
- **Weeks 4–10:** Launch 1 or 2 protected teams on the biggest loss drivers, logging every blocker.
- **Weeks 10–12:** Review results and the blocker log. Decide how much more separation is needed based on evidence rather than conviction.

This gets you acting now and learning fast. It also keeps the most important question in front of everyone: not "lab or no lab," but "why are customers leaving, and what's the fastest way to stop it?"

## Turn 2

**User:** If the churn data shows customers are leaving over implementation and service rather than missing innovation, is fixing that still my mandate, or will I be stepping on other executives' turf without their buy-in?

**Assistant:**

# Is Fixing Implementation and Service Your Mandate?

Short answer: **the problem is part of your mandate, but the fix mostly isn't yours to own.** Your job is to help the company stop losing. It isn't to take over service delivery. How you handle that line will shape your credibility for the rest of your tenure.

## 1. Reread your mandate

The CEO hired you to "lead innovation and produce outsized results." The results are the point, and innovation is the means. If the data shows innovation in the narrow sense (new products, new features) won't move retention, then **telling him so clearly is itself one of the most valuable things you can deliver.** Most executives protect their function's relevance. You'd be showing you care more about the company's outcome than your own scope. That buys trust you'll need later.

But "the problem is my concern" is different from "the problem is mine to run." Implementation and service almost certainly belong to someone: a COO, a head of professional services, a head of customer success. They have teams, budgets, and accountability. If you walk in with a fix, you create two problems:
- **Authority without accountability:** you're shaping outcomes they'll be judged on.
- **Accountability without authority:** if the CEO then hands you the problem, you're on the hook for results delivered by teams that don't report to you.

## 2. Look for where the service problem starts upstream

Implementation and service pain in enterprise insurance software often *isn't* purely a services failure. It's frequently a symptom of product and architecture choices:
- Configuration requires custom code instead of business-user tooling.
- Data migration from legacy systems is manual and bespoke every time.
- Integrations with rating engines, document systems, and third-party data are one-off builds.
- Upgrades are so painful that customers stay on old versions and accumulate problems.
- There's no sandbox or testing tooling, so every change is risky and slow.
- Support is reactive because there's little telemetry or self-service diagnostics.

**If the root causes sit here, fixing them is squarely innovation territory.** Examples include accelerators, migration tooling, low-code configuration, reusable integration kits, and upgrade automation. You'd be working *for* the services organization, removing the product debt that makes their job hard, not taking it over.

So when you do the churn analysis, go one level deeper. For each implementation or service complaint, ask: *is this a people and process problem, or is the product making this hard?* That split tells you where you lead and where you support.

## 3. How to avoid a turf war

**Talk to the affected executives before the CEO sees the analysis.** Nothing damages peer relationships faster than a new hire presenting data to the boss that makes colleagues look bad. Walk each relevant executive through what you found privately, and frame it as "here's what customers are saying; help me understand it." Don't frame it as "here's what's broken in your area."

**Assume they already know, and ask why it hasn't been fixed.** Usually they do know. The real questions are:
- What's stopped this from getting fixed? Headcount, product constraints, competing priorities, a past attempt that failed?
- What would you do with more capacity or different tools?
- What part of this is caused by things outside your control?

Their answers will often point directly at the upstream product issues, where you can help.

**Offer capacity, not critique.** Your pitch is: "I have a mandate and some resources to try new approaches. I'd like to point some of that at the problems making your job harder. You own the outcome. I'll bring a team and methods." Most operators welcome help that makes them more successful and doesn't threaten their control.

**Then go to the CEO together if possible.** "The head of services and I looked at churn together, and here's what we propose" is far stronger than a solo presentation. It also shows the CEO you can work within the organization, which matters given his stated belief.

## 4. Get explicit clarity from the CEO

Don't let scope drift quietly. Once the data is in, have a direct conversation. You might say: "The churn data points mostly at implementation and service. That isn't what I was hired for. Here's how I think my role can contribute, and here's what I think the service owners should lead. Does that match what you want?"

He may answer in one of three ways:
- **"Yes, support them."** Clean. You become an enabler, with a portfolio aimed at upstream causes.
- **"No, I want you to fix it."** Then you need matching authority: a joint mandate, dotted-line influence, or a clearly scoped initiative with named owners. Don't accept the accountability without it.
- **"Stay focused on new products; service is someone else's job."** That's worth knowing too. Say plainly that new products alone likely won't stop the churn, so the risk is on record. Then look for innovation bets that reduce implementation burden anyway.

## 5. When to push harder

Deference has limits. If the service owners deny the data, block access, or resist any change, and churn keeps rising, you have an obligation to escalate. Do it with evidence and after genuinely trying to partner. The company's survival outranks everyone's comfort, including yours. But start from the assumption that your peers want to win too. Most of the time that assumption is correct, and it gets you much further than starting from suspicion.

## In short

- **Your mandate** is to help the company stop losing customers and start winning.
- **Your role** is to diagnose, surface the truth, fix the product-side causes, and lend capacity and methods to the owners of service and implementation.
- **Your method** is to share findings privately with peers first, ask before prescribing, propose jointly, and clarify scope explicitly with the CEO.

Done this way, a finding that seems to shrink your mandate can end up expanding your influence, because you'll be seen as the person who solves the company's real problem rather than the one guarding a function.

## Turn 3

**User:** What if the implementation pain actually starts with sales, where reps overpromise custom work to hit quota, so the real fix runs through compensation plans the CEO himself signed off on?

**Assistant:**

# When the Root Cause Runs Through Sales Comp and the CEO

This is the most consequential version of the problem so far. It moves from "which department fixes this" to "the system the CEO designed is producing the outcome he's trying to fix." Handled well, it's also your biggest opportunity to show the value of an outsider.

## 1. First, test the conjecture

"Reps overpromise to hit quota" is a plausible story, but there's a competing explanation that fits the same facts: **reps promise custom work because the product can't win deals without it.** If competitors offer capabilities out of the box that your product lacks, reps fill the gap with promises, and quota pressure just amplifies it.

The two stories call for different fixes:
- **If it's mainly comp:** change incentives and add deal guardrails.
- **If it's mainly product gaps:** comp changes alone will cut overpromising, but they'll also cut wins. Reps will lose the deals they currently save with custom promises. The real fix is closing the most-promised gaps in the product, which is squarely your territory.

Most likely it's both. The proportion matters.

**Quick checks, in about two weeks:**
- Pull the last 20 to 30 closed deals. Tag each by how much custom scope was promised and what it was.
- Compare against implementation outcomes: overruns, delays, margin, and early churn or escalations. Does custom scope predict pain?
- Look for patterns in *what* gets promised. If the same five customizations show up repeatedly, that's a product roadmap, not a sales discipline problem.
- Check timing. Do custom-heavy deals cluster at quarter-end or when reps are behind quota? That points strongly at comp.
- Talk to sales engineers and implementation leads. They usually know exactly which deals were oversold and why.
- Talk to a few reps too, without judgment: "What do you have to promise to win? What happens if you don't?"

## 2. Understand why the plan exists

The CEO didn't sign off on a plan designed to cause churn. It probably rewarded bookings or contract value because that's what the company, the board, or investors needed at the time. Reps are behaving rationally inside that system.

That framing matters for both accuracy and tone. The plan is likely working exactly as designed. **It was designed to optimize for a different problem than the one you now have.** Nobody has to be wrong for it to need changing.

## 3. Build the case in money, not blame

Before you raise this with anyone senior, quantify it:
- **Implementation cost overruns** on custom-heavy deals versus standard ones
- **Delivery margin** lost to custom work that was sold at standard prices
- **Time to go-live** and its effect on revenue recognition, if relevant
- **Churn and escalation rates** by deal type
- **Lifetime value** of oversold deals versus clean ones

If oversold deals book big and then churn in year two, the comp plan may be paying reps for revenue that never fully materializes. That's a financial argument a CEO and CFO can act on without anyone admitting fault.

## 4. Sequence the conversations carefully

The same principle applies as before, with higher stakes: **no one should be surprised in front of the CEO, especially the CEO.**

1. **Head of sales (CRO or equivalent).** This is their plan to run, and they may already feel the problem. Their reps take the blame when implementations blow up. Frame it as a shared question: "The data suggests custom promises are driving implementation pain and churn. How do you see it? What pressure are your reps under?" If they co-own the proposal, it becomes a sales-led improvement instead of an attack on sales.
2. **CFO.** They care about margin and revenue quality, and they probably helped model the comp plan. They're a natural ally, and their numbers will be more credible than yours.
3. **Services or implementation lead.** They live with the consequences and will strongly support the data.
4. **The CEO, ideally with the CRO beside you.** "Sales and I looked at this together" changes the conversation entirely.

## 5. How to raise it with the CEO

- **Lead with the customer and the money, not the comp plan.** Start from churn and its financial cost, show the link to custom promises, and let the comp connection emerge from the evidence.
- **Give him an easy way to change course.** "The plan did what it was built to do. Our problem has changed, and the plan hasn't caught up" lets him update without admitting a mistake.
- **Bring a small, reversible first step,** not a demand to overhaul compensation.
- **Treat his response as data.** This is the clearest test of his original belief. Can the company turn around within existing systems? Only if leadership will change the systems it owns. If he engages, that's a strong sign the turnaround can work from inside. If he won't touch a plan he signed, you've learned something important about where the real constraint sits.

## 6. Fixes that don't require blowing up comp

Abrupt mid-year comp changes can drive away your best reps and damage the pipeline. Start with guardrails that work now, and save structural changes for the next plan cycle.

**Immediate guardrails:**
- **Deal desk or scope review:** any custom commitment above a set threshold needs sign-off from implementation or product before contract.
- **Sales engineer or implementation sign-off** on statements of work for complex deals.
- **Priced custom work:** customizations get estimated and charged, not given away to close the deal.
- **Standard packages:** preconfigured offerings reps can sell confidently without inventing scope.

**Next comp cycle:**
- Pay part of commission at go-live or first renewal, not just at signing.
- Add implementation margin or customer health to the plan.
- Include clawbacks or reduced credit for deals that churn early.
- Reward multi-year retention, not just new bookings.

**Your contribution as innovation lead:**
- Productize the most frequently promised customizations, so reps can promise them honestly.
- Build configuration tools and accelerators that turn "custom" into "configured."
- Give sales demo and sandbox tools that show real capability, reducing the need to promise what doesn't exist.

This last category is what keeps you from being only the messenger. You're not just saying "sales is overselling." You're making it possible for them to win without overselling.

## 7. Your personal risk

You're new, and this touches the CEO's decisions, the CRO's team, and people's paychecks. Reduce the risk by:
- Being very confident in the data before you share it
- Keeping early conversations private and exploratory
- Framing everything as a system problem, never as individual failure
- Making sure peers get credit for any fix
- Proposing steps small enough that saying yes is easy

But don't bury it. If the evidence is solid and the root cause runs through comp, then fixing implementation or service without addressing it treats symptoms while the cause keeps generating new ones. A CEO who hired someone to "produce outsized results" needs to hear this, and you may be one of the few people positioned to say it. Insiders often see the problem but can't raise it because of history or dependence on the plan.

## In short

- **Verify first.** Separate comp-driven overpromising from product gaps that force reps to promise custom work.
- **Quantify it** in margin, churn, and lifetime value.
- **Build allies** with the CRO and CFO before the CEO conversation.
- **Frame the plan** as designed for yesterday's problem, and give the CEO room to update.
- **Pair it** with guardrails now, comp changes next cycle, and product work that removes the need to oversell.

If you do this well, you'll have shown that "working within existing systems" and "changing them" aren't opposites. The existing talent can deliver once the incentives stop working against them.

## Turn 4

**User:** What if the bookings-heavy comp plan exists because the board or investors reward the CEO on bookings growth, so the real constraint sits above him?

**Assistant:**

# When the Constraint Sits Above the CEO

This question follows a pattern worth naming. Each layer you examine reveals a deeper cause: service, then sales, then comp, now the board. That's good diagnostic work, but it has a trap. **There's always a constraint above the one you can touch.** Investors answer to their limited partners, and public companies answer to analysts. At some point you have to act at the level you can influence and make the problem visible to the level above. You can't wait for the root cause to be fixed before doing anything.

With that in mind, here's how to think about this layer.

## 1. Test the conjecture first

"The board rewards bookings, so the CEO has no choice" might be true. Three alternatives also fit the same facts:
- **The CEO assumes the board wants bookings** because that's what it cared about in the past, but board priorities have shifted.
- **The board already sees the churn and is worried,** and the CEO hasn't connected it to the comp plan.
- **The board rewards bookings, but would reward retention just as readily** if the story and numbers were put in front of it.

**Quick checks:**
- **Who owns the company?** This matters more than anything else.
  - A private equity owner with an exit in two years has different incentives than a long-horizon investor.
  - A public company answers to analyst metrics.
  - A founder-controlled company may have more flexibility than it appears.
- **What's in the board deck?** Ask the CFO which metrics get reported and discussed. If net revenue retention, gross retention, or cohort churn appear, the board already cares. If only bookings and pipeline appear, the lens is narrow.
- **How is the CEO paid?** The CFO or head of HR likely knows, at least in outline. Bookings targets, revenue targets, EBITDA, or exit value each create different pressures.
- **What has the board said recently?** Ask the CEO directly and neutrally: "What does the board focus on most? What worries them?" His answer tells you both their priorities and his perception of them.

## 2. Find where the board's interests already align with fixing churn

Even a bookings-focused board has a stake in retention, whether or not it has noticed yet:
- **Churn eventually erodes revenue.** Bookings that walk out the door in year two don't compound. At some point the board will see revenue growth stall despite strong bookings.
- **Buyers and investors scrutinize retention.** In any sale or fundraise, diligence teams examine cohort retention and net revenue retention closely. Software companies with poor retention often sell at meaningfully lower valuations than those with strong retention, because retained revenue compounds. For a PE owner planning an exit, this is a direct hit to their return.
- **Implementation overruns hurt margin,** which matters to anyone valuing the company on profitability.

So the pitch upward isn't "stop caring about bookings." It's **"our bookings are lower quality than they look, and that will cost you at exit."** Framed that way, fixing churn protects the board's goals rather than competing with them.

## 3. Be honest about the case where the conflict is real

Sometimes the incentives above genuinely conflict with the company's long-term health. For example, an owner planning to exit within 18 months may rationally prefer booked growth now, even if churn will hurt the next owner. If that's the situation, no amount of analysis will change it, because the board's goal isn't what you assumed.

It's worth knowing early, because it changes your strategy:
- **Short-horizon owner:** focus on fixes that improve retention *without* reducing bookings. Your work should make the company look better in diligence soon, such as improving implementation success on new deals and stabilizing at-risk accounts.
- **Long-horizon owner:** there's room for deeper changes to comp and product strategy.

It also raises a personal question, discussed below.

## 4. Your role: equip the CEO, don't go around him

**Don't go to the board yourself.** Bypassing the CEO would break his trust and very likely end your tenure, even if you're right. The board relationship is his.

What you can do is make it easier for him to change the story upward:
- **Build the analysis through the CFO.** Show retention by cohort, lifetime value of oversold versus clean deals, implementation margin, and a projection of what current churn does to revenue in two to three years. The CFO's numbers carry weight with boards.
- **Propose adding retention metrics to board reporting,** such as net revenue retention, gross retention, and implementation success rate. Once the board sees them regularly, incentives tend to follow.
- **Help frame a "quality growth" narrative:** "We're shifting from bookings volume to bookings that stick, and here's the evidence it will increase enterprise value."
- **Offer early wins he can show,** such as a few rescued at-risk accounts or a cleaner implementation cohort, so he's bringing results rather than just a theory.

## 5. Look for moves that don't threaten bookings

Several fixes from earlier reduce churn without cutting reported bookings. Some even increase them:
- **Priced custom work** turns giveaways into revenue.
- **Productized customizations** let reps close deals honestly, without losing them.
- **Standard packages** can shorten sales cycles.
- **Implementation accelerators** cut delivery cost without touching the sales motion.
- **At-risk account rescue** protects existing revenue directly.

These give the CEO room to improve retention now, before any board-level conversation. They build the evidence that makes that conversation easier.

## 6. The personal question

At this point you're effectively asking whether the job is winnable. Signals to watch over your first few months:

**Encouraging:**
- The CEO engages with the retention data rather than deflecting.
- The CFO is willing to put retention metrics in front of the board.
- The board, when shown the numbers, asks good questions.
- Small guardrails get approved without a fight.

**Concerning:**
- The CEO acknowledges the problem but won't raise it upward.
- The owner's horizon is so short that retention doesn't matter to them.
- You're asked to produce "innovation" that looks good in board decks but doesn't touch the real problem.

If the concerning signals dominate, you may be in a role designed to create the appearance of transformation rather than the substance. That's worth recognizing early. You can still do valuable work, but you'd calibrate your ambitions and your own career decisions accordingly.

## In short

- **Don't chase the root cause forever.** Act at the highest level you can influence, and make the problem visible to the level above.
- **Test whether the board truly rewards bookings over retention,** or whether that's an assumption no one has checked.
- **Frame retention as protecting the board's own goals,** especially enterprise value at exit.
- **Equip the CEO through the CFO and better metrics.** Never go around him.
- **Prioritize fixes that improve retention without hurting bookings,** so progress starts now.
- **Watch the signals** to learn whether you're in a real turnaround or a performance of one.

The through-line of this whole conversation holds here too: the organization can change from within only if the people who own each system are willing to change it. Your job is to make the case so clear, and the first steps so easy, that saying yes is the rational choice at every level.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

**Don't build a separate lab yet, and don't simply work through existing channels either.** Spend the next 90 days finding out why customers leave, fixing the fastest levers with the people who own them, and letting the evidence decide how much structure you need. Your first deliverable to the CEO is the truth about churn, not an innovation program.

Here's the plan.

## Weeks 1–3: Diagnose

**Goal:** a clear, quantified answer to "why are we losing customers and deals?"

1. **Churn and loss analysis.** Pull the last 20 to 30 churned accounts and lost deals. Tag each by primary reason:
   - capability gap
   - architecture / cloud
   - implementation
   - service
   - price
   - relationship
2. **Custom-scope analysis.** For recent closed deals, tag how much custom work was promised and what it was. Compare against implementation overruns, margin, and early churn. Note whether custom-heavy deals cluster at quarter-end.
3. **Interviews.** Talk to 5 to 8 customers or lost prospects, a few reps, sales engineers, implementation leads, and customer success managers. Ask reps what they have to promise to win.
4. **Context from the CFO.** Find out:
   - who owns the company and what their horizon is
   - what metrics the board sees
   - how the CEO is measured
5. **One conversation with the CEO.** Ask what "outsized results" means to him, what the board worries about, and what he's seen go wrong with innovation efforts before.

**Output:** a short memo with the main loss drivers, their financial cost, and the root causes you can trace.

## Weeks 3–5: Build alignment

Share findings privately, in this order:
1. **Head of sales,** framed as a shared problem, not an indictment
2. **CFO,** to validate the numbers and model the cost
3. **Head of services or implementation**

Then go to the **CEO**, ideally with the head of sales or the CFO beside you. Lead with customers and money. Frame whatever system needs changing as "built for yesterday's problem." Bring a proposal small enough to approve on the spot.

At the same meeting, **clarify your scope explicitly.** Agree on what you'll lead, what you'll support, and who owns each outcome.

## Weeks 5–12: Act on three tracks

**Track 1: Guardrails, owned by sales and services, supported by you**
- Scope review for custom commitments above a set threshold
- Implementation sign-off on complex statements of work
- Custom work priced rather than given away

These are cheap, reversible, and don't reduce bookings.

**Track 2: One or two protected teams, led by you**
- Point them at the biggest loss driver the data reveals. Likely targets are the most frequently promised customizations, migration or configuration tooling, or rescuing a few at-risk accounts.
- Staff them partly with respected insiders.
- Give them targeted exemptions only, such as their own release path, lightweight approvals, and dedicated engineers.
- Tie each team to a real customer and to a core executive who owns adoption.
- **Log every blocker.** That log is your evidence for how much separation the company actually needs.

**Track 3: Measurement, led by the CFO and supported by you**
- Start tracking gross retention, net revenue retention, implementation success, and outcomes on custom-heavy versus standard deals.
- Propose adding them to board reporting.

## Day 90: Decide based on what you learned

| If you find... | Then... |
|---|---|
| Churn is driven mostly by fixable implementation, service, or sales issues, and the protected teams moved without major blocks | Stay embedded. Scale the protected-team model. The CEO's instinct was largely right. |
| A fundamental architecture gap the core can't close, or the blocker log shows the core consistently stalling new work | Make the case for a more separate unit, now with evidence and allies. Your original instinct was right. |
| Comp is a major driver | Propose comp changes for the next plan cycle, with the head of sales co-owning the proposal. |
| Leadership won't change the systems it owns, or the owner's horizon makes retention irrelevant | Reassess what's achievable in this role, and calibrate your ambitions accordingly. |

## Principles to hold throughout

- **Customers first.** Every initiative traces back to a reason customers leave or don't buy.
- **No surprises.** Peers see findings before the CEO does. You never go around the CEO to the board.
- **Systems, not blame.** People are responding rationally to the incentives they were given.
- **Small and reversible first.** Make saying yes easy.
- **Measure outcomes,** meaning retention and wins, not demos or activity.
- **Give credit away.** Your influence grows when peers succeed with your help.

## This week

1. Request churn, loss, and deal data from sales operations and finance.
2. Schedule introductory conversations with the heads of sales, services, and finance. Frame them as learning, not auditing.
3. Book time with the CEO to understand his definition of success.
4. Pick 3 churned customers and try to get them on the phone.

The debate about a lab versus existing systems will largely resolve itself once you know why customers are leaving and where the organization actually gets stuck. Start there.

## Outcome summary (sent to Jev)

The recommendation is to neither build a separate innovation lab yet nor simply work through existing channels. Instead, spend 90 days finding out why customers leave, fixing the fastest levers with the people who own them, and letting evidence decide how much structure is needed. The first deliverable to the CEO is the truth about churn, not an innovation program.

The reasoning is that both positions argue about internal structure while ignoring customers. A lab can't fix a retention problem in the installed base, but existing processes will throttle new work if forced through unchanged. The better approach is to "separate the rules, not the organization."

- **Weeks 1–3:** Analyze 20–30 churned accounts and lost deals, tagging each by primary reason. Check whether promised custom scope predicts implementation overruns and early churn. Interview customers, reps and implementation staff. Learn from the CFO who owns the company, what the board sees, and how the CEO is measured.
- **Weeks 3–5:** Share findings privately with sales, finance and services before the CEO. Frame the problems as systems "built for yesterday's problem," and clarify scope explicitly.
- **Weeks 5–12:** Run three tracks:
  - deal guardrails such as scope review and priced custom work
  - one or two protected teams with targeted exemptions, staffed partly by respected insiders and tied to real customers, logging every blocker
  - retention metrics proposed for board reporting

At day 90, decide based on evidence. Stay embedded if the teams moved freely. Argue for a separate unit if there's an architecture gap or consistent stalling. Propose comp changes next cycle if overselling drives churn.

The main caveats are to never go around the CEO to the board and to avoid chasing root causes endlessly. If leadership won't change the systems it owns, reassess whether the role is winnable.
