from cerberus import Validator

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


def registry_updater_validator(body: dict) -> dict:
    body_validator = Validator(
        {
            "data": {
                "type": "dict",
                "required": True,
                "schema": {
                    "name": {"type": "string", "required": False},
                    "address": {"type": "string", "required": False},
                    "cupom": {"type": "boolean", "required": False},
                },
            }
        }
    )

    if body_validator.validate(body):
        return body

    raise HttpUnprocessableEntity(body_validator.errors)
