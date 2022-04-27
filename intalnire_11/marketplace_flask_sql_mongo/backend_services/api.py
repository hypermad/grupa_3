import json
from functools import wraps

from flask import Response
from backend_services.storage_layer import StorageLayer



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
                return response(f(*args, **kwargs), 200)
            except (InvalidUser,
                    InvalidBook,
                    ValueError,
                    UserAlreadyExists,
                    ResourceNotFound,
                    BookAlreadyExists,
                    ReservationAlreadyExists,
                    ReservationIsInvalid) as e:
                return response(str(e), 400)
            except KeyError as e:
                return response(f'{str(e)} is required', 400)
            except DatabaseCommunicationIssue as e:
                return response(str(e), 500)

        return wrapper

    return decorator


class UserApi:

    @handle_request()
    def create_user(self, storage_type, user_payload):
        user = StorageLayer(storage_type, user_payload).create_user(user_dict=user)
        return user

    @handle_request()
    def list_users(self):
        user_list = UserService().user_service.list_users()
        return user_list

    @handle_request()
    def delete_user(self, user_id):
        return UserService().delete_user(user_id)

    @handle_request()
    def update_user(self, new_user, user_id):
        new_user = UserService().update_user(user_id=user_id, new_user=new_user)
        return new_user

    @handle_request()
    def get_user(self, user_id):
        user = UserService().get_user(user_id)
        return user
