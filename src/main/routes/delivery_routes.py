from flask import Blueprint, jsonify, request

from src.composer.registry_find_composer import registry_finder_composer
from src.composer.registry_order_composer import registry_order_composer
from src.composer.registry_updater_composer import registry_updater_composer
from src.errors.error_controller import handle_errors
from src.main.http_types.http_request import HttpRequest

delivery_routes_bp = Blueprint("delivery_routes", __name__)


@delivery_routes_bp.route("/delivery/order", methods=["POST"])
def registry_order():
    try:
        user_case = registry_order_composer()
        http_request = HttpRequest(body=request.json)
        response = user_case.registry(http_request)
        return jsonify(response.body), response.status_code
    except Exception as e:
        return jsonify(handle_errors(e))


@delivery_routes_bp.route("/delivery/order/<order_id>", methods=["GET"])
def registry_finder(order_id):
    try:
        user_case = registry_finder_composer()
        http_request = HttpRequest(params={"order_id": order_id})
        response = user_case.find(http_request)
        return jsonify(response.body), response.status_code
    except Exception as e:
        return jsonify(handle_errors(e))


@delivery_routes_bp.route("/delivery/order/<order_id>", methods=["PATCH"])
def registry_updater(order_id):
    try:
        user_case = registry_updater_composer()
        http_request = HttpRequest(params={"order_id": order_id}, body=request.json)
        response = user_case.update(http_request)
        return jsonify(response.body), response.status_code
    except Exception as e:
        return jsonify(handle_errors(e))
