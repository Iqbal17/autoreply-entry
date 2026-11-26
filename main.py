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


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    check_gate(ENTRY)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
