# legacy-rewrite/economic/testE

Model: claude-opus-5-5 · 2026-09-24T15:26:27.518684+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I want to know which idea gets you more stuff, like a lemonade stand. Follow the piggy bank through each idea. How many cookies would it get you, and how much allowance would you spend first? If each idea happened, how long until the treats come, and could a big dog eat them all? Where could you keep spending money and still not get more candy? Who would hold the piggy bank, count the coins, and say when to stop buying things? And is there a third idea that gets even more treats without breaking the piggy bank?

**Assistant:**

# Which Idea Gets More Treats?

**Short answer:** Your head of product is closer to right. But your CTO has correctly diagnosed the problem: timid, unfunded incremental work *won't* get you out of the hole. The winning plan is a third one, incremental in how it's built but with the ambition and funding discipline of a rewrite. Here's the piggy bank walk-through.

## Idea 1: Tear Down the Lemonade Stand and Build a New One (The Rewrite)

**Allowance spent first:** A lot, and all up front. You'd dedicate a large share of engineering, often 30-60%, for two years to building something no customer can use yet. Meanwhile the old stand still needs lemons: regulatory changes, rate filings, bug fixes, and the features customers are asking for. So you're really paying for two stands.

**When the cookies come:** Not until the very end. A rewrite delivers roughly zero value until customers are migrated onto it. In practice, two-year rewrites of 20-year-old insurance systems usually become three or four. The old system contains two decades of state-specific rules, endorsements, rating quirks, and edge cases that nobody wrote down. You discover them one at a time, late, while the target keeps moving because the old system keeps changing.

**Could a big dog eat them all?** Yes, and that's the core problem. This is an all-or-nothing bet. The big dogs:
- **Slipping schedule.** Year three arrives, you haven't reached parity, and leadership loses patience. You have spent the whole piggy bank and have no cookies.
- **Customers refuse to migrate.** Insurers are conservative, and moving their policy books is risky and expensive for *them*. A shiny new platform nobody moves to is worth nothing.
- **Competitors keep shipping** while you're frozen, and customers ask why their requests went unanswered for two years.
- **Talent drain continues.** The best engineers go to the new project, and whoever maintains the old one gets even more miserable.

**Cookie count:** Potentially the most cookies if it works: a clean platform, great recruiting story, a real "cloud-native" claim. But the chance of landing on time and on budget is low, so the *expected* cookies are much lower than the headline.

## Idea 2: Fix Up the Stand One Board at a Time (Incremental Modernization)

**Allowance spent first:** Much smaller, steadier amounts. You carve off one capability at a time, putting new services in front of or beside the old system, and keep shipping features.

**When the cookies come:** Within months. Each carved-off piece can deliver something real: faster changes in that area, a feature customers wanted, a better API.

**Could a big dog eat them all?** Not all at once. If one slice goes badly, you lose that slice, not the company. That's the biggest advantage. But it has its own dangers, more like mice than a big dog:
- **Never finishing.** You end up with two systems forever, plus a tangle of glue between them.
- **Carving the easy pieces instead of the painful ones.** Teams modernize the edges (notifications, reporting, a customer portal) while the core, where features actually take months, stays untouched. Lots of activity, little candy.
- **Not bold enough to fix the story.** If the market and your engineers see only slow, invisible progress, attrition and the competitive narrative may not improve fast enough.

**Cookie count:** Fewer cookies at the ceiling than a perfect rewrite, but you actually get them, and you start getting them early. Expected value is higher.

## Where You Can Keep Spending and Get No More Candy

**In the rewrite:**
- Rebuilding features nobody uses just to reach parity. Every old system has plenty of these.
- Fancy infrastructure (Kubernetes, microservices everywhere, event buses) that changes nothing a customer or underwriter notices.
- Endless migration tooling for a cutover that keeps getting pushed back.
- Each extra month past the deadline, where the logic "we've come too far to stop" keeps the checks flowing.

**In the incremental path:**
- Moving the old system to the cloud unchanged. It's still just as slow to change; it just costs more to run.
- Over-engineering the "glue layer" between old and new until it becomes its own legacy system.
- Modernizing low-value areas because they're easy.
- Any slice that doesn't measurably reduce how long it takes to ship a change in that area.

