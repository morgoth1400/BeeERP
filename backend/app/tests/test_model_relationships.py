import pytest

from app.db.base import Base


def get_relationships():
    relationships = []

    for mapper in Base.registry.mappers:
        model = mapper.class_

        for relationship in mapper.relationships:
            related_model = relationship.mapper.class_

            relationships.append(
                pytest.param(
                    model,
                    relationship.key,
                    related_model,
                    relationship.back_populates,
                    id=(
                        f"{model.__name__}.{relationship.key}"
                        f"<->{related_model.__name__}."
                        f"{relationship.back_populates}"
                    ),
                )
            )

    return relationships


@pytest.mark.parametrize(
    "model, relationship_name, related_model, reverse_name",
    get_relationships(),
)
def test_model_relationship(
    model,
    relationship_name,
    related_model,
    reverse_name,
):
    relationship = getattr(model, relationship_name).property

    assert relationship.back_populates == reverse_name

    reverse_relationship = getattr(
        related_model,
        reverse_name,
    ).property

    assert reverse_relationship.back_populates == relationship_name
