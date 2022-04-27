import os
from pathlib import Path
import logging

from sqlalchemy.ext.declarative import declarative_base


def calea_catre_baza_de_date():
    calea_catre_fisierul_de_baze_de_date = Path(
        os.path.dirname(os.path.abspath(__file__)),
        "marketplace.json"
    )
    return calea_catre_fisierul_de_baze_de_date


logging.basicConfig(level=logging.ERROR,
                    format="%(asctime)s - %(module)s::%(funcName)s - [%(levelname)s] - %(message)s")
logger = logging.getLogger("LibraryBackend")

Base = declarative_base()
