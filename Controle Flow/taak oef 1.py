startkap= float(input())
rente= float(input())
jaren=int(input())
t=1
for t in range(1,jaren+1): # "+1" want doet loop bij laaste waarde niet
    print(f"Bedrag na {t} jaar: €{startkap*(1+rente)**t:.2f}.")
if rente>=0:
    print(f"Na {jaren} jaar bedraagt de winst €{(startkap*(1+rente)**jaren)-startkap:.2f}.")
else:
    print(f"Na {jaren} jaar bedraagt het verlies €{-((startkap * (1 + rente) ** jaren) - startkap):.2f}.")


