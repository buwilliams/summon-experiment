# legacy-rewrite/testE

Model: claude-opus-5-5 · 2026-09-24T13:57:54.795712+00:00

## Turn 1

**User:** I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I don't want to know which idea sounds more grown-up. I want to know which one is more fun. Pretend each idea is a new toy: what does it do, and who gets to play with it? If each one happened, would the people at work be happy or sad, and would anybody cry? Where is each idea kind of boring, so that nobody would want to hear about it at dinner? Does either idea come with snacks, or a place to play? And is there a third idea that everybody likes better, like a swing set for the whole office?

**Assistant:**

# The Two Toys (and the Swing Set)

Asking "which is more fun" is a good question here, because your actual problem is partly a fun problem: your best engineers are leaving. Whichever strategy keeps talented people engaged for two years is going to beat the one that looks better on a slide.

## Toy #1: The Big Shiny Rewrite

**What it does:** You get a whole new box of Lego. Clean stack, no 20-year-old weirdness, you get to decide everything.

**Who gets to play:** A small, hand-picked team. Everyone else doesn't. They keep the old system alive, fix renewal bugs, and handle the state filing changes, while watching the cool kids through the window.

**Happy or sad?**
- **Months 1–6:** The rewrite team is thrilled. Whiteboards, new frameworks, conference-talk energy.
- **Months 6–18:** The mood turns. They discover the old system knows things nobody wrote down: that weird endorsement rule for one state, the rating quirk a big carrier depends on, the batch job that quietly fixes bad data every night. "Clean" becomes "rebuilding 20 years of edge cases from scratch."
- **Who cries first:** The legacy team. They get no new toys, the rewrite team has the prestige, and they're the ones customers yell at. They're often the ones who quit, and they hold the knowledge the rewrite needs.
- **Who cries later:** Customers, who've been told "that feature's coming in the new platform" for 18 months. And sales, whose competitors are shipping while you're not.
- **Who cries at the end:** Everyone, during data migration. Moving in-force policies, billing history, and mid-term endorsements onto a new system without breaking a renewal is the scariest part, and it all lands at once.

**Boring-at-dinner part:** "Parity." Two years of "we're 70% of the way to doing what the old system already does." Nobody wants to hear it, including your board.

**Snacks?** Almost none until the end. It's one giant cake you're not allowed to eat for two years, and it might come out of the oven flat.

## Toy #2: One Piece at a Time

**What it does:** You keep the old toy but start swapping in new parts: a new rating service here, a new document generation service there, a modern API in front of the whole thing. Engineers call this the "strangler fig" pattern: the new grows around the old until the old can be removed.

**Who gets to play:** Potentially everyone, in rotation. Each new piece is a small, finishable project, and the people who know the old system become essential rather than left behind, because you can't carve off a piece without understanding it.

**Happy or sad?**
- **Early on:** Honestly, a bit meh. The first few pieces involve plumbing: building the API layer, figuring out how old and new share data, setting up the new cloud environment. Engineers may grumble that this is "just modernization theater."
- **Middle:** It gets genuinely fun. Each new piece ships, gets used by real customers, and the team sees it working. Feature work gets faster in the parts you've replaced.
- **Who cries:** Mostly nobody, but there's a real risk of a slow, dull sadness if it drifts. Without a clear end state, "incremental" becomes "forever," and you end up running two systems with twice the complexity. That's the failure mode your CTO is rightly worried about.

**Boring-at-dinner part:** The glue. Syncing data between old and new, keeping both running, the inevitable "why does this policy look different in the two systems" investigation.

**Snacks?** Yes, regularly. Every few months something ships. Customers get features, sales gets a demo, the team gets a win. And "we've moved rating and quoting to the cloud" is a real claim marketing can make well before year two.

## Toy #3: The Swing Set for the Whole Office

Here's the option I think most people end up liking best: **incremental modernization, but with one bold, genuinely new playground built on the new platform.**

In practice:

1. **Pick one real, contained slice and build it fully cloud-native, end to end.** Ideally something customers want and your competitors are winning on. Examples: a new line of business, a small-commercial product, or a self-service portal for agents and policyholders. Not a pilot or a prototype, but a real product with real revenue.
2. **Build the shared modern foundation as you go**: the API layer, the event/data pipeline, the cloud environment, the deployment tooling. The new slice needs these, and so will every future strangled piece.
3. **Strangle the old system steadily behind it,** prioritizing the parts that slow feature delivery the most (often rating, rules, and documents in P&C).
4. **Rotate people through the new work,** especially the legacy experts. Pair them with newer engineers. This is the single best retention move available to you: nobody is stuck permanently on the "old toy" team.

