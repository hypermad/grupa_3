import json
from sqlalchemy import Column, String

from baza_de_date import Base
from baza_de_date.sqlalchemy_serializer import SQLAlchemySerializer


class ProductsSQLDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'products'

    id = Column(String, primary_key=True)
    product_name = Column(String)
    product_price = Column(String, unique=True)
    data_inregistrare = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("id_produs", None)
        self.product_name = fields["product_name"]
        self.product_price = fields["product_price"]
        self.data_inregistrare = fields.get("data_inregistrare", None)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
