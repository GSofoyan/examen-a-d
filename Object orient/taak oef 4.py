class BankRekening:
    def __init__(self, naam, rn,bedrag=0):      #standaaard waarde geven maakt het optioneel

        self.naam=naam
        self.rn=rn
        self.bedrag=bedrag

    def __str__(self):
        return f"{self.naam}, {self.rn}, bedrag: {self.bedrag}"
    def __repr__(self):
        return f"BankRekening('{self.naam}', '{self.rn}', {self.bedrag})"
    def storten(self,n):
        self.bedrag += n
    def afhalen(self,n):
        self.bedrag -= n

