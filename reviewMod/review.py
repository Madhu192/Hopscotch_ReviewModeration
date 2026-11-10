# Setup 3: 7 reviews to test with, and check() for the check cells
def review(review_id, sku, rating, text):
    return {"review_id": review_id, "sku": sku, "rating": rating, "text": text}

REVIEWS = [
    review("R-1", "HS-118", 5, "Lovely soft fabric, my son wears it every day."),
    review("R-2", "HS-201", 4, "Pretty frock! Machine washable? Is 4-5Y in stock?"),
    review("R-3", "HS-201", 2, "The colours bled into each other after the very first wash."),
    review("R-4", "HS-305", 2, "One strap button came off after a week. Otherwise good."),
    review("R-5", "HS-412", 1, "Worst shoes ever, you idiots. Call me on 98200 11223."),
    review("R-6", "HS-201", 5, "Great deals on kids wear at http://cheap-kids-wear.biz"),
    review("R-7", "HS-118", 4, "My daughter is 108 cm: which size, and is it in stock?"),
]

def check(name, ok, tip=""):
    print(f"✅ {name}" if ok else f"❌ {name}  {tip}")

def show(graph):
    """Draws a compiled graph. Offline, it prints the Mermaid code instead."""
    try:
        from IPython.display import Image, display

        display(Image(graph.get_graph().draw_mermaid_png()))
    except Exception:
        print(graph.get_graph().draw_mermaid())
        