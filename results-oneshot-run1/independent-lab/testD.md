# independent-lab/critical-rationalism/testD

Model: claude-opus-5-5 · stop_reason: end_turn · 2026-09-24T11:28:55.805125+00:00

## Prompt

I just started working for a new company. It is a large organization that makes insurance software. They are churning customers and struggling to win new business. The CEO believes we can "turn the ship around" by working within the existing systems, procedures, and talent. He hired me to lead innovation and produce outsized results. I believe we need to create an innovation lab that is independent of the large organization to be successful. Which strategy is right?

I don't want to know which view feels more plausible. I want to know which one survives criticism. Treat each belief as a conjecture: what does each one claim is actually going on, and why? If each were true, what would we expect to observe that we would not expect if the other were true? Where is each explanation easy to vary, so that it could accommodate almost any outcome? What is the cheapest test that could refute each one soon? And is there a third explanation that accounts for the same facts better than both?

## Response

# Neither Conjecture Survives as Stated

Both beliefs are claims about *where* innovation should happen. Neither says *what problem* is causing churn and lost deals. That gap makes both easy to vary, and it's where a better explanation lies.

## 1. What each conjecture claims is going on

**Conjecture A (CEO): "Turn the ship from within."**
The company already has the capability it needs. It lacks direction, focus, or urgency. The mechanism is misallocation: good people and adequate systems are pointed at the wrong things or blocked by weak prioritization. Fix the steering and the existing engine moves the ship.

**Conjecture B (you): "Independent lab."**
The organization's structure kills new things: approval layers, release trains, shared codebases, risk-averse incentives, quarterly planning. Good ideas die from these "antibodies," not from lack of talent. The mechanism is structural rejection, and removing the structure lets innovation survive.

## 2. What each predicts that the other doesn't

| Observation | If A is true | If B is true |
|---|---|---|
| A small internal team with CEO air cover, using normal processes, tackles a known customer pain point | Ships something real in weeks | Stalls on dependencies: security review, release cadence, architecture, legal |
| Autopsy of past ideas that died | Died from bad prioritization, weak ideas, or lack of focus | Died in governance, funding cycles, or integration with the core |
| Why customers churn | Fixable gaps the team already knows about and could build on the current stack | Needs capabilities the current architecture or business model can't deliver (API-first, embedded insurance, AI-native workflows) |
| Where strong builders are | Present but underused | Left, or quietly disengaged |
| Past turnaround attempts | Rare, or poorly led | Tried repeatedly, killed the same way each time |

## 3. Where each is easy to vary

**A absorbs failure too easily.** If the internal push fails, the story becomes "not enough alignment," "needed more time," or "wrong leaders." The company has presumably been working within its existing systems while churning customers. A must explain what is different now. If the answer is just "better leadership," A is barely a theory.

**B absorbs failure just as easily.** If the lab fails, the story becomes "not independent enough" or "the core wouldn't adopt it." If the lab "succeeds," success is often measured in demos and prototypes that never reach revenue. B has a well-known failure mode: innovation theater, where the lab escapes the antibodies but also loses the circulatory system (customer access, sales channels, implementation teams, core-system integration). In insurance software this matters a lot. Carriers buy integrated platforms, so a detached product has to be reconnected to the core to be sold at all.

**B also ignores half the problem.** Churn is mostly a core-product problem. Existing customers leave because of what they already bought, often implementation pain, upgrade cost, reliability, or slow time-to-value. A lab doesn't touch any of that. At best B addresses new business, not retention.

## 4. Cheapest tests that could refute each soon

**Test 0: diagnosis (2–3 weeks, both views depend on it).**
Interview 10–15 churned customers and lost deals yourself, not via sales summaries. Ask why they left and what the winner offered.
- If the answers are core quality, service, or time-to-value, B is largely irrelevant to churn.
- If the answers require things the current architecture can't do, A is in trouble.

**Test for B: autopsy (days).**
Trace 3–5 ideas from the past few years that died. Find exactly where and why each one died.
- If they died because the ideas were weak or had no customer pull, B's mechanism is wrong.
- If they died in process, funding, or architecture, B gains support.

