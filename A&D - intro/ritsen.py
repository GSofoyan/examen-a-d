def samenvoegen(lijst1, lijst2):
    if len(lijst1) <= len(lijst2):
        kort = lijst1
        lang = lijst2
    else:
        kort = lijst2
        lang = lijst1

    newlijst =[]

    for i in range(len(kort)):
        newlijst.append(lijst1[i])      #ipv kort[i] want dan switcht de volgorde van de lijsten mss
        newlijst.append(lijst2[i])

    return newlijst

def weven(lijst1, lijst2):
    if len(lijst1) <= len(lijst2):
        kort = lijst1
        lang = lijst2
    else:
        kort = lijst2
        lang = lijst1

    newlijst =[]
    j = 0 #gaan we later nodig hebben als i uit range is van kortste (dit niet in loop zetten anders gaat het elke keer resetten naar 0)
    for i in range(len(lang)):       #dit runnen tot korte fully in zit , daarna is index i een error voor de korte , dus onderste deel
        if i < len(kort):
            newlijst.append(lijst1[i])
            newlijst.append(lijst2[i])

        else:
            if lang == lijst1:      #voor volgorde te behouden van lijst 1 eerst
                newlijst.append(lijst1[i])

                if j < len(kort):
                    newlijst.append(lijst2[j])
                    j += 1
                else:
                    j = 0                           #als j uit range: reset
                    newlijst.append(lijst2[j])
                    j += 1


            else: #kort == lijst1
                if j < len(kort):
                    newlijst.append(lijst1[j])
                    j += 1
                else:
                    j = 0
                    newlijst.append(lijst1[j])
                    j += 1
                newlijst.append(lijst2[i])

    return newlijst

def ritsen(lijst1, lijst2):
    if len(lijst1) <= len(lijst2):
        kort = lijst1
        lang = lijst2
    else:
        kort = lijst2
        lang = lijst1

    newlijst =[]

    for i in range(len(lang)):
        if i < len(kort):
            newlijst.append(lijst1[i])
            newlijst.append(lijst2[i])

        else:
            newlijst.append(lang[i])
    return newlijst