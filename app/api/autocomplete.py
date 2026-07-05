from fastapi import APIRouter

from app.search.autocomplete import autocomplete

router = APIRouter()


@router.get("/autocomplete")
def get_autocomplete(q: str):

    return {
        "query": q,
        "suggestions": autocomplete(q)
    }