class Verwarming:
    def __init__(self,naam : str, temperatuur = 10.0, minimum =0.0 , maximum =100.0  ):
        assert isinstance(naam,str), "naam must be of type str"
        assert isinstance(temperatuur,float) or isinstance(temperatuur,int), "temp must be of type float or int"
        assert isinstance(minimum,float) or isinstance(minimum,int), "mini must be of type float or int"
        assert isinstance(maximum,float) or isinstance(maximum,int), "mini must be of type float or int"

        self.naam = naam
        self.temp = temperatuur     #later komt methode "temperatuur" dus hier self.temp
        self.minimum = minimum       #anders is bij het aanroepen x.temperatuur een waarde en een methode
        self.maximum = maximum

    def __str__(self):
        return f"{self.naam}: huidige temperatuur: {self.temp:.1f}; toegelaten min: {self.minimum:.1f}; toegelaten max: {self.maximum:.1f}"
    def __repr__(self):
        return f"Verwarming('{self.naam}', {self.temp:.1f}, {self.minimum:.1f}, {self.maximum:.1f})"
    def wijzig_temperatuur(self, verandering):
        assert isinstance(verandering,float) or isinstance(verandering,int), "verander must be of type float or int"
        self.temp += verandering
        if self.temp > self.maximum:
            self.temp = self.maximum
        if self.temp < self.minimum:
            self.temp = self.minimum
    def temperatuur(self):
        return float(self.temp)



