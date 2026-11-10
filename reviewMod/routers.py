"""Plain-code routing decisions for the LangGraph workflow."""

from typing import Literal

from .nodes.clean_review import LINK
from .state import ReviewState

MAX_TRIPS = 4


def triage(state: ReviewState) -> str | list[str]:
    if LINK.search(state["text"]) or state["kind"] == "abusive":
        return "hide_review"
    if state["kind"] == "question":
        return "answer_agent"
    if state["kind"] == "complaint":
        return ["count_complaints", "get_return_rate", "vendor_record"]
    return "publish_review"


def after_agent(state: ReviewState) -> str:
    if not state["messages"][-1].tool_calls:
        return "publish_review"
    if state["trips"] > MAX_TRIPS:
        return "publish_review"
    return "tools"