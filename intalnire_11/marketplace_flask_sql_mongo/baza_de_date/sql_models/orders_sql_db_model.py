import json
from sqlalchemy import Column, String

from baza_de_date import Base
from baza_de_date.sqlalchemy_serializer import SQLAlchemySerializer


class OrdersSQLDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'orders'

    id = Column(String, primary_key=True)
    order_name = Column(String)
    order_quantity = Column(String, unique=True)
    data_inregistrare = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("id_comanda", None)
        self.order_name = fields["order_name"]
        self.order_quantity = fields["order_quantity"]
        self.data_inregistrare = fields.get("data_inregistrare", None)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
