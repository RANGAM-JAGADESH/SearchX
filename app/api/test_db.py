from fastapi import APIRouter
from sqlalchemy import text

from app.db.database import engine

router = APIRouter()


@router.get("/test-db")
def test_database():

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "success",
            "message": "Connected to PostgreSQL 🎉"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }