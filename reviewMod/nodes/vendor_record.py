"""Look up the quality alerts associated with a product's vendor."""

from ..data import PRODUCTS, VENDOR_ALERTS
from ..state import ReviewState


def vendor_record(state: ReviewState) -> dict[str, int]:
    vendor = PRODUCTS[state["review"]["sku"]]["vendor_id"]
    return {"vendor_alerts": VENDOR_ALERTS.get(vendor, 0)}