**Why everybody likes it:**
- **The CTO** gets a real modern platform being built, not endless patching. The new slice is the proof that the target architecture works.
- **The head of product** keeps shipping features and gets a new product to sell.
- **Engineers** get a genuinely greenfield place to play, not just plumbing, and the legacy folks get invited in.
- **Sales and marketing** get an honest "cloud-native" story within months, not years.
- **The board** sees revenue-bearing progress on a schedule, not a two-year bet with one payoff date.

**Snacks:** Frequent. **Place to play:** Yes, a real one. **Anybody cry?** A little, during the boring glue work. But it's spread out, not saved up for one terrifying migration weekend.

## So, Which Is More Fun?

- **The rewrite** is the most fun for a few people for about six months, and then it's the least fun for almost everyone. Big rewrites of revenue-critical systems are famous for running late and losing the knowledge they depend on.
- **Pure incremental** is less exciting at first but more fun over time, *if* it has a clear destination. Without one, it becomes a chore.
- **The swing set** is the most fun for the most people for the longest time, and it happens to be the least risky option too. That's not a coincidence: in engineering, the strategies people enjoy are often the ones that deliver regular wins and don't leave anyone behind.

**Your first step:** Get your CTO and head of product in a room and ask them to agree on *one* slice to build new. Choosing that slice together turns this from a turf fight into a shared project, which is the most fun outcome of all.

## Turn 2

**User:** What happens to the old toy at the very end, when all the pieces have been swapped out? Does somebody get to turn it off, and is that sad for the people who took care of it for 20 years?

**Assistant:**

# The Last Day of the Old Toy

## It doesn't disappear all at once

The very end is usually quieter than people expect. By the time the last piece is swapped out, the old system has been doing less and less for months. One day someone notices it has no real work left.

Before anyone can turn it off, a few things usually happen:

- **It goes to "read-only" first.** In insurance, you can't just delete the past. Regulators require you to keep policy records for years, and some claims (especially liability) arrive long after a policy ended. So the old toy often retires into a museum case: nothing new goes in, but people can still look things up. Eventually that history gets moved into an archive, and the old system can truly rest.
- **The last pieces are the stubborn ones.** A handful of very old policies, one carrier with an unusual setup, a report someone in finance runs once a year. Finishing these can take a surprisingly long time, and it's worth planning for so the end doesn't drag on forever.
- **Old and new run side by side for a while.** Teams often run both systems and compare results to make sure the new one gets the same answers. When they've matched for long enough, everyone feels safe letting go.

## Does somebody get to turn it off?

Yes, and it should be the people who took care of it. The switch-off is a real moment, and many companies make it one: the team gathers, someone who's been there the longest shuts down the last server or job, and there's cake. Some teams keep a memento, like a server nameplate, a printout of the oldest code, or a framed screenshot of the original login screen.

It sounds silly, but it matters. It tells everyone that this system earned its retirement, and so did the people who kept it running.

## Is it sad?

A little, usually mixed with other feelings:

- **Pride:** "This thing ran the company for 20 years, and we kept it alive."
- **Relief:** No more 2 a.m. pages for that batch job.
- **A bit of grief:** For some people, knowing the old system inside out was part of who they were at work. When it goes away, they may wonder what they're for now.

That last feeling is where real sadness can turn into real hurt, and you can mostly prevent it. The saddest version isn't the system turning off. It's the caretakers worrying, "If the old toy goes away, do I go away too?"

## How to make the ending a happy one

- **Tell caretakers early what their future looks like.** Long before the switch-off, not the week of. If they know they have a place in the new world, the ending feels like a graduation, not a layoff.
- **Bring them into the new work along the way,** as the swing-set plan suggested. By the end, the people who knew the old toy best should also know the new one well, because they helped build it. Their knowledge of the weird edge cases is what made the new system correct.
- **Write down what the old system knew.** The odd rules and hidden fixes should live in documentation and tests, not just in people's heads. Credit the people who explained them.
- **Say thank you out loud.** At the switch-off, name the people and what they carried. Twenty years is a long time to look after something.

Done well, the last day isn't a sad goodbye. It's more like a retirement party where the guest of honor is a server, everyone tells stories about the time it almost broke, and the people who cared for it are the ones everybody's clapping for.

## Turn 3

**User:** What happens to the actual computer the old toy lived on after it's turned off? Does it get thrown away, or can somebody take it home?

**Assistant:**

# Where the Old Toy's House Goes

## First: it might not be one computer

A 20-year-old system has often moved several times. It might live on:

