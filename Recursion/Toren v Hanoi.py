


def hanoi(n):
    global stappen
    stappen = 0
    return hanoiHelper(n,"A","B","C",begin= True)  #laatste argument is om door te hebben wnr je terug bent op 1ste stap om laatste lijn te printen


def hanoiHelper(n, van, via, naar, begin : bool):
    #aantalstappen = 0 NIET HIER! WANT ZAL ANDERS BIJ ELKE RECURSIE 0 WORDEB
    global stappen
    if n == 1:

        print("Schijf",n,"van",van, "naar", naar)
        stappen += 1
    else:
        hanoiHelper(n-1, van, naar, via, begin=False)
        print("Schijf", n, "van", van, "naar", naar)
        stappen += 1
        hanoiHelper(n-1, via, van, naar,begin=False )

    if begin == True:                           #up and down gegaan en nu terug op recusie 1
        print(stappen,"stappen gedaan")