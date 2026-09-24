# churn-cause/critical-rationalism/testB

Model: claude-opus-5-5 · 2026-09-24T15:29:29.784036+00:00

## Turn 1

**User:** You are a world-class philosopher of science.

I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

# Short answer: you can't know yet, and neither can they

Both VPs have offered a plausible causal story. Both stories also happen to recommend investing in the speaker's own function. That doesn't make either wrong, but it means you're hearing two hypotheses, not two findings. The good news is that they make **different predictions** about data you almost certainly already have, so you can find out which is closer to the truth in a few weeks rather than arguing about it for a few quarters.

## 1. Reframe the question

"Which belief is right?" assumes one cause. Churn doubling is an aggregate. It could be:

- **Mostly one cause.** One VP is largely right.
- **A mixture.** Different segments churn for different reasons, such as small carriers failing to adopt while large carriers are poached by AI-heavy competitors.
- **An interaction.** The causes feed each other. Customers who never got to full value *perceive* product gaps because they never adopted the analytics you already have. Or rapid feature additions make implementations longer and messier.
- **Something else entirely.** Regional carrier M&A, a pricing change, a new buyer persona (CIOs replacing claims VPs), or a single competitor's aggressive discounting.

Keep all of these on the table until the evidence removes them.

## 2. Ask the most diagnostic question first: what changed ~18 months ago?

A doubling is a change, so look for a change in its causes:

- Did implementation staffing, methodology, or partners change?
- Did a competitor launch an AI/analytics product?
- Did you change pricing or packaging, or move upmarket or downmarket?
- Was there a wave of acquisitions among your customers?

If the churn inflection lines up with one of these, that is strong evidence. If product gaps have existed for years but churn only recently rose, the product hypothesis needs an explanation for the timing, such as competitors only recently crossing a threshold.

## 3. Use discriminating predictions

| Evidence | If Product is right | If Services is right |
|---|---|---|
| **When churn occurs** | Spread across renewals, including mature, long-tenured customers | Concentrated at first or second renewal |
| **Implementation history of churned accounts** | Similar to retained accounts | Longer, over budget, more escalations |
| **Adoption before churning** | Healthy usage that hit the product's ceiling | Low adoption and key modules never went live |
| **Use of your *existing* analytics** | Used, and found insufficient | Largely unused |
| **Where churned customers go** | To competitors with stronger AI/analytics | To whoever promised an easier rollout, back to legacy or in-house, or anywhere cheaper |
| **Support tickets before churn** | Feature requests | Configuration, integration, and "how do I" issues; slow resolution |
| **New-logo win/loss** | Losing new deals on features too | Winning deals but losing customers post-sale |

The win/loss row is especially useful. Prospects haven't experienced your implementation, so if you're losing *new* deals on features, the product gap is real in the market regardless of what's driving churn.

## 4. Be skeptical of stated reasons

Exit surveys and churn-call notes will probably favor "missing features." That isn't because it's true. It's the easiest, least confrontational thing to say. "Your competitor has AI" is a cleaner story for the canceling executive than "our team never finished the rollout." The person who signs the cancellation is also often not the person who lived through implementation.

So treat stated reasons as one data source, weighted below **behavioral** data: usage, time-to-go-live, ticket history, and destination. Where they conflict, believe the behavior. A few candid conversations with former *end users*, not just buyers, are worth more than a stack of survey responses.

## 5. What to do

**This week: make the hypotheses falsifiable.** Sit both VPs down and ask each: *"What would we see in the data if you were wrong?"* Get them to commit in writing before anyone looks. This is the single most valuable step. It turns a turf fight into a shared inquiry, and it prevents both sides from reinterpreting ambiguous results as confirmation.

**Next 2–4 weeks: run the analysis.** Pull every churned account from the last 18–24 months plus a comparable sample of retained accounts. For each, code tenure at churn, implementation duration and overrun, modules live versus purchased, usage trend, ticket themes, segment and size, and destination. Then compare. You don't need sophisticated statistics; with a few dozen churned accounts, clear patterns will be visible.

**In parallel: take low-regret actions that are right under either hypothesis.**
- Identify at-risk renewals in the next two quarters and intervene now.
- Start measuring **time-to-value** as a company-level metric if you aren't already.
- Check whether customers are using the analytics you already ship. If they aren't, building more analytics is premature under *either* story.

