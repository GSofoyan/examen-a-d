


def main():
    massa = float(input())
    lengte = int(input())/100 #van cm naar meter

    Bmi = massa / (lengte ** 2)
    print(f"{Bmi:.2f}")
    if Bmi < 18.5:
        print("Ondergewicht")
    elif Bmi < 25:
        print("Gezond gewicht")
    elif Bmi < 30:
        print("Overgewicht")
    else:
        print("Obesitas")
main()