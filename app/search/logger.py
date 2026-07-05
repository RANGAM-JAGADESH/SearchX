from app.db.database import SessionLocal
from app.models.search_log import SearchLog


def log_search(
    query: str,
    total_results: int,
    brand: str | None = None,
    category: str | None = None,
):

    db = SessionLocal()

    try:

        log = SearchLog(
            query=query,
            brand=brand,
            category=category,
            total_results=total_results,
        )

        db.add(log)
        db.commit()

    finally:
        db.close()