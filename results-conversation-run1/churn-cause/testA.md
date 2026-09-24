# churn-cause/testA

Model: claude-opus-5-5 · 2026-09-24T14:00:07.407701+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

**Assistant:**

You can't tell which belief is right from the arguments alone, and neither can your VPs. Both stories are plausible, both fit the timing (the generative-AI wave and competitor AI launches landed roughly 18 months ago, and implementation problems compound over that span too), and each VP's theory conveniently points at the other's function. The good news is that the two hypotheses make **different, testable predictions**, and you likely already have most of the data to test them.

## What each hypothesis predicts

| Signal | If it's product gaps | If it's implementation/service |
|---|---|---|
| Adoption of churned accounts | Many were fully live and using the product well, then left anyway | Most never reached full deployment or deep usage |
| Correlation with implementation length | Weak | Strong: long implementations churn far more |
| Where they went | Specific competitors, citing specific features | Anywhere, or to a competitor that promised a smoother experience |
| New-logo sales | Win rates also falling against the same competitors on features | Win rates fine; problems start after signing |
| Support history | Normal ticket volume and CSAT before churn | Elevated tickets, escalations, low CSAT, stalled milestones |
| Healthy accounts | Even well-adopted accounts are showing risk | Well-adopted accounts retain well regardless of feature set |

## The interaction that may resolve the argument

Poor implementation can *create* a perceived product gap. If customers never get fully live, they never use the analytics you already have, and a competitor's demo looks like a leap forward. Listen for exit-interview lines like "we didn't know you could do that" or "we never got the reporting set up." If you hear those often, the feature gap is partly a symptom of the service problem, and building more features into a product customers can't fully deploy won't help.

The reverse can also be true. A flawless implementation won't save you if carriers now expect AI-assisted triage or fraud detection that you simply don't offer.

## Rule out other explanations first

Before choosing between the two, check for causes neither VP mentioned:
- **Carrier consolidation.** Regional carriers get acquired, and the acquirer often moves them onto its own platform. This churn isn't about you at all.
- **Upmarket competitors moving down.** Large core-system vendors bundling claims into suites.
- **Pricing.** Renewal increases or competitor discounting.
- **Cohort effects.** A batch of customers sold during a specific period, perhaps oversold or poorly qualified.
- **Champion turnover** at the customer.
- **What changed internally 18 months ago.** Services team turnover, a new product version that made implementations more complex, a change in sales comp.

## A 3–4 week diagnostic

1. **Build a churn dataset** of every churned account over 18 months, plus a comparison set of retained accounts. For each, pull contract date, implementation duration versus plan, go-live status, adoption depth at 6 and 12 months, support tickets and CSAT, ARR, where they went, and stated reason.
2. **Run cohort and correlation cuts.** Does churn track implementation length and adoption depth? Does it concentrate in certain cohorts, sizes, or implementation teams?
3. **Do neutral exit interviews** with 10–15 churned customers and 5–10 at-risk ones. Have someone who reports to neither VP run them (you, or an outside firm). Ask open questions before feature-specific ones, so you don't lead the witness.
4. **Pull win/loss data from sales** to see whether the same competitors and features show up in lost new deals.
5. **Attribute churned ARR to a primary cause** (product gap, implementation/service, consolidation, price, other). This turns "who's right" into "what share of the problem is each," which is what you need for allocating budget.

## What to do in the meantime

Some moves are worth doing regardless of the answer:
- **Triage at-risk renewals now.** Identify accounts renewing in the next two quarters with low adoption or stalled implementations, and assign senior attention.
- **Run an adoption push on existing capabilities,** especially analytics. It's cheap, it helps retention whichever story is right, and it also tests the hypothesis. If usage-driven accounts stabilize, that's evidence for the services view.
- **Track time-to-first-value** as a company-level metric if you don't already.
- **Hold off on major roadmap re-prioritization** until the diagnostic is done, unless you already have clear evidence of a specific feature causing losses.

## How to decide once you have data

- **Churn concentrated in poorly implemented accounts:** fix onboarding first. Shorten implementations, create a standardized fast-path deployment, and gate new feature investment on customers being able to reach value.
- **Churn common among healthy, well-adopted accounts leaving for specific features:** the product VP is right, and roadmap acceleration is justified. Target the specific features customers cite, not "AI" broadly.
- **Mixed, which is most likely:** allocate in proportion to attributed churned ARR, and sequence so that improvements in implementation make new features actually reachable.

