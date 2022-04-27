class UserAlreadyExists(Exception):
    def __init__(self, value):
        super().__init__(f"User with email: {value['email']} already exists")


class ResourceNotFound(Exception):
    def __init__(self, resource_type, field, value):
        super().__init__(f"{resource_type} with {field} = {value} was not found")
