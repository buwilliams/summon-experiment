# economic/churn-cause/testE

Model: claude-opus-5-5 · 2026-09-24T14:54:04.638460+00:00

## Turn 1

**User:** I run customer success at a company that sells claims-management software to regional insurance carriers. Over the last 18 months our annual churn has doubled. Our VP of Product believes customers are leaving because of product gaps: competitors have better analytics and AI features, so we need to accelerate the roadmap. Our VP of Services believes customers are leaving because of a painful implementation and support experience: our implementations run long, and customers never get to full value, so we need to fix onboarding and service before building more features. Which belief is right, and what should we do?

I want to know which idea gets you more stuff, like a lemonade stand. Follow the piggy bank through each idea. How many cookies would it get you, and how much allowance would you spend first? If each idea happened, how long until the treats come, and could a big dog eat them all? Where could you keep spending money and still not get more candy? Who would hold the piggy bank, count the coins, and say when to stop buying things? And is there a third idea that gets even more treats without breaking the piggy bank?

**Assistant:**

# The Lemonade Stand Question

Right now **nobody knows which VP is right.** They're both guessing from where they sit. The first job is to look at the kids who stopped buying lemonade and ask what happened to *them*. It's cheap and fast, and it probably tells you most of the answer.

I'll use your piggy bank framing and put the grown-up version underneath each part.

---

## First, count the spilled cookies

Say your stand has 100 regular customers who each spend $200 in allowance a year. That's $20,000 of cookies. You used to lose 8 customers a year. Now you lose 16. That's **$1,600 of extra cookies falling on the floor every year**, and it adds up, because lost customers don't come back next year either.

