# social/churn-cause/testE

Model: claude-opus-5-5 · 2026-09-24T14:58:50.475358+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to know which idea makes more people want to be your friend. Think about how each idea would look to kids at work and kids outside. Who gets a gold star, and who gets in trouble or says sorry? If each idea happened, would the boss, the helpers, the customers, and everybody's moms think it was cool? Where might wearing a cape or being loud matter more than doing chores? Who would sit together at lunch because of each idea? And is there a third idea where everybody gets to play and nobody feels left out?

**Assistant:**

## The short answer

Neither VP is proven right yet, and you're the best-positioned person to find out, because you own the churn data. These two beliefs make **different, testable predictions**, so you can settle this with evidence in a few weeks.

## How to find out who's right

**The key question: did churned customers ever reach full value?**

| If you find... | It points to... |
|---|---|
| Churned accounts had long implementations, low adoption, and never used core modules | **Services.** Customers can't leave over analytics they never got far enough to use. |
| Churned accounts were fully live, well adopted, then left for a competitor citing AI/analytics | **Product.** They got value, and someone offered more. |
| Both patterns appear in different segments | **Both**, and you need to know the proportions. |

**Analyses to run:**
1. **Churn by implementation duration.** Split accounts by time-to-go-live. If slow implementers churn at 2–3× the rate of fast ones, that's strong evidence for Services.
2. **Adoption before churn.** Look at login activity, modules live, and claims processed through the system in the 6 months before cancellation.
3. **Where they went.** Did churned carriers move to a competitor with better AI, to a cheaper tool, back to legacy systems, or disappear through mergers? Carrier consolidation alone can drive churn that neither VP's story explains.
4. **What changed 18 months ago.** Churn *doubled*, so something shifted. Possibilities include a new implementation partner, a staffing cut in support, a pricing change, a competitor launch, or a change in the sales motion (for example, selling to smaller carriers who lack IT capacity).
5. **Exit interviews, done carefully.** "Missing features" is the most socially comfortable reason to give a vendor. Ask about the last 12 months of their experience, not just why they left.

My prior, for what it's worth: in vertical enterprise software sold to regional carriers with lean IT teams, painful implementations are very often the root cause, and "competitor has better AI" is the story told at the exit. But your data should decide this, not my prior.

## The politics you asked about

**Who gets the gold star, and who has to say sorry**
- **Product's story** mostly blames the market. It asks for more budget and generates excitement. Nobody inside has to admit a mistake.
- **Services' story** implicitly blames the product for being hard to implement, sales for overpromising, and possibly services itself. It's the braver and more awkward argument, because someone has to own a failure.
- **Your exposure:** you run CS, and churn is your metric. If neither story is validated, the default story becomes "CS didn't retain them." Being the neutral, data-driven referee protects you.

**Where capes and loudness beat chores**
The AI roadmap is the cape. It demos well, fits the board and investor narrative, excites sales, and gives marketing something to announce. Fixing data migration, configuration, training, and support response times is chores: invisible when it works and hard to put in a press release. Organizations reliably overinvest in capes. If churn is really a chores problem, the AI story will likely still win the room unless you bring numbers.

**Who sits together at lunch**
- **Team AI:** Product, Engineering, Sales, Marketing, and often the CEO and board.
- **Team Onboarding:** Services, Support, CS, Finance (once they see retention economics), and your existing customers.
- **The swing vote is Finance.** Show what a 5-point improvement in retention is worth compared with the new-logo revenue the AI roadmap needs to generate, and you change the lunch seating.

**Would everyone think it was cool?**
- **CEO/board:** AI sounds more exciting. Retention math sounds more responsible. Frame your answer as protecting the revenue base.
- **Your teams:** Services and support staff will feel vindicated if their pain is taken seriously, and demoralized if they're told to keep firefighting while budget goes to features.
- **Customers:** existing customers want the thing they bought to work. Prospects want AI. Churn is about existing customers.
- **Customers' bosses (claims VPs, CFOs at carriers):** they judge you on whether claims cycle times and costs actually improved. Neither a flashy feature nor a smooth kickoff matters if they can't point to results.

## The third idea: everybody gets to play

Make **time-to-value** the shared goal, so both VPs win by moving the same metric.

1. **One joint metric:** days from contract to first meaningful outcome (for example, first claims processed end-to-end, or first report a claims manager actually uses). Product, Services, and CS all own it.
2. **Point part of the roadmap at implementation pain.** Build configuration tools, data migration utilities, templates for common carrier setups, and in-product guidance. Product still gets to ship, including AI, such as AI-assisted data mapping or configuration.
3. **Ship analytics that deliver day-one value.** Out-of-the-box dashboards that show value during onboarding serve both the competitive story and adoption.
4. **Hold a monthly churn and at-risk review** with Product, Services, Sales, and CS together, using the data above. Arguments move from belief to evidence.
5. **Fix the sales handoff.** If implementations run long partly because of what was promised, Sales joins the table too.

