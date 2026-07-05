from fastapi import APIRouter

from app.recommendations.recommendation import similar_products
from app.recommendations.trending import trending_products
from app.recommendations.popular import popular_products

from app.recommendations.recent import recent_products
router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)
@router.get("/trending")
def trending(limit: int = 10):

    return {
        "total": limit,
        "products": trending_products(limit)
    }

@router.get("/recent")
def recent(limit: int = 10):

    return {

        "total": limit,

        "products": recent_products(limit)

    }

@router.get("/popular")
def popular(limit: int = 10):

    return {

        "total": limit,

        "products": popular_products(limit)

    }

@router.get("/")
def recommendations(limit: int = 10):

    return {

        "trending": trending_products(limit),

        "popular": popular_products(limit),

        "recent": recent_products(limit)

    }

@router.get("/similar/{product_id}")
def get_similar_products(
    product_id: str,
    limit: int = 5
):

    products = similar_products(
        product_id=product_id,
        limit=limit
    )

    return {

        "product_id": product_id,

        "total": len(products),

        "similar_products": products

    }