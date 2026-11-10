"""Structured model outputs used by the review workflow."""

from typing import Literal

from pydantic import BaseModel, Field


class ReviewRead(BaseModel):
    kind: Literal["praise", "question", "complaint", "abusive"]
    issue_type: Literal["none", "size_fit", "quality_defect", "delivery", "other"] = Field(
        description="What a complaint is about; none for other kinds"
    )