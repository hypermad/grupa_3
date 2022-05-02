"""
Singleton pattern example.
"""


class SingletonClass:
    __instance = None
    sector = "IT"

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


if __name__ == "__main__":
    print()
    a = SingletonClass("Andrei")
    print(a.name)
    print(a.sector)
    print()
    m = SingletonClass("Mihai")
    print(m.name)
    print(a.name)
    c = SingletonClass("Cristi")
    print(c.name)
    print(a.name)
    print(m.name)
    print(m)
    print(id(m))
    print(a)
    print(id(a))
    print(c)
    print(id(c))
