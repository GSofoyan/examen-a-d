class Geld:
    def __init__(self,bedrag):
        self.bedrag=bedrag
        if type(self.bedrag) == int:
            self.centen=0
            self.euros=self.bedrag
        if type(self.bedrag) == float:
            if self.bedrag<0:
                print("Negatieve bedragen zijn niet toegelaten")

            else:
                str_bedr= str(self.bedrag)  #omzetten naar string om komma te zoeken
                index_komma= str_bedr.find('.')     #bij float is een komma een punt
                self.centen= int(str_bedr[index_komma +1:])
                self.euros=int(str_bedr[:index_komma])
        if type(self.bedrag) == Geld:
            self.centen= self.bedrag.centen
            self.euros=self.bedrag.euros
        if type(self.bedrag) == str:
            if "€" in self.bedrag and "," in self.bedrag:     #als de string juiste vorm heeft
                index_comma = self.bedrag.find(',')
                self.centen= int(self.bedrag[index_comma+1:])
                self.euros=int(self.bedrag[1:index_comma])   #van de 2e element (1e=€)
            else:
                print("Opmaak Geld string niet correct")
                self.centen=0       #verbetering wou het zo lol
                self.euros=0
    def get_centen(self):
        return self.centen
    def get_euros(self):
        return self.euros

    def __str__(self):
        if self.centen >9:
            return "€"+str(self.euros)+"."+str(self.centen)
        else:
            return (f"€{self.euros}.{self.centen}0")    #als bv. €100.5  zal .centen = "5" zijn (is kleiner dan "10" zie "if" statement)
                                                        #daardoor kom je in "else" deel, en daar plak je "0" achter zodat het €100.50 toont
    def vermenigvuldig(self, n):
        multiplied_money = Geld(n*self.bedrag)     #van uitkomst ook geld object maken
        return multiplied_money
    def optellen(self,andere_bedrag):
        som=(andere_bedrag.bedrag + self.bedrag)
        sum_money = Geld(som)
        return sum_money

