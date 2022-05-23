import json

from flask import Flask, Response
from backend_service_layers.api import app_response
from database.sql import SQLiteDatabaseConnection
from backend_service_layers.api import ItemApi
app = Flask("Marketplace API")


@app.route("/get_item/<string:storage_type>/<string:item_type>/<string:item_id>", methods=["GET"])
def get_item(storage_type, item_type, item_id):
    response = ItemApi(storage_type, item_type).get_item(item_id)
    return app_response(response)


@app.route("/put_item/<string:storage_type>/<string:item_type>", methods=["POST"])
def put_item(storage_type, item_type):
    response = ItemApi(storage_type, item_type).create_item()
    return app_response(response)

@app.route("/list_items/<string:storage_type>/<string:item_type>", methods=["GET"])
def list_items(storage_type, item_type):
    response = ItemApi(storage_type, item_type).list_items()
    return app_response(response)


@app.route("/delete_item/<string:storage_type>/<string:item_type>/<string:item_id>", methods=["DELETE"])
def delete_item(storage_type, item_type, item_id):
    response = ItemApi(storage_type, item_type).delete_item(item_id)
    return app_response(response)


def validate_request_body(name, second_parameter):
    if not name or not second_parameter:
        return Response(status=500, response=json.dumps({"message": f"{name} or {second_parameter} is missing"}))
    if len(name) < 1 or len(name) > 50:
        return Response(status=500, response=json.dumps(
            {"message": f"{name} must be longer than 1 character and less than 50 characters"}))


if __name__ == "__main__":
    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()
    app.run()
