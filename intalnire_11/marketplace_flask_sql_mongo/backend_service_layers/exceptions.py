class UserAlreadyExists(Exception):
    def __init__(self, value):
        super().__init__(f"User with email: {value['email_address']} already exists")


class ResourceNotFound(Exception):
    def __init__(self, value):
        super().__init__(f"{value} was not found")
