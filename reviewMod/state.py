# Part 1a: the state
import operator
from typing import Annotated, Literal, NotRequired, TypedDict

from langchain_core.messages import AnyMessage


class Review(TypedDict):
    review_id: str
    sku: str
    rating: int
    text: str


class ReviewState(TypedDict):
    review: Review
    text: NotRequired[str]
    kind: NotRequired[Literal["praise", "question", "complaint", "abusive"]]
    issue_type: NotRequired[Literal["none", "size_fit", "quality_defect", "delivery", "other"]]
    complaint_count: NotRequired[int]
    return_rate: NotRequired[float]
    vendor_alerts: NotRequired[int]
    reply: NotRequired[str]
    messages: NotRequired[Annotated[list[AnyMessage], operator.add]]
    trips: NotRequired[int]
    answer: NotRequired[str]
    status: NotRequired[str]
    