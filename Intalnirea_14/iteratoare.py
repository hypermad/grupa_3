"""

Interesting iterator stuff: https://docs.python.org/3/library/itertools.html

"""

lista_simpla = [1, 2, 6, 9, 5]
tupla_simpla = (1, 2, 6, 9, 5)
# for item in lista_simpla:
#     print(item)

iterator_lista_simpla = iter(lista_simpla)
iterator_tupla_simpla = iter(tupla_simpla)


# print(type(iterator_lista_simpla))
# print(type(iterator_tupla_simpla))
#
# print(next(iterator_lista_simpla))
# print(next(iterator_lista_simpla))
# print(next(iterator_tupla_simpla))
# print(next(iterator_tupla_simpla))

def example_iteration():
    iterable_value = 'Andrei'
    iterable_obj = iter(iterable_value)
    while True:
        try:
            # Iterate by calling next
            item = next(iterable_obj)
            print(item)
        except StopIteration:
            # exception will happen when iteration will be over
            break


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a > 8:
            raise StopIteration
        x = self.a
        self.a += 1
        return x


if __name__ == "__main__":
    # my_numbers = MyNumbers()
    # my_numbers_iter = iter(my_numbers)
    # print(next(my_numbers_iter))
    # print(next(my_numbers_iter))
    # print(next(my_numbers_iter))
    # my_numbers.a += 1
    # print(next(my_numbers_iter))
    # example_iteration()
    # for item in MyNumbers():
    #     print(item)
    from math import sqrt

    """
    exemplu utilizare
    """
    def check_prime(number):
        for divisor in range(2, int(sqrt(number) + 1)):
            if number % divisor == 0:
                return False
        return True


    class Primes:
        def __init__(self, max):
            self.max = max
            self.number = 1

        def __iter__(self):
            return self

        def __next__(self):
            self.number += 1

            if self.number >= self.max:
                raise StopIteration
            elif check_prime(self.number):
                return self.number
            else:
                return self.__next__()

    # primes = Primes(1000)
    # for item in primes:
    #     print(item)

