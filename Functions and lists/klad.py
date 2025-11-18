


def gemeenschappelijke_karakters(s1,s2):
    i = 0
    j = 0
    gem=""
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j] and s1[i] not in gem:
                gem+=s1[i]

    print(len(gem))
gemeenschappelijke_karakters("hallo","kaasguyo")

Nested_list = eval(input())
flat=[]
for i in range(len(Nested_list)):
    flat+=Nested_list[i]
print(flat)

def display_average_hours(weekly_hours_table):
    averages = []

    # Stap 2: Itereer door de werknemers (rijen in de tabel)
    for i in range(len(weekly_hours_table)):
        # Bereken het gemiddelde voor de huidige werknemer
        average_hours = sum(weekly_hours_table[i]) / len(weekly_hours_table[i])
        # Voeg het werknemer-ID en gemiddelde toe aan de lijst
        averages.append([average_hours,i+1])
    averages.sort(reverse=True)#key is om aan te duiden op welke index je wilt sorteren: wij willen averages dus 2e is [1] dan sorteren op [0]
                                                                        #reverse om van hoog naar laag                        ^aangezien we 2 gegevens hebben per element
    # Print de header
    print("Employee, Average Daily Hours")
    print("---------------------------------")

    # Print elke werknemer met hun gemiddelde uren
    for i in range(len(averages)):
        print(f"Employee {averages[i][1]}\t{averages[i][0]:.2f} hours")         #employee is eerste gegeven WN-ID

display_average_hours([
    [8, 7, 8, 8, 6, 7, 9],
    [7, 7, 7, 8, 8, 8, 7],
    [6, 6, 6, 6, 6, 6, 6],
    [9, 9, 9, 9, 9, 9, 9],
    [5, 5, 5, 5, 5, 5, 5],
    [8, 7, 8, 8, 7, 8, 7],
    [7, 8, 7, 8, 7, 8, 7],
    [6, 6, 6, 6, 6, 6, 6]
]
)






