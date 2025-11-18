class Verkeerslicht:
    def __init__(self, toestand = "rood"):
        if (toestand == "rood" or toestand == "groen" or toestand == "oranje"):
            self.toestand = toestand
        else:
            print("error")



    def __str__(self):
        return f"{self.toestand}"
    def __repr__(self):
        return f"Verkeerslicht('{self.toestand}')"
    def volgende(self):
        if self.toestand == "rood":
            self.toestand = "groen"
            return None
        if self.toestand == "groen":
            self.toestand = "oranje"
            return None
        if self.toestand == "oranje":
            self.toestand = "rood"
            return None

