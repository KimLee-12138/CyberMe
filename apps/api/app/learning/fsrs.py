"""FSRS-5 (Free Spaced Repetition Scheduler) — core scheduling algorithm.

Ratings:
  1 = again  — completely forgot
  2 = hard   — recalled with difficulty
  3 = good   — recalled correctly
  4 = easy   — recalled easily

State machine:  new → learning → review → relearning → review

Default parameters from FSRS-5 public benchmark.
"""

import math
from datetime import datetime, timedelta, timezone

# FSRS-5 default weights (17 parameters)
W = [
    0.4021, 0.5778, 2.498, 5.8209,   # w[0..3]: initial stability for again/hard/good/easy
    4.9335, 0.9402, 0.8622, 0.0115,  # w[4..7]: difficulty & stability factors
    1.4922, 0.1413, 0.9443, 2.1854,  # w[8..11]: stability factors
    0.0513, 0.3383, 1.2686, 0.2915,  # w[12..15]: more factors
    2.6148,                            # w[16]
]

DECAY = -0.5  # exp(ln(0.5)) per stability unit
FACTOR = 0.9 ** (1 / DECAY)


def _elapsed_days(due_at: datetime | None) -> float:
    """Days since the card was due (or 0 if not yet due)."""
    if due_at is None:
        return 0.0
    now = datetime.now(timezone.utc)
    delta = (now - due_at).total_seconds() / 86400.0
    return max(0.0, delta)


def _retrievability(elapsed_days: float, stability: float) -> float:
    """Probability of recall after elapsed days given current stability."""
    if stability <= 0:
        return 1.0
    return (1.0 + FACTOR * elapsed_days / (9.0 * stability)) ** DECAY


def new_card() -> dict:
    """Create a new card in initial state."""
    return {
        "state": "new",
        "stability": 0.0,
        "difficulty": 0.0,
        "reps": 0,
        "lapses": 0,
        "due_at": datetime.now(timezone.utc).isoformat(),
    }


def schedule(card_state: dict, rating: int) -> dict:
    """Schedule next review given a card and a rating (1=again, 2=hard, 3=good, 4=easy).

    Returns updated card dict with new state, stability, difficulty, due_at, reps, lapses.
    """
    rating = max(1, min(4, rating))
    state = card_state.get("state", "new")
    stability = float(card_state.get("stability", 0))
    difficulty = float(card_state.get("difficulty", 0))
    reps = int(card_state.get("reps", 0))
    lapses = int(card_state.get("lapses", 0))
    due_at_str = card_state.get("due_at")
    due_at = datetime.fromisoformat(due_at_str) if due_at_str else datetime.now(timezone.utc)

    elapsed = _elapsed_days(due_at)
    r = _retrievability(elapsed, stability) if stability > 0 else 1.0

    if rating == 1:  # ── Again ──
        # Difficulty increases (easier to remember next time with higher difficulty)
        difficulty = min(difficulty + W[4], 1.0)
        # Mean reversion on difficulty
        difficulty = W[5] * 0.0 + (1.0 - W[5]) * difficulty
        # Reset stability
        stability = W[0]
        reps = 0
        lapses += 1
        # State → relearning
        state = "relearning"
        # Short interval: 1 minute
        interval_minutes = 1

    elif rating == 2:  # ── Hard ──
        difficulty = max(0.0, min(1.0, difficulty + W[4] * (rating - 3)))
        difficulty = W[5] * 0.0 + (1.0 - W[5]) * difficulty

        if state == "new":
            stability = W[1]
        elif state in ("learning", "relearning"):
            stability = W[1]
        else:
            # Apply hard penalty if retrieval was poor
            hard_penalty = W[15] if r < 0.5 else 1.0
            stability *= 1.0 + math.exp(W[6]) * (11.0 - difficulty) ** W[7] * (math.exp(W[8] * (1.0 - r)) - 1.0) * hard_penalty

        reps += 1
        state = "review"
        interval_days = stability * (0.9 ** (1.0 / DECAY))  # Convert stability to days

    elif rating == 3:  # ── Good ──
        difficulty = max(0.0, min(1.0, difficulty + W[4] * (rating - 3)))
        difficulty = W[5] * 0.0 + (1.0 - W[5]) * difficulty

        if state == "new":
            stability = W[2]
        elif state in ("learning", "relearning"):
            stability = W[2]
        else:
            stability *= 1.0 + math.exp(W[9]) * (11.0 - difficulty) ** W[10] * (math.exp(W[11] * (1.0 - r)) - 1.0)

        reps += 1
        state = "review"
        interval_days = stability * (0.9 ** (1.0 / DECAY))

    else:  # ── Easy (rating == 4) ──
        difficulty = max(0.0, min(1.0, difficulty + W[4] * (rating - 3)))
        difficulty = W[5] * 0.0 + (1.0 - W[5]) * difficulty

        if state == "new":
            stability = W[3]
        elif state in ("learning", "relearning"):
            stability = W[3]
        else:
            stability *= 1.0 + math.exp(W[12]) * (11.0 - difficulty) ** W[13] * (math.exp(W[14] * (1.0 - r)) - 1.0)

        reps += 1
        state = "review"
        interval_days = stability * (0.9 ** (1.0 / DECAY))

    if rating >= 2:
        # Successful review — schedule forward
        interval_seconds = int(interval_days * 86400)
        # Clamp: min 10 minutes, max 365 days
        interval_seconds = max(600, min(interval_seconds, 365 * 86400))
    else:
        interval_seconds = interval_minutes * 60

    new_due = datetime.now(timezone.utc) + timedelta(seconds=interval_seconds)

    return {
        "state": state,
        "stability": round(stability, 4),
        "difficulty": round(difficulty, 4),
        "reps": reps,
        "lapses": lapses,
        "due_at": new_due.isoformat(),
        "due_at_dt": new_due,
        "interval_seconds": interval_seconds,
    }
