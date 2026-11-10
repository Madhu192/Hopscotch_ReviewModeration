"""Read-only tools available to the customer-question agent."""

from langchain_core.tools import tool

from .data import CARE, SIZE_CHARTS, STOCK


@tool
def get_size_chart(sku: str) -> dict:
    """Return each available size label and the height range it fits for a product."""
    return SIZE_CHARTS.get(sku, {})


@tool
def get_care_instructions(sku: str) -> str:
    """Return washing and drying instructions for a product."""
    return CARE.get(sku, "unknown")


@tool
def check_stock(sku: str, size: str) -> dict:
    """Return stock for a product and size label, such as 4-5Y."""
    return {"size": size, "in_stock": STOCK.get(sku, {}).get(size)}


TOOLS = [get_size_chart, get_care_instructions, check_stock]