# Sticky

Good product messaging is something a buyer can say back to you, in their own words, to
someone who was not in the room.

`sticky` is also an Agent Skill that applies the rules below when you build, rewrite, or
review product marketing messaging with a coding agent: value propositions, homepage heroes,
one-liners, launch posts, sales narratives, and battlecards. To install it:

##### NPM

```bash
npx skills add anilkk/sticky
```

##### pnpm

```bash
pnpm dlx skills add anilkk/sticky
```

Then pick a mode:

```txt
/sticky interview <product>   it interviews you, then builds the messaging doc from your answers
/sticky rewrite hero.md       it rewrites messaging you already have
/sticky review homepage.md    it critiques and leaves your file alone
```

The site has the rules, a worked example, and the install steps:
[anilkumark.de/sticky](https://www.anilkumark.de/sticky).

## Why the name

Sticky messaging is the kind a buyer remembers after the call and repeats to their boss. It
sticks because it was built from words customers already use, and because it says one clear,
provable thing. Everything in this repository serves those two ends. The name also nods to
Chip and Dan Heath's *Made to Stick*.

Most messaging fails before a word of copy is written. A team picks adjectives in a workshop,
ships "the AI-powered platform for modern teams," and wonders why sales reps improvise their own
pitch on every call. The copy was fine. It was just never true for anyone in particular.

So the first work is not on the page. It is finding the customer who loves you most, learning
what they would do if you vanished, and writing down the words they used to explain why they
stayed.

> Messaging is clear, different, and believable, and a buyer can repeat it.

What follows are sixteen rules, each tied to the book or framework it comes from.

---

## Clear

### 1. Name the customer before the product

Pick the customer who gets the most value fastest and would be upset if you disappeared. Write
for them. Messaging aimed at "developers, data teams, and enterprises" is aimed at nobody, and
every sentence gets softer to avoid offending one of the three.

*From Emma Stratton's A+ customer and April Dunford's best-fit customer.*

### 2. Start from what they would do without you

The buyer is always comparing you with something: a spreadsheet, an intern, an open-source
script, a competitor, or doing nothing. Name that alternative first. Your value only exists in
the gap between you and it.

*From April Dunford, Obviously Awesome: competitive alternatives come before features.*

### 3. Say what it is in words the buyer already uses

If a visitor cannot tell what category you are in within five seconds, nothing else on the page
matters. Use the category the buyer would type into a search box, then explain how you are
different inside it. Inventing a category is a strategy with a budget, not a copywriting choice.

*From Fletch PMM's "clarity before differentiation" and Dunford's frame of reference.*

### 4. One value proposition, then three benefits

A message has one main promise and a few supporting reasons to believe it. Write one value
proposition, three benefits that hold it up, and the features that prove each benefit. If you
have seven benefits, you have not decided yet.

*From Emma Stratton, Make It Punchy: the Value, Benefit, Feature (VBF) structure.*

### 5. Use the words people say out loud

Would a buyer say this sentence to a friend at a barbecue? "Leverage," "seamless,"
"best-in-class," and "unlock" fail. A precise technical term your buyer uses daily, like
"residential proxy" or "SOC 2," passes. Jargon is a word your reader would not use, not a word
that sounds technical.

*From Emma Stratton's BBQ test and jargon blacklist.*

---

## Different

### 6. Lead with what only you can claim

Read your headline with a competitor's logo next to it. If it still works, it is not
differentiation. List the attributes you have and alternatives lack, then lead with the one
your best customers care about most.

*From April Dunford: unique attributes, then the value they enable.*

### 7. Have a point of view about the market

A message without an opinion is a feature list with a logo. Say what has changed in the world,
what the old way gets wrong, and what you believe instead. The opinion must be one that a
reasonable competitor would disagree with.

*From Alex James, Message Matters Most (the umbrella opinion), and Stratton's
Shift, Villain, Dream, Solution story.*

### 8. Match the buyer's awareness

A buyer who does not know they have the problem needs the problem named. A buyer comparing three
vendors needs the difference. The same headline cannot serve both, so pick the stage your best
customer is in when they meet this page.

*From Eugene Schwartz, Breakthrough Advertising, as applied by Alex James.*

### 9. Translate every feature into a before and after

"Automatic retries" is a feature. "Your scraper keeps running when the site changes its layout
at 2 a.m." is the after. Describe the before, what it costs, and what changes, then let the
feature be the reason it is true.

*From Force Management, Command of the Message: before scenarios, negative consequences, and
positive business outcomes.*

---

## Believable

### 10. Prove each claim or cut it

Every claim needs a proof point beside it: a number, a named customer, a benchmark you can
link, or a demo. "Fast" is a claim. "Median response in 1.2 seconds across 40 million requests
last month" is proof. If you have no proof, say less.

*From Command of the Message's proof points.*

### 11. Borrow the customer's words

The strongest lines in most messaging documents were said by a customer first. Pull them from
sales calls, support tickets, churn interviews, and reviews. Quote them exactly; do not tidy
them into your brand voice.

*From Dunford's evidence gate and Rob Fitzpatrick's The Mom Test.*

### 12. Name the outcome for each person in the deal

The engineer wants fewer pages at night. Their manager wants the roadmap to ship. The CFO wants
one fewer vendor. One benefit, translated three ways, beats three unrelated benefits.

*From Fletch PMM's stakeholder outcome translation and Command of the Message.*

### 13. Be specific enough to be wrong

"Trusted by leading companies" cannot be checked, so nobody believes it. "Used by 3 of the top
5 US retailers to track prices daily" can be checked, so it persuades. Vague claims are safe
because they say nothing.

*Adapted from Addy Osmani's [clarity](https://github.com/addyosmani/clarity), rule 6.*

---

## Making it

### 14. Pass the retell test

After a call or a demo, ask the buyer to explain the product to their boss. Write down what
they say. If it does not resemble your value proposition, the message did not land, however
good it reads in the doc.

### 15. Test it in a live call, not in a doc

Messaging is a claim about what will happen in a buyer's head. Run it in five sales calls,
listen to the recordings, and keep what made the buyer lean in. A messaging doc nobody has said
out loud is a draft.

*From April Dunford, Sales Pitch.*

### 16. Keep messaging upstream of copy

Positioning decides who you are for and why you win. Messaging turns that into a few sentences.
Copy adapts those sentences to a headline, an email, or a slide. When copy keeps changing,
the fix is usually one level up.

*From Emma Stratton: positioning, then messaging, then copywriting.*

---

## The skill in this repository

The skill asks for evidence before it writes copy, treats customer verbatims as source material,
refuses to invent proof points, and judges messaging by whether a buyer could repeat it.

```txt
SKILL.md                      the operating manual
commands/                     optional /sticky-interview, -rewrite, -review wrappers
references/interview.md       the positioning interview: customer, alternatives, proof
references/frameworks.md      the books and frameworks, and when each one applies
references/edit.md            messaging diagnoses and fidelity safeguards
references/review.md          review format and verdicts
references/surfaces.md        what a hero, one-liner, deck, launch post, and battlecard each owe
assets/messaging-doc.md       the messaging doc template the interview fills in
evals/cases.json              behavioral cases: invented proof, medium fit, false positives
evals/JUDGE.md                blinded comparison protocol
scripts/message_lint.py       jargon, unproven superlatives, we/you balance; no score by design
scripts/validate_package.py   package, routing, and eval validation
samples/                      one homepage hero before and after, labelled as a model rewrite
```

### What each mode does

**`/sticky interview <product>`** asks before it writes. It wants the customer who loves you,
the alternative they replaced, three moments where the product mattered, and the exact words
customers used. Then it fills in the messaging doc: one value proposition, three benefits,
features as proof, and a four-paragraph story. Wherever it needs a fact only you have, it leaves
a marked gap:

```txt
[TK: which customer said "we stopped babysitting scrapers"? Name and role.]
```

**`/sticky rewrite hero.md`** diagnoses the largest problem first, in this order: wrong
customer, missing alternative, no difference, unproven claim, jargon. It rewrites only as much
as the request allows.

**`/sticky review homepage.md`** leads with a piece-level verdict, then marks each line
`keep`, `revise`, `ask-customer`, or `cut`. `ask-customer` means the line could be fixed, but
the fix needs evidence that only your customers can supply.

### Linting

```bash
python3 scripts/message_lint.py hero.md
```

It lists jargon, superlatives without nearby proof, and the balance of "we" against "you". It
refuses to produce a score. Read it as a map of where to look.

---

## Further reading

- *Obviously Awesome* and *Sales Pitch*, April Dunford.
- *Make It Punchy*, Emma Stratton.
- *Message Matters Most*, Alex James.
- *Breakthrough Advertising*, Eugene Schwartz.
- *The Mom Test*, Rob Fitzpatrick.
- *Command of the Message*, Force Management.
- [Fletch PMM](https://www.fletchpmm.com/), Anthony Pierri and Robert Kaminski.
- [clarity](https://github.com/addyosmani/clarity), Addy Osmani, whose structure this repository
  borrows.

MIT. By [Anil Kumar Krishnashetty](https://www.anilkumark.de).
