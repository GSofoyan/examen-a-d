def gemeenschappelijke_karakters(s1,s2):
    gem_kar = 0
    i=0
    j=0
    for i in range(0,len(s1)):
        if i == 0 or s1[i] not in s1[0:i]: #als het een letter is die nog niet voorkwam, gaan we deze letter (deze "i") testen , s[0] zal echter altijd in vorige deel zitten dus enkel voor != s[0], we doen [0:i] want "i" wordt niet meegepakt dus in feite is het 0 tot en met i-1
            for j in range(0,len(s2)): #als dat het geval is, check i met elke letter van j
                if j ==0 or s2[j] not in s2[0:j]: #maar ook hier mag je i niet twee keer checken met zelfde letter uit s2
                    if s1[i] == s2[j]:
                        gem_kar = gem_kar + 1
    return gem_kar



