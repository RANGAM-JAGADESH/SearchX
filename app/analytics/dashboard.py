from sqlalchemy import func

from app.db.database import SessionLocal
from app.models.search_log import SearchLog


# ----------------------------------------
# Top Searches
# ----------------------------------------
def top_searches(limit: int = 10):

    db = SessionLocal()

    try:
        results = (
            db.query(
                SearchLog.query,
                func.count(SearchLog.id).label("count")
            )
            .group_by(SearchLog.query)
            .order_by(func.count(SearchLog.id).desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "query": r.query,
                "count": r.count
            }
            for r in results
        ]

    finally:
        db.close()


# ----------------------------------------
# Trending Brands
# ----------------------------------------
def top_brands(limit: int = 10):

    db = SessionLocal()

    try:
        results = (
            db.query(
                SearchLog.brand,
                func.count(SearchLog.id).label("count")
            )
            .filter(SearchLog.brand.isnot(None))
            .group_by(SearchLog.brand)
            .order_by(func.count(SearchLog.id).desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "brand": r.brand,
                "count": r.count
            }
            for r in results
        ]

    finally:
        db.close()


# ----------------------------------------
# Trending Categories
# ----------------------------------------
def top_categories(limit: int = 10):

    db = SessionLocal()

    try:
        results = (
            db.query(
                SearchLog.category,
                func.count(SearchLog.id).label("count")
            )
            .filter(SearchLog.category.isnot(None))
            .group_by(SearchLog.category)
            .order_by(func.count(SearchLog.id).desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "category": r.category,
                "count": r.count
            }
            for r in results
        ]

    finally:
        db.close()


# ----------------------------------------
# Zero Result Searches
# ----------------------------------------
def zero_results(limit: int = 20):

    db = SessionLocal()

    try:
        results = (
            db.query(
                SearchLog.query,
                func.count(SearchLog.id).label("count")
            )
            .filter(SearchLog.total_results == 0)
            .group_by(SearchLog.query)
            .order_by(func.count(SearchLog.id).desc())
            .limit(limit)
            .all()
        )

        return [
            {
                "query": r.query,
                "count": r.count
            }
            for r in results
        ]

    finally:
        db.close()


# ----------------------------------------
# Daily Search Trends
# ----------------------------------------
def daily_searches():

    db = SessionLocal()

    try:
        results = (
            db.query(
                func.date(SearchLog.searched_at).label("date"),
                func.count(SearchLog.id).label("count")
            )
            .group_by(func.date(SearchLog.searched_at))
            .order_by(func.date(SearchLog.searched_at))
            .all()
        )

        return [
            {
                "date": str(r.date),
                "count": r.count
            }
            for r in results
        ]

    finally:
        db.close()


# ----------------------------------------
# Dashboard
# ----------------------------------------
def dashboard():

    db = SessionLocal()

    try:

        total_searches = db.query(
            func.count(SearchLog.id)
        ).scalar()

        zero_result_searches = (
            db.query(func.count(SearchLog.id))
            .filter(SearchLog.total_results == 0)
            .scalar()
        )

        success_rate = 0.0

        if total_searches:
            success_rate = round(
                ((total_searches - zero_result_searches) / total_searches) * 100,
                2
            )

        overview = {
            "total_searches": total_searches,
            "zero_result_searches": zero_result_searches,
            "success_rate": success_rate
        }

    finally:
        db.close()

    return {
        "overview": overview,
        "top_searches": top_searches(),
        "top_brands": top_brands(),
        "top_categories": top_categories(),
        "zero_result_queries": zero_results(),
        "daily_searches": daily_searches()
    }