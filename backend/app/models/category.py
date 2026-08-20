from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.product import Product


class Category(Base):
    __tablename__ = "categories"

    def __repr__(self):
        return f"Category(id={self.id}, name='{self.name}')"

    # RELATIONSHIPS
    products: Mapped[list["Product"]] = relationship(back_populates="category")

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
