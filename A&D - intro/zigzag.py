def iszigzag(lijst):
    for i in range(0,len(lijst),2):
        if i == 0: #eerst element kunnen we neiet vergelijken met i-1
            if lijst[i] < lijst[i+1]:
                return False
        elif i != len(lijst)-1:  #is niet eerste of laatste element
            if lijst[i] < lijst[i-1] or lijst[i] < lijst[i+1]:
                return False
        else:  #dan is i laatste element en kunnen we het niet met +1 vergelijken
            if lijst[i] < lijst[i-1]:
                return False
    return True

def zigzag_traag(lijst):
    lijst.sort()
    for i in range(0,len(lijst),2):
        if i != len(lijst)-1:   #is niet laatste elemet
           lijst[i],lijst[i+1] = lijst[i+1],lijst[i]

    return None

def zigzag_snel(lijst):
    for i in range(0,len(lijst),2):
        if i == 0: #eerst element kunnen we niet vergelijken met i-1
            if lijst[i] < lijst[i+1]:
                lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]

        elif i != len(lijst) - 1:  # is niet eerste of laatste element
            if lijst[i] < lijst[i-1]:
                lijst[i], lijst[i - 1] = lijst[i - 1], lijst[i]
            if lijst[i] < lijst[i+1]:
                lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]
        else:  # dan is i laatste element en kunnen we het niet met +1 vergelijken
            if lijst[i] < lijst[i - 1]:
                lijst[i], lijst[i - 1] = lijst[i - 1], lijst[i]
    return None