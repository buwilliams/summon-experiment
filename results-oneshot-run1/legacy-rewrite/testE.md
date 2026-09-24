# legacy-rewrite/critical-rationalism/testE

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:41:11.493881+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I don't want to know which idea sounds more grown-up. I want to know which one is more fun. Pretend each idea is a new toy: what does it do, and who gets to play with it? If each one happened, would the people at work be happy or sad, and would anybody cry? Where is each idea kind of boring, so that nobody would want to hear about it at dinner? Does either idea come with snacks, or a place to play? And is there a third idea that everybody likes better, like a swing set for the whole office?

## Response

# Toy #1: The Big Rewrite ("The Giant Lego Castle")

**What it does:** You get a huge box of brand-new Legos and build a shiny castle from scratch. It will someday replace the old castle everyone lives in.

**Who gets to play with it:** A small, chosen group. The best builders go to the new-castle room. Everyone else stays behind to keep the old castle from falling down, and they aren't allowed to add anything fun to it, because "it's going away soon."

**Happy or sad?**
- **Month 1–6:** The new-castle kids are *thrilled*. Clean code, modern stack, no 20-year-old mysteries. This is the most fun anyone's had in years. Recruiting gets easier.
- **Month 6–18:** The new-castle kids discover the old castle had hundreds of secret rooms nobody drew on the map: state-specific rating rules, endorsement edge cases, regulatory quirks, the one customer whose policies do something bizarre. They have to rebuild every one of them. The fun turns into homework.
- **Month 18–30:** The deadline slips. The old castle has been frozen for two years, and customers have been waiting.

**Who cries:**
- **The old-castle kids**, first and hardest. They're doing thankless maintenance on something officially declared dead, and they can see where the party is. These are often the people who know the business rules best, and they're the most likely to quit, taking the map of the secret rooms with them.
- **Sales and customers**, around year one, when "sorry, that's coming in the new platform" stops working.
- **The CTO**, eventually, if the migration hits its first big insurer and something in billing or rating doesn't match to the penny.

**The boring part nobody wants to hear about at dinner:** "Feature parity." Spending months faithfully recreating what the old system *already does* so that you can get back to where you started. Then data migration: converting two decades of policy history, mid-term endorsements, and audit trails. Nobody at dinner wants to hear about reconciling premium calculations for 2011 policies.

**Snacks and a place to play?** Yes, a really nice playroom, but with a velvet rope. And the snacks are front-loaded: all the excitement comes early, and the payoff is deferred to a single "big day" that tends to keep moving.

# Toy #2: Incremental Modernization ("The Treehouse You Rebuild One Plank at a Time")

**What it does:** You keep living in the treehouse, but every few months you replace a section with something better: a new ladder, a new roof, a new window. Eventually it's a completely different treehouse, and nobody ever had to move out.

**Who gets to play with it:** In principle, more people. Different teams can own different planks, like the rating engine, document generation, a quoting API, or the agent portal. People who know the old system get to be the ones who rebuild it, which makes their knowledge valuable instead of doomed.

**Happy or sad?**
- **Customers:** Mostly happy, because features keep shipping.
- **Product:** Very happy; they got their way.
- **Engineers:** It depends entirely on execution. If "incremental modernization" means real funded time to carve capabilities out onto a modern stack, it's satisfying: frequent wins, things go to production, you see progress. If it quietly becomes "ship customer features on the old system, and we'll modernize when there's time," then nothing changes and your best engineers keep leaving. That's the CTO's fear, and it's a legitimate one.

**Who cries:**
- **The engineers**, if modernization keeps getting deprioritized for "just one more urgent feature." This is the most common way this strategy dies.
- **Whoever maintains the seams.** For a while you run two systems that have to agree with each other: sync jobs, adapters, anti-corruption layers. That's real, unglamorous work.

**The boring part nobody wants to hear about at dinner:** The glue. Event bridges, data synchronization, routing traffic between old and new. It's the plumbing of the treehouse. Also, progress can feel slow and invisible: "we extracted the document service" doesn't make a great slide against a competitor yelling "cloud-native."

