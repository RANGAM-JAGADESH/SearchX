from app.search.client import es
from app.db.database import SessionLocal
from app.models.product import Product


def sync_products():

    db = SessionLocal()

    products = db.query(Product).all()

    print(f"Found {len(products)} products")

    success = 0

    for product in products:

        document = {

            "product_id": product.product_id,

            "title": product.title,

            "description": product.description,

            "brand": product.brand,

            "category": product.category,

            "price": float(product.price),

            "rating": float(product.rating),

            "stock": product.stock,

            "image_url": product.image_url,

            "suggest": {
                "input": [
                    product.title
                ]
            }

        }
        es.index(
            index="products",
            id=product.id,
            document=document
        )

        success += 1

        if success % 500 == 0:

            print(f"Indexed {success} products...")

    print()

    print(f"Successfully Indexed {success} Products!")

    db.close()