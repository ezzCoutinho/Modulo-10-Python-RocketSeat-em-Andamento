from pymongo import MongoClient

from src.configs.credentials import credentials


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = f"mongodb://{credentials['username']}:{credentials['password']}@{credentials['host']}:{credentials['port']}"
        self.__database_name = "rocket_db"
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self) -> MongoClient:
        return self.__db_connection
