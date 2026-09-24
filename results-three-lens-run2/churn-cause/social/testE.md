# churn-cause/social/testE

Model: claude-opus-5-5 · 2026-09-24T15:33:30.918900+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to know which idea makes more people want to be your friend. Think about how each idea would look to kids at work and kids outside. Who gets a gold star, and who gets in trouble or says sorry? If each idea happened, would the boss, the helpers, the customers, and everybody's moms think it was cool? Where might wearing a cape or being loud matter more than doing chores? Who would sit together at lunch because of each idea? And is there a third idea where everybody gets to play and nobody feels left out?

**Assistant:**

## The short answer

Neither VP has shown they're right yet, and it may be both. Each is offering a belief that also happens to justify more budget for their own team. Your best move is to be the person who answers the question with evidence rather than picking a side. Churn data can usually settle this within 30–60 days.

## Part 1: Figuring out which belief is right

**1. Check whether churned customers ever reached full value.** This is the single most diagnostic cut. Split churned accounts by:
- Did they fully go live, and how long did it take versus the plan?
- Did they adopt the features you already have, including your existing analytics?
- Usage depth in the 6 months before renewal

How to read the results:
- **If churners mostly never fully implemented or adopted**, the Services story wins. A customer who never used your current analytics isn't leaving because your analytics are weaker than a competitor's.
- **If churners were fully live, heavily using the product, and still left for a competitor**, the Product story wins.
- **If it's mixed**, you'll likely see the interaction effect described below.

**2. Ask what changed 18 months ago.** Churn doubling suggests a shift, not a slow decline. Candidates include:
- A competitor launching AI or analytics features
- Turnover on your implementation team
- A move toward larger or more complex carriers
- Changes in how sales scopes deals
- A major release or migration
- Pricing changes

Line the timeline up against churn by cohort.

**3. Get honest exit reasons.** Customers often say "missing features" because it's polite and easy to say. "Your implementation burned us out" is harder to say to your face. A third-party win/loss interviewer typically gets the truer answer. Talk to the carrier's claims operations lead, not just the executive sponsor.

**4. Look for the likely combined story.** At regional carriers, a common pattern looks like this:
1. A long implementation, often slowed by core-system integration and data migration, means the customer never sees ROI.
2. At renewal, their leadership, who are also under board pressure about AI, sees a competitor's AI demo.
3. The weak value makes the shiny alternative easy to justify.

In that case, service is the root cause and features are the trigger.

## Part 2: The popularity and politics questions, translated

**Who gets a gold star, and who says sorry?**
- **Product story:** Product gets the gold star and a bigger budget. The implied apology is mild: "we were a bit behind the market." Services and Sales are let off the hook.
- **Services story:** This is the more uncomfortable one, which gives it some credibility. It points fingers at several teams:
  - Sales, for overpromising or underscoping
  - Implementation, for slow delivery
  - Product, for software that's hard to configure

  Notably, your VP of Services is partly indicting their own area. That's worth noticing.

**Cape versus chores (visibility versus substance).**
- AI features are the cape. They're announceable, press-release friendly, and exciting to the board, investors, and prospects.
- Onboarding fixes are chores. They're invisible, slow to show results, and hard to celebrate.
- The risk is that the organization picks the cape because it's more fun to present, even if the chores are the actual fix.
- Improvement in churn from the chores shows up at renewal, 12 or more months later. That makes them easy to underfund.

**Who would think each idea is cool?**

| Group | Features / AI | Fix onboarding and service |
|---|---|---|
| CEO / board | Very appealing, fits the AI narrative | Appealing only if framed as retention economics |
| Sales / marketing | Loves it, new things to sell | Mixed, since it may mean tighter scoping of deals |
| Implementation / support teams | Worried about more complexity to deploy | Relieved, if resourced; defensive, if framed as blame |
| Existing customers | Nice, but "make what I bought work first" | Strongly appreciated |
| Prospects | Very appealing | Hard to see before buying |
| Employees' families ("the moms") | Easy to brag about at dinner | Less exciting, but it's how people avoid burnout |

