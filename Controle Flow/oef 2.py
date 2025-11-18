jaar= int(input("Jaar"))
if jaar%4==0 and jaar%100!=0 or jaar%400==0: #als het deelbaar door 4 en geen eeuwjaar maar als het eewjaar is moet het deelbaar door 400
    print("schrikkeljaar")
else:
    print("geen schrikkeljaar")