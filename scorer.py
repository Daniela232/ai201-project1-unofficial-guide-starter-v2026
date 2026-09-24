"""
Milestone: the scorer run_eval.py imports.

judge(question, expects, answer, results) -> bool

That name and that signature are required, or run_eval.py runs unscored
and the Run columns come out blank without any error.

This is a substring test: it checks whether the expects phrase appears
in the answer, case-insensitive. It can catch a missing fact (the phrase
just is not there) but it cannot catch an added one (the phrase is
there, and so is a made-up sentence next to it). That is why not every
criterion gets automated -- this covers the ones that repeat, the rest
get read by eye.
"""


def judge(question: str, expects: str, answer: str, results) -> bool:
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()
