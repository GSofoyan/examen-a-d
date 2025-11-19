from vbexa_speler_pass import Player
from vbexa_speler_pass import Pass

class PassGraph:
    def __init__(self,path_name:str =None):
            self.players = []
            self.adj={}
            if path_name is not None:
                self.lees_in(path_name)

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

    def player(self):
        kopie =[]
        for speler in self.players:
            kopie.append(speler)

        return kopie
    def passes(self):
        alle=[]
        for speler in self.adj:
            for pas in self.adj[speler]:
                alle.append(pas)

        return alle

    def lees_in(self,path_name:str):
        try:
            file = open(path_name,'r')
        except:
            return f"File {path_name} doesnt excist."

        x= True
        line = file.readline()
        while "[PLAYERS]" not in line:
                line = file.readline()

        line=file.readline()

        while "[PASSES]"not in line:
            if line[0] == "#" or line == "":
                line = file.readline()
                continue

            else:
                lijst = line.strip().split(";")
                try:
                    self.add_player(Player(lijst[0].strip(),int(lijst[1].strip())))
                    line=file.readline()
                except ValueError as ex:
                    print(ex)

        line=file.readline()
        while line != "":
            if line[0] == "#":
                line = file.readline()
                continue
            else:
                lijst_1 =line.strip().split("->")
                lijst_1[0] = lijst_1[0].strip()
                lijst_1[1]= lijst_1[1].split(":")
                lijst_1[1][0]=lijst_1[1][0].strip()
                lijst_1[1][1]=lijst_1[1][1].strip()
                sender = self.get_player(lijst_1[0])
                receiver = self.get_player(lijst_1[1][0])
                nr_of_times = int(lijst_1[1][1])
                try:
                    self.add_pass(sender, receiver, nr_of_times)
                except ValueError as ex:
                    print(ex)

        file.close()

    def save_to_txt(self,path:str):
        file = open(path,"w")
        file.write("[PLAYERS]\n")
        for speler in self.players:
            file.write(f"{speler.name};{speler.nr}\n")

        file.write("[PASSES]\n")
        for pas in self.passes():
            file.write(f"{pas.sender.name}->{pas.receiver.name}:{pas.nr_of_times}\n")

        file.close()













