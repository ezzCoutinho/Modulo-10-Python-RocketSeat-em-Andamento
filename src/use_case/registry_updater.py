from typing import Dict

from src.errors.error_controller import handle_errors
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.orders_repository_interface import (
    OrdersRepositoryInterface,
)
from src.validators.registry_updater_validator import registry_updater_validator


class RegistryUpdater:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def update(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.query.get("order_id")
            body = http_request.body
            self.__validate_body(body)

            self.__update_order(order_id, body)

            return self.__format_response()
        except Exception as e:
            return handle_errors(e)

    def __validate_body(self, body: Dict) -> None:
        registry_updater_validator(body)

    def _update_order(self, object_id: str, new_data: Dict) -> None:
        update_fields = new_data["data"]
        self.__orders_repository.edit_registry(object_id, update_fields)

    def __format_response(self, order_id: str) -> Dict:
        return HttpResponse(
            body={
                "data": {
                    "order_id": order_id,
                    "type": "Order",
                    "count": 1,
                    "edited": True,
                }
            },
            status_code=200,
        )
