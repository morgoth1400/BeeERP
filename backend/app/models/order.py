from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.customer import Customer
    from app.models.order_line import OrderLine


class Order(Base):
    __tablename__ = "orders"

    def __repr__(self):
        return f"Order(id={self.id}, customer_id={self.customer_id}, status='{self.status}')"

    # RELATIONSHIPS
    customer: Mapped["Customer"] = relationship(back_populates="orders")

    order_lines: Mapped[list["OrderLine"]] = relationship(back_populates="order")

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)

    order_date: Mapped[Date] = mapped_column(Date)

    delivery_date: Mapped[Date | None] = mapped_column(Date)

    status: Mapped[str] = mapped_column(String(30))
