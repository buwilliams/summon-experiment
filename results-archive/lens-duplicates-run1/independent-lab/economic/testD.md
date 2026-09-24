# independent-lab/economic/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:35:43.490536+00:00

## Prompt

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

I want to understand how each proposal makes the business more profitable. Follow the money through each strategy. What revenue would it generate or protect, and what investment and operating costs would it require? If each proposal went ahead, when would returns arrive and what risks could wipe them out? Where could spending grow without a corresponding improvement in profits? Who would control the budget, own the financial results, and decide when to stop investing? And is there a third approach that offers better returns for the capital at risk while keeping the business profitable?

## Response

# Internal Transformation vs. Independent Innovation Lab: Following the Money

Neither pure strategy is right for a company that is losing customers *and* losing deals. The CEO's approach protects revenue fastest but may not change enough to win new business. Your lab could create future revenue, but it does nothing about the revenue walking out the door today. And launching it against the CEO's stated philosophy puts both the lab and your credibility at risk.

The better answer is to sequence and stage the capital. Below is the financial logic, then a third approach.

## First: The Money Problem You're Actually Solving

I don't have your numbers, so here is an illustrative model. Replace it with real figures in your first 30 days.

| Assumption | Illustrative value |
|---|---|
| Annual revenue | $300M |
| Recurring (subscription/maintenance) | $240M ARR |
| Gross churn | 12% ≈ **$29M ARR lost per year** |
| New ARR booked | $20M per year (falling win rate) |
| Net result | Shrinking about $9M ARR per year, compounding |

Three facts about insurance software shape everything that follows:

1. **Lost customers are very expensive to replace.** Enterprise insurance sales cycles often run 12–24 months, and implementations run 12–36 months. A dollar of churned ARR can take two or more years to replace, at high acquisition cost.
2. **Retained revenue is high-margin.** Maintenance and subscription revenue on an installed base often carries 70–85% gross margin. Each point of churn reduction drops almost straight to profit.
3. **Buyers are conservative.** Carriers buy from vendors with regulatory credibility, integration depth, and reference customers. New products from unknown units face a long credibility gap.

So the first question isn't "lab or no lab." It's **why are customers leaving and why are you losing deals?** The answer determines which strategy pays:

- **Churn from implementation pain, service quality, slow releases, or cost to operate:** fixable largely inside the existing organization. The CEO's approach has real merit.
- **Product architecturally behind cloud-native competitors** (modern policy, billing, and claims platforms; insurtechs): internal fixes slow the decline but don't reverse it. You need a new platform, which is bigger than a lab.
- **Losing specific segments** (e.g., MGAs, specialty lines, embedded insurance) to focused competitors: a targeted new-product bet may be justified.

## Strategy A: The CEO's Approach (Work Within Existing Systems)

**Revenue generated or protected**
- Mostly *protected* revenue. Cutting churn from 12% to 8% saves about $10M ARR per year, and it compounds: three years of retention improvement can be worth $25–30M+ in ARR that would otherwise be gone.
- Modest new revenue from better win rates if implementation time and product gaps improve.

**Investment and operating costs**
- Mostly reallocation of existing people and budget, plus perhaps $3–6M per year incremental for customer success, implementation tooling, defect backlog reduction, and targeted features.
- Low capital at risk.

**When returns arrive**
- Two to four quarters for retention gains, which show up at renewals.
- Win-rate improvements take 12–24 months to appear, because of the sales cycle.

**Risks that could wipe out returns**
- **The same system that produced the decline stays in charge.** Incentives, release processes, and decision rights that caused churn remain intact.
- **Incrementalism hits a ceiling.** If the product is fundamentally behind, you delay churn rather than prevent it. Renewals get pushed out one or two years, then lost anyway.
- **"Innovation" gets starved** every time a quarterly target is threatened.

**Where spending grows without profit**
- **Retention discounting:** saving accounts with price cuts protects revenue but erodes margin.
- **One-off customizations for at-risk customers:** each creates permanent maintenance cost and slows future releases.
- **Consultants, reorganizations, and "transformation programs"** that measure activity rather than retention or win rate.
- **Pilot sprawl:** dozens of small initiatives, none funded enough to matter, none ever killed.

