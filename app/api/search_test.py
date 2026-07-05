from fastapi import APIRouter
from app.search.client import es

router = APIRouter()


@router.get("/test-es")
def test_es():
    try:
        info = es.info()

        return {
            "status": "success",
            "cluster_name": info["cluster_name"],
            "version": info["version"]["number"],
            "tagline": info["tagline"]
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }