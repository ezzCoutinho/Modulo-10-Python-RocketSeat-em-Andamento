from typing import Dict
from src.main.http_types.http_response import HttpResponse
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from src.errors.types.http_not_found import HttpNotFound


def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntity, HttpNotFound)):
        return HttpResponse(
            body={"errors": [{"title": error.name, "detail": error.message}]},
            status_code=error.status_code,
        )

    return HttpResponse(
        body={"errors": [{"title": "Server Error", "detail": str(error)}]},
        status_code=500,
    )
