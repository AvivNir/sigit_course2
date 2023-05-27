def decypher():
    password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
    decrypted_password = ''.join(chr(ord(char) + 2) for char in password)
    print(decrypted_password)


if __name__ == '__main__':
    decypher()
    # unlock"with"the"code<"nine"four"one"two
