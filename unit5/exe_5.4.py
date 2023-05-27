def check_id_valid(id_number):
    """
      Checks the validity of an ID number

      Parameters:
      - id_number (int): The ID number to be checked

      Returns:
      - bool: True if the ID number is valid, False otherwise
    """
    # first stage
    digits = [int(d) for d in str(id_number)]
    multiplied_digits = [digits[i] * (1 if i % 2 == 0 else 2) for i in range(len(digits))]
    # second stage
    summed_digits = [n if n <= 9 else (n // 10) + (n % 10) for n in multiplied_digits]
    # third stage
    total_sum = sum(summed_digits)
    # fourth stage
    return total_sum % 10 == 0


class IDIterator:
    """
      Iterator class for generating valid ID numbers

      Parameters:
      - _id (int): The current ID number
    """

    # Initializes the IDIterator object
    def __init__(self, id_):
        self._id = id_

    # Returns the iterator object
    def __iter__(self):
        return self

    def __next__(self):
        """
        Returns the next valid ID number

        Raises:
        - StopIteration: If the end of the range (999999999) is reached
        """

        if self._id >= 999999999:
            raise StopIteration
        self._id += 1
        while not check_id_valid(self._id):
            self._id += 1
        return self._id


def id_generator(id_number):
    """
        Generator function for generating valid ID numbers

        Parameters:
        - id_number (int): The starting ID number

        Yields:
        - int: The next valid ID number
    """
    while id_number < 999999999:
        id_number += 1
        while not check_id_valid(id_number):
            id_number += 1
        yield id_number


def main():
    # part 1
    # print(check_id_valid(123456780))
    # print(check_id_valid(123456782))

    # part 2
    # id_number = int(input("Enter ID: "))
    # id_iterator = IDIterator(id_number)
    # for i in range(10):
    #     print(next(id_iterator))

    # part 3
    # id_number = int(input("Enter ID: "))
    # id_gen = id_generator(id_number)
    # for i in range(10):
    #     print(next(id_gen))

    id_number = int(input("Enter ID: "))
    choice = input("Generator or Iterator? (gen/it)? ")

    # ask for input until valid choice
    while choice != "gen" and choice != "it":
        print("Please enter 'gen' or 'it'.")
        choice = input("Generator or Iterator? (gen/it)? ")

    if choice == "gen":
        id_gen = id_generator(id_number)
        id_numbers = [next(id_gen) for _ in range(10)]

    elif choice == "it":
        id_iter = IDIterator(id_number)
        id_numbers = [next(id_iter) for _ in range(10)]

    else:
        return

    # print the id numbers
    for number in id_numbers:
        print(number)


if __name__ == '__main__':
    main()
