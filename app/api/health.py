from datetime import datetime
import time

from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import SessionLocal
from app.search.client import es
from app.cache.redis_client import redis_client

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():

    start = time.perf_counter()

    services = {}

    # -----------------------------------
    # API
    # -----------------------------------

    services["api"] = {
        "status": "healthy"
    }

    # -----------------------------------
    # PostgreSQL
    # -----------------------------------

    try:

        db = SessionLocal()

        db.execute(text("SELECT 1"))

        db.close()

        services["postgres"] = {
            "status": "healthy"
        }

    except Exception as e:

        services["postgres"] = {
            "status": "unhealthy",
            "error": str(e)
        }

    # -----------------------------------
    # Elasticsearch
    # -----------------------------------

    try:

        es.info()

        services["elasticsearch"] = {
            "status": "healthy"
        }

    except Exception as e:

        services["elasticsearch"] = {
            "status": "unhealthy",
            "error": str(e)
        }

    # -----------------------------------
    # Redis
    # -----------------------------------

    try:

        redis_client.ping()

        services["redis"] = {
            "status": "healthy"
        }

    except Exception as e:

        services["redis"] = {
            "status": "unhealthy",
            "error": str(e)
        }

    # -----------------------------------
    # Overall Status
    # -----------------------------------

    overall = "healthy"

    for service in services.values():

        if service["status"] == "unhealthy":

            overall = "degraded"
            break

    elapsed = round(
        (time.perf_counter() - start) * 1000,
        2
    )

    return {

        "status": overall,

        "timestamp": datetime.utcnow().isoformat(),

        "response_time_ms": elapsed,

        "services": services

    }