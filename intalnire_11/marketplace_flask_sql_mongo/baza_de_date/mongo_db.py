from pymongo import MongoClient
from urllib import parse
from baza_de_date.mongo_models.users_mongo_db_model import UsersMongoDBModel
from pathlib import Path
import os
with open(Path(os.path.dirname(os.path.abspath(__file__)), "db_pwd_mongo.txt"), "r") as password_file:
    connection_url = f"mongodb+srv://andrei_itf:{parse.quote_plus(password_file.readline())}@itf.x5m6f.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


class MongoDB:
    client = MongoClient(connection_url, tls=True, tlsAllowInvalidCertificates=True)
    db = client["itf"]
    collection = db["my_itf_collection"]

    def create_user(self, user_model: UsersMongoDBModel):
        self.collection.insert_one(user_model.__dict__)
        return user_model._id

    def get_user_by_id(self, user_id):
        result = self.collection.find_one({"_id": user_id})
        return result

    def get_user_by_email(self, email):
        result = self.collection.find(filter={"email_address": email})
        return list(result)

    def list_all_users(self):
        result = self.collection.find(filter={"user_name": {"$exists": 1}})
        return list(result)

    def delete_user_by_id(self, user_id):
        self.collection.delete_one({"_id": user_id})
