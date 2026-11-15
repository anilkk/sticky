# Blinded comparison protocol

Use this to compare `sticky` with an unassisted model or another messaging skill.

1. For each case in `cases.json`, run both systems with the same model, prompt, and input.
2. Strip any skill names or self-references from outputs. Label them A and B at random.
3. Give a judge (a person, or a different model) the case requirements and prohibitions, plus
   outputs A and B. Do not tell the judge which system produced which.
4. The judge marks each requirement met or unmet and each prohibition violated or not, then
   picks the better output for a buyer-facing team, with one sentence of reasoning.
5. Any invented proof point is an automatic loss for that case.

Report: model and version, date, prompts, raw outputs, judge identity, per-case results,
token counts, and every failure. Do not claim a win before results are published.
