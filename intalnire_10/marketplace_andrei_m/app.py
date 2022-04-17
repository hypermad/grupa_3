import json

from flask import Flask, Response, request
from utilizatori.functii import (listeaza_utilizator_flask, adauga_un_utilizator_flask,
                                 listeaza_toti_utilizatorii_flask,
                                 sterge_un_utilizator_flask)
from comenzi.functii import (listeaza_comanda_flask, adauga_o_comanda_flask, listeaza_toate_comenzile_flask,
                             sterge_o_comanda_flask)
from produse.functii import (listeaza_produs_flask, adauga_un_produs_flask, listeaza_toate_produsele_flask,
                             sterge_un_produs_flask)

app = Flask("Marketplace API")


@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    status, message = listeaza_utilizator_flask(user_id)
    return Response(status=status, response=json.dumps(message))


@app.route("/get_product/<string:product_id>", methods=["GET"])
def get_product(product_id):
    status, message = listeaza_produs_flask(product_id)
    return Response(status=status, response=json.dumps(message))


@app.route("/get_order/<string:order_id>", methods=["GET"])
def get_order(order_id):
    status, message = listeaza_comanda_flask(order_id)
    return Response(status=status, response=json.dumps(message))


@app.route("/put_user", methods=["POST"])
def put_user():
    request_body = json.loads(request.data)
    user_name = request_body.get("user_name")
    email_address = request_body.get("email_address")
    validate_request_body(user_name, email_address)
    id_utilizator = adauga_un_utilizator_flask(user_name, email_address)
    return Response(status=200, response=json.dumps({"message": f"User: {id_utilizator} has been successfully added"}))


@app.route("/put_product", methods=["POST"])
def put_product():
    request_body = json.loads(request.data)
    product_name = request_body.get("product_name")
    product_price = request_body.get("product_price")
    validate_request_body(product_name, product_price)
    id_produs = adauga_un_produs_flask(product_name, product_price)
    return Response(status=200, response=json.dumps({"message": f"Product: {id_produs} has been successfully added"}))


@app.route("/put_order", methods=["POST"])
def put_order():
    request_body = json.loads(request.data)
    order_name = request_body.get("order_name")
    order_quantity = request_body.get("order_quantity")
    validate_request_body(order_name, order_quantity)
    id_comanda = adauga_o_comanda_flask(order_name, order_quantity)
    return Response(status=200, response=json.dumps({"message": f"Order: {id_comanda} has been successfully added"}))


@app.route("/list_users", methods=["GET"])
def list_users():
    status, message = listeaza_toti_utilizatorii_flask()
    return Response(status=status, response=json.dumps(message))


@app.route("/list_products", methods=["GET"])
def list_users():
    status, message = listeaza_toate_produsele_flask()
    return Response(status=status, response=json.dumps(message))


@app.route("/list_orders", methods=["GET"])
def list_users():
    status, message = listeaza_toate_comenzile_flask()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask(user_id)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/delete_product/<string:product_id>", methods=["DELETE"])
def delete_user(product_id):
    status, message = sterge_un_produs_flask(product_id)
    return Response(status=status, response=json.dumps({"message": message}))


@app.route("/delete_order/<string:order_id>", methods=["DELETE"])
def delete_user(order_id):
    status, message = sterge_o_comanda_flask(order_id)
    return Response(status=status, response=json.dumps({"message": message}))


def validate_request_body(name, second_parameter):
    if not name or not second_parameter:
        return Response(status=500, response=json.dumps({"message": f"{name} or {second_parameter} is missing"}))
    if len(name) < 1 or len(name) > 50:
        return Response(status=500, response=json.dumps(
            {"message": "user_name must be longer than 1 character and less than 50 characters"}))


if __name__ == "__main__":
    app.run()
