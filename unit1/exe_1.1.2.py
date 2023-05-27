

def double_letter(my_str):
    return ''.join(letter + letter for letter in my_str)


if __name__ == '__main__':
    print(double_letter("python"))