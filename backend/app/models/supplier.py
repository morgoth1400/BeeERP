from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    def __repr__(self):
        return f"Supplier(id={self.id}, name='{self.name}')"

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    contact: Mapped[str | None] = mapped_column(String(150))
