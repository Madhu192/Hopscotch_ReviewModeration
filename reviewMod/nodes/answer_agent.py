"""Answer customer questions by asking the model to call read-only tools."""

from langchain_core.messages import HumanMessage, SystemMessage

from ..model import get_model_with_tools
from ..state import ReviewState

AGENT_RULES = """You answer customers' questions in Hopscotch reviews.
Use the tools for facts; never guess. Ask for independent tools together.
When you have the facts, reply with the answer only: friendly, under 50 words."""


def answer_agent(state: ReviewState) -> dict:
    question = HumanMessage(
        f"Product: {state['review']['sku']}\nReview: {state['text']}"
    )
    history = [SystemMessage(AGENT_RULES), question] + state.get("messages", [])
    response = get_model_with_tools().invoke(history)

    update = {"messages": [response]}
    trips = state.get("trips", 0)
    if response.tool_calls:
        trips += 1
    else:
        update["answer"] = response.content
    update["trips"] = trips
    return update