import pytest

from src.validators.registry_updater_validator import registry_updater_validator


@pytest.mark.skip(reason="SKIPPED")
def test_registry_updater_validator():
    body = {
        "data": {
            "name": "João",
            "address": "Rua limão",
            "cupom": False,
        }
    }
    registry_updater_validator(body)


@pytest.mark.skip(reason="SKIPPED")
def test_registry_updater_validator_with_errors():
    body_with_errors = {
        "data": {
            "name": "123",
            "address": "Rua limão",
            "cupom": "False",
        }
    }
    with pytest.raises(Exception):
        registry_updater_validator(body_with_errors)
