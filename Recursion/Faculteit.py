def faculteit(x):
    if x == 0:
        return 1
    else:
        return x * faculteit(x-1)


testen = int(input("Hoeveel testen?"))
for i in range(testen):
    n = int(input("Welke getal testen?"))
    if n > 13:
        print("invoer te groot")
    else:
        print(faculteit(n))