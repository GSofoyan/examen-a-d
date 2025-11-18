bin=input("6tallig binair getal aub")
b1=int(bin[0])*2**5 #als je 'int' er niet bij zet zal hij eerst getal bv: '0' * 2**6 doen als:  64 keer '0'dus: 0000000... doen, ipv 0*64=0

b2=int(bin[1])*2**4

b3=int(bin[2])*2**3

b4=int(bin[3])*2**2

b5=int(bin[4])*2**1

b6=int(bin[5])*2**0

dec= b1+b2+b3+b4+b5+b6
print("Het opgegeven binair getal komt overeen met",str(dec)+".")

