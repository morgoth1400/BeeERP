from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Order(Base):
    __tablename__ = "orders"

    def __repr__(self):
        return f"Order(id={self.id}, customer_id={self.customer_id}, status='{self.status}')"

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"), nullable=False)

    order_date: Mapped[Date] = mapped_column(Date)

    delivery_date: Mapped[Date | None] = mapped_column(Date)

    status: Mapped[str] = mapped_column(String(30))
