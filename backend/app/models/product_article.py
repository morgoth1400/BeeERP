from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.article import Article
    from app.models.product import Product


class ProductArticle(Base):
    __tablename__ = "product_articles"

    def __repr__(self):
        return (
            f"ProductArticle("
            f"product_id={self.product_id}, "
            f"article_id={self.article_id}, "
            f"quantity={self.quantity})"
        )

    # RELATIONSHIPS
    product: Mapped["Product"] = relationship(back_populates="components")

    article: Mapped["Article"] = relationship(back_populates="products")

    # ATTRIBUTES
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)

    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"), primary_key=True)

    quantity: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
