from datetime import datetime
from pytz import country_timezones, timezone
from baza_de_date.sql import SQLiteDatabaseConnection
from common.utils import genereaza_id
from baza_de_date.sql_models.users_sql_db_model import UsersSQLDBModel


def listeaza_utilizator_flask_sql(id_utilizator):
    db = SQLiteDatabaseConnection()
    with db:
        user = db.get_user_by_id(id_utilizator)
        if not user:
            return 404, f"Utilizator-ul {id_utilizator} nu se afla in baza de date"
        user = user.serialize()
    return 200, user


def adauga_un_utilizator_flask_sql(request_body):
    db = SQLiteDatabaseConnection()
    with db:
        if db.get_user_by_email(request_body["email_address"]):
            return 400, f"Utilizator-ul cu email-ul {request_body['email_address']} deja exista in baza de date"
    id_utilizator = genereaza_id({request_body["user_name"]: request_body["email_address"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    request_body["id_utilizator"] = id_utilizator
    request_body["data_inregistrare"] = data_inregistrare
    user_model = UsersSQLDBModel(**request_body)
    with db:
        id_utilizator = db.create_user(user_model)
    return 201, f"User: {id_utilizator} has been successfully added"


def listeaza_toti_utilizatorii_flask_sql():
    db = SQLiteDatabaseConnection()
    with db:
        user_list = UsersSQLDBModel.serialize_list(db.list_all_users())
        if not user_list:
            return 404, "Nu exista utilizatori"
    return 200, user_list


def sterge_un_utilizator_flask_sql(id_utilizator):
    db = SQLiteDatabaseConnection()
    with db:
        rows = db.delete_user_by_id(id_utilizator)
    if rows == 0:
        return 404, f"Utilizator-ul {id_utilizator} nu se afla in baza de date"
    return 200, f"Successfully deleted user {id_utilizator}"
