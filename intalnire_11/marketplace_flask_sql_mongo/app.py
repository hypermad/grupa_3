import json

from flask import Flask, Response, request
from utilizatori.functii import (listeaza_utilizator_flask, adauga_un_utilizator_flask, adauga_utilizator_in_sql_db,
                                 listeaza_toti_utilizatorii_flask,
                                 sterge_un_utilizator_flask)
from comenzi.functii import (listeaza_comanda_flask, adauga_o_comanda_flask, listeaza_toate_comenzile_flask,
                             sterge_o_comanda_flask)
from produse.functii import (listeaza_produs_flask, adauga_un_produs_flask, listeaza_toate_produsele_flask,
                             sterge_un_produs_flask)

from baza_de_date.sql import SQLiteDatabaseConnection

app = Flask("Marketplace API")


if __name__ == "__main__":
    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()
    app.run()