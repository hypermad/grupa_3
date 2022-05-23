from backend_service_layers.storage_interface import StorageInterface
from database.sql import SQLiteDatabaseConnection
from database.mongo_db import MongoDB
from database.database_models.sql_models import UsersSQLDBModel, ProductsSQLDBModel, OrdersSQLDBModel
from database.database_models.mongo_models import UsersMongoDBModel, ProductsMongoDBModel, OrdersMongoDBModel
from backend_service_layers.exceptions import UserAlreadyExists, ResourceNotFound

DB_MAPPING = {
    "sql": SQLiteDatabaseConnection,
    "mongo": MongoDB
}

ITEM_MODEL_MAPPING = {
    "sql": {
        "user": UsersSQLDBModel,
        "order": OrdersSQLDBModel,
        "product": ProductsSQLDBModel
    },
    "mongo": {
        "user": UsersMongoDBModel,
        "order": ProductsMongoDBModel,
        "product": OrdersMongoDBModel
    }
}


class StorageLayer(StorageInterface):

    def __init__(self, storage_type, item_type):
        self.storage_type = storage_type
        self.item_type = item_type
        database_object = DB_MAPPING.get(storage_type)
        if database_object:
            self.database_object = database_object()
        else:
            raise ValueError("Selected database is invalid or does not exist")
        self.item_model = ITEM_MODEL_MAPPING[self.storage_type][self.item_type]

    def get_item(self, item_id):
        with self.database_object:
            item = self.database_object.get_item(item_id, self.item_model)
            if not item:
                raise ResourceNotFound(item_id)

    def create_item(self, request_body):
        self.item_model = self.item_model(**request_body)
        if request_body.get("email_address"):
            with self.database_object:
                if self.database_object.get_user_by_email(request_body["email_address"]):
                    raise UserAlreadyExists(request_body)
        with self.database_object:
            self.database_object.create_item(self.item_model)

    def list_items(self):
        with self.database_object:
            return self.database_object.list_items(self.item_model, self.item_type)

    def delete_item(self, item_id):
        with self.database_object:
            return self.database_object.delete_item(item_id, self.item_model)
