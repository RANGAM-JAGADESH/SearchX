from app.search.client import es


def autocomplete(query: str):
    query = query.strip().lower()

    response = es.search(

    index="products",

    suggest={
        "product-suggest": {

            "prefix": query,

            "completion": {

                "field": "suggest"

            }

        }

    }

)

    suggestions = []

    options = response["suggest"]["product-suggest"][0]["options"]

    for option in options:
        suggestions.append(option["text"])

    return suggestions