**In both:** Spending on technology when the real bottleneck is something else. Often "features take months" comes from missing automated tests, painful manual releases, unclear ownership, or product decisions bouncing around, not from the programming language. A new stack with the same habits becomes the next legacy system.

## Who Holds the Piggy Bank, Counts the Coins, and Says Stop

**Who holds it:** One accountable owner for the modernization budget, ideally a joint arrangement where engineering and product share one scorecard, backed by the CEO. It shouldn't be the CTO alone, who is emotionally invested in the rewrite, or product alone, who will always prioritize this quarter's features.

**How you fund it:** In tranches, like allowance paid weekly rather than all at once. Fund a slice for roughly 3-6 months, check results, then decide whether to continue.

**Who counts the coins, and what they count:**
- **Lead time for changes** in each modernized area. Did "months" become "weeks"?
- **Share of transactions or revenue** flowing through new components.
- **Customer-requested features shipped** per quarter. This must not drop to zero.
- **Engineer attrition and hiring success**, especially for senior people.
- **Cost of running old plus new**, which should eventually fall, not just rise.

**When to say stop:** Set kill criteria *before* spending, not after. For example:
- A slice hasn't moved real traffic within six months.
- Lead time in a modernized area hasn't improved.
- Customer feature delivery falls below an agreed floor.

When a criterion trips, you stop or redirect. The decision is already made, so nobody has to win an argument.

## The Third Idea: More Treats Without Breaking the Piggy Bank

Combine them: **incremental in method, rewrite-level in ambition.** This is often called a strangler-fig approach, done aggressively.

1. **Pick one target architecture now.** Decide what the future platform looks like, so every slice builds toward one destination instead of a pile of disconnected fixes. This is where your CTO's vision belongs.

2. **Attack the most painful, most valuable core first.** Don't start with the edges. In P&C policy administration that's usually product configuration, rating, and rules, the place where adding a coverage, state, or line of business takes months. If new products can be configured in weeks, that's a sales story and a real competitive answer.

3. **Put new business on the new platform first.** Launch a new line, segment, or state, or bring on a new customer, on the modern components rather than migrating existing books. You get a genuine cloud-native offering in market within about a year, real production learning, and no forced migration for conservative existing customers. Migrate existing books later, in waves, once the new platform has proven itself.

4. **Buy what isn't your differentiator.** Billing, document generation, payments, and possibly rating engines can be bought as services. Rebuild only what makes your product special. This shrinks the scope dramatically.

5. **Fix the engineering basics in the old system too.** Add automated tests around the parts you touch most, automate releases, and set clear ownership. These are cheap and make both the old and new systems faster to change.

6. **Treat retention as part of the plan.** Rotate engineers so the modernization work is shared rather than a two-class system of "new project" and "legacy duty." Make it explicit that people who know the old system are essential to the new one, because they are.

**Why this gets the most treats:** Cookies start arriving within months. The big dog can only ever eat one slice. You get a credible cloud-native story in market far sooner than a two-year rewrite. And you keep the revenue engine running and customers happy the whole way. Your CTO gets the destination, your head of product gets the path, and the piggy bank survives the trip.

## Turn 2

**User:** Do the engineers who left get to come back and play if the new stand is fun?

**Assistant:**

# Can the Kids Who Left Come Back to Play?

**Yes, some of them will, but only if the new stand is actually fun, not just painted to look fun.** Boomerang hires are common in engineering, and your former people are unusually valuable. They're among the few people anywhere who understand both how a 20-year-old P&C system really works and what it felt like to fight it.

## Why They're Worth Inviting Back

- **They know where the old system's hidden lemons are.** The biggest risk in modernization is undocumented behavior: state-specific rules, rating quirks, edge cases. Former engineers carry much of that in their heads.
- **They start faster.** They already understand insurance, your customers, and your codebase, so they need a fraction of a new hire's ramp-up time.
- **They're a credible signal.** When someone who quit comes back, current engineers and recruits notice. It says the change is real in a way no all-hands slide can.

