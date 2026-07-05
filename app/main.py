from fastapi import FastAPI
from app.api.search_test import router as search_router
from app.api.test_db import router
from app.api.search import router as search_api
from app.api.autocomplete import router as autocomplete_router
from app.api.analytics import router as analytics_router
from app.api.recommendations import router as recommendation_router
from app.api.analytics import router as analytics_router
from app.api.cache import router as cache_router
from app.api.health import router as health_router
from app.api.metrics import router as metrics_router

app = FastAPI(
    title="SearchX API",
    version="1.0.0"
)

app.include_router(router)
app.include_router(search_router)
app.include_router(search_api)
app.include_router(autocomplete_router)
app.include_router(analytics_router)
app.include_router(recommendation_router)
app.include_router(cache_router)
app.include_router(health_router)
app.include_router(metrics_router)
@app.get("/")
def home():
    return {
        "message": "Welcome to SearchX 🚀"
    }