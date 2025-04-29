import pytest

from src.models.repository.orders_repository import OrdersRepository


class CollectionMock:
    def __init__(self) -> None:
        self.insert_one_attributes = {}
        self.find_attributes = {}

    def insert_one(self, intput_data: any):
        self.insert_one_attributes["dict"] = intput_data

    def find(self, *args):
        self.find_attributes["args"] = args
        return []


class DbCollectionMock:
    def __init__(self, collection_name) -> None:
        self.get_collection_attributes = {}
        self.collection_name = collection_name

    def get_collection(self, collection_name):
        self.get_collection_attributes["name"] = collection_name
        return self.collection_name


@pytest.mark.skip(reason="SKIPPED")
def test_insert_document():
    collection_mock = CollectionMock()
    db_collection_mock = DbCollectionMock(collection_mock)
    orders_repository = OrdersRepository(db_collection_mock)

    data = {"name": "John", "age": 30}
    orders_repository.insert_document(data)
    print()
    print(collection_mock.insert_one_attributes)

    assert collection_mock.insert_one_attributes["dict"] == data


# @pytest.mark.skip(reason="SKIPPED")
def test_select_many_with_properties():
    collection_mock = CollectionMock()
    db_collection_mock = DbCollectionMock(collection_mock)
    orders_repository = OrdersRepository(db_collection_mock)

    data = {"testando": "find"}
    orders_repository.select_many_with_properties(data)
    print()
    print(collection_mock.find_attributes)
    print(collection_mock.find_attributes["args"][0])
    print(collection_mock.find_attributes["args"][1])

    expected_args = (data, {"_id": 0, "cupom": 0})
    assert collection_mock.find_attributes["args"] == expected_args
    assert collection_mock.find_attributes["args"][0] == data
    assert collection_mock.find_attributes["args"][1] == {"_id": 0, "cupom": 0}
