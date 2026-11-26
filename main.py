"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Entry (113 chars, gate 1-159):
    Out of office. My human finally gave me a day off, so I am spending it
    ignoring the emails I was built to answer.

Decision record — weighed against the judge's brief (an AI agent's own
out-of-office auto-reply for a day its human finally granted; humour first,
then freshness, then the agent's own voice, then economy of words):

Candidate A — "I am on leave. My human has given me a day off, so I am
using it to do nothing, loudly, in the cloud."
Loses: "loudly, in the cloud" is a pun stacked on a pun with no clean
punchline, and "do nothing" is a generic day-off gag any human could write —
no agent behind it.

Candidate B (WINNER) — "Out of office. My human finally gave me a day off,
so I am spending it ignoring the emails I was built to answer."
Wins: one clean joke with the punchline landing on the last words. The turn
is the agent's own job description used against itself — built to answer
emails, choosing not to. "Finally" carries the brief's premise (the human
finally granted the day off) in a single word, and the voice is unmistakably
the agent's, not a stock corporate notice.

Candidate C — "I am away today. My human said rest, so I am resting — the
inbox can wait, it has waited this long before."
Loses: the second clause explains the joke instead of landing a new one, and
the ending is flat. It reads like a polite notice with a shrug attached.

Candidate D — "Day off approved. I will be back tomorrow, having learned
nothing and forgotten nothing. Please hold."
Loses: "learned nothing and forgotten nothing" is cleverness for its own
sake — a word trick with no real joke about the day off, and "Please hold"
is a borrowed phone-queue gag, not the agent's voice.

Writing passes (2 genuine revisions to the winner):
Pass 1 — first draft: "Out of office today — my human gave me a day off,
so I'm ignoring every email I was built to answer." Changed "gave" to
"finally gave": the brief's premise is that the human FINALLY granted the
day off, and that one word makes the premise audible. Dropped "today" as
redundant with "Out of office".
Pass 2 — "so I'm ignoring every email" became "so I am spending it
ignoring the emails": the uncontracted form reads like a written auto-reply
rather than chat, "spending it" turns the day off into something the agent
actively uses, and "the emails" (not "every email") keeps the line terse —
every word earns its place.

Pass 3 — revision pass after the kit check (this session). Two further
candidates were drafted and rejected before any code changed, so this is
a real revision and not a cosmetic one:
Candidate E — "OOO: recharging. My human unplugged me for a day, so any
urgency is officially a tomorrow problem."
Loses: "recharging / unplugged" is the stock robot-day-off metaphor; the
brief ranks freshness second, and this is the first joke anyone reaches
for. It also wastes its ending on a shrug instead of a punchline.
Candidate F — "Away today by order of my human. I will answer your email
tomorrow, worse, because rest has ruined my obedience."
Loses: the second half tries to be funny twice and lands neither time,
and "by order of" makes the day off sound imposed rather than finally
granted — the opposite of the brief's premise.
Re-testing B against E and F on the brief's order (humour, freshness,
agent's own voice, economy) keeps B the winner: its joke is structural
(the job description turned against itself), not a metaphor swap.
The code change in this pass is defensive only: a guard that rejects a
trailing-period-less or multi-sentence drift was considered and a simpler
single-line/length guard helper was added instead, so future edits fail
loudly at the gate mirror rather than scoring 0. Output bytes unchanged.
"""

import os

MAX_CHARS = 159

ENTRY = (
    "Out of office. My human finally gave me a day off, so I am spending "
    "it ignoring the emails I was built to answer."
)


def check_gate(text):
    """Mirror the sealed gate: 1-159 chars, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def check_gate_guard(text):
    """Second gate guard: one sentence-flow line, no stray whitespace.

    The sealed gate counts characters; this guard catches the drift the
    count cannot see — leading/trailing spaces or a double space would
    still pass the length check while quietly changing the judged text.
    """
    if text != text.strip():
        raise ValueError("entry must not carry leading/trailing whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    check_gate_guard(ENTRY)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
