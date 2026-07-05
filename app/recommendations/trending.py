from app.search.client import es


def trending_products(limit: int = 10):

    body = {
        "query": {
            "match_all": {}
        },
        "sort": [
            {"rating": {"order": "desc"}},
            {"stock": {"order": "desc"}}
        ],
        "size": limit
    }

    response = es.search(
        index="products",
        body=body
    )

    results = []

    for hit in response["hits"]["hits"]:

        product = hit["_source"]
        product.pop("suggest", None)
        product["score"] = hit["_score"]

        results.append(product)

    return results