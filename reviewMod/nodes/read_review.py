"""Classify a sanitized review with structured model output."""

from functools import lru_cache

from langchain_core.prompts import ChatPromptTemplate

from ..model import get_llm
from ..schemas import ReviewRead
from ..state import ReviewState

read_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You read product reviews for Hopscotch, a kids' clothing store."),
        ("human", "Rating: {rating} stars\nReview: {text}"),
    ]
)


@lru_cache(maxsize=1)
def _reader():
    return read_prompt | get_llm().with_structured_output(ReviewRead)


def read_review(state: ReviewState) -> dict[str, str]:
    result = _reader().invoke(
        {"rating": state["review"]["rating"], "text": state["text"]}
    )
    return {"kind": result.kind, "issue_type": result.issue_type}