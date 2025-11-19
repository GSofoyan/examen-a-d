from vbexa_speler_pass import Player
from vbexa_speler_pass import Pass

class PassGraph:
    def __init__(self):
        self.players = []
        self.adj={}

    def add_player(self, player):
        for speler in self.players:
            if speler.name == player.name:
                return None
        self.players.append(player)
        self.adj[player.name] = []

    def has_player(self, player):
        if isinstance(player, Player):
            player = player.name

        if player in self.adj:
            return True

    def get_player(self, player: str):
        for speler in self.players:
            if speler.name == player:
                return speler
        return None

    def add_pass(self,sender:Player, receiver:Player, nr_of_times :int =1):
        if sender not in self.players or receiver not in self.players:
            return None
        if nr_of_times <= 0:
            return None
        NewPass = Pass(sender, receiver, nr_of_times)
        for speler in self.adj:
            if speler == sender.name:
                for pas in self.adj[speler]:
                    if pas.__eq__(NewPass):
                        pas.nr_of_times += nr_of_times
                        return None

                self.adj[speler].append(NewPass)
                return None

    def get_pass(self, sender_name, receiver_name):
        if sender_name not in self.adj or receiver_name not in self.adj:
            return None

        for speler in self.adj:
            if speler == sender_name:
                for pas in self.adj[speler]:
                    naam =pas.receiver
                    if pas.receiver.name == receiver_name:
                        return pas

                return None

    def neighbors(self, sender_name):
        if sender_name not in self.adj:
            return []

        for speler in self.adj:
            if speler == sender_name:
                return self.adj[speler]

    def pass_intensity(self, sublist: list[str] | None = None) -> float:
        totaal_passen = 0
        for speler in self.adj:
            if speler in sublist:
                for pas in self.adj[speler]:
                    if pas.receiver.name in sublist:
                        totaal_passen += pas.nr_of_times

        noemer = len(sublist) *(len(sublist)-1)

        return totaal_passen/noemer

    def top_pairs(self,k :int =5):
        top = []
        while k > 0:
            maxi = 0
            for speler in self.adj:
                for pas in self.adj[speler]:
                    if pas not in top:
                        if pas.nr_of_times > maxi:
                            maxi = pas.nr_of_times
                            grootste = pas

            top.append(grootste)
            k -= 1

        return top

    def distribution_from(self,sender_name:str):
        if sender_name not in self.adj:
            return None
        lijst=[]
        for speler in self.adj:
            if speler == sender_name:
                for pas in self.adj[speler]:
                    lijst.append([pas.nr_of_times,pas.receiver.name])
        lijst.sort(reverse=True)
        return [(naam,count) for [count,naam] in lijst]







x= PassGraph()
Hz=Player("Hazard", 10)
KDB=Player("KDB", 7)
Luk=Player("Lukaku", 9)
BigG=Player("Gevorg", 17)
x.add_player(Hz)
x.add_player(KDB)
x.add_player(Luk)
x.add_player(BigG)
x.add_pass(KDB,Luk,3)
x.add_pass(Hz,Luk,2)
x.add_pass(KDB,Luk,7)
x.add_pass(BigG,Hz,4)
x.add_pass(Hz,BigG,5)
x.add_pass(Luk,KDB,6)
x.add_pass(Hz,Luk,100)
print(x.distribution_from("Hazard"))













