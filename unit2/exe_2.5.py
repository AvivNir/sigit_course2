class Animal:
    """
      Represents an animal in the zoo.

      Parameters:
      - zoo_name (str): The name of the zoo. Shared by all instances of Animal.
      - _name (str): The name of the animal.
      - _hunger (int): The level of hunger of the animal.
    """
    zoo_name = "Hayaton"

    # Initializes an Animal instance with a name and hunger level.
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    # Returns the name of the animal.
    def get_name(self):
        return self._name

    # Checks if the animal is hungry.
    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    # Decreases the hunger level of the animal by 1.
    def feed(self):
        self._hunger = self._hunger - 1

    # Makes the animal talk.
    def talk(self):
        self.talk()

    # Performs a special action based on the animal type.
    def special(self):
        if isinstance(self, Dog):
            Dog.fetch_stick(self)

        elif isinstance(self, Cat):
            Cat.chase_laser(self)

        elif isinstance(self, Skunk):
            Skunk.stink(self)

        elif isinstance(self, Unicorn):
            Unicorn.sing(self)

        elif isinstance(self, Dragon):
            Dragon.breath_fire(self)


class Dog(Animal):
    """
        Represents a dog, a subclass of Animal.
    """

    # Makes the dog bark.
    def talk(self):
        print("woof woof")

    # Makes the dog fetch a stick.
    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    """
       Represents a cat, a subclass of Animal.
    """

    # Makes the cat meow.
    def talk(self):
        print("meow")

    # Makes the cat chase a laser.
    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    """
        Represents a skunk, a subclass of Animal.
    """

    # Makes the skunk make a sound.
    def talk(self):
        print("tsssss")

    # Makes the skunk emit a smell.
    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    """
      Represents a unicorn, a subclass of Animal.
    """

    # Makes the unicorn say a greeting.
    def talk(self):
        print("Good day, darling")

    # Makes the unicorn sing.
    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    """
       Represents a dragon, a subclass of Animal.
    """

    # Makes the dragon roar.
    def talk(self):
        print("Raaaawr")

    # Makes the dragon breathe fire.
    def breath_fire(self):
        print("$@#$#@$")


def main():
    lizzy_the_dragon = Dragon("Lizzy", 1450)
    brownie_the_dog = Dog("Brownie", 10)
    zelda_the_cat = Cat("Zelda", 3)
    stinky_the_skunk = Skunk("Stinky")
    keith_the_unicorn = Unicorn("Keith", 7)
    zoo_lst = []
    zoo_lst.extend([lizzy_the_dragon, brownie_the_dog, zelda_the_cat, stinky_the_skunk, keith_the_unicorn])
    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))

    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__ + " " + animal.get_name())
            animal.talk()
            animal.special()
        while animal.is_hungry():
            animal.feed()

    print("zoo name: " + Animal.zoo_name)


if __name__ == '__main__':
    main()
