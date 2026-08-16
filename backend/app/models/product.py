from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Product(Base):
    __tablename__ = "products"

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category_id={self.category_id})"

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)

    preparation_time: Mapped[int | None] = mapped_column(Integer)

    base_price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))
