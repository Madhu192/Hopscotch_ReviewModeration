"""Look up recent complaints for a product and issue type."""

from ..data import COMPLAINTS_14_DAYS
from ..state import ReviewState


def count_complaints(state: ReviewState) -> dict[str, int]:
    pair = (state["review"]["sku"], state["issue_type"])
    return {"complaint_count": COMPLAINTS_14_DAYS.get(pair, 0)}