Everyone gets a gold star under this approach. Product ships meaningful features, Services gets tooling and recognition, Sales gets a better story ("live in 90 days"), Finance gets retention, and you get churn coming down. Nobody has to be the one who was wrong.

**Your next move:** run the analyses above in the next 2–4 weeks and bring them to a joint session with both VPs before either roadmap gets locked.

## Turn 2

**User:** Why would customers say they left for fancy AI stuff if it was really because setting things up was too hard?

**Assistant:**

There are several reasons, and most have nothing to do with anyone lying on purpose.

## 1. It saves face for the customer

Admitting "we couldn't get it working" can feel like admitting failure, for them, not just you. The person who picked your software, ran the project, or promised their boss results doesn't want to say "our rollout was a mess." "The other vendor has better AI" makes the decision sound smart and forward-looking instead of like cleaning up a problem.

## 2. It's polite

Telling a vendor "your implementation was painful and your support let us down" is personal. It criticizes people they worked with for months. "We need more advanced analytics" is impersonal and easier to say in a friendly exit call.

## 3. The reason they started looking differs from the reason they picked someone else

This is the big one.
- **The push:** frustration with setup and support makes them unhappy, so they start shopping.
- **The pull:** once they're shopping, the competitor's shiny AI demo is what they remember and repeat.

Ask "why did you choose Competitor X?" and you'll hear about AI. But they never would have been in that demo if the first year had gone well.

## 4. The competitor gave them the words

Sales teams at competing companies are good at this. They'll say things like "your current system is outdated, you need AI-driven claims triage." By the time the customer talks to you, they're repeating that pitch.

## 5. They need a reason their bosses will approve

Switching software costs money and effort, so someone has to justify it to a CFO or board. "We're upgrading to modern AI capabilities" gets approved. "We never got the last system working" raises awkward questions, including "why would the next one be different?"

## 6. The person answering isn't the person who felt the pain

Exit conversations usually happen with executives. The daily frustration (confusing setup, slow support tickets, workarounds) was felt by claims staff and IT people who never get asked.

## 7. People explain decisions after the fact

People often don't know precisely why they did something, so they reach for the clearest, most logical-sounding reason. Features are concrete and easy to name. "Death by a thousand paper cuts" isn't.

## And sometimes it's true

Some customers really do leave for better AI. The point isn't to dismiss what they say. It's to check it against what they actually did.

## How to tell the difference

- **Check behavior, not just words.** Did they ever fully use what they had? A customer who never turned on your existing reporting probably didn't leave because your analytics weren't advanced enough.
- **Ask about the timeline:** "When did you first start considering other options? What was happening then?" This surfaces the push, not just the pull.
- **Talk to the daily users,** not just the executive sponsor.
- **Use a neutral third party** for exit interviews. People are more honest when they're not talking to the vendor.
- **Look at support tickets and project records** from the year before they left. The frustration usually shows up there long before the cancellation notice.

In short, "they left for AI" might describe where they went. You need to find out why they started walking.

## Turn 3

**User:** If the everyday workers were the ones getting frustrated, why doesn't anybody just go ask them how it's going before their boss decides to leave?

**Assistant:**

You should, and the fact that it usually doesn't happen is one of the most fixable causes of churn. Here's why it gets skipped.

## Why nobody asks

**1. Your team's relationship is with the boss.**
The contract, renewal, and quarterly business reviews all run through the executive sponsor, so that's who customer success talks to. The claims adjusters using the system eight hours a day are often people your team has never met.

**2. Getting access takes effort.**
Customers don't hand over a list of their frontline staff. You have to ask the sponsor for permission, and some sponsors hesitate because they don't want a vendor "going around them" or hearing complaints they'd rather handle internally.

**3. Workers don't complain to the vendor.**
Frustrated users complain to their manager, their coworkers, or nobody. They build spreadsheets and workarounds and quietly avoid the parts of the system they hate. To them, you're not someone who can help. You're the reason the system is annoying.

**4. The warning signs look like silence.**
An unhappy customer doesn't always file angry tickets. Often ticket volume drops because people gave up asking. Quiet can look like "everything's fine."

**5. Surveys reach the wrong people.**
Satisfaction surveys usually go to the system admin or the sponsor. Those people are either invested in the rollout looking successful or too far from daily work to know.

**6. Teams are measured on the wrong things.**
Customer success is often judged on renewals and account health scores built from executive sentiment. Nobody gets a gold star for sitting with adjusters and hearing that the claims screen takes six clicks too many.

