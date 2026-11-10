"""In-memory product, complaint, batch, and customer-service data."""

PRODUCTS = {
    "HS-118": {"vendor_id": "V2", "batch_id": "B4"},
    "HS-201": {"vendor_id": "V3", "batch_id": "B7"},
    "HS-305": {"vendor_id": "V1", "batch_id": "B2"},
    "HS-412": {"vendor_id": "V4", "batch_id": "B9"},
}

COMPLAINTS_14_DAYS = {
    ("HS-201", "quality_defect"): 6,
    ("HS-305", "quality_defect"): 1,
    ("HS-118", "size_fit"): 3,
}

BATCH_SALES = {
    "B4": {"sold": 800, "returned": 40},
    "B7": {"sold": 400, "returned": 64},
    "B2": {"sold": 600, "returned": 18},
    "B9": {"sold": 300, "returned": 9},
}

VENDOR_ALERTS = {"V1": 0, "V2": 1, "V3": 2, "V4": 0}

SIZE_CHARTS = {
    "HS-118": {"3-4Y": "98-104 cm", "4-5Y": "104-110 cm", "5-6Y": "110-116 cm"},
    "HS-201": {"2-3Y": "92-98 cm", "3-4Y": "98-104 cm", "4-5Y": "104-110 cm"},
}

CARE = {
    "HS-118": "Machine wash cold. Do not tumble dry.",
    "HS-201": "Machine wash cold, inside out, with similar colours.",
}

STOCK = {
    "HS-118": {"3-4Y": 14, "4-5Y": 9, "5-6Y": 0},
    "HS-201": {"2-3Y": 6, "3-4Y": 0, "4-5Y": 12},
}