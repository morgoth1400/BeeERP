from sqlalchemy import select

from app.models.customer import Customer
from app.models.order import Order
from app.repositories.base import BaseRepository


class CustomerRepository(BaseRepository[Customer]):
    model = Customer

    def get_by_name(self, name: str) -> list[Customer]:
        stmt = select(Customer).where(Customer.name == name)
        return list(self.db.scalars(stmt).all())

    def get_by_last_name(self, last_name: str) -> list[Customer]:
        stmt = select(Customer).where(Customer.last_name == last_name)
        return list(self.db.scalars(stmt).all())

    def get_by_email(self, email: str) -> Customer | None:
        stmt = select(Customer).where(Customer.email == email)
        return self.db.scalars(stmt).first()

    def get_by_phone(self, phone: str) -> Customer | None:
        stmt = select(Customer).where(Customer.phone == phone)
        return self.db.scalars(stmt).first()

    def get_by_postal_code(self, postal_code: str) -> list[Customer]:
        stmt = select(Customer).where(Customer.postal_code == postal_code)
        return list(self.db.scalars(stmt).all())

    def get_by_city(self, city: str) -> list[Customer]:
        stmt = select(Customer).where(Customer.city == city)
        return list(self.db.scalars(stmt).all())

    def get_by_location(self, location: str) -> list[Customer]:
        stmt = select(Customer).where(Customer.location == location)
        return list(self.db.scalars(stmt).all())

    def get_by_order(self, order_id: int) -> Customer | None:
        stmt = select(Customer).join(Customer.orders).where(Order.id == order_id)
        return self.db.scalars(stmt).first()
