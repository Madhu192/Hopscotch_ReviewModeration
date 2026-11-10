"""Calculate a product batch's percentage return rate."""

from ..data import BATCH_SALES, PRODUCTS
from ..state import ReviewState


def get_return_rate(state: ReviewState) -> dict[str, float]:
    batch = PRODUCTS[state["review"]["sku"]]["batch_id"]
    sales = BATCH_SALES[batch]
    return {"return_rate": round(sales["returned"] / sales["sold"] * 100, 1)}