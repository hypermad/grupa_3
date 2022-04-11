import json

from flask import Flask, Response, request
from utilizatori.functii import adauga_un_utilizator_flask, listeaza_toti_utilizatorii_flask, sterge_un_utilizator_flask

app = Flask("Marketplace API")


@app.route("/get_user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    return Response(status=200, response=json.dumps({"message": f"Hello, I'm A user: {user_id}"}))


@app.route("/put_user", methods=["POST"])
def put_user():
    message = json.loads(request.data)
    user_name = message.get("user_name")
    email_address = message.get("email_address")
    if not user_name or not email_address:
        return Response(status=500, response=json.dumps({"message": "user_name or email_address is missing"}))
    if len(user_name) < 1 or len(user_name) > 50:
        return Response(status=500, response=json.dumps(
            {"message": "user_name must be longer than 1 character and less than 50 characters"}))
    id_utilizator = adauga_un_utilizator_flask(user_name, email_address)
    return Response(status=200, response=json.dumps({"message": f"User: {id_utilizator} has been successfully added"}))


@app.route("/list_users", methods=["GET"])
def list_users():
    return Response(status=200, response=json.dumps(listeaza_toti_utilizatorii_flask()))


@app.route("/delete_user/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    status, message = sterge_un_utilizator_flask(user_id)
    return Response(status=status, response=json.dumps({"message": message}))
    # a doua varianta
    # response = sterge_un_utilizator_flask(user_id)
    # return response

if __name__ == "__main__":
    app.run()
