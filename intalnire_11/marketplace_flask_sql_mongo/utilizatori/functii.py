"""

Utilizatorii ar trebui sa aiba structura:
("id_utilizator": {
    "nume": "Numele" - string,
    "email": "EmailAddress" - string,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
from datetime import datetime
from pytz import country_timezones, timezone
from common.utils import genereaza_id, sterge
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date


def listeaza_utilizator_flask(id_utilizator):
    datele = citeste_datele_din_baza_de_date()
    if datele["utilizatori"].get(id_utilizator):
        return 200, datele["utilizatori"].get(id_utilizator)
    else:
        return 404, f"Utilizator-ul {id_utilizator} nu se afla in baza de date"


def adauga_un_utilizator_flask(request_body):
    id_utilizator = genereaza_id({request_body["user_name"]: request_body["email_address"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["utilizatori"][id_utilizator] = {
        "nume": request_body["user_name"],
        "email": request_body["email_address"],
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)
    return id_utilizator


def listeaza_toti_utilizatorii_flask():
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    :return:
    """
    datele = citeste_datele_din_baza_de_date()
    utilizatori = datele.get('utilizatori')
    if len(utilizatori) > 0:
        return 200, utilizatori
    else:
        return 404, "Nu exista utilizatori"


def sterge_un_utilizator_flask(user_id):
    return sterge(user_id, "utilizatori")
