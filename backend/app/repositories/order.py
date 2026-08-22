from sqlalchemy import Date, select

from app.models.order import Order
from app.repositories.base import BaseRepository


class OrderRepository(BaseRepository[Order]):
    model = Order

    def get_by_customer_id(self, customer_id: int) -> list[Order]:
        stmt = select(Order).where(Order.customer_id == customer_id)
        return list(self.db.scalars(stmt).all())

    def get_by_status(self, status: str) -> list[Order]:
        stmt = select(Order).where(Order.status == status)
        return list(self.db.scalars(stmt).all())

    def get_by_order_date(self, order_date: Date) -> list[Order]:
        stmt = select(Order).where(Order.order_date == order_date)
        return list(self.db.scalars(stmt).all())

    def get_by_delivery_date(self, delivery_date: Date) -> list[Order] | None:
        stmt = select(Order).where(Order.delivery_date == delivery_date)
        return list(self.db.scalars(stmt).all())
