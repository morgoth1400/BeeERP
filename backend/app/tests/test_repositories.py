import inspect
import pkgutil
from datetime import date
from decimal import Decimal
from importlib import import_module

import pytest

from app.db.session import SessionLocal
from app.models.article import Article
from app.models.category import Category
from app.models.customer import Customer
from app.models.order import Order
from app.models.order_line import OrderLine
from app.models.product import Product
from app.models.supplier import Supplier
from app.repositories.base import BaseRepository


def discover_repositories():
    import app.repositories

    repositories = []

    for module_info in pkgutil.iter_modules(app.repositories.__path__):
        if module_info.name == "base":
            continue

        module = import_module(f"app.repositories.{module_info.name}")

        # "_" refers to the class name string, and "repository" to the class object
        for _, repository in inspect.getmembers(module, inspect.isclass):
            if (
                issubclass(repository, BaseRepository)
                and repository is not BaseRepository
                and repository.__module__ == module.__name__
            ):
                repositories.append(repository)

    return repositories


@pytest.fixture
def db_session():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture(
    params=discover_repositories(),
    ids=lambda repository: repository.__name__,
)
def repository(request, db_session):
    return request.param(db_session)


@pytest.fixture
def repository_data(repository, db_session):
    if repository.model is Customer:
        customer = Customer(
            name="Test",
            last_name="Customer",
            registration_date=date.today(),
        )

        def update(customer):
            customer.name = "Updated Customer"

        def assert_updated(customer):
            assert customer.name == "Updated Customer"

        return customer, update, assert_updated

    if repository.model is Category:
        category = Category(
            name="Test Category",
        )

        def update(category):
            category.name = "Updated Category"

        def assert_updated(category):
            assert category.name == "Updated Category"

        return category, update, assert_updated

    if repository.model is Supplier:
        supplier = Supplier(
            name="Test Supplier",
        )

        def update(supplier):
            supplier.name = "Updated Supplier"

        def assert_updated(supplier):
            assert supplier.name == "Updated Supplier"

        return supplier, update, assert_updated

    if repository.model is Article:
        supplier = Supplier(
            name="Test Supplier",
        )
        db_session.add(supplier)
        db_session.flush()

        article = Article(
            name="Test Article",
            quantity=Decimal("10.00"),
            price=Decimal("5.00"),
            supplier_id=supplier.id,
        )

        def update(article):
            article.name = "Updated Article"

        def assert_updated(article):
            assert article.name == "Updated Article"

        return article, update, assert_updated

    if repository.model is Product:
        category = Category(
            name="Test Category",
        )
        db_session.add(category)
        db_session.flush()

        product = Product(
            name="Test Product",
            category_id=category.id,
            preparation_time=10,
            base_price=Decimal("10.00"),
        )

        def update(product):
            product.name = "Updated Product"

        def assert_updated(product):
            assert product.name == "Updated Product"

        return product, update, assert_updated

    if repository.model is Order:
        customer = Customer(
            name="Test",
            last_name="Customer",
            registration_date=date.today(),
        )
        db_session.add(customer)
        db_session.flush()

        order = Order(
            customer_id=customer.id,
            order_date=date.today(),
            status="pending",
        )

        def update(order):
            order.status = "completed"

        def assert_updated(order):
            assert order.status == "completed"

        return order, update, assert_updated

    if repository.model is OrderLine:
        customer = Customer(
            name="Test",
            last_name="Customer",
            registration_date=date.today(),
        )
        db_session.add(customer)
        db_session.flush()

        order = Order(
            customer_id=customer.id,
            order_date=date.today(),
            status="pending",
        )
        db_session.add(order)
        db_session.flush()

        category = Category(
            name="Test Category",
        )
        db_session.add(category)
        db_session.flush()

        product = Product(
            name="Test Product",
            category_id=category.id,
            base_price=Decimal("10.00"),
        )
        db_session.add(product)
        db_session.flush()

        order_line = OrderLine(
            order_id=order.id,
            product_id=product.id,
            quantity=Decimal("1.00"),
            unit_price=Decimal("10.00"),
            discount=Decimal("0.00"),
        )

        def update(order_line):
            order_line.quantity = Decimal("2.00")

        def assert_updated(order_line):
            assert order_line.quantity == Decimal("2.00")

        return order_line, update, assert_updated

    raise ValueError(f"Unsupported model: {repository.model}")


def test_repository_has_model(repository):
    assert repository.model is not None


def test_get_by_id(repository, repository_data):
    repository_object, _, _ = repository_data

    repository.create(repository_object)

    result = repository.get_by_id(repository_object.id)

    assert result is repository_object


def test_get_by_id_returns_none_for_nonexistent_id(repository):
    result = repository.get_by_id(-1)

    assert result is None


def test_get_all(repository, repository_data):
    repository_object, _, _ = repository_data

    repository.create(repository_object)

    result = repository.get_all()

    assert result == [repository_object]


def test_get_all_with_limit(repository, repository_data):
    repository_object, _, _ = repository_data

    repository.create(repository_object)

    result = repository.get_all(limit=1)

    assert result == [repository_object]


def test_get_all_with_skip(repository, repository_data):
    repository_object, _, _ = repository_data

    repository.create(repository_object)

    result = repository.get_all(skip=1)

    assert result == []


def test_create(repository, repository_data):
    repository_object, _, _ = repository_data

    result = repository.create(repository_object)

    assert result is repository_object
    assert result.id is not None


def test_delete(repository, repository_data):
    repository_object, _, _ = repository_data

    repository.create(repository_object)

    object_id = repository_object.id

    repository.delete(repository_object)

    assert repository.get_by_id(object_id) is None


def test_update(repository, repository_data):
    repository_object, update, assert_updated = repository_data

    repository.create(repository_object)

    update(repository_object)

    result = repository.update(repository_object)

    assert_updated(result)