Your role is an advantage here. CS sits between both functions and sees the customer lifecycle end to end, so you're well placed to run this analysis as a neutral party. Frame it to both VPs as "let's find out what share each of you is right about." That framing gets cooperation more easily than a verdict does.

## Turn 2

**User:** What if our data is too messy for this, like we never consistently tracked implementation milestones or adoption depth? Can we still run the diagnostic, or do we mostly have to rely on exit interviews?

**Assistant:**

Yes, you can still run it. Messy data changes *how* you do the diagnostic, not *whether*. And you probably have more usable data than you think; it's just scattered rather than tracked.

## Your advantage: small numbers

Regional carriers mean your churned-account count is likely in the dozens, not thousands. That makes a **hand-built, account-by-account reconstruction** feasible. At 1–2 hours per account, 40 churned accounts plus 20–30 retained ones for comparison is a few weeks of work for one or two people. You don't need a clean dataset. You need a case file per account.

## Reconstruct milestones and adoption from "exhaust" data

Even if nobody tracked implementation milestones, the implementation left traces:

**Implementation duration and difficulty**
- Contract and SOW signature dates
- Services billing records: when hours started, when they tapered off, overruns versus the original estimate
- Change orders and SOW amendments (a strong signal of trouble)
- Project tickets, Jira epics, or shared project plans
- Go-live emails, kickoff and cutover calendar invites
- License activation or production environment provisioning dates

**Adoption depth**
- **Claims volume processed through your system.** This is probably your single best proxy. Compare it to the carrier's actual claim volume, which you can estimate from public statutory filings or their own reports. A carrier running 20% of its claims through your platform never really adopted it.
- Active users versus licensed seats, from raw application or authentication logs even if nobody built a dashboard
- Which modules were configured and which integrations actually went live
- Whether they ever used the analytics or reporting features (this directly tests the "they didn't know we had it" scenario)

**Service experience**
- Support ticket counts, severity, escalations, and time to resolve. Ticketing systems are usually the one clean dataset you have.
- CSAT or NPS responses, even if sparse
- CRM notes, QBR decks, renewal-risk notes, and escalation emails

**What happened at churn**
- Where they went: competitor press releases and case studies, LinkedIn job posts mentioning the new system, conference talks
- M&A announcements, to quickly identify consolidation-driven churn

## Mine internal memory, carefully

Your CSMs, implementation leads, and account executives know a lot about each account, but they are not neutral. Implementation leads may blame the product and account executives may blame services. To get useful input:
- **Ask for facts before opinions.** Was it fully live? Which modules? Roughly when? Did they ever use reporting? Only then ask why they think it churned.
- **Use a simple coding rubric**, for example: go-live status (full / partial / never), adoption (high / medium / low), primary churn driver, and a confidence rating for each.
- **Have two people code each account independently** where possible, and look closely at disagreements.

## Exit interviews still matter, but know their limits

Interviews become more important when data is thin, but they have predictable biases:
- **Stated reasons are often the final trigger, not the root cause.** "Your competitor had better AI" may be the last straw after two years of frustration.
- **The person you reach may not be the decision-maker**, or may have joined after the painful implementation.
- **Politeness and rationalization.** Feature gaps are an easy, impersonal reason to give.

To counter these:
- Ask for a **chronological narrative**: "Walk me through from signing to the decision to leave. When did you first start looking at alternatives?"
- Interview **multiple roles** at the same carrier where possible: a claims operations user, IT, and the executive buyer often tell different stories.
- Use a **neutral interviewer**, ideally a third party.
- Ask open questions before any feature-specific ones.

## Triangulate rather than rely on one source

For each account, combine the reconstructed data, internal coding, and interview findings (where you have one). Where all three agree, you can be confident. Where they conflict, the conflict itself is informative. For example, "the customer cited AI features, but they only ran 15% of claims through us" suggests a service root cause beneath a product explanation.

## Precision you actually need

You don't need a precise answer. The decision is essentially how to split investment between two broad options, so you need to know whether the pattern is roughly 80/20, 50/50, or 20/80. Directional evidence from 40 well-reconstructed accounts is enough for that. Report findings with explicit confidence levels so neither VP can dismiss the work as either overclaiming or hand-waving.

## Fix the data going forward

Treat this as the moment to instrument a minimal set of metrics, so the next diagnosis is easier:
- Planned versus actual go-live date
- Time to first value, defined concretely, for example first claim processed in production
- Percentage of the carrier's claim volume running through your system
- Module and integration adoption
- Primary churn reason, coded consistently at every loss

Five fields tracked consistently will be worth more than an elaborate health score nobody maintains.

## Turn 3

