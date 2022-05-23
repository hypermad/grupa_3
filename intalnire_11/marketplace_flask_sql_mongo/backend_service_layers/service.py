from backend_service_layers.storage_layer import StorageLayer
from flask import request
import json
import uuid
from datetime import datetime
from pytz import country_timezones, timezone


class ItemService:
    def __init__(self, storage_type, item_type):
        self.storage_type = storage_type
        if item_type in ["user", "order", "product"]:
            self.item_type = item_type
        else:
            raise ValueError("Selected item_type is invalid or does not exist")

    def get_item(self, item_id):
        return StorageLayer(self.storage_type, self.item_type).get_item(item_id)

    def create_item(self):
        item_id = str(uuid.uuid4())
        request_body = json.loads(request.data)
        request_body[f"{self.item_type}_id"] = item_id
        request_body["timestamp"] = datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
        StorageLayer(self.storage_type, self.item_type).create_item(request_body)
        return item_id

    def list_items(self):
        return StorageLayer(self.storage_type, self.item_type).list_items()

    def delete_item(self, item_id):
        StorageLayer(self.storage_type, self.item_type).delete_item(item_id)
        return f"Item {item_id} was removed from the database"
