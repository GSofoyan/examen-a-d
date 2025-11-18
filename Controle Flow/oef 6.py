zin= input("Geef de zin die het toverwoord bevat.")
naam = zin[13:zin.index("en")-1]
woord= zin[zin.index("\"")+1:-2]
print("Het toverwoord van", naam, "is","\""+woord+"\". De lengte van het toverwoord is", str(len(woord)),"letters.")