**User:** How do I actually get churned customers to agree to an exit interview, especially the ones who left angry or left over a year ago, and should I offer them anything for their time?

**Assistant:**

You'll get more yeses than you expect if you make it clear this is genuinely about learning, not a disguised sales call. Many churned customers, including angry ones, want to be heard. The trick is making it safe, easy, and worth their time.

## Who should reach out

- **Someone senior who wasn't the day-to-day contact.** You, or your CEO for high-value or especially angry accounts. A senior ask signals you're taking it seriously.
- **Not a salesperson.** Anything that smells like a win-back attempt kills response rates and contaminates the answers.
- **Use warm relationships where they exist.** If a former CSM or implementation lead had good rapport, have them make the introduction, then hand off to the interviewer.
- **Consider a third-party research firm** for angry accounts or when you want maximum candor. People are more honest with someone who isn't from the company they left, and a firm can offer genuine anonymity.

## How to frame the ask

- **Lead with learning, and explicitly rule out selling.** "This isn't a sales call, and no one will follow up to try to win you back unless you ask."
- **Keep it short and specific.** Ask for 20–30 minutes by phone or video at their convenience. Don't ask for an hour.
- **Offer anonymity or confidentiality.** Say whether their name will be attached to feedback shared internally, and let them choose.
- **Tell them what you'll do with it.** "We're making decisions about where to invest over the next year, and your experience will directly shape them."

### Sample outreach

> Subject: 20 minutes of honest feedback?
>
> Hi [Name],
>
> I lead customer success at [Company]. I know [Carrier] moved off our platform [last year], and I'd value 20–30 minutes of your candid perspective on why, including what we got wrong.
>
> We're making major decisions right now about where to invest, and hearing directly from customers who left is the most useful input we can get. This isn't a sales call, and no one will contact you about coming back.
>
> Happy to work around your schedule, and I can keep your comments anonymous if you'd prefer. [Optional: As a thank-you, we'd like to make a donation to a charity of your choice.]
>
> Thanks for considering it,
> [Name]

Follow up once or twice over two to three weeks, by email and then by LinkedIn or phone. Stop after that.

## Customers who left angry

**Don't skip them.** They're often your most informative interviews, and excluding them biases your findings toward milder explanations.

- **Acknowledge it up front.** "I know your experience with us was frustrating, and I'd like to understand it properly." A brief, sincere acknowledgment often opens the door.
- **Have a senior person make the ask**, especially if the anger was about feeling ignored.
- **Don't defend or explain during the interview.** Listen, ask clarifying questions, and thank them. Correcting their account, even when it's inaccurate, ends the candor.
- **Check for open disputes first.** If there's active litigation, a billing dispute, or contract conflict, involve legal before reaching out, and consider skipping that account.

## Customers who left more than a year ago

- **Follow the people, not the account.** Your original contact may have moved to another carrier. They can still describe what happened, and they're a potential future buyer, which is another reason to keep it strictly non-sales.
- **Help their memory.** Share the reconstructed timeline from your data ("You signed in March 2022, went live in early 2023...") and ask them to correct and fill it in. Chronological prompts get far better recall than "Why did you leave?"
- **Interview whoever is there now** if the original contact is gone, but note that they may know only the ending of the story.

## Should you offer anything?

A modest thank-you helps, but it matters less than the framing, and insurance carriers often have strict corporate gift policies. Offer options:

- **A charitable donation in their name** ($100–$250). This is the safest default, since it avoids gift-policy problems and feels appropriate for executives.
- **A gift card or honorarium** of similar size, for those allowed to accept one. B2B research firms commonly pay executive honoraria in roughly the $150–$500 range for a 30–60 minute interview, so you're within norms.
- **A summary of what you learned** across all interviews, anonymized. Many industry peers value this more than money, and it signals you'll act on their input.

**Avoid offering discounts, credits, or return-customer pricing as the incentive.** It turns the conversation into a negotiation and signals the call is really about winning them back.

## Set realistic expectations

- Response rates vary widely. Expect a higher yes rate from customers who left on good terms or recently, and lower from angry or long-gone ones.
- **Reach out to roughly two to three times as many accounts as the interviews you need.** To land 10–15 interviews, contact 30–40.
- Track who declines. If angry or long-implementation customers decline at much higher rates, that pattern is itself a finding, and you should weight your data reconstruction more heavily for those accounts.

## Close the loop

Send a thank-you within a day. A few months later, send a short note about what you changed based on the interviews. It costs almost nothing, builds real goodwill in a small industry where carriers talk to each other, and occasionally reopens doors you didn't try to reopen.