**Then allocate by segment, not by winner.** The likely outcome is something like "churn among small carriers is mostly failed implementation; churn among our largest accounts is mostly competitive product loss." That tells you to fix onboarding for one segment and prioritize specific roadmap items for the other. That is a better answer than either VP's.

## The general lesson

When two smart people disagree about a cause, the productive move is rarely to judge whose argument is more persuasive. Ask what each view predicts that the other doesn't, then go look. You're in a fortunate position: the evidence that settles this is already sitting in your CRM, support system, and usage logs.

## Turn 2

**User:** What if our usage and implementation data is spotty for older accounts? Can we still trust the comparison with only a few dozen churned customers?

**Assistant:**

# Yes, with the right expectations

Spotty data and a small sample are two different problems. The first is more dangerous than the second, so take them in that order.

## 1. The bigger risk: *which* data is missing

A small sample makes your estimates noisy. Missing data that isn't random makes them **biased**, and bias doesn't shrink as you gather more.

Your situation has a specific trap. Older accounts are disproportionately likely to have churned *and* to have poor data. Recent accounts are more likely to be retained *and* well instrumented. So if you compare "churned accounts with usable data" to "retained accounts with usable data," you may be comparing different eras, not different outcomes. That's a confound between time and churn status.

Three ways to handle it:

**Check whether missingness tracks the outcome.** Before any analysis, make a simple table of the share of churned versus retained accounts with complete data, broken out by signing year. If completeness is similar across groups within each cohort, the missingness is less worrying. If churned accounts are systematically less documented, keep that in front of you as you interpret everything else.

**Treat missingness as a possible signal.** Sometimes data is missing *because* of the thing you're studying. An account with no usage logs may never have gone fully live. An account with no implementation record may have been rushed through with little process. Don't quietly drop these accounts; code "data missing" as its own category and see whether it clusters among churners.

**Run a sensitivity analysis.** For accounts with unknown values, compute the result twice: once assuming every unknown favors the Product hypothesis, once assuming every unknown favors Services. If the conclusion survives both extremes, missing data isn't driving it. If it flips, you've learned exactly how much the gaps matter and where to spend effort filling them.

## 2. Recover more than you think is lost

"We don't have usage data" usually means "we don't have it in the dashboard." Implementation and adoption leave traces elsewhere:

- **Billing and contracts.** SOW dates, change orders, and professional-services hours billed are good proxies for implementation length and overrun.
- **Support-ticket timestamps.** The date tickets shift from setup questions to operational ones marks a rough go-live.
- **CRM and email.** CSM notes, escalation threads, and QBR decks often record which modules went live and when.
- **People.** Long-tenured CSMs and implementation leads can often reconstruct an account's story in ten minutes. That's memory-based and imperfect, so record it as lower-confidence, but it's far better than nothing.
- **Former customers.** A handful of calls with ex-users, not just ex-buyers, can fill gaps and check the other sources.

Record where each data point came from, so you can later check whether conclusions hold using only the more reliable sources.

## 3. What a few dozen cases can and can't tell you

With, say, 30 churned and 60 retained accounts:

- **You can detect large differences.** If 70% of churned accounts had implementation overruns versus 25% of retained accounts, that won't be a fluke.
- **You can't detect subtle ones.** 40% versus 32% is within the noise at this size.

That limitation matters less than it sounds. **Churn doubled.** Whatever caused that is, almost by definition, a big effect. If neither hypothesis produces a clear, large difference in your data, that is itself informative. It suggests the cause is something neither VP named, such as M&A, pricing, or a single competitor, or a mix of modest factors.

Two further protections for small samples:

**Rely on convergence, not any single number.** One weak signal proves little. But if churners show longer implementations *and* lower adoption *and* setup-heavy tickets *and* first-renewal timing *and* destinations that aren't feature leaders, those are partly independent lines of evidence pointing the same way. Agreement across them is much more trustworthy than any one comparison. Conversely, if the signals conflict, don't pick the one you like; that's a sign of mixed causes or a segment split.

**Supplement the statistics with case reasoning.** With few cases, you can study each one. Pick 8–10 churned accounts spanning segments and write a short causal narrative for each: what happened, when, and what the evidence was at each step. Patterns that appear across well-documented cases are credible even when counts are too small for formal tests. Take care to include cases that might *contradict* each hypothesis, not just illustrative ones.

## 4. You don't need certainty, just enough to act

