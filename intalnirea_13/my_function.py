def matematica(a=None, b=None):
    if not a and not b:
        return "Trebuie specificate 2 numere"
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Valorile introduse trebuie sa fie numere"
    else:
        print("hello")
        return a + b
