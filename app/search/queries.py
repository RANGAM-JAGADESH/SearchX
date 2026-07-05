from app.search.client import es
import json

from app.cache.redis_client import redis_client
from app.search.client import es
from app.metrics.metrics import record_request
import time


def search_products(
    query: str,
    page: int = 1,
    limit: int = 10,
    brand: list[str] | None = None,
    category: list[str] | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
    min_rating: float | None = None,
    in_stock: bool = False,
    sort: str = "relevance",
):
    start_time = time.perf_counter()
    query = query.strip().lower()

    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "multi_match": {
                            "query": query,
                            "fields": [
                                "title^5",
                                "brand^3",
                                "category^2",
                                "description"
                            ],
                            "type": "best_fields",
                            "fuzziness": "AUTO"
                        }
                    }
                ],
                "filter": []
            }
        },

        "from": (page - 1) * limit,
        "size": limit,

        "highlight": {
            "pre_tags": ["<em>"],
            "post_tags": ["</em>"],
            "fields": {
                "title": {},
                "description": {},
                "brand": {},
                "category": {}
            }
        },

        "aggs": {

            "brands": {
                "terms": {
                    "field": "brand",
                    "size": 20,
                    "order": {
                        "_count": "desc"
                    }
                }
            },

            "categories": {
                "terms": {
                    "field": "category",
                    "size": 20,
                    "order": {
                        "_count": "desc"
                    }
                }
            },

            "price_ranges": {
                "range": {
                    "field": "price",
                    "ranges": [
                        {"key": "0-100", "to": 100},
                        {"key": "100-500", "from": 100, "to": 500},
                        {"key": "500-1000", "from": 500, "to": 1000},
                        {"key": "1000+", "from": 1000}
                    ]
                }
            },

            "ratings": {
                "range": {
                    "field": "rating",
                    "ranges": [
                        {"key": "4+", "from": 4},
                        {"key": "3+", "from": 3},
                        {"key": "2+", "from": 2},
                        {"key": "1+", "from": 1}
                    ]
                }
            },

            "stock": {
                "filters": {
                    "filters": {
                        "in_stock": {
                            "range": {
                                "stock": {
                                    "gt": 0
                                }
                            }
                        },
                        "out_of_stock": {
                            "term": {
                                "stock": 0
                            }
                        }
                    }
                }
            }

        }

    }

    filters = body["query"]["bool"]["filter"]

    # -------------------------
    # Brand Filter
    # -------------------------

    if brand:

        filters.append(
            {
                "terms": {
                    "brand": brand
                }
            }
        )

    # -------------------------
    # Category Filter
    # -------------------------

    if category:

        filters.append(
            {
                "terms": {
                    "category": category
                }
            }
        )

    # -------------------------
    # Price Filter
    # -------------------------

    if min_price is not None or max_price is not None:

        price_filter = {}

        if min_price is not None:
            price_filter["gte"] = min_price

        if max_price is not None:
            price_filter["lte"] = max_price

        filters.append(
            {
                "range": {
                    "price": price_filter
                }
            }
        )

    # -------------------------
    # Rating Filter
    # -------------------------

    if min_rating is not None:
        filters.append(
            {
                "range": {
                    "rating": {
                        "gte": min_rating
                    }
                }
            }
        )

    # -------------------------
    # Stock Filter
    # -------------------------

    if in_stock:
        filters.append(
            {
                "range": {
                    "stock": {
                        "gt": 0
                    }
                }
            }
        )

    # -------------------------
    # Sorting
    # -------------------------

    sort_options = {

        "price_asc": [
            {
                "price": {
                    "order": "asc"
                }
            }
        ],

        "price_desc": [
            {
                "price": {
                    "order": "desc"
                }
            }
        ],

        "rating": [
            {
                "rating": {
                    "order": "desc"
                }
            }
        ],

        "stock": [
            {
                "stock": {
                    "order": "desc"
                }
            }
        ]

    }

    if sort != "relevance":
        body["sort"] = sort_options.get(sort, [])

    # -------------------------
    # Redis Cache
    # -------------------------

    cache_key = json.dumps(body, sort_keys=True)

    cached = redis_client.get(cache_key)

    if cached:

        data = json.loads(cached)

        data["cached"] = True

        data["query_time_ms"] = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )
        record_request(
            response_time=data["query_time_ms"],
            cached=True
        )

        return data

    response = es.search(
        index="products",
        body=body
    )
    es_time = response["took"]

    total = response["hits"]["total"]["value"]

    results = []

    for hit in response["hits"]["hits"]:

        source = hit["_source"]

        source.pop("suggest", None)

        source["score"] = hit["_score"]

        source["highlight"] = hit.get("highlight", {})

        results.append(source)

    aggs = response["aggregations"]

    facets = {

    "brands": [

        {
            "value": b["key"],
            "count": b["doc_count"],
            "selected": brand is not None and b["key"] in brand
        }

        for b in aggs["brands"]["buckets"]

    ],

    "categories": [

        {
            "value": c["key"],
            "count": c["doc_count"],
            "selected": category is not None and c["key"] in category
        }

        for c in aggs["categories"]["buckets"]

    ],

    "price_ranges": [

        {
            "range": b["key"],
            "count": b["doc_count"]
        }

        for b in aggs["price_ranges"]["buckets"]

    ],
    "ratings": [

        {
            "rating": b["key"],
            "count": b["doc_count"]
        }

        for b in aggs["ratings"]["buckets"]

    ],

    "stock": [

    {
        "value": "In Stock",
        "count": aggs["stock"]["buckets"]["in_stock"]["doc_count"],
        "selected": in_stock
    },

    {
        "value": "Out of Stock",
        "count": aggs["stock"]["buckets"]["out_of_stock"]["doc_count"],
        "selected": False
    }

]

}

    result = {

    "total": total,

    "results": results,

    "facets": facets,

    "cached": False,

    "elasticsearch_time_ms": es_time,

    "query_time_ms": round(
        (time.perf_counter() - start_time) * 1000,
        2
    )

}

# Cache for 5 minutes
    redis_client.setex(
        cache_key,
        300,
        json.dumps(result)
    )

    record_request(
        response_time=result["query_time_ms"],
        cached=False
    )

    return result