from cerberus import Validator


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

    raise Exception(body_validator.errors)
