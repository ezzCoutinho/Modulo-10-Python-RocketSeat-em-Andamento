from typing import Dict, List

from bson import ObjectId


class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, documents: List[Dict]) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(documents)

    def select_many(self, doc_filter: Dict) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return list(data)

    def select_one(self, doc_filter: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(doc_filter)
        return data

    def select_many_with_properties(self, doc_filter: Dict) -> List:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter, {"_id": 0, "cupom": 0})
        return list(data)

    def select_if_property_exists(self) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({"address": {"$exists": True}}, {"_id": 0, "itens": 0})
        return list(data)

    def select_by_object_id(self, object_id: str) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data

    def edit_registry(self, object_id: str, new_data: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},
            {"$set": new_data},
        )

    def edit_many_registries(self, doc_filter: Dict, new_data: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(doc_filter, {"$set": new_data})

    def edit_registry_with_increment(self, doc_filter: Dict, new_data: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(doc_filter, {"$inc": new_data})

    def delete_registry(self, doc_filter: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one(doc_filter)

    def delete_many_registries(self, doc_filter: Dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(doc_filter)
