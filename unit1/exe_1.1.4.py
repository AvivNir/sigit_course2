import functools


def sum_of_digits(number):
    return functools.reduce(lambda a, b: int(a) + int(b), str(number), 0)


if __name__ == '__main__':
    print(sum_of_digits(104))
