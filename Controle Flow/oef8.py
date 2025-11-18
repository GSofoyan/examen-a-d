doorgaan= "ja"
while doorgaan == "ja":
    wn= int(input())
    omzet=float(input())
    balanstot= float(input())
    zelfs= int(input())

    if wn<250 and (omzet<50000 or balanstot<43000) and zelfs<=25:
        print("Het bedrijf is EEN KMO")

    else:
        print("Het bedrijf is GEEN KMO")
    doorgaan= input().lower()



