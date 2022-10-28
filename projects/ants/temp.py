from re import A


class Aaa:
    name = 'a'

    def __init__(self):
        self.num = 2
    
    def mix(self, b):
        return self.num * b

class Bbb(Aaa):
    name = 'b'

    def __init__(self):
        self.num = 3

    def mix(self, b):
        return super().mix(b)