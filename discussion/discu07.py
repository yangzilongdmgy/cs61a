from lzma import _OpenBinaryWritingMode


class Email:
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
    
class Server:
    def __init__(self):
        self.clients = {}
    
    def send(self, email):
        pass
    
    def register_client(self, client, client_name):
        self.clients[client_name] = client



class Pet:

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print('This Dog says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner)
        self.lives = lives

    def talk(self):
        print(self.name, " says meow!")

    def lose_life(self):
        if self.lives <= 0:
            print("This cat has no more lives to lose.")
        else:
            self.lives -= 1
            if self.lives <= 0:
                self.is_alive = False

class NoisyCat(Cat):
    def talk(self):
        super().talk()
        super().talk()