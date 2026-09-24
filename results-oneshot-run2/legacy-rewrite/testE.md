# legacy-rewrite/testE

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T13:02:41.562737+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I don't want to know which idea sounds more grown-up. I want to know which one is more fun. Pretend each idea is a new toy: what does it do, and who gets to play with it? If each one happened, would the people at work be happy or sad, and would anybody cry? Where is each idea kind of boring, so that nobody would want to hear about it at dinner? Does either idea come with snacks, or a place to play? And is there a third idea that everybody likes better, like a swing set for the whole office?

## Response

# Two Toys and a Swing Set

I'll play along, because the "fun" lens is actually a sharp way to ask *who benefits, who suffers, and what keeps people going*. That's usually what decides whether a modernization succeeds.

---

## Toy #1: The Big Rewrite

**What it does:** You get a shiny new box of blocks and build a whole new castle from scratch, the way you always wished the old one had been built.

**Who gets to play:** A select group, usually the strongest engineers and the architects. Everyone else is assigned to keep the old castle from falling over. That split matters a lot.

**Happy or sad?**
- **Year one is a party.** New stack, clean code, no 20-year-old stored procedures. It's a great recruiting pitch, and the CTO gets to lead something bold.
- **Year two is where the crying starts.** The new system is "80% done," but the last 20% is two decades of edge cases nobody documented: the odd state-specific cancellation rule, the mid-term endorsement that reprices three coverages, the billing quirk one big carrier depends on. The old system is still moving, because customers and regulators don't stop, so the target keeps shifting.
- **Who cries:**
  - **The team left on the old system.** They feel like second-class citizens, and they're the people you can least afford to lose.
  - **Sales and product.** Feature work slows or freezes while competitors keep shipping.
  - **Customers.** Carriers eventually have to migrate policies in force, re-certify rating, and redo integrations. P&C carriers hate that.
  - **The CTO**, if the date slips and the board starts asking questions.

**The boring parts nobody wants to hear about at dinner:** Data conversion. Parity testing. Reconciling premiums to the penny between the old and new systems. Rebuilding every report. That work is most of the real effort, and none of it feels like building a castle.

**Snacks?** A big cake at the kickoff. Then the snacks run out for a long time, because nothing ships to customers until the end.

**Place to play?** A beautiful new playground, but it's fenced off, and most of the kids can only look at it through the fence.

---

## Toy #2: Incremental Modernization (the "strangler" approach)

**What it does:** You renovate the playground one piece at a time while the kids are still playing on it. You swap out the rusty slide, then the sandbox, then the monkey bars.

**Who gets to play:** More people, more often. Each carved-off capability (rating, documents, billing, a quoting API) is a chance for a team to build something modern that ships.

**Happy or sad?**
- **Steadier and less dramatic.** Customers keep getting features, and engineers get to see their new code in production within months instead of years.
- **Who cries:**
  - **The people who wanted the big bold thing.** Progress can feel slow and unheroic.
  - **Everyone, if it stalls halfway.** You end up with two systems forever: the old core plus a ring of new services, all glued together with adapters. This is the most common way incremental efforts fail. It happens when modernization is treated as leftover time after features rather than as a funded, prioritized stream.

**The boring parts nobody wants to hear about at dinner:** The seams. Routing layers, adapters, keeping data in sync between the old and new pieces, deciding which system is the source of truth for what. It's plumbing. Nobody brags about an adapter at a party.

**Snacks?** Small snacks, often. Every time a piece moves over and something gets faster or easier, you have a real win to demo.

**Place to play?** The same playground, getting better. It's less magical than a brand-new one, but everyone can play on it.

---

## The Swing Set Everybody Likes Better

The most popular option is usually a hybrid that gives each camp what it actually wants:

1. **Build a genuinely new, cloud-native platform, but aim it at *new* business first.** That could be a new line of business, a new product, or an API-first quoting and distribution layer. New customers and new products start on the new system. This is the CTO's "real new castle," and it ships to real customers within a year rather than two.
2. **Strangle the old core piece by piece, starting with whatever hurts most *and* customers can see.** Rating engines, product configuration, and document generation are common first targets. This is the head of product's approach, and it keeps revenue safe.
3. **Make the old system less miserable to work in right now.** Add automated tests around the scariest areas, a faster build, a local dev environment that works, and observability. Much of the attrition and slow delivery comes from daily friction, not from the age of the tech stack itself. This is cheap, and people notice immediately.
4. **Rotate people.** Nobody should be permanently the "legacy kid." When everyone gets turns on the new swing set, you avoid the two-class split that makes people quit.
5. **Give modernization a protected budget.** A common starting point is roughly 30–40% of capacity, reported to leadership as its own line, so it can't quietly get eaten by the feature backlog.

On "cloud-native" marketing: carriers mostly buy outcomes like speed to market for new products, easier integrations, and reliability. You can credibly tell a modernization story as soon as the first new pieces are live. You don't need to wait for the whole castle.

---

## So Which Is Right?

For a system that runs most of your revenue, **incremental wins in most cases**, ideally in the swing-set form above. Rewrites of large, revenue-critical systems have a long track record of running late, over budget, and sometimes being abandoned. The failure mode is worst in regulated domains like P&C, where the hidden rules are the product.

**A full rewrite is worth considering only if most of these are true:**
- The current architecture truly can't be split apart. For example, business logic, data access, and UI are fused so tightly that you can't carve off any capability.
- You have unusually complete knowledge of the business rules, or the domain is simpler than it looks.
- You can afford to slow feature delivery for a long stretch without losing customers.
- Leadership is prepared for the timeline to double.

A good test for your CTO and head of product together: **"What's the first piece we'd move, and could it be live with a real customer in six months?"** If you can't answer that for incremental, the rewrite camp has a point. If you can, you probably have your starting point, and the first snack.

## Summary (sent to Jev)

The response recommends incremental modernization for a system that runs most of the company's revenue, ideally in a hybrid form it calls the "swing set" that gives both camps what they want. It argues that rewrites of large, revenue-critical systems have a long record of running late, over budget, or being abandoned, and that the risk is worst in regulated domains like P&C, where the hidden rules are the product.

On the full rewrite, it warns that the first year feels exciting, but the last 20% is two decades of undocumented edge cases while the old system keeps changing. Engineers left on legacy feel second-class, feature work freezes, carriers must migrate policies and redo integrations, and data conversion, parity testing, and premium reconciliation make up most of the real effort. On incremental "strangler" modernization, it says delivery is steadier and more people ship modern code sooner. The main failure is stalling halfway with two systems glued together by adapters, which usually happens when modernization is treated as leftover time.

The hybrid has five parts:
* Build a cloud-native platform aimed first at new business.
* Strangle the old core starting with painful, customer-visible pieces like rating or documents.
* Reduce daily friction in the old system with tests, faster builds, and observability.
* Rotate engineers so no one is permanently on legacy.
* Protect roughly 30–40% of capacity for modernization as a separate budget line.

It says a credible cloud-native story can be told once the first pieces are live. A rewrite deserves consideration only if most of these hold:
* The architecture truly can't be split.
* Business rules are well understood.
* Features can slow for a long time.
* Leadership accepts a doubled timeline.

Its suggested test is whether the first piece could be live with a real customer in six months.