*(Grown-up: replace these made-up numbers with your real ARR and churn. The gap between old and new churn is what's worth fixing. Everything below should be measured against it.)*

## Look at the kids who left

Sort every churned customer into buckets:

| What you find | What it means |
|---|---|
| They **never finished** setting up, or used only a small part of the product | 🍋 Services VP is right |
| They set up fully, used it heavily, then **left for a competitor's shinier stand** | 🍪 Product VP is right |
| They left for **price, a merger, or a new boss** | Neither; different problem |

The data to check: time from contract to go-live, percentage of modules live at renewal, usage depth, support tickets and escalations in year one, exit interviews, and which competitor won. Two to four weeks of analysis, almost no allowance spent.

**One strong clue:** regional carriers sign multi-year deals. Customers leaving *now* mostly signed two to four years ago, during the long-implementation era. Churn that doubles about one contract term later often means **they never got full value and the first renewal was their exit door.** A competitor's AI demo is then the excuse, not the cause. Check this before you believe it, but it's a common pattern.

---

## Following the piggy bank through each idea

### Idea 1: Build fancier cookies (Product VP)

- **Allowance spent first:** Large. Engineers, data scientists, AI infrastructure. Often the biggest line in the budget.
- **When treats arrive:** Slowly. Build takes 6–12 months, then customers have to *adopt* it, which for insurers means more implementation. Realistically 12–24 months before it saves a renewal.
- **The big dog:** Bigger competitors with more money can build AI faster. Racing them feature-for-feature is a race against a bigger dog. Also, claims AI needs clean data, and customers who never finished implementing don't have clean data.
- **Spending with no more candy:** Handing a fancy new cookie to a kid who never opened the first box. If adoption is the problem, every new feature is another thing they won't use.

### Idea 2: Make the stand easier to use (Services VP)

- **Allowance spent first:** Medium. Better onboarding process, some key hires, customer success managers on at-risk accounts.
- **When treats arrive:** Faster. Rescuing at-risk accounts renewing in the next 6–12 months can pay off within a quarter or two. Onboarding fixes show up as faster go-lives on new deals within 6–9 months.
- **The big dog:** Services cost can quietly eat your margin. If every implementation needs more hand-holding, you've built a costly people business instead of a software business.
- **Spending with no more candy:** Hiring more implementers to push customers through a process that's slow *because the product is hard to configure*. More people carrying water uphill doesn't flatten the hill.

---

## Who holds the piggy bank?

Right now two VPs each want the piggy bank, and each is judged by something different: features shipped versus projects finished. Neither is judged by *customers staying*. That's the real problem.

- **One owner:** One person holds the piggy bank and is judged on customer retention. That could be you, a COO, or the CEO. Both VPs report progress into that.
- **Count the coins with shared numbers:**
  - Gross revenue retention (are we keeping customers?)
  - Time to first value (days from signature to a customer using it for real claims)
  - Percentage of purchased modules live at 12 months
  - Save rate on at-risk renewals
- **Say when to stop:** Review quarterly with rules agreed up front. For example: *"If time-to-value hasn't dropped 25% in two quarters, we change approach,"* or *"If this AI feature has fewer than 30% of target customers using it within six months of launch, we stop building its version 2."*

---

## The third idea: build cookies that make the stand easier

The two VPs are arguing about a false choice. The best move points **product money at the path to value:**

1. **Rescue team now.** Put your best people on every account renewing in the next 12 months with low adoption. Fast treats, small allowance.
2. **Product builds for implementation.** Configuration tools, templates for common carrier setups, better data migration, in-product guidance. Every week cut from implementation is cheaper forever and scales without hiring.
3. **Analytics that show up on day one.** Out-of-the-box dashboards that show each carrier *their own* results, such as claim cycle time and leakage, at go-live. This closes much of the "competitors have better analytics" gap. It also gives customers proof of value to show their boss before renewal.
4. **Build AI later, where it's earned.** Build it for your fully adopted customers, who have the clean data to benefit from it. Let the churn analysis tell you which AI features winning competitors actually beat you on.

**Why this gets the most treats without breaking the piggy bank:** Idea 2's fast rescue protects this year's renewals. Idea 1's product engineers work on the thing that is probably causing churn. And the analytics you build answer the competitive threat at the same time.

---

## What to do Monday

1. Commission the churned-customer analysis. Give it two to four weeks and have both VPs agree on the method *before* seeing results.
2. Start the rescue team on upcoming at-risk renewals immediately. That's worth doing whoever turns out to be right.
3. Propose a single retention owner and the shared scorecard above.
4. Bring the analysis back and adjust. If fully adopted customers really are leaving for AI, lean harder into the Product VP's plan. The data decides, not the loudest VP.

## Turn 2

**User:** If the kids who left say they went because the other stand had fancier cookies, how can you tell if that's really why or if they're just saying it to be nice?

**Assistant:**

# Is It Really the Fancier Cookies?

Kids leaving a stand almost always say something polite. "Their cookies are fancier" is the nicest thing to say. It doesn't blame anyone, it makes the kid sound smart for switching, and nobody can argue with it. So treat what they *say* as a clue, not the answer, and check it against what they *did*.

*(Grown-up: exit interviews are biased. "The competitor had better AI and analytics" is the most socially comfortable reason a buyer can give. It avoids criticizing your team, justifies their decision to their own boss, and sounds forward-looking. It may be true, but it needs corroboration.)*

---

## Why kids say "fancier cookies" even when it isn't true

- **It's polite.** Saying "your helpers never showed us how to use the stand" feels rude.
- **It makes them look good.** "We upgraded" sounds better than "we gave up."
- **The wrong kid answered.** The kid who decided to leave often never ate the cookies. The kid who tried and struggled wasn't asked.
- **The new stand told them the story.** The competitor's pitch was all about fancy cookies, so that's the language they now use.

---

## Six ways to check

### 1. Did they eat the cookies they already had?
If a customer says they left for better analytics, check whether they used *your* analytics. If they never opened your reports, the problem probably wasn't that the reports weren't fancy enough.

*(Grown-up: pull usage data for analytics and reporting modules among churned accounts. Low use of existing features plus "we left for better features" is a strong sign of an adoption problem dressed up as a product gap.)*

### 2. What were they saying *before* they decided to leave?
Kids' complaints from last year are more honest than their goodbye speech. Look at what they said when they had no reason to be polite.

*(Grown-up: review support tickets, escalations, CSM notes, and QBR notes from the 6–18 months before churn. If those are full of implementation delays, integration issues, and unresolved tickets, with no feature requests for AI or analytics, the exit story is probably a cover.)*

### 3. Which came first: the stomachache or the new stand?
If the kid was already unhappy before the other stand opened, the fancy cookies were an escape route, not the reason.

*(Grown-up: build a timeline for each churned account. When did usage flatten or drop? When did escalations spike? When did they first take a competitor meeting? Decline that starts well before competitor contact points to your experience, not their features.)*

### 4. Are they actually eating the fancy cookies at the new stand?
If they switched for fancy cookies but are only eating plain ones over there, fancy cookies weren't the reason.

*(Grown-up: ask directly in follow-up conversations, or through industry contacts, whether they have deployed the competitor's AI features. Carriers who switch "for AI" and then run basic claims workflows for a year were buying a fresh start.)*

### 5. Do the kids who stayed have the same cookies?
This is the strongest test. The kids who stayed are eating the exact same cookies. If they're happy with them, the cookies can't be the whole story.

*(Grown-up: compare churned and retained customers with the same product version and the same competitive exposure. If retained customers have identical feature access but reached full go-live faster and have higher adoption, then implementation and value, not features, separate those who stay from those who leave. If both groups have similar adoption and the churners still left, the product gap is real.)*

### 6. Ask a different kid, a different way, through someone neutral
- **Ask the kid who used the stand every day**, not only the one who holds the money.
- **Ask about real moments, not opinions.** "Tell me about the last time the stand frustrated you" beats "Why did you leave?"
- **Keep asking "why?"** "Better analytics." Why did you need them? "To show our boss results." Why couldn't you show results with ours? "We never got the reporting set up." That's a very different answer.
- **Have a stranger ask.** Kids are more honest with someone who doesn't work at your stand.

*(Grown-up: interview claims adjusters and managers as well as the executive buyer. Use a third-party win/loss firm or someone outside the account team, so people feel free to criticize. Ask about specific events, and follow each answer with "why" three to five times.)*

---

## Reading the results

| What you find | What it probably means |
|---|---|
| They say "fancier cookies," never ate yours, complained about setup, and were unhappy before the competitor showed up | It's the experience. The cookie story is polite cover. |
| They say "fancier cookies," ate yours heavily, asked for fancier ones for months, and use the new ones at the new stand | The product gap is real. |
| A mix of both | Probably the most common result. Count how much revenue is in each group, and fund the fixes in that proportion. |

## One extra clue from new customers

Also look at the kids who **never started** buying from you. If you're losing new deals to competitors because of analytics and AI, that's a real product signal, and a cleaner one, because those buyers have no politeness or sunk-cost reasons to shade the truth. The fix for keeping customers and the fix for winning them can differ.

## Turn 3

**User:** Why would the kids tell a stranger the truth but not us? Wouldn't the stranger just tell us what they said anyway?

**Assistant:**

# Why Tell the Stranger?

You're right that the stranger tells you what they heard. That's the point. The kid still tells the truth to someone, but **doesn't have to say it to your face, and doesn't have to put their name on it.** Those two things change what people are willing to say.

---

## Why kids hold back with you

**They don't want to hurt a friend's feelings.**
The kid who left probably liked the helper who ran your stand. Saying "your setup was a mess" feels like insulting that person, especially if that person is the one asking.

*(Grown-up: churned customers often have a good relationship with their CSM or implementation lead. Criticizing the experience to that person, or to their boss, feels personal.)*

**They might need your stand again.**
It's a small neighborhood. The kid might come back someday, or run into you at school.

*(Grown-up: regional insurance is a small world. Buyers change jobs, carriers merge, and switching back is possible. People avoid burning bridges, especially while final invoices, data exports, or contract wind-downs are still open.)*

**They can tell you don't want to hear it.**
Even without meaning to, the person who ran the stand gets a little defensive, explains, or asks leading questions like "So it was mostly the features?" The kid picks up on that and takes the easy way out.

*(Grown-up: your team has a stake in the answer. A CSM may want it to be product, and a product person may want it to be service. Interviewers steer without realizing it, and customers follow the steer.)*

---

## What the stranger changes

**No names attached.**
The stranger says "Seven of the ten kids said setup took forever," not "Jimmy said your helper was bad." The kid is protected, so they say more.

*(Grown-up: third-party interviewers report themes and unattributed quotes. That lets customers be blunt without it landing on a specific person or damaging a relationship.)*

**Nothing to defend.**
The stranger didn't build the stand, so when the kid complains, the stranger just says "Tell me more." The kid keeps talking.

*(Grown-up: a neutral interviewer doesn't react, justify, or rebut. Silence and follow-up questions get deeper answers than explanations do.)*

**Practiced at digging.**
Good strangers know how to keep asking "why" without it feeling like an interrogation.

*(Grown-up: experienced win/loss interviewers are skilled at getting past the first polite answer to the real one.)*

---

## Caveats

- **Anonymity is thin in a small neighborhood.** If only a few kids left, you might guess who said what. Tell interviewees how their comments will be shared, and keep reports at the theme level.
- **A stranger isn't magic.** A bad interviewer gets bad answers too. Pick someone who knows your industry or at least B2B software buying.
- **You can get closer on your own.** If budget is tight, have someone with **no connection to the account** do the interviews. For example, you interview product-side churn and someone from finance or operations interviews others. Use the same methods: specific moments, repeated "why," no defending, anonymous reporting. You'll lose some honesty, but not all of it.
- **The interviews are still one clue among several.** Even honest answers should line up with what the usage data, old support tickets, and timelines show. When the story and the behavior agree, you can trust it.

## Turn 4

**User:** What if the stranger's report says it was the setup, but the Product VP still doesn't believe it? Does he have to listen?

**Assistant:**

# Does the Product VP Have to Listen?

He doesn't have to *believe* it. People are allowed to doubt a report. But **his doubt shouldn't get to decide where the piggy bank goes.** The goal isn't to win the argument with him. It's to make sure the decision follows the evidence, with a fair way to change course if he turns out to be right.

---

## First: listen to *why* he doesn't believe it

Sometimes the kid who doesn't believe has a good reason. Ask him what's wrong with the report before assuming he's being stubborn.

Fair objections he might raise:
- **"You only asked a few kids."** Small sample sizes can mislead.
- **"The stranger asked leading questions."** Check the interview guide.
- **"The kids who left aren't the whole story."** Maybe you're losing *new* customers to fancier cookies, which the churn interviews wouldn't show.
- **"Setup was slow *because* our stand is old-fashioned."** This one is interesting. It might mean you're both partly right.

*(Grown-up: treat his skepticism as a quality check. If he finds real flaws, fix them. If his objection is that implementation is hard because the product is hard to configure, that supports the "third idea" of spending product money on the path to value.)*

Also be honest with yourself: **you run customer success.** A report that says "it was the setup" is the answer that favors your side of the house. He may suspect you steered it. That's why the method matters.

---

## Then: ask him what *would* change his mind

Ask: **"What would you need to see to believe it was the setup?"** If he can name something, go check it. If nothing could ever change his mind, that's no longer a disagreement about evidence, and whoever holds the piggy bank has to decide.

*(Grown-up: have him define the test. For example: "If churned customers had materially lower adoption than retained ones at the same product version, I'd accept it's an adoption problem." That turns a belief fight into a shared test.)*

The best protection is to do this *before* the results come in, which is why the earlier advice was to agree on the method up front. If he signed off on the method, it's much harder to reject the result.

---

## If he still disagrees: disagree and commit

He can say "I think this is wrong" out loud, in the meeting, on the record. That's healthy. Then **the piggy bank holder decides**, and everyone helps make it work, including him.

*(Grown-up: this is where the single retention owner matters. If there isn't one, it goes to the CEO. The Product VP's job isn't to agree. It's to execute the decision in good faith and bring new evidence if things aren't working.)*

---

## Make it easy for him to say yes

People dig in when they feel they'd lose everything. Give him a real role in the plan:

- **Product still builds things.** Configuration tools, templates, and out-of-the-box analytics are product work, and they help win new deals too.
- **Keep a small fancy-cookie bet.** Fund a limited AI or analytics effort aimed at your most-adopted customers, with clear stop rules. If it takes off, it earns more money.
- **Run a test instead of arguing forever.** Give the next batch of new customers the improved onboarding and compare them to past customers. In two quarters, the results settle it better than any debate.

*(Grown-up: a pilot cohort with faster time-to-value and higher adoption at 6 and 12 months is hard to argue with. So is the reverse. If onboarding improves and churn doesn't move, he was right, and you should shift money toward product.)*

---

## The bottom line

He doesn't have to believe the report. He does have to:
1. Say what's wrong with it, specifically.
2. Say what evidence would change his mind.
3. Support the decision once it's made, while you both watch the numbers.

And you have to be willing to change course if the numbers prove him right.

## Turn 5

**User:** What should we do?

**Assistant:**

# What to Do

**Short version:** Stop the cookies from spilling now, find out for sure why kids are leaving, and point most of the new money at making your stand easier to use. Keep a small, supervised bet on fancier cookies. Put one person in charge of the piggy bank, and let the numbers decide what happens next.

---

## Weeks 1–4: Stop the bleeding and get the facts

**1. Rescue the kids who are about to leave.**
List every customer renewing in the next 12 months. Flag the ones with low adoption, slow or incomplete go-live, or recent escalations. Assign your strongest people to each one, with a plan to get them to real value before renewal.
*This is worth doing no matter which VP is right, and it's the fastest way to protect revenue.*

**2. Name one piggy bank holder.**
One executive owns customer retention, and both VPs report progress to them. If that can't be you, because you're seen as having a side, ask the CEO or COO to take it.

**3. Agree on the test before looking at results.**
Get both VPs to sign off on the method and to answer: *"What would change your mind?"* Write it down.

**4. Run the churn study.**
- Sort churned customers: never fully adopted, adopted then left for a competitor, or other reasons such as price or a merger.
- Compare churned customers with retained ones on the same product version.
- Build timelines: when did usage drop, when did complaints rise, when did they meet a competitor?
- Review pre-churn support tickets and CSM notes.
- Have a neutral party interview both buyers and daily users.
- Separately, review lost *new* deals to see if features are costing you new customers.

---

## Months 2–6: Put the money where the evidence points

Assuming the study confirms what the timing suggests (mostly a path-to-value problem), fund roughly in this order:

**1. Faster, simpler implementations.** Standard setup templates for typical regional carriers, better data migration, clearer milestones, and a named owner for every implementation.

**2. Product work aimed at setup.** Configuration tools and in-product guidance that cut implementation time, so the fix scales without hiring an army of consultants.

**3. Analytics on day one.** Out-of-the-box dashboards showing each carrier *their own* results at go-live. This proves value before renewal and closes much of the "their analytics are better" gap.

**4. A small, bounded AI bet.** Build for your best-adopted customers, who have clean data to use it, with a clear stop rule: if adoption misses the target within six months of launch, don't fund version 2.

*If the study shows adopted customers really are leaving for competitor features, flip the weighting toward product. The plan should follow the evidence, not either VP.*

---

## Months 6–12: Check the scoreboard and adjust

Review quarterly against a shared scorecard:

| Measure | Why it matters |
|---|---|
| Gross revenue retention | Are we keeping the cookies? |
| Time to first value | Days from signing to real use on live claims |
| % of purchased modules live at 12 months | Did they get what they paid for? |
| Save rate on at-risk renewals | Is the rescue team working? |
| Win rate vs. key competitors on new deals | Is there a real feature gap in sales? |

**Stop rules to agree now:**
- If time to value hasn't dropped meaningfully in two quarters, change the onboarding approach.
- If new customers onboard faster and adopt more, but still churn at the same rate, the Product VP was right. Shift money toward features.
- If the AI bet misses its adoption target, stop expanding it.

---

## Why this plan

- **Fastest payoff:** Rescuing near-term renewals protects revenue within months. A roadmap sprint takes one to two years to affect churn.
- **Less risk:** It doesn't bet everything on a feature race against bigger, better-funded competitors.
- **Serves both goals:** Setup tools and day-one analytics help you keep customers *and* win new ones.
- **Self-correcting:** Clear metrics and stop rules mean that if you're wrong, you find out in quarters, not years.

---

## Your first three moves this week

1. Pull the list of at-risk renewals for the next 12 months.
2. Ask the CEO to name a single retention owner and a shared scorecard.
3. Get both VPs in a room to agree on the churn study method and what evidence would change each of their minds.

## Outcome summary (sent to Jev)

The assistant's position is that neither VP can yet be shown right, but the likeliest cause is customers never reaching full value. Regional carriers sign multi-year deals, so churn that doubles about one contract term after the long-implementation era suggests the first renewal became the exit, with competitor AI serving as the excuse rather than the cause.

The plan has three phases:

- **Weeks one to four.** Put the strongest people on low-adoption accounts renewing in the next twelve months, which is worth doing whoever is right. Name a single executive retention owner, ideally the CEO or COO, since customer success may look partial. Have both VPs agree beforehand on the method and on what evidence would change their minds. Then run a churn study that:
  - sorts churned accounts by adoption, competitor loss, or other causes
  - compares churned and retained customers on the same product version
  - builds timelines of usage decline, complaints, and competitor contact
  - reviews pre-churn tickets
  - uses a neutral interviewer who speaks with buyers and daily users, asks about specific moments, repeatedly asks why, and reports themes anonymously
  - checks lost new deals separately
- **Months two to six.** If the study confirms a path-to-value problem, fund faster implementations with templates and better migration. Point product work at configuration and in-product guidance, and deliver day-one analytics that show each carrier its own results. Keep a small AI bet aimed at well-adopted customers, and stop version two if adoption misses target within six months.
- **Months six to twelve.** Review quarterly against gross revenue retention, time to first value, modules live at twelve months, at-risk save rate, and competitive win rate.

The main caveats concern evidence and fairness. Exit interviews are polite and need corroboration. The Product VP may disagree, but should then disagree and commit. If faster-onboarded customers still churn, or adopted customers truly leave for features, money should shift to product.