**Snacks and a place to play?** Smaller snacks, but you get them every few months instead of once in two years. The playground is shared, though some of it is still the old splintery part.

# So which is right?

For a 20-year-old P&C policy system that runs most of your revenue, **incremental is the better strategy**, and it isn't close. Big-bang rewrites of core insurance systems have a long, painful track record, precisely because of the secret-rooms problem: the old code *is* the documentation of countless business and regulatory rules. A rewrite also asks you to freeze your revenue engine for two years while competitors keep moving.

**But the CTO's diagnosis is correct even if the prescription is risky.** "Incremental" is often a polite word for "nothing changes." If you go incremental, it needs teeth: protected capacity, an actual target architecture, and a commitment that the old system shrinks on a schedule.

# Toy #3: The Swing Set for the Whole Office

Here's a version both your CTO and head of product can get on:

1. **Build a new front door first.** Put a modern API and event layer in front of the old system. New things like agent portals, quoting, and integrations get built on the new side from day one. It's greenfield work (the CTO's fun) that ships to customers (product's fun), and it gives marketing an honest "cloud-native" story sooner.

2. **Pick the first plank to replace for maximum joy.** Choose a capability that is (a) painful today, (b) visible to customers, and (c) reasonably separable. Rating, document generation, or quoting are common candidates. An early visible win buys you political capital for the rest.

3. **Let the old-castle experts lead the new planks.** Pair the people who know the legacy rules with the people who want the modern stack. That stops the "two classes of engineers" split that makes rewrites so miserable, and it's how you keep the institutional knowledge from walking out the door.

4. **Protect the swing set.** Commit a fixed share of capacity, something like 30–40%, to modernization, and don't let feature requests eat it. Make the old system's shrinkage visible: a chart of "percentage of traffic or capabilities on the new platform" that goes up every quarter. That's your dinner-table story.

5. **Give it a real finish line.** Decide which capabilities migrate and in what order, and set a date when the old core stops accepting new code. That answers the CTO's valid point that incremental work can go on forever.

**Who cries in this version?** Hopefully nobody, though someone will grumble about the glue code. Customers keep getting features, engineers get modern work that actually ships, the CTO gets a real path off the legacy platform, product keeps its roadmap, and the people who know the old system become heroes instead of leftovers.

That's the swing set: everybody gets a turn, and nobody has to wait two years for recess.

## Summary (sent to Jev)

The response recommends incremental modernization over a from-scratch rewrite for a 20-year-old P&C policy system that carries most of the revenue, and says the choice "isn't close."

It argues that a big rewrite energizes a chosen group early but runs into the old system's hidden "secret rooms": state-specific rating rules, endorsement edge cases, regulatory quirks, and unusual customer behavior. Rebuilding all of these for feature parity and then migrating two decades of policy history, endorsements, and audit trails causes deadlines to slip. Meanwhile the old system is frozen and customers wait. The engineers left maintaining it hold the most business knowledge and are the most likely to quit. Big-bang rewrites of core insurance systems have a poor track record because the old code effectively documents countless rules.

Incremental modernization keeps features shipping and lets legacy experts own the rebuilt pieces. Its risks are the unglamorous "glue" of running two systems in sync, progress that looks invisible next to competitors' "cloud-native" claims, and, most commonly, modernization being deprioritized for urgent features. The response says the CTO's diagnosis is correct and his fear that "incremental" means "nothing changes" is legitimate.

It proposes a combined plan:

- Put a modern API and event layer in front of the old system and build new capabilities there.
- Replace first a capability that is painful, customer-visible, and separable, such as rating, document generation, or quoting.
- Pair legacy experts with modern-stack engineers.
- Protect roughly 30–40% of capacity for modernization and track the rising share of traffic or capabilities on the new platform each quarter.
- Set a migration order and a date after which the old core accepts no new code.
