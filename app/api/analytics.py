from fastapi import APIRouter

from app.analytics.dashboard import (
    top_searches,
    top_brands,
    top_categories,
    zero_results,
    daily_searches,
)
from app.analytics.dashboard import (
    dashboard,
    top_searches,
    top_brands,
    top_categories,
    zero_results,
    daily_searches,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/top-searches")
def get_top_searches():

    return top_searches()


@router.get("/top-brands")
def get_top_brands():

    return top_brands()


@router.get("/top-categories")
def get_top_categories():

    return top_categories()


@router.get("/zero-results")
def get_zero_results():

    return zero_results()


@router.get("/daily-searches")
def get_daily_searches():

    return daily_searches()

@router.get("/dashboard")
def analytics_dashboard():

    return dashboard()