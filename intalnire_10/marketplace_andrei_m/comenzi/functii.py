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
from pprint import pprint
from pytz import country_timezones, timezone

from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from common.utils import genereaza_id, sterge


def adauga_o_comanda():
    detalii_comanda = {}
    print("Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n")
    while True:
        id_produs = input(" Produsul: ")
        if id_produs == "stop":
            break
        else:
            CantitateProdus = input(" Cantitatea: ")
            detalii_comanda[id_produs] = CantitateProdus

    id_comanda = genereaza_id(detalii_comanda)
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["comenzi"][id_comanda] = {
        "detalii_comanda": detalii_comanda,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)


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


def listeaza_toate_comenzile():
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzilor
    """

    datele = citeste_datele_din_baza_de_date()
    comenzi = datele.get('comenzi')
    if len(comenzi) > 0:
        pprint(comenzi)
    else:
        print("Nu exista comenzi")


def sterge_o_comanda():
    sterge(input("\nIntroduceți identificatorul comenzii de sters: "),
           "comenzi")


