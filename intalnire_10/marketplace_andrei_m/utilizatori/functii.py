"""

Utilizatorii ar trebui sa aiba structura:
("id_utilizator": {
    "nume": "Numele" - string,
    "email": "EmailAddress" - string,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
from datetime import datetime
from pprint import pprint

from pytz import country_timezones, timezone

from database.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from common.utils import genereaza_id, sterge


def listeaza_utilizator_flask(id_utilizator):
    datele = citeste_datele_din_baza_de_date()
    if datele["utilizatori"].get(id_utilizator):
        return 200, datele["utilizatori"].get(id_utilizator)
    else:
        return 404, f"Utilizator-ul {id_utilizator} nu se afla in baza de date"


def adauga_un_utilizator():
    nume, email = "", ""
    while len(nume) < 1 or len(nume) > 50:
        nume = input("Introduceti numele utilizatorului:\n")
        if len(nume) < 1 or len(nume) > 50:
            print("Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere")
    while len(email) < 1:
        email = input("Introduceti emailul utilizatorului:\n")

    id_utilizator = genereaza_id({nume: email})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["utilizatori"][id_utilizator] = {
        "nume": nume,
        "email": email,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)





def adauga_un_utilizator_flask(user_name, email_address):
    id_utilizator = genereaza_id({user_name: email_address})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["utilizatori"][id_utilizator] = {
        "nume": user_name,
        "email": email_address,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)
    return id_utilizator


def listeaza_toti_utilizatorii():
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    :return:
    """
    datele = citeste_datele_din_baza_de_date()
    utilizatori = datele.get('utilizatori')
    if len(utilizatori) > 0:
        pprint(utilizatori)
    else:
        print("Nu exista utilizatori")


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


def sterge_un_utilizator():
    sterge(input("\nIntroduceti identificatorul utilizatorului de sters: "), "utilizatori")


def sterge_un_utilizator_flask(user_id):
    return sterge(user_id, "utilizatori")
