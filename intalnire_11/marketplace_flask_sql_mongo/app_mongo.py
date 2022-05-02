import json
from flask import Flask, Response, request
from utilizatori.utilizatori_mongodb import (adauga_un_utilizator_flask_mongo, listeaza_utilizator_flask_mongo,
                                             listeaza_toti_utilizatorii_flask_mongo, sterge_un_utilizator_flask_mongo)


app = Flask("Marketplace API")


@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    status, message = listeaza_utilizator_flask_mongo(user_id)
    return Response(status=status, response=json.dumps(message))


@app.route("/put_user", methods=["POST"])
def put_user():
    request_body = json.loads(request.data)
    user_name = request_body.get("user_name")
    email_address = request_body.get("email_address")
    if not user_name or not email_address:
        return Response(status=500, response=json.dumps("user_name or email_address is missing"))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=500,
                        response=json.dumps("user_name must be longer than 1 character and less than 50 characters"))
    status, message = adauga_un_utilizator_flask_mongo(request_body)
    return Response(status=status, response=json.dumps(message))


@app.route("/list_users", methods=["GET"])
def list_users():
    status, message = listeaza_toti_utilizatorii_flask_mongo()
    return Response(status=status, response=json.dumps(message))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask_mongo(user_id)
    return Response(status=status, response=json.dumps({"message": message}))


if __name__ == "__main__":
    app.run()
