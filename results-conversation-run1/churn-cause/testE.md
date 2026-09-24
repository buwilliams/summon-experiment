# churn-cause/testE

Model: claude-opus-5-5 · 2026-09-24T14:14:43.147726+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I don't want to know which idea sounds more grown-up. I want to know which one is more fun. Pretend each idea is a new toy: what does it do, and who gets to play with it? If each one happened, would the people at work be happy or sad, and would anybody cry? Where is each idea kind of boring, so that nobody would want to hear about it at dinner? Does either idea come with snacks, or a place to play? And is there a third idea that everybody likes better, like a swing set for the whole office?

**Assistant:**

# Two Toys and a Swing Set

## Toy #1: The Shiny Robot (VP of Product's idea)

**What it does:** It lights up, talks, and does tricks. It predicts which claims are fraudulent, draws pretty charts, and says "AI" out loud. It's the toy you see in the commercial.

**Who gets to play with it:** Mostly engineers, who love building it, and salespeople, who love showing it off. Customers *want* to play with it, but only the ones who have already finished setting up the regular toys. A robot is no fun if the batteries never got installed.

**Happy or sad?**
- 😄 Product and engineering are thrilled. This is the fun homework.
- 😄 Sales is happy, because demos get sparkly.
- 😢 Services might cry. Every new feature is one more thing to configure during implementations that already take too long. The robot arrives with 40 more pieces in the box.
- 😢 Customers stuck mid-implementation feel sad and a little left out, watching a toy they can't reach yet.

**The boring part:** Underneath every robot is a lot of wiring. AI and analytics need clean, well-connected claims data, and regional carriers often have old systems and messy data. Nobody at dinner wants to hear about data pipelines.

**Snacks and a place to play:** Yes! This toy comes with a launch party, cake, and a stage for a keynote demo. That's part of why it's tempting.

## Toy #2: The Really Good Building Blocks (VP of Services' idea)

**What it does:** It makes the toys you already have actually snap together. Setup is faster, someone helps when you're stuck, and customers get to the "oh, this is great" moment sooner.

**Who gets to play with it:** Customers, a lot and early. Also the services and support teams, who stop spending their days apologizing.

**Happy or sad?**
- 😄 Customers are quietly happy. Their claims adjusters stop grumbling.
- 😄 Services people are relieved, the kind of happy where you can finally breathe.
- 😐 Engineers may be a bit sad if their robot gets put on the shelf.
- 😐 Sales can get grumpy: "Faster onboarding" is harder to wow people with than "AI."
- Probably nobody cries, but nobody throws a parade either.

**The boring part:** Almost all of it. Migration templates, implementation checklists, support ticket routing. It's the definition of "not dinner conversation." That's exactly why it tends to get skipped, even when it matters most.

**Snacks and a place to play:** Smaller snacks, like go-live pizza with a customer's team. The play space is the customer's own office, which is less glamorous but is where they decide whether to renew.

## So which toy is the real answer?

Here's the honest part: **you can't tell from the toys; you have to play detective.** And there's a simple clue that settles most of it:

**Look at the customers who left. Did they ever finish setting up?**

- If most churned customers **never fully went live or used the product deeply**, the robot can't be the reason. They never got far enough to miss fancier features. That points to Services.
- If churned customers were **fully live, used the product heavily, and then left for a competitor's analytics**, that points to Product.

A few more clues worth gathering:
- **How long did churned customers' implementations take** compared with customers who stayed?
- **What do exit interviews say, and what does the usage data say?** "Your competitor has AI" is a polite, easy thing to say on the way out. Often the real story is "we never got value, and the other guy's demo looked shiny."
- **Who is winning your customers?** Is it competitors with better features, or ones with a reputation for easy onboarding?

My hunch, for regional carriers with small IT teams and older systems: the building blocks explain more of the churn than people expect. But the detective work takes a few weeks, and it's worth doing so this doesn't stay a contest between two VPs.

## The Swing Set: Something Everybody Can Play On

The swing set is **product work that makes onboarding easier.** Instead of "robot vs. blocks," build toys that snap together by themselves:

- **Analytics that work on day one.** Prebuilt dashboards and reports that light up as soon as data flows in, with no custom build. This gives Product its analytics story *and* gives customers value in week two instead of month nine.
- **AI that helps with setup.** Use AI for tedious implementation jobs like mapping old data fields, suggesting configurations, and flagging data problems. The shiny toy gets used to install the batteries.
- **Tools that make implementation easier.** Self-serve configuration and migration tools that engineers build and Services uses.

Then give everyone **one shared scoreboard: time-to-first-value.** That means how many days until a new customer is getting real, visible value. Product, Services, and Sales all push the same swing.

