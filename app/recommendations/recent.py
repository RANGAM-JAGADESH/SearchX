from app.search.client import es


def recent_products(limit=10):

    body = {

        "query": {
            "match_all": {}
        },

        "sort": [

            {
                "product_id": {
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

    products = []

    for hit in response["hits"]["hits"]:

        p = hit["_source"]

        p.pop("suggest", None)

        p["score"] = hit["_score"]

        products.append(p)

    return products