from sqlalchemy import select

from app.models.order_line import OrderLine
from app.repositories.base import BaseRepository


class OrderLineRepository(BaseRepository[OrderLine]):
    model = OrderLine

    def get_by_order_id(self, order_id: int) -> OrderLine | None:
        stmt = select(OrderLine).where(OrderLine.order_id == order_id)
        return self.db.scalars(stmt).first()

    def get_by_product_id(self, product_id: int) -> OrderLine | None:
        stmt = select(OrderLine).where(OrderLine.product_id == product_id)
        return self.db.scalars(stmt).first()
