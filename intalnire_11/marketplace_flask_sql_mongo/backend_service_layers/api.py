import json
from functools import wraps

from flask import Response
from backend_service_layers.service import ItemService
from backend_service_layers.exceptions import UserAlreadyExists, ResourceNotFound

CONTENT_TYPE = "application/json"


def app_response(api_response):
    return Response(response=api_response['body'], status=api_response['status_code'], content_type=CONTENT_TYPE)


def response(message, status_code):
    return {
        'status_code': str(status_code),
        'body': json.dumps(message)
    }


def handle_request():
    """
    Handle common exceptions.
    :return: Decorated function.
    """

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                result = response(f(*args, **kwargs), 200)
                return result
            except (UserAlreadyExists, ResourceNotFound, ValueError) as e:
                return response(str(e), 400)
            except KeyError as e:
                return response(f'{str(e)} is required', 400)

        return wrapper

    return decorator


class ItemApi:
    def __init__(self, storage_type, item_type):
        self.storage_type = storage_type
        self.item_type = item_type

    @handle_request()
    def get_item(self, item_id):
        ItemService(self.storage_type, self.item_type).get_item(item_id)
        return ItemService(self.storage_type, self.item_type).get_item(item_id)

    @handle_request()
    def create_item(self):
        return ItemService(self.storage_type, self.item_type).create_item()

    @handle_request()
    def list_items(self):
        return ItemService(self.storage_type, self.item_type).list_items()

    @handle_request()
    def delete_item(self, user_id):
        return ItemService(self.storage_type, self.item_type).delete_item(user_id)
