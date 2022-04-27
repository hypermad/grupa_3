from storage_interface import StorageInterface
from baza_de_date.sql import SQLiteDatabaseConnection
from baza_de_date.mongo_db import MongoDB

import uuid
DB_MAPPING = {
    "sql": SQLiteDatabaseConnection,
    "mongo": MongoDB
}


class StorageLayer(StorageInterface):

    def __init__(self, storage_type, request_payload):
        self.storage_type = storage_type
        self.request_payload = request_payload
        database_object = DB_MAPPING.get(storage_type)
        if database_object:
            self.database_object = database_object()
        else:
            raise ValueError("Selected database is invalid or does not exist")

    def create_user(self):
        user_id = str(uuid.uuid4())
        return self.database_object.create_user(user_id, self.request_payload)


    def list_users(self):
        pass

    def delete_user(self):
        pass

    def update_user(self):
        pass

    def get_user(self):
        pass