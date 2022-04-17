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


def adauga_o_comanda_flask(order_name, order_quantity):
    id_comanda = genereaza_id({order_name: order_quantity})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["comenzi"][id_comanda] = {
        "order_name": order_name,
        "order_quantity": order_quantity,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)
    return id_comanda


def modifica_comanda():
    datele = citeste_datele_din_baza_de_date()
    identificator_de_sters = input("Introduceți identificatorul comenzii care se modifica: ")
    while True:
        actiune = input(
            "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
        detalii_comanda = datele["comenzi"][identificator_de_sters]["detalii_comanda"]
        if actiune == 'a':
            add_prod = input("Introduceti produsul:")
            add_cant = input("Introduceti cantitatea:")
            detalii_comanda[add_prod] = add_cant
        elif actiune == 'm':
            add_prod = input("Introduceti produsul:")
            add_cant_noua = input("Introduceti cantitatea noua la acest produs")
            detalii_comanda[add_prod] = add_cant_noua
        elif actiune == 's':
            sterge_prod = input("Stergeti produsul:")
            detalii_comanda.pop(sterge_prod)
        else:
            print("Nu ati ales nici o actiune!")
            break


def listeaza_toate_comenzile_flask():
    datele = citeste_datele_din_baza_de_date()
    comenzi = datele.get('comenzi')
    if len(comenzi) > 0:
        return 200, comenzi
    else:
        return 404, "Nu exista comenzi"


def sterge_o_comanda_flask(order_id):
    return sterge(order_id, "comenzi")
