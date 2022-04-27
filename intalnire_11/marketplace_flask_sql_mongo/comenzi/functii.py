"""
Comenzile ar trebui sa aiba structura:
("id_comanda": {
    "id_comanda": "Idcomanda" - string,
    "detalii_comanda":
        [{"IdProdus": CantitateProdus}]
        - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
    "data_inregistrare": "DataInregistrare" - string,
})

"""
from datetime import datetime
from pytz import country_timezones, timezone

from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from common.utils import genereaza_id, sterge


def listeaza_comanda_flask(id_comanda):
    datele = citeste_datele_din_baza_de_date()
    if datele["comenzi"].get(id_comanda):
        return 200, datele["comenzi"].get(id_comanda)
    else:
        return 404, f"Comanda {id_comanda} nu se afla in baza de date"


def adauga_o_comanda_flask(request_body):
    id_comanda = genereaza_id({request_body["order_name"]: request_body["order_quantity"]})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["comenzi"][id_comanda] = {
        "order_name": request_body["order_name"],
        "order_quantity": request_body["order_quantity"],
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)
    return id_comanda


def listeaza_toate_comenzile_flask():
    datele = citeste_datele_din_baza_de_date()
    comenzi = datele.get('comenzi')
    if len(comenzi) > 0:
        return 200, comenzi
    else:
        return 404, "Nu exista comenzi"


def sterge_o_comanda_flask(order_id):
    return sterge(order_id, "comenzi")
