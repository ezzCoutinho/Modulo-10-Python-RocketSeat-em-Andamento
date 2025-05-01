from src.models.connection.connection_handler import db_connection_handler
from src.models.repository.orders_repository import OrdersRepository
from src.use_case.registry_updater import RegistryUpdater


def registry_updater_composer() -> RegistryUpdater:
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    user_case = RegistryUpdater(model)
    return user_case
