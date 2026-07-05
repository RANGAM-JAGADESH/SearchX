from app.search.client import es


def related_suggestions(query: str):

    response = es.search(
        index="products",
        body={
            "size": 5,
            "_source": ["title"],
            "query": {
                "match": {
                    "title": {
                        "query": query,
                        "fuzziness": "AUTO"
                    }
                }
            }
        }
    )

    suggestions = []

    seen = set()

    for hit in response["hits"]["hits"]:

        title = hit["_source"]["title"]

        if title not in seen:
            suggestions.append(title)
            seen.add(title)

    return suggestions