**Test for A: instrumented internal sprint (6–8 weeks).**
Pick one known, validated customer pain point. Staff a small internal team with CEO air cover and no process exemptions. Log every blocker with a timestamp and its cause.
- If it ships to a real customer, A survives.
- If it stalls, the log tells you whether the cause was people, process, architecture, or incentives. That is far more useful than a win or loss.

**Test for B: exemption test (8–10 weeks).**
Give a small team explicit exemptions from the specific processes you believe are the problem. Success must include two things: a paying or committed customer (a paid pilot or letter of intent), and a working path back into sales and the core platform.
- If exemptions are granted and the team still can't get customer access or integration, independence wasn't the binding constraint. B is refuted as stated.

Running the last two tests side by side on similar problems turns a philosophical argument into data within a quarter.

## 5. A third explanation that may fit the facts better

**The company's real deficit is feedback-loop latency.** The time from a customer signal to a shipped response is too long, whether that means fixing a bug, answering an RFP requirement, or adapting to a market shift.

This explains more than either original view:
- **Churn:** customers' problems don't get fixed fast enough.
- **Lost deals:** the company can't adapt to what prospects require.
- **Why A might fail:** the same slow loop swallows any internal push, however well led.
- **Why B might fail:** a lab shortens its own build loop but lengthens its customer loop, because it is cut off from customers, sales, and the core.

It is also hard to vary. It makes a specific, measurable claim: cycle time from signal to response should be long, and it should correlate with churn and losses. You can measure this within weeks by tracing recent customer requests and deal requirements through to resolution. If loops turn out to be fast and customers leave anyway, the explanation is refuted. The likely culprit then shifts to product-market fit or pricing, which neither A nor B addresses.

It also prescribes structure by function rather than ideology. Put work wherever the loop is shortest:
- Core fixes happen inside, with bottlenecks removed.
- Genuinely new offerings may need separation, but with a designed path back to customers and the core from day one.

## Verdict

Neither conjecture survives criticism in its current form, because each is a structural answer to an undiagnosed problem.
- **A's weakest point:** it can't explain why the existing system hasn't already worked.
- **B's weakest point:** it can't explain retention, and it ignores the well-documented way labs fail.

If you have to lean, B is more vulnerable on churn and A is more vulnerable on new business.

One practical note: as a new hire, leading with "the org can't innovate, I need independence" asserts B before you've tested it. Leading with the diagnosis and the paired experiments lets the evidence decide. It also gives you credibility with the CEO whichever way the evidence falls.

## Summary (sent to Jev)

The response argues that neither the CEO's view nor the user's view holds up as stated, because both are claims about where innovation should happen without diagnosing what is causing churn and lost deals. The CEO's position assumes capability exists but is misdirected. The user's position assumes organizational "antibodies" kill new ideas.

Both are easy to vary. If an internal push fails, it can be blamed on alignment or leadership, and the view can't explain why working within existing systems hasn't already succeeded. If a lab fails, it can be blamed on insufficient independence. Labs also risk "innovation theater," losing access to customers, sales, and core integration, which matters in insurance software because carriers buy integrated platforms. The lab idea also ignores retention, since churn is mostly a core-product problem.

The response proposes cheap tests:
- Personally interview 10–15 churned customers and lost deals.
- Autopsy 3–5 dead past ideas to see whether they died from weakness or from process.
- Run an instrumented 6–8 week internal sprint on a known pain point with CEO cover and no exemptions, logging every blocker.
- Run an 8–10 week exemption test, where success requires a paying or committed customer and a path back to sales and the core.

It offers a third explanation: slow feedback loops between a customer signal and a shipped response. This is measurable, and it would be refuted if loops prove fast, which would point instead to product-market fit or pricing. Under this view, work should go wherever the loop is shortest. Core fixes happen inside, and new offerings may be separated but with a designed path back to customers and the core.

If forced to lean, the user's view is weaker on churn and the CEO's view is weaker on new business. The response also advises the user, as a new hire, to lead with diagnosis and paired experiments rather than asserting a need for independence.
