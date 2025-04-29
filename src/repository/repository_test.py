import pytest

from src.models.connection.connection_handler import DBConnectionHandler
from src.repository.orders_repository import OrdersRepository
from bson import ObjectId

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="SKIPPED")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"name": "Ola", "Municipality": "São Paulo", "Order": "1234567890"}
    orders_repository.insert_document(my_doc)


@pytest.mark.skip(reason="SKIPPED")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_docs = [
        {"name": "elemento1", "Municipality": "São Paulo", "Order": "1234567890"},
        {"name": "elemento2", "Municipality": "São Paulo", "Order": "1234567890"},
        {"name": "elemento3", "Municipality": "São Paulo", "Order": "1234567890"},
    ]
    orders_repository.insert_list_of_documents(my_docs)


@pytest.mark.skip(reason="SKIPPED")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"client": "Aroldo Fernandes"}
    data = orders_repository.select_many(doc_filter)

    for item in data:
        print(item["itens"])


@pytest.mark.skip(reason="SKIPPED")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    data = orders_repository.select_one(doc_filter)
    print(data)


@pytest.mark.skip(reason="SKIPPED")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    data = orders_repository.select_many_with_properties(doc_filter)

    for cupom in data:
        print(cupom)


@pytest.mark.skip(reason="SKIPPED")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    data = orders_repository.select_if_property_exists()

    for item in data:
        print(item)


@pytest.mark.skip(reason="SKIPPED")
def test_select_many_with_multiple_filters():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.pizza": {"$exists": True},
    }  # Semelhante a AND em uma busca SQL
    data = orders_repository.select_many(doc_filter)

    for item in data:
        print(item)


@pytest.mark.skip(reason="SKIPPED")
def test_select_many_with_multiple_filters_with_or():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"itens.pizza.tipo": "vegana"},
            {"address": {"$exists": True}},
        ]
    }  # Semelhante a OR em uma busca SQL
    data = orders_repository.select_many(doc_filter)

    for item in data:
        print(item)


@pytest.mark.skip(reason="SKIPPED")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "680acfcc6a2842ab2f0fde9f"
    data = orders_repository.select_by_object_id(object_id)
    print(data)


@pytest.mark.skip(reason="SKIPPED")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    object_id = "680ad3b36a2842ab2f0fdea1"
    orders_repository.edit_registry(object_id, {"itens.pizza.tipo": "CALABRESA"})


@pytest.mark.skip(reason="SKIPPED")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "_id": ObjectId("680ad3b36a2842ab2f0fdea1"),
        "itens.pizza.tipo": {"$exists": True},
    }
    new_data = {"itens.pizza.tipo": "Vegana"}
    orders_repository.edit_many_registries(doc_filter, new_data)


def test_edit_registry_with_increment():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"itens.refrigerante.quantidade": {"$exists": True}}
    new_data = {"itens.refrigerante.quantidade": 91}
    orders_repository.edit_registry_with_increment(doc_filter, new_data)