The goal isn't proof. It's to shift your confidence enough to make a better allocation decision than you'd make today. Ask yourself: *what result would make us move budget, and in which direction?* If the evidence clears that bar, act. If it doesn't, act on the low-regret moves (at-risk renewal interventions, checking whether existing analytics are used) and keep investigating.

## 5. Fix the data going forward

Whatever this analysis finds, the fact that you can't easily answer "why are customers leaving?" is itself a finding. Start capturing, for every new account:

- implementation start, planned go-live, and actual go-live;
- modules purchased versus modules live;
- a simple monthly usage and health signal;
- a structured churn record covering destination and the competitor named, plus the stated reason alongside the CSM's assessment.

In two or three quarters you'll have a clean, prospective dataset. It will confirm or correct what you conclude now, and you won't face this problem again.

## Bottom line

You can trust the comparison for **large, consistent patterns**, provided you check whether missingness tracks churn, recover what you can from indirect sources, and test whether conclusions survive pessimistic assumptions about the gaps. Treat small differences and single signals as inconclusive. And given that churn doubled, a real cause should be visible even in imperfect data.

## Turn 3

**User:** How do I get both VPs to actually commit in writing to what would prove them wrong, without it feeling like a trap?

**Assistant:**

# Make it a shared bet, not a cross-examination

It feels like a trap when one person is being asked to state the conditions of their defeat while someone else watches. It feels like good practice when everyone, including you, writes down predictions before seeing the data, and when the outcome decides a *plan* rather than a *winner*. Most of the work is in how you set it up.

## 1. Change the question you ask

"What would prove you wrong?" puts people on the defensive. Ask instead:

- **"If you're right, what should we see in the churned accounts?"** People are glad to describe what their theory predicts. That's the same commitment, framed positively.
- **"What would surprise you?"** This gets at disconfirming evidence without the word "wrong."
- **"What result would make you want a different plan?"** This ties the commitment to a decision, not to their ego.

A clear prediction is a falsifiable claim. You don't have to say so.

## 2. Make it symmetric, and go first yourself

Nothing feels less like a trap than the person running the process exposing themselves too. Write down your own predictions, including where you're genuinely unsure. Include at least one hypothesis neither VP holds (M&A, pricing, a specific competitor), so it's clearly not a two-person contest you're refereeing.

Apply the same questions, the same template, and the same deadline to both VPs. Any asymmetry will be read as taking sides.

## 3. Take the zero-sum stakes off the table early

The fear underneath the resistance is usually "if the data goes against me, I lose budget, headcount, or credibility." Address it directly:

- **Say out loud that mixed results are the likely outcome.** "My guess is we'll find you're each right about different segments. The point is to know which."
- **Pre-agree that the output is an allocation, not a verdict.** Better still, sketch together in advance what each broad outcome would mean for the plan, so no one is negotiating their future after the numbers are in.
- **If you can, get your CEO or their shared boss to endorse the process** and to say explicitly that updating a view on evidence will be treated as a strength. People take intellectual risks when leadership visibly rewards it.

## 4. Give them ownership of the test

People trust tests they helped design and resist tests imposed on them. Invite each VP to:

- propose the metrics and definitions ("what counts as an implementation overrun?");
- name the evidence they think would be most convincing for their side;
- flag data they think is unreliable *before* results exist.

This does double duty. It makes them co-authors rather than subjects, and it closes off the most common post-hoc escape: "that metric doesn't really measure what matters."

## 5. Ask for ranges and confidence, not certainty

A hard binary prediction ("most churners will have had bad implementations") feels like staking everything on one throw. Let them hedge honestly:

- "I'd expect at least half of churned accounts to have gone to feature-leading competitors, and I'm about 70% confident."
- "If fewer than a third did, I'd seriously reconsider."

That still pins down a meaningful prediction. It also makes updating feel like a normal adjustment rather than a public reversal.

## 6. Sequence it: private, then shared

1. **Separately, 1:1.** Ask each VP for their predictions privately first. People state views more candidly without an audience, and it prevents anchoring on or posturing against each other.
2. **Together.** Share all predictions, including yours, side by side. Discuss where they genuinely diverge; that's where the data will be informative. Agree on definitions and data sources.
3. **Lock it.** Circulate a one-page document everyone has seen, dated before analysis begins.
4. **Review.** When results come in, go back to the document together, row by row.

## 7. A simple template

For each person:

| | |
|---|---|
| **My main explanation for the churn increase** | |
| **What we should see if I'm right** (2–4 specific patterns) | |
| **What would surprise me** | |
| **Result that would change my recommended plan** | |
| **Confidence** | |
| **Other factors I think might be contributing** | |

