# churn-cause/economic/testE

Model: claude-opus-5-5 · 2026-09-24T15:31:14.627386+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to know which idea gets you more stuff, like a lemonade stand. Follow the piggy bank through each idea. How many cookies would it get you, and how much allowance would you spend first? If each idea happened, how long until the treats come, and could a big dog eat them all? Where could you keep spending money and still not get more candy? Who would hold the piggy bank, count the coins, and say when to stop buying things? And is there a third idea that gets even more treats without breaking the piggy bank?

**Assistant:**

# The Lemonade Stand Has a Leak

Your stand used to lose about 1 in 10 customers each year. Now it loses about 2 in 10. Two grown-ups disagree about why:

- **The Product Grown-Up:** "The stand across the street has fancier lemonade (analytics, AI). We need a better recipe."
- **The Services Grown-Up:** "People wait so long for their first cup, and it's hard to drink, that they give up before they taste it. Fix the line and the cups."

## Which one is right?

Nobody knows yet, and you can find out cheaply before spending your allowance. **Sort the kids who walked away into two piles:**

1. **Kids who got their lemonade, drank it for a while, then left for the fancy stand.** They finished implementation, used the product, and churned anyway. That points to **product gaps**.
2. **Kids who were still waiting in line, or got a cup but never really drank it.** They had long implementations, low adoption, or never used the analytics you already have. That points to **implementation and service**.

A few more things to check:

- **When did the leak start?** Did churn jump when a competitor launched AI features, or when your implementation backlog grew, a key services lead left, or you signed bigger, more complex carriers?
- **Don't fully trust what departing kids say.** "Your competitor has better AI" is a polite, easy exit reason. "We never got it working" sometimes sounds like "it lacks features," because customers can't see features they never turned on.
- **Claims software is hard to leave.** A regional carrier switching systems is expensive and painful. When they leave anyway, it's usually because something hurt for a long time, which often means they never reached value.

My guess from how these stories usually go: **most of your leak is pile #2, with some pile #1 mixed in.** Your data should decide, not my guess. The sorting takes about 3–4 weeks and costs almost nothing.

## Following the Piggy Bank Through Each Idea

The numbers below are illustrative. Plug in your own.

### Idea 1: Build Fancier Lemonade (Product Roadmap)

| | |
|---|---|
| **Allowance spent first** | A lot. Engineers, data people, and AI work are the most expensive coins you have. |
| **Cookies you get** | You keep the kids in pile #1, and the fancy recipe helps you win new customers in sales demos. |
| **How long until treats** | Slow. Maybe 9–18 months to build. Then customers have to *adopt* the new features, **through the same slow, painful implementation process.** Treats might not show up for two years. |
| **Could a big dog eat them?** | Yes. The competitor keeps building too, so you may finish and still be behind. AI features in insurance also need clean customer data and compliance review, which slows everything down. |

**Where more money stops getting candy:** Features customers can't implement give you zero cookies. Worse, every new feature makes implementation *more* complicated, which can make the Services Grown-Up's problem bigger. That's pouring lemonade into a cup with a hole.

### Idea 2: Fix the Line and the Cups (Implementation and Service)

| | |
|---|---|
| **Allowance spent first** | Medium. Better onboarding process, templates, data-migration help, some staff, and success managers watching accounts. |
| **Cookies you get** | You keep the kids in pile #2. Also, customers who reach full value renew, buy more, and refer other carriers. |
| **How long until treats** | Faster. You can see results with the *next group* of new customers within a few months, as time-to-value drops. You can also rescue current customers stuck mid-implementation right away. |
| **Could a big dog eat them?** | Two dogs. First, if the real problem is pile #1, you've built a lovely line for lemonade people still don't want. Second, if you fix it mostly by hiring more people, costs grow with every customer and margins suffer. |

**Where more money stops getting candy:** Adding helpers to a process where every implementation is custom-built from scratch. Extra hand-holding can also hide a product that's simply hard to use, and pouring effort into customers who were a bad fit won't save them either.

## Who Holds the Piggy Bank?

**Not either VP.** Each one would be grading their own homework, and each honestly believes their idea is right.

