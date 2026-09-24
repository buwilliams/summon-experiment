# churn-cause/economic/testA

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:57:45.348891+00:00

## Prompt

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

## Response

## The short answer

Nobody can tell you which belief is right from the arguments alone, including me. Both are plausible, and they're often the same problem seen from two angles. A customer who never got fully implemented will experience your product as missing capabilities, and when a competitor demos slick AI analytics, that's the reason they'll give for leaving. So the stated reason and the root cause can differ.

The good news is that these two hypotheses leave different fingerprints in data you probably already have. As head of CS, you're well positioned to run the diagnostic and turn a political argument into an empirical one.

## First question: what changed 18 months ago?

Churn doubling is a shift, not a slow drift. Before testing either theory, list what changed around that time:

- **Competitive landscape:** a new entrant, a competitor launching AI features, or aggressive pricing.
- **Your product:** a major release, re-platforming, or a deprecated feature.
- **Your services org:** attrition, a reorg, offshoring, or a new implementation methodology.
- **Your customer mix:** a sales push that signed smaller or less-ready carriers, a new segment, or a big cohort of contracts from a past push now hitting first renewal.
- **The market:** carrier consolidation (acquired customers churn regardless), cost pressure, or regulatory changes.
- **Pricing or contract terms.**

Sometimes the answer is sitting in that list, and neither VP's theory is the main story.

## How to tell the two hypotheses apart

| Signal | Points to **Services** | Points to **Product** |
|---|---|---|
| Implementation length of churned vs. retained accounts | Churners had notably longer or incomplete implementations | No meaningful difference |
| Timing of churn | Clusters at first renewal | Spread out, including long-tenured accounts |
| Adoption before churn | Low usage, few modules live, few active users | Healthy, deep usage, then departure |
| Use of your *existing* analytics | Churners citing "analytics" never used what you have | Churners were heavy analytics users who hit a ceiling |
| Support history | High ticket volume, escalations, low CSAT | Relatively clean support history |
| New-logo win/loss | Win rates steady (prospects like the product) | Losing new deals to the same competitors on the same features |
| Where churners go | Varied destinations, or back to legacy/in-house | Concentrated on one or two competitors with specific capabilities |

Two of these are especially telling:

1. **Existing analytics usage.** If customers leave "for better analytics" but never adopted the analytics you already ship, the gap is value realization, not the roadmap.
2. **New-logo win rates.** Real product gaps usually show up in sales losses too, because prospects compare features directly. If sales is winning fine but customers leave, suspect the post-sale experience.

## Be skeptical of exit-interview reasons

"Your competitor has better AI" is the easiest thing to tell a vendor on the way out. It's impersonal and hard to argue with. "Your implementation was a mess and our team never trusted the system" is awkward to say. To get past this:

- Look at behavioral data (usage, timelines, tickets) before stated reasons.
- Separate the economic buyer's reason from the end users' experience. They're often different.
- Have someone neutral (not the account's CSM) do structured churn interviews that ask about the whole journey, not just "why are you leaving?"
- Ask churned customers what they expected at go-live versus what they got.

## What I'd do

**1. Run a 4–6 week churn diagnostic you own.** Pull every churned account from the last 18 months plus a matched set of retained accounts. For each, gather implementation duration versus plan, time to go-live, modules adopted, active users, analytics usage, support tickets and CSAT, tenure at churn, destination competitor, and segment/size. Add 10–15 structured interviews with churned customers.

**2. Get both VPs to agree on the evidence criteria before the results come in.** Put the table above, or your version of it, in front of them and ask: "If we see X, will you agree it's primarily a services problem? If we see Y, product?" This is the most important step. It keeps the analysis from becoming ammunition that each side reads its own way.

**3. Expect a mixed answer and segment it.** A common outcome is that the two problems split by customer type. Smaller carriers may churn from implementation pain, while larger, mature customers churn for capability. That tells you not just *whether* to invest in each area but *for whom*.

**4. Make low-regret moves now, without waiting.**
- Build an at-risk list of accounts with stalled implementations, low adoption, or upcoming first renewals, and run intervention plays on them.
- Start tracking time-to-first-value and adoption depth as leading indicators if you don't already.
- Arrange value-realization sessions for accounts not using the analytics you already have. This is cheap, and it also tests the hypothesis in real time.

## My honest prior

For vertical enterprise software sold to regional insurers, which are often lean on IT and change-management capacity, implementation and adoption failures are a very common hidden churn driver, and they frequently get reported as "product gaps." So I'd lean toward the Services hypothesis being at least a large part of the story, and I'd especially want to see whether churners had adopted your existing analytics.

But that's a prior, not a conclusion. If churners were deeply adopted, happy with support, and are all leaving for one competitor's AI capabilities while sales loses to the same competitor, your VP of Product is right and waiting would be costly. The diagnostic can answer this in about a month.

## Summary (sent to Jev)

The response says neither belief can be judged right from the arguments alone. Both are plausible and may be the same problem seen from two angles: a customer who was never fully implemented will experience the product as missing capabilities and may cite a competitor's AI analytics when leaving, so stated reasons and root causes can differ. Because churn doubled rather than drifted, it first recommends listing what changed 18 months ago: the competitive landscape, the product, the services org, the customer mix, market consolidation, and pricing. The answer might lie there instead.

To distinguish the hypotheses, it compares churned and retained accounts on implementation length, churn timing, adoption before churn, support history, new-logo win rates, and where churners go. Two signals matter most. If customers leave "for better analytics" but never used the existing analytics, the problem is value realization. If sales wins new deals fine while customers leave, the post-sale experience is the likely cause. It warns that exit-interview reasons are unreliable and urges using behavioral data, separating buyers' and users' views, and having neutral parties conduct structured interviews.

Its plan has four steps. First, run a four-to-six-week churn diagnostic covering all churned accounts plus matched retained ones, with 10–15 interviews. Second, and most important, get both VPs to agree on evidence criteria before results arrive. Third, expect a mixed answer, perhaps split by customer segment. Fourth, take low-regret actions now: build an at-risk list, track time-to-first-value, and hold value-realization sessions for customers not using the existing analytics.

Its prior leans toward Services being a large part of the story, but it stresses that this is not a conclusion. Product would be right if churners were deeply adopted and are leaving for one competitor's AI.
