"""In-memory stand-ins for moderation and publishing destinations."""

MODERATION_QUEUE: list[str] = []
PUBLISHED: list[dict[str, str]] = []
QUALITY_ALERTS: list[dict[str, str]] = []


def clear_stores() -> None:
    MODERATION_QUEUE.clear()
    PUBLISHED.clear()
    QUALITY_ALERTS.clear()