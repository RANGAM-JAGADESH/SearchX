from fastapi import APIRouter

from app.cache.redis_client import redis_client

router = APIRouter(
    prefix="/cache",
    tags=["Cache"]
)


# -------------------------
# Clear Redis Cache
# -------------------------

@router.delete("/clear")
def clear_cache():

    redis_client.flushdb()

    return {
        "message": "Redis cache cleared."
    }


# -------------------------
# Cache Statistics
# -------------------------

@router.get("/stats")
def cache_stats():

    info = redis_client.info()

    return {
        "used_memory": info["used_memory_human"],
        "connected_clients": info["connected_clients"],
        "total_commands": info["total_commands_processed"],
        "keys": redis_client.dbsize()
    }