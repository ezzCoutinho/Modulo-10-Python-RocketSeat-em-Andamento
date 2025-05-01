from src.models.connection.connection_handler import db_connection_handler
from src.models.repository.orders_repository import OrdersRepository
from src.use_case.registry_finder import RegistryFinder


def registry_finder_composer() -> RegistryFinder:
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    user_case = RegistryFinder(model)
    return user_case
