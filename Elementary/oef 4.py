binaire_waarde = int(input("Geef een binaire waarde (hoogstens 8 bits): "))


b0 = binaire_waarde % 10
binaire_waarde //= 10
b1 = binaire_waarde % 10
binaire_waarde //= 10
b2 = binaire_waarde % 10
binaire_waarde //= 10
b3 = binaire_waarde % 10
binaire_waarde //= 10
b4 = binaire_waarde % 10
binaire_waarde //= 10
b5 = binaire_waarde % 10
binaire_waarde //= 10
b6 = binaire_waarde % 10
binaire_waarde //= 10
b7 = binaire_waarde % 10


decimale_waarde = (
    b7 * 2**7 +
    b6 * 2**6 +
    b5 * 2**5 +
    b4 * 2**4 +
    b3 * 2**3 +
    b2 * 2**2 +
    b1 * 2**1 +
    b0 * 2**0
)
print(decimale_waarde)