import json
from sqlalchemy import Column, String

from database import Base
from database.sqlalchemy_serializer import SQLAlchemySerializer


class UsersSQLDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'users'

    id = Column(String, primary_key=True)
    user_name = Column(String)
    email_address = Column(String, unique=True)
    timestamp = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("user_id", None)
        self.user_name = fields["user_name"]
        self.email_address = fields["email_address"]
        self.timestamp = fields.get("timestamp", None)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"


class OrdersSQLDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'orders'

    id = Column(String, primary_key=True)
    order_name = Column(String)
    order_quantity = Column(String, unique=True)
    timestamp = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("order_id", None)
        self.order_name = fields["order_name"]
        self.order_quantity = fields["order_quantity"]
        self.timestamp = fields.get("timestamp", None)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"


class ProductsSQLDBModel(Base, SQLAlchemySerializer):
    __tablename__ = f'products'

    id = Column(String, primary_key=True)
    product_name = Column(String)
    product_price = Column(String, unique=True)
    timestamp = Column(String)

    def __init__(self, **fields):
        self.id = fields.get("product_id", None)
        self.product_name = fields["product_name"]
        self.product_price = fields["product_price"]
        self.timestamp = fields.get("timestamp", None)

    def __repr__(self):
        return f"{json.dumps(self.serialize())}"
