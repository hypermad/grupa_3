from app_mongo import get_user


def test_get_user(mocker, mock_get_user):
    mocker.patch("app_mongo.listeaza_utilizator_flask_mongo", return_value=mock_get_user)
    result = get_user(None)
    assert result.status == "200 OK"
    assert result.data == b'{"nume": "yolo", "email": "yolo@gmail.com", "data_inregistrare": "2021-08-31T01:19:59.543850+03:00"}'

