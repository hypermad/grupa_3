from pymongo import MongoClient
from urllib import parse
from pathlib import Path
import os
# with open(Path(os.path.dirname(os.path.abspath(__file__)), "db_pwd_mongo.txt"), "r") as password_file:
    # connection_url = f"mongodb+srv://test_user:{parse.quote_plus(password_file.readline())}@itf.x5m6f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
connection_url = f"mongodb+srv://andrei:andrei@itf.x5m6f.mongodb.net/?retryWrites=true&w=majority"
# print(connection_url)

class MongoDB:
    def __enter__(self):
        self.client = MongoClient(connection_url, tls=True, tlsAllowInvalidCertificates=True)
        self.db = self.client["itf"]
        self.collection = self.db["my_itf_collection"]

    def get_item(self, item_id, item_model):
        result = self.collection.find_one({"_id": item_id})
        return result

    def create_item(self, item_model):
        self.collection.insert_one(item_model.__dict__)
        return item_model._id

    def get_user_by_email(self, email):
        result = self.collection.find(filter={"email_address": email})
        return list(result)

    def list_items(self, item_model, item_type):
        result = self.collection.find(filter={f"{item_type}_name": {"$exists": 1}})
        return list(result)

    def delete_item(self, item_id):
        self.collection.delete_one({"_id": item_id})

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()