The last row matters. It lets each VP acknowledge in advance that the other's view may be partly right, which makes the eventual result much easier to accept.

## 8. What to say

Something like:

> "You've both made strong cases, and honestly I think you're both seeing something real. Before we dig into the data, I'd like each of us, including me, to write down what we expect to find. That way we're testing ideas instead of arguing about them afterward, and nobody can be accused of reading the results to fit their view. I'm assuming we'll learn you're each right about different parts of the problem. What I want is to know which parts, so we put money in the right places."

## 9. Protect the process when results arrive

How you handle the first result determines whether anyone commits honestly next time:

- **Credit good predictions and good updating equally.** If a VP says "that changed my mind," say publicly that you value it.
- **Don't keep score.** Never frame the review as "Product was right, Services was wrong."
- **Take disputes about the data seriously, but check them against the pre-agreed definitions.** If someone wants to reinterpret, ask whether they'd have accepted that reinterpretation had the result gone their way.

## Bottom line

It stops feeling like a trap when it's **symmetric** (you commit too), **co-designed** (they shape the test), **low-stakes for identity** (the outcome is a plan, and mixed results are expected), and **honest about uncertainty** (ranges and confidence levels are allowed). Pre-registration is ultimately a protection for everyone: it guarantees that whoever turns out to be right can't be dismissed, and whoever turns out to be partly wrong can say they called what they could.

## Turn 4

**User:** What if one of the VPs refuses to commit to specific predictions, or keeps them vague enough that nothing could contradict them?

**Assistant:**

# First figure out why, then respond to the reason

Vagueness isn't always evasion. Before pushing, work out which of these you're dealing with, because each calls for a different response.

| Likely reason | What it sounds like | What helps |
|---|---|---|
| **Fear of losing** (budget, credibility, status) | "It's complicated," "the data won't capture it" | Lower the stakes further; make updating safe |
| **Genuine uncertainty** | "I really don't know what we'd see" | Help them articulate; accept ranges |
| **Unfamiliarity with the exercise** | Long narrative answers, no specifics | Offer concrete options to react to |
| **The belief isn't really empirical** | "We need AI regardless of why people churn" | Separate the strategy question from the diagnostic one |
| **Political positioning** | Agrees in the room, stays vague on paper | Make the process's consequences clear and neutral |

Often it's a mix. Treat it first as a problem of articulation, not character. You'll be right more often, and you'll preserve the relationship if you're wrong.

## 1. Make it easier to be specific

Many people who resist abstract questions will happily react to concrete ones.

**Offer candidate predictions to edit.** Instead of "what would you expect?", say: "Here are four things I'd guess your view predicts. Which do you agree with, which would you change, and which don't follow?" It's much easier to correct a draft than to write from scratch. It also shows you've taken their view seriously enough to work out its implications.

**Ask comparative questions.** "Would you expect churned accounts to have *longer* or *shorter* implementations than retained ones?" A direction is a real prediction, and most people will commit to one.

**Ask about the decision, not the prediction.** "Suppose we found that 80% of churned accounts never took the analytics module live. Would you still recommend accelerating the analytics roadmap first?" A hypothetical about action often gets a clearer answer than a question about evidence, and it reveals whether their plan actually depends on the data.

**Use the reverse question.** "What would you expect to see if [the other VP] were right?" People are often sharper about the other side's predictions, and the answer implicitly defines what they themselves expect *not* to see.

## 2. Distinguish a strategy view from a diagnosis

This is the most important move, and it's the one most likely to unlock things.

"Competitors have better AI, so we need to build it" may be two claims fused together:

1. **A diagnostic claim:** product gaps are driving *current* churn. This is testable with your data.
2. **A strategic claim:** we need AI and analytics to stay competitive over the next several years, regardless of why today's customers are leaving. This is a legitimate judgment about the market, but churn data can't settle it.

The same split may apply to the Services VP: "our implementations are too slow" may be both an explanation of churn and an independent operational concern.

Name the distinction explicitly and generously: "I think you may be making two arguments, and one of them doesn't depend on this analysis at all. Let's put the long-term competitive case on a separate track so it doesn't ride on what the churn data shows." This often dissolves the resistance, because the VP no longer feels their whole agenda is on trial. It also sharpens the diagnostic claim, which is now the only thing being tested.

## 3. Be clear about what vagueness costs, without making it a threat

