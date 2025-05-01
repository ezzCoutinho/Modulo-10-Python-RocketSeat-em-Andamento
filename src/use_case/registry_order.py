from datetime import datetime
from typing import Dict

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.orders_repository_interface import (
    OrdersRepositoryInterface,
)


class RegistryOrder:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        try:
            body = http_request.body
            new_order = self.__format_new_order(body)
            self.__registry_order(new_order)
            return self.__format_response()
        except Exception as e:
            return HttpResponse(
                body={"error": str(e)},
                status_code=400,
            )

    def __format_new_order(self, body: Dict) -> Dict:
        new_order = body["data"]
        new_order = {**new_order, "created_at": datetime.now()}
        return new_order

    def __registry_order(self, new_order: Dict) -> None:
        self.__orders_repository.insert_document(new_order)

    def __format_response(self) -> Dict:
        return HttpResponse(
            body={"data": {"type": "Order", "count": 1, "registry": True}},
            status_code=201,
        )
