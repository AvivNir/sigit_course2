class GreetingCard:
    def __init__(self, _recipient="Dana Ev", _sender="Eyal Ch"):
        self._recipient = _recipient
        self._sender = _sender

    def greeting_msg(self):
        print("name of the sender: " + self._sender + " \nname of the recipient " + self._recipient)




