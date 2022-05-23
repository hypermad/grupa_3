from database.sql import SQLiteDatabaseConnection
from exceptions import UserAlreadyExists
from database.sql_models.users_sql_db_model import UsersSQLDBModel


def adauga_utilizator_in_sql_db(user_dict):
    db = SQLiteDatabaseConnection()
    with db:
        if db.get_user_by_email(user_dict["email"]):
            raise UserAlreadyExists(user_dict)
    user_model = UsersSQLDBModel(**user_dict)
    with db:
        db.add_user(user_model)
        user_dict = db.get_user_by_email(user_model.email).serialize()
    return user_dict
