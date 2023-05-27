

def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, range(1, number)))


if __name__ == '__main__':
    print(four_dividers(3))
