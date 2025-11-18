

getal= int(input())
Isprime = True
devisor=2
while devisor <= getal/2:
    if getal%devisor == 0:
        Isprime = False
        break
    devisor+=1
if Isprime == True:
    print(f"{getal} is een priemgetal")
else:
    print(f"{getal} is geen priemgetal")