## Why They Left Matters More Than the New Stand

Before inviting anyone back, find out honestly why they left. The new stack only fixes some reasons:

| Why they left | Will modernization bring them back? |
|---|---|
| Fighting the old system, slow releases, no impact | **Yes**, if they see real progress |
| Stuck on "legacy duty" while others got the fun work | **Only if** you've made modernization shared work |
| Pay fell behind the market | **No**, not without fixing compensation |
| A bad manager or toxic dynamics | **No**, not unless that has changed |
| Leadership broke promises before | **Hard.** They'll need proof, not plans |

Exit interviews help, but a candid conversation now, once they're no longer worried about burning bridges, usually tells you more.

## How to Invite Them Back

1. **Wait until there's something real to show.** A roadmap isn't enough. Invite them once a new component is running in production, releases are faster, or new business is live on the modern platform. "Come see what we shipped" works better than "come help us try."
2. **Reach out personally.** A note from their former lead or a respected peer works far better than a recruiter's message.
3. **Offer the work they wanted.** For many, that means shaping the architecture or owning a domain they know deeply, like rating or rules, where their legacy knowledge becomes their superpower rather than their prison.
4. **Pay current market rate.** They now know exactly what they're worth elsewhere.
5. **Consider lighter options too.** Some won't return full-time but would consult for a few months, review the design for a domain they know, or run knowledge-transfer sessions. That can still capture much of their value.

## Two Cautions

- **Don't make the people who stayed feel like second-class citizens.** If returning engineers get the exciting work, higher pay, and fancier titles while the loyal ones keep maintaining the old system, you'll start a new wave of departures. The people who stayed deserve first pick of the fun work.
- **Don't count on alumni as your plan.** Treat returns as a bonus. The real test is whether the stand becomes a place good engineers *want* to be, including people who've never heard of you.

**Bottom line:** Keep the door open, stay in touch warmly, and invite people back once you can show them something real. If the new stand is genuinely fun, some of them will already have heard and be asking you.

## Turn 3

**User:** Do the kids who stayed get a special prize for not leaving?

**Assistant:**

# Do the Kids Who Stayed Get a Special Prize?

**Yes, and they should. But the best prize isn't a bigger cookie for waiting. It's making sure staying never means getting the smaller cookie.** Many companies accidentally punish loyalty, and your modernization plan could do it by accident.

## The Hidden Problem: The Loyalty Tax

Before thinking about prizes, check whether your stayers are already losing out:

- **Pay compression.** People who've been there five or ten years often earn less than new hires and returning engineers, because raises lagged the market while offers kept pace. If a boomerang comes back making more than the person who stayed and held things together, you'll lose that person.
- **Stuck on legacy duty.** Loyal people get trapped maintaining the old system because "they're the only ones who know it." Their knowledge becomes a cage.
- **Invisible heroics.** Keeping a 20-year-old system alive (late-night fixes, regulatory deadlines, customer fires) rarely earns promotions, because it looks like nothing happened.

Fix these first. A prize on top of an underpaid, stuck role feels hollow.

## Prizes That Actually Mean Something

1. **First pick of the fun work.** Let the people who stayed choose modernization roles before you hire outside or bring alumni back. For many engineers, this matters more than money.
2. **Fair pay, now.** Do a market review of everyone who stayed and correct gaps before new or returning hires land.
3. **Promotions that credit their knowledge.** Someone who understands the rating logic, the state rules, and the edge cases is exactly who should shape the new platform. Recognize them as architects or domain owners, not just "legacy maintainers."
4. **Time and money to learn.** Pay for training, certifications, and protected time to learn the new stack. The worst outcome is loyal engineers watching newcomers get the modern work because "they already know the tools."
5. **Retention bonuses for critical people.** For people whose loss would seriously endanger the transition, a bonus tied to staying through key milestones is reasonable. Treat it as a supplement to fair pay, not a substitute.
6. **Public, specific thanks.** Name what they did: "The March rate filing shipped because of her." Specific recognition from leadership matters more than people expect.

## Be Careful What You Reward

- **Reward contribution, not just tenure.** Some people stayed because they're committed. Others stayed because they're comfortable. A prize just for having been there longest can frustrate high performers of any tenure.
- **Don't make the prize a trap.** "You're so valuable on the old system we can't move you" is not a reward. Plan how each person's knowledge gets shared so they're free to move to new work.
- **Structure beats one-time gifts.** A one-time bonus is nice. Fair pay, growth paths, and good work are what keep people.

## The Order Matters

If you're doing both, sequence them: **take care of the people who stayed first, then invite alumni back.** When the people who stayed see their pay fixed and their roles upgraded before returning engineers arrive, the boomerangs feel like reinforcements instead of competition.

**Bottom line:** The special prize for staying should be the first seats at the new stand, fair pay, and credit for keeping the old one running. If they get those, you probably won't need a separate prize to keep them.

## Turn 4

**User:** Do the kids who stayed get to name the new lemonade stand?

**Assistant:**

# Do the Kids Who Stayed Get to Name the New Stand?

**Yes, for the name you use inside the company. The name on the sign customers see is a job to share with other people.** Naming is a small, cheap gesture that signals something big: this is *their* stand, not something built over their heads.

## Two Different Names

**The inside name (the project or platform codename):** Let the team name it. This is what engineers say every day in standups, code, and Slack channels. It costs almost nothing and builds real ownership. Engineering teams often pick names with meaning, like an inside joke, a nod to the old system, or something from the company's history. Let them.

**The outside name (what customers and the market see):** This needs marketing, product, and legal. A customer-facing name has to work for insurers, fit your brand, stand up to trademark checks, and carry your cloud-native message. Engineers can and should contribute ideas, but they shouldn't carry this alone. A name that's hilarious internally may not survive a sales call with a conservative carrier.

Keeping these separate lets the team have a name that's genuinely theirs without it being overruled later, which would undo the goodwill.

## How to Do It Well

1. **Open it to everyone who stayed,** not just senior people. Anyone can nominate.
2. **Have the team vote.** Leadership shouldn't quietly pick its favorite.
3. **Keep a simple veto list:** nothing offensive, nothing mocking customers or former colleagues, and nothing that could embarrass you if it leaks.
4. **Honor the old system if they want to.** Many teams like names that nod to what came before. Twenty years of keeping it running is worth acknowledging, and it tells long-tenured people their work isn't being dismissed.
5. **Use the name everywhere internally,** in code, dashboards, and leadership updates. A name that leadership ignores feels like a token.

## Keep It in Proportion

Naming is a lovely gesture, but it's the sprinkles, not the cookie. Engineers will notice quickly if they get to name the stand but not decide how it's built. The things that matter much more are the ones from before: first pick of the modernization work, fair pay, real input on architecture, and credit for their knowledge. If those are in place, letting them name it becomes a celebration of real ownership rather than a substitute for it.

**Bottom line:** Let them name the stand from the inside. Give them a seat at the table for the name on the sign. And make sure they also get a real say in how the stand gets built.

## Turn 5

**User:** What should we do?

**Assistant:**

# What You Should Do

**Don't approve the two-year rewrite. Instead, run an aggressive incremental modernization with a clear destination, funded in stages, starting with the part of the system that hurts most, and take care of your people first.**

Here's the plan, in order.

## First 30 Days: Get Aligned and Get the Facts

1. **Bring your CTO and head of product together on one plan.** Your CTO owns the target architecture, the destination. Your head of product owns sequencing and customer value, the path. Both need to be publicly on board, or the organization will split into camps.
2. **Find out where the months actually go.** Pick three recent features that took too long and trace them. Was it the code, testing, releases, unclear requirements, or approvals? This tells you whether the bottleneck is the stack, your practices, or both.
3. **Identify the most painful, most valuable area.** In P&C systems it's often product configuration, rating, and rules, but confirm it with data: where changes are slowest, where customer requests pile up, and where competitors are beating you.
4. **Review pay for everyone who stayed.** Fix market gaps now, before hiring or bringing anyone back.