**Budget control, results ownership, and stop decisions**
- Existing business-unit leaders control budget and own the P&L.
- The weakness is that **nobody decides to stop.** Initiatives rarely get killed in a large organization. They linger and absorb capacity.
- Your role risks becoming advisory: accountable for "outsized results" without controlling the resources.

## Strategy B: Independent Innovation Lab (Your Proposal)

**Revenue generated or protected**
- New revenue from new products or segments, such as AI-assisted underwriting or claims, products for MGAs and insurtechs, embedded insurance, or a modern cloud product line.
- Almost no protected revenue in the near term. The lab doesn't fix why today's customers are leaving.

**Investment and operating costs**
- A credible lab with 20–40 people (product, engineering, design, data, and some go-to-market) likely costs $6–12M per year fully loaded.
- Add integration costs later, because insurance products must connect to core systems, data, and compliance.
- Expect $20–35M cumulative over three years before meaningful revenue.

**When returns arrive**
- Pilots with design partners: year 1–2.
- First paying enterprise customers: year 2–3.
- Material revenue, meaning enough to offset churn: typically year 4 or later, if it works.
- Meanwhile, in the illustrative model, you've lost roughly $85M in ARR over those three years if churn isn't addressed in parallel.

**Risks that could wipe out returns**
- **Loss of executive sponsorship. This is the biggest risk.** The CEO doesn't believe in this model. Labs without committed CEO backing usually get cut at the first bad quarter, which in a declining company comes soon.
- **The adoption gap.** The lab builds things the core business can't sell, integrate, or support. The lab's success then produces no company revenue.
- **Distribution dependency.** Your biggest asset is existing carrier relationships. An independent lab is cut off from them unless deliberately connected.
- **Base-rate risk.** Most new-product bets fail. With perhaps a 1-in-4 chance of a meaningful hit, the expected value is low unless the potential payoff is very large.
- **Cultural backlash.** The core organization sees the lab as privileged and undermines it.

**Where spending grows without profit**
- Headcount creep before product-market fit.
- Rebuilding infrastructure the core already has (security, compliance, hosting) in the name of independence.
- "Platform" ambitions: a lab that decides to rewrite the core system becomes a multi-year, $50M+ program without the governance of one.
- Vanity pilots with unpaid "partners" who never convert.

**Budget control, results ownership, and stop decisions**
- You would control the budget, but financial results are often owned by nobody. The lab has no P&L, and the core business doesn't count lab revenue as its own.
- Stop decisions typically become political rather than evidence-based.

## Strategy C: A Better Risk-Adjusted Approach

The idea is to **stop the bleeding first and fund bets like a venture investor.** Structure this as a portfolio with three layers, funded in stages, with explicit kill criteria and a CFO at the table.

### Layer 1: Revenue Defense (about 60–70% of your effort in year 1)

A churn and win-loss program run with authority, not as advice.

- **Diagnose:** interview churned and at-risk customers and lost deals, and segment churn by cause and by account profitability.
- **Fix the top two or three drivers**, typically implementation time, release quality, cost to operate, or a missing capability.
- **Budget:** a few million dollars incremental, largely self-funding within a year.
- **Owner:** co-owned by you and the Chief Revenue Officer or COO. Metrics are gross revenue retention, net revenue retention, win rate, and implementation time.
- **Discipline:** don't save unprofitable accounts with custom work or deep discounts. Some churn is healthy.

This is where the CEO is right, and delivering here earns you the credibility and capital for Layer 2.

### Layer 2: Embedded Strike Teams (about 20–30%)

These are small teams of 6–10 people that operate with startup rules (their own backlog, fast releases, direct customer access) inside the company. Each is attached to a specific revenue problem, for example:

- Cut implementation time by half with configuration tooling or AI-assisted migration.
- Build a modern API and integration layer so the legacy product competes on openness.
- Add AI capabilities to claims or underwriting workflows that existing customers will pay for as add-ons.

These use the existing distribution, customers, and data, which is the advantage an independent lab gives up. Returns arrive in 6–18 months through upsell, retention, and win rate.

### Layer 3: Staged New-Business Bets (about 10%)

This is where your lab instinct belongs, but small and metered.

