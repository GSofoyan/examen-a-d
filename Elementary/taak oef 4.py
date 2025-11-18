print("Ik vind voor jou de combinatie aan centjes")
print("dat overeenkomt met een bepaald bedrag.")
bedrag= int(input("Geef een bedrag tussen 0 en 100:"))
print(bedrag,"centje(s) bestaat uit:")
print(bedrag//50,"centje(s) van 50 cent")
bedrag=bedrag%50
print(bedrag//20,"centje(s) van 20 cent")
bedrag=bedrag%20
print(bedrag//10,"centje(s) van 10 cent")
bedrag=bedrag%10
print(bedrag//5,"centje(s) van 5 cent")
bedrag=bedrag%5
print(bedrag//2,"centje(s) van 2 cent")
bedrag=bedrag%2
print(bedrag//1,"centje(s)")