In philosophy of science, a claim compatible with every possible observation isn't thereby false. It's just that no observation can *support* it. A theory that forbids nothing gains no credit from any result.

The practical version, said neutrally and applied to everyone:

> "The analysis is going ahead either way, and it'll inform how we allocate next year. Where someone has said what they expect, the results can support their case. Where a view is left open, the data can't really count in its favor, because we can't tell whether it confirmed anything. I'd rather both of your views had the chance to be supported."

This frames specificity as being *in their interest*, which it is. A vague position can't win. It can only avoid losing, and in a budget discussion that's usually a weaker position than committing and being partly right.

Two cautions:

- **Don't say it as a warning to one person.** Say it to both, ideally when explaining the process, before anyone has been vague.
- **Don't punish the VP who did commit.** If one VP made specific predictions and some were wrong, while the other stayed vague and so was "never wrong," the lesson everyone learns is to stay vague. Make sure the one who committed is visibly credited for it, whatever the results.

## 4. Record the vague position anyway

If a VP still won't be specific, write down what they *did* say as faithfully as you can, and share it with them for correction: "Here's how I've captured your view. Is this fair?"

This helps in two ways:

- It often prompts them to sharpen it themselves, because a vague statement looks weaker on paper than it sounded in conversation.
- It guards against the most common failure: reinterpreting a vague prediction after the fact so it seems to have anticipated whatever happened. With the dated record in hand, you can ask, "Is this what you expected when we wrote it down?"

## 5. Watch for escape routes after the results arrive

Even people who committed may try to explain away inconvenient results. Some adjustment is legitimate; the data really can be flawed. Unlimited adjustment isn't. The difference:

- **Legitimate:** "The implementation data for 2022 accounts was unreliable, and we flagged that before the analysis." The objection was raised in advance, or it identifies a specific, checkable flaw.
- **Evasive:** "Churned customers wouldn't *say* they left for AI features, but that's the real reason." A new, untestable auxiliary claim appears only after the prediction failed, and it would rescue the theory from any result.

When a post-hoc explanation appears, ask two questions: *Would you have accepted this reasoning if the result had gone your way?* and *What further evidence would show whether this explanation is right?* If there's a real answer to the second, it's worth checking. If there isn't, note it and move on.

## 6. If it still doesn't work

- **Take it 1:1 and ask directly what they're worried about.** "I've noticed it's been hard to pin down predictions. Is there something about how this will be used that concerns you?" The answer is often something you can fix, like fear that results will be shown to the CEO without context.
- **Involve the shared sponsor if needed,** not as an escalation against the VP, but to reaffirm that the process applies to everyone and that updating on evidence is expected and valued.
- **Proceed anyway.** The analysis doesn't require unanimous buy-in. You can still examine what the data shows about each hypothesis as you understand it. The pre-registered predictions add rigor and fairness, but the underlying evidence remains informative even if one VP never commits.

## A script for the 1:1

> "I want to make sure your view gets a fair hearing in this. Right now it's framed broadly enough that I'm not sure what the data could show in its favor, and I'd hate for the analysis to come back and your case not get credit because we never said what to look for. Can we try getting concrete? Here are a few things I think your view predicts. Tell me which ones you'd stand behind. And if part of your argument is really about where the market's going long-term, let's pull that out separately, because I don't think churn data should decide that."

## Bottom line

Assume articulation difficulty before bad faith, and make specificity easy by offering drafts, directions, and decision hypotheticals. Separate the testable diagnosis from the long-term strategic judgment, which is often what the resistance is really protecting. Be honest, with both VPs equally, that a claim nothing could contradict is also a claim nothing can support. Then record what was said and proceed. The evidence will still inform the decision, and the process protects anyone willing to be specific.

## Turn 5

**User:** What should we do?

**Assistant:**

# The plan

You don't have to pick a side today. Here's the sequence I'd run, in about six weeks.

## Now: low-regret moves (this week)

These are right whichever VP turns out to be correct, so start them immediately.

1. **Protect upcoming renewals.** List every account renewing in the next two quarters, flag the at-risk ones (low usage, stalled implementation, recent escalations, executive turnover), and assign an owner and a save plan to each. Every retained account is worth more than any analysis.
2. **Check whether customers use what you already have.** Pull adoption of your existing analytics. If most customers aren't using it, that tells you something important under *either* hypothesis.
3. **Freeze nothing, commit nothing big.** Keep the roadmap and services work moving as planned, but hold off on major reallocations until the evidence is in. Six weeks of patience is cheap compared with a year of misdirected investment.

