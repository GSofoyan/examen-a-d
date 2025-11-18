class Vertegenwoordiger:
    def __init__(self,naam="",omzet=0.0):
        self.naam=str(naam)
        self.omzet=float(omzet)

    def getNaam(self):
        return self.naam
    def getOmzet(self):
        return self.omzet

    def setOmzet(self,omzet):
        self.omzet=float(omzet)

    def setNaam(self,naam):
        self.naam=str(naam)



    def __str__(self):
        return f"Vertegenwoordiger[naam='{self.naam}', omzet={self.omzet:.2f}]"
