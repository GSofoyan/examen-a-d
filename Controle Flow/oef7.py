merknaam = input()
stad = input()
merknaamcheck = merknaam.lower()
stadcheck = stad.lower()
i_m = int(0)
i_s = int(0)
merknaamprint= str("")#lege string
while i_m < (len(merknaam)):# "<" want bv bij Ocala lengte = 5 maar indexen begint van 0 en gaat dus tot 4
    if i_s < len(stad) and stadcheck[i_s] == merknaamcheck[i_m]: #eerste deel is voor als we de laatste letter uit stad gevonden hebben in merknaam, maar er zijn nog letters in merknaam erachter die niet meer in stad zitten, dat we voor die letters direct jumpen naar "else"(enplus als we dit er niet bij zetten geeft het een error voor de deel erachter bij "if" want dan zal die index te groot zijn voor de woord om te checken
        merknaamprint += str(f"[{merknaam[i_m]}]")#die letter toevoegen met haken rond
        i_s += 1
        i_m += 1 #juiste letter gevonden dus next letter in stad en merk checken


    else:
        merknaamprint +=str(f"{merknaam[i_m]}")# die letter toevoegen zonder haken rond
        i_m += 1 # niet juiste letter gevonden dus zelfde letter stad checken met next van merk

merknaamprint=merknaamprint.replace("][","")
print(merknaamprint)

