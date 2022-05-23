"""
Ce face functia si ce va returna/afisa ?
"""


def question_1():
    names = ['Chris', 'Jack', 'John', 'Daman']
    print(names[-1][-1])


def question_2():
    animals = [
        {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
        {'type': 'elephant', 'name': 'Devon', 'age': 3},
        {'type': 'puma', 'name': 'Moe', 'age': 5}
    ]
    print(sorted(animals, key=lambda animal: animal['age'], reverse=True))


def question_3():
    a = 5
    b = 5
    if a == b:
        print("egale")
    b += 1
    if a is b:
        print("identice")


def question_4():
    class DummyClass:
        pass

    rezultat = [DummyClass()] * 3
    alt_rezultat = [DummyClass() for _ in range(0, 3)]

    print(rezultat)
    print(alt_rezultat)


if __name__ == "__main__":
    question_4()
