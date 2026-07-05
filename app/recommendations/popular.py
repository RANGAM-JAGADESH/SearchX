from app.search.client import es


def popular_products(limit=10):

    body = {

        "query": {
            "match_all": {}
        },

        "sort": [
            {
                "stock": {
                    "order": "desc"
                }
            },
            {
                "rating": {
                    "order": "desc"
                }
            }
        ],

        "size": limit

    }

    response = es.search(
        index="products",
        body=body
    )

    results = []

    for hit in response["hits"]["hits"]:

        p = hit["_source"]

        p.pop("suggest", None)

        p["score"] = hit["_score"]

        results.append(p)

    return results