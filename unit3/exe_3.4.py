import string


def checkPassword(password):
    """
       Checks if a password meets certain requirements.

       Parameters:
       - password (str): The password to be checked.

       Raises:
       - PasswordMissingUppercase: If the password does not contain any uppercase letters.
       - PasswordMissingLowercase: If the password does not contain any lowercase letters.
       - PasswordMissingDigit: If the password does not contain any digits.
       - PasswordMissingSpecial: If the password does not contain any special characters.

       Returns:
       - bool: True if the password meets all the requirements.
       """
    if not any(c.isupper() for c in password):
        raise PasswordMissingUppercase()
    elif not any(c.islower() for c in password):
        raise PasswordMissingLowercase()
    elif not any(c.isdigit() for c in password):
        raise PasswordMissingDigit()
    elif not any(c in string.punctuation for c in password):
        raise PasswordMissingSpecial()
    return True


def check_input(username, password):
    """
      Check if the provided username and password meet the specified conditions.

      Parameters:
      - username (str): The username to be checked.
      - password (str): The password to be checked.

      Raises:
      - UsernameContainsIllegalCharacter: If the username contains illegal characters.
      - UsernameTooShort: If the username is too short.
      - UsernameTooLong: If the username is too long.
      - PasswordTooShort: If the password is too short.
      - PasswordTooLong: If the password is too long.
      - PasswordMissingCharacter: If the password is missing a mandatory character.

    """
    legal_characters = string.ascii_letters + string.digits + '_'
    if any(char not in legal_characters for char in username):
        illegal_character = next(char for char in username if char not in legal_characters)
        position = username.index(illegal_character)
        raise UsernameContainsIllegalCharacter(illegal_character, position)

    elif len(username) < 3:
        raise UsernameTooShort

    elif len(username) > 16:
        raise UsernameTooLong

    elif len(password) < 8:
        raise PasswordTooShort

    elif len(password) > 40:
        raise PasswordTooLong

    flag = checkPassword(password)

    if flag:
        print("OK")


class UsernameContainsIllegalCharacter(Exception):
    """
      Exception raised when the username contains illegal characters.
    """

    def __init__(self, illegal_character, position):
        self.illegal_character = illegal_character
        self.position = position

    def __str__(self):
        return "The username contains an illegal character " + self.illegal_character + " at index " + self.position


class UsernameTooShort(Exception):
    """
       Exception raised when the username is too short.
    """


class UsernameTooLong(Exception):
    """
       Exception raised when the username is too long.
    """


class PasswordMissingCharacter(Exception):
    """
       Exception raised when the password is missing a mandatory character.
    """
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    """
       Exception class representing a missing uppercase character in the password.
       Inherits from PasswordMissingCharacter.
    """
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingLowercase(PasswordMissingCharacter):
    """
       Exception class representing a missing lowercase character in the password.
       Inherits from PasswordMissingCharacter.
    """
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingDigit(PasswordMissingCharacter):
    """
      Exception class representing a missing digit character in the password.
      Inherits from PasswordMissingCharacter.
    """
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingSpecial(PasswordMissingCharacter):
    """
      Exception class representing a missing special character in the password.
      Inherits from PasswordMissingCharacter.
    """
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooShort(Exception):
    """
        Exception raised when the password is too short.
        """


class PasswordTooLong(Exception):
    """
        Exception raised when the password is too long.
    """


def main():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            check_input(username, password)
            break
        except UsernameContainsIllegalCharacter as e:
            print(str(e))
        except UsernameTooShort :
            print("The username is too short")
        except UsernameTooLong:
            print("The username is too long")
        except PasswordMissingCharacter as e:
            print(str(e))
        except PasswordTooShort:
            print("The password is too short")
        except PasswordTooLong:
            print("The password is too long")


if __name__ == '__main__':
    main()
