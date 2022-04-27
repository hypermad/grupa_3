"""

Produsele ar trebui sa aiba structura:
("id_produs": {
    "nume_produs": "NumeleProdusului" - string,
    "pret": "Pret" - intreg/float,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
from datetime import datetime

from pytz import country_timezones, timezone

from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from common.utils import genereaza_id, sterge


def listeaza_produs_flask(id_produs):
    datele = citeste_datele_din_baza_de_date()
    if datele["produse"].get(id_produs):
        return 200, datele["produse"].get(id_produs)
    else:
        return 404, f"Produsul {id_produs} nu se afla in baza de date"


def adauga_un_produs_flask(request_body):
    id_produs = genereaza_id({request_body["order_name"]: request_body["order_quantity"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["produse"][id_produs] = {
        "nume_produs": request_body["order_name"],
        "pret": request_body["order_quantity"],
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)
    return id_produs


def listeaza_toate_produsele_flask():
    datele = citeste_datele_din_baza_de_date()
    produse = datele.get('produse')
    if len(produse) > 0:
        return 200, produse
    else:
        return 404, "Nu exista produse"


def sterge_un_produs_flask(product_id):
    return sterge(product_id, "produse")
