"""Write a public complaint reply and a quality-team alert."""

from functools import lru_cache

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from ..model import get_llm
from ..state import ReviewState
from ..stores import QUALITY_ALERTS

REPLY_RULES = (
    "Say sorry and thank them. Say it is passed on to the quality team. "
    "Never promise a refund or discount: returns go through the Orders page. Under 50 words."
)
ALERT_INSTRUCTION = (
    "Write a two-sentence alert for the quality team under 40 words. Name the product and "
    "problem, cite the evidence, and suggest one next step."
)

reply_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You write Hopscotch's public replies to complaints. Rules:\n" + REPLY_RULES),
        ("human", "Review ({rating} stars): {text}"),
    ]
)
alert_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", ALERT_INSTRUCTION),
        ("human", "Product: {sku}\nReview: {text}\nEvidence: {evidence}"),
    ]
)


@lru_cache(maxsize=1)
def _reply_writer():
    return reply_prompt | get_llm() | StrOutputParser()


@lru_cache(maxsize=1)
def _alert_writer():
    return alert_prompt | get_llm() | StrOutputParser()


def reply_and_alert(state: ReviewState) -> dict[str, str]:
    reply = _reply_writer().invoke(
        {"rating": state["review"]["rating"], "text": state["text"]}
    )
    evidence = (
        f"{state['complaint_count']} recent complaints; {state['return_rate']}% returns; "
        f"{state['vendor_alerts']} vendor alerts"
    )
    alert = _alert_writer().invoke(
        {"sku": state["review"]["sku"], "text": state["text"], "evidence": evidence}
    )
    QUALITY_ALERTS.append({"sku": state["review"]["sku"], "alert": alert})
    return {"reply": reply}