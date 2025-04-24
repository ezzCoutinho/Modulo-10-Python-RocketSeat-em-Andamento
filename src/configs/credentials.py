import os

credentials = {
    "username": os.getenv("MONGO_INITDB_ROOT_USERNAME"),
    "password": os.getenv("MONGO_INITDB_ROOT_PASSWORD"),
    "host": os.getenv("MONGO_HOST"),
    "port": os.getenv("MONGO_PORT"),
}
