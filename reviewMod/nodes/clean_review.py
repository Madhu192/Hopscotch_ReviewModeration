"""Redact personal information and detect links in review text."""

import re

from ..state import ReviewState

PHONE = re.compile(r"(\+91[\s-]?)?\b\d{5}\s?\d{5}\b")
EMAIL = re.compile(r"\S+@\S+\.\w+")
LINK = re.compile(r"https?://|www\.", re.IGNORECASE)


def clean_review(state: ReviewState) -> dict[str, str]:
    text = state["review"]["text"]
    text = PHONE.sub("[phone hidden]", text)
    text = EMAIL.sub("[email hidden]", text)
    return {"text": text}