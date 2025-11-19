class Player:
    def __init__(self, name, nr):
        self.name = name
        self.nr = nr

    def __eq__(self, other):
        return isinstance(other,Player) and self.name ==other.name and self.nr == other.nr

class Pass:
    def __init__(self,sender : Player,receiver : Player,nr_of_times: int):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = nr_of_times

    def get_weight(self):
        return self.nr_of_times

    def get_start(self):
        return self.sender
    def get_end(self):
        return self.receiver
    def __eq__(self, other):
        return isinstance(other,Pass) and (self.sender == other.sender and self.receiver == other.receiver)

    def __str__(self):
        return f"Pass from <{self.sender}> to <{self.receiver}>"

Hz=Player("Hazard", 10)
KDB=Player("KDB", 7)
Luk=Player("Lukaku", 9)
P1 = Pass(KDB,Luk,3)
P2 = Pass(Hz,Luk,2)
P3 = Pass(KDB,Luk,7)
print(P1.__eq__(P3))
print(P2.__eq__(P3))
