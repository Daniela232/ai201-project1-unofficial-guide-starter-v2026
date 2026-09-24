# The Unofficial Guide

By Daniela Valerio Desanero — corpus: campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This is a Q&A tool for the campus_life corpus, basically a bunch of real student posts about housing, dining, classes, and other campus stuff. You can ask it normal questions like 'is the housing lottery random' or 'what are the printing fees' and it'll dig through the docs and give you a real answer with the source attached. If you ask it something totally unrelated, like a random trivia question, it's smart enough to just say it doesn't know instead of making something up.

## Chunking Strategy

**Chunk size:** Not fixed — split on paragraph breaks (blank lines), with a 120-character minimum so no fragment is too small to be useful.
**Overlap:** None.

Most of the documents in `campus_life` are short posts: a title line followed by one or two paragraphs, each covering a distinct idea (e.g. "wait times" vs. "hours and cost" in the same dining hall post). The starter's fixed 800-character window barely touched these documents at all — almost nothing reached 800 characters, so it output 88 chunks from 88 documents, doing effectively nothing.

Splitting on paragraph breaks respects how these documents are actually written: one paragraph, one idea. A short leading title line on its own would become a useless orphan chunk, so any paragraph under 120 characters gets merged into its neighbor. Since I'm splitting at natural breaks rather than an arbitrary character count, no sentence gets cut in half, so overlap isn't needed.

Result: 88 documents became 121 chunks, averaging 230 characters (down from an 800-character ceiling), shortest 120, longest 421.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_cs_210_exams.txt#0` — produced by: `chunker.py::split_documents`

```
CS 210 Data Structures — assessment

Two midterms and a final, all drawn from lecture material rather than the textbook. Midterms are curved, the final is not.

Do the labs even though they're only 10% — the exams reuse the lab problems.
```

**Chunk 3** — source: `course_phys_130_exams.txt#0` — produced by: `chunker.py::split_documents`

```
PHYS 130 Mechanics — assessment

Three midterms, no final, plus a lab practical. Not curved, but the lowest midterm is dropped.

The lab practical is worth 20% and almost nobody prepares for it.
```

**Chunk 4** — source: `housing_aldridge_hall.txt#0` — produced by: `chunker.py::split_documents`

```
Aldridge Hall — what it's actually like

I lived here my sophomore year. Built 1968, renovated 2019. Rooms are doubles with a shared bathroom per floor.
```

**Chunk 5** — source: `housing_morrow_house_laundry.txt#0` — produced by: `chunker.py::split_documents`

```
Laundry in Morrow House

Machines take $1.50 wash, $1.25 dry, coin or card. There are eight washers and six dryers for the building, which is the wrong ratio and means the dryers back up on Sunday evenings.

Best time to do laundry here is Tuesday or Wednesday morning. Sunday after 6pm you will wait.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** Is the housing lottery random?

**Answer:**

```
No, the housing lottery is not random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, with random selection used only as a tie-break (admin_housing_lottery.txt).
```

**My relevance cutoff:** 0.6 (the starter's default). I ran my five in-corpus test questions and the five OUT_OF_SCOPE questions and got a clean gap: in-corpus questions topped out at 0.488, out-of-corpus questions started at 0.803. A cutoff of 0.6 sits comfortably in that gap with room on both sides.

| Question | In corpus? | Best distance |
|---|---|---|
| Do I really need to buy the books for my CS class, or are they available in the library? | Yes | 0.488 |
| What are the printing fees for color and black and white? | Yes | 0.321 |
| Is the housing lottery random? | Yes | 0.254 |
| What time is the cafe open until? | Yes | 0.381 |
| How loud is Aldridge Hall at night? | Yes | 0.413 |
| What is the capital of Mongolia? | No | 0.825 |
| How do I change the oil in a diesel engine? | No | 0.934 |
| Who won the 1994 World Cup? | No | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.803 |
| How do I write a for loop in Rust? | No | 0.877 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** My embedding step kept crashing with some ONNXRuntime error on my Mac. I asked Claude to help me figure it out and it turned out to be a known bug with Apple's CoreML stuff. Claude found the fix (adding preferred_providers to force it to run on CPU instead), but I'm the one who actually edited the file and reindexed everything.

**2.** For the chunking part, I had no idea how to split up the documents in a way that made sense. I showed Claude a few of my actual files and it suggested splitting on paragraph breaks instead of just cutting every 800 characters, since my docs are mostly short posts with one idea per paragraph. I looked over the logic (like the 120 character minimum so we don't get tiny useless chunks) before we actually put it in.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. At least 4 of 7 random chunks stand alone | 4 of 7 | 5/7 | 5/7 | 5/7 | MET |
| 5. 8 of 10 answers name a specific source | 8 of 10 | 15/15 | 15/15 | 15/15 | MET |

Produced by `run_eval.py::main`, full output committed in `results/run_2026-09-23_2108_before.md`.

Real output, criterion 1 (Is the housing lottery random?), run 1, best distance 0.2541, passed the gate, sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, housing_aldridge_hall.txt, housing_innisfree_hall.txt:

```
The housing lottery is not entirely random in the way most people assume. Rising sophomores get a number drawn at random, but juniors and seniors are ordered first by accumulated credit hours, with random tie-breaks used only for ties.