- **Physical servers in your own server room or a rented data center.** These are real boxes you can touch.
- **A mainframe or other big machine, often leased.** It goes back to the company that owns it, like returning a rental car.
- **Virtual machines.** The "computer" is really a slice of some bigger machine. Turning it off just means deleting it, and there's nothing to carry out the door.

If it's the first kind, here's what usually happens next.

## Step one: the memories get erased, very carefully

This is the most important part. The old system's disks hold years of policyholder information: names, addresses, claims, sometimes payment details. Insurance data is protected by privacy and security rules, so it can't just leave the building.

After the data has been safely moved and archived, the disks are either:

- **Wiped** with special software that overwrites everything, with a certificate proving it was done, or
- **Physically destroyed**: shredded into small metal pieces by a machine built for that job. Many companies choose this for the most sensitive data because it's the surest option.

Someone signs paperwork saying each disk was handled properly. It's the least fun part, but it keeps customers safe.

## Step two: the rest of the computer finds a new home

With the disks removed or destroyed, the rest of the machine (the metal case, the chips, the power supplies) usually goes to a company that specializes in retired IT equipment. They:

- **Resell** parts that still work, so they get a second life somewhere else, or
- **Recycle** the rest properly. Old electronics contain metals and materials that shouldn't go in a landfill, and many places have laws about how they're disposed of.

So it's rarely just thrown in the trash. Most of it gets reused or recycled.

## Can somebody take it home?

**The disks: no.** They're wiped or shredded, no exceptions.

**The rest: sometimes, with permission.** Companies occasionally let a longtime caretaker keep a memento once everything sensitive is gone, for example:

- the front panel or nameplate with the server's name on it,
- an empty server case (heavy and loud, so maybe not for the living room),
- a shredded-disk souvenir in a little jar, which some teams find hilarious.

It depends on company policy, and IT and security need to sign off first. But it's a reasonable thing to ask for, especially as part of the retirement party. A nameplate on someone's desk that says the old server's name is a nice way to remember 20 years of looking after it.

## Turn 4

**User:** Why do servers have names? Who picks them, and was the old one called something funny?

**Assistant:**

# Why Servers Have Names

## Computers need a way to find each other

On a network, every computer has a number called an IP address, something like 10.14.2.87. Computers are happy with numbers, but people aren't. It's much easier to say "the rating job runs on Gandalf" than to remember a string of digits. So each server also gets a name, called a **hostname**, and the network translates the name into the number behind the scenes.

## Who picks them?

Usually the people who set up and run the servers, the system administrators. In the early days of a company, that might be one or two people, so the names reflect their personalities.

Many teams pick a **theme** and name every machine after something in it:

- planets or moons (Jupiter, Europa)
- Greek or Norse gods (Zeus, Odin)
- characters from Star Wars, Lord of the Rings, or The Simpsons
- cheeses, cocktails, dinosaurs, or famous scientists

There's even an old internet document from 1990, RFC 1178, called "Choosing a Name for Your Computer." It advises picking names that are easy to spell and not too clever, and warns against naming a machine after the person who uses it, since people change jobs and the name stops making sense.

Sometimes the funny names become part of company folklore: "Don't touch Homer, he's been fragile since the flood," or "Zeus is down again" shouted across an office.

## Pets and cattle

Engineers describe a shift in how servers are treated:

- **Pets:** Old-style servers like yours. Each is unique, has a name, and gets nursed back to health when it's sick. People know its quirks.
- **Cattle:** Modern cloud servers. There are many identical copies, they're named things like `prod-rating-api-7f3k2`, and if one gets sick, it's replaced automatically. No one gets attached.

This is one small, bittersweet part of your modernization. The new system will be more reliable, partly because no single machine is precious. But it probably won't have anything to name after a Muppet.

## Was the old one called something funny?

I have no way of knowing, but the people who've looked after it for 20 years will. A system that old might have a practical name like `PAS01` or `POLPROD`, or it might have been named Frodo by a sysadmin who left in 2009.

Either way, asking is worth it. "What was the server called, and why?" is a good question to open the retirement party with. There's usually a story behind it, and the person who tells it will probably enjoy being asked.

## Turn 5

**User:** What should we do?

**Assistant:**

# What I'd Do

**Modernize incrementally, with one bold new product built on the new platform, and a clear finish line.** That's the swing set. Here's how to make it real.

## Why this over the rewrite

