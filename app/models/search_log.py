from sqlalchemy import Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SearchLog(Base):

    __tablename__ = "search_logs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    query: Mapped[str] = mapped_column(
        String(255)
    )

    brand: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    total_results: Mapped[int] = mapped_column(
        Integer
    )

    searched_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )