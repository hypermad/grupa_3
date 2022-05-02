from functools import wraps
#
#
def decodator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper-ul a fost executat inainte de {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function
#
#
@decodator_function
def afisare():
    print("Functia a rulat")
#
#
# @decodator_function
# def afisare_informatii(nume, varsta):
#     print(f"afisare_informatii a rulat cu parametrii {nume}, {varsta}")
#
#
# afisare()
# print()
# afisare_informatii("Andrei", 99)


# afisare = decodator_function(afisare)
# print(afisare)


# afisare_informatii("Andrei", 99)
# print()
# afisare()
#
# import time
#
#
# def timp_executie(functie_originala):
#     @wraps(functie_originala)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = functie_originala(*args, **kwargs)
#         t2 = time.time() - t1
#         print(f"{functie_originala.__name__} a fost executata in {t2} secunde")
#         return result
#
#     return wrapper
#
#
# @timp_executie
# def afisare_informatii(nume, varsta):
#     time.sleep(1)
#     print(f"afisare_informatii a rulat cu parametrii {nume}, {varsta}")
#
#
# afisare_informatii("Andrei", 99)


def calcul_tva(functie):
    @wraps(functie)
    def tva_wrapper(*args):
        rezultat = functie(*args)
        pret_tva = rezultat * 1.09
        print(f"Pretul painii plus tva este {pret_tva}")
        return pret_tva

    return tva_wrapper


@calcul_tva
def pret_paine(suma):
    print(f"Pretul unei paini fara TVA este {suma}")
    return suma


a = pret_paine(10)
print(a)
