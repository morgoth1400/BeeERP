from sqlalchemy import inspect

from app.db.session import engine
from app.models import (
    Article,
    Category,
    Customer,
    Order,
    OrderLine,
    Product,
    ProductArticle,
    Supplier,
)

MODELS = [
    Customer,
    Category,
    Product,
    Supplier,
    Article,
    ProductArticle,
    Order,
    OrderLine,
]


def test_registered_tables():
    inspector = inspect(engine)

    database_tables = set(inspector.get_table_names())

    expected_tables = {model.__tablename__ for model in MODELS}

    assert expected_tables.issubset(database_tables)


def test_model_columns_match_database():
    inspector = inspect(engine)

    for model in MODELS:
        model_columns = {column.name for column in model.__table__.columns}

        database_columns = {column["name"] for column in inspector.get_columns(model.__tablename__)}

        assert model_columns == database_columns
