class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


if __name__ == '__main__':
    zoie = Dog("zoie", 3)
    walle = Dog("walle", 5)

    zoie.birthday()

    print(zoie.get_age())
    print(walle.get_age())
