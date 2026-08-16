from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class ProductArticle(Base):
    __tablename__ = "product_articles"

    def __repr__(self):
        return (
            f"ProductArticle("
            f"product_id={self.product_id}, "
            f"article_id={self.article_id}, "
            f"quantity={self.quantity})"
        )

    # ATTRIBUTES
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)

    article_id: Mapped[int] = mapped_column(ForeignKey("articles.id"), primary_key=True)

    quantity: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
