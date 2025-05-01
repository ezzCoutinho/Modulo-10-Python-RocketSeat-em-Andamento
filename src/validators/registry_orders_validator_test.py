import pytest

from src.validators.registry_orders_validator import registry_orders_validator


@pytest.mark.skip(reason="SKIPPED")
def test_registry_orders_validator():
    body = {
        "data": {
            "name": "João",
            "address": "Rua limão",
            "cupom": False,
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "pizza", "quantidade": 3},
            ],
        }
    }
    registry_orders_validator(body)


@pytest.mark.skip(reason="SKIPPED")
def test_registry_orders_validator_with_errors():
    body_with_errors = {
        "data": {
            "name": 123,
            "address": "Rua limão",
            "cupom": "False",
            "items": [
                {"item": "Refrigerante", "quantidade": 2},
                {"item": "pizza", "quantidade": 3},
            ],
        }
    }
    with pytest.raises(Exception):
        registry_orders_validator(body_with_errors)
