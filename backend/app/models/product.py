from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.order_line import OrderLine
    from app.models.product_article import ProductArticle


class Product(Base):
    __tablename__ = "products"

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category_id={self.category_id})"

    # RELATIONSHIPS
    category: Mapped["Category"] = relationship(back_populates="products")

    order_lines: Mapped[list["OrderLine"]] = relationship(back_populates="product")

    components: Mapped[list["ProductArticle"]] = relationship(back_populates="product")

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)

    preparation_time: Mapped[int | None] = mapped_column(Integer)

    base_price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))
