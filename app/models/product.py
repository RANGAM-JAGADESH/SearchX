from datetime import datetime

from sqlalchemy import (
    BigInteger,
    String,
    Text,
    Numeric,
    Integer,
    TIMESTAMP
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    product_id: Mapped[str] = mapped_column(
        String(100)
    )

    title: Mapped[str] = mapped_column(
        Text
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    brand: Mapped[str] = mapped_column(
        String(200)
    )

    category: Mapped[str] = mapped_column(
        String(200)
    )

    price: Mapped[float] = mapped_column(
        Numeric(10, 2)
    )

    rating: Mapped[float] = mapped_column(
        Numeric(3, 1)
    )

    stock: Mapped[int] = mapped_column(
        Integer
    )

    image_url: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP
    )