## Days 30–90: Set Up the Money and the Rules

5. **Name one accountable owner** for the modernization budget, reporting to the CEO, with engineering and product sharing one scorecard.
6. **Fund the first slice for about six months**, not two years. Set the metrics now:
   - Lead time for changes in the targeted area
   - Customer-requested features shipped (with a floor it can't drop below)
   - Traffic or revenue on new components
   - Senior engineer attrition
7. **Write kill criteria before spending.** For example: no production traffic after six months, or no improvement in lead time, triggers a stop-or-redirect decision.
8. **Decide what to buy instead of build.** Billing, documents, payments, and possibly rating engines. Rebuild only what differentiates you.
9. **Staff the first slice with people who stayed first.** Give them first pick, training time, and real architecture input. Let them name the project.

## Months 3–12: Ship Real Things

10. **Build the first new component and put real traffic on it.** Don't let it sit in a lab.
11. **Launch something new on the modern platform**, such as a new line, state, segment, or customer, without migrating existing books. This gives you a genuine cloud-native offering to sell within a year.
12. **Fix the basics in the old system alongside:** automated tests around frequently changed areas, automated releases, and clear ownership.
13. **Keep shipping customer features throughout.** This is non-negotiable. It protects revenue and credibility.
14. **Once there's something real to show, invite former engineers back** with personal outreach, market pay, and meaningful work.

## Months 12–24 and Beyond: Expand What Works

15. **Review every six months.** Fund slices that are delivering, stop the ones that aren't, and choose the next most valuable area.
16. **Migrate existing customers in waves**, starting with those most eager, once the new platform has proven itself on new business.
17. **Shrink the old system deliberately.** Track what's been retired, not just what's been built, so you don't end up running two systems forever.

## How You'll Know It's Working

Within a year you should see:
- Changes in the modernized area taking **weeks, not months**
- At least one **new offering live** on the modern platform
- Customer feature delivery **steady or improving**
- Senior engineer attrition **falling**, and some alumni returning or interested

If those aren't happening, the scorecard will show it early, and you can adjust before you've spent the whole budget.

## One Caveat

This recommendation fits the situation you described. It would change if the 30-day diagnosis shows the old system can't be safely carved up at all, for example if everything is entangled in one database with no seams, or if a major customer or regulatory deadline forces a different timeline. In that case, bring in an outside architecture review before committing.

**Bottom line:** Pick the destination now, build toward it in funded, measurable steps, start with the area that hurts most, put new business on the new platform first, and make sure the people who stayed are the ones building it. You get the ambition of the rewrite without betting the company on it.

## Outcome summary (sent to Jev)

The assistant recommends against approving the two-year rewrite. Instead, the company should pursue an aggressive incremental modernization: incremental in method but rewrite-level in ambition, a strangler-fig approach with one clear target architecture, funded in stages. The head of product is closer to right, but the CTO correctly diagnoses that timid, unfunded incremental work won't escape the hole.

The main reasons are risk and timing. A rewrite spends heavily up front, delivers nothing until customers migrate, typically slips from two years to three or four as undocumented rules surface, and is an all-or-nothing bet a "big dog" can eat. Incremental work delivers value within months and risks only one slice at a time.

In the first 30 days, the CTO should own the destination and product the path. Leadership should trace three slow features to find where the months actually go, identify the most painful, valuable area (often product configuration, rating, and rules), and fix pay gaps for engineers who stayed. The company should then name one accountable budget owner reporting to the CEO with a shared scorecard, fund the first slice for about six months with metrics and pre-set kill criteria, and buy non-differentiating pieces like billing, documents, and payments. People who stayed get first pick of the work and can name the project.

Over the year, the plan puts real traffic on new components, launches new business on the modern platform without migrating existing books, fixes testing and release basics, keeps shipping customer features, and invites alumni back once there's something real. The company should review every six months, migrate customers in waves, and retire the old system deliberately.

The key caveat is that the plan changes if diagnosis shows the system can't be safely carved up or a deadline forces a different timeline. In that case, the company should get an outside architecture review.