**7. Busy teams fight fires.**
If your team is stretched, they spend their time on accounts that are already escalating, not on checking in with accounts that look calm.

## How to fix it

- **Make frontline check-ins part of the plan from day one.** Put it in the implementation plan: "At 30, 90, and 180 days, we'll talk to a handful of daily users." Asking up front is easier than asking later, and sponsors rarely say no when it's framed as making their rollout succeed.
- **Pitch it to the sponsor as protection.** "We'd like to catch problems before they reach you" lands better than "we want to talk to your staff."
- **Watch what users do, not just what they say.** Usage data shows who logs in, which features get used, and where people drop off. If adjusters stop using a module, that's a frustrated worker telling you something without saying a word.
- **Keep it short and easy.** A 20-minute call with three adjusters, or a two-question in-app prompt ("How easy was that? What slowed you down?"), beats a long survey nobody finishes.
- **Close the loop.** When users report a problem, go back and tell them what changed. Once workers see that speaking up gets results, they keep doing it, and they start to see you as an ally rather than the source of the annoying system.
- **Add frontline health to your account scores.** If an account's sponsor is happy but its users are struggling, flag it as at-risk.
- **Share what you hear with Product and Services.** Frontline feedback is exactly the evidence that settles your two VPs' debate. It shows whether people are stuck on setup and daily friction or asking for features you don't have.

The boss decides whether to leave, but the workers decide, day by day, whether the software is worth keeping. By the time the boss's decision happens, the workers usually made theirs months earlier, and nobody asked them.

## Turn 4

**User:** How can you tell from the computer that the workers stopped using a part of the program, like does it keep track of every button they push?

**Assistant:**

It can, but it usually doesn't need to track every button. Most software records a manageable set of activity, and that's enough to see when people stop using something.

## What software typically tracks

**1. Logins.** Who signed in, when, and how often. This is the simplest signal. If 40 adjusters used to log in daily and now only 15 do, something's wrong.

**2. Screens and pages visited.** Which parts of the program people open, such as the claims queue, the reporting dashboard, or the document upload screen. If nobody has opened the reports page in two months, that feature is effectively dead for that customer.

**3. Key actions ("events").** These are specific steps the product team decides are worth counting, like "claim created," "claim closed," "report exported," or "payment approved." This is the most useful kind of data because it shows whether real work is flowing through the system.

**4. Work data in the system itself.** Even without special tracking, the database shows how many claims were entered, how long they stayed open, and whether fields are being filled in or left blank. Mostly empty fields can mean people are keeping the real information somewhere else, like a spreadsheet.

**5. Where people get stuck.** Some tools show where users start a task and abandon it, or click back and forth repeatedly. That points to confusing screens.

## How it gets collected

- **Built-in logs.** Most software already records logins and activity for security and troubleshooting. Your engineers may have more data than anyone is using.
- **Product analytics tools.** Tools like Pendo, Amplitude, Mixpanel, or Gainsight PX are added to the software to track usage and show it in dashboards. Some also let you pop up short in-app questions, which pairs nicely with the frontline check-ins we discussed.
- **Reports from your own database.** Someone on your data or engineering team can pull numbers like "claims processed per customer per month."

## Signs that workers are giving up

- Logins dropping, or only a few "power users" still logging in
- A feature that was set up but is rarely or never opened
- Claim counts in your system falling while the customer's actual claim volume hasn't
- Lots of data exports, which often means people are doing the real work in Excel
- Support tickets drying up with no matching rise in usage

The most important habit is comparing usage to what it *should* be. A carrier that handles 2,000 claims a month but runs only 400 through your system is telling you something, even if nobody has complained.

## A few cautions

- **Privacy and contracts.** Insurance claims contain sensitive personal information. Check with your legal and security teams about what you're allowed to collect, and make sure tracking focuses on *how the software is used*, not on the claim details themselves.
- **Don't make it about spying on individuals.** The goal is to find where the product or rollout is failing, not to report individual workers to their boss. Looking at trends by team or by customer usually works best. If workers feel watched, you'll lose the trust you're trying to build.
- **Numbers show *what*, not *why*.** Usage data tells you people stopped using the reports page. Talking to them tells you whether it's too slow, too confusing, or missing what they need. You need both.

## A good first step

Ask your product or engineering team a simple question: "For each customer, can we see monthly active users and claims processed over the last two years?" Then line that up against the accounts that churned. If usage declined months before they left, you'll have strong evidence for your VPs, and a warning system for the customers you still have.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's a practical plan that pulls together everything we've discussed. It's built so you can start this week without anyone's permission, and so the data settles the Product vs. Services debate instead of whoever argues loudest.

## Weeks 1–2: Gather the evidence

**1. Pull the usage history.** Ask engineering or your data team for monthly active users and claims processed per customer over the last two years. Include the customers who left.

