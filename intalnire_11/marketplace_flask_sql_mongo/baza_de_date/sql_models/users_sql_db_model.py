import json
from sqlalchemy import Column, String

from baza_de_date import Base
from baza_de_date.sqlalchemy_serializer import SQLAlchemySerializer


class UsersSQLDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'users'

    id = Column(String, primary_key=True)
    user_name = Column(String)
    email_address = Column(String, unique=True)
    data_inregistrare = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("id_utilizator", None)
        self.user_name = fields["user_name"]
        self.email_address = fields["email_address"]
        self.data_inregistrare = fields.get("data_inregistrare", None)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
