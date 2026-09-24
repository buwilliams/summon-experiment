# legacy-rewrite/economic/testE

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:49:26.845957+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I want to know which idea gets you more stuff, like a lemonade stand. Follow the piggy bank through each idea. How many cookies would it get you, and how much allowance would you spend first? If each idea happened, how long until the treats come, and could a big dog eat them all? Where could you keep spending money and still not get more candy? Who would hold the piggy bank, count the coins, and say when to stop buying things? And is there a third idea that gets even more treats without breaking the piggy bank?

## Response

# Which Idea Fills the Piggy Bank?

**Short answer:** Your head of product is closer to right, but plain incremental work often fizzles. The best plan is a third idea: incremental modernization with a deadline, a scoreboard, and one new lemonade stand built fresh on the side.

---

## Idea 1: Tear Down the Stand and Build a New One (The Big Rewrite)

**Allowance spent first:** Almost all of it, for a long time. You pay a big team to build the new stand *and* keep paying people to run the old one, because that's where the money comes from. The CTO says two years. Rewrites of 20-year-old insurance systems usually take two to three times longer than planned, because the old stand hides thousands of little rules nobody wrote down: state filings, rating quirks, endorsements, and odd policies a customer bought in 2009.

**Cookies:** Zero until the new stand opens. Then maybe a lot, *if* it opens and customers agree to move to it.

**When treats arrive:** Year three or four, realistically.

**Could a big dog eat them all?** Yes, several dogs:
- **The feature-freeze dog.** Customers ask for things during those years. If you say "wait for the new system," competitors sell to them.
- **The copy-everything dog.** The new stand must do everything the old one does before anyone will switch. That job never seems to end.
- **The tired-builder dog.** Your best people staff the rewrite. The people left maintaining the old system get more frustrated, and attrition gets *worse*.
- **The patience dog.** Around month 18, with nothing shipped, the board or CEO loses faith and cancels the project. You've spent the allowance and have no stand.

**Where money buys no candy:** Rebuilding features nobody uses anymore. A rewrite copies the whole old stand, including the junk.

---

## Idea 2: Fix the Stand One Board at a Time (Incremental)

**Allowance spent first:** A little at a time, with small, steady spending while the old stand keeps selling.

**Cookies:** Small batches, often. Each piece you carve off (say, a modern rating engine or a new quoting screen) makes that part faster to change, and customers see it within months.

**When treats arrive:** First cookies in 3 to 6 months, and more every quarter after.

**Could a big dog eat them all?** Different dogs here:
- **The never-finish dog.** Teams modernize the easy parts, then stall. Five years later you run two systems forever, which is worse than one old one.
- **The glue dog.** Keeping old and new parts talking to each other costs real money. If nobody counts it, it quietly eats the savings.
- **The "not cloud-native enough" dog.** Sales still can't say the thing competitors say.

**Where money buys no candy:** Modernizing parts that rarely change. If a module is ugly but nobody has touched it in three years, rewriting it buys nothing. Money only makes candy where the **pain is**: the parts that change often, slow down features, or make engineers quit.

---

## Who Holds the Piggy Bank?

This matters more than which idea you pick. Right now the CTO and head of product are arguing about *how*, and nobody owns *how much and until when*.

- **One person holds the piggy bank:** a single accountable executive for modernization, probably you. It shouldn't be split between the CTO and product.
- **Someone counts coins every quarter** with a scoreboard everyone can see:
  - How long a typical feature takes from idea to customer
  - The share of new business (quotes and policies) flowing through new parts
  - Engineer attrition and hiring success
  - The cost of running and changing the old system
  - Money spent on glue between old and new
- **Stop-buying rules are agreed upfront.** For example: "If a carved-off piece hasn't cut feature time for that area within two quarters, we stop and rethink." Or: "If glue costs pass X% of the budget, we speed up retiring the old parts."

---

## The Third Idea: A Deadline, a Scoreboard, and a New Stand on the Side

This gets the most treats without breaking the bank:

1. **Cheap cookies first (months 0–6).** Make the old stand less miserable to work in. Add automated tests, faster builds and deploys, and cloud hosting if you're not there yet. This is inexpensive, helps keep engineers, and speeds up *every* feature, old or new.

2. **Carve where it hurts (ongoing).** Rank system areas by how often they change and how much they slow you down. In P&C, that's usually product and rating configuration, quoting and distribution, and integrations and APIs. Rebuild those first, behind the old system.

3. **Open a new stand for new customers (year 1–2).** Pick one segment you don't serve well today, such as a specialty line, small commercial, or MGAs. Build for it on the new platform from day one. It proves the new platform with real revenue, gives your best engineers modern work, and gives sales an honest "cloud-native" story. You don't have to migrate existing carriers first.

4. **Put a date on it.** "The old system stops taking new business by year X, and the last carriers migrate by year Y." Without that date, idea 2's never-finish dog wins.

5. **Close the marketing gap separately.** A cloud-hosted SaaS offering, clean APIs, and a modern interface over the old core can make you credibly "cloud-native" to buyers long before the core is replaced. Don't let a sales slogan push you into a two-year rewrite.

---

## Cookie Count at a Glance

| | Allowance spent first | First treats | Big-dog risk | Cookies in the end |
|---|---|---|---|---|
| Big rewrite | Very high | Years 3–4 | Very high | Lots, *if* it survives |
| Plain incremental | Low and steady | Months | Medium (stalls) | Medium |
| **Third idea** | Moderate, staged | Months | Lower | **Most** |

**Bottom line:** The CTO is right that the old stand can't last forever. Product is right that you can't stop selling lemonade to rebuild it. The winning move is to keep selling, fix the parts that hurt most, open a new stand for new customers, and have one person hold the piggy bank with a clear rule for when to stop spending.

## Summary (sent to Jev)

The response holds that the head of product is closer to right but that plain incremental work often fizzles. It recommends a third approach: incremental modernization with a deadline, a scoreboard, and a new platform built fresh for new customers.

It rejects the big rewrite because rewrites of 20-year-old insurance systems typically run two to three times over plan, since the old system hides thousands of undocumented rules. Benefits would not arrive until year three or four. The risks it names are:
- a feature freeze that hands customers to competitors
- an endless job of copying everything the old system does, including unused features
- worsening attrition among engineers left maintaining the old system
- leadership losing faith and cancelling the project around month 18

Plain incremental work delivers value within 3 to 6 months. Its risks are stalling after the easy parts and running two systems forever, unmeasured integration "glue" costs quietly eating savings, and still lacking a cloud-native sales story. It also warns that modernizing rarely changed modules buys nothing.

The response argues that ownership matters more than method. One accountable executive, probably the user, should hold the budget and review a quarterly scoreboard covering:
- feature lead time
- the share of new business flowing through new components
- attrition and hiring
- old-system costs
- glue spending

Stop rules should be agreed upfront.

Its plan has five steps:
1. In months 0–6, improve the old system with automated tests, faster builds and deploys, and cloud hosting.
2. Carve off high-change, high-pain areas first, such as rating configuration, quoting, and integrations.
3. In years 1–2, build a new platform for an underserved segment like specialty lines, small commercial, or MGAs.
4. Set firm dates for ending new business on the old system and completing migration.
5. Close the marketing gap separately through SaaS hosting, APIs, and a modern interface, rather than letting a slogan drive a rewrite.
