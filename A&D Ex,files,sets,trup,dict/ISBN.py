def overzicht(lijst):
    aantal_per_region = 8* [0] #lijst volgens volgorde vb

    for code in lijst:
        o= int(code[0])+int(code[2])+int(code[4])+int(code[6])+int(code[8])+int(code[10])
        e= int(code[1])+int(code[3])+int(code[5])+int(code[7])+int(code[9])+int(code[11])

        if int(code[12]) != (10-(o+3*e) % 10 ) % 10:            #chech of het wel valid code is??
            aantal_per_region[7] += 1

        elif code[0:3] == "978" or code[0:3] == "979":   # pakt index 3 niet mee!

            if code[3] == "0" or code[3] == "1" :
                aantal_per_region[0] += 1
            elif code[3] == "2":
                aantal_per_region[1] += 1
            elif code[3] == "3":
                aantal_per_region[2] += 1
            elif code[3] == "4":
                aantal_per_region[3] += 1
            elif code[3] == "5":
                aantal_per_region[4] += 1
            elif code[3] == "7":
                aantal_per_region[5] += 1
            elif code[3] == "6" or code[3] == "8" or code[3] == "9":
                aantal_per_region[6] += 1
        else:
            aantal_per_region[7] += 1   #zijn fouten



    print("Engelstalige landen:", aantal_per_region[0])
    print("Franstalige landen:", aantal_per_region[1])
    print("Duitstalige landen:", aantal_per_region[2])
    print("Japan:", aantal_per_region[3])
    print("Russischtalige landen:", aantal_per_region[4])
    print("China:", aantal_per_region[5])
    print("Overige landen:", aantal_per_region[6])
    print("Fouten:", aantal_per_region[7])

