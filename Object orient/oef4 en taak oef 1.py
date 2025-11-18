from datetime import datetime


class Persoon:
    def __init__(self,naam, voornaam, woonplaats, jaar_geboorte_datum, maand_geboorte_datum, dag_geboorte_datum):
        self.naam = naam
        self.voornaam = voornaam
        self.woonplaats = woonplaats
        self.geboorte_datum = datetime.date(jaar_geboorte_datum,maand_geboorte_datum,dag_geboorte_datum)    #je geeft aan deze module Y,M,D en geeft de datum

    def get_naam(self):
        return self.naam

    def get_voornaam(self):
        return self.voornaam

    def get_woonplaats(self):
        return self.woonplaats

    def get_geboorte_datum(self):
        return self.geboorte_datum

    def set_voornaam(self, new_voornaam):
        self.voornaam = new_voornaam

    def set_woonplaats(self, new_woonplaats):
        self.woonplaats = new_woonplaats

    def is_ouder_dan(self, other_persoon):
        if self.geboorte_datum==other_persoon.geboorte_datum:
            return False
        if self.geboorte_datum<other_persoon.geboorte_datum:            #ouder dus geboortedatum is kleiner
            return True
        else:
            return False

    def is_jonger_dan(self, other_persoon):
        if self.geboorte_datum==other_persoon.geboorte_datum:
            return False
        if self.geboorte_datum>other_persoon.geboorte_datum:
            return True
        else:
            return False

    def wonen_in_zelfde_stad(self, other_persoon):
        if self.woonplaats==other_persoon.woonplaats:
            return True
        else:
            return False