- **Who holds it:** One person who owns *keeping customers*, not building features or running services. That's usually the CEO, a GM, or a Chief Customer/Revenue Officer. Since you run customer success, you're a natural person to propose and run the diagnosis, even if someone above you owns the final budget.
- **Who counts the coins:** Finance or RevOps, tracking a shared scorecard both VPs agree to up front:
  - Gross and net revenue retention, by customer group
  - Time from contract signing to go-live and to "first real value"
  - Percentage of customers fully implemented
  - Adoption of the analytics features you *already have*
  - Coded churn reasons, checked against actual usage data
- **Who says "stop buying":** Agree on stop rules *before* spending. For example:
  - "If time-to-value hasn't dropped 30% in two quarters, we rethink the services plan."
  - "If fully implemented customers still churn at more than X%, product gaps are real and roadmap spending goes up."

## The Third Idea: Make the Lemonade Easier to Get and Better at the Same Time

This is where I'd put most of the allowance. **Spend product money on features that make implementation faster and value show up sooner.** That way both grown-ups are working on the same problem.

- **"Value in the box":** Pre-built setups and dashboards designed for regional carriers, so customers see useful analytics in week one instead of month nine.
- **Build the tools your services team keeps making by hand:** data migration tools, pre-built integrations with the policy systems carriers commonly use, and configuration templates.
- **Point AI at the painful parts of setup first**, like automatically mapping old claims data or suggesting configurations. That's a real AI story for sales, and it shrinks implementation time.
- **Consider partnering for fancy analytics** instead of building it all yourself, so you close the feature gap faster and cheaper.
- **Start a rescue squad now:** find current customers who are near renewal and not fully live, and get them to value before they leave.

This idea gets more treats because **every coin works twice.** It fixes the leak (Services) *and* makes the lemonade better (Product). And it doesn't break the piggy bank, because it doesn't depend on hiring more people for every new customer.

## What To Do, In Order

1. **Weeks 1–4:** Sort the churned customers into the two piles using real usage and implementation data. Present it to both VPs together.
2. **Right away, in parallel:** Launch the rescue squad for at-risk accounts near renewal.
3. **Weeks 4–6:** Agree on one piggy-bank owner, a shared scorecard, and stop rules.
4. **Next 2–3 quarters:** Put most new product money into implementation-speeding and value-in-the-box features. Fund only the competitive features that pile #1 shows are truly costing you deals and renewals.
5. **Check the scorecard every quarter**, and move money toward whichever idea is actually producing cookies.

**Grown-up version in one sentence:** Diagnose churn by whether departing customers ever reached value, put one retention owner in charge with shared metrics and pre-agreed stop rules, and point product investment at shortening time-to-value, so the roadmap and onboarding fixes become the same plan instead of competing ones.

## Turn 2

**User:** What's in the rescue squad? Do they get capes?

**Assistant:**

# The Rescue Squad

**Yes, they get capes.** Small morale touches help, because this is hard, unglamorous work. But the real superpower is that **they can make things happen fast without waiting in line.**

## Who's on the Squad

Keep it small, about 3–6 people for a few dozen at-risk accounts:

| Role | What they do |
|---|---|
| **Squad lead (from your CS team)** | Owns the list, runs the weekly check-in, reports results. The captain. |
| **Senior implementation person** | Can diagnose *why* a customer is stuck and unstick it: data migration, configuration, integrations. |
| **A product person or engineer on call** | Fixes the small bugs and gaps blocking go-live. Not new features, just the pebbles in the shoe. |
| **A solutions or analytics person** | Shows customers the value they already paid for, like the dashboards and reports they never turned on. |
| **An executive sponsor** | Calls the customer's executive, clears internal roadblocks, and approves concessions. |

**The special power:** The squad jumps the queue. Their tickets go first, and engineering sets aside a small, fixed slice of time for them. Without that, they're just a group of people with capes waiting in the same line as everyone else.

## Who Gets Rescued

Look for kids who are **close to walking away and still worth saving:**

1. **Renewal in the next 6–12 months.** Claims software has long decision cycles, so 90 days out is usually too late.
2. **Not fully live, or live but barely using it.** Stalled implementation, low logins, or key modules like analytics never turned on.
3. **Warning signs:** Support ticket spikes, an unhappy champion, a new executive at the carrier, questions about contract terms, or silence where there used to be activity.

Then sort them:

