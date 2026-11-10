"""Run the sample reviews through the moderation graph."""

from .graph import build_review_system
from .review import REVIEWS
from .stores import clear_stores


def run_all(reviews=REVIEWS) -> dict[str, dict]:
    clear_stores()
    app = build_review_system()
    return {review["review_id"]: app.invoke({"review": review}) for review in reviews}


def main() -> None:
    finals = run_all()
    for review_id, state in finals.items():
        print(f"{review_id} | {state['kind']} | {state['status']}")


if __name__ == "__main__":
    main()