- One or two bets at a time, each funded in tranches: for example, $500K to validate, $2M to reach paying design partners, and larger funding only after hitting pre-agreed milestones.
- Require paying design partners early. Carriers willing to pay for a pilot are the strongest evidence.
- Consider **partner, acquire, or invest** as alternatives to building. Buying a small insurtech with traction can be cheaper and faster than a three-year build.
- Independence is earned: a bet that proves traction can spin out into a more autonomous unit.

### Governance for All Three Layers

| Question | Answer |
|---|---|
| Who controls the budget? | An investment committee: CEO, CFO, you, and the CRO |
| Who owns financial results? | Layer 1: the business unit P&L. Layer 2: shared with the product line whose revenue it affects. Layer 3: you, with a separate P&L. |
| Who decides when to stop? | The committee, against kill criteria set *before* funding (e.g., "no paying design partner by month 9 means stop") |
| How is it funded? | Ring-fence part of the retention gains from Layer 1 to fund Layers 2 and 3. This keeps the business profitable and makes innovation self-financing. |

## Comparison

| | A: Work within | B: Independent lab | C: Staged portfolio |
|---|---|---|---|
| Capital at risk (3 yrs, illustrative) | Low ($10–15M, mostly reallocated) | High ($20–35M) | Moderate ($12–20M, staged) |
| Time to first returns | 2–4 quarters | 2–4 years | 2–4 quarters |
| Addresses churn | Yes | No | Yes |
| Addresses new business | Weakly | Potentially strongly | Moderately, and grows over time |
| Biggest risk | Too incremental | Loss of sponsorship; adoption gap | Complexity; needs strong governance |
| Fits CEO's stated view | Fully | Conflicts | Largely, while expanding it |

## A Caveat Worth Taking Seriously

If your diagnosis shows the core product is architecturally obsolete (on-premise, monolithic, and losing head-to-head against cloud-native platforms), the math changes. Then neither the CEO's plan nor a lab is enough. The company faces a platform-replacement decision costing tens of millions over several years. That is a board-level capital allocation choice (build, buy, or merge), not an innovation program, and you should frame it that way.

## What to Do in the Next 90 Days

1. **Build the real version of the model above:** ARR, churn by cause, win-loss reasons, cost to serve, and margin by customer segment.
2. **Deliver one visible retention win** that the CEO can see in renewal numbers.
3. **Propose Strategy C as an extension of the CEO's thesis rather than a rejection of it:** "Working within the system is right for protecting revenue. Here's a small, staged, self-funded way to also create new revenue."
4. **Get the CFO on your side early.** Kill criteria and staged funding are what make innovation investable in a company under pressure.

Your instinct that the existing organization won't produce outsized results on its own is probably correct. But the path to independence runs through proving you can protect the revenue that exists today.

## Summary (sent to Jev)

The response argues that neither pure strategy fits a company that is both losing customers and losing deals. Working within existing systems protects revenue fastest but may be too incremental to win new business. An independent lab might create future revenue but does nothing about current churn, and launching it against the CEO's philosophy endangers the lab and the new leader's credibility.

It first urges diagnosing why customers leave and deals are lost. Using an illustrative model to be replaced with real figures within 30 days, it notes that churned insurance-software revenue takes years to replace, retained revenue is high-margin, and buyers are conservative. Churn from service or implementation problems favors internal fixes. An architecturally outdated product requires a new platform. Losses in specific segments may justify targeted bets.

It recommends a staged portfolio:
- **Revenue defense (60–70% of year-one effort):** a churn and win-loss program with real authority.
- **Embedded strike teams (20–30%):** small startup-style teams inside the company, tied to specific revenue problems and using existing distribution.
- **New-business bets (about 10%):** funded in tranches with paying design partners and pre-set kill criteria, with partnering or acquisition as alternatives to building.

An investment committee of the CEO, CFO, innovation leader, and CRO would govern all three layers. Part of the retention gains would fund the innovation work, and independence would be earned through traction.

The key caveat is that if the core product proves architecturally obsolete, the issue becomes a board-level platform-replacement decision rather than an innovation program.

For the next 90 days, it advises building the real model, delivering a visible retention win, pitching the portfolio as an extension of the CEO's thesis, and winning over the CFO early.
