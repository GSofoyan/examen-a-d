massa =float(input("massa: "))
lengte=float(input("lengte: "))
Bmi= massa/(lengte**2)
print(Bmi)
if Bmi<18:
    print("Ondergewicht")
elif Bmi<25:
    print("Normaal gewicht")
elif Bmi<30:
    print("Overgewicht")
elif Bmi>=30:
    print("Obesitas")

