ivest= float(input())
jaren= int(input())
rente= float(input())

i=0
naw=0
for i in range(0,jaren):
    inkomst=float(input())
    uitg= float(input())
    winst= inkomst - uitg
    naw+= winst/((1+rente)**i)
ncw=float(naw-ivest)
print(f"De netto constante waarde over {jaren} jaar is € {ncw:.2f}.")
winst = ncw-ivest
if winst>0:
    print(f"Hoera! Er wordt een winst geboekt van € {winst:.2f}!")
elif winst<0:
    print(f"Er is helaas een verlies van € {winst:.2f}.")
elif winst==0:
    print(f"Er wordt exact break-even gedraaid.")