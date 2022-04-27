import sqlalchemy
from functools import wraps
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from backend_services.storage_interface import StorageInterface

from baza_de_date import logger, Base
from baza_de_date.users_db_model import UsersDBModel


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


class SQLiteDatabaseConnection(StorageInterface):

    def __init__(self):
        self.engine = create_engine("sqlite:///db.sqlite", echo=False)
        self.session = None
        self.connection_name = None
        self.inspect = sqlalchemy.inspect(self.engine)

    def __enter__(self):
        self.session = sessionmaker(bind=self.engine)()

    @check_session()
    def create_tables_if_not_exists(self):
        try:
            if not self.inspect.has_table(UsersDBModel.__tablename__, schema=None):
                logger.info(f"Creating table {UsersDBModel.__tablename__}...")
                try:
                    Base.metadata.create_all(self.engine)
                except Exception as ex:
                    logger.error(ex)
                logger.info(f"Created table {UsersDBModel.__tablename__}...")
            else:
                logger.info(f"Table {UsersDBModel.__tablename__} already exists!")
        except SQLAlchemyError as e:
            logger.error(e, exc_info=True)
            raise

    @check_session()
    def create_user(self, user_id, user_model: UsersDBModel):
        self.session.add(user_model)

    @check_session()
    def get_user_by_email(self, email):
        return self.session.query(UsersDBModel).filter(UsersDBModel.email == email).one_or_none()

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
