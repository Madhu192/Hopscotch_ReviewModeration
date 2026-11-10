"""Send abusive or spam reviews to the moderation queue."""

from ..state import ReviewState
from ..stores import MODERATION_QUEUE
from .clean_review import LINK


def hide_review(state: ReviewState) -> dict[str, str]:
    reason = "spam link" if LINK.search(state["text"]) else "abuse"
    MODERATION_QUEUE.append(state["review"]["review_id"])
    return {"status": f"hidden: {reason}"}