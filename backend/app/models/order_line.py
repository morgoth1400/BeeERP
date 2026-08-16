from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class OrderLine(Base):
    __tablename__ = "order_lines"

    def __repr__(self):
        return f"OrderLine(id={self.id}, order_id={self.order_id}, product_id={self.product_id})"

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)

    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)

    quantity: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    discount: Mapped[Decimal] = mapped_column(Numeric(5, 2))
