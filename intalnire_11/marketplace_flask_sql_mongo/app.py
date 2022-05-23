from flask import Flask, Response
from database.sql import SQLiteDatabaseConnection
from backend_service_layers.api import ItemApi

app = Flask("Marketplace API")
CONTENT_TYPE = "application/json"


def app_response(api_response):
    return Response(response=api_response['body'], status=api_response['status_code'], content_type=CONTENT_TYPE)


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


if __name__ == "__main__":
    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()
    app.run()
