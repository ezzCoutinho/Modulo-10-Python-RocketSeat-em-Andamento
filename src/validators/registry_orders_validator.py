from cerberus import Validator

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


def registry_orders_validator(body: dict) -> dict:
    body_validator = Validator(
        {
            "data": {
                "type": "dict",
                "required": True,
                "schema": {
                    "name": {"type": "string", "required": True},
                    "address": {"type": "string", "required": True},
                    "cupom": {"type": "boolean", "required": True},
                    "items": {
                        "type": "list",
                        "required": True,
                        "schema": {
                            "type": "dict",
                            "schema": {
                                "item": {"type": "string", "required": True},
                                "quantidade": {
                                    "type": "integer",
                                    "min": 1,
                                    "required": True,
                                },
                            },
                        },
                    },
                },
            }
        }
    )

    if body_validator.validate(body):
        return body

    raise HttpUnprocessableEntity(body_validator.errors)