## Turn 4

**User:** Once I'm actually in the interview, what questions should I ask, and how do I keep from leading them toward one VP's theory without meaning to?

**Assistant:**

The core principle: **let them tell the story before you ask about any specific cause.** Leading usually happens not in one bad question but in the order of questions and in which topics you probe more deeply. A structured guide, used consistently across every interview, is your main protection.

## Interview guide (about 30 minutes)

### 1. Opening (2–3 minutes)
- Thank them, restate that this isn't a sales call, and confirm confidentiality preferences.
- Ask permission to record, or to have a colleague take notes.
- Set the tone: "There are no wrong answers, and nothing you say will offend me. The more candid, the more useful."
- Confirm their role and how involved they were, from selection through the decision to leave.

### 2. The unprompted story (8–10 minutes)
This is the most important section. Ask one broad question and mostly listen.

- "Walk me through your experience with us, from when you first signed to when you decided to move on."

Then use only neutral follow-ups: "What happened next?" "Tell me more about that." "How did that affect things?"

Resist the urge to probe the topics you care about here. Note what they bring up on their own, because **unprompted mentions are your strongest evidence.**

### 3. The decision (5–7 minutes)
Separates the final trigger from the root cause.

- "When did you first start thinking about alternatives? What was going on at the time?"
- "Was there a specific moment or event that tipped the decision?"
- "Who was involved in the decision, and did people see it differently?"
- "If you had to name the single biggest reason, what would it be? What would come second?"

### 4. Balanced probes (8–10 minutes)
Now cover each area, **with the same depth and number of questions for each**, whether or not they raised it. Rotate the order across interviews so product doesn't always come first or last.

**Getting live and reaching value**
- "How did getting up and running compare to what you expected?"
- "At the point you left, how much of your claims work was running through our system?"

**Ongoing support and relationship**
- "When you needed help, what was that like?"
- "How did you feel about the attention you got from us over time?"

**Product capabilities**
- "How well did the product meet your needs once you were using it?"
- "What reporting or analytics did your team actually rely on day to day?"

**Alternatives**
- "What other options did you consider? What did they offer that stood out?"
- "How did you evaluate them?"

**Other factors**
- "Were there changes on your side, such as leadership, strategy, budget, or an acquisition, that played a role?"
- "How much did cost or pricing factor in?"

### 5. Counterfactual and close (3–5 minutes)
- "What would have had to be different for you to stay?"
- "If you were advising us on one thing to fix, what would it be?"
- "Is there anything I should have asked but didn't?"
- Thank them and confirm how you'll follow up.

If you want to test the "they didn't know we had it" scenario, do it **only at the very end**, after all open questions: "Were you aware we offered [specific capability]?" Asking earlier would plant the idea.

## Leading versus neutral wording

| Leading | Neutral |
|---|---|
| "Was the implementation too long?" | "How did getting up and running compare to what you expected?" |
| "Did our competitor have better AI features?" | "What did the other options offer that stood out?" |
| "Were you frustrated with support?" | "When you needed help, what was that like?" |
| "So it was mainly about features?" | "How would you summarize the main reasons?" |
| "Did you know we had analytics?" | "What reporting did your team rely on?" |

Watch for questions that embed an answer ("too long," "better," "frustrated") or offer only one explanation to agree with.

## Techniques to stay neutral during the conversation

- **Don't name either theory.** Never mention that people internally disagree about product versus services.
- **Use their words back to them.** If they say "it was a slog," ask "What made it a slog?" rather than "So the implementation was slow?"
- **Get specific examples.** "Can you give me an example?" helps distinguish real experiences from general impressions, and specific events are harder to shade.
- **Be comfortable with silence.** Pause for a few seconds after they finish. People often add the most important point after a pause.
- **Keep your reactions even.** Nodding enthusiastically when they mention features, and going quiet when they mention support, teaches them what you want to hear. Respond with the same neutral "That's helpful" to everything.
- **Don't summarize prematurely.** Summaries tend to compress toward what the interviewer expected. If you summarize, do it at the end and ask them to correct it.
- **Separate experience from interpretation.** "The competitor's AI was better" is interpretation. "Our adjusters were still building reports manually in spreadsheets" is experience. Probe for the experience underneath.

## Safeguards beyond the interview itself

