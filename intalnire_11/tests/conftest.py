import pytest


@pytest.fixture
def mock_get_user():
    status = 200
    message = {
        "nume": "yolo",
        "email": "yolo@gmail.com",
        "data_inregistrare": "2021-08-31T01:19:59.543850+03:00"
    }
    return status, message


@pytest.fixture
def get_user_information():
    return {"nume": "yolo",
            "email": "yolo@gmail.com",
            "data_inregistrare": "2021-08-31T01:19:59.543850+03:00"
            }
