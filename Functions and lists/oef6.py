def lees_scores():
    scores =[]
    while True:    #je laat loop infinite doorgaan, de stop conditie komt in body zelf met "break"
        invoer= input()
        if invoer == "stop":
            break
        else:
            scores.append(int(invoer))
    return scores

def bereken_scores(scores : list):
    berekens =[]
    for i in range(len(scores)):
        if scores[i] >= 0 and scores[i] <= 100:
            berekens.append(scores[i])
    berekens.sort()
    berekens= berekens[1:len(berekens)-1]
    eindscore= round(sum(berekens)/len(berekens))
    return eindscore

