from typing import Dict

from src.errors.error_controller import handle_errors
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.orders_repository_interface import (
    OrdersRepositoryInterface,
)
from src.errors.types.http_not_found import HttpNotFound


class RegistryFinder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def find(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.query.get("order_id")
            order = self.__search_order(order_id)
            return self.__format_response(order)
        except Exception as e:
            return handle_errors(e)

    def search_order(self, order_id: str) -> Dict:
        order = self.__orders_repository.select_by_object_id(order_id)

        if not order:
            raise HttpNotFound("Order not found")

        return order

    def __format_response(self, order: Dict) -> Dict:
        return HttpResponse(
            body={"data": {"count": 1, "type": "Order", "attributes": order}},
            status_code=200,
        )
