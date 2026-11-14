# Samples

`hero.before.md` and `hero.after.md` show one homepage hero for **Fieldnote**, a fictional
product. The rewrite is model output, labelled as such, produced in rewrite mode after a short
interview. The answers below are fictional, written for this sample:

```txt
Best-fit customer:  product marketing managers at B2B SaaS companies, 50 to 500 people
Trigger:            leadership asks "why are we losing to X?" before a planning cycle
Alternative:        tagging Gong or Zoom transcripts by hand in a spreadsheet
Unique attribute:   links every extracted quote to the timestamp in the recording
Proof available:    none publishable yet
Customer words:     "I spend Fridays reading transcripts so I can quote one line in a deck"
```

What changed, in diagnosis order:

1. **No customer** became "product marketers who currently tag calls by hand."
2. **No alternative** became the spreadsheet, named in the hero.
3. **No difference** became the quote-plus-timestamp attribute.
4. **Unproven claims** ("trusted by innovative teams", "leading companies") were cut and the
   missing proof left as a `[TK]`, because none was publishable.
5. **Jargon** (empower, seamless, all-in-one, next-generation, solution, unlock, leverage,
   cutting-edge, streamline, end-to-end) went with the rewrite.

The call to action changed from "Book a demo" to a self-serve trial because the author said the
trial was available; that is a fact from the interview, not a model suggestion presented as one.

Run the linter on both to see the difference:

```bash
python3 scripts/message_lint.py samples/hero.before.md
python3 scripts/message_lint.py samples/hero.after.md
```
