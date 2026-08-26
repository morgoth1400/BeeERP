from sqlalchemy import select

from app.models.product import Product
from app.models.product_article import ProductArticle
from app.repositories.base import BaseRepository


class ProductRepository(BaseRepository[Product]):
    model = Product

    def get_by_name(self, name: str) -> Product | None:
        stmt = select(Product).where(Product.name == name)
        return self.db.scalars(stmt).first()

    def get_by_article(self, article_id: int) -> list[Product] | None:
        stmt = (
            select(Product).join(Product.components).where(ProductArticle.article_id == article_id)
        )
        return list(self.db.scalars(stmt).all())

    def get_by_category(self, category: str) -> Product | None:
        stmt = select(Product).where(Product.category == category)
        return self.db.scalars(stmt).first()