- **Red:** Worth a lot, at high risk. Rescue first.
- **Yellow:** Moderate risk. Give them a lighter version of the playbook.
- **Gray:** Poor fit or already decided. Be honest about these. Some kids have already left the stand, and chasing them eats cookies you could save elsewhere.

## The Rescue Playbook

**Step 1: The honest check-in (week 1–2).**
Your executive calls theirs. Say something like: "We know this hasn't gone the way we promised. We want to fix it. What would success look like for you in 90 days?" Listen more than you pitch.

**Step 2: Diagnose what's really wrong (week 2–3).**
Is it stuck implementation? Missing training? A real feature gap? A relationship problem? Write it down in plain words.

**Step 3: The 90-day get-well plan.**
A short, written plan both sides sign off on:
- 2–4 concrete outcomes, like "Adjusters using the system for all new auto claims," not "improve adoption"
- Who does what by when, on both sides
- A weekly or biweekly check-in

**Step 4: Deliver visible wins fast.**
Pick the quickest thing that makes a claims manager's day better, and do it in the first few weeks. Early proof buys patience for the harder fixes.

**Step 5: Reach the finish line.**
Close out the plan with a review meeting: "Here's what we promised, here's what we did, here's the value you're getting." This conversation sets up the renewal.

## The Squad's Tool Belt

Agree ahead of time on what the squad can offer, so they don't have to ask permission for every cookie:

- Free implementation or configuration help to finish stalled setups
- Training for the carrier's users, ideally on-site for key teams
- A named senior contact and faster support
- Early access to relevant roadmap items, but only with honest timelines
- **Commercial concessions as a last resort:** a contract extension, a service credit, or a short-term discount tied to hitting the plan's milestones

**Warning:** Don't lead with discounts. If the customer isn't getting value, a cheaper version of the same problem still churns next year.

## Counting the Coins

Track these every week:

- **Number of at-risk accounts moved from red to yellow to green**
- **Revenue saved:** at-risk revenue that renews
- **Time to unblock:** how fast stalled implementations get moving again
- **Adoption change** in rescued accounts
- **Why accounts were stuck**, coded and counted

## Stop Rules

- **Per account:** If a red account shows no real movement after about 60 days, or the customer won't engage, step back to a lighter-touch approach.
- **For the squad:** Review after one or two quarters. If it's saving meaningful revenue, keep it going and keep feeding it. If not, figure out why before spending more.

## The Hidden Treasure

The squad does more than save accounts. **It's your best diagnostic tool.** Every rescue tells you exactly why customers get stuck, which answers the question the two VPs are arguing about.

If the squad keeps finding the same five implementation problems, those are your first "value in the box" projects. If they keep hitting real feature gaps that block renewals, the Product VP has evidence for their roadmap.

**So the capes matter less than the notebook.** Have the squad write down every problem they find, count them, and bring them to the leadership meeting. The rescue squad saves this year's cookies, and its notebook tells you how to stop the leak for good.

## Turn 3

**User:** Does the squad get to eat the cookies they save?

**Assistant:**

# Yes, the Squad Gets Cookies, But Count Them Carefully

The squad should share in what they save. It's hard work and they should be rewarded for it. But **how you hand out cookies changes what the squad does.** Reward the wrong thing and you get the wrong behavior.

## How Cookie Rewards Can Go Wrong

| If you reward... | The squad might... |
|---|---|
| **Revenue saved, full stop** | Give away big discounts to get signatures. You "save" the account but lose a chunk of the cookies. |
| **Number of accounts saved** | Pick the easy rescues and avoid the hard, valuable ones. |
| **Moving accounts off the red list** | Quietly label healthy accounts "red" at the start so they're easy to "rescue." |
| **This year's renewal only** | Patch things just enough to renew, then the customer churns next year anyway. |

None of this requires bad people. It's what happens when the reward is easier to hit than the real goal.

## A Better Cookie Jar

**1. Pay on cookies kept, minus cookies given away.**
Measure saved revenue *after* discounts and credits. A $200K renewal at a 40% discount isn't the same win as a full-price renewal.

**2. Someone else decides who's at risk.**
RevOps or finance sets the at-risk list and the risk levels *before* the squad starts, using agreed rules. The squad doesn't get to grade its own starting line.

