from app.search.client import es


def similar_products(product_id: str, limit: int = 5):

    body = {

        "query": {

            "bool": {

                "must": {

                    "more_like_this": {

                        "fields": [
                            "title",
                            "description",
                            "brand",
                            "category"
                        ],

                        "like": [
                            {
                                "_index": "products",
                                "_id": product_id
                            }
                        ],

                        "min_term_freq": 1,
                        "min_doc_freq": 1

                    }

                },

                "must_not": [
                    {
                        "ids": {
                            "values": [
                                product_id
                            ]
                        }
                    }
                ]

            }

        },

        "size": limit

    }

    response = es.search(
        index="products",
        body=body
    )

    products = []

    for hit in response["hits"]["hits"]:

        product = hit["_source"]

        product.pop("suggest", None)

        product["score"] = hit["_score"]

        products.append(product)

    return products