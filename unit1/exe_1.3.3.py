
def is_funny(string):
    return all(x == 'h' or x == 'a' for x in string)


if __name__ == '__main__':
    print(is_funny("hahahahahaha"))
    print(is_funny("453dsfsdf45"))