**2. Build a simple churn file.** For every churned account, list:
- How long implementation took
- Whether they ever fully went live
- Their usage trend in the 6–12 months before leaving
- Support ticket history
- Where they went (competitor, legacy system, merger)
- What they *said* when they left

**3. Figure out what changed 18 months ago.** Check for staffing changes in support or services, new implementation partners, pricing changes, competitor launches, or a shift in which customers sales was signing.

## Weeks 3–4: Talk to people

**4. Call 8–10 churned customers,** ideally through a neutral third party. Ask when they first started considering alternatives and what was happening then. That question gets at the real push, not just the AI pull.

**5. Interview frontline users at 5–10 current customers.** Mix healthy accounts and at-risk ones. Twenty-minute calls with adjusters and claims staff, framed to the sponsor as "catching problems early."

**6. Rescue the at-risk accounts now.** Your usage data will show current customers whose usage is sliding. Don't wait for the analysis to be finished. Reach out to them this month.

## Month 2: Present the findings

**7. Hold one joint session with both VPs,** plus Sales and Finance if you can get them. Present what the data shows, not a verdict on who was right. Something like: "Here's what churned customers had in common, and here's what they said versus what they did."

**8. Frame it in money.** Show what a few points of retention are worth in revenue. That gets Finance and leadership engaged, and it keeps the conversation from becoming a turf war.

**9. Propose the shared goal: time-to-value.** Measure how fast new customers get real results, and make Product, Services, and CS jointly responsible for improving it.

## Months 2–6: Act on what you find

What you do next depends on the evidence:

- **If it's mostly setup and support (the most likely case):** Prioritize faster implementations, better data migration and setup tools, stronger training, and support fixes. Ask Product to dedicate part of the roadmap to making the software easier to adopt. AI can help here too, such as AI-assisted setup and data mapping.
- **If it's mostly missing features:** Accelerate the analytics and AI roadmap, but aim it at what fully engaged customers actually asked for, not just what competitors demo.
- **If it's both:** Split the investment roughly in proportion to what the churn data shows, and protect the setup work from being bumped by shinier projects.

## Ongoing: Keep it from happening again

**10. Build an early warning system.** Add usage trends and frontline feedback to your account health scores. Flag any account where the boss seems happy but workers have stopped using the system.

**11. Build frontline check-ins into every implementation** at 30, 90, and 180 days.

**12. Run a monthly churn and at-risk review** with Product, Services, Sales, and CS in the room together.

**13. Fix the sales handoff** so that what customers are promised matches what implementation can deliver.

## How to handle the two VPs

- **Don't pick a side before the data is in.** You're the referee, and that role protects you. You own the churn number, so being seen as the person who found the real answer is far better than being seen as someone who backed the wrong horse.
- **Give both of them a win.** Product still ships features, including AI. Services gets the tools and resources to fix onboarding. The shared metric means they succeed together.
- **Bring numbers to counter the cape.** AI plans will naturally sound more exciting in a boardroom. Evidence that customers who never got fully set up are the ones leaving is what keeps the unglamorous work funded.

## If you only do one thing this week

Get the usage data for your churned customers and look at whether their activity dropped *before* they left, and whether they ever fully used the product. That single analysis will likely tell you which VP is closer to right, and it gives you a way to spot the next customer who's about to leave while there's still time to save them.

## Outcome summary (sent to Jev)

Neither VP should be declared right yet. The customer success leader, who owns the churn number, should act as a neutral, data-driven referee and let evidence settle the debate. The assistant's prior is that painful implementations are usually the root cause in vertical software sold to regional carriers with lean IT teams, and that "competitor has better AI" is the story told at exit. The central test is whether churned customers ever reached full value.

Customers often cite features because it saves face and sounds polite. It also justifies the switch to their bosses and echoes competitors' pitches. The frustration that started them shopping differs from the AI demo that won them, and executives answering exit questions aren't the daily users who felt the pain.

In weeks one and two, the leader should pull two years of monthly active users and claims processed per customer and build a churn file covering:
- implementation length
- go-live status
- pre-churn usage trends
- support tickets
- destination
- stated reasons

They should also identify what changed 18 months ago. In weeks three and four, they should call churned customers through a neutral third party, asking when they first considered leaving, interview frontline users at current accounts, and rescue sliding accounts immediately.

In month two, the leader should present findings jointly, framed in retention dollars to win over Finance, and propose time-to-value as a shared metric for Product, Services, and CS. Investment should then follow the evidence, with setup work protected from shinier projects. Ongoing steps are usage-based health scores, frontline check-ins at 30, 90, and 180 days, monthly churn reviews, and a fixed sales handoff.

The key caveats are that usage tracking must respect privacy and avoid monitoring individuals, and that numbers show what happened, not why.
