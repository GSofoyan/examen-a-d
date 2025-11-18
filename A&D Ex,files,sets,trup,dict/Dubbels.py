def dubbel(lijst):
    bekeken= []
    for x in lijst:             #search kan sneller door binary!
        if x in bekeken:
            return x        #er is max 1 dus return die direct
        else:
            bekeken.append(x)
    return None

def dubbels(lijst):
   bekeken =[]
   enkel= set()
   meerder= set()
   for x in lijst:
       if x in meerder:     #als het al in meerdere zit(komt 3e keer voor), is het al uit enkel en zal line 19 crash geven als we niet skippen
           continue
       if x in bekeken:     #het is al een gepasseerd (1 keer), dus uit enkel en in meerder
           meerder.add(x)
           enkel.remove(x)
       else:
           bekeken.append(x)
           enkel.add(x)

   return enkel,meerder
