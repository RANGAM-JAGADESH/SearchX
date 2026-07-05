from sqlalchemy import func

from app.db.database import SessionLocal
from app.models.search_log import SearchLog


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
                "query": row.query,
                "count": row.count
            }
            for row in results
        ]

    finally:
        db.close()