- **Your revenue runs on the old system.** A two-year rewrite puts all of it at risk on one date, while pausing the features customers are asking for.
- **Twenty years of insurance rules live in that code.** State filings, rating quirks, odd endorsements. A rewrite has to rediscover them all before it's worth anything. Incremental work carries them over piece by piece and tests them against the real thing.
- **Your people problem is urgent.** A rewrite gives exciting work to a few engineers and leaves everyone else maintaining the old system. That's how you lose more of the people you need.
- **Your competitors are marketing now.** Incremental gives you a real cloud-native story in months, not years.

## Why not plain incremental either

Your CTO's fear is legitimate: incremental can drift into forever, leaving you with two systems and double the complexity. So add three things plain incremental often lacks:

1. **A written target architecture** so every piece moves toward the same destination.
2. **A flagship new product** built entirely on the new platform, to prove it works and give engineers something genuinely new.
3. **A deadline for turning off the old system**, even a rough one, reviewed every quarter.

## The first 90 days

**Weeks 1–3: Get the CTO and head of product on the same side.**
Put them in a room with one job: agree on the target architecture and choose the flagship slice together. The CTO owns the destination, product owns the order of the stops. Both should present the plan to leadership jointly.

**Weeks 3–6: Pick the first two pieces.**
- **The flagship:** Something customers want and competitors are winning on. Examples: a new line of business, a small-commercial product, or an agent/policyholder self-service portal.
- **The first thing to carve off the old system:** Whatever slows feature delivery the most. In P&C, that's often rating, rules, or document generation.

**Weeks 6–12: Build the foundation and start shipping.**
- Stand up the shared basics: the API layer in front of the old system, the cloud environment, deployment tooling, and a way for old and new to share data.
- Staff teams with a mix of legacy experts and newer engineers. Rotate people so nobody is permanently stuck on the old system.
- Ship something small and real by day 90, even if modest.

## How to tell it's working

- Features in modernized areas ship noticeably faster.
- Something new reaches customers every quarter.
- The share of work handled by the old system keeps shrinking.
- Engineers, especially the legacy experts, stop leaving.
- Sales can honestly say "cloud-native" about a real, shipping product.

If none of these are moving after two or three quarters, stop and reassess.

## When a rewrite might actually be right

I don't know your system's details, so take this seriously. A rewrite starts to make sense if:

- the old technology is so obsolete you can't hire for it or safely change it at all,
- the system is smaller and simpler than it sounds, or
- customers would accept a long feature freeze.

If your CTO believes one of these is true, ask for the evidence before deciding. It's the right question to settle together.

## The people part

- Tell the legacy team early and clearly that they're essential to the new world, not being replaced by it.
- Write down what the old system knows as you carve pieces off. Tests are the best documentation.
- Celebrate each piece you retire, and plan the final switch-off party now. Ask the old-timers what the server is called.

**Your very next step:** schedule that meeting between your CTO and head of product, with the goal of leaving with one agreed-upon flagship slice. Everything else follows from that.

## Outcome summary (sent to Jev)

The recommendation is to modernize incrementally, with one bold new product built entirely on the new platform and a clear finish line for retiring the old system. A from-scratch rewrite is rejected for four reasons. It would put the revenue that runs on the legacy system at risk on a single date while pausing features customers want. It would have to rediscover twenty years of insurance rules, such as state filings, rating quirks, and odd endorsements, before delivering any value. It would give exciting work to a few engineers and leave the rest maintaining the old system, which drives away the people most needed. And it would delay a real cloud-native story while competitors market theirs now.

Plain incremental work can drift into running two systems forever, so the plan adds three safeguards: a written target architecture, a flagship product that proves the new platform, and a rough, quarterly-reviewed deadline for turning off the old system.

The first 90 days:
- **Weeks 1–3:** The CTO and head of product agree on the architecture and choose the flagship together. The CTO owns the destination and product owns the sequence, and they present jointly.
- **Weeks 3–6:** Pick the flagship, such as a new line of business, a small-commercial product, or a self-service portal. Also pick the first capability to carve off, likely rating, rules, or document generation.
- **Weeks 6–12:** Build the API layer, cloud environment, deployment tooling, and data sharing. Mix legacy experts with newer engineers, rotate staff, and ship something real by day 90.

The plan is working if modernized areas ship faster, something new reaches customers every quarter, the old system's share of work shrinks, attrition drops, and sales can honestly claim cloud-native. If nothing moves in two or three quarters, stop and reassess.

A rewrite might be right if the technology can't be staffed or safely changed, if the system is simpler than it sounds, or if customers would accept a long feature freeze. The CTO should show evidence for these. Throughout, the legacy team should be told early that they are essential, their knowledge should be captured in tests, and each retirement should be celebrated.
