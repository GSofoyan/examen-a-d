

import calendar

def print_month(jaar, maand):

    print_month_title(jaar, maand)

    print_month_body(jaar, maand)

def print_month_title(jaar, maand):
    # Haal de naam van de maand op en druk de titel
    maand_naam = calendar.month_name[maand]
    print(f"          {maand_naam}   {jaar}")
    print("-----------------------------")
    print(" Mon Tue Wed Thu Fri Sat Sun")

def print_month_body(jaar, maand):
    start_lengte=calendar.monthrange(jaar, maand)
    start= start_lengte[0]  #startdag van maand
    lengte=start_lengte[1] #dagen in maand

    i=0
    for i in range(start):
        print("    ",end="")
    for i in range(1,lengte+1):
        print(f"{i:4d}",end="")
        if (i+start)%7==0:  #als positie 7,14,21,28 is zal het springen om nieuwe lijn te starten (start is aantal dagen leeg in begin en i is calenderdag dus samen zijn de positie in de kalender)
            print()

    #hieronder was gwn omdat dodona correctie zesty was tqt skip

    start=int(start)
    lengte=int(lengte)
    restant=int(start+lengte)
    if restant<35:
        print("    "*(35-restant))
    if restant>35:
        print("    "*(42-restant))

