import pytest

from src.models.connection.connection_handler import DBConnectionHandler
from src.repository.orders_repository import OrdersRepository

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


def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    data = orders_repository.select_one(doc_filter)
    print(data)
