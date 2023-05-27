
def intersection(list_1, list_2):
    return list(set([a for a in list_1 if a in list_2]))


if __name__ == '__main__':
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