## Weeks 1–2: set up the test

4. **Get predictions on paper.** Meet each VP 1:1, then together. Use the template from before. Write down your own predictions too, plus alternative explanations neither VP named (M&A, pricing, a specific competitor).
5. **Split strategy from diagnosis.** Put the long-term "do we need AI to compete in three years?" question on its own track. It deserves a decision, but churn data won't make it.
6. **Agree definitions and data sources** before anyone looks at results.

## Weeks 2–5: run the analysis

7. **Find the inflection.** What changed around 18 months ago? Line up churn timing against staffing, pricing, competitor launches, and customer M&A.
8. **Build the churn file.** For every churned account and a comparison set of retained ones, record tenure at churn, implementation length and overrun, modules live versus purchased, usage trend, ticket themes, segment, and destination. Fill gaps from billing, tickets, CRM notes, and people's memories, and note which source each data point came from.
9. **Check your new-logo win/loss.** That's the cleanest test of whether product gaps are real in the market.
10. **Write up 8–10 case narratives** across segments, including ones that cut against each hypothesis.
11. **Stress-test the conclusion.** Does it hold under pessimistic assumptions about the missing data? Do several independent signals point the same way?

## Week 6: decide

12. **Review against the pre-registered predictions,** together, row by row.
13. **Allocate by segment and cause, not by winner.** The most likely result is something like "onboarding failure drives churn among smaller carriers; competitive product loss drives it among the largest." Fund each fix where the evidence puts it.
14. **Set measurable targets** for whatever you fund, such as time-to-go-live, first-renewal retention, or competitive losses, so you know within two or three quarters whether it's working.

## Ongoing

15. **Instrument everything from now on:** go-live dates, modules live, monthly health scores, and structured churn records. Next time you won't need a six-week forensic exercise.
16. **Revisit in two quarters** with clean prospective data to confirm or correct what you concluded.

## If you forced me to bet today

I'd put modestly more weight on the **implementation and time-to-value** story as the main driver of *current* churn. In enterprise software with long, complex rollouts, customers who never reach full value are a very common source of churn. "Missing features" is also the easiest reason for a departing customer to give, whatever the real one. And customers who never adopted your existing analytics will naturally see a competitor's analytics as better.

But the product concern is likely real in the *market*, especially if competitors recently shipped AI capabilities. It may matter more for new sales and future retention than for the churn you're seeing now.

Treat that as a prior, not a conclusion. The whole point of the next six weeks is to let the evidence overrule it, including my guess.

## Bottom line

Protect renewals now. Get everyone's predictions on paper. Spend a month on the evidence you already have. Then fund the fixes the data supports, segment by segment, with targets that will tell you whether you were right.

## Outcome summary (sent to Jev)

Neither VP's belief can be confirmed yet, so the recommendation is to avoid picking a side and instead run a roughly six-week diagnostic. Both explanations are plausible hypotheses that make different, checkable predictions, and the evidence already sits in the CRM, support system, billing records, and usage logs.

Immediately, the company should take low-regret steps that are right under either view:

- Identify at-risk renewals over the next two quarters and assign owners and save plans.
- Check whether customers actually use the existing analytics.
- Keep current work moving while deferring major reallocations.

Next, each VP should privately, then jointly, write down predictions before seeing data. The customer success lead should do the same. These predictions should include alternatives such as M&A, pricing, or a specific competitor. The long-term question of whether AI is needed to compete should be split off, since churn data cannot settle it. Everyone should agree on definitions and sources in advance.

The analysis itself should:

- Pinpoint what changed about 18 months ago.
- Compare churned and retained accounts on tenure at churn, implementation length, modules live, usage, ticket themes, segment, and destination.
- Examine new-logo win/loss.
- Write eight to ten case narratives, including ones that cut against each hypothesis.

Conclusions should be trusted only for large, convergent patterns that survive pessimistic assumptions about missing data. Missingness itself may be a signal.

Funding should then go by segment and cause, not by winner, with measurable targets. The company should also instrument go-live dates, module adoption, health scores, and structured churn records going forward, and revisit in two quarters.

As a tentative prior, slightly more weight goes to implementation and time-to-value as the main driver of current churn. Departing customers tend to cite missing features, and non-adopters of existing analytics naturally find competitors' better. However, product gaps are likely real in the market, and this guess should be overruled if the evidence contradicts it.
