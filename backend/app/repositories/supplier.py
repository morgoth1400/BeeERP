from sqlalchemy import select

from app.models.supplier import Supplier
from app.repositories.base import BaseRepository


class SupplierRepository(BaseRepository[Supplier]):
    model = Supplier

    def get_by_name(self, name: str) -> Supplier | None:
        stmt = select(Supplier).where(Supplier.name == name)
        return self.db.scalars(stmt).first()
