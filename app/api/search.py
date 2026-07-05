from fastapi import APIRouter
from app.search.logger import log_search
from app.schemas.sort import SortOption
from app.search.queries import search_products
from app.search.suggestions import related_suggestions
from fastapi import Query

router = APIRouter()


@router.get("/search")
def search(
    q: str,
    page: int = 1,
    limit: int = 10,
    brand: list[str] | None = Query(default=None),
    category: list[str] | None = Query(default=None),   
    min_price: float | None = None,
    max_price: float | None = None,
    min_rating: float | None = None,
    in_stock: bool = False,
    sort: SortOption = SortOption.relevance,
):

    response = search_products(
        query=q,
        page=page,
        limit=limit,
        brand=brand,
        category=category,
        min_price=min_price,
        max_price=max_price,
        min_rating=min_rating,
        in_stock=in_stock,
        sort=sort.value,
    )
    log_search(
    query=q,
    brand=brand,
    category=category,
    total_results=response["total"]
)

    suggestions = related_suggestions(q)

    return {
    "query": q,

    "filters": {
        "brand": brand,
        "category": category,
        "min_price": min_price,
        "max_price": max_price,
        "min_rating": min_rating,
        "in_stock": in_stock,
        "sort": sort.value,
    },

    "page": page,

    "page_size": limit,

    "total_results": response["total"],

    "related_suggestions": suggestions,

    "facets": response["facets"],

    "results": response["results"],
}