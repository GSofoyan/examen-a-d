def sorteer(rij):
    lengte = 1 #lengte van een sublijst
    while lengte < len(rij): # Zolang de stap kleiner is dan de lijstlengte, blijven we mergen
        for i in range(0, len(rij), 2*lengte): #moet steeds stappen van 2* lengte zetten (want vergelijkt steeds paren van sublijsten)
            middel = i + lengte
            if i + 2*lengte <= len(rij):
                einde = (i + 2 * lengte) -1 #-1 want we hebben index nodig
            else:
                einde = len(rij) -1    #als out of bounds zit gwn naar laatste element brengen

            links = rij[i:middel]
            rechts = rij[middel:einde +1] #laatste element niet meegenomen dus +1

            i1 = 0
            i2 = 0
            index_helerij = i
            while i1 < len(links) and i2 < len(rechts):
                if links[i1] <= rechts[i2]:
                    rij[index_helerij] = links[i1]
                    i1 += 1
                    index_helerij += 1
                else:
                    rij[index_helerij] = rechts[i2]
                    i2 += 1
                    index_helerij += 1

            while i1 < len(links):
                rij[index_helerij] = links[i1]
                i1 += 1
                index_helerij += 1

            while i2 < len(rechts):
                rij[index_helerij] = rechts[i2]
                i2 += 1
                index_helerij += 1

        lengte *=2 #na elke stap, dubbelt de lengte van elke sublijst
    