from intalnirea_13.my_function import matematica
import pytest

def test_matematica_valid_output():
    rezultat = matematica(1, 2)
    assert rezultat == 3


def test_matematica_input_invalid():
    rezultat = matematica(1, "2")
    assert rezultat == "Valorile introduse trebuie sa fie numere"


def test_matematica_input__inexistent():
    rezultat = matematica()
    assert rezultat == "Trebuie specificate 2 numere"


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3),
                                            (1, "2", "Valorile introduse trebuie sa fie numere"),
                                            (None, None, "Trebuie specificate 2 numere"),
                                            (None, "3", "Valorile introduse trebuie sa fie numere")])
def test_matematica_input_1_input_invalid(a, b, expected):
    rezultat = matematica(a, b)
    assert rezultat == expected
