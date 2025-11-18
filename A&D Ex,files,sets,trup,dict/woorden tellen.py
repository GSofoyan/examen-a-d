def woorden_splitsen(doc):

    text = open(doc, 'r')
    clean_txt = ""
    for line in text:
        for char in line:
            if char.isalpha():
                clean_txt += char
            else:
                clean_txt += " " #als het geen letter is (dan seperator) smijten we er een space tussen om te seperaten

#nu is cleantxt gwn een string van de woorden met spatie tussen

    text.close()
    lijst= clean_txt.split() #maakt lijst door spaties te splitsen

    return lijst

def woorden_tellen(doc):
    text = open(doc, 'r')
    dictio = {}
    for line in text:
        line = line.lower() #om geen verschil tussen hoofdletters
        for char in line:
            if char in "|@#[^{}<>,;:/=~&é\"'(§!)$*¨%£?+.-_µ`":
                line = line.replace(char, " ")

        words = line.split()
        for word in words:
            if word in dictio:
                dictio[word] += 1   #als het er al inzit :add 1
            else:
                dictio[word] = 1    #maak nieuwe met waarde 1

    return dictio