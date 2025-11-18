jaar_renteperc= float(input())
aantal_jaren=float(input())
leenbedrag=float(input())

maand_rente= jaar_renteperc/1200
maand= leenbedrag * maand_rente/(1-1/(1+maand_rente)**(aantal_jaren*12))
totaal= maand*12*aantal_jaren

print("The monthly payment is",int(maand))
print("The total payment is",int(totaal))
