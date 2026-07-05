from app.search.client import es


def create_products_index():

    index_name = "products"

    if es.indices.exists(index=index_name):
        print("✅ Index already exists.")
        return

    es.indices.create(
        index=index_name,
        body={
            "settings": {
                "analysis": {
                    "normalizer": {
                        "lowercase_normalizer": {
                            "type": "custom",
                            "filter": [
                                "lowercase"
                            ]
                        }
                    }
                }
            },
            "mappings": {
                "properties": {

                    "product_id": {
                        "type": "keyword"
                    },

                    "title": {
                        "type": "text"
                    },

                    "suggest": {
                        "type": "completion"
                    },

                    "description": {
                        "type": "text"
                    },

                    "brand": {
                        "type": "keyword",
                        "normalizer": "lowercase_normalizer"
                    },

                    "category": {
                        "type": "keyword"
                    },

                    "price": {
                        "type": "float"
                    },

                    "rating": {
                        "type": "float"
                    },

                    "stock": {
                        "type": "integer"
                    },

                    "image_url": {
                        "type": "keyword"
                    }

                }
            }
        }
    )

    print("🎉 Products Index Created Successfully!")