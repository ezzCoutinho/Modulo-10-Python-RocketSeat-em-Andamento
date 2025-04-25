from typing import Dict, List


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
