from baza_de_date.sql import SQLiteDatabaseConnection
from exceptions import UserAlreadyExists
from baza_de_date.users_db_model import UsersDBModel


def adauga_utilizator_in_sql_db(user_dict):
    db = SQLiteDatabaseConnection()
    with db:
        if db.get_user_by_email(user_dict["email"]):
            raise UserAlreadyExists(user_dict)
    user_model = UsersDBModel(**user_dict)
    with db:
        db.add_user(user_model)
        user_dict = db.get_user_by_email(user_model.email).serialize()
    return user_dict