- **Pilot the guide** on two or three interviews, then fix confusing or leading questions before continuing. Don't change it after that, so interviews stay comparable.
- **Record and transcribe** where permitted. Memory and notes drift toward what you expected.
- **Have someone else code the transcripts**, ideally without knowing which account's data showed poor implementation. Use the same rubric as your data reconstruction: primary driver, secondary driver, unprompted versus prompted mention, and confidence.
- **Weight unprompted mentions more heavily** than answers to direct probes.
- **Check your own lean.** Before starting, write down which theory you privately suspect. Then, when coding, look especially hard for evidence against it.
- **Share raw quotes with both VPs**, not just your conclusions. It builds trust in the findings and lets each of them see the evidence directly, which will matter when one of them doesn't like the result.

## Turn 5

**User:** What should we do?

**Assistant:**

Here's the plan in one place, plus my honest read.

## My lean, held loosely

If I had to bet before seeing your data, I'd expect **implementation and adoption to be the larger root cause, with product gaps often the stated trigger.** In claims software, long implementations and partial adoption are common, and customers who never reach full value are the ones most easily pulled away by a competitor's AI demo. But that is a prior, not a conclusion. The diagnostic exists precisely so neither I, you, nor either VP gets to decide this by instinct.

## The plan

### Weeks 0–2: Set up
- **Get CEO sponsorship** and position yourself as the neutral owner of the diagnostic.
- **Agree on the decision rule before seeing results.** With both VPs in the room, write down what evidence would shift investment toward product, toward services, or toward a split. Pre-committing prevents whoever loses from relitigating the method afterward.
- **Hold major roadmap changes** unless there's already clear evidence of a specific feature costing deals.
- **Triage at-risk renewals** for the next two quarters: low adoption, stalled implementations, or recent escalations get senior attention now.
- **Start tracking the five core fields** going forward: planned vs. actual go-live, time to first claim in production, share of claim volume on your platform, module and integration adoption, and coded churn reason.

### Weeks 1–6: Gather evidence
- Reconstruct case files for churned accounts plus a retained comparison group, using billing, tickets, logs, and CRM history.
- Run 10–15 exit interviews and 5–10 at-risk customer interviews with the neutral guide.
- Pull win/loss data from sales.
- Rule out consolidation, pricing, and cohort effects early, since these can quickly account for part of the churn.

### Weeks 6–8: Decide
- Attribute churned ARR to primary causes, with confidence levels.
- Present to the CEO and both VPs together, with raw quotes and account examples alongside the conclusions.
- Apply the pre-agreed decision rule and allocate investment roughly in proportion to the findings.

### After: Act and measure
- **Pilot fixes rather than launching everything at once.** For example, a fast-path implementation for new customers, or a targeted feature that multiple churned customers named.
- **Measure leading indicators.** Churn shows up at renewal, often a year or more later, so track time to value, adoption depth, and support escalations to know within months whether changes are working.
- **Give both VPs a shared retention metric** so the product-versus-services split stops being a turf question and becomes a joint problem.

## The one thing to get right

The most important step is the pre-agreed decision rule. The research will likely show a mix, and without prior agreement each VP will read the mix as confirming their view. With it, you turn a two-year argument into a decision you can make in about two months.

## Outcome summary (sent to Jev)

Neither belief can be declared right from argument alone. Instead, run a roughly two-month neutral diagnostic, owned by customer success with CEO sponsorship, to measure what share of churned ARR each cause explains. The assistant's prior, held loosely, is that implementation and adoption failures are the larger root cause, with product gaps often the stated trigger, because customers who never reach full value are easily pulled away by a competitor's AI demo.

Before looking at results, both VPs should agree in writing on what evidence would shift investment toward product, toward services, or toward a split. This is the single most important step, since the findings will likely be mixed and each VP would otherwise read them as confirmation.

Meanwhile:
- Hold major roadmap changes unless a specific feature is clearly costing deals.
- Triage at-risk renewals for the next two quarters.
- Push adoption of existing analytics.
- Start tracking five fields: planned versus actual go-live, time to first production claim, share of claim volume on the platform, module and integration adoption, and a coded churn reason.

The diagnostic has four parts:
- **Account reconstruction.** Build case files for churned and retained accounts from billing, tickets, logs, and CRM history. Messy data is workable because account counts are small.
- **Interviews.** Hold 10–15 exit interviews and 5–10 at-risk interviews using a neutral, open-first guide.
- **Win/loss data** from sales.
- **Early screening** for consolidation, pricing, and cohort effects.

Then attribute churned ARR to causes with confidence levels, and present raw quotes alongside conclusions. Allocate investment proportionally, pilot fixes such as fast-path implementation or specific cited features, and track leading indicators, because churn appears only at renewal. Finally, give both VPs a shared retention metric.
