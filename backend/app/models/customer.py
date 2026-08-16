from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Customer(Base):
    __tablename__ = "customers"

    def __repr__(self):
        return f"Customer(id={self.customer_id}, name='{self.name}', last_name='{self.last_name}')"

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    last_name: Mapped[str | None] = mapped_column(String(150))

    phone: Mapped[str | None] = mapped_column(String(20))

    address: Mapped[str | None] = mapped_column(String(200))

    postal_code: Mapped[str | None] = mapped_column(String(10))

    city: Mapped[str | None] = mapped_column(String(100))

    location: Mapped[str | None] = mapped_column(String(100))

    email: Mapped[str | None] = mapped_column(String(150))

    registration_date: Mapped[Date] = mapped_column(Date)

    notes: Mapped[str | None] = mapped_column(Text)
