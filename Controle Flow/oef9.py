from xml.dom.minidom import ProcessingInstruction

print("Find all prime numbers <= n, enter n:")
n = int(input())
test = 2
aantal=0
print("The prime numbers are:")
while test<= n:
    Isprime = True
    devisor=2
    while devisor <= test/2:
        if test%devisor == 0:
            Isprime = False
            break
        devisor+=1
    if Isprime == True:
        aantal += 1
        print(f"{test:5d}",end=" ")
        if aantal % 10 ==0:
            print()
    test+=1
print("")
print(aantal,"prime(s) less than or equal to",n)