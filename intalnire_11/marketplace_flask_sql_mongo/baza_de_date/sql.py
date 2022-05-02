from functools import wraps

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from baza_de_date import logger, Base
from baza_de_date.sql_models.users_sql_db_model import UsersSQLDBModel
from baza_de_date.sql_models.products_sql_db_model import ProductsSQLDBModel
from baza_de_date.sql_models.orders_sql_db_model import OrdersSQLDBModel


def check_session():
    """
    Decorator function to check if the session has been initialized

    :return: callable
    :raises Exception
    """

    def check_session_wrapper(callable_func):
        @wraps(callable_func)
        def decor_inner(instance, *args, **kwargs):
            if not instance.session:
                raise AttributeError('No session. Please use context manager.')
            return callable_func(instance, *args, **kwargs)

        return decor_inner

    return check_session_wrapper


class SQLiteDatabaseConnection:

    def __init__(self):
        self.engine = create_engine("sqlite:///db.sqlite", echo=False)
        self.session = None
        self.inspect = sqlalchemy.inspect(self.engine)

    def __enter__(self):
        self.session = sessionmaker(bind=self.engine)()

    @check_session()
    def create_tables_if_not_exists(self):
        try:
            if not (self.inspect.has_table(UsersSQLDBModel.__tablename__, schema=None)
                    and self.inspect.has_table(ProductsSQLDBModel.__tablename__, schema=None)
                    and self.inspect.has_table(OrdersSQLDBModel.__tablename__, schema=None)):
                logger.info(f"Creating table {UsersSQLDBModel.__tablename__}...")
                try:
                    Base.metadata.create_all(self.engine)
                except Exception as ex:
                    logger.error(ex)
                logger.info(f"Created table {UsersSQLDBModel.__tablename__}...")
            else:
                logger.info(f"Table {UsersSQLDBModel.__tablename__} already exists!")
        except SQLAlchemyError as e:
            logger.error(e, exc_info=True)
            raise

    @check_session()
    def create_user(self, user_model: UsersSQLDBModel):
        self.session.add(user_model)
        return user_model.id

    @check_session()
    def get_user_by_id(self, user_id):
        return self.session.query(UsersSQLDBModel).filter(UsersSQLDBModel.id == user_id).one_or_none()

    @check_session()
    def get_user_by_email(self, email):
        return self.session.query(UsersSQLDBModel).filter(UsersSQLDBModel.email_address == email).one_or_none()

    @check_session()
    def list_all_users(self):
        return self.session.query(UsersSQLDBModel).all()

    @check_session()
    def delete_user_by_id(self, user_id):
        deleted_rows = self.session.query(UsersSQLDBModel).filter(UsersSQLDBModel.id == user_id).delete()
        return deleted_rows

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.session.rollback()
            self.session.close()
            return False
        else:
            try:
                self.session.commit()
            except Exception as err:
                logger.error(f"Commit failed: {err}")
                self.session.rollback()
                self.session.close()
        self.session.close()