**3. Check the cookies again later.**
Pay part of the reward at renewal and hold part back for 6–12 months. The second part pays out if the account is still healthy: live, adopted, not flagged red again. This rewards real rescues over temporary patches.

**4. Reward value, not just signatures.**
Tie part of the reward to hitting the get-well plan's milestones, like reaching go-live or getting adjusters actively using the system.

**5. Share the jar as a team.**
Make most of the reward team-based. One person gets the renewal signature, but it took the implementation specialist, the engineer, and the executive sponsor to earn it. Individual rewards for single saves create turf fights over who "owns" the win.

**6. Pay for the notebook too.**
The squad's diagnostic work is part of their value. Recognize it, not just the saves.

## Not All Rewards Are Cookies

Money matters, but some of the best rewards aren't cash:

- **Visibility:** Squad members present their findings to leadership. That's career fuel.
- **Career paths:** Squad experience should count toward promotion. It's some of the hardest customer work in the company.
- **Rotation:** Rotating people through the squad spreads the skills and prevents burnout. Rescue work is draining.
- **Yes, the capes:** Small, silly recognition builds team identity. It works better than people expect.

## Don't Forget the Rest of the Stand

If only the squad gets rewarded for retention, you create a problem: everyone else may feel that keeping customers is *the squad's job*.

- Put a **company-wide retention goal** in the bonus plans for Product, Services, Sales, and CS, so everyone shares the jar.
- Credit the **people who prevent problems** in the first place, like the implementation team that gets customers live fast. Their customers never need rescuing, so their wins are invisible unless you look for them.
- Watch for **sales promising things** that create future rescues. If a rep oversells a custom setup, some of the cost of that rescue should show up on their side of the ledger.

## The Short Version

**The squad eats some of the cookies they save, but:**
- counted after any cookies they gave away,
- from a list they didn't write themselves,
- with some held back until the customer stays happy,
- shared as a team,
- and with the whole stand eating from the same jar, so everyone wants fewer customers to need rescuing.

The best sign the squad is working isn't a lot of heroic saves. **It's a squad that slowly runs out of customers to rescue.**

## Turn 4

**User:** If the squad runs out of kids to rescue, are they sad? Do they get to go play?

**Assistant:**

# When the Squad Runs Out of Rescues

**They shouldn't be sad, as long as you tell them from day one that running out of rescues is winning.** If people fear the squad disbanding means losing their jobs or status, they'll quietly keep finding "emergencies." So promise a good landing up front: "When this works, you'll be the people who help build what comes next."

## Honestly, the List Rarely Hits Zero

Even a great lemonade stand has the occasional unhappy kid. Carriers get new executives, merge, cut budgets, or hit strange problems. So the squad usually doesn't disappear. **It shrinks from an emergency team into a small, always-ready one.**

## Signs It's Time to Shrink

- Fewer new accounts landing on the red list each quarter
- New customers going live faster, with fewer stalling mid-implementation
- The squad's notebook showing the *same* problems less often
- Squad members with open time on their calendars

## Where the Squad Members Go Play

Their experience is valuable, so put it where it prevents the next leak:

| Where they go | What they do there |
|---|---|
| **Onboarding and implementation** | Fix the process upstream so customers never get stuck in the first place. |
| **Product ("value in the box")** | Help design the templates, migration tools, and setup features they wished they'd had during rescues. |
| **Customer health monitoring** | Build the early-warning system that spots trouble months sooner. |
| **Sales and scoping** | Help set honest expectations in deals, so fewer customers are oversold into a rough start. |
| **Leadership roles** | Some will be ready to run teams. Rescue work teaches a lot fast. |

A small core, maybe one or two people plus on-call experts, stays as the standing squad for the rare real emergency.

## Keep the Notebook Open

The most important thing to keep isn't the team. **It's the habit.** Someone should still track why customers get stuck, count it, and bring it to leadership every quarter. Without that, the old problems creep back quietly, and 18 months from now you're forming a new squad.

## Throw a Party

Mark the win. Share the numbers: revenue saved, accounts turned around, problems fixed for good. Thank the squad in front of the company, and let them keep the capes. It tells everyone that preventing problems is valued as much as heroics.

**So yes, they get to go play,** mostly on the parts of the stand that keep future kids from ever needing rescue. A squad that works itself out of a job has done exactly what you built it to do.

