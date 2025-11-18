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
    berekens = [x for x in scores if x>= 0 and x <= 100]
    berekens.sort()
    berekens= berekens[1:len(berekens)-1]
    eindscore= round(sum(berekens)/len(berekens))
    return eindscore

