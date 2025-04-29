from abc import ABC, abstractmethod
from typing import Dict, List


class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_document(self, document: Dict) -> None:
        pass

    @abstractmethod
    def insert_list_of_documents(self, documents: List[Dict]) -> None:
        pass

    @abstractmethod
    def select_many(self, doc_filter: Dict) -> List[Dict]:
        pass

    @abstractmethod
    def select_one(self, doc_filter: Dict) -> Dict:
        pass

    @abstractmethod
    def select_many_with_properties(self, doc_filter: Dict) -> List:
        pass

    @abstractmethod
    def select_if_property_exists(self) -> Dict:
        pass

    @abstractmethod
    def select_by_object_id(self, object_id: str) -> Dict:
        pass

    @abstractmethod
    def edit_registry(self, object_id: str, new_data: Dict) -> None:
        pass

    @abstractmethod
    def edit_many_registries(self, doc_filter: Dict, new_data: Dict) -> None:
        pass

    @abstractmethod
    def edit_registry_with_increment(self, doc_filter: Dict, new_data: Dict) -> None:
        pass

    @abstractmethod
    def delete_registry(self, doc_filter: Dict) -> None:
        pass

    @abstractmethod
    def delete_many_registries(self, doc_filter: Dict) -> None:
        pass
