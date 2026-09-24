# churn-cause/economic/testE

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T12:01:20.719190+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to know which idea gets you more stuff, like a lemonade stand. Follow the piggy bank through each idea. How many cookies would it get you, and how much allowance would you spend first? If each idea happened, how long until the treats come, and could a big dog eat them all? Where could you keep spending money and still not get more candy? Who would hold the piggy bank, count the coins, and say when to stop buying things? And is there a third idea that gets even more treats without breaking the piggy bank?

## Response

# The Lemonade Stand Problem

Your lemonade stand used to lose 1 out of every 10 customers each year. Now it loses 2 out of 10. Two grown-ups have different ideas:

- **Product Grown-Up:** "The stand down the street has fancier lemonade with sparkles (AI and analytics). We need sparkles!"
- **Services Grown-Up:** "People wait so long for their first cup, and it's never quite right when it comes. Fix the pouring first!"

## First: Who's right?

**Probably both a little, but you can find out in about a month before spending your allowance.** Ask three questions:

1. **When do customers leave?** If most leave in their first year or two, before they ever got a good cup, the pouring is the problem (Services). If happy long-time customers leave, the sparkles are the problem (Product).
2. **Did the leavers ever drink the lemonade?** Check whether they finished implementation, how many users logged in, and which features they used. Customers who never reached full value don't leave because of missing features. They leave because they never got the features you already have.
3. **Where did they go, and what did they say?** If they went to a competitor with better AI, that's Product. If they went to a competitor that promised a faster, easier setup, or they just complained about support, that's Services. And sometimes a customer gets gobbled up by a bigger insurance company that already uses someone else's stand. That's nobody's fault, and it matters a lot with regional carriers, where mergers are common.

**My hunch:** The two causes are tangled. Customers who never got full value are the ones who listen when a competitor waves sparkles at them. A customer who loves your lemonade doesn't shop around much.

## Following the piggy bank

| | **Fix the Pouring (Services)** | **Add Sparkles (Product)** |
|---|---|---|
| **Allowance spent first** | Smaller. Better onboarding playbooks, templates, some tools, maybe a few people. | Bigger. Engineers, data people, AI work, for a long time. |
| **Cookies it could get you** | Saves customers you're losing *now*, and every new customer too. Happier customers also buy more. | Could win back customers leaving for competitors and help win new deals, but only if customers actually reach the new features. |
| **How long until treats come** | Months. New customers feel it right away. | A year or more to build, then more time for customers to adopt it. |
| **Could a big dog eat them?** | Yes. If competitors really are pulling way ahead, a smoother setup won't save you forever. | Yes, a bigger dog. Customers may leave before the sparkles arrive. Competitors may ship first. And sparkles poured into a leaky cup leak out too. |

**The big warning:** If customers never get full value from what you have today, new features land in the same broken setup process. You'd spend a lot on sparkles almost nobody tastes.

## Where you could keep spending and get no more candy

**Sparkles money pits:**
- Building features for customers who haven't turned on the old ones
- Chasing every shiny AI feature a competitor announces
- Building things one big customer asked for that nobody else uses

**Pouring money pits:**
- Hiring more helpers without making the recipe simpler. More people doing a messy, custom setup is still messy, just more expensive.
- Doing every setup from scratch instead of using a standard recipe for regional carriers
- Giving extra support to customers who have already decided to leave

## Who holds the piggy bank?

Right now, each grown-up is guarding their own jar. That's why they're arguing.

- **One person owns the whole piggy bank.** That's someone above both VPs (the CEO, COO, or a Chief Customer Officer) whose job is how much money you *keep* from customers, not just how much you *win*.
- **Everyone counts the same coins.** Use one shared scoreboard: how many customers stay, how long until a customer gets their first real win, how many people actually use the product, and why the leavers left.
- **Decide when to stop buying before you start.** For example: "If time-to-first-win isn't down by a third in six months, we change the plan." Or: "If nobody uses the new analytics feature within 90 days of launch, we stop building more of it." Set stop points ahead of time so nobody keeps spending because they're embarrassed to quit.

## The third idea: make the sparkles *help* the pouring

Instead of choosing, point Product's builders at the setup problem:

1. **Spend 4–6 weeks finding out why customers really leave.** It's cheap, and it keeps you from betting the whole piggy bank on a guess.
2. **Rescue customers who are about to leave.** Find the ones who never finished setup or barely use the product, and help them get a real win now. That brings treats back fastest.
3. **Have Product build tools that make setup faster.** Ready-made setups for regional carriers, easier ways to move data in, and fewer custom steps. That counts as roadmap work, just aimed at the real leak.
4. **Make your first sparkle a "look what you got" dashboard.** Build an analytics view that shows each customer, early, how much faster claims are moving or how much money they're saving. It answers the competitor's analytics pitch *and* helps customers see value sooner. One cookie, two kids fed.
5. **Only then build the bigger AI features.** Aim them at what the leavers actually said they wanted, and launch them into a setup process that works.

**In short:** Don't pick a grown-up. Count why the coins are leaving first. Fix the leak in the cup. Then make sure every sparkle you add is one customers can actually taste. That way you keep more lemonade money *and* have more to spend on the fancy stuff later.

## Summary (sent to Jev)

The response does not pick either VP. It says both are probably partly right and recommends spending about four to six weeks finding out why customers actually leave before committing major money. Its hunch is that the causes are tangled: customers who never reached full value are the ones who listen when competitors pitch better features, while satisfied customers rarely shop around.

To diagnose churn, it proposes three questions. First, when do customers leave? Early departures point to Services, and loss of long-time happy customers points to Product. Second, did leavers finish implementation and actually use the product? Third, where did they go and what did they say? It notes that mergers among regional carriers can cause churn that is nobody's fault.

It compares costs. Fixing onboarding is cheaper and shows results within months. Building AI and analytics costs more and takes a year or more, and it only pays off if customers reach the new features. Its central warning is that new features launched into a broken setup process will go largely unused. It lists money pits on both sides: building for customers who haven't adopted existing features, chasing every competitor announcement, adding support staff without standardizing a messy custom setup, and supporting customers who have already decided to leave.

For governance, it recommends a single owner above both VPs who is accountable for retention, a shared scorecard, and stop points set in advance.

Its plan is:
1. Diagnose.
2. Rescue at-risk customers who never finished setup.
3. Have Product build tools that speed implementation.
4. Ship an early value dashboard first.
5. Only then build larger AI features aimed at what leavers said they wanted.
