class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "UnderAge: Your age is " + str(self.age) + ". In " + str(18 - self.age) + " year, you'll be able to reach Ido's birthday!"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(str(e))


if __name__ == '__main__':
    send_invitation("Aviv", 17)
    send_invitation("Nir", 20)
