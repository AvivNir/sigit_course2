import functools


def longest_name():
    """
        Prints the longest name in the file.

        Reads the names from the file "D:\Desktop\python\names.txt"
        ,finds the longest name and prints it.
    """
    text = open("D:\Desktop\python\\names.txt").read().split()
    print(max(text, key=len))


def length_sum():
    """
       Prints the sum of the lengths of names in the file.

       Reads the names from the file "D:\Desktop\python\names.txt"
       and calculates the sum of their lengths and prints it.
    """
    text = open("D:\Desktop\python\\names.txt").read().split()
    print(functools.reduce(lambda x, y: x + y, map(len, text)))


def shortest_names():
    """
        Prints the shortest names in the file.

        Reads the names from the file "D:\Desktop\python\names.txt"
        and finds the shortest name/s.
        Prints the shortest name/s to the console, with each name on a new line.
    """
    text = open("D:\Desktop\python\\names.txt").read().split()
    print('\n'.join([name for name in text if len(name) == len(min(text, key=len))]))


def length_file():
    """
       Writes the lengths of names to a file.

       Reads the names from the file "D:\Desktop\python\names.txt"
       and writes the lengths of the names to a new file lengths.txt.
       Each length is written on a new line in the output file.
    """
    new_file = open("D:\Desktop\python\\lengths.txt", "w")
    names = open("D:\Desktop\python\\names.txt").read().split()
    [new_file.write(str(length) + "\n") for length in list(map(lambda name: len(name), names))]


def all_len_name():
    """
      Prints names with a specific length.

      Asks the user to enter a name length.
      Reads the names from the file "D:\Desktop\python\names.txt"
      and prints the names that have the specified length.
    """

    length = int(input("please enter the name's length "))
    names = open("D:\Desktop\python\\names.txt").read().split()
    [print(name) for name in names if len(name) == length]


def main():
    longest_name()
    length_sum()
    shortest_names()
    length_file()
    all_len_name()


if __name__ == '__main__':
    main()