## Turn 5

**User:** What should we do?

**Assistant:**

# What To Do

Stop arguing about which VP is right and **find out, while saving the customers you can right now.** Then spend on what the evidence shows, favoring work that fixes both problems at once.

## This Week

1. **Pull the list of every customer who churned in the last 18 months.** For each one, note whether they fully went live, how long implementation took, and how much they used the product, especially the analytics you already have.
2. **Pull the list of customers renewing in the next 12 months** who aren't fully live or are barely using the product. These are your first rescues.
3. **Ask your CEO (or whoever owns the budget) to name one owner for retention**, not either VP, and propose yourself to run the diagnosis.

## Weeks 1–4: Diagnose and Start Rescuing

- **Sort churned customers into two piles:** left after reaching value (points to product gaps) versus never reached value (points to implementation and service).
- **Check timing:** did churn jump with a competitor launch, or with implementation backlogs and staff changes?
- **Stand up the rescue squad** for your highest-value at-risk accounts: a CS lead, a senior implementation person, an engineer on call, an analytics person, and an executive sponsor. Give them queue-jumping power.
- **Present the findings to both VPs together**, as shared evidence rather than a verdict against either one.

## Weeks 4–6: Set the Rules

- **Agree on a shared scorecard:** gross and net retention, time-to-value, percentage fully live, adoption, and coded churn reasons.
- **Agree on stop rules before spending**, for example: "If time-to-value doesn't drop 30% in two quarters, we rethink," and "If fully implemented customers still churn above X%, we shift more money to the roadmap."
- **Set squad rewards carefully:** team-based, measured after discounts, with part held back until customers stay healthy.

## Next 2–3 Quarters: Spend Where It Works Twice

- **Put most new product money into shortening time-to-value:** carrier-ready templates, data migration tools, integrations with common policy systems, and dashboards that work in week one. Use AI on setup pain first.
- **Fund only the competitive features the evidence shows are actually costing you renewals.** Consider partnering for advanced analytics instead of building it all.
- **Fix onboarding upstream** using what the rescue squad learns, so fewer customers get stuck.
- **Review the scorecard every quarter** and move money toward whatever is working.

## What I'd Bet On

Most of your churn is likely customers who never reached full value, with some real feature gaps mixed in. If so, fixing implementation and building features that speed it up will pay off faster and cheaper than racing competitors on AI. But **let your churn data confirm that before you commit the big money.** The diagnosis takes a month and costs almost nothing.

**One sentence:** Diagnose churn by whether customers ever reached value, rescue at-risk accounts now, put one person in charge of retention with shared metrics and stop rules, and aim the roadmap at getting customers to value faster.

## Outcome summary (sent to Jev)

The recommendation is to stop debating which VP is right and find out cheaply, while rescuing at-risk customers now. The assistant's bet is that most churn comes from customers who never reached full value, with some real feature gaps mixed in, but the churn data should confirm this before big money is committed.

The core test is to sort every customer who churned in the last 18 months into two piles. Customers who went live, used the product, and left anyway point to product gaps. Customers stuck in long implementations or barely using existing analytics point to implementation and service. The timing of the churn jump also matters: did it follow a competitor launch, or implementation backlogs and staff changes? The diagnosis takes about a month and costs almost nothing. Exit reasons shouldn't be taken at face value, since "better AI" is an easy excuse, and customers can't see features they never turned on.

In parallel, a small rescue squad with queue-jumping power should target high-value accounts renewing within 6–12 months that aren't fully live. Its rewards should be team-based, measured after discounts, and partly held back until accounts stay healthy. Its notebook of why customers get stuck doubles as diagnostic evidence.

Budget authority should go to a single retention owner rather than either VP. That owner would use a shared scorecard covering retention, time-to-value, percent fully live, adoption, and coded churn reasons, with stop rules agreed before spending.

The favored "third idea" is to aim most new product money at shortening time-to-value, where every coin works twice:

* carrier-ready templates
* migration tools
* integrations with common policy systems
* week-one dashboards
* AI applied to setup pain

Competitive features should be funded only where evidence shows they cost renewals, possibly through partnerships. Building more features first is slower and riskier, because they must pass through the same painful implementation. Money should shift quarterly toward whatever works.
