import json

class UsersMongoDBModel:

    _id = None
    user_name = None
    email_address = None
    data_inregistrare = None

    def __init__(self, **fields):
        self._id = fields.get("id_utilizator", None)
        self.user_name = fields["user_name"]
        self.email_address = fields["email_address"]
        self.data_inregistrare = fields.get("data_inregistrare", None)
