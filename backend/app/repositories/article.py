from sqlalchemy import select

from app.models.article import Article
from app.models.product_article import ProductArticle
from app.repositories.base import BaseRepository


class ArticleRepository(BaseRepository[Article]):
    model = Article

    def get_by_name(self, name: str) -> Article | None:
        stmt = select(Article).where(Article.name == name)
        return self.db.scalars(stmt).first()

    def get_by_product(self, product_id: int) -> list[Article] | None:
        stmt = select(Article).join(Article.products).where(ProductArticle.product_id == product_id)
        return list(self.db.scalars(stmt).all())
