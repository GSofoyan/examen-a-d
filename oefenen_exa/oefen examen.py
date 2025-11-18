
#OEFENING OP KLASSEN

class Share:
    def __init__(self, symbol, quantity):
        assert quantity > 0.0, "Voeg juiste hoeveelheid toe aub"
        self.symbol = symbol
        self.quantity = quantity

class Wallet:
    def __init__(self):
        self.shares = []

    def add_share(self, symbool, hoeveelheid):
        self.shares.append(Share(symbool, hoeveelheid))

    def remove_share(self, symbool, hoeveelheid):
        for share in self.shares:
            if share.symbol == symbool:
                assert share.quantity >= hoeveelheid, "U hebt niet zoveel van dit aandeel"
                share.quantity -= hoeveelheid

    def get_share_quantity(self, symbool):
        for share in self.shares:
            if share.symbol == symbool:
                return share.quantity

    def get_portfolio_value(self, prijzen):
        value = 0.0
        for share in self.shares:
            for i in range(len(prijzen)):
                if prijzen[i][0] == share.symbol:
                    value += share.quantity * prijzen[i][1]
        return value


#ANDERE OEFENING


def annuiteit(bedrag,rente,jaren):
    return bedrag*rente/(1-(1+rente)**(-jaren))

def _aflossingstabel_rente(bedrag,rente,jaren):
    rentedeel = []
    openstaand = bedrag
    for i in range(0,jaren):
        rentedeel.append(openstaand*rente)
        aflossing = annuiteit(bedrag,rente,jaren)- openstaand*rente
        openstaand -= aflossing
    return rentedeel
def _aflossingstabel_kapitaal(bedrag,rente,jaren):
    kapdeel=[]
    for i in range(0,jaren):
        kapi = annuiteit(bedrag,rente,jaren) - _aflossingstabel_rente(bedrag,rente,jaren)[i]
        kapdeel.append(kapi)
    return kapdeel
def  aflossingstabel_print(bedrag,rente,jaren):
    print("+------+----------+----------+----------+")
    for i in range(0,jaren):
        print(f"|{i+1:5d} |{annuiteit(bedrag,rente,jaren):9.2f} |{_aflossingstabel_rente(bedrag,rente,jaren)[i]:9.2f} |{_aflossingstabel_kapitaal(bedrag,rente,jaren)[i]:9.2f} |")
    print("+------+----------+----------+----------+")




