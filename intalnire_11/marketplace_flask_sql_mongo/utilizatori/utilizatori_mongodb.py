from baza_de_date.mongo_db import MongoDB
from datetime import datetime
from pytz import country_timezones, timezone
from common.utils import genereaza_id
from baza_de_date.mongo_models.users_mongo_db_model import UsersMongoDBModel


def listeaza_utilizator_flask_mongo(id_utilizator):
    db = MongoDB()
    user = db.get_user_by_id(id_utilizator)
    if not user:
        return 404, f"Utilizator-ul {id_utilizator} nu se afla in baza de date"
    return 200, user


def adauga_un_utilizator_flask_mongo(request_body):
    db = MongoDB()
    if db.get_user_by_email(request_body["email_address"]):
        return 400, f"Utilizator-ul cu email-ul {request_body['email_address']} deja exista in baza de date"
    id_utilizator = genereaza_id({request_body["user_name"]: request_body["email_address"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0])).isoformat()
    request_body["id_utilizator"] = id_utilizator
    request_body["data_inregistrare"] = data_inregistrare
    user_model = UsersMongoDBModel(**request_body)
    id_utilizator = db.create_user(user_model)
    return 201, f"User: {id_utilizator} has been successfully added"


def listeaza_toti_utilizatorii_flask_mongo():
    db = MongoDB()
    user_list = db.list_all_users()
    if not user_list:
        return 404, "Nu exista utilizatori"
    return 200, user_list


def sterge_un_utilizator_flask_mongo(id_utilizator):
    db = MongoDB()
    if not db.get_user_by_id(id_utilizator):
        return 404, f"Utilizator-ul {id_utilizator} nu se afla in baza de date"
    db.delete_user_by_id(id_utilizator)
    return 200, f"Successfully deleted user {id_utilizator}"
