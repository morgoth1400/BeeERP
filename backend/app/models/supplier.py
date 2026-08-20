from typing import TYPE_CHECKING

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.article import Article


class Supplier(Base):
    __tablename__ = "suppliers"

    def __repr__(self):
        return f"Supplier(id={self.id}, name='{self.name}')"

    # RELATIONSHIPS
    articles: Mapped[list["Article"]] = relationship(back_populates="supplier")

    # ATTRIBUTES
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    contact: Mapped[str | None] = mapped_column(String(150))