Source: admin_housing_lottery.txt
```

Real output, criterion 3, from `run_eval.py::check_out_of_scope`, cutoff 0.6, refused 5 of 5:

```
What is the capital of Mongolia? -- best distance 0.825 -- refused
How do I change the oil in a diesel engine? -- best distance 0.934 -- refused
Who won the 1994 World Cup? -- best distance 0.886 -- refused
What is the recommended dosage of ibuprofen for a headache? -- best distance 0.803 -- refused
How do I write a for loop in Rust? -- best distance 0.877 -- refused
```

Real output, criterion 4, from `chunker.py::split_documents` via `app.py chunks -n 7` (identical across all three runs, since chunking is deterministic):

```
Chunk 4 | source: course_stat_150.txt#1 | produced by: chunker.py::split_documents

Expect 5 to 6 hours a week outside class.

The one piece of advice: the dropped midterm makes the first one low-stakes; use it to learn the format.
```

This one is the weakest of the 7: it never names the course, so "the first one" (referring to a midterm) only makes sense if you already know you are reading about STAT 150.

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer, 4 of 5 | MET | All three runs landed on 4 of 5. The one miss every time was the Aldridge Hall noise question: the only chunk retrieved says quiet floors are enforced, but never actually describes how loud the building is at night, so the retrieved chunk did not contain the answer. This one came close to missing since 4 of 5 is exactly my target, not comfortably above it. |
| 2 | Every answer names a source, 5 of 5 | MET | All 15 outputs (5 questions times 3 runs) named a specific file. No exceptions across any run. |
| 3 | Gate stops out-of-corpus questions, 4 of 5 | MET | The gate is deterministic, so one pass was the whole measurement. All 5 out-of-scope questions were refused, and their distances (0.803 to 0.934) sit well clear of the 0.6 cutoff. |
| 4 | At least 4 of 7 random chunks stand alone | MET | I judged all 7 chunks by reading them without their surrounding context. 5 of 7 clearly stood alone. The other 2 were borderline: one referenced "the housing lottery" without explaining it, and one referenced "the first one" (a midterm) without naming which course, which only makes sense with outside context. Both of those leaned toward not standing alone, but even counting them as failures, 5 of 7 clears my target of 4 of 7. |
| 5 | 8 of 10 answers name a specific source | MET | All 15 outputs across the 5 questions and 3 runs named one specific file each. None were vague or absent. |

**A note on scoring:** After writing `scorer.py` (a substring test: does the `expects` phrase appear in the answer?), I re-ran the test and the automated scorer marked all 15 outputs "pass," including the Aldridge Hall noise question. My `expects` phrase was "quiet floors," and the generated answer does contain that phrase ("the quiet floors on levels 3 and 4 in Aldridge Hall are genuinely enforced"). But the question asked how loud the building actually is at night, and the answer never really answers that, it just confirms a policy exists. The substring test cannot tell the difference between a phrase appearing because it truly answers the question and a phrase appearing in a sentence that is close to the topic but does not actually respond to it. I'm keeping my manual verdict of 4 of 5 for criterion 1 rather than the scorer's 5 of 5, since a careful read shows the retrieved chunk did not actually contain the answer to what was asked.

## Diagnoses

I didn't miss any of my five criteria, every run passed. But that's not usually a good thing. If everything passes easily, it might mean the targets were too easy, not that the system is great.

If I had to pick one to make harder, it's criterion 1. Every run landed at exactly 4 out of 5, right at the edge, not above it. The one question that kept failing was "how loud is Aldridge Hall at night." Looking into it, my corpus just doesn't have a real answer to that question. There's a chunk that says quiet floors are enforced, but nothing about how loud it actually gets at night. So this question isn't really testing if my system works, it's testing if my system admits when it doesn't know something. Next time I'd either raise the target to 5 out of 5, or just pick a different test question that my corpus can actually answer.

Criterion 4 also felt a little easy. I got 5 out of 7 chunks that stood on their own, which beats my target of 4 out of 7, but 2 of those 5 were shaky calls. One mentioned "the housing lottery" without explaining what that is. Another said "the first one" without saying which class it meant. If I ran this test again a few more times, it wouldn't surprise me if it dropped to exactly 4 out of 7. So this one passed, but not by a lot.

## The Improvement

**What I changed:** I added one new rule to the grounding instruction in `generate.py::GROUNDING_INSTRUCTION`: if the documents only mention a related policy or fact but do not directly answer what was asked, the model must say so plainly rather than letting the related detail stand in for an answer.

**Why I picked it:** My diagnosis found that the Aldridge Hall noise question retrieved a chunk that mentions a related policy (quiet floors are enforced) but never actually describes loudness, and the model was answering as if that policy substituted for a real answer. This rule targets exactly that gap between "the documents mention something related" and "the documents actually answer the question."

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. At least 4 of 7 random chunks stand alone | 4 of 7 | 5/7 | 5/7 | 5/7 | MET |
| 5. 8 of 10 answers name a specific source | 8 of 10 | 15/15 | 15/15 | 15/15 | MET |

Produced by `run_eval.py::main`, full output committed in `results/run_2026-09-23_2151_after.md`.

All five structural verdicts are unchanged from before. That is expected: this improvement only edited the grounding prompt in `generate.py::GROUNDING_INSTRUCTION`, and none of my five criteria measure the wording of a generated answer closely enough to catch the actual effect. The real change only shows up in the answer text itself, below.

Real output, Aldridge Hall question (the case the fix targeted), run 2, best distance 0.4141, passed the gate, sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_noise.txt, housing_innisfree_hall_noise.txt, housing_morrow_house_noise.txt, housing_old_brewhouse_noise.txt:

```
The provided documents do not directly answer how loud Aldridge Hall is at night. They only state that quiet floors on floors 3 and 4 are genuinely enforced (housing_aldridge_hall_noise.txt).
```

Compare that to the same question before the change (run 1, before): "Based on the provided documents, the quiet floors on floors 3 and 4 in Aldridge Hall are genuinely enforced (housing_aldridge_hall_noise.txt). The documents do not provide specific information about noise levels at night beyond this." The before version buried the disclaimer as an afterthought; the after version leads with it, which is the improvement working as intended.

Real output, the books question (not the case the fix targeted, but affected anyway), run 2, best distance 0.4796, passed the gate, sources retrieved: admin_library_holds.txt, course_cs_340.txt, course_cs_340_exams.txt, money_textbooks.txt, study_library_hours.txt:

```
The provided documents do not directly answer whether you need to buy the books for your CS class or if they are available in the library. (Source: money_textbooks.txt, course_cs_340.txt, course_cs_340_exams.txt, admin_library_holds.txt, study_library_hours.txt)
```

This is the cost. Before the change, this same question reliably surfaced the useful "two-hour reserve" fact from money_textbooks.txt. After the change, the model got more cautious across the board, and on this run it withheld a fact it actually had, rather than only withholding on the case that genuinely lacked an answer.

**Did it help?** Yes, partially, and it came with a real cost. On the exact case the diagnosis pointed at, Aldridge Hall, the new rule worked 2 of 3 runs, correctly leading with "the documents do not directly answer this" instead of quietly substituting the enforcement policy as if it answered the question. But none of my five structural criteria moved, since none of them score the wording of the generated answer closely enough to catch this. And the same caution that fixed Aldridge Hall also made the model hedge on the books question in run 2, where it had a real, useful fact (the two-hour reserve) and chose not to state it. So this was a real improvement on the specific failure I diagnosed, but it was not free: it traded a false confidence problem for an occasional false caution problem elsewhere. If I had more time I would narrow the new rule so it only triggers when the retrieved chunk is about a clearly different sub-topic than the question, rather than any time part of a multi-part question goes unanswered.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