**Why everybody likes it better:**
- Engineers still get to build cool things.
- Sales still gets a great demo: "Live in weeks, with analytics from day one."
- Services gets fewer painful implementations.
- Customers get to the fun part sooner, and they're far less likely to leave.

**Snacks:** You can celebrate every time the time-to-value number drops. That's a party where everyone is invited.

**Your move:** Run the churn detective work first (a few weeks), share the findings with both VPs together, and pitch the swing set as the plan. It's much easier to agree on a toy when nobody had to lose the argument to get there.

## Turn 2

**User:** How do you find the customers who left so you can ask them if they finished setting up — do you just call them on the phone, or would they be too mad to talk to you?

**Assistant:**

# Finding the Customers Who Left

Good news: **you mostly don't need to ask them.** The clue that matters most, "did they finish setting up?", is already sitting in your own toy box.

## Step 1: Check your own records first (no phone needed)

Before you call anyone, pull the churned customers from the last 18 months and look at what your company already knows:

- **CRM and contract records:** who left, when, and their stated reason (if anyone wrote one down)
- **Implementation records:** start date, planned go-live date, *actual* go-live date, or whether they ever went live at all
- **Product usage data:** how many users logged in, which modules they used, and whether usage grew, stayed flat, or faded before they left
- **Support tickets:** how many, how angry, and how long they stayed open
- **Your own team's memory:** the CSMs and implementation leads who worked those accounts usually know the real story

Put it in one simple spreadsheet, one row per churned customer, and do the same for a group of customers who *stayed*. Comparing the two usually tells you a lot, sometimes most of what you need.

## Step 2: Then call some of them, to learn the "why"

Your records tell you *what* happened. Only people can tell you *why*. So yes, pick up the phone, but set it up well.

**Will they be too mad to talk?** Some will. But a lot of former customers are surprisingly willing, and the mad ones often have the most to say. People like being asked, especially when they think someone might finally listen. Expect maybe a third to half to say yes if you ask nicely.

**How to make it more likely they'll talk:**

- **Choose the caller carefully.** Don't send the account rep they had a rough time with. A senior leader works well (you, or even your CEO for bigger accounts), since it signals you take it seriously. A neutral outside researcher also works: people are often more honest with someone who doesn't work for you.
- **Make clear it's not a sales call.** Say so right up front: "We're not trying to win you back. We want to understand what we got wrong."
- **Keep it short.** Ask for 20 minutes, not an hour.
- **Say thank you with something small.** A gift card or a donation to a charity they pick is a nice touch. Check their company's rules first, since some insurers limit gifts.
- **Reach the right people.** Try to talk to both the executive who signed off on leaving and someone who used the product every day, like a claims manager. They often tell very different stories.

**Good questions to ask:**
- "Walk me through the moment you started thinking about leaving."
- "How did setup and implementation go, honestly?"
- "Was there a point where the product was really working for you?"
- "What does your new system do that ours didn't?" Listen carefully here: is it features, or is it "they got us running fast"?

Mostly listen. Don't argue or explain. If they say something unfair, just write it down.

## A bonus

Regional insurance is a small world. Carriers talk to each other, and customers who leave sometimes come back when their new vendor disappoints them. A respectful, humble phone call does more than gather clues. It leaves a door open.

## A tip for next time

Start doing **exit interviews as soon as a customer gives notice**, while memories are fresh and you might even save the account. And track implementation milestones and time-to-value for *current* customers, so you can spot the ones drifting toward the door before they leave.

## Turn 3

**User:** If the computer can already see when a customer stops logging in, can you see right now which ones are starting to get bored, and what would you say to them before they leave?

**Assistant:**

I can't see your customers' data myself, but your team almost certainly can, and yes, you can often spot the bored ones months before they leave.

## Signs a customer is getting bored

No single sign means much on its own. Look for **changes over time** and **several signs at once**:

