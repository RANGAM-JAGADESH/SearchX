def normalize_dummyjson(product):
    """
    Convert DummyJSON product into SearchX format
    """

    return {
        "product_id": str(product.get("id", "")),
        "title": product.get("title", ""),
        "description": product.get("description", ""),
        "brand": product.get("brand", ""),
        "category": product.get("category", ""),
        "price": float(product.get("price", 0)),
        "rating": float(product.get("rating", 0)),
        "stock": int(product.get("stock", 0)),
        "image_url": product["images"][0] if product.get("images") else ""
    }


def normalize_fakestore(product):
    """
    Convert FakeStore product into SearchX format
    """

    return {
        "product_id": str(product.get("id", "")),
        "title": product.get("title", ""),
        "description": product.get("description", ""),
        "brand": "Unknown",
        "category": product.get("category", ""),
        "price": float(product.get("price", 0)),
        "rating": float(product.get("rating", {}).get("rate", 0)),
        "stock": int(product.get("rating", {}).get("count", 0)),
        "image_url": product.get("image", "")
    }