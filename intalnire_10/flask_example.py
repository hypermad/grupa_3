from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/home_page", methods=["GET"])
def home_page():
    return f"Hello, Welcome to my Homepage"


@app.route("/afisare_mesaj", methods=["POST"])
def afisare_mesaj():
    requested_messsage = json.loads(request.data)
    return f"Hello, the message you wanted displayed is: {requested_messsage['message']}"


@app.route("/afisare_mesaj_text", methods=["POST"])
def afisare_mesaj_text():
    requested_messsage = request.data.decode()
    return f"Hello, the message you wanted displayed is: {requested_messsage}"


@app.route("/get_user/<user>", methods=["GET"])
def get_user(user):
    return f"Hello, I'm user {user}"


@app.route("/delete_user/<user>", methods=["DELETE"])
def delete_user(user):
    return f"{user} has been deleted"


if __name__ == "__main__":
    app.run()