**Who sits together at lunch (coalitions)?**
- **The features coalition:** Product, Sales, Marketing, and probably the CEO.
- **The service coalition:** Services, Support, CS (you), and Finance, if you show that retention is cheaper than replacing lost revenue.
- **Your position:** You're the natural swing vote and neutral referee. You own the renewal data and the customer relationships. That gives you more influence here than either VP, as long as you stay evidence-led.

## Part 3: A third idea where everybody plays

**1. One shared scoreboard.** Make both VPs jointly accountable for:
- Net revenue retention
- Time-to-first-value, meaning days from contract to the customer's first meaningful outcome

When both teams are measured on the same thing, the fight turns into collaboration.

**2. Point the AI roadmap at the onboarding problem.** This lets Product keep its cape while doing the chores. Examples:
- AI-assisted data mapping and migration from legacy claims systems
- Configuration templates for common regional-carrier setups
- Analytics dashboards that work out of the box in week one, instead of after months of setup
- In-product guidance that drives adoption

These are real, marketable AI features that also shorten implementations.

**3. Run a joint 30-day churn diagnostic.** Co-sponsor it with both VPs and share the findings openly. Then split investment according to what the data shows, not according to who argued louder.

**4. Give everyone a win to announce.**
- Product ships "AI-powered implementation."
- Services gets resources and a cleaner handoff from Sales.
- Sales gets a faster time-to-value promise it can actually keep.
- The board gets both an AI story and a retention story.
- Nobody has to publicly lose.

**What to bring to your next leadership meeting:** "Before we fund either plan, give me 30 days to tell you whether our churned customers ever reached full value. That answer tells us where the money goes." It's hard for anyone to argue against, and it positions you as the person who solved it.

## Turn 2

**User:** Do the grown-ups get to eat cake when they stop fighting and play together?

**Assistant:**

Yes, but they should earn it at the right moments, and everyone should get a slice.

**When to cut the cake**

Churn improvements show up at renewal, often a year later. If you wait for that, the teams will lose patience long before there's anything to celebrate. So celebrate early signals that predict retention:

- **First cake:** The joint diagnostic is done and both VPs present the findings together. This rewards the truce itself.
- **Second cake:** Time-to-first-value drops meaningfully for a new cohort of customers.
- **Third cake:** A shipped feature measurably shortens implementations, such as AI-assisted data mapping cutting weeks off a go-live.
- **Big cake:** A carrier that was at risk renews, ideally with a quote from them about why.

**Who gets a slice**

Everyone who contributed, including the less visible people. The implementation specialist who fixed a messy data migration deserves as much recognition as the engineer who shipped the AI feature. If only the "cape" work gets celebrated, people learn that chores don't count, and the old fight comes back.

**Who hands it out**

Ideally the CEO, and in front of both teams together. Recognition from the top for the joint result, not for one side, signals that collaboration is what gets rewarded.

**One rule**

Don't serve cake just for announcing the plan. Celebrate evidence of progress, even small progress. That keeps the celebrations meaningful and the focus on customers actually getting value.

And yes, sometimes it should be literal cake. Shared food after a hard-won milestone does a surprising amount to make former rivals feel like one team.

## Turn 3

**User:** What kind of cake? Can it be chocolate with sprinkles?

**Assistant:**

Chocolate with sprinkles is an excellent choice. It's a crowd-pleaser, and sprinkles make everything feel like a celebration.

If you want to have a little fun with it:

- **Two-flavor cake:** Chocolate on one side, vanilla on the other, for Product and Services. It's one cake, so nobody can miss the point.
- **Sprinkles for everyone:** Each sprinkle is a small win that added up, which is exactly how retention improves.
- **Customer's choice:** For the big cake, ask the carrier who renewed what their favorite is. It's a nice reminder of who all this is for.

A practical tip: check for allergies and dietary needs so nobody's left out of the celebration. That would defeat the whole purpose.

So yes, chocolate with sprinkles. Your teams will have earned it.

## Turn 4

**User:** Can the customers come to the party too and bring their dogs?

**Assistant:**

Yes, customers should absolutely come. They might be the most important guests.

**Why inviting customers is a great idea**

- **They're the reason for the party.** Celebrating a smoother onboarding or a saved renewal with the customer makes the win feel real to your teams.
- **They tell the best stories.** A claims manager saying "we went live in half the time we expected" is more motivating than any dashboard.
- **It builds loyalty.** Customers who feel like partners, not just accounts, are much less likely to leave.

