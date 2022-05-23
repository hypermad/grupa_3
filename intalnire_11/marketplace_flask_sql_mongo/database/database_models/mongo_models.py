class UsersMongoDBModel:
    _id = None
    user_name = None
    email_address = None
    timestamp = None

    def __init__(self, **fields):
        self._id = fields.get("user_id", None)
        self.user_name = fields["user_name"]
        self.email_address = fields["email_address"]
        self.timestamp = fields.get("timestamp", None)


class OrdersMongoDBModel:
    _id = None
    order_name = None
    order_quantity = None
    timestamp = None

    def __init__(self, **fields):
        self._id = fields.get("order_id", None)
        self.order_name = fields["order_name"]
        self.order_quantity = fields["order_quantity"]
        self.timestamp = fields.get("timestamp")


class ProductsMongoDBModel:
    _id = None
    product = None
    price = None
    timestamp = None

    def __init__(self, **fields):
        self._id = fields.get("product_id")
        self.product = fields["product_name"]
        self.price = fields["price"]
        self.timestamp = fields.get("timestamp", None)
