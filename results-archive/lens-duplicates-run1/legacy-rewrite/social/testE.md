# legacy-rewrite/social/testE

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:45:15.665788+00:00

## Prompt

I lead engineering for a mid-sized company whose core product is a 20-year-old policy administration system for property and casualty insurers. It still works and it runs most of our revenue, but every new feature takes months, our best engineers keep leaving, and two competitors now market themselves as "cloud-native." Our CTO believes we must rewrite the platform from scratch on a modern stack over the next two years, because incremental fixes will never get us out of the hole. Our head of product believes we should modernize incrementally, carving off one capability at a time behind the existing system while continuing to ship features customers are asking for. Which strategy is right?

I want to know which idea makes more people want to be your friend. Think about how each idea would look to kids at work and kids outside. Who gets a gold star, and who gets in trouble or says sorry? If each idea happened, would the boss, the helpers, the customers, and everybody's moms think it was cool? Where might wearing a cape or being loud matter more than doing chores? Who would sit together at lunch because of each idea? And is there a third idea where everybody gets to play and nobody feels left out?

## Response

## The short answer

**Incremental modernization is the right default, but only if it's funded and led as seriously as a rewrite would be.** Your CTO is right that you're in a hole. He's likely wrong that a from-scratch rewrite is the way out.

### Why a full rewrite is so risky for you specifically

- **The old system is the spec.** Twenty years of rating rules, state-specific forms, endorsements, edge-case billing logic, and regulatory fixes live in that code, often undocumented. Rewrites routinely discover this in year two, when "80% done" turns out to be 40%.
- **You can't freeze the business.** Carriers will keep asking for features, rate changes, and compliance updates. You'll either maintain two systems (doubling cost) or stop shipping (losing customers to those cloud-native competitors).
- **Migration is the real project.** Moving live policies, claims history, and in-force books between systems is where P&C conversions die. Carriers' risk and IT teams know this, and many won't migrate on your timeline anyway.
- **Two years is almost never two years.** Rewrites of core insurance platforms commonly run to three or four, with value delivered only at the end.

### Where the CTO has a point

Incremental efforts often become "incremental forever": a few services peeled off, the monolith untouched, nothing actually retired. If "incremental" means "keep doing what we're doing with a nicer name," he's right to reject it. And some foundations (data model, deployment pipeline, hosting) may genuinely need replacing rather than patching.

A rewrite becomes more defensible if the codebase truly can't be decomposed, the underlying tech is unsupportable, or you're really building a *new product for a new market* rather than replacing the old one.

---

## The popularity question: who wants to be friends with each idea?

### The Big Rewrite 🦸 (the cape idea)

**Gold stars early:**
- The CTO looks bold and visionary.
- Engineers who get picked for the new team are thrilled, and recruiting gets easier ("come build greenfield").
- Marketing and sales get a shiny story to counter "cloud-native" competitors.
- The board often loves it at first. It sounds decisive.

**Who gets in trouble or says sorry:**
- Product and customer success spend two years apologizing to customers for slow or frozen features.
- The engineers left maintaining the old system feel like the B-team, and they're the ones who know where the bodies are buried. When they leave, the rewrite loses its best source of truth.
- Around month 18–30, when it's late and over budget, the CTO is the one saying sorry, often to a much less excited board.

**Lunch tables:** This is the biggest hidden cost. A rewrite splits the cafeteria into the "new platform" table and the "legacy" table, and resentment builds between them. Knowledge stops flowing exactly when you need it most.

**Would customers and their moms think it's cool?** Carriers' executives might like the pitch. Their IT, risk, and compliance people (the practical grown-ups) will be nervous about a big-bang migration of their book of business. Regulators don't care about your stack; they care that filings and forms are right.

**Cape vs. chores:** Almost all cape. It wins the announcement and loses the delivery.

### Incremental Modernization 🧹 (the chores idea)

**Gold stars:**
- The head of product, customer success, and sales teams serving existing accounts, because features keep shipping.
- Existing customers, who see steady progress with less risk.
- Finance, which gets value delivered every quarter instead of a two-year bet.

**Who's less impressed:**
- Engineers may feel it's "still the old system" unless they see real, visible retirement of legacy pieces.
- The board and marketing may find it unexciting and harder to pitch against "cloud-native" rivals.
- The CTO may feel overruled, which is a real risk if it turns into a win/lose fight.

**Lunch tables:** Mixed teams that work on both old and new keep knowledge flowing and people talking.

**Cape vs. chores:** Mostly chores. It works, but it can lose the storytelling war if nobody tells the story.

---

## The third idea: everybody gets to play

A **structured strangler approach with a visible greenfield flagship**:

1. **Build the new platform foundation for real.** That means a modern data layer, APIs, cloud hosting, and CI/CD, owned and led by the CTO. He gets his cape, and it's a genuine one.
2. **Launch something new on it early.** Pick a new product line, segment, or capability (e.g., small commercial, a new rating engine, a digital quoting/portal layer) and ship it cloud-native within 9–12 months. That gives marketing an honest "cloud-native" story and gives engineers greenfield work.
3. **Carve capabilities off the old system one at a time**, in order of business value and pain: rating, documents, billing, and so on. Each move ends with *retiring* the old piece, not just duplicating it.
4. **Keep shipping customer features**, preferably on the new pieces as they come online. The head of product owns sequencing so customers keep getting what they asked for.
5. **Rotate people across old and new.** No legacy-only team. Your veterans become the most valued people in the building, because they know what the rules actually are.
6. **Measure it publicly.** Track the percentage of transactions on new components, legacy modules retired, lead time for features, and engineer attrition. This keeps "incremental" from quietly stalling, which addresses the CTO's legitimate fear.

**Who sits together at lunch:** The CTO and head of product co-own one roadmap instead of competing for the CEO's vote. Engineers mix across old and new. Sales has a story, customers have features, and the board sees quarterly proof instead of a two-year promise.

**The one thing to avoid:** Letting this become a contest the CTO or head of product "wins." Whichever strategy you choose, if one of them walks away defeated, you'll lose either the technical leadership or the customer credibility you need to pull it off.

## Summary (sent to Jev)

The response recommends incremental modernization as the default, provided it is funded and led as seriously as a rewrite. It agrees with the CTO that the company is in a hole but argues a from-scratch rewrite is likely the wrong way out. The old system is effectively the spec, holding twenty years of undocumented rating rules, forms, billing logic, and regulatory fixes. The business cannot freeze, so a rewrite means running two systems or halting features. Migrating live policies and in-force books is where P&C conversions fail. And two-year rewrites commonly stretch to three or four, with value only at the end.

It concedes the CTO's point that incremental efforts often become "incremental forever," and that some foundations may need replacing. A rewrite is more defensible if the code can't be decomposed, the technology is unsupportable, or the goal is really a new product for a new market.

Weighing who favors each idea, it calls the rewrite a "cape" idea. It wins the announcement, excites the board, marketing, and chosen engineers, and splits staff into "new" and "legacy" lunch tables, but it loses the delivery. Incremental work is "chores." It pleases product, customers, and finance but can lose the storytelling war.

It proposes a third path, a structured strangler approach with a visible greenfield flagship:
- The CTO leads a real new foundation.
- Something new ships cloud-native within 9–12 months.
- Capabilities are carved off and retired by value and pain.
- Product owns feature sequencing.
- People rotate across old and new.
- Progress metrics are published, such as the share of transactions on new components, modules retired, feature lead time, and attrition.

Its key caveat is not to let either leader "win" and leave defeated.
