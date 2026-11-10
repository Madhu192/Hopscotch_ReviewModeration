"""Model configuration and lazy model construction."""

import os
from functools import lru_cache

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


@lru_cache(maxsize=1)
def get_llm() -> ChatOpenAI:
    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("Set OPENROUTER_API_KEY in the .env file before running the graph.")

    return ChatOpenAI(
        model="openai/gpt-4o-mini",
        temperature=0,
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )


@lru_cache(maxsize=1)
def get_model_with_tools():
    from .tools import TOOLS

    return get_llm().bind_tools(TOOLS)