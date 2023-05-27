from file1 import GreetingCard as gc
from file2 import BirthdayCard as bc


def main():
    birthday_card = gc()
    greeting_card = bc()
    print("Your greeting card:")
    greeting_card.greeting_msg()
    print(" \nYour birthday card:")
    birthday_card.greeting_msg()


if __name__ == '__main__':
    main()
