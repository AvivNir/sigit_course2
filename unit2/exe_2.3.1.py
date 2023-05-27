class Dog:
    count_animals = 0  # Class variable to count the number of animals

    def __init__(self, name="Octavio", age=0):
        self._name = name
        self._age = age
        Dog.count_animals += 1

    def birthday(self):
        self._age += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


if __name__ == '__main__':
    yossi = Dog("Yossi")
    octavio = Dog()

    print(yossi.get_name())
    print(octavio.get_name())

    yossi.set_name("Moshiko")

    print(yossi.get_name())
    print(Dog.count_animals)