**Easy ways to include them**

- Invite a few happy customers to a team celebration, in person or on video.
- Start a customer advisory group where they help shape both the product roadmap and the onboarding process. That way both VPs hear from them directly.
- Host a customer celebration at your user conference or a regional meetup for carrier customers.

**And the dogs?**

If the venue is dog-friendly, why not? Dogs make any gathering friendlier. If bringing them isn't practical, a virtual party where everyone introduces their pet on camera works surprisingly well. Nothing breaks the ice between a software vendor and an insurance carrier like a golden retriever wandering into frame.

Just keep the chocolate cake away from the dogs. Chocolate is bad for them, so have some dog treats on hand so they can celebrate too.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the plan, from first step to cake.

**Next week: Propose a truce**
- Meet with both VPs together.
- Say: "Before we fund either plan, let's find out whether our churned customers ever reached full value. Give me 30 days."
- Ask the CEO to back the diagnostic so it has authority and neither VP feels ambushed.

**Days 1–30: Find the real answer**
- Pull churned accounts from the last 18 months and check whether they:
  - Fully went live, and how long it took
  - Used the features they already had, especially analytics
  - Showed usage decline before renewal
- Build a timeline of what changed 18 months ago: competitor launches, team turnover, bigger customers, sales process changes.
- Have a neutral third party interview 10–15 former customers about why they left.
- Present the findings jointly with both VPs, not as a verdict on either one.

**Days 30–60: Set shared goals**
- Make both VPs jointly own:
  - Net revenue retention
  - Time-to-first-value for new customers
- Split investment based on what the data showed.
- Prioritize AI features that speed up onboarding, like data mapping, setup templates, and out-of-the-box dashboards. This gives Product a shiny feature and fixes the service problem at the same time.

**Days 60–180: Fix and measure**
- Tighten the handoff from Sales to Implementation so deals are scoped realistically.
- Track time-to-first-value monthly for each new customer cohort.
- Assign an early-warning owner for accounts showing low adoption before renewal.
- Start a small customer advisory group to guide both roadmap and onboarding.

**Throughout: Celebrate progress**
- Cake when the diagnostic is done.
- Cake when time-to-value drops.
- Cake when an at-risk customer renews. Invite them, and their dog if it works out.
- Recognize implementation and support people as much as engineers.

**Your role**

You own the customer data and the renewal relationships, so you're best placed to be the neutral referee. Stay evidence-led, keep both VPs winning publicly, and keep the focus on one question: did customers get value?

Chocolate with sprinkles, of course.

## Outcome summary (sent to Jev)

Neither VP has yet shown they are right, and both may be partly correct. Each belief conveniently justifies more budget for its owner's team, so the head of customer success should act as a neutral, evidence-led referee rather than pick a side. The most diagnostic question is whether churned customers ever reached full value. If churners mostly never fully implemented or adopted existing features, including current analytics, the services explanation holds. If they were fully live, heavy users and still left for competitors, the product explanation holds. A likely combined pattern is that long implementations prevent ROI, and a competitor's AI demo then gives leadership an easy reason to switch. In that case service is the root cause and features are the trigger.

The plan starts next week by asking both VPs, with CEO backing, for a 30-day diagnostic. That diagnostic covers three things:

* Go-live status, time to go live, feature adoption and pre-renewal usage decline for churned accounts over the last 18 months.
* A timeline of what changed 18 months ago, such as competitor launches, team turnover, larger customers or sales-process changes.
* Neutral third-party interviews with 10–15 former customers, ideally claims operations leads.

Findings are presented jointly. Within 60 days, both VPs should share accountability for net revenue retention and time-to-first-value, investment should be split according to the data, and AI work should be aimed at onboarding problems: data mapping, setup templates and out-of-the-box dashboards. Over six months, the company should tighten sales-to-implementation scoping, track time-to-first-value by cohort, assign an early-warning owner for low-adoption accounts and form a customer advisory group.

Key caveats:

* Exit interviews often understate implementation pain.
* Service fixes are less visible than AI features, and their payoff appears only at renewal, so they are easy to underfund.
* Celebrate evidence of progress rather than plans, and recognize implementation staff equally.
