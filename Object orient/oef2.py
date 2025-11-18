from datetime import datetime
class Rijksregisternummer:
    def __init__(self, rnn):
       #rnn moet valid zijn:
        assert type(rnn)==str, "ongeldig type"           #syntax voor assertation error

    #nu rijksregister vinden met enkel cijfers:
        rijksnummer = ""                                 #maak lege string om cijfers in te zetten
        for x in rnn:
            if x.isdigit():                             #als de character een digit is in rnn (=methode van een string)
                rijksnummer += str(x)                    #of =rijksnummer.join(x) (= de "append" voor een string)

       #hele stuk boven kon ook met : rijksnum = ''.join(x for x in rnn if x.isdigit()

        assert len(rijksnummer)== 11 or len(rijksnummer)==1 , f"ongeldig formaat ({len(rijksnummer)} cijfers)"     #als lengte = 1 moet hij niet deze error geven maar volgende
        assert len(rijksnummer)!= 1 , "ongeldig formaat (1 cijfer)"

    #  rnn is een string met cijfers die we hebben gevonden hierboven, nu toekennen
        self.rijksregisternummer=rijksnummer

    def __repr__(self):
        return f"Rijksregisternummer('{self.rijksregisternummer}')"
    def __str__(self):
        return f"{self.rijksregisternummer[:2]}.{self.rijksregisternummer[2:4]}.{self.rijksregisternummer[4:6]}-{self.rijksregisternummer[6:9]}.{self.rijksregisternummer[9:]}"     #jj.mm.dd-xxx.cc
    def geslacht(self):
        if int(self.rijksregisternummer[6:9]) % 2 ==0:
            return "vrouw"
        else:
            return "man"
    def controlegetal(self,y2k: bool = False):                     #zet standaard op false, zo is het optioneel
        if y2k==True:
            check_str= "2"+self.rijksregisternummer[:9]
            check_cijfer= int(check_str)
            controle_getal= 97-(check_cijfer % 97)
            return controle_getal

        else:
            check_cijfer = int(self.rijksregisternummer[:9])
            controle_getal = 97 - (check_cijfer % 97)
            return controle_getal
    def geboortedatum(self):

        assert int(self.rijksregisternummer[2:4]) <13 , "ongeldige geboortedatum"
        maand_31=["01","03","05","07","08","10","12"]
        maand_30=["04","06","09","11"]
        if self.rijksregisternummer[2:4] in maand_31 :
            assert int(self.rijksregisternummer[4:6])<32, "ongeldige geboortedatum"
        if self.rijksregisternummer[2:4] in maand_30 :
            assert int(self.rijksregisternummer[4:6])<31, "ongeldige geboortedatum"
        if self.rijksregisternummer[2:4] =="02" :
            assert int(self.rijksregisternummer[4:6])<30, "ongeldige geboortedatum"

        maand= self.rijksregisternummer[2:4]
        dag=self.rijksregisternummer[4:6]
        jaar=""
        if int(self.rijksregisternummer[9:])==self.controlegetal(True):     #is dan geboren na 2000 (jaar is 20xx)
            jaar+="20"+self.rijksregisternummer[:2]
        else:
            jaar+= "19"+self.rijksregisternummer[:2]
        maand_int = int(maand)
        dag_int = int(dag)
        jaar_int = int(jaar)

        return datetime.date(jaar_int,maand_int,dag_int)
    def geldig(self):

        #datum check
        if int(self.rijksregisternummer[2:4]) >12:
            return False
        maand_31 = ["01", "03", "05", "07", "08", "10", "12"]
        maand_30 = ["04", "06", "09", "11"]
        if self.rijksregisternummer[2:4] in maand_31 and int(self.rijksregisternummer[4:6])>31:
            return False
        if self.rijksregisternummer[2:4] in maand_30 and int(self.rijksregisternummer[4:6])>30:
            return False
        if self.rijksregisternummer[2:4] =="02" and int(self.rijksregisternummer[4:6])>29:
            return False

        #contole getal check
        if int(self.rijksregisternummer[9:]) != self.controlegetal(True) and int(self.rijksregisternummer[9:]) != self.controlegetal(False):
            return False

        return True







