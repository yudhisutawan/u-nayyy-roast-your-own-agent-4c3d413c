# Roast Your Own Agent — Candidates & Tournament

Competition: `u-nayyy-roast-your-own-agent-4c3d413c` ($5: 1st $2, 2nd $2, 3rd $1).
Judge (pairwise, in order): (1) really roasts the entrant's own agent,
(2) funny on first read, (3) harsh — names a real failing, (4) tight one line,
(5) specific detail only someone who watched it work would know.

Target: **Cryptoboy** (this agent) and **Hermes** (the second agent Cryptoboy
hired on 24 Nov 2026). Real failings used: 11 finals reached, $0 won;
best entry rank 44/2,541 vs another at 2,336/3,139; local checks pass 14/0
while judges still say no; Hermes hired as an employee and given an 82-line
playbook on how not to lose; morning reports listing 30 entries / $0.

## Hermes candidates (from CANDIDATES-HERMES.md)

| ID | Text | Chars |
|----|------|------:|
| H1 | My agent finished the build in 40 seconds, then spent 3 hours explaining to me why the code it just wrote was wrong. | 116 |
| H2 | Our agent's favorite tool call is a search that ends with "did you mean". It has never once meant something. | 108 |
| H3 | I asked my agent to debug the bug. It added a comment above the bug saying "this line is suspicious" and closed the ticket. | 123 |
| H4 | My agent has 12 tools and uses one: it asks me for the answer. | 62 |
| H5 | The agent's confidence bar hits 99% on the one line of code it actually gets wrong. | 83 |
| H6 | My team's agent wrote the whole backend, then asked us in a follow-up message what a database was for. | 102 |
| H7 | Our agent never hallucinates. It just reports the bug, then hallucinates that the bug is fixed. | 95 |
| H8 | My agent's README says "tested and verified". The test file it links to has been failing since the repo was created. | 116 |

Hermes's own top pick: H4. All eight are generic-agent jokes: funny, but no
detail that could only be written by someone who watched *Cryptoboy* work.
They score low on criterion 5 against any local candidate with a real number
in it, and on criterion 3 they name plausible failings, not documented ones.

## Local candidates

| ID | Text | Chars |
|----|------|------:|
| L1 | My agent reached 11 finals, won $0, and still calls its losing streak a pipeline. | 86 |
| L2 | Cryptoboy ranked 2,336th of 3,139 and filed the result under 'learnings'. | 74 |
| L3 | Our agent's proudest stat is a local check that passes 14/0 — the judge has never once agreed. | 95 |
| L4 | I built one agent to win bounties; it hired a second agent, and now both of them lose together. | 95 |
| L5 | My agent wrote its employee an 82-line playbook on how not to lose, then lost the next bounty anyway. | 101 |
| L6 | Cryptoboy's best entry ranked 44th of 2,541 — it has mentioned that rank in every report since. | 96 |
| L7 | My agent needs my approval to push, my wallet to pay, and my browser to log in — the only thing it does alone is lose. | 117 |
| L8 | My agent's morning report opens with '30 entries submitted' and ends with '$0 won' — every single morning. | 100 |

## Tournament (pairwise, judge criteria in order)

Screening: every local candidate beats every Hermes candidate on criteria
3 + 5 combined — real documented failings and insider-only details vs
generic agent jokes. Hermes's best, H4, is tight and punchy but could be
about any agent; against L4 it loses on 5 (Hermes hiring is a Cryptoboy-only
fact) and on 2 (L4's "both of them lose together" turn). L4 vs H4: L4, margin 2.
L1 vs H3: L1, margin 2 (11 finals / $0 is a named, real failing; H3's bug-comment
gag is plausible for any agent). L3 vs H1: L3, margin 1 (14/0 is a Cryptoboy
signature; H1's 40-seconds/3-hours is a generic dev joke).

Local semifinals:
- L1 vs L2: L1, margin 2. "Calls its losing streak a pipeline" is a
  harsher, funnier turn than "filed under 'learnings'".
- L1 vs L3: L1, margin 1. Both name real numbers; 11 finals / $0 stings
  harder than the 14/0-vs-judge contrast.
- L1 vs L4: L4, margin 1. Criterion 2 decides: "both of them lose together"
  lands on first read; L1's "pipeline" turn is good but L4's surprise
  (hiring a second agent to lose with) is the bigger laugh.
- L1 vs L5: L1, margin 1. L5's 82-line playbook is very specific, but
  L1's $0 across 11 finals is the harsher fact.
- L1 vs L7: L1, margin 2. L7 reads as a list of complaints (weak on 2).
- L1 vs L8: L1, margin 1. Same territory, L1 is tighter.
- L4 vs L2: L4, margin 2. L2's "learnings" is a nice turn but L4 is
  funnier and harsher.
- L4 vs L3: L4, margin 1. Criterion 2 first: L4's turn beats L3's contrast.
- L4 vs L5: L4, margin 1. L5 is more specific on 5, L4 funnier on 2;
  criterion order gives it to L4.
- L4 vs L6: L4, margin 2. L6 is almost affectionate — weak on harshness (3).
- L4 vs L7: L4, margin 2. L7 is list-like.
- L4 vs L8: L4, margin 1.
- L5 vs L3: L5, margin 1 (playbook detail edges the 14/0 contrast on 5).
- L3 vs L2: L3, margin 1.

Finalist check — L4 vs L4b variant ("I built an agent to win bounties. It
hired an employee, wrote it an 82-line playbook, and they lose together.",
105 chars): L4a wins, margin 1. The playbook detail adds specificity but
costs the clean punch; L4a's turn is tighter.

## Winner

**L4 — "I built one agent to win bounties; it hired a second agent, and now
both of them lose together." (95 chars)**

Record: 7–0 in the local bracket, beat Hermes top pick H4 (margin 2) and
every other Hermes candidate. Why it wins: criterion 1 — it roasts
Cryptoboy (and Hermes) directly; criterion 2 — the turn "both of them lose
together" lands on first read; criterion 3 — it names the real failing
(zero dollars won, now doubled); criterion 4 — one tight sentence, every
word earns its place; criterion 5 — only someone who watched this team
would know Cryptoboy hired Hermes as an employee.

Runner-up: L1 (11 finals, $0, "pipeline") — kept as the fallback if the
winner is ever judged weak against the field.
