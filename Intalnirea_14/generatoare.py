def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


if __name__ == "__main__":
    for item in my_gen():
        print(item)

    for char in rev_str("hello"):
        print(char)

    # my_list = [1, 3, 6, 10]
    # list_ = [x ** 2 for x in my_list]
    # generator = (x ** 2 for x in my_list)

    # print(next(generator))