**Using the toy less**
- Fewer people logging in, or the same few people logging in less often
- Logins dropping after a busy start, especially 3 to 9 months after go-live
- Only basic features in use, with modules they paid for sitting untouched
- People exporting data to spreadsheets instead of using your reports (a big one: it means they're building workarounds)

**Never finished setting up**
- Implementation running past its planned go-live date
- Go-live happened, but some teams or claim types never moved over

**Going quiet or getting grumpy**
- Their champion stops answering emails or skips check-ins
- Support tickets suddenly spike (frustration), or suddenly stop (they've given up)
- Tickets that say "still" or "again"

**Changes on their side**
- Your champion or executive sponsor leaves the company
- They're acquired, merge, or get a new CIO or head of claims
- They start asking about contract terms, data export, or the renewal date far earlier than usual

**Make a simple watch list.** Pick 5 or 6 of these signals, give each customer a green, yellow, or red rating every month, and review the yellows and reds as a team. It doesn't need to be fancy. A spreadsheet works fine to start, and customer success software can automate it later. Test it by checking whether your churned customers would have turned red before they left. If they would have, you've got a good early-warning system.

## What to say to them before they leave

The most important rule: **don't open with "We noticed your logins dropped."** That feels like being watched. Open with *their* goals, not your data.

**1. Reach out with curiosity**
> "We're checking in with carriers like you to see whether you're getting what you hoped for from the system. What's working, and what's frustrating your team?"

Then listen. The real problem usually comes out in the first ten minutes.

**2. Go back to why they bought it**
> "When you signed on, the goal was to cut claim cycle times. How close are you to that?"

This refocuses everyone on value instead of features.

**3. Fix something real, fast**
Offer something concrete, not a pitch:
- A free working session to finish a stalled piece of setup
- Training for a new team or a new claims manager
- A pre-built report that replaces the spreadsheet they're exporting to

A quick, visible win matters more than a big promise.

**4. Find a new champion if the old one left**
> "Since Maria moved on, who's the best person for us to partner with?"

A customer whose champion left is a customer at high risk. Rebuild that relationship quickly.

**5. Bring in a senior leader for the red accounts**
For your most at-risk and valuable customers, a call from you or an executive says "you matter to us." It's even better if you come with a plan and not just an apology.

**6. Follow up and show the change**
A few weeks later, go back with evidence: "Your adjusters are now using the new dashboard daily." That's what turns a bored customer back into a happy one.

## One thing to watch for

If you find that lots of customers get bored at the *same point*, for example right after implementation or in the same module, that's not a problem to fix one call at a time. It's a clue about the Product vs. Services debate, so feed it back into the churn detective work. And it's exactly what your swing-set metric, time-to-first-value, is meant to catch early.

## Turn 4

**User:** Why does one person like Maria leaving her job make the whole insurance company want to stop using the toy? Doesn't everybody else there still know how to play with it?

**Assistant:**

Great question. Usually everybody else *does* still know how to play with it. What they lose isn't the ability to use the toy. They lose the person who **picked it, explained it, and stood up for it.**

## What Maria was really doing

Think of Maria as the kid who brought the toy to the playground. Other kids play with it, but she's the one who:

**1. Chose it and defended it**
She probably helped pick your software over competitors. She had a personal stake in it working, so when things got bumpy, she pushed through instead of giving up.

**2. Knew the secret tricks**
She knew the workarounds, why things were set up a certain way, and who to call at your company when something broke. Much of that was never written down. It walks out the door with her.

**3. Explained why it matters**
Adjusters know which buttons to press. Maria knew how to tell the executives, "This cut our claim cycle time by 12%." Without someone translating the toy into business results, it becomes just a line item on a budget.

**4. Fought for it at renewal time**
When the CFO asked, "Do we really need this?", Maria said yes and had reasons. When she's gone, nobody raises their hand, and a question with no defender often ends with "let's look at other options."

**5. Was the relationship**
The trust between the carrier and your company often lived between Maria and your CSM. The new person doesn't know your team and has no reason to give you the benefit of the doubt.

## Why the new person may want a different toy

When someone replaces Maria, a few things tend to happen:

- **They bring their favorite toy from their last job.** A new head of claims who used a competitor's system elsewhere may naturally prefer what they know.
- **They want to make their own mark.** New leaders often review everything their predecessor chose. "Let's re-evaluate vendors" is an easy early project.
- **They only see the problems.** They didn't see how bad things were before your software arrived, so the improvements feel normal and the frustrations stand out.
- **They had nothing to do with the choice.** If it fails, it isn't their failure. If they switch, they get credit for the new thing.

None of this means the toy stopped working. It means the **story about why the toy matters** left with Maria.

## How to keep one person from being the whole playground

This is often called **"multi-threading": having relationships with several people at each customer**, not just one.

- **Know at least 3 to 5 people at every account**: an executive sponsor, a day-to-day champion, a couple of power users, and someone in IT
- **Get the value in writing.** Regular business reviews that show results in the customer's terms (cycle times, costs, adjuster productivity) mean the story survives even if Maria leaves
- **Train more than one power user** so the secret tricks aren't stuck in one head
- **Document their setup**: why things are configured the way they are, and their workarounds
- **Move fast when a champion leaves.** Reach out to the new person within weeks. Offer a welcome session, a recap of what the system has achieved for them, and help getting up to speed. Treat them like a brand-new customer, because in a way they are.
- **Stay in touch with Maria.** Champions who move to other carriers often bring your product with them. Maria leaving can turn into Maria buying from you again somewhere else.

## Back to your churn mystery

This is worth adding to your detective work: **for churned customers, did a key champion or executive leave in the year before they churned?** If that shows up a lot, part of your churn isn't about features *or* implementation. It's about relationships that were too thin. That's something Customer Success can fix directly, without waiting on either VP.

## Turn 5

**User:** What should we do?

**Assistant:**

# The Plan: What to Do, in Order

Here's everything pulled together into one plan you can bring to your leadership team.

## Weeks 1–4: Solve the mystery

**1. Build the churn spreadsheet.**
One row per customer who left in the last 18 months, plus a comparison group that stayed. For each, record:
- Implementation length (planned vs. actual) and whether they fully went live
- Usage trend before they left
- Support ticket volume and tone
- Whether a champion or executive left
- Who they switched to, and the stated reason

**2. Call 10–15 former customers.**
Use a senior or neutral caller, keep it to 20 minutes, and make clear it's not a sales pitch. Talk to both executives and daily users.

**3. Make it a joint investigation.**
Invite both VPs to help design it and review the results. If they build the detective kit together, they're far more likely to accept what it finds.

## Weeks 4–6: Decide based on what you find

Let the evidence choose the toy:

| If you find... | Then the main fix is... |
|---|---|
| Most churned customers never fully went live or got value | **Services**: fix implementation and onboarding first |
| Churned customers were fully live, used it deeply, and left for competitors' features | **Product**: speed up the roadmap on the specific gaps named |
| Churn often followed a champion leaving | **Customer Success**: build broader relationships at every account |
| A mix (the most likely result) | **The swing set**, with priorities set by which cause is biggest |

Share the results with both VPs *together*, framed as "here's what the customers told us," not "here's who was right."

## Starting now, no need to wait: Protect current customers

You can do these while the investigation runs:

- **Build a simple health watch list.** Rate every account green, yellow, or red monthly using 5–6 signals (usage trends, stalled setup, quiet champions, ticket spikes, leadership changes, early renewal questions). Check it against past churn to make sure it would have caught them.
- **Reach out to the red accounts.** Start with curiosity, go back to their original goals, and offer one concrete, fast fix.
- **Map relationships at your top accounts.** If you only know one person there, that's a risk. Aim for 3–5 contacts per account.
- **Start exit interviews** the moment any customer gives notice.

## Months 2–6: Build the swing set

Once the data points the way, launch the shared plan:

- **One shared metric: time-to-first-value.** Product, Services, Sales, and Customer Success all own it together, and it gets reported at leadership meetings.
- **Product builds for faster setup:** analytics that work on day one, tools that make migration and configuration easier, and AI that speeds up implementation.
- **Services simplifies onboarding:** standard implementation playbooks, clear milestones, and quicker handoffs.
- **Customer Success runs regular business reviews** that show results in the customer's own terms, so the story survives when a champion leaves.
- **Celebrate progress.** Every time time-to-value drops or a red account turns green, share it. That's your snack table.

## How you'll know it's working

- Time-to-first-value is going down
- Fewer implementations run late
- Fewer accounts are red on the watch list
- Renewals improve among newer customers first (they're the ones getting the better experience)
- Eventually, annual churn starts falling back toward where it was

## The one-sentence version

**Spend a month finding out why customers actually left, protect the ones at risk right now, and then get Product and Services pushing the same swing: getting customers to real value faster.**

The best part of this plan is that nobody has to lose the argument. Both VPs are probably partly right, and the data will show how much of each. Your job is to be the one who brings the flashlight.

## Outcome summary (sent to Jev)

The assistant recommends not picking between the two VPs yet. Instead, spend about a month finding out why customers actually left, protect at-risk customers now, and then get Product and Services working toward a shared goal: getting customers to real value faster. Its reasoning is that both VPs are probably partly right, and only evidence can show how much of each explains the churn. It suspects that for regional carriers with small IT teams, older systems, and messy data, implementation problems explain more of the churn than people expect. It also notes that "your competitor has AI" is an easy exit excuse that can mask "we never got value."

In weeks one through four, build a spreadsheet of customers who churned in the last 18 months alongside a comparison group that stayed. Record each account's implementation length, whether it fully went live, its usage trends, its support tickets, any champion departures, which competitor it switched to, and its stated reasons. Then call 10–15 former customers, using a senior or neutral caller and speaking to both executives and daily users. Both VPs should help design and review this investigation.

The evidence then decides the priority. Customers who never went live point to Services. Heavy users who left for competitors' features point to Product. Churn that follows champion departures points to thin relationships that Customer Success can fix. A mix, the likeliest result, calls for product work that speeds onboarding: day-one analytics, AI-assisted implementation, and easier migration tools. That work should be tracked through one shared metric, time-to-first-value.

Meanwhile, the assistant recommends several steps that can start immediately:
- Run a monthly green/yellow/red health watch list, validated against past churn.
- Reach out to red accounts with curiosity rather than surveillance.
- Build three to five contacts per account.
- Start exit interviews as soon as customers give notice.
