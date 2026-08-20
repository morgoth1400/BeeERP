from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.product_article import ProductArticle
    from app.models.supplier import Supplier


class Article(Base):
    __tablename__ = "articles"

    def __repr__(self):
        return f"Article(id={self.id}, name='{self.name}')"

    # RELATIONSHIPS
    products: Mapped[list["ProductArticle"]] = relationship(back_populates="article")

    supplier: Mapped["Supplier"] = relationship(back_populates="articles")

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    quantity: Mapped[Decimal] = mapped_column(Numeric(12, 2))

    price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))

    unit_type: Mapped[str | None] = mapped_column(String(20))

    unit_price: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))

    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
