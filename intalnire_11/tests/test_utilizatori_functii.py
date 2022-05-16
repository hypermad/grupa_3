from utilizatori.functii import listeaza_utilizator_flask


def test_listeaza_utilizator_flask_not_found(mocker):
    mocker.patch("utilizatori.functii.citeste_datele_din_baza_de_date", return_value={"utilizatori": {}})
    result = listeaza_utilizator_flask("id")
    assert result[0] == 404
    assert result[1] == "Utilizator-ul id nu se afla in baza de date"


def test_listeaza_utilizator_flask_valid_response(mocker, get_user_information):
    mocker.patch("utilizatori.functii.citeste_datele_din_baza_de_date",
                 return_value={"utilizatori": {"123456789": get_user_information}})
    status, message = listeaza_utilizator_flask("123456789")
    assert status == 200
    assert